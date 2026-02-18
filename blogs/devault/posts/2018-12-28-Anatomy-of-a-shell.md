---
title: "Anatomy of a shell"
date: 2018-12-28
url: https://drewdevault.com/2018/12/28/Anatomy-of-a-shell.html
slug: Anatomy-of-a-shell
word_count: 680
---

I’ve been contributing where I can to Simon Ser’s  [mrsh](https://git.sr.ht/~emersion/mrsh)  project, a
work-in-progress strictly POSIX shell implementation. I worked on some small
mrsh features during my holiday travels and it’s in the forefront of my mind, so
I’d like to share some of its design details with you.

There are two main components to a shell: parsing and execution. mrsh uses a
simple  [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser)  to generate an AST (Abstract Syntax
Tree, or an in-memory model of the structure of the parsed source). This design
was chosen to simplify the code and avoid dependencies like flex/bison, and is a
good choice given that performance isn’t critical for parsing shell scripts.
Here’s an example of the input source and output AST:

```
#!/bin/sh
say_hello() {
	echo "hello $1!"
}

who=$(whoami)
say_hello "$who"
```

This script is parsed into this AST (this is the output of  `mrsh -n test.sh` ):

```
program
program
└─command_list ─ pipeline
  └─function_definition say_hello ─ brace_group
    └─command_list ─ pipeline
      └─simple_command
        ├─name ─ word_string [3:2 → 3:6] echo
        └─argument 1 ─ word_list (quoted)
          ├─word_string [3:8 → 3:14] hello
          ├─word_parameter
          │ └─name 1
          └─word_string [3:16 → 3:17] !
program
program
└─command_list ─ pipeline
  └─simple_command
    └─assignment
      ├─name who
      └─value ─ word_command ─ program
        └─command_list ─ pipeline
          └─simple_command
            └─name ─ word_string [6:7 → 6:13] whoami
program
└─command_list ─ pipeline
  └─simple_command
    ├─name ─ word_string [7:1 → 7:10] say_hello
    └─argument 1 ─ word_list (quoted)
      └─word_parameter
        └─name who
```

Most of these names come directly from the  [POSIX shell specification](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) .
The parser and AST is made available as a standalone public interface of
libmrsh, which can be used for a variety of use-cases like syntax-aware text
editors, syntax highlighting (see  [`highlight.c`](https://git.sr.ht/~emersion/mrsh/tree/master/highlight.c) ), linters, etc. The most
important use-case is, of course, task planning and execution.

Most of these AST nodes becomes a  *task* . A task defines an implementation of
the following interface:

```
struct task_interface {
	/**
	 * Request a status update from the task. This starts or continues it.
	 * `poll` must return without blocking with the current task's status:
	 *
	 * - TASK_STATUS_WAIT in case the task is pending
	 * - TASK_STATUS_ERROR in case a fatal error occured
	 * - A positive (or null) code in case the task finished
	 *
	 * `poll` will be called over and over until the task goes out of the
	 * TASK_STATUS_WAIT state. Once the task is no longer in progress, the
	 * returned state is cached and `poll` won't be called anymore.
	 */
	int (*poll)(struct task *task, struct context *ctx);
	void (*destroy)(struct task *task);
};
```

Most of the time the task will just do its thing. Many tasks will have sub-tasks
as well, such as a command list executing a list of commands, or each branch of
an if statement, which it can defer to with  `task_poll` . Many tasks will wait on
an external process, in which case it can return TASK_STATUS_WAIT to have the
process  `wait` ed on. Feel free to browse the  [full list of tasks](https://git.sr.ht/~emersion/mrsh/tree/master/shell/task)  to get
an idea.

One concern more specific to POSIX shells is built-in commands. Some commands
have to be built-in because they manipulate the shell’s state, such as  `.`  and
 `cd` . Others, like  `true`  &  `false` , are there for performance reasons, since
they’re simple and easily implemented internally. POSIX specifies  [a list of
special builtins](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_14)  which are necessary to implement in the shell
itself. There’s  [a second list](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_01_01)  that must be present for the shell
environment to be considered POSIX compatible (plus some reserved names like
 `local`  and  `pushd`  that invoke undefined behavior - mrsh aborts on these).

Here are some links to more interesting parts of the code so you can explore on
your own:

* [Redirection](https://git.sr.ht/~emersion/mrsh/tree/master/shell/redir.c)  &  [pipelines](https://git.sr.ht/~emersion/mrsh/tree/master/shell/task/pipeline.c)
* [Function definition](https://git.sr.ht/~emersion/mrsh/tree/master/shell/task/function_definition.c)  &  [execution](https://git.sr.ht/~emersion/mrsh/tree/master/shell/task/command_function.c)
* [The . builtin](https://git.sr.ht/~emersion/mrsh/tree/master/builtin/dot.c)
* [main.c and the REPL](https://git.sr.ht/~emersion/mrsh/tree/master/main.c)

I might write more articles in the future diving into specific concepts, feel
free to shoot me an email if you have suggestions. Shoutout to Simon for
building such a cool project! I’m looking forward to contributing more until we
have a really nice strictly POSIX shell.
