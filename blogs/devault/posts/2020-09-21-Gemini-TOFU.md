---
title: "TOFU recommendations for Gemini"
date: 2020-09-21
url: https://drewdevault.com/2020/09/21/Gemini-TOFU.html
slug: Gemini-TOFU
word_count: 625
---

I will have more to say about  [Gemini](https://gemini.circumlunar.space/)  in the future, but for now, I wanted to
write up some details about one thing in particular: the trust-on-first-use
algorithm I implemented for my client,  [gmni](https://sr.ht/~sircmpwn/gmni) . I think you should implement
this algorithm, too!

First of all, it’s important to note that the Gemini specification explicitly
mentions TOFU and the role of self-signed certificates: they are the norm in
Geminiland, and if your client does not support them then you’re going to be
unable to browse many sites. However, the exact details are left up to the
implementation. Here’s what mine does:

First, on startup, it finds the known_hosts file. For my client, this is
 `~/.local/share/gmni/known_hosts`  (the exact path is adjusted as necessary per
the XDG basedirs specification). Each line of this file represents a known host,
and each host has four fields separated by spaces, in this order:

* Hostname (e.g. gemini.circumlunar.space)
* Fingerprint algorithm (e.g. SHA-512)
* Fingerprint, in hexadecimal, with ‘:’ between each octet (e.g. 55:01:D8…)
* Unix timestamp of the certificate’s notAfter date

If a known_hosts entry is encountered with a hashing algorithm you don’t
understand, it is disregarded.

Then, when processing a request and deciding whether or not to trust its
certificate, take the following steps:

1. Verify that the certificate makes sense. Check the notBefore and notAfter
dates against the current time, and check that the hostname is correct
(including wildcards). Apply any other scrutiny you want, like enforcing a
good hash algorithm or an upper limit on the expiration date. If these checks
do not pass, the trust state is INVALID, GOTO 5.
2. Compute the certificate’s fingerprint. Use the entire certificate (in OpenSSL
terms,  `X509_digest`  will do this), not just the public key. 1
3. Look up the known_hosts record for this hostname. If one is found, but the
record is expired, disregard it. If one is found, and the fingerprint does
not match, the trust state is UNTRUSTED, GOTO 5. Otherwise, the trust state
is TRUSTED. GOTO 7.
4. The trust state is UNKNOWN. GOTO 5.
5. Display information about the certficate and its trust state to the user, and
prompt them to choose an action, from the following options:
  * If INVALID, the user’s choices are ABORT or TRUST_TEMPORARY.
  * If UNKNOWN, the user’s choices are ABORT, TRUST_TEMPORARY, or TRUST_ALWAYS.
  * If UNTRUSTED, abort the request and display a diagnostic message. The user
must manually edit the known_hosts file to correct the issue.
6. Complete the requested action:
  * If ABORT, terminate the request.
  * If TRUST_TEMPORARY, update the session’s list of known hosts.
  * If TRUST_ALWAYS, append a record to the known_hosts file and update the
session’s list of known hosts.
7. Allow the request to proceed.

If the trust state is UNKNOWN, instead of requring user input to proceed, the
implementation MAY proceed with the request IF the UI displays that a new
certificate was trusted and provides a means to review the certificate and
revoke that trust.

Note that being signed by a certificate authority in the system trust store is
not considered meaningful to this algorithm. Such a cert is TOFU’d all the same.

That’s it! If you have feedback on this approach, please  [send me an
email](mailto:sir@cmpwn.com) .

My implementation doesn’t  *entirely*  match this behavior, but it’s close and
I’ll finish it up before 1.0. If you want to read the code,  [here it is](https://git.sr.ht/~sircmpwn/gmni/tree/master/src/tofu.c) .

Bonus recommendation for servers: you  **should**  use a self-signed certificate,
and you  **should not**  use a certificate signed by one of the mainstream
certificate authorities. We don’t need to carry along the legacy CA cabal into
our brave new Gemini future.

1. Rationale: this fingerprint matches the output of `openssl x509 -sha512 -fingerprint`. ↩︎
