---
title: "A quick review of my Let's Encrypt setup"
date: 2018-06-27
url: https://drewdevault.com/2018/06/27/My-lets-encrypt-setup.html
slug: My-lets-encrypt-setup
word_count: 577
---

Let’s Encrypt makes TLS much easier for pretty much everyone, but can still
be annoying to use. It took me a while to smooth over the cracks in my Let’s
Encrypt configuration across my (large) fleet of different TLS-enabled services.
I wanted to take a quick moment to share setup with you.

2020-01-02 update: acme-client is unmaintained and caught the BSD disease
anyway. I use  [uacme](https://github.com/ndilieto/uacme)  and my current
procedure is documented on my  [new server checklist](/new-server.html) . It might
not be exactly applicable to your circumstances, YMMV.

The main components are:

* [acme-client](https://kristaps.bsd.lv/acme-client/)
* nginx
* cron

nginx and cron need no introduction, but acme-client deserves a closer look. The
acme client blessed by Let’s Encrypt is  [certbot](https://certbot.eff.org/) , but
BOY is it complicated. It’s a big ol’ pile of Python and I’ve found it fragile,
complicated, and annoying. The goal of maintaining your nginx and apache configs
for you is well intentioned but ultimately useless for advanced users. The
complexity of certbot is through the roof, and complicated software breaks.

I bounced between alternatives for a while but when I found acme-client, it
totally clicked. This one is written in C with minimal dependencies (LibreSSL
and libcurl, no brainers IMO). I bring a statically linked acme-client binary
with me to new servers and setup time approaches zero as a result.

I use nginx to answer challenges (and for some services, to use the final
certificates for HTTPS - did you know you can use Let’s Encrypt for more
protocols than just HTTPS?). I quickly  `mkdir -p /var/www/acme/.well-known/acme-challenge` , make sure nginx can read it, and add
the following rules to nginx to handle challenges:

```
server {
    listen 80;
    listen [::]:80;
    server_name example.org;

    location ^~ /.well-known/acme-challenge {
        alias /var/www/acme;
    }
}
```

If I’m not using the certificates for HTTPS, this is all I need. But assuming I
have some kind of website going, the full configuration usually looks more like
this:

```
server {
    listen 80;
    listen [::]:80;
    server_name example.org;

    location / {
        return 302 https://$server_name$request_uri;
    }

    location ^~ /.well-known/acme-challenge {
        alias /var/www/acme;
    }
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name example.org;

    ssl_certificate /etc/ssl/acme/$server_name/fullchain.pem;
    ssl_certificate_key /etc/ssl/acme/$server_name/privkey.pem;

    location ^~ /.well-known/acme-challenge {
        alias /var/www/acme;
    }

    # ...application specific rules...
}
```

This covers the nginx side of things. To actually do certificate negotiation, I
have a simple script I carry around:

```
exec >>/var/log/acme 2>&1
date

acme() {
    site=$1
    shift
    acme-client -vNn \
        -c /etc/ssl/acme/$site/ \
        -k /etc/ssl/acme/$site/privkey.pem \
        $site $*
}

acme example.org subd1.example.org subd2.example.org

nginx -s reload
```

The first two lines set up a log file in  `/var/log/acme`  I can use to debug any
issues that arise. Then I have a little helper function that wires up
acme-client the way I like it, and I can call it for each domain I need certs
for on this server. The last line changes if I’m doing something other than
HTTPS with the certs (for example,  `postfix reload` ).

One gotcha is that acme-client will bail out if the directories don’t exist when
you run it, so a quick  `mkdir -p /etc/ssl/acme/example.org`  when adding new
sites is necessary

The final step is a simple cron entry that runs the script daily:

```
0 0 * * * /usr/local/bin/acme-update-certs
```

It’s that easy. It took me a while to get a Let’s Encrypt setup that was simple
and satisfactory, but I believe I’ve settled on this one. I hope you find it
useful!
