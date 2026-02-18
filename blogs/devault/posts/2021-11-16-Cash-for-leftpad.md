---
title: "I will pay you cash to delete your npm module"
date: 2021-11-16
url: https://drewdevault.com/2021/11/16/Cash-for-leftpad.html
slug: Cash-for-leftpad
word_count: 695
---

npm’s culture presents a major problem for global software security. It’s
grossly irresponsible to let dependency trees grow to thousands of dependencies,
from vendors you may have never heard of and likely have not critically
evaluated, to solve trivial tasks which could have been done from scratch in
mere seconds, or, if properly considered, might not even be needed in the first
place.

We need to figure out a way to curb this reckless behavior, but how?

I have an idea. Remember left-pad? That needs to happen more often.

I’ll pay you cold hard cash to delete your npm module. The exact amount will be
determined on this equation, which is designed to offer higher payouts for
modules with more downloads and fewer lines of code. A condition of this is that
you must delete it without notice, so that everyone who depends on it wakes up
to a broken build.

Let’s consider an example:  [isArray](https://www.npmjs.com/package/isarray) . It has only four lines of code:

```
var toString = {}.toString;

module.exports = Array.isArray || function (arr) {
  return toString.call(arr) === '[object Array]';
};
```

With 51 million downloads this week, this works out to a reward of $710.

To prevent abuse, we’ll have to agree to each case in advance. I’ll review your
module to make sure it qualifies, and check for any funny business like
suspicious download figures or minified code. We must come to an agreement
 *before*  you delete the module, since I will not be able to check the line
counts or download numbers after it’s gone.

I may also ask you to wait to delete your module, so that the chaos from each
deletion is separated by a few weeks to maximize the impact. Also, the reward is
capped at $1,000, so that I can still pay rent after this.

Do we have a deal?  Click here to apply →

Alright, the gig is up: this is satire. I’m not actually going to pay you to
delete your npm module, nor do I want to bring about a dark winter of chaos in
the Node ecosystem. Plus,  [it wouldn’t actually work](https://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy) .

I do hope that this idea strikes fear in the hearts of any Node developers that
read it, and in other programming language communities which have taken after
npm. What are you going to do if one of your dependencies vanishes?  What if
someone studies the minified code on your website, picks out an obscure
dependency they find there, then bribes the maintainers?

Most Node developers have no idea what’s in their dependency tree. Most of them
are thousands of entries long, and have never been audited. This behavior is
totally reckless and needs to stop.

Most of my projects have fewer than 100 dependencies, and many have fewer than
10. Some have zero. This is by design. You can’t have a free lunch, I’m afraid.
Adding a dependency is a serious decision which requires consensus within the
team, an audit of the new dependency, an understanding of its health and
long-term prospects, and an ongoing commitment to re-audit them and be prepared
to change course as necessary.

isArray license:

```
Copyright (c) 2013 Julian Gruber <julian@juliangruber.com>.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
