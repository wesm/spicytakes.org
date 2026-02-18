---
title: "Day 51: Fixed my logging and made a couple of puzzles"
date: 2021-02-02
url: https://jvns.ca/blog/2021/02/02/day-51--made-a-couple-of-puzzles/
slug: day-51--made-a-couple-of-puzzles
word_count: 336
---


Here are a couple of things I did yesterday!


### some logging improvements


I was having a problem on my server where I was logging in 3 different ways:

1. Rails was logging to a file called `production.log`
2. my Go proxy was logging to Docker Compose’s default log thing (whatever that is)
3. my Firecracker manager service was logging to journald


This was very annoying because I was constantly confused about where to look
for logs and it was impossible to see everything in one place.


I set `RAILS_LOG_TO_STDOUT=1` and told Docker Compose to log to journald instead like this:


```
  rails:
    environment:
      - RAILS_LOG_TO_STDOUT=1 
    logging:
      driver: "journald"
      options:
        tag: "rails"
    build: 
        dockerfile: docker/rails/Dockerfile
        context: .

```


Once I had the logs in journald, it took me a little while to figure out how to
ask journalctl to actually show me the logs for those services and it was
pretty unwieldy, so I added this little function to my `.bashrc` to help me
out.


```
function logs {
    journalctl -b SYSLOG_IDENTIFIER=$1 | less +G
}

```


### some strace puzzles


I wrote a couple of starter puzzles about strace. Here’s the description for
the one called “the case of the misconfigured logger”


> There’s a program in your home directory called run-me. For some reason, it’s been misconfigured so that it’s writing its logs to /dev/null instead of to a file. But you need to know what it’s writing!


> Use strace to find out what it’s writing.


and one called “the case of the mystery log file”


> There’s a program in your home directory called run-me. It’s logging its output to a log file, but you can’t find the name of the log file ANYWHERE in its documentation!


> Use strace to find out the name of the log file.


These aren’t particularly good yet, probably because I spent maybe 5 minutes
writing them. Lots of work to do on this front, but I’ll probably do most of it
after RC is over.
