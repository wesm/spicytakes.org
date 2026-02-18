---
title: "Day 32: A Rails model that doesn't use the database with ActiveHash"
date: 2021-01-07
url: https://jvns.ca/blog/2021/01/07/day-32--a-rails-model-that-doesn-t-use-the-database-with-activehash/
slug: day-32--a-rails-model-that-doesn-t-use-the-database-with-activehash
word_count: 789
---


Hello! RC took a few weeks ago, and it’s back now! I’m batching these posts a
few days at a time, so here’s what happened on Tuesday.


### deployed docker-compose to production


On Monday I set up a dev environment with Docker Compose ([blog
post](https://jvns.ca/blog/2021/01/04/docker-compose-is-nice/)), but I wasn’t sure if it would work well in production.


My “production” in this case is a single DigitalOcean droplet, and I thought
that setting up a new server to use docker-compose instead of what I already
had would be a lot of work.


It turned out to be easier than I thought and it only took a couple of hours
and I felt like my new setup was WAY more robust afterwards.


### the steps to setting up docker-compose in production


I think all of my steps were:

- use DigitalOcean’s one-click Docker droplet to start an instance
- install `net-tools` so that I could use netstat
- install `golang` so that I could build go programs outside the container (though I’ll probably switch to doing this in a container soon, it’ll be better)
- clone my Github repo to a bare repository on the droplet (`git clone https://github.com/my/repo --bare`)
- set up a post-receive hook (like in [this example](https://macarthur.me/posts/deploying-code-with-a-git-hook)), [here’s my post-receive hook](https://github.com/jvns/incident-service/blob/main/scripts/post-receive)
- write a `docker-compose-prod.yml` (you can [see it here](https://github.com/jvns/incident-service/blob/3e1ac221a7eed24032ae0a20fcd222552b56f995/docker-compose-prod.yml)) with a slightly different configuration for production
- Add my server as a remote, like `git remote add railsbox root@1.2.3.4:/my-repo.git`
- run `git push railbox`
- make a dump of my database with `pg_dump` and restore it in the new database
- copy some secrets that aren’t in git over to the server (SSH keys, the Rails secret master key, and some secret environment variables)
- fix a bunch of miscellaneous problems with my configuration files to make them actually work
- update my DNS records
- done!


This is pretty far from “just click one thing and you’re done” but I feel like
if I had to do it again because I lost my production server it wouldn’t be too
bad. It’s definitely much better than “just create a lot of systemd files by
hand” which is what I was doing before.


### making it easier for me to edit my puzzles


All of this docker-compose stuff wasn’t actually my goal for the day, though!


My real goal was: I have this sort of puzzle game, and I was storing the
definitions for my puzzles (basically the title and a `cloud-init.yaml` file)
in the database.


This really wasn’t working for me because I needed to make a lot of updates to
the puzzles (at least to start) and having to do it through a web interface
felt way too slow.


Andther problem I was having was that the puzzles tables wasn’t synced between
dev and prod, which made it hard to test.


### enter ActiveHash!


[ActiveHash](https://github.com/zilkey/active_hash) is a Ruby gem that let you
just define all of your data for a model in a hashmap or file instead of having
a database table.


This feels good for now because I only have like 6 puzzles and so having them
all in a file makes it way easier to edit them.


The main thing that makes me feel nervous about it is that right now I’m
entering the puzzle IDs manually (like `id: 1`) and I need to make sure to not
accidentally reuse/change the IDs. This is important because some other fields
in the database reference the puzzle ID.


### my current Puzzle class


Here’s what my Puzzle with ActiveHash looks like. It’s really simple.


```
class Puzzle < ActiveHash::Base
  def to_param
    "#{id}-#{slug}"
  end

  def finished?(user)
    PuzzleStatus.where(user_id: user.id).where(puzzle_id: self.id).first&.finished || false
  end

  def cloud_init
    File.read("puzzles/#{group}/#{slug}/cloud-init.yaml")
  end

  self.data = [
    {
      id: 1,
      group: "networking",
      slug: "connection-timeout",
      title: "The Case of the Connection Timeout",
      published: false,
    },
    ... more data here

```


### I can still use some ActiveRecord methods!


Things like `belongs_to` and `has_many` don’t work (which kinda makes sense to
me), but I can still do `Puzzle.find(id)` to find a puzzle by its ID, so I
didn’t have to change too much of my code.


And because I’m using ActiveRecord methods, if I ever want to switch back to
using a database to manage them, it should be pretty easy!


### what I had to do to switch to this class


I needed to:

- remove all of the edit/update/create code from my Puzzles controller
- write a migration to drop the `puzzles` table from the database
- remove the `puzzles.yml` fake data from my tests (because it was inserting that data into the database, which was failing)


and probably some more things that I’ve forgotten


### that’s all!


I felt pretty happy about both these changes.
