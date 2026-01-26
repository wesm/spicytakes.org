---
title: "Using a command line script to export from OmniGraffle"
description: "A quick post on how I did the export script using   AppleScript and Ruby"
date: 2018-08-21T00:00:00
tags: ["tools"]
url: https://martinfowler.com/articles/2017-graffle-export.html
slug: 2017-graffle-export
word_count: 496
---


From time to time I draw a bunch of diagrams in OmniGraffle, and then need to
    convert them all to a format I can show in a web page. If I only have one or two, then
    doing it each time works ok. But if I have a dozen or more, then I find
    it easier to have a script. That way I can safely export them all whenever I need to.


Fortunately Omnigraffle makes this possible by providing an automation interface
    which allows me to talk to it via AppleScript. It does change over the years, and
    needed a couple of hours fiddling to get it to work this morning. So I thought I'd jot
    down my notes in case anyone else wants to do it.


Eventually there may be a better way to do this. The Omni Group is putting together a richer
    automation environment that will be [callable from
    JavaScript](https://omni-automation.com). As I write this there is no access to the export
    functionality from JavaScript, so I relied on the
    AppleScript route instead.


I'm not familiar with AppleScript, and didn't like it much when I have
    used it. So I like to keep any code in AppleScript to a minimum. I did the
    usual googling around and cobbled together a small script that exports the
    current front document. It assumes there's only one canvas in the file,
    which is true for files I'm working with.


omni2png.scptâ¦


```
  on convertGraffleFile(outputFile)
    tell application "OmniGraffle"
      export front document scope "all graphics" as "SVG" to file outputFile
      close front document
    end tell
  end convertGraffleFile
  
  on run argv
     convertGraffleFile(item 1 of argv)
  end run
```


I want to do all this to all files in a certain folder that match a certain name
    pattern. Much of this logic I want to have in a familiar language, and ruby is what I
    use for such scripting.


omni.rbâ¦


```
  module Omni
    def self.convert_file folder, name
      input = folder + (name + ".graffle")
      return unless input.exist?
      output = folder + (name + ".svg")
      return if FileUtils::uptodate?(output.to_s, [input.to_s])
      system "open #{input}"
      call_conversion(macpath(output))
    end
  
    def self.convert_rgram folder
      convert_file folder, "rgram2"
    end
  
    def self.call_conversion output
      cmd = "osascript lib/omni2png.scpt #{output}"
      result = system cmd
      puts "error processing #{output}" unless result
    end
  
    def self.convert_all_rgrams
      Pathname('catalog').children
        .select {|p| p.directory?}
        .each {|p| convert_rgram p }
    end
  
    def self.macpath arg
      return arg.expand_path.to_s.tr("/", ":")[1..-1]
    end
  end
```


This code looks at all child directories of `catalog`, for each one that
    contains a `ggram.graffle` exports into a similarly named `png`
    file. It only does it if the dates indicate that the `png` file needs to be
    rewritten.


You might find it odd that I open the file using a command line call
    (`system`) rather opening the file within the AppleScript script.
    The reason I do that is that sometimes I get irritating errors opening an
    OmniGraffle document from within AppleScript (it says there's a permission
    error, but has no trouble if I open it manually or by the command line)


---
