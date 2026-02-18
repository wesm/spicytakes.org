---
title: "How to set up a blog in 5 minutes"
date: 2014-10-08
url: https://jvns.ca/blog/2014/10/08/how-to-set-up-a-blog-in-5-minutes/
slug: how-to-set-up-a-blog-in-5-minutes
word_count: 639
---


Some people at [Hacker School](https://hackerschool.com) were asking
for advice / directions for how to set up a blog. So here are some
directions for a simple possible way!


There are lots of ways to set up a blog. This way will let you write
posts with Markdown, version them with Git, publish them with `git push origin gh-pages`, and, most importantly, think for exactly 0
seconds about what your site should look like. You’ll need a working
Ruby environment which is the hardest part. I use
[rbenv](https://github.com/sstephenson/rbenv#basic-github-checkout) to
manage my Ruby. I have spent months being confused about how to make
Ruby work, so If you also need to set up Ruby it will take more than 5
minutes and this will be a total lie.


But! If you do, there is no excuse for you to not have a blog
within 5 minutes (or at least not more than an hour). It took me 40
minutes but that was because I was also writing this blog post.


I used to worry a lot about what my website looked like, and then I
realized if I wrote interesting blog posts basically nobody cared!


All of my internal monologues about whether I should make it orange or
not were for nothing. (the answer to orange is always yes, though).
Lots of people subscribe with RSS anyway and never look at this site
in the first place :) (I eventually commissioned my awesome friend
[Lea](http://www.instamatique.com/lea/) to redesign this site and now
I think it looks awesome).


So if you have something to say, even if it is only one blog post’s
worth of things, you can totally set up a site! Let’s start.


We’ll be using

- [Jekyll](http://jekyllrb.com/), a static site generator
- [Octopress](http://github.com/octopress/octopress) to create a
skeleton site without having to think about what it should look like
- GitHub pages to host our site


### Step 1: Install Octopress:


```
$ gem install octopress --pre
$ rbenv rehash

```


### Step 2: Create a GitHub repo


You’ll need a place to put your blog! I made a new repository at
[https://github.com/jvns/fake-website](https://github.com/jvns/fake-website).
If you want your blog to appear at `your-username.github.io`, call
this repo `your-username.github.io`. GitHub has some more instructions
[here](https://help.github.com/articles/user-organization-and-project-pages/)
and
[here](https://help.github.com/articles/creating-project-pages-manually/).


If you want your blog to be on a custom non-GitHub domain that you
own, there are directions about
[how to set up a custom domain](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/).


### Step 3: Create a skeleton site


Now we can make a website!


```
octopress new fake-website
cd fake-website
jekyll serve

```


This will create a new skeleton of an Octopress blog, and serve it to
you on [http://localhost:4000](http://localhost:4000), where you can
tinker to your heart’s content. Not too much! Remember, you only have
5 minutes.


### Step 4: Push your website to GitHub


Now that we’ve maybe tinkered a bit, we’re ready for the world to see
our (empty) website! If you put a Jekyll site in the `gh-pages` branch
of a GitHub repository, GitHub will build it and serve it for you.


From inside `fake-website`, I did:


```
git init
git add .
git commit -m"My awesome blog"
git remote add origin git@github.com:jvns/fake-website
git checkout -b gh-pages
git push -u origin gh-pages

```


### Step 5: Edit _config.yml


When I do this, I have a website magically generated at
[http://jvns.github.io/fake-website](http://jvns.github.io/fake-website).
But it looks totally broken! You need to make one more change: edit
`_config.yml` to change the base URL of your website.
[Here’s my commit to fix it](https://github.com/jvns/fake-website/commit/ae89338857ee37c98c102be6fef6febbefbf0ede).
20


### Step 6: Go blog (takes more than 5 minutes oops)


At this point you have probably discovered that if anyone on the
internet tells you something takes 5 minutes they are definitely
lying. But maybe you have succeeded anyway.


You can create new blog posts with `octopress new post "My Awesome Post"`. I’m excited to see what you write!
