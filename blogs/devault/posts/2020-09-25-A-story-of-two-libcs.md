---
title: "A tale of two libcs"
date: 2020-09-25
url: https://drewdevault.com/2020/09/25/A-story-of-two-libcs.html
slug: A-story-of-two-libcs
word_count: 1152
---

I received a bug report from Debian today, who had fed some garbage into
 [scdoc](https://git.sr.ht/~sircmpwn/scdoc) , and it gave them a SIGSEGV back.
Diving into this problem gave me a good opportunity to draw a comparison between
musl libc and glibc. Let’s start with the stack trace:

```
==26267==ERROR: AddressSanitizer: SEGV on unknown address 0x7f9925764184
(pc 0x0000004c5d4d bp 0x000000000002 sp 0x7ffe7f8574d0 T0)
==26267==The signal is caused by a READ memory access.
    0 0x4c5d4d in parse_text /scdoc/src/main.c:223:61
    1 0x4c476c in parse_document /scdoc/src/main.c
    2 0x4c3544 in main /scdoc/src/main.c:763:2
    3 0x7f99252ab0b2 in __libc_start_main
/build/glibc-YYA7BZ/glibc-2.31/csu/../csu/libc-start.c:308:16
    4 0x41b3fd in _start (/scdoc/scdoc+0x41b3fd)
```

And if we pull up that line of code, we find…

```
if (!isalnum(last) || ((p->flags & FORMAT_UNDERLINE) && !isalnum(next))) {
```

Hint: p is a valid pointer. “last” and “next” are both uint32_t. The segfault
happens in the second call to isalnum. And, the key: it can only be reproduced
on glibc, not on musl libc. If you did a double-take, you’re not alone. There’s
nothing here which could have caused a segfault.

Since it was narrowed down to glibc, I pulled up the source code and went
digging for the isalnum implementation, expecting some stupid bullshit. But
before I get into their stupid bullshit, of which I can assure you there is  *a
lot* , let’s briefly review the happy version. This is what the musl libc
 `isalnum`  implementation looks like:

```
int isalnum(int c)
{
	return isalpha(c) || isdigit(c);
}

int isalpha(int c)
{
	return ((unsigned)c|32)-'a' < 26;
}

int isdigit(int c)
{
	return (unsigned)c-'0' < 10;
}
```

As expected, for any value of  `c` , isalnum will never segfault. Because why the
fuck would isalnum segfault? Okay, now, let’s compare this to the
 [glibc implementation](https://sourceware.org/git/?p=glibc.git;a=blob;f=ctype/ctype.h;h=351495aa4feaf23993fe65afc0760615268d044e;hb=HEAD) . When opening this header, you’re greeted with the
typical GNU bullshit, but let’s trudge through and grep for isalnum.

The first result is this:

```
enum
{
  _ISupper = _ISbit (0),        /* UPPERCASE.  */
  _ISlower = _ISbit (1),        /* lowercase.  */
  // ...
  _ISalnum = _ISbit (11)        /* Alphanumeric.  */
};
```

This looks like an implementation detail, let’s move on.

```
__exctype (isalnum);
```

But what’s  `__exctype` ? Back up the file a few lines…

```
#define __exctype(name) extern int name (int) __THROW
```

Okay, apparently that’s just the prototype. Not sure why they felt the need to
write a macro for that. Next search result…

```
#if !defined __NO_CTYPE
# ifdef __isctype_f
__isctype_f (alnum)
// ...
```

Okay, this looks useful. What is  `__isctype_f` ? Back up the file now…

```
#ifndef __cplusplus
# define __isctype(c, type) \
  ((*__ctype_b_loc ())[(int) (c)] & (unsigned short int) type)
#elif defined __USE_EXTERN_INLINES
# define __isctype_f(type) \
  __extern_inline int                                                         \
  is##type (int __c) __THROW                                                  \
  {                                                                           \
    return (*__ctype_b_loc ())[(int) (__c)] & (unsigned short int) _IS##type; \
  }
#endif
```

Oh…. oh dear. It’s okay, we’ll work through this together. Let’s see,
 `__isctype_f`  is some kind of inline function… wait, this is the else branch
of  `#ifndef __cplusplus` . Dead end. Where the fuck is isalnum  *actually* 
defined? Grep again… okay… here we are?

```
#if !defined __NO_CTYPE
# ifdef __isctype_f
__isctype_f (alnum)
// ...
# elif defined __isctype
# define isalnum(c)     __isctype((c), _ISalnum) // <- this is it
```

Hey, there’s that implementation detail from earlier! Remember this?

```
enum
{
  _ISupper = _ISbit (0),        /* UPPERCASE.  */
  _ISlower = _ISbit (1),        /* lowercase.  */
  // ...
  _ISalnum = _ISbit (11)        /* Alphanumeric.  */
};
```

Let’s suss out that macro real quick:

```
# include <bits/endian.h>
# if __BYTE_ORDER == __BIG_ENDIAN
#  define _ISbit(bit)   (1 << (bit))
# else /* __BYTE_ORDER == __LITTLE_ENDIAN */
#  define _ISbit(bit)   ((bit) < 8 ? ((1 << (bit)) << 8) : ((1 << (bit)) >> 8))
# endif
```

Oh, for fuck’s sake. Whatever, let’s move on and just assume this is a magic
number. The other macro is  `__isctype` , which is similar to the  `__isctype_f`  we
were just looking at a moment ago. Let’s go look at that  `ifndef __cplusplus` 
branch again:

```
#ifndef __cplusplus
# define __isctype(c, type) \
  ((*__ctype_b_loc ())[(int) (c)] & (unsigned short int) type)
#elif defined __USE_EXTERN_INLINES
// ...
#endif
```

…

Well, at least we have a pointer dereference now, that could explain the
segfault. What’s  `__ctype_b_loc` ?

```
/* These are defined in ctype-info.c.
   The declarations here must match those in localeinfo.h.

   In the thread-specific locale model (see `uselocale' in <locale.h>)
   we cannot use global variables for these as was done in the past.
   Instead, the following accessor functions return the address of
   each variable, which is local to the current thread if multithreaded.

   These point into arrays of 384, so they can be indexed by any `unsigned
   char' value [0,255]; by EOF (-1); or by any `signed char' value
   [-128,-1).  ISO C requires that the ctype functions work for `unsigned
   char' values and for EOF; we also support negative `signed char' values
   for broken old programs.  The case conversion arrays are of `int's
   rather than `unsigned char's because tolower (EOF) must be EOF, which
   doesn't fit into an `unsigned char'.  But today more important is that
   the arrays are also used for multi-byte character sets.  */
extern const unsigned short int **__ctype_b_loc (void)
     __THROW __attribute__ ((__const__));
extern const __int32_t **__ctype_tolower_loc (void)
     __THROW __attribute__ ((__const__));
extern const __int32_t **__ctype_toupper_loc (void)
     __THROW __attribute__ ((__const__));
```

That is just so, super cool of you, glibc. I just  *love*  dealing with locales.
Anyway, my segfaulted process is sitting in gdb, and equipped with all of this
information I wrote the following monstrosity:

```
(gdb) print ((unsigned int **(*)(void))__ctype_b_loc)()[next]
Cannot access memory at address 0x11dfa68
```

Segfault found. Reading that comment again, we see “ISO C requires that the
ctype functions work for ‘unsigned char’ values and for EOF”. If we
cross-reference that with the specification:

> In all cases [of functions defined by ctype.h,] the argument is an int, the
> value of which shall be representable as an unsigned char or shall equal the
> value of the macro EOF.

So the fix is obvious at this point. Okay, fine, my bad. My code is wrong. I
apparently cannot just hand a UCS-32 codepoint to isalnum and expect it to tell
me if it’s between 0x30-0x39, 0x41-0x5A, or 0x61-0x7A.

But, I’m going to go out on a limb here: maybe isalnum should never cause a
program to segfault no matter what input you give it. Maybe because the spec
says you  *can*  does not mean you  *should* . Maybe, just maybe, the behavior of
this function should not depend on five macros, whether or not you’re using a
C++ compiler, the endianness of your machine, a look-up table, thread-local
storage, and two pointer dereferences.

Here’s the musl version as a quick reminder:

```
int isalnum(int c)
{
	return isalpha(c) || isdigit(c);
}

int isalpha(int c)
{
	return ((unsigned)c|32)-'a' < 26;
}

int isdigit(int c)
{
	return (unsigned)c-'0' < 10;
}
```

Bye!
