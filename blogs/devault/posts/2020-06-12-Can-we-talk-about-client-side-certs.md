---
title: "Can we talk about client-side certificates?"
date: 2020-06-12
url: https://drewdevault.com/2020/06/12/Can-we-talk-about-client-side-certs.html
slug: Can-we-talk-about-client-side-certs
word_count: 894
---

I’m working on improving the means by which API users authenticate with the
SourceHut API. Today, I was reading  [RFC 6749](https://tools.ietf.org/html/rfc6749)  (OAuth2) for this purpose,
and it got me thinking about the original OAuth spec. I recalled vaguely that it
had the API clients actually  *sign*  every request, and…  [yep, indeed it
does](https://tools.ietf.org/html/rfc5849) . This also got me thinking: what else signs requests? TLS!

OAuth is very complicated. The RFC is 76 pages long, the separate bearer token
RFC (6750) is another 18, and no one has ever read either of them. Add JSON Web
Tokens (RFC 7519, 30 pages), too. The process is complicated and everyone
implements it themselves — a sure way to make mistakes in a
security-critical component. Not all of the data is authenticated, no
cryptography is involved at any step, and it’s easy for either party to end up
in an unexpected state. The server has to deal with problems of revocation and
generating a secure token itself. Have you ever met anyone who feels positively
about OAuth?

Now, take a seat. Have a cup of coffee. I want to talk about client-side
certificates. Why didn’t they take off? Let’s sketch up a hypothetical TLS-based
protocol as an alternative to OAuth.  Picture the following…

1. You, an API client developer, generate a certificate authority and
intermediate, and you upload your CA certificate to the Service Provider as
part of your registration as a user agent.
2. When you want a user to authorize you to access their account, you generate a
certificate for them, and redirect them to the Service Provider’s
authorization page with a  CSR 
in tow. Your certificate includes, among other things, the list of authorized
scopes for which you want to be granted access. It is already signed with
your client CA key, or one of its intermediates.
3. The client reviews the desired access, and consents. They are redirected back
to your API client application, along with the signed certificate.
4. Use this client-side certificate to authenticate your API requests. Hooray!

Several advantages to this approach occur to me.

* You get strong encryption and authentication guarantees for free.
* TLS is basically the single most ironclad, battle-tested security mechanism on
the internet, and mature implementations are available for every platform.
Everyone implements OAuth themselves, and often poorly.
* Client-side certificates are stateless. They contain all of the information
necessary to prove that the client is entitled to access.
* If you handle SSL termination with nginx, haproxy, etc, you can reject
unauthorized requests before your application backend ever even sees them.
* The service provider can untrust the client’s CA in a single revocation, if
they are malicious or lose their private keys.
* The API client and service provider are both always certain that the process
was deliberately initiated by the API client. No weird state tokens to carry
through the process like OAuth uses!
* Lots of free features: any metadata you like, built-in expirations, API
clients can self-organize into intermediates at their discretion, and so on.
* Security-concious end users can toggle a flag in their account which would, as
part of the consent process, ask them to sign the API client’s certificate
themselves, before the signed certificate is returned to the API client. Then
any API request authorized for that user’s account has to be signed by the API
client, the service provider,  *and*  the user to be valid.

Here’s another example: say your organization has several services, each of
which interacts with a subset of Acme Co’s API on behalf of their users. Your
organization generates a single root CA, and signs up for Acme Co’s API with it.
Then you issue intermediate CAs to each of your services, which are  *only* 
allowed to issue CSRs for the subset of scopes they require. If any service is
compromised, it can’t be used to get more access than it already had, and you
can revoke just that one intermediate without affecting the rest.

Even some famous downsides, such as  CRLs  and  OCSP , are mitigated here, because the system is much more
centralized. You control all of the endpoints which will be validating
certificates, you can just distribute revocations directly to them as soon as
they come in.

The advantages are clearly numerous. Let’s wrap it up in a cute, Google-able
name, write some nice tooling and helper libraries for it, and ship it!

Or, maybe not. I have a nagging feeling that I’m missing something here. It
doesn’t seem right that such an obvious solution would have been left on the
table, by everyone, for decades. Maybe it’s just that the whole certificate
signing dance has left a bad taste in everyone’s mouth — many of us have
not-so-fond memories of futzing around with the awful OpenSSL CLI to generate a
CSR. But, there’s no reason why we couldn’t do it better, and more streamlined,
if we had the motivation to.

There are also more use-cases for client-side certificates that seem rather
compelling, such as an alternative to user passwords. Web browser support for
client-side certificates totally sucks, but that is a solvable problem.

For the record, I have no intention of using this approach for the SourceHut
API. This thought simply occurred to me, and I want to hear what you think. Why
aren’t we using client-side certificates?
