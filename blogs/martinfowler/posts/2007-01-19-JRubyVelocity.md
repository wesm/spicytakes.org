---
title: "JRuby Velocity"
description: "I had a need yesterday to play around with velocity in order to 	explore some stuff on templating and macros. I like velocity's 	simple template language, but this was one of those times where I 	wasn"
date: 2007-01-19T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/JRubyVelocity.html
slug: JRubyVelocity
word_count: 379
---


I had a need yesterday to play around with velocity in order to
	explore some stuff on templating and macros. I like velocity's
	simple template language, but this was one of those times where I
	wasn't using it in the context of some Java or .NET work. At that
	point working with velocity becomes a bit of a pain as you have to
	setup the context and run the processor in Java.


This kind of situation calls for a scripting language, my
	preferred scripting language is Ruby, and thus I
	thought this was a great case for trying JRuby. My conclusion is that
	it works a treat, but I'll bore you with the details.


I downloaded JRuby and unpacked it in
	`/usr/local/lib` with a symlink so I could get to it with
	`/usr/local/lib/jruby`.


I then put a simple redirecting shell into
	`/usr/local/bin`


```

JAVA_HOME=/usr/lib/jvm/java-1.5.0-sun
JRUBY_HOME=/usr/local/lib/jruby

/usr/local/lib/jruby/bin/jruby â$@â

```


I could then run JRuby.


```

$ jruby -v
ruby 1.8.5 (0) [java]

```


(Actually it took me ages to get that to work, I eventually found
the bug between the chair and the keyboard. I'm too embarrassed to tell
you what it was.)


To run velocity you have to add it to JRuby's classpath.


```

CLASSPATH=path/to/velocity-dep-1.4.jar
export CLASSPATH
jruby â$@â

```


To help run velocity I wrote a little helper class.


```

require 'java'

class VelocityLauncher
  def initialize context, template
    @context = context
    @template = template
  end

  include_class 'org.apache.velocity.app.Velocity'
  include_class 'org.apache.velocity.VelocityContext'
  include_class 'java.io.StringWriter'

  def run
    vc = VelocityContext.new(@context)
    writer = StringWriter.new
    Velocity.init
    Velocity.evaluate(vc, writer, "LOG", @template)
    return writer.getBuffer
  end
end

```


Now I can take write a little template:


```

This is an announcement from $host

Our chief weapons are:
#foreach ($w in $weapons) 
  - $w 
#end

```


To populate it, all I need is a ruby hash, which is easy to
	make.


```

ct = {'host' => 'Cardinal Fang', 
  'weapons' => ['Fear', 'Surprise', 'Ruthless Efficiency']}
template = File.readlines('template.txt').join

puts VelocityLauncher.new(ct, template).run

```


I can imagine extending this to a nice command line runner for
	velocity which would take a context file of the form:


```

host = 'Cardinal Fang'
weapons = ['Fear', 'Surprise', 'Ruthless Efficiency']

```


But I don't need that yet, so I'll do it another day (and I'm
	pretty sure what the binding for 'another day' is).
