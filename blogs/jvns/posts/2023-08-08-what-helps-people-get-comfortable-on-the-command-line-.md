---
title: "What helps people get comfortable on the command line?"
date: 2023-08-08
url: https://jvns.ca/blog/2023/08/08/what-helps-people-get-comfortable-on-the-command-line-/
slug: what-helps-people-get-comfortable-on-the-command-line-
word_count: 1760
---


Sometimes I talk to friends who need to use the command line, but are
intimidated by it. I never really feel like I have good advice (I’ve been using
the command line for too long), and so I asked some people [on Mastodon](https://social.jvns.ca/@b0rk/110842645317766338):


> if you just stopped being scared of the command line in the last year or
> three — what helped you?


> (no need to reply if you don’t remember, or if you’ve been using the command
> line comfortably for 15 years — this question isn’t for you :) )


This list is still a bit shorter than I would like, but I’m posting it in the
hopes that I can collect some more answers. There obviously isn’t one single
thing that works for everyone – different people take different paths.


I think there are three parts to getting comfortable: **reducing risks**, **motivation** and **resources**. I’ll
start with risks, then a couple of motivations and then list some resources.


### ways to reduce risk


A lot of people are (very rightfully!) concerned about accidentally doing some
destructive action on the command line that they can’t undo.


A few strategies people said helped them reduce risks:

