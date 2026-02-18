---
title: "Configuring aerc for git via email"
date: 2020-04-20
url: https://drewdevault.com/2020/04/20/Configuring-aerc-for-git.html
slug: Configuring-aerc-for-git
word_count: 393
---

I use  [aerc](https://aerc-mail.org)  as my email client (naturally — I
wrote it, after all), and I use  [git send-email](https://git-send-email.io)  to
receive patches to many of my projects. I designed aerc specifically to be
productive for this workflow, but there are a few extra things that I use in my
personal aerc configuration that I thought were worth sharing briefly. This blog
post will be boring and clerical, feel free to skip it unless it’s something
you’re interested in.

When I want to review a patch, I first tell aerc to  `:cd sources/<that project>` , then I open up the patch and give it a read. If it needs work, I’ll
use “rq” (“reply quoted”), a keybinding which is available by default, to open
my editor with the patch pre-quoted to trim down and reply with feedback inline.
If it looks good, I use the first of my custom keybindings: “ga”, short for git
am. The entry in  `~/.config/aerc/binds.conf`  is:

```
ga = :pipe -mb git am -3<Enter>
```

This pipes the entire message (-m, in case I’m viewing a message part) into  `git am -3`  (-3 uses a three-way merge, in case of conflicts), in the background
(-b). Then I’ll use C-t (ctrl-T), another keybinding which is included by
default, to open a terminal tab in that directory, where I can compile the code,
run the tests, and so on. When I’m done, I use the “gp” keybinding to push the
changes:

```
gp = :term git push<Enter>
```

This runs the command in a new terminal, so I can monitor the progress. Finally,
I like to reply to the patch, letting the contributor know their work was merged
and thanking them for the contribution. I have a keybinding for this, too:

```
rt = :reply -Tthanks<Enter>
```

My “thanks” template is at  `~/.config/aerc/templates/thanks`  and looks like
this:

```
Thanks!

{% raw %}
{{exec "{ git remote get-url --push origin;
    git reflog -2 origin/master --pretty=format:%h; }
  | xargs printf 'To %s\n   %s..%s  master -> master\n'" ""}}
{% endraw %}
```

That git command prints a summary of the most recent push to master. The result
is that my editor is pre-filled with something like this:

```
Thanks!

To git@git.sr.ht:~sircmpwn/builds.sr.ht
   7aabe74..191f4a0  master -> master
```

I occasionally append a few lines asking questions about follow-up work or
clarifying the deployment schedule for the change.
