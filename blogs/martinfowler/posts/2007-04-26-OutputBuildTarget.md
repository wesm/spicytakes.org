---
title: "Output Build Target"
description: "In the past few days I've been reviewing an in-progress article   by a Julian Simpson, a colleague of mine, on refactoring ant   files. Julian is one our âdeployment dudesâ who've been responsible"
date: 2007-04-26T00:00:00
tags: ["build scripting"]
url: https://martinfowler.com/bliki/OutputBuildTarget.html
slug: OutputBuildTarget
word_count: 867
---


In the past few days I've been reviewing an in-progress article
  by a Julian Simpson, a colleague of mine, on refactoring ant
  files. Julian is one our âdeployment dudesâ who've been responsible
  for applying our agile-oriented work habits to the deployment of
  systems. In doing this Julian has run into more than his fair share
  of gnarly [ant](http://ant.apache.org/) build scripts. His article is a nice description of
  some his favorite ways to clean up the mess.


One of his observations particularly intrigued me, pointing out
  that ant files tend to decompose into targets named after tasks
  (e.g. âcompileâ, âunit-testâ). These tasks often get combined into
  imperative target invocations


```

<target name="cruise" depends="clean, compile, copy-static-files, 
unit-test, publish, javadoc, tag"/>
```


This kind of style smells wrong because it's a mismatch with the
[dependency-based

computational model](https://martinfowler.com/articles/rake.html#DependencyBasedProgramming) that build files are based on. In using this
you look at each target, ask what it depends on, and put those
dependencies into the target. So here your `unit-test` task
should depend on the `compile` and
`copy-static-files` targets directly and shouldn't be
mentioned by a later target.


When faced with a peice of apparant idiocy the easy thing to do
  is make some flippant comment like âmaybe they have such a simple system
  that they can run their tests without compilingâ. But often it's
  worth delving a little deeper.


Both Julian and I have a Unix background, so we are familiar with
the [make](http://en.wikipedia.org/wiki/Make) build language. Like Ant, make uses dependency-based
programming. Both systems break down their work into targets linked
through dependency relationships. But there's a subtle difference. In
ant you give a target a name and indicate which other targets you
depend on. In make, however, you state an output file, the input files
it depends on, and how to get from one to the other.


So compiling a two file hello world (in C) in make looks something like this


```

hello : hello.o greet.o
  gcc -o hello hello.o greet.o

hello.o : hello.c 
  gcc -c hello.c

greet.o: greet.c
  gcc -c greet.c


```


The first line says that the target file `hello`
  depends on the files `hello.o` and
  `greet.o`. The second line tells you how to make the
  target from the source files (and in a real make file much of this
  is general rules so you don't have to duplicate them). We then have
  similar rules to show how to make the inputs to the top rule.


In ant (with Java) looks like this


```

<project name = "hello" default = "test">
  <target name = "compile">
    <javac 
      srcdir = "src"
      destdir = "build"
    />
  </target>
  <target name = "test" depends = "compile">
    <junit printsummary="on">
      <classpath location = "build"/>
      <test name = "Tester"/>
    </junit>
  </target>   
</project>
```


Here we say we have a test task that depends on the compile
  task, meaning that the compile task needs to be run at some point
  before we run the test task.


Both of these fragments demonstrate dependencies but this
difference in naming affects how we think about them.  I wonder how
that naming convention pulls your brain away from thinking about
dependencies and into thinking about imperative rules.


Another aspect of this is how we deal with unneccessary
  work. Builds always seem to take longer than we'd like, so we do a
  great deal to avoid doing things we don't need to do. Indeed this is
  the whole point of using dependency based programming in the first
  place. Even if a target is mentioned multiple times, it will only be
  run once.


But this desire to avoid unnecessary work also goes into running
  the targets themselves. The fundamental mechanism in make for
  avoiding work is to compare the modification times of the output and
  input files. If the output is younger than the youngest input, then it's
  clearly up to date and doesn't need to be re-made.


Ant doesn't do this, instead it relies on ant tasks doing their
  own analysis to see what needs to be run. This makes a lot of sense
  when a compiler needs to figure out which output classes need to be
  rebuilt after a change. Often, however, people  write
  targets themselves that don't do some kind of checking. With
  any target you should be sure that it won't do any significant work
  unless something could have changed; focusing on the output is a
  good way to do this.


Sometimes the output isn't obvious. What is the output of a
  unit-test task? Putting my make hat on, I'd say âsome sort of
  fileâ. You could have the test report be the result and check in the
  task that test report file was older than any of the inputs -
  although that may not be as easy as you would like. The report
  needn't even contain anything, it could be just a
  [TouchFile](https://martinfowler.com/bliki/TouchFile.html).


Are my unix-make roots going overboard here? Possibly. But I
  would suggest that you look at your build files and to consider:

- Name each target after its product (not the activity it does).
- Make sure a target does no significant work if it doesn't need
    to.
- State each target's dependencies directly, let the build
    system work out the imperative sequence to follow.
