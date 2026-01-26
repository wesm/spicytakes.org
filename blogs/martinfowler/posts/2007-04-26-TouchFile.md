---
title: "Touch File"
description: "When doing builds usingmake, you determine whether you need to   do work by comparing the modificiaton dates of the output file and   the input files. For things like compiling (a.outdepends offoo.c) "
date: 2007-04-26T00:00:00
tags: ["build scripting"]
url: https://martinfowler.com/bliki/TouchFile.html
slug: TouchFile
word_count: 499
---


When doing builds using [make](http://en.wikipedia.org/wiki/Make), you determine whether you need to
  do work by comparing the modificiaton dates of the output file and
  the input files. For things like compiling (`a.out` depends of `foo.c`)
  this works well, but sometimes the output is harder to see.


One example is running of tests - what's the output there? One
  output is a test report. The target for the test report can then
  compare the dates of the report file with the dates for the
  executable and any test data files. That way we ensure we only run
  tests when something has changed.


Most of the time the output files  contain useful information.
But for the purpose of determining whether a target needs to be run,
you actually don't care about the contents of the output file, only
its date. As a result a common idiom in make scripts is an empty file
that's only used as a time marker. I call this a âtouch fileâ because
it's usually only manipulated by the unix touch command, which just
updates the modification time of a file.


Touch files are often useful when you are trying to compare dates
  over a range of files. If your output is a whole tree of files, it
  can quicker to update a touch file than it is to navigate through
  the whole tree looking at update times.


Touch files are a common and natural idiom for make, however they
  are less common for [ant](http://ant.apache.org/). They are, however, still often useful. This
  struck me particularly in the last few days as I was examining how
  hibernate's HQL [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html) is
  implemented. At the heart of HQL is a trio of Antlr parsers, whose
  grammar is defined by three grammar files. If any of these grammar
  files changes, the parser source code needs to be regnerated.


Here's the ant source for this:


```

<target name="init.antlr" 
        depends="init" 
        description="Check ANTLR dependencies.">
  <uptodate property="antlr.isUpToDate" 
            targetfile="${dir.out.antlr-package}/.antlr_run">
    <srcfiles dir="${dir.grammar}" includes="*.g"/>
  </uptodate>
</target>

<target name="antlr" 
        depends="init.antlr" 
        unless="antlr.isUpToDate" 
        description="Generate ANTLR parsers.">
  <taskdef name="antlrtask" 
           classname="org.apache.tools.ant.taskdefs.optional.ANTLR">
    <classpath>
      <fileset dir="${dir.lib}">
        <include name="ant-antlr-*.jar"/>
        <include name="antlr-*.jar"/>
      </fileset>
    </classpath>
  </taskdef>
  <mkdir dir="${dir.out.antlr-package}" />
  <antlrtask target="${dir.grammar}/hql.g" 
             outputdirectory="${dir.out.antlr-package}" />
  <antlrtask target="${dir.grammar}/hql-sql.g" 
             outputdirectory="${dir.out.antlr-package}" />
  <antlrtask target="${dir.grammar}/sql-gen.g" 
             outputdirectory="${dir.out.antlr-package}" />
  <touch file="${dir.out.antlr-package}/.antlr_run"/>
</target>

```


Note that the `init.antlr` task sets the `antlr.isUpToDate` property
  based on a specific `.antlr_run` file. The main antlr
  task doesn't run if this property is true. At the end of the antlr
  task, it touches the `.antlr.run` file, which is empty.


Within the main build for hibernate, this is the task that's
  used. As a result the parser source files are only generated if
  needed. If you really want to force a regeneration of the files,
  there's a separate target:


```

<target name="antlr.regen" 
        depends="init,cleanantlr,antlr" 
        description="Regenerate all ANTLR generated code." />

<target name="cleanantlr" 
        depends="init" 
        description="Clean up the generated ANTLR parsers.">
  <delete dir="${dir.out.antlr-package}"/>
</target>

```


Note that this target achieves its aim by stating a dependency on
  the `cleanAntlr` task. It doesn't indicate a dependency
  on `init.antlr` as that dependency is already in the
  `antlr` task.
