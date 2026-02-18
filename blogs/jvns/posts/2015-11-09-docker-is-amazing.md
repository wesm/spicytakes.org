---
title: "Docker is amazing"
date: 2015-11-09
url: https://jvns.ca/blog/2015/11/09/docker-is-amazing/
slug: docker-is-amazing
word_count: 336
---


I didn’t really understand what Docker was *for* until yesterday. I mean, containers. Cool. Whatever.


Yesterday I was trying to get an environment for some neural networks experiments (exciting post upcoming featuring THE QUEEN!). And it was, well, horrible. I needed Ubuntu 14.04, and I thought I was going to have reinstall my operating system, and I am apparently past the age when that was fun. I needed all these C++ things and nothing was working and I did not know what to do.


AND THEN I REMEMBERED ABOUT DOCKER.


I downloaded an Ubuntu 14.04 image, and suddenly I just had Ubuntu 14.04! And I could INSTALL THINGS ON IT. Without worrying! And if I put them in a Dockerfile, it would let OTHER PEOPLE set up the same environment. Whoa.


And it’s fast! It’s not like a virtual machine which takes forever to start – starting a Docker container is just like, well, starting a program. Fast. Now I can run all my experiments inside the container and it’s not a problem.


[Here’s what the Dockerfile looks like!](https://github.com/jvns/neural-nets-are-weird/blob/master/Dockerfile) It was really easy! I just do the same random crap I might do to set up my environment normally (do you see where I install some packages, and then replace the sources.list from, uh, Debian wheezy, with an Ubuntu sources.list in the middle? yeah I did that.). But I don’t have to worry about screwing up my computer while doing it, and then even if it’s a mess, it’s a *reproducible* mess!


It includes the following gem:


```

RUN cd /opt/caffe \
   && cp Makefile.config.example Makefile.config \
   && echo LS0tIE1ha2VmaWxlLmNvbmZpZy5leGFtcGxlCTIwMTUtMTEtMDcgMTU6NDU6MTIuNTEzNjQ3ODc2IC0wNTAwCisrKyBNYWtlZmlsZS5jb25maWcJMjAxNS0xMS0wOCAyMDozODoyMi4xMDcwNTA2MDggLTA1MDAKQEAgLTUsNyArNSw3IEBACiAjIFVTRV9DVUROTiA6PSAxCiAKICMgQ1BVLW9ubHkgc3dpdGNoICh1bmNvbW1lbnQgdG8gYnVpbGQgd2l0aG91dCBHUFUgc3VwcG9ydCkuCi0jIENQVV9PTkxZIDo9IDEKK0NQVV9PTkxZIDo9IDEKIAogIyB1bmNvbW1lbnQgdG8gZGlzYWJsZSBJTyBkZXBlbmRlbmNpZXMgYW5kIGNvcnJlc3BvbmRpbmcgZGF0YSBsYXllcnMKICMgVVNFX09QRU5DViA6PSAwCkBAIC02NSwxNCArNjUsMTQgQEAKIAkJL3Vzci9saWIvcHl0aG9uMi43L2Rpc3QtcGFja2FnZXMvbnVtcHkvY29yZS9pbmNsdWRlCiAjIEFuYWNvbmRhIFB5dGhvbiBkaXN0cmlidXRpb24gaXMgcXVpdGUgcG9wdWxhci4gSW5jbHVkZSBwYXRoOgogIyBWZXJpZnkgYW5hY29uZGEgbG9jYXRpb24sIHNvbWV0aW1lcyBpdCdzIGluIHJvb3QuCi0jIEFOQUNPTkRBX0hPTUUgOj0gJChIT01FKS9hbmFjb25kYQotIyBQWVRIT05fSU5DTFVERSA6PSAkKEFOQUNPTkRBX0hPTUUpL2luY2x1ZGUgXAotCQkjICQoQU5BQ09OREFfSE9NRSkvaW5jbHVkZS9weXRob24yLjcgXAotCQkjICQoQU5BQ09OREFfSE9NRSkvbGliL3B5dGhvbjIuNy9zaXRlLXBhY2thZ2VzL251bXB5L2NvcmUvaW5jbHVkZSBcCitBTkFDT05EQV9IT01FIDo9IC9vcHQvY29uZGEKK1BZVEhPTl9JTkNMVURFIDo9ICQoQU5BQ09OREFfSE9NRSkvaW5jbHVkZSBcCisJCSAkKEFOQUNPTkRBX0hPTUUpL2luY2x1ZGUvcHl0aG9uMi43IFwKKwkJICQoQU5BQ09OREFfSE9NRSkvbGliL3B5dGhvbjIuNy9zaXRlLXBhY2thZ2VzL251bXB5L2NvcmUvaW5jbHVkZSBcCiAKICMgV2UgbmVlZCB0byBiZSBhYmxlIHRvIGZpbmQgbGlicHl0aG9uWC5YLnNvIG9yIC5keWxpYi4KIFBZVEhPTl9MSUIgOj0gL3Vzci9saWIKLSMgUFlUSE9OX0xJQiA6PSAkKEFOQUNPTkRBX0hPTUUpL2xpYgorUFlUSE9OX0xJQiA6PSAkKEFOQUNPTkRBX0hPTUUpL2xpYgogCiAjIEhvbWVicmV3IGluc3RhbGxzIG51bXB5IGluIGEgbm9uIHN0YW5kYXJkIHBhdGggKGtlZyBvbmx5KQogIyBQWVRIT05fSU5DTFVERSArPSAkKGRpciAkKHNoZWxsIHB5dGhvbiAtYyAnaW1wb3J0IG51bXB5LmNvcmU7IHByaW50KG51bXB5LmNvcmUuX19maWxlX18pJykpL2luY2x1ZGUK \
   | base64 -d \ 
   | patch -u Makefile.config

```


where I edited a file manually, made a patch, base64 encoded it, and just pasted the string into the Dockerfile so that the edits I needed would work.


The next time I need to compile a thing with horrible dependencies that I don’t have on my computer and that conflict with everything, I’m totally using Docker.
