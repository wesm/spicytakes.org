---
title: "Flexible Antlr Generation"
description: "I've been exploring various alternative languages and grammars 	for external DSLs. One of my main tools for this isAntlr. With this 	kind of exploration I have a project with multiple similar grammar "
date: 2007-04-17T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/FlexibleAntlrGeneration.html
slug: FlexibleAntlrGeneration
word_count: 899
---


I've been exploring various alternative languages and grammars
	for external DSLs. One of my main tools for this is [Antlr](HelloAntlr.html). With this
	kind of exploration I have a project with multiple similar grammar
	files where I want to run essentially the same thing with different
	grammars. Although I only have a few grammar files at the moment, I
	could well end up with a couple of dozen.


Using these in my build is currently rather awkward. Up to now,
	I've had explicit calls to Antlr to build each grammar file. The
	file gets done whether or not it's changed recently, which slows the
	whole build down. What I'd like is a way to automatically figure out
	where the grammar files are to build, and build them if necessary.


I keep the grammar files in directories like `src/parser1/Catalog.g,
	src/parser2/Catalog.g` and I want to generate them to `gen/parser1,
	gen/parser2`. That way I can keep the generated
	`gen` directory out of source control (as it should
	be). Some directories have a regular grammar file (always called
	Catalog.g) only, others also have a tree walker grammar (called
	CatalogWalker.g) if I do tree building and walking.


It may be possible to get ant to do this, but my ant is rusty and
	frankly I'm happy to keep it that way. My usual build process these
	days is to use Rake, but it has an issue here - calling Antlr
	multiple times would lead to multiple JVM invocations which can be
	slow due to the start-up time of the JVM. After toying with some
	alternatives I thought that it would be worth giving JRuby a spin.


Ruby makes it easy to find and select out the directories that
	match my naming conventions


```

Dir['src/parser*'].
  select{|f| f =~ %r[src/parser\d+]}.
  collect{|f| Antlr.new(f)}.
  each {|g| g.run}

```


The regular expressions used for File globs (as in
	`src/parser*` isn't quite enough for my naming
	convention, so I have to filter the results with a more precise
	regexp. Once I have my real directories I create a command object to
	process them.


As I was working on this, I decided that I wanted to be able to
	run the script both with regular ruby (calling Antlr via the command
	line) and JRuby (calling the Antlr command facade directly). That
	way I could run the script on machines that didn't have JRuby
	installed. Doing so is pretty easy, I just have to keep the JRuby
	bits isolated.


The `Antlr` class does all the figuring out of what
	needs to be done and delegates to an internal engine to actually
	call Antlr in the two different styles. I initialize the object with
the directory to process, and it figures out the right target
directory and whether it needs to generate a walker.


```
class Antlr...
  def initialize dir
    @dir = dir
    @grammarFile = File.join @dir, 'Catalog.g'
    raise âNo Grammar file in #{dir}â unless File.exists? @grammarFile
    walker_name = File.join @dir, 'CatalogWalker.g'
    @walker = File.exists?(walker_name) ? walker_name : nil
    @dest = @dir.sub %r[src/], 'gen/'
  end

```


When I run the object it checks to see if it needs to run before
	invoking the engine.


```

class Antlr...
  def run
    return if current?
    puts "%s => %s " % [@grammarFile, @dest]
    mkdir_p @dest 
    run_tool    
    self
  end
  def current?
    return false unless File.exists? @dest
    output = File.join(@dest,'CatalogParser.java')
    sources = [@grammarFile]
    sources << @walker if @walker
    return uptodate?(output, sources)
  end
```


The `run_tool` method takes the data out of fields and
	puts it onto command line arguments for Antlr (I'll call the facade
	with a string array of arguments too.)


```

class Antlr...
  def run_tool
    args = []
    args << '-o' << @dest 
    args << "-lib" << @dest if @walker
    args << @grammarFile
    args << @walker if @walker
    @@engine.run_tool args
  end
```


For the engine I have two implementations. The simplest just
	makes a command line call.


```

class AntlrCommandLine
  def run_tool args
    classpath = Dir['lib/*.jar'].join(File::PATH_SEPARATOR)
    system âjava -cp #{classpath} org.antlr.Tool #{args.join ' '}â
  end
end

```


The JRuby version is a bit more involved as it has to import the
	Antlr facade file and sort out classpaths.


```

class AntlrJruby
  def initialize 
    require 'java'
    Dir['lib/*.jar'].each{|j| require j}
    include_class 'org.antlr.Tool'
  end
  def run_tool args
    Tool.new(args.to_java(:string)).process
  end
end

```


With all the time I've spent tearing my hair out with classpaths
	I just love the fact that I can just require a jar at runtime
	here. Especially since the code `Dir['lib/*.jar'].each{|j|
	require j}` loads all the jars in a directory - which is
	something that java makes horribly hard.


The last trick is ensuring that the right engine is used for the
	job. I do this with some inline code inside the Antlr command
	class.


```

class Antlr...
  tool_class = (RUBY_PLATFORM =~ /java/) ? AntlrJruby : AntlrCommandLine
  @@engine = tool_class.new

```


Pretty simple and sweet that it runs in regular ruby or JRuby.


But there's a punch line and joke's on me. I set all this up to
	use JRuby because I was afraid that the start up time of the JVMs
	would make running it from C ruby too slow. But the the C ruby
	actually does a clean build faster than the JRuby version. Maybe
	this will change once I get more grammar files to build, but for the
	moment it looks like I've fallen victim to premature
	optimization. (And it's not worthwhile for me to figure out why,
	both builds are fast enough for now.)
