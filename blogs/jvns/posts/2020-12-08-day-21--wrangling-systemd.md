---
title: "Day 21: wrangling systemd & setting up git deploys to a VM"
date: 2020-12-08
url: https://jvns.ca/blog/2020/12/08/day-21--wrangling-systemd/
slug: day-21--wrangling-systemd
word_count: 678
---


On Monday I decided to take a break from machine learning, so I spent all day
setting up a server for this incidents-as-a-service project I’m working on on
digital ocean.


Here are a few things I learned:


### digital ocean apps are compatible with Heroku


I was originally going to use GCP for this project, but I got mad because of my
experience with IAM on Friday and decided to try Digital Ocean instead. It
turns out that Digital Ocean is MUCH EASIER to use than GCP (at least at
first) and so I decided to try it out.


One cool thing I found out is that Digital Ocean’s new “app platform” lets you
deploy Heroku apps to it pretty seamlessly.


This ended up not working for me because I needed to SSH to other instances for
my project and this doesn’t seem to be possible from a Digital Ocean “app”
(which I guess is a container behind a pretty restrictive firewall).


So I decided to use a Digital Ocean VM instead.


### digital ocean has nice VM images


My project is a Rails app. Digital Ocean seems to have a “marketplace” with a
[Ruby on Rails](https://marketplace.digitalocean.com/apps/ruby-on-rails) page, and so I clicked “Create Ruby on Rails droplet” and it created a VM for me that had:

- nginx
- Rails
- Postgres
- systemd services for all of those


all set up what seems to be a pretty reasonable way. I thought this was great
and it seemed to be a pretty good starting point to set up a Rails app. I
thought about using containers but I decided not to, maybe I’ll go back and
make the whole thing more reproducible later.


I liked that there’s a Postgres already running on the machine, since it’s
way cheaper than a managed Postgres. And I figure if I want to migrate to
managed Postgres I can always do that later.


### you can implement push-to-deploy with a git post-receive hook


Once I had that VM running, I was mad that I didn’t have the nice “push to
deploy” experience that I got with Heroku / digital ocean apps, so I Googled other options.


I found this really nice blog post [Deploying Code with a Git Hook on a DigitalOcean Droplet](https://macarthur.me/posts/deploying-code-with-a-git-hook)
about how to use a git post-receive hook to deploy to a VM on push.


This approach feels more like “hacked together bash script” than “fancy stable
system” but after spending some time wrangling systemd I got it to work and
it’s kind of fun to have a more basic system where I push directly to the VM
I’m running my code on.


### systemd can run a script before your service starts


After I deploy my code with `git push`, I need to make sure to install new gems
/ run Rails migrations / etc.


There are lots of ways to do this, but I found out that you can set an
`ExecStartPre` in systemd to run a script before the service starts. So if I
run `service rails restart`, it’ll run my `restart.sh` script first and install
any new required gems, etc.


My Rails systemd file’s Service section looks something like this:


```
[Service]
Type=simple
User=rails
Group=rails
WorkingDirectory=/my/rails/directory
ExecStart=/bin/bash -lc 'bundle exec puma'
Environment=RAILS_ENV=production
ExecStartPre=/bin/bash -x /path/to/my/restart/script
TimeoutSec=300s
RestartSec=300s
Restart=always

```


I needed to make `TimeoutSec` bigger because the restart script runs `bundle install` and sometimes that can take a while.


### journald needed to be restarted for some reason


I spent a LOT of time being confused because systemd-journald didn’t have my
Rails app’s logs, even though it seemed to be running correctly.


Eventually I restarted journald and it fixed everything, but I don’t really
understand why. I really don’t understand systemd yet but maybe one day I’ll
get there.


### that’s all!


I found setting up a VM in a very non-reproducible way with a hacked together
build/deploy system pretty fun. I might redo it to use containers/something
that might be easier to maintain if the project ends up being something I want
to keep.
