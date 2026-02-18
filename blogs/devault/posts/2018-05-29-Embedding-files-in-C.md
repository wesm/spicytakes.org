---
title: "Embedding files in C programs with koio"
date: 2018-05-29
url: https://drewdevault.com/2018/05/29/Embedding-files-in-C.html
slug: Embedding-files-in-C
word_count: 333
---

Quick blog post today to introduce a new tool I wrote:
 [koio](https://git.sr.ht/~sircmpwn/koio) . This is a small tool which takes a
list of files and embeds them in a C file. A library provides an fopen shim
which checks the list of embedded files before resorting to the real filesystem.

I made this tool for  [chopsui](https://github.com/SirCmpwn/chopsui) , where I
eventually want to be able to bundle up sui markup, stylesheets, images, and so
on in a statically linked chopsui program. Many projects have small tools which
serve a similar purpose, but it was simple enough and useful enough that I chose
to make something generic so it could be used on several projects.

The usage is pretty simple. I can embed  `ko_fopen.c`  in a C file with this
command:

```
$ koio -o bundle.c ko_fopen.c://ko_fopen.c
```

I can compile and link with  `bundle.c`  and do something like this:

```
#include <koio.h>

void koio_load_assets(void);
void koio_unload_assets(void);

int main(int argc, char **argv) {
    koio_load_assets();
    FILE *src = ko_fopen("//ko_fopen.c", "r");
    int c;
    while ((c = fgetc(src)) != EOF) {
        putchar(c);
    }
    fclose(src);
    koio_unload_assets();
    return 0;
}
```

The generated  `bundle.c`  looks like this:

```
#include <koio.h>

static struct {
	const char *path;
	size_t len;
	char *data;
} files[] = {
	{
		.path = "//ko_fopen.c",
		.len = 408,
		.data =
"#define _POSIX_C_SOURCE 200809L\n#include <errno.h>\n#include <stdlib.h>\n#inc"
"lude <stdio.h>\n#include \"koio_private.h\"\n\nFILE *ko_fopen(const char *path"
", const char *mode) {\n\tstruct file_entry *entry = hashtable_get(&koio_vfs, p"
"ath);\n\tif (entry) {\n\t\tif (mode[0] != 'r' || mode[1] != '\\0') {\n\t\t\ter"
"rno = ENOTSUP;\n\t\t\treturn NULL;\n\t\t}\n\t\treturn fmemopen(entry->data, en"
"try->len, \"r\");\n\t}\n\treturn fopen(path, mode);\n}\n",
	},
};

void koio_load_assets(void) {
	ko_add_file(files[0].path, files[0].data, files[0].len);
}

void koio_unload_assets(void) {
	ko_del_file(files[0].path);
}
```

A very simple tool, but one that I hope people will find useful. It’s very
lightweight:

* 312 lines of C
* /bin/koio is ~40 KiB statically linked to musl
* libkoio.a is ~18 KiB
* Only mandatory dependencies are POSIX 2008 and a C99 compiler
* Only optional dependency is  [scdoc](https://git.sr.ht/~sircmpwn/scdoc)  for the
manual, which is similarly lightweight

Enjoy!
