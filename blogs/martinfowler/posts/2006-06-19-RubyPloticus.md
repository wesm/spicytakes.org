---
title: "Ruby Ploticus"
description: "In my recent post onEvaluatingRubyI mentioned that a colleague 	had put together a web app with some fancy numerical graphs. Someone 	emailed to ask how he did that. I added my short answer, ploticus,"
date: 2006-06-19T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/bliki/RubyPloticus.html
slug: RubyPloticus
word_count: 837
---


In my recent post on [EvaluatingRuby](https://martinfowler.com/bliki/EvaluatingRuby.html) I mentioned that a colleague
	had put together a web app with some fancy numerical graphs. Someone
	emailed to ask how he did that. I added my short answer, ploticus,
	to the original bliki entry, but that led to the question of how he
	interfaced ruby with ploticus?


I actually ran into a similar problem myself recently as I wanted
	to use ploticus to graph some data for a personal project. The
	solution I came up with was actually very similar, if rather less
	refined, than the one my colleague used. As a result I thought I'd
	share it.


First a caveat - this is literally something I knocked up one
	evening. It isn't intended to be robust, performant or otherwise
	enterprisey. It's just for some data I use for me, myself, and I.


A sophisticated way to drive a C library like ploticus is to bind
	directly to the C API. Ruby makes this easy, so I'm told, but it's
	too much work for me (particularly if I want to be done before
	cocktail-hour). So my approach is to build a ploticus script and
	pipe it into ploticus. Ploticus can run by taking a script from
	standard input that controls what it does, so all I have to do is
	run ploticus within ruby and pipe commands into it. Roughly like
	this:


```

  def generate script, outfile
    IO.popen("ploticus -png -o #{outfile} -stdin", 'w'){|p| p << script}
  end

```


To build up the script, I like to get objects that can work in my
	terms, and produce the necessary ploticus stuff. If you have
	anything that uses the prefabs, then putting together something is
	easy. I wanted to do clustered bar graphs, [like this](http://ploticus.sourceforge.net/gallery/students.htm), which requires
	a ploticus script.


I built what I needed in three levels. At the lowest level is
	PloticusScripter, a class that builds up ploticus script
	commands. Here it is:


```

class PloticusScripter
  def initialize
    @procs = []
  end
  def proc name
    result =  PloticusProc.new name
    yield result
    @procs << result
    return result
  end
  def script
    result = ""
    @procs.each do |p|
      result << p.script_output << "\n\n"
    end
    return result    
  end
end
class PloticusProc
  def initialize name
    @name = name
    @lines = []
  end
  def script_output
    return (["#proc " + @name] + @lines).join("\n")
  end
  def method_missing name, *args, &proc
    line = name.to_s + ": "
    line.tr!('_', '.')
    args.each {|a| line << a.to_s << " "}
    @lines << line
  end
end
```


As you see the scripter is just a list of proc commands (well
	they could be anything that responds to script_output - but I didn't
	need anything else yet). I can instantiate the scripter, call proc
	repeatedly to define my ploticus procs, then when I'm done call
	script to get the entire script for piping into ploticus.


The next level is something to build clustered bar graphs:


```

class PloticusClusterBar 
  attr_accessor :rows, :column_names
  def initialize
    @rows = []
  end
  def add_row label, data
    @rows << [label] + data
  end
  def getdata scripter
    scripter.proc("getdata") do |p|
      p.data generate_data
    end
  end
  def colors
    %w[red yellow blue green  orange]
  end
  def clusters scripter
    column_names.size.times do |i|
      scripter.proc("bars") do |p|
        p.lenfield i + 2
        p.cluster i+1 , "/", column_names.size
        p.color colors[i]
        p.hidezerobars 'yes'
        p.horizontalbars 'yes'
        p.legendlabel column_names[i]
      end    
    end
  end

  def generate_data
    result = []
    rows.each {|r| result << r.join(" ")}
    result << "\n"
    return result.join("\n")    
  end  
end

```


This allows me to build a graph with simple calls to
	`add_row` to add data rows. This makes it much more easy
	for me to build up the data for the graph.


To make a particular graph, I'll write a third class on top of
	that:


```

#produces similar to  ploticus example in ploticus/gallery/students.htm

class StudentGrapher
  def initialize
    @ps = PloticusScripter.new
    @pcb = PloticusClusterBar.new
  end
  def run
    load_data
    @pcb.getdata @ps
    areadef
    @pcb.clusters @ps    
  end
  def load_data
    @pcb.column_names = ['Exam A', 'Exam B', 'Exam C', 'Exam D']
    @pcb.add_row '01001', [44, 45, 71, 89]
    @pcb.add_row '01002', [56, 44, 54, 36]
    @pcb.add_row '01003', [46, 63, 28, 87]
    @pcb.add_row '01004', [42, 28, 39, 49]
    @pcb.add_row '01005', [52, 74, 84, 66]    
  end
  def areadef
    @ps.proc("areadef") do |p|
      p.title "Example Student Data"
      p.yrange 0, 6
      p.xrange 0, 100
      p.xaxis_stubs "inc 10"
      p.yaxis_stubs "datafield=1"
      p.rectangle 1, 1, 6, 6
    end
  end
  def generate outfile
    IO.popen("ploticus -png -o #{outfile} -stdin", 'w'){|p| p << script}
  end
  def script
    return @ps.script
  end

end


def run
  output = 'fooStudents.png'
  File.delete output if File.exists? output
  s = StudentGrapher.new
  s.run
  s.generate output
end


```


It's a very simple example, but it's a good illustration of what
	I call the [Gateway](https://martinfowler.com/eaaCatalog/gateway.html)
	pattern. The PloticusClusterBar class is the gateway with the
	perfect interface for what I want to do. I make it transform between
	that convenient interface and what the real output needs to be. The
	PloticusScripter class is another level of gateway. Even for a
	simple thing like this I find a design of composed objects like this
	a good way to go. Which may only say how my brain's got twisted over
	the years.
