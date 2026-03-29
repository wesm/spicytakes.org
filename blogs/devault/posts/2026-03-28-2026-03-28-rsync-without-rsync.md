---
title: "tar: a slop-free alternative to rsync"
date: 2026-03-28
url: https://drewdevault.com/2026/03/28/2026-03-28-rsync-without-rsync.html
slug: 2026-03-28-rsync-without-rsync
word_count: 445
---

So apparently  [rsync is slop](https://codeberg.org/small-hack/open-slopware)  now. When I heard, I wanted to drop a quick
note on my blog to give an alternative: tar. It doesn’t do everything that rsync
does, in particular identifying and skipping up-to-date files, but tar + ssh can
definitely accomodate the use case of “transmit all of these files over an SSH
connection to another host”.

Consider the following:

```
tar -cz public | ssh example.org tar -C /var/www -xz
```

This will transfer the contents of  `./public/`  to
 `example.org:/var/www/public/` , preserving file ownership and permissions and so
on, with gzip compression. This is roughly the equivalent of:

```
rsync -a public example.org:/var/www/
```

Here’s the same thing with a lightweight progress display thanks to  [pv](https://ivarch.com/programs/pv.shtml) :

```
tar -cz public | pv | ssh example.org tar -C /var/www -xz
```

I know tar is infamously difficult to remember how to use. Honestly, I kind of
feel that way about rsync, too. But, here’s a refresher on the most important
options for this use-case. To use tar, pick one of the following modes with the
command line flags:

* `-c` : create an archive
* `-x` : extract an archive

Use  `-f <filename>`  to read from or write to a file. Without this option, tar
uses stdin and stdout, which is what the pipelines above rely on. Use  `-C <path>`  to change directories before archiving or extracting files. Use  `-z`  to
compress or decompress the tarball with gzip. That’s basically everything you
need to know about tar to use it for this purpose (and for most purposes,
really).

With rsync, to control where the files end up you have to memorize some rules
about things like whether or not each path has a trailing slash. With tar, the
rules are, in my opinion, a bit easier to reason about. The paths which appear
on the command line of  `tar -c`  are the paths that  `tar -x`  will open to create
those files. So if you run this:

```
tar -c public/index.html public/index.css
```

You get a tarball which has  `public/index.html`  and  `public/index.css`  in it.

When  `tar -x`  opens this tarball, it will call
 `fopen("public/index.html", "w")` . So, whatever tar’s working directory is, it
will extract this file into  `./public/index.html` . You can change the working
directory before tar does this, on either end, by passing  `tar -C <path>` .

Of course, you could just use scp, but this fits into my brain better.

I hope that’s useful to you!

**Update** : As a fun little challenge I wrapped up this concept in a small
program that makes it easier to use:

[https://git.sr.ht/~sircmpwn/rtar](https://git.sr.ht/~sircmpwn/rtar)

Example:

```
rtar -R /var/www me@example.org public/*
```
