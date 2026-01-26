---
title: "Hello Sablecc"
description: "As I explore parser generator tools for externalDomainSpecificLanguages, I've saidHelloAntlrandHelloSablecc. If you spend much time looking at parser   generators you can't really avoid looking at the"
date: 2007-05-13T00:00:00
tags: ["parser generators"]
url: https://martinfowler.com/bliki/HelloSablecc.html
slug: HelloSablecc
word_count: 1493
---


I've done a small amount of playing around with SableCC
	recently. It took a bit of effort to get a âHello Worldâ style
	parser going, so I thought I'd put some notes here as to what I did
	to get it working. I'm not saying this is the best way to do it, but
	it may be useful if you're looking to play with it.


SableCC is a compiler-compiler tool for the Java environment. It
	handles LALR(1) grammars (for those who remember their grammar
	categories). In other words it's a bottom up parser (unlike JavaCC
	and Antlr which are top-down).


Like with most compiler-compiler tools, you define a grammar for
	your language in a grammar file and run the compiler-compiler to
	generate a parser for this language. Since this is a hello-world
	example my language is a bare minimum one just to get the
	compiler-compiler going. The language just is a list of items like
	this:


```

item camera
item laser

```


Where 'item' is a keyword and the second word is a name. I want
	the parser to turn this into an instance of a Configuration class
	which contains a list of items.


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


The input I showed earlier should be read in to pass the following
	test.


```

    @Test public void itemsAddedToItemList() {
      Reader input = null;
      try {
        input = new FileReader("rules.txt");
      } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
      }
      Configuration config = CatalogParser.parse(input);
      assertNotNull(config.getItem("camera"));
      assertNotNull(config.getItem("laser"));
    }

```


Of course using a compiler-compiler for this is total overkill
	for this kind of case, but the point of a hello-world example is to
	get the environment working on a simple case so you can move
	onto the interesting cases with the basics working. Whenever I play
	with a new technology I always like to get something like this going
	first, before I delve into the interesting aspects.


Using a compiler-compiler makes the build process a bit more
	involved. You have to first run the compiler-compiler on the
	grammar file to generate the parser, then compile both your custom
	code and the generated parser to create the overall program, then run
	(and test it). So at this point I can't get away with just doing
	everything inside my IntelliJ and actually have to put together an
	ant file. It was a while since I'd put together an ant file and so
	it took me a bit to re-remember how to use ant language. To run
	SableCC I used the Java task:


```

   <property name = "gendir" value = "gen"/>
   <target name = "gen" >
      <mkdir dir="${gendir}"/>
      <java jar = "lib/sablecc.jar" fork = "true" failonerror="true">
         <arg value = "-d"/>
         <arg value = "${gendir}"/>
         <arg value = "catalog.sable"/>
      </java>
    </target>

```


I generate the code into the `gen` directory, to keep
it separate from the code I write myself in the `src` and
`test` directories. I then compile it all together with a
javac task.


```

 <property name = "builddir" value = "classes/production/sable"/>
  <path id="classpath">
       <fileset dir = "lib">
           <include name = "*.jar"/>
       </fileset>
       <pathelement path = "${builddir}"/>
  </path>
  <target name = "compile" depends = "gen, copyDats">
    <mkdir dir="${builddir}"/>
    <javac destdir="${builddir}" classpathref="classpath">
      <src path = "src"/>
      <src path = "${gendir}"/>
      <src path = "test"/>
    </javac>
  </target>

```


As well as compiling, I also have to move two data files for the
	parser into the build directory. The data contains the tables used
	for the parser and lexer. The build directory is nested in the way I
	have it so it will work nicely with IntelliJ. (I really ought to
	separate the tests into a separate output directory too, but I was
	feeling lazy.)


```

  <target name = "copyDats">
      <mkdir dir="${builddir}"/>
      <copy todir = "${builddir}">
        <fileset dir = "${gendir}" includes = "**/lexer.dat"/>
        <fileset dir = "${gendir}" includes = "**/parser.dat"/>
      </copy>
    </target>

```


I then have a test task to run the tests.


```

  <target name = "test" depends="compile">
     <junit haltonfailure = "on">
      <formatter type="brief"/>
      <classpath refid = "classpath"/>
      <batchtest todir="${builddir}" >
        <fileset dir = "test" includes = "**/*Tester.java"/>
      </batchtest>
     </junit>
   </target>

```


