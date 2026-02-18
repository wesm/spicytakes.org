---
title: "My wish-list for the next YAML"
date: 2021-07-28
url: https://drewdevault.com/2021/07/28/The-next-YAML.html
slug: The-next-YAML
word_count: 604
---

[YAML](http://yaml.org)  is both universally used, and universally reviled. It
has a lot of problems, but it also is so useful in solving specific tasks that
it’s hard to replace. Some new kids on the block (such as TOML) have
successfully taken over a  *portion*  of its market share, but it remains in force
in places where those alternatives show their weaknesses.

I think it’s clear to most that YAML is in dire need of replacement, which is
why many have tried. But many have also failed. So what are the key features of
YAML which demonstrate its strengths, and key weaknesses that could be improved
upon?

Let’s start with some things that YAML does well, which will have to be
preserved.

* **Hierarchical relationships emphasized with whitespace**. There is no better
way of representing a hierarchical data structure than by actually organizing
your information visually. Note that semantically meaningful whitespace is not
actually required — the use of tokens like { is acceptable — so
long as, by convention, hierarchies are visually apparent.
* **Defined independently of its implementation**. There should not be a
canonical implementation of the format (though a reference implementation is,
perhaps, acceptable). It should not be defined as “a config library for
$language”. Interoperability is key. It must have a specification.
* **Easily embeds documents written in other formats**. This is the chief reason
that YAML still dominates in CI configuration: the ability to trivially write
scripts directly into config file, without escaping anything or otherwise
molesting the script. 
 `tasks:
- configure: |
    jit_flags=""
    if [ "$(uname -m)" != "x86_64" ]
    then
        jit_flags=--without-jit
    fi
    ./configure \
        --prefix=/usr \
        $jit_flags
- build: |
    make
- test: |
    make check
`
* **Both machine- and human-editable**. It’s very useful for both humans and
machines to collaborate on a YAML file. For instance, humans write build
manifests for their git.sr.ht repos, and then the project hub adds steps to
download and apply patches from mailing lists before submitting them to the
build driver. For the human’s part, the ability to easily embed scripts (see
above) and write other config parameters conveniently is very helpful —
everyone hates config.json.
* **Not a programming language**. YAML entities are a problem, but we’ll talk
about that separately. In general, YAML files are not programs. They’re just
data. This is a good thing. If you want, you can use a *separate*
pre-processor, like jsonnet.

What needs to be improved upon?

* **A much simpler grammar**. No more billion laughs, please. Besides this, 90%
of YAML’s features go un-used, which increases the complexity of
implementations, not to mention their attack surface, for little reason.
* **A means of defining a schema**, which can influence the interpretation of
the input. YAML does this poorly. Consider the following YAML list: 
 `items:
- hello
- 24
- world
` Two of these are strings, and one is a number. Representing numbers and
strings plainly like this makes it easier for humans to write, though
requiring humans to write their values in a format which provides an
unambiguous type is not so inconvenient as to save this trait from the cutting
room floor. Leaving the ambiguity in place, without any redress, provides a
major source of bugs in programs that consume YAML.
* **I don’t care about JSON interoperability**. Being a superset of JSON is
mildly useful, but not so much so as to compromise any other features or
design. I’m prepared to yeet it at the first sign of code smells.

Someday I may design something like this myself, but I’m really hoping that
someone else does it instead. Good luck!
