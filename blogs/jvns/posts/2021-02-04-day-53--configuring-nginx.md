---
title: "Day 53: a little nginx, IPv6, and wireguard"
date: 2021-02-04
url: https://jvns.ca/blog/2021/02/04/day-53--configuring-nginx/
slug: day-53--configuring-nginx
word_count: 371
---


I spent the day on Wednesday trying to run my puzzle thing on fly.io. I got
part of the way there and learned a few things along the way:


### miscellaneous IPv6 learning


I’d never really used IPv6 before, and I learned that IPv6 address are often in
square brackets. For example to get `rails` to listen on IPv6 addresses,
I had to run:


```
CMD ["rails", "server", "-b", "[::]"]

```


`CMD ["rails", "server", "-b", "0.0.0.0"]` will only listen on IPv4 addresses!


But you don’t *always* seem to need square brackets, for example I ssh’d to an IPv6 address like this:


```
ssh fdaa:0:bff:a7b:aa4:4c98:4224:2

```


I think the rule might be that you need to use square brackets if you’re going
to include a port, like `fade::5` port `53` is `[fade::5]:53`, because
otherwise it would be ambiguous whether the port is part of the IP address or
not.


### how to make nginx re-resolve DNS every time


I learned that if you do


```
proxy_pass http://some-website.com:2000;

```


in an nginx configuration, nginx will resolve `some-website.com` to an IP
address once when it boots, and then never update again. This was not good
because the IP addresses of my backends were changing all the time, so I needed
to figure out how to get nginx to re-resolve DNS.


Instead I needed to do something like this:


```
location @rails {
    resolver [fdaa::3];
    set $backend "http://rails.internal:8080";
    proxy_pass $backend;
}

```


It turns out that if you `proxy_pass` to something with a variable with it,
nginx will resolve DNS. You also need to set a DNS server to use explicitly,
nginx won’t use what’s in `/etc/resolv.conf`.


This actually still doesn’t work and I don’t know why, nginx. Maybe I’ll figure
that out today.


### setting up Wireguard seems easy


I set up Wireguard for the first time and it was very straightforward!


The other side I was connecting to was already set with Wireguard, so I just
needed to set up my laptop using the configuration they said to use. I just
needed to:

1. do `apt-get install wireguard`
2. Download the Wireguard configuration file the other side wanted me to use and put it in `/etc/wireguard/fly.conf`
3. Run `wg-quick up fly`
4. done!