- regular backups (one person mentioned they accidentally deleted their entire
home directory last week in a command line mishap, but it was okay because
they had a backup)
- For code, using git as much as possible
- Aliasing `rm` to a tool like [safe-rm](https://launchpad.net/safe-rm) or [rmtrash](https://github.com/PhrozenByte/rmtrash) so that you can’t accidentally delete something you shouldn’t (or just `rm -i`)
- Mostly avoid using wildcards, use tab completion instead. (my shell will tab complete `rm *.txt` and show me exactly what it’s going to remove)
- Fancy terminal prompts that tell you the current directory, machine you’re on, git branch, and whether you’re root
- Making a copy of files if you’re planning to run an untested / dangerous command on them
- Having a dedicated test machine (like a cheap old Linux computer or Raspberry Pi) for particularly dangerous testing, like testing backup software or partitioning
- Use `--dry-run` options for dangerous commands, if they’re available
- Build your own `--dry-run` options into your shell scripts


### a “killer app”


A few people mentioned a “killer command line app” that motivated them to start
spending more time on the command line. For example:

- [ripgrep](https://github.com/BurntSushi/ripgrep)
- jq
- wget / curl
- git (some folks found they preferred the git CLI to using a GUI)
- ffmpeg (for video work)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- hard drive data recovery tools (from [this great story](https://github.com/summeremacs/public/blob/main/20230629T180135--how-i-came-to-use-emacs-and-other-things__emacs_explanation_linux_origin_raspberrypi_story_terminal.org))


A couple of people also mentioned getting frustrated with GUI tools (like heavy
IDEs that use all your RAM and crash your computer) and being motivated to
replace them with much lighter weight command line tools.


### inspiring command line wizardry


One person mentioned being motivated by seeing cool stuff other people were
doing with the command line, like:

- [Command-line Tools can be 235x Faster than your Hadoop Cluster](https://adamdrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html)
- [this “command-line chainsaw” talk by Gary Bernhardt](https://www.youtube.com/watch?v=ZQnyApKysg4&feature=youtu.be)


### explain shell


Several people mentioned [explainshell](https://explainshell.com/) where you
can paste in any shell incantation and get it to break it down into different
parts.


### history, tab completion, etc:


There were lots of little tips and tricks mentioned that make it a lot easier
to work on the command line, like:

- up arrow to see the previous command
- Ctrl+R to search your bash history
- navigating inside a line with `Ctrl+w` (to delete a word), `Ctrl+a` (to go to
the beginning of the line), `Ctrl+e` (to go to the end), and `Ctrl+left arrow` / `Ctrl+right arrow` (to
jump back/forward a word)
- setting bash history to unlimited
- `cd -` to go back to the previous directory
- tab completion of filenames and command names
- learning how to use a pager like `less` to read man pages or other large text files (how to search, scroll, etc)
- backing up configuration files before editing them
- using pbcopy/pbpaste on Mac OS to copy/paste from your clipboard to stdout/stdin
- on Mac OS, you can drag a folder from the Finder into the terminal to get its path


### fzf


Lots of mentions of using [fzf](https://github.com/junegunn/fzf) as a better
way to fuzzy search shell history. Some other things people mentioned using fzf for:

- picking git branches (`git checkout  $(git for-each-ref --format='%(refname:short)' refs/heads/ | fzf)`)
- quickly finding files to edit (`nvim $(fzf)`)
- switching kubernetes contexts (`kubectl config use-context $(kubectl config get-contexts -o name | fzf --height=10 --prompt="Kubernetes Context> ")`)
- picking a specific test to run from a test suite


The general pattern here is that you use fzf to pick something (a file, a git
branch, a command line argument), fzf prints the thing you picked to stdout,
and then you insert that as the command line argument to another command.


You can also use fzf as an tool to automatically preview the output and quickly iterate, for example:

- automatically previewing jq output (`echo '' | fzf --preview "jq {q} < YOURFILE.json"`)
- or for `sed` (`echo '' | fzf --preview "sed {q} YOURFILE"`)
- or for `awk` (`echo '' | fzf --preview "awk {q} YOURFILE"`)


You get the idea.


In general folks will generally define an alias for their `fzf` incantations so
you can type `gcb` or something to quickly pick a git branch to check out.


### raspberry pi


Some people started using a Raspberry Pi, where it’s safer to experiment
without worrying about breaking your computer (you can just erase the SD card and start over!)


### a fancy shell setup


Lots of people said they got more comfortable with the command line
when they started using a more user-friendly shell setup like
[oh-my-zsh](https://ohmyz.sh/) or [fish](https://fishshell.com/). I really
agree with this one – I’ve been using fish for 10 years and I love it.


A couple of other things you can do here:

- some folks said that making their terminal prettier helped them feel more
comfortable (“make it pink!”).
- set up a fancy shell prompt to give you more information (for example you can
make the prompt red when a command fails). Specifically [transient prompts](https://www.reddit.com/r/zsh/comments/dsh1g3/new_powerlevel10k_feature_transient_prompt/)
(where you set a super fancy prompt for the current command, but a much
simpler one for past commands) seem really nice.


Some tools for theming your terminal:

- I use [base16-shell](https://github.com/chriskempson/base16-shell)
- [powerlevel10k](https://github.com/romkatv/powerlevel10k) is a popular fancy zsh theme which has transient prompts
- [starship](https://github.com/starship/starship) is a fancy prompt tool
- on a Mac, I think [iTerm2](https://iterm2.com/) is easier to customize than the default terminal


### a fancy file manager


A few people mentioned fancy terminal file managers like
[ranger](https://github.com/ranger/ranger) or
[nnn](https://github.com/jarun/nnn), which I hadn’t heard of.


### a helpful friend or coworker


Someone who can answer beginner questions and give you pointers is invaluable.


### shoulder surfing


Several mentions of watching someone more experienced using the terminal –
there are lots of little things that experienced users don’t even realize
they’re doing which you can pick up.


### aliases


Lots of people said that making their own aliases or scripts for commonly used
tasks felt like a magical “a ha!” moment, because:

- they don’t have to remember the syntax
- then they have a list of their most commonly used commands that they can summon easily


### cheat sheets to get examples


A lot of man pages don’t have examples, for example the [openssl s_client](https://linux.die.net/man/1/s_client) man page has no examples.
This makes it a lot harder to get started!


People mentioned a couple of cheat sheet tools, like:

- [tldr.sh](https://tldr.sh/)
- [cheat](https://github.com/cheat/cheat) (which has the bonus of being editable – you can add your own commands to reference later)
- [um](http://ratfactor.com/cards/um) (an incredibly minimal system that you have to build yourself)


For example the [cheat page for openssl](https://github.com/cheat/cheatsheets/blob/master/openssl) is really
great – I think it includes almost everything I’ve ever actually used openssl
for in practice (except the `-servername` option for `openssl s_client`).


One person said that they configured their `.bash_profile` to print out a cheat
sheet every time they log in.


### don’t try to memorize


A couple of people said that they needed to change their approach – instead of
trying to memorize all the commands, they realized they could just look up
commands as needed and they’d naturally memorize the ones they used the most
over time.


(I actually recently had the exact same realization about learning to read x86
assembly – I was taking a class and the instructor said “yeah, just look
everything up every time to start, eventually you’ll learn the most common
instructions by heart”)


Some people also said the opposite – that they used a spaced repetition app
like Anki to memorize commonly used commands.


### vim


One person mentioned that they started using vim on the command line to edit
files, and once they were using a terminal text editor it felt more natural to
use the command line for other things too.


Also apparently there’s a new editor called
[micro](https://micro-editor.github.io/) which is like a nicer version of
pico/nano, for folks who don’t want to learn emacs or vim.


### use Linux on the desktop


One person said that they started using Linux as their main daily driver, and
having to fix Linux issues helped them learn. That’s also how I got comfortable
with the command too back in ~2004 (I was really into installing lots of
different Linux distributions to try to find my favourite one), but my guess is
that it’s not the most popular strategy these days.


### being forced to only use the terminal


Some people said that they took a university class where the professor made
them do everything in the terminal, or that they created a rule for themselves
that they had to do all their work in the terminal for a while.


### workshops


A couple of people said that workshops like [Software Carpentry](https://software-carpentry.org/)
workshops (an introduction to the command line, git, and Python/R programming
for scientists) helped them get more comfortable with the command line.


You can see the [software carpentry curriculum here](https://software-carpentry.org/lessons/).


### books & articles


a few that were mentioned:


articles:

- [The Terminal](https://furbo.org/2014/09/03/the-terminal/)
- [command line kung fu](http://blog.commandlinekungfu.com/) (has a mix of Unix and Windows command line tips)


books:

- [effective linux at the command line](https://www.oreilly.com/library/view/efficient-linux-at/9781098113391/)
- unix power tools (which might be outdated)
- The Linux Pocket guide


videos:

- [CLI tools aren’t inherently user-hostile](https://www.youtube.com/watch?v=IcV9TVb-vF4)  by Mindy Preston
- Gary Bernhardt’s [destroy all software screencasts](https://www.destroyallsoftware.com/screencasts)
- [DistroTube](https://www.youtube.com/@DistroTube)
