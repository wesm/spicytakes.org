---
title: "Hello Antlr"
description: "As I explore parser generator tools for externalDomainSpecificLanguages, I've saidHelloAntlrandHelloSablecc. If you spend much time looking at parser   generators you can't really avoid looking at the"
date: 2007-05-13T00:00:00
tags: ["parser generators"]
url: https://martinfowler.com/bliki/HelloAntlr.html
slug: HelloAntlr
word_count: 1274
---


After saying [HelloSablecc](https://martinfowler.com/bliki/HelloSablecc.html) I also wanted to try out [Antlr](http://www.antlr.org/), which
	is another compiler-compiler for the Java space. As with that entry,
	this is just about getting Antlr going with a very simple âhello
	worldâ style grammar.


Like SableCC, Antlr is a compiler-compiler tool. It's been around
	for a while, and I've run into a few projects that use it. Unlike
	SableCC (and the venerable lex/yacc combo) it generates a recursive
	descent parser using LL grammars. Compiler heads like to argue about
	whether LL or LALR are better, I'll not step into that debate here.


My simple case is to parse a file of a list of items like this:


```

item camera
item laser

```


Each line has the 'item' keyword followed by a single word for
	the name of an item. I shall load each item object into a
	configuration object that keeps them all together.


```

public class Configuration {
  private Map<String, Item> items = new HashMap<String, Item>();
  public Item getItem(String key) {
    return items.get(key);
  }
  public void addItem(Item arg) {
    items.put(arg.getName(), arg);
  }
public class Item {
  private String name;
  public Item(String name) {
     this.name = name;
   }

```


Here's a test for that, using the file I showed above.


```

 @Test public void readTwoItems() {
    Reader input = null;
    try {
      input = new FileReader("catalog.txt");
    } catch (FileNotFoundException e) {
      throw new RuntimeException(e);
    }
    Configuration config = ParserCommand.parse(input);
    assertNotNull(config.getItem("camera"));
    assertNotNull(config.getItem("laser"));
    assertEquals(2, config.getItems().size());
  }

```


As before - using a compiler-compiler for this problem is silly,
	but then is printing âhello worldâ on a console. For the same reason
	as I always write âhello worldâ with a new environment, I like to
	write something dirt simple to just make sure I can get things
	working at all before I start doing anything real with it.


One hassle with using an compiler-compiler like this is that it
	makes the build process more complicated. I have to run antlr on the
	grammar file to create java classes for the parser, then include
	them in the compilation. So it's time to fight with ant again -
	here's the ant target:


```

  <property name = "dir.parser" value = "${dir.gen}/parser"/>
  <path id = "path.antlr">
    <fileset dir = "${dir.lib}">
      <include name = "antlr*.jar"/>
      <include name = "stringtemplate*.jar"/>
    </fileset>
  </path>
  <target name = "gen" >
    <mkdir dir="${dir.parser}"/>
    <java classname="org.antlr.Tool" classpathref="path.antlr" fork = "true" failonerror="true">
      <arg value="-o"/>
      <arg value="${dir.parser}"/>
      <arg value="Catalog.g"/>
     </java>
  </target>

```


This generates code into the `gen` directory. This way
	generated code is separate from source code I write myself. Another
	target does the compilation


```

 <property name = "dir.build" value = "classes/production/antlrLair"/> 
 <target name = "compile" depends = "gen">
    <mkdir dir="${dir.build}"/>
    <javac destdir="${dir.build}" classpathref="classpath">
      <src path = "src"/>
      <src path = "${dir.gen}"/>
      <src path = "test"/>
    </javac>
  </target>

```


I can then run the tests with a final target.


```

<target name = "test" depends="compile">
    <junit haltonfailure = "on">
      <formatter type="brief"/>
      <classpath refid = "classpath"/>
      <batchtest todir="${dir.build}" >
        <fileset dir = "test" includes = "**/*Test.java"/>
      </batchtest>
     </junit>
   </target>

```


Antlr works with a grammar file `Catalog.g`. The
	grammar file defines the productions in the grammar and also actions
	that the parser takes when it encounters productions. The grammar
	file also defines the lexer (you can split them if you want). In
	this sense Antlr is more traditional (and flexible) than
	SableCC. SableCC doesn't allow actions, instead you generate a parse
	tree or AST and walk that with java. Antlr allows arbitrary actions,
	or it supports building a tree in the same manner as SableCC. (Antlr
	also uses a grammar file to walk the tree.) Since I'm building up a
	simple domain model of items and a configuration I'll forgo the
	tree building and do all the work in my actions.


I'll go through this file in chunks, with descriptions as I go. I
start with a grammar heading


```
grammar Catalog;
```


Antlr supports a number of points at which you can inject code
	into the generated parser (instead of the generating a superclass
	which SableCC does.) I put package declarations and imports into the
	header.


```

@header{
package parser;
import model.*;
}
@lexer::header {
package parser;
}

```


The next code injection is to put code into the body of the
	generated class. Essentially this adds members to the class, hence
	the name of the command.


```

@members {
  public Configuration result = new Configuration();
}
```


Now I can get into the productions of the grammar. I'll do this
	top down, since it's a top-down parser. I begin by saying that the
	catalog consists of multiple `item` clauses followed by the end of the
	file.


```
catalog :  item* EOF;
```


Next I define the item clause as the literal string 'item'
	followed by a string.


```
item 	: 'item'  name=STRING 
   {result.addItem(new Item ($name.text));};

```


Here I also put in the action, which is to create a new item in
	the model with the name set to the value of the string. The code
	inside the curlies is java code which is added to the parser after
	that term is recognized. I can name elements in the production which
	I then refer to in the action. Here I've given the string the name
	'name', which makes sense in context even though it makes for an
	awkward write-up.


The last productions define the lexer elements for string and whitespace.


```

STRING 	: ('a'..'z' | 'A'..'Z')+ ;
WS : (' ' |'\t' | '\r' | '\n')+ {skip();} ;

```


The action of whitespace is to skip (ignore) it.


There are a few things that make Antlr easier to work with than
	SableCC. Antlr has a nice IDE called [AntlrWorks](http://www.antlr.org/works/) that can plug into
	IntelliJ. The tool will give you syntax highlighting and completion
	on grammar elements, plot syntax diagrams for your grammar, and
	allow you to enter test fragments to parse - displaying the
	resulting parse tree. It's a very helpful tool to see what the
	parser is doing. However there's no highlighting/completion for the
	code inside actions, which is an understandable pain.


Another good feature of Antlr is the fact that there is a [decent

book](http://www.pragmaticprogrammer.com/titles/tpantlr/index.html) on it in the works. The book gives detailed coverage of how
the tool works and useful background on language and compiler
principles. It does assume you're working on a full blown language and
that you'll be generating code - which isn't necessarily so for DSL
work. However the detail it gives looks like it will be invaluable as
I probe deeper.


Antlr's actions seem like an easier bet if you want to populate a
	model - I'm not sure how useful an intermediate parse tree or AST
	would be here. Again further investigation will give me a better
	feel. The more complex the language the more useful it is to have an
	intermediate tree representation. I like Antlr's flexibility in
	allowing you to do actions or tree building with transformations.


Inevitably I did have problems even with this simple example. My
biggest blocker was that I originally defined the catalog term as
`catalog :  item*;`, that is without the `EOF`. I
then got confused because the parser didn't indicate an error when it
got spurious input (like `xitem foo`). This wasn't helped
by inconsistencies between Antlr and AntlrWorks (the latter did show
an error and older versions of AntlrWorks would handle whitespace
differently too.)


(Another big cause of trouble was getting ant and JUnit to work.
I don't want to have to think about the amount of time I've spent over
the years trying to diagnose classpath problems, especially with the [infamous](http://cafe.elharo.com/java/errormsg/) âAnt could
not find the task or a class this task relies upon.â message.)
