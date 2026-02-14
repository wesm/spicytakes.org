---
title: "Turbo 8 is dropping TypeScript"
date: 2023-09-06
url: https://world.hey.com/dhh/turbo-8-is-dropping-typescript-70165c01
slug: turbo-8-is-dropping-typescript-70165c01
word_count: 501
---

By all accounts, TypeScript has been a big success for Microsoft. I've seen loads of people sparkle with joy from dousing JavaScript with explicit types that can be checked by a compiler. But I've never been a fan. Not after
[giving it five minutes](https://signalvnoise.com/posts/3124-give-it-five-minutes)
, not after giving it five years. So it's with great pleasure that I can announce
[we're dropping TypeScript](https://github.com/hotwired/turbo/pull/971)
from the next big release of Turbo 8.
The fact is that I actually rather like JavaScript. I'd go so far as to say it's my second favorite language after Ruby. Yes, a distant second, but a second none the less. This wasn't always the case. But after we got proper classes in JavaScript, and all the other improvements that flowed since ES6, it's become a real joy to write.
I still don't think JavaScript is well-suited for most of the work we do on the server side of the web-app equation, but fully respect and appreciate that others feel differently. To me, it's simply our good fortune that we now have such a capable JavaScript, which browsers are able to interpret without any need for a compiler at all.
TypeScript just gets in the way of that for me. Not just because it requires an explicit compile step, but because it pollutes the code with type gymnastics that add ever so little joy to my development experience, and quite frequently considerable grief. Things that should be easy become hard, and things that are hard become `any`. No thanks!
This isn't a plea to convert anyone of anything, though. As I discussed in
[Programming types and mindsets](https://world.hey.com/dhh/programming-types-and-mindsets-5b8490bc)
, very few programmers are typically interested in having their opinion on typing changed. Most programmers find themselves drawn strongly to typing or not quite early in their career, and then spend the rest of it rationalizing The Correct Choice to themselves and others.
That's part of the magic of this JavaScript v TypeScript dichotomy, and full credit to the TypeScript gang for realizing that a full take-over of JavaScript was never going to happen, so complete compatibility had to be baked in from the start. Just because Turbo 8 is dropping TypeScript won't mean you can't write your client code in it, or use any other library that employs it. We get to mix and match, which is wonderful.
It's also necessary. Because unlike languages like Ruby, which are languages of choice when it comes to the server side, JavaScript is a language of necessity when it comes to the client side. While you may compile dialects into it, you still have to accept the fact that running code in the browser means running JavaScript. So being able to write that, free of any tooling, and free of any strong typing, is a blessing under the circumstances.
So farewell, TypeScript. May you bring much rigor and satisfaction to your tribe while letting the rest of us enjoy JavaScript in the glorious spirit it was originally designed: Free of strong typing.
