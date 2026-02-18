---
title: "The fish shell is awesome"
date: 2017-04-23
url: https://jvns.ca/blog/2017/04/23/the-fish-shell-is-awesome/
slug: the-fish-shell-is-awesome
word_count: 798
---


3 years ago, I switched from using bash or zsh to fish ([https://fishshell.com/)](https://fishshell.com/)). I like it so
much that I wanted to write a blog post about why! There are a few
fish features that mean that I’ll probably never switch back to bash.


### no configuration


First – I know that zsh+oh-my-zsh is really awesome, and you can almost certainly configure
zsh to do all everything I’m gonna describe in this post. The thing I like personally about fish is that I
don’t have to configure it! I just install it on all my computers, it
comes with a lot of awesome features out of the box, and I don’t need to
do any configuration.


My fish configuration file literally just sets some environment
variables and that’s it.


### feature 1: autosuggestions


This is the one true reason I adore fish, I don’t care about any other
feature nearly as much.


The first amazing thing that fish does is **autocompletion from my shell
history**. As I type,
it’ll automatically suggest (in light grey) a command that I ran
recently. I can press the right arrow key to accept the completion, or
keep typing to ignore it.


Here’s what that looks like in practice: (in this example I just typed
the “v” key and it guessed that I want to run the previous vim command
again)


This autocompletion is also **contextual**. If I type ‘v’ in my home
directory, it’ll just suggest `vim`, but if I cd into `work/homepage`
and type `v`, it’ll suggest the file I edited when I was in that
directory. I LOVE that it takes the directory I’m in into account and it
means that the autocompletions work so much better.


The filename autocompletions are also smarter than in bash: I can type `ls 2017`, press tab, and it’ll autocomplete to `ls outreachy-flyer-2017-May.jpg`.


### feature 2: really good syntax highlighting


When I type a command that doesn’t exist, fish highlights it in red,
like this. `python4` gets highlighted in red, and `python3` in blue,
because python3 is a real program on my system and python4 isn’t.


This is nice and it helps me all the time to see when I make typos.


### feature 3: loops that are easier to use


Did you see that for loop in that screen shot before? Yeah!


```
for i in *.yaml
  echo $i
end

```


It’s so READABLE. All the control flow statements just end with `end`,
not `done` or `fi` or `esac`.
And it actually has a usable editor for loops. I can use my arrow keys
to go up to the first line and edit something if I made a mistake.


You will also notice at this point that fish’s loops are real different
from bash loops. bash/sh syntax really does not work inside fish.


### feature 4: no more ctrl+r


This one isn’t so important but I still like it.


I search my history all the time! For example, I never remember where my
fish configuration is because it’s kind of in a weird spot. But I
remember that it’s called config.fish so I just need to search for that.


In bash to search your history, you use “ctrl+r” and then it says
“reverse-i-search” for some reason and then you find your thing. In
fish, here’s how it works

1. type `config.fish`
2. press the up arrow. `vim ~/.config/fish/config.fish` appears
3. right, that’s the file! Press enter. Done!


This is not really so different than bash’s ctrl+r but for some
reason it makes me happy that I can just press the up arrow any time to
search my history.


### fish is great! maybe try it!


some other random cool stuff about fish:

- it comes in with built in autocompletions for a lot of commands, you
don’t have to do anything special to install them
- also apparently it automatically generates completions by parsing man
pages? that’s so smart and amazing. I just learned that today!
- you can configure it from a web browser (:D :D). I don’t really
configure my fish but I think this is cool because they’re like “hey,
you don’t have to learn our configuration language to make some basic
changes, just go to this webpage!”. It’s such a different approach!
- It has a [great 1-page tutorial](https://fishshell.com/docs/current/tutorial.html#tut_why_fish) that walks you through all the basic features and the differences from other shells.


fish isn’t POSIX compliant, and that still trips me up sometimes, it’s
similar but just different enough that I sometimes get confused about
how to set environment variables. This doesn’t make me love fish any
less, though! If I ever need to run a bash script or something I just
switch to bash for a couple minutes, it takes like 1 second to type
`bash` =)
