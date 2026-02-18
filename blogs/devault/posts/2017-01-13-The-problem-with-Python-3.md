---
title: "The only problem with Python 3's str is that you don't grok it"
date: 2017-01-13
url: https://drewdevault.com/2017/01/13/The-problem-with-Python-3.html
slug: The-problem-with-Python-3
word_count: 757
---

I’ve found myself explaining Python 3’s str to people online more and more often
lately. There’s this ridiculous claim about that Python 3’s string handling is
broken or somehow worse than Python 2, and today I intend to put that myth to
rest.  Python 2 strings are broken, and Python 3 strings are sane. The only
problem is that you don’t grok strings.

The basic problem many people seem to have with Python 3’s strings arises when
they write code that treats bytes like a string, because that’s how it was in
Python 2. Let me make this as clear as possible:

I want you to read that, over and over again, until it sinks in. A string is
basically an array of characters (characters being Unicode codepoints), whereas
bytes is an array of bytes, aka octets, aka unsigned 8 bit integers. That’s
right - bytes is an array of unsigned 8 bit integers, or as the name would
imply, bytes.  If you  *ever*  do string operations against bytes, you are Doing
It Wrong because bytes are not strings.

It’s entirely possible that your bytes contains an  *encoded representation*  of a
string. That encoding could be ASCII, UTF-8, UTF-32, etc. These encodings are
means of representing strings as bytes, aka unsigned 8 bit integers. In order to
treat it like a string, you first must  *decode*  it. Luckily Python 3 makes this
painless:  `bytes.decode()` . This defaults to UTF-8, but you can specify any
encoding you want:  `bytes.decode('latin-1')` . If you want bytes again, use
 `str.encode()` , which again defaults to UTF-8 but accepts any encoding. If you
have a bytes that contains an encoded string, your first order of business is
decoding it.

Let’s look at some examples of why this matters in practice:

```
Python 3.6.0 (default, Dec 24 2016, 08:03:08) 
[GCC 6.2.1 20160830] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'おはようございます'
'おはようございます'
>>> 'おはようございます'[::-1]
'すまいざごうよはお'
>>> 'おはようございます'[0]
'お'
>>> 'おはようございます'[1]
'は'
```

Or in Python 2:

```
Python 2.7.13 (default, Dec 21 2016, 07:16:46) 
[GCC 6.2.1 20160830] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 'おはようございます'
'\xe3\x81\x8a\xe3\x81\xaf\xe3\x82\x88\xe3\x81\x86\xe3\x81\x94\xe3\x81\x96\xe3\x81\x84\xe3\x81\xbe\xe3\x81\x99'
>>> 'おはようございます'[::-1]
'\x99\x81\xe3\xbe\x81\xe3\x84\x81\xe3\x96\x81\xe3\x94\x81\xe3\x86\x81\xe3\x88\x82\xe3\xaf\x81\xe3\x8a\x81\xe3'
>>> print('おはようございます'[::-1])
㾁㄁㖁㔁ㆁ㈂㯁㊁ã
>>> 'おはようございます'[0]
'\xe3'
>>> 'おはようございます'[1]
'\x81'
```

For anything other than ASCII, Python 2 “strings” are broken. Python 3’s string
handling is superb. The problem with it has only ever been that you don’t
actually know how strings work. Instead of starting ignorant flamewars about it,
learn how it works.

## Actual examples people have given me

**“Python 3 can’t handle bytes as file names”**

Yes it can. Just stop treating them like strings:

```
>>>open(b'test-\xd8\x01.txt', 'w').close()
```

Note the use of bytes as the file name, not str. \xd8\x01 is unrepresentable as
UTF-8.

```
>>> [open(f, 'r').close() for f in os.listdir(b'.')]
[None]
```

Note the use of bytes as the path to os.listdir (the documentation says that if
you want bytes back as file names, pass bytes as the path. The docs are helpful
like that). Also note the lack of crashes or broken behavior.

**“Python 3’s csv module writes b’Hello’,b’World’ into CSV files”**

CSV files are “comma seperated values”. Is each value an array of unsigned 8 bit
integers? No, of course not. They’re strings. So why would you pass an array of
unsigned 8 bit integers to it?

**“Python 3 doesn’t support writing files as latin-1”**

Sure it does.

```
with open('some latin-1 file', 'rb') as f:
  text = f.read().decode('latin-1')
with open('some utf8 file', 'wb') as f:
  f.write(text.encode('utf-8'))
```

Python 2’s shitty design has broken your mindset. Unlearn it.

## Python 2 is dead, long live Python 3

Listen. It’s time you moved to Python 3. You’re missing out on a lot of really
great improvements to the language and are stuck with a lot of problems. Python
2 is really being EoL’d, and closing your eyes and covering your ears singing
“la la la” doesn’t change that. The transition is really not that difficult or
time consuming, and well worth it. Some people say only new projects should be
written in Python 3. I say that’s bollocks - all projects should be written in
Python 3 and you need to migrate,  *now* .

Python 3 is better. Much, much better. For every legitimate criticism of Python
3 I’ve seen, I’ve seen 10 that are bullshit. Come join us in the wonderful world
of sane string handling, type decorations, async/await, and more awesome
features. Every library supports it now. Let go of your biases and evaluate the
language honestly.
