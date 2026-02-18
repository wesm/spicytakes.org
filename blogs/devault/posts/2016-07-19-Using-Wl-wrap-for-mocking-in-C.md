---
title: "Using -Wl,--wrap for mocking in C"
date: 2016-07-19
url: https://drewdevault.com/2016/07/19/Using-Wl-wrap-for-mocking-in-C.html
slug: Using-Wl-wrap-for-mocking-in-C
word_count: 456
---

One of the comforts I’ve grown used to in higher level languages when testing
my code is mocking. The idea is that in order to test some code in isolation,
you should “mock” the behavior of things it depends on. Let’s see a (contrived)
example:

```
int read_to_end(FILE *f, char *buf) {
    int r = 0, l;
    while (!feof(f)) {
        l = fread(buf, 1, 256, f);
        r += l;
        buf += l;
    }
    return r;
}
```

If we want to test this function without mocking, we would need to actually open
a specially crafted file and provide a  `FILE*`  to the function. However, with
the linker  `--wrap`  flag, we can define a wrapper function. Using  `-Wl,[flag]` 
in your C compiler command line will pass  `[flag]`  to the linker. Gold (GNU) and
lld (LLVM) both support the wrap flag, which specifies a function to be
“wrapped”. If I use  `-Wl,--wrap=fread` , then the code above will be compiled
like so:

```
int read_to_end(FILE *f, char *buf) {
    int r = 0, l;
    while (!feof(f)) {
        l = __wrap_fread(buf, 1, 256, f);
        r += l;
        buf += l;
    }
    return r;
}
```

And if I add  `-Wl,--wrap=feof`  we’ll get this:

```
int read_to_end(FILE *f, char *buf) {
    int r = 0, l;
    while (!__wrap_feof(f)) {
        l = __wrap_fread(buf, 1, 256, f);
        r += l;
        buf += l;
    }
    return r;
}
```

Now, we can define some functions that do the behavior we need to test instead
of invoking fread directly:

```
int feof_return_value = 0;

int __wrap_feof(FILE *f) {
    assert(f == (FILE *)0x1234);
    return feof_return_value;
}

void test_read_to_end_eof() {
    // ...
    feof_return_value = 1;
    read_to_end((FILE *)0x1234, buf);
    // ...
}
```

Using  `--wrap`  also conveniently defines  `__real_feof`  and  `__real_fread`  if we
need them.

Unfortunately, you can’t have two different wrappers for the same function in
an executable. This could lead to having to write several executables for each,
or making your wrapper function smart enough to have several configurable
outcomes.

Eventually I intend to write my own test framework for C, which will use
wrappers to support mocking. I want wrappers to be done automatically and have
it behave something like this:

```
static int fake_fread(void *ptr, size_t size,
        size_t nmemb, FILE *stream) {
    const char *hello = "Hello world!";
    memcpy(ptr, hello, strlen(hello) + 1);
    return strlen(hello) + 1;
}

void test_read_to_end() {
    FILE *test = (FILE *)0x1234;
    char *buffer = char[1024];

    mock_t *mock_feof = configure_mock(feof, "p");
    mock_feof->call(0)->returns(0);
    mock_feof->returns(1);

    // pzzp is pointer, size_t, size_t, pointer
    // Tells us what the fread arguments look like
    mock_t *mock_fread = configure_mock(fread, "pzzp");
    mock_fread->exec(fake_fread);

    read_to_end(test, buffer);

    assert(mock_feof->call_count == 2);
    assert((FILE*)mock_feof->call(0)->args(0) == test);

    assert(mock_fread->call_count == 1);
    assert((FILE*)mock_fread->call(0)->args(0) == buffer);
    assert((FILE*)mock_fread->call(0)->args(3) == test);

    assert(strcmp(buffer, "Hello world!") == 0);
}
```