To get the parser up and going I need to define the grammar for
	my simple language using SableCC's grammar syntax.


```

Package catalogParser;

Tokens
  itemdef = 'item';
  string = ['a' .. 'z'] +;
  blank = (' ' | 13 | 10)+;
  
Ignored Tokens
    blank;

Productions
  configuration =
    item *
  ;
  item = 
    itemdef string
  ;

```


Like most compiler-compilers, SableCC splits the work into a
lexer and a parser. The lexer reads in characters and chunks them into
tokens as defined by the `Tokens` section of the grammar
file. In this case it's really simple: strings are lower case letters,
the keyword `item` is its own token. I also define what is
blank whitespace and tell the lexer to throw it away in the
`Ignores` clause.


The lexer will then feed a stream of `itemdef` and `string` tokens to
	the parser. The parser uses two productions to deal with this. It
	describes a configuration as multiple items, and each item as an
	itemdef and a string (for its name).


This defines the grammar for my input, but doesn't say how to get
	from the input to my configuration and item objects. In order to do
	this I need to write some code to map between what I've parsed and
	the objects I want to create. In most compiler-compilers I do this
	by embedding actions into the grammar. SableCC, however, works
	another way. It automatically creates a parse tree and then gives me
	a visitor to walk this parse tree. I can then subclass the visitor
	to do interesting things. In this case, as I walk the parse tree, I
	take each item node on the parse tree and turn it into the real
	items in my model.


```

public class CatalogParser extends DepthFirstAdapter {
  private Configuration result;
  public void outAItem(AItem itemNode) {
    System.out.println("found item");
    result.addItem(new Item(itemNode.getString().toString().trim()));
  }

```


The parse tree uses naming conventions to bind the grammar to the
	objects created in the tree. So the grammar creates nodes called
	`AItem` to match the item production in the grammar. The method
	`outAItem` is called as the visitor leaves the item node and allows me
	to access whatever is on the item, in this case the underlying
	string token. I can then create the item in my model using that
	string as the name.


The last bit of code is that to run the parser on the file, which
	I do by making the catalog parser a command object.


```

  public static Configuration parse(Reader input) {
    Configuration result = new Configuration();
    new CatalogParser(input, result).run();
    return result;
  }
  public CatalogParser(Reader input, Configuration result) {
    this.input = input;
    this.result = result;
  }
  public void run() {
    try {
      createParser(input).parse().apply(this);
    } catch (Exception e) {
      throw new RuntimeException(e);
     }
  }
  private Parser createParser(Reader input) {
    return new Parser(new Lexer(new PushbackReader(input)));
  }

```


So that's the basics of getting it going. So far I haven't
	started to delve further, so my thoughts about SableCC are somewhat
	preliminary, but then the whole point of this blog is to write
	half-formed thoughts.


SableCC is a bit awkward to use. There's little documentation,
	other than the author's thesis. Fortunately the thesis is much more
	understandable than many others I've come across so I was able to
	figure out how to get things going. During my work I made a mistake
	in the grammar and found it tricky to get diagnostics. The error
	messages weren't too informative and I resorted to debuggers and
	print statements inside the generated parser code. Fortunately the
	problem was in the tokenizing, so I realized my boo-boo by looking
	at the output from the lexer. LALR parsers are notoriously hard to
	follow, so I'm glad I didn't have to delve in there. Antlr scores
	rather better on this front. Recursive descent parsers are easier to
	follow and there is an [Antlr book](http://www.pragmaticprogrammer.com/titles/tpantlr/index.html) in the works which should help me
	a lot as I explore that.


So far I'm not convinced by the approach of removing parser
	actions and automatically generating a parse tree. Since it's a
	parse tree, you have to walk it to do anything useful. Nat Pryce let
	me know about [tree transformation rules](http://nat.truemesh.com/archives/000531.html) in the latest SableCC, which
	look more useful since it defines an abstract syntax tree rather
	than a parse tree. You still have to walk it to create objects in
	the domain model, but it's easier to walk. (The latest version of
	Antlr has similar features.) One plus in tree walking is that
	if I'm making changes to the tree walker I don't need to re-generate
	- which keeps me in IntelliJ. However Antlr, has AntlrWorks which
	  plugs into IntelliJ and looks very nice.
