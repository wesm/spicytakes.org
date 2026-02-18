---
title: "Popular git config options"
date: 2024-02-16
url: https://jvns.ca/blog/2024/02/16/popular-git-config-options/
slug: popular-git-config-options
word_count: 2332
---


Hello! I always wish that command line tools came with data about how popular their various options are, like:

- “basically nobody uses this one”
- “80% of people use this, probably take a look”
- “this one has 6 possible values but people only really use these 2 in practice”


So I [asked about people’s favourite git config options on Mastodon](https://social.jvns.ca/@b0rk/111885363143321068):


> what are your favourite git config options to set? Right now I only really
> have `git config push.autosetupremote true` and `git config init.defaultBranch main` set in my `~/.gitconfig`, curious about what other
> people set


As usual I got a TON of great answers and learned about a bunch of very popular
git config options that I’d never heard of.


I’m going to list the options, starting with (very roughly) the most popular
ones. Here’s a table of contents:

- pull.ff only or pull.rebase true
- merge.conflictstyle zdiff3
- rebase.autosquash true
- rebase.autostash true
- push.default simple, push.default current
- init.defaultBranch main
- commit.verbose true
- rerere.enabled true
- help.autocorrect 10
- core.pager delta
- diff.algorithm histogram
- core.excludesfile ~/.gitignore
- includeIf: separate git configs for personal and work
- fsckobjects: avoid data corruption
- submodule stuff
- and more
- how to set these
- config changes I’ve made after writing this post


All of the options are documented in `man git-config`, or [this page](https://git-scm.com/docs/git-config).


### `pull.ff only` or `pull.rebase true`


These two were the most popular. These both have similar goals: to avoid accidentally creating a merge commit
when you run `git pull` on a branch where the upstream branch has diverged.

- `pull.rebase true` is the equivalent of running `git pull --rebase` every time you `git pull`
- `pull.ff only` is the equivalent of running `git pull --ff-only` every time you `git pull`


I’m pretty sure it doesn’t make sense to set both of them at once, since `--ff-only`
overrides `--rebase`.


Personally I don’t use either of these since I prefer to decide how to handle
that situation every time, and now git’s default behaviour when your branch has
diverged from the upstream is to just throw an error and ask you what to do
(very similar to what `git pull --ff-only` does).


### `merge.conflictstyle zdiff3`


Next: making merge conflicts more readable! `merge.conflictstyle zdiff3` and `merge.conflictstyle diff3` were both super popular (“totally indispensable”).


The main idea is
The consensus seemed to be “diff3 is great, and zdiff3 (which is newer) is even better!”.


So what’s the deal with `diff3`. Well, by default in git, merge conflicts look like this:


```
<<<<<<< HEAD
def parse(input):
    return input.split("\n")
=======
def parse(text):
    return text.split("\n\n")
>>>>>>> somebranch

```


I’m supposed to decide whether `input.split("\n")` or `text.split("\n\n")` is
better. But how? What if I don’t remember whether `\n` or `\n\n` is right? Enter diff3!


Here’s what the same merge conflict look like with `merge.conflictstyle diff3` set:


```
<<<<<<< HEAD
def parse(input):
    return input.split("\n")
||||||| b9447fc
def parse(input):
    return input.split("\n\n")
=======
def parse(text):
    return text.split("\n\n")
>>>>>>> somebranch

```


This has **extra information**: now the original version of the code is in the middle! So we can see that:

- one side changed `\n\n` to `\n`
- the other side renamed `input` to `text`


So presumably the correct merge conflict resolution is `return text.split("\n")`, since that combines the changes from both sides.


I haven’t used zdiff3, but a lot of people seem to think it’s better. The blog post [Better Git Conflicts with zdiff3](https://ductile.systems/zdiff3/) talks more about it.


### `rebase.autosquash true`


Autosquash was also a new feature to me. The goal is to make it easier to modify old commits.


Here’s how it works:

- You have a commit that you would like to be combined with some commit that’s 3 commits ago, say `add parsing code`
- You commit it with `git commit --fixup OLD_COMMIT_ID`, which gives the new commit the commit message `fixup! add parsing code`
- Now, when you run `git rebase --autosquash main`, it will automatically combine all the `fixup!` commits with their targets


`rebase.autosquash true` means that `--autosquash` always gets passed automatically to `git rebase`.


### `rebase.autostash true`


This automatically runs `git stash` before a git rebase and `git stash pop` after. It basically passes `--autostash` to `git rebase`.


Personally I’m a little scared of this since it potentially can result in merge
conflicts after the rebase, but I guess that doesn’t come up very often for
people since it seems like a really popular configuration option.


### `push.default simple`, `push.default current`, `push.autoSetupRemote true`


These [`push`](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushdefault) options tell `git push` to automatically push the current branch to a remote branch with the same name.

- `push.default simple` is the default in Git. It only works if your branch is already tracking a remote branch
- `push.default current` is similar, but it’ll always push the local branch to a remote branch with the same name.
- `push.autoSetupRemote true` is a little different – this one makes it so when you first push a branch, it’ll automatically set up tracking for it


I think I prefer `push.autoSetupRemote true` to `push.default current` because
`push.autoSetupRemote true` also lets you **pull** from the matching remote
branch (though you do need to push first to set up tracking). `push.default current` only lets you push.


I believe the only thing to be careful of with `push.autoSetupRemote true` and
`push.default current` is that you need to be confident that you’re never going
to accidentally make a local branch with the same name as an unrelated remote
branch. Lots of people have branch naming conventions (like `julia/my-change`)
that make this kind of conflict very unlikely, or just have few enough
collaborators that branch name conflicts probably won’t happen.


### `init.defaultBranch main`


Create a `main` branch instead of a `master` branch when creating a new repo.


### `commit.verbose true`


This adds the whole commit diff in the text editor where you’re writing your
commit message, to help you remember what you were doing.


### `rerere.enabled true`


This enables [rerere](https://git-scm.com/book/en/v2/Git-Tools-Rerere) ("**re**use **re**covered **re**solution"), which remembers how you resolved merge conflicts
during a `git rebase` and automatically resolves conflicts for you when it can.


### `help.autocorrect 10`


By default git’s autocorrect try to check for typos (like `git ocmmit`), but won’t actually run the corrected command.


If you want it to run the suggestion automatically, you can set
[`help.autocorrect`](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpautoCorrect)
to `1` (run after 0.1 seconds), `10` (run after 1 second), `immediate` (run
immediately), or `prompt` (run after prompting)


### `core.pager delta`


The “pager” is what git uses to display the output of `git diff`, `git log`, `git show`, etc. People set it to:

- [`delta`](https://github.com/dandavison/delta) (a fancy diff viewing tool with syntax highlighting)
- `less -x5,9` (sets tabstops, which I guess helps if you have a lot of files with tabs in them?)
- `less -F -X` (not sure about this one, `-F` seems to disable the pager if everything fits on one screen if but my git seems to do that already anyway)
- `cat` (to disable paging altogether)


I used to use `delta` but turned it off because somehow I messed up the colour
scheme in my terminal and couldn’t figure out how to fix it. I think it’s a
great tool though.


I believe delta also suggests that you set up `interactive.diffFilter  delta --color-only` to syntax highlight code when you run `git add -p`.


### `diff.algorithm histogram`


Git’s default diff algorithm often handles functions being reordered badly. For example look at this diff:


```
-.header {
+.footer {
     margin: 0;
 }

-.footer {
+.header {
     margin: 0;
+    color: green;
 }

```


I find it pretty confusing. But with `diff.algorithm histogram`, the diff looks like this instead, which I find much clearer:


```
-.header {
-    margin: 0;
-}
-
 .footer {
     margin: 0;
 }

+.header {
+    margin: 0;
+    color: green;
+}

```


Some folks also use `patience`, but `histogram` seems to be more popular. [When to Use Each of the Git Diff Algorithms](https://luppeng.wordpress.com/2020/10/10/when-to-use-each-of-the-git-diff-algorithms/) has more on this.


### `core.excludesfile`: a global .gitignore


`core.excludeFiles = ~/.gitignore` lets you set a global gitignore file that
applies to all repositories, for things like `.idea` or `.DS_Store` that you
never want to commit to any repo. It defaults to `~/.config/git/ignore`.


### `includeIf`: separate git configs for personal and work


Lots of people said they use this to configure different email addresses for
personal and work repositories. You can set it up something like this:


```
[includeIf "gitdir:~/code/<work>/"]
path = "~/code/<work>/.gitconfig"

```


### `url."git@github.com:".insteadOf 'https://github.com/'`


I often accidentally clone the HTTP version of a repository instead of the
SSH version and then have to manually go into `~/.git/config` and edit the
remote URL. This seems like a nice workaround: it’ll replace
`https://github.com` in remotes with `git@github.com:`.


Here’s what it looks like in `~/.gitconfig` since it’s kind of a mouthful:


```
[url "git@github.com:"]
	insteadOf = "https://github.com/"

```


One person said they use `pushInsteadOf` instead to only do the replacement for
`git push` because they don’t want to have to unlock their SSH key when
pulling a public repo.


A couple of other people mentioned setting `insteadOf = "gh:"` so they can `git remote add gh:jvns/mysite` to add a remote with less typing.


### `fsckobjects`: avoid data corruption


A couple of people mentioned this one. Someone explained it as “detect data
corruption eagerly. Rarely matters but has saved my entire team a couple
times”.


```
transfer.fsckobjects = true
fetch.fsckobjects = true
receive.fsckObjects = true

```


### submodule stuff


I’ve never understood anything about submodules but a couple of person said they like to set:

- `status.submoduleSummary  true`
- `diff.submodule  log`
- `submodule.recurse  true`


I won’t attempt to explain those but there’s [an explanation on Mastodon by @unlambda here](https://hachyderm.io/@unlambda/111942468084436716#.).


### and more


Here’s everything else that was suggested by at least 2 people:

- `blame.ignoreRevsFile .git-blame-ignore-revs` lets you specify a file with commits to ignore during `git blame`, so that giant renames don’t mess up your blames
- `branch.sort -committerdate`, makes `git branch` sort by most recently used branches instead of alphabetical, to make it easier to find branches. `tag.sort taggerdate` is similar for tags.
- `color.ui false`: to turn off colour
- `commit.cleanup scissors`: so that you can write `#include` in a commit message without the `#` being treated as a comment and removed
- `core.autocrlf false`: on Windows, to work well with folks using Unix
- `core.editor emacs`: to use emacs (or another editor) to edit commit messages
- `credential.helper osxkeychain`: use the Mac keychain for managing
- `diff.tool difftastic`: use [difftastic](https://difftastic.wilfred.me.uk/) (or `meld` or `nvimdiffs`) to display diffs
- `diff.colorMoved default`: uses different colours to highlight lines in diffs that have been “moved”
- `diff.colorMovedWS allow-indentation-change`: with `diff.colorMoved` set, also ignores indentation changes
- `diff.context 10`: include more context in diffs
- `fetch.prune true` and `fetch.prunetags` - automatically delete remote tracking branches that have been deleted
- `gpg.format ssh`: allow you to sign commits with SSH keys
- `log.date iso`: display dates as `2023-05-25 13:54:51` instead of `Thu May 25 13:54:51 2023`
- `merge.keepbackup false`, to get rid of the `.orig` files git creates during a merge conflict
- `merge.tool meld` (or `nvim`, or `nvimdiff`) so that you can use `git mergetool` to help resolve merge conflicts
- `push.followtags true`: push new tags along with commits being pushed
- `rebase.missingCommitsCheck error`: don’t allow deleting commits during a rebase
- `rebase.updateRefs true`: makes it much easier to rebase multiple stacked branches at a time. [Here’s a blog post about it](https://andrewlock.net/working-with-stacked-branches-in-git-is-easier-with-update-refs/).


### how to set these


I generally set git config options with `git config --global NAME VALUE`, for
example `git config --global diff.algorithm histogram`. I usually set all of my
options globally because it stresses me out to have different git behaviour in
different repositories.


If I want to delete an option I’ll edit `~/.gitconfig` manually, where they look like this:


```
[diff]
	algorithm = histogram

```


### config changes I’ve made after writing this post


My git config is pretty minimal, I already had:

- `init.defaultBranch main`
- `push.autoSetupRemote true`
- `merge.tool meld`
- `diff.colorMoved default` (which actually doesn’t even work for me for some reason but I haven’t found the time to debug)


and I added these 3 after writing this blog post:

- `diff.algorithm histogram`
- `branch.sort -committerdate`
- `merge.conflictstyle zdiff3`


I’d probably also set `rebase.autosquash` if making carefully crafted pull
requests with multiple commits were a bigger part of my life right now.


I’ve learned to be cautious about setting new config options – it takes me a
long time to get used to the new behaviour and if I change too many things at
once I just get confused. `branch.sort -committerdate` is something I was
already using anyway (through an alias), and I’m pretty sold that `diff.algorithm histogram` will make my diffs easier to read when I reorder functions.


### that’s all!


I’m always amazed by how useful to just ask a lot of people what stuff they like and
then list the most commonly mentioned ones, like with this [list of new-ish command line tools](https://jvns.ca/blog/2022/04/12/a-list-of-new-ish--command-line-tools/)
I put together a couple of years ago. Having a list of 20 or 30 options to consider feels so much more efficient than combing through a list of [all 600 or so git config options](https://jvns.ca/data/all-git-options.txt)


It was a little confusing to summarize these because git’s default
options have actually changed a lot of the years, so people occasionally have
options set that were important 8 years ago but today are the default. Also a
couple of the experimental options people were using have been removed and
replaced with a different version.


I did my best to explain things accurately as of how git works right now in
2024 but I’ve definitely made mistakes in here somewhere, especially because I
don’t use most of these options myself. Let me know on Mastodon if you see a
mistake and I’ll try to fix it.


I might also ask people about aliases later, there were a bunch of great ones
that I left out because this was already getting long.
