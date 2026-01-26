---
title: "Hello Racc"
description: "When I saidHelloCupI was looking at a yacc based parser in a   language that didn't require me to handle my dirty pointers. Another   alternative to play with is Ruby which now has a yaccish parser   "
date: 2007-05-30T00:00:00
tags: ["parser generators"]
url: https://martinfowler.com/bliki/HelloRacc.html
slug: HelloRacc
word_count: 1067
---


When I said [HelloCup](https://martinfowler.com/bliki/HelloCup.html) I was looking at a yacc based parser in a
  language that didn't require me to handle my dirty pointers. Another
  alternative to play with is Ruby which now has a yaccish parser
  built in to the standard library - inevitably called [racc](http://i.loveruby.net/en/projects/racc/).


Racc has an interesting interplay between ruby and grammar
  syntax. You define the grammar with a racc file which will generate
  a parser class.


Again I'll do my simple hello world case. The input text is


```

item camera
item laser

```


I'll populate item objects inside a catalog, using the following
  model classes.


```

class Item
  attr_reader :name
  def initialize name
    @name = name
  end
end

class Catalog 
  extend Forwardable
  def initialize
    @items = []
  end
  def_delegators :@items, :size, :<<, :[] 
end

```


`Forwardable` is a handy library that allows me to
delegate methods to an instance variable. In this case I delegate a
bunch of methods to the `@items` list.


I test what I read with this.


```

class Tester < Test::Unit::TestCase
  def testReadTwo
    parser = ItemParser.new
    parser.parse "item camera\nitem laser\n"
    assert_equal 2, parser.result.size
    assert_equal 'camera', parser.result[0].name
    assert_equal 'laser', parser.result[1].name
  end
  def testReadBad
    parser = ItemParser.new
    parser.parse "xitem camera"
    fail
    rescue #expected
  end   
end

```


To build the file and run the tests I use a simple rake file.


```

# rakefile...
task :default => :test

file 'item.tab.rb' => 'item.y.rb' do
  sh 'racc item.y.rb'
end

task :test => 'item.tab.rb' do 
  require 'rake/runtest'
  Rake.run_tests 'test.rb'
end

```


The `racc` command needs to be installed on your
  system. I did it the easy way on Ubuntu with
  `apt-get`. It takes the input file and creates one named
  `inputFileName.tab.rb`.


The parser grammar class is a special format, but one that's
  pretty familiar to yaccish people. For this simple example it looks
  like this:


```

#file item.y.rb...
class ItemParser
  token 'item'  WORD
  rule
    catalog: item | item catalog;
    item: 'item' WORD {@result << Item.new(val[1])};
end

```


The tokens clause declares the token's we get from the lexer. I
  use the string `'item'` and `WORD` as a
  symbol. The rule clause starts the production rules which are in the
  usual BNF form for yacc. As you might expect I can write actions
  inside curlies. To refer to the elements of the rule I use the
  `val` array, so `val[1]` is the equivalent to
  `$2` in yacc (ruby uses 0 based array indexes, but I've
  forgiven it). Should I wish to return a value from the rule
  (equivalent to yacc's `$$`) I assign
  it to the variable `result`.


The most complicated part of using racc is to sort out the lexer.
Racc expects to call a method that yields tokens, where each token is a
two-element array with the first element being the type of token
(matching the token declaration) and the second element the value
(what shows up in `val` - usually the text). You mark the
end of the token stream with `[false, false]`. The sample
code with racc uses regular expression matching on a string. A better
choice for most cases is to use `StringScanner`, which is
in the standard ruby library.


I can use this scanner to convert a string into an array of tokens.


```

#file item.y.rb....
---- inner
def make_tokens str
  require 'strscan'
  result = []
  scanner = StringScanner.new str
  until scanner.empty?
    case
      when scanner.scan(/\s+/)
        #ignore whitespace
      when match = scanner.scan(/item/)
        result << ['item', nil]
      when match = scanner.scan(/\w+/)
        result << [:WORD, match]
      else
        raise "can't recognize  <#{scanner.peek(5)}>"
    end
  end
  result << [false, false]
  return result
end
```


To integrate the scanner into the parser, racc allows you to
place code into the generated parser class. You do this by adding code
to the grammar file. The declaration `---- inner` marks the
code to go inside the generated class (you can also put code at the
head and foot of the generated file). I'm calling a `parse`
method in my test, so I need to implement that.


```

#file item.y.rb....
---- inner
attr_accessor :result

def parse(str)
  @result = Catalog.new
  @tokens = make_tokens str
  do_parse
end

```


The `do_parse` method initiates the generated
  parser. This will call `next_token` to get at the next
  token, so we need to implement that method and include it in the
  inner section.


```

#file item.y.rb....
---- inner
def next_token
  @tokens.shift
end

```


This is enough to make racc work with the file. However as I play
  with it I find the scanner more messy than I would like. I really
  just want it to tell the lexer what patterns to match and what to
  return with them. Something like this.


```

#file item.y.rb....
---- inner
def make_lexer aString
  result = Lexer.new
  result.ignore /\s+/
  result.keyword 'item'
  result.token /\w+/, :WORD
  result.start aString
  return result
end

```


To make this work I write my own lexer wrapper over the base
  functionality provided by StringScanner. Here's the code to set up
  the lexer and and handle the above configuration.


```

class Lexer...
  require 'strscan'
  def initialize 
    @rules = []
  end
  def ignore pattern
    @rules << [pattern, :SKIP]
  end
  def token pattern, token
    @rules << [pattern, token]
  end
  def keyword aString
    @rules << [Regexp.new(aString), aString]
  end
  def start aString
    @base = StringScanner.new aString
  end

```


To perform the scan I need to use StringScanner to compare the
  rules against the input stream.


```

class Lexer...
  def next_token
    return [false, false] if @base.empty?
    t = get_token
    return (:SKIP == t[0]) ? next_token : t
  end
  def get_token
    @rules.each do |key, value|
      m = @base.scan(key)
      return [value, m] if m
    end 
    raise  "unexpected characters  <#{@base.peek(5)}>"
  end  

```


I can then alter the code in the parser to call this lexer
  instead.


```

#file item.y.rb....
---- inner
def parse(arg)
  @result = Catalog.new
  @lexer = make_lexer arg
  do_parse
end

def next_token
  @lexer.next_token
end
```


As well as giving me a better way to define the rules, this also
  allows the grammar to control the lexer because it's only grabbing
  one token at a time - this would give me a mechanism to implement
  lexical states later on.


On the whole racc is pretty easy to set up and use - providing
  you know yacc. The documentation is on the minimal side of
  sketchy. There's a simple manual on the website and some sample
  code. There's also a very helpful [presentation](http://cmills.freeshell.org/) on racc. I also
  got a few tips from our [Mingle](http://studios.thoughtworks.com/mingle-project-intelligence) team who've used it for a nifty customization language inside Mingle.
