---
title: "The world's stupidest IRC bot"
date: 2021-03-29
url: https://drewdevault.com/2021/03/29/The-worlds-dumbest-IRC-bot.html
slug: The-worlds-dumbest-IRC-bot
word_count: 858
---

I’m an  [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat)  power user,
having been hanging out in 200+ channels on 10+ networks 24/7 for the past 10
years or so. Because IRC is
 [standardized](https://tools.ietf.org/html/rfc2812)  and simple, a common
pastime for IRC enthusiasts is the creation of bots. In one of the social
channels I hang out in, we’ve spent the past 6 years gradually building the
world’s stupidest IRC bot: wormy.

For a start, wormy is highly schizophrenic. Though it presents itself as a
single bot, it is in fact a
 [bouncer](https://en.wikipedia.org/wiki/BNC_(software))  which combines the
connections of 7 independent bots. At one point, this number was higher —
as many as 11 — but some bots were consolidated.

```
<@sircmpwn> .bots
<wormy> Serving text/html since 2017, yours truly ["ps"] For a list of commands, try `.help`
<wormy> minus' parcel tracking bot r10.b563abc (built on 2020-06-06T12:02:13Z, https://git.sr.ht/~minus/parcel-tracking-bot)
<wormy> minus' dice bot r16.498a0b8 (built on 2020-02-04T20:16:14Z, https://git.sr.ht/~minus/dice-irc-bot)
<wormy> Featuring arbitrary code execution by design and buffer overflows by mistake, jsbot checking in
<wormy> Radiobot coming to you live from The Internet, taking listener requests at 1-800-GUD-SONGS
<wormy> urlbot: live streaming moe directly to your eyeballs
<wormy> o/ SirCmpwn made me so he wouldn't forget shit so much
```

These bots provide a variety of features for channel members, such as checking
tracking numbers for parcels out for delivery, requesting songs for our private
internet radio, reading out the mimetypes and titles of URLs mentioned in the
channel, or feeding queries into Wolfram Alpha.

```
<wormy> Now playing: 8369492 小さき者への贖罪の為のソナタ  by ALI PROJECT from 禁書 (4m42s FLAC)
<wormy> Now playing: 1045361 アキノサクラ by Wakana from magic moment (5m0s FLAC) #live ♥ minus
<wormy> Now playing: d0b1cb3 Forevermore by F from Cafe de Touhou 3 (4m9s FLAC) ♥ hummer12007
<wormy> Now playing: 0911e90 Moeru San Shimai by Iwasaki Taku from Tengen Toppa Gurren Lagann Original Soundtrack - CD01 (3m3s FLAC)
<wormy> Now playing: ac1a17e rebellion anthem by Yousei teikoku from rebellion anthem (5m15s MP3) ♥ minus
<wormy> Now playing: a5ab39a Desirable Dream by GET IN THE RING from Aki-秋- (4m38s FLAC) ♥ minus
```

Things really took off with the introduction of a truly stupid bot last year:
 [jsbot](https://git.sr.ht/~sircmpwn/jsbot) . This bot adds a  `.js`  command which
executes arbitrary JavaScript (using Fabrice Bellard’s
 [quickjs](https://bellard.org/quickjs/) ) expressions, and sending their
stringified result to the channel.

```
<@sircmpwn> .js Array(16).join("wat" - 1) + " Batman!"
<wormy> => NaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaN Batman!
```

We soon realized, however, that what we had effectively created was a persistent
JavaScript environment which was connected to IRC. This has made it possible to
write even more IRC bots in the least practical manner imaginable: by writing
JavaScript statements, one line at a time, into IRC messages, and hoping it
works.

This has not been an entirely smart move.

One “feature”, inspired by  [Bryan
Cantrill](https://www.youtube.com/watch?v=30jNsCVLpAE) , records every time the
word “fuck” is used in the channel. Then, whenever anyone says “wtf”, the bot
helpfully offers up an example of the usage of the word “fuck” by printing one
of the recorded messages. Here’s how it was made:

```
<sircmpwn> .js let wtf = [];
<wormy>  => undefined
<sircmpwn> .js on(/fuck/, msg => wtf.push(msg.text))
<wormy>  => 25
<sircmpwn> .js on(/^what the fuck$/, msg => msg.reply(wtf[Math.floor(Math.random() * wtf.length)]))
<wormy>  => 26
```

Here’s one which records whenever someone says “foo++” or “foo--” and keeps
track of scores:

```
.js on(/^([a-zA-Z0-9_]+)(\+\+|--)$/, (msg, thing, op) => { if (typeof scores[thing] === "undefined") scores[thing] = 0; scores[thing] += op === "++" ? 1 : -1; msg.reply(`${thing}: ${scores[thing]}`) });
.js on(/\.score (.*)/, (msg, item) => msg.reply(scores[item]));
.js let worst = () => Object.entries(scores).sort((a, b) => a[1] - b[1]).slice(0, 5).map(s => `${s[0]}: ${s[1]}`).join(", ");
.js let best = () => Object.entries(scores).sort((a, b) => b[1] - a[1]).slice(0, 5).map(s => `${s[0]}: ${s[1]}`).join(", ");
.js on(/^.worst$/, msg => msg.reply(worst()));
.js on(/^.best$/, msg => msg.reply(best()));
```

Other “features” written in horrible one-liners include SI unit conversions,
rewriting undesirable URLs (e.g. m.wikipedia.org => en.wikipedia.org), answering
“wormy you piece of shit” with “¯\_(ツ)_/¯”, and giving the obvious response to
“make me a sandwich”.

Eventually it occurred to us that we had two dozen stupid IRC bots storing not
only their state, but their code, in a single long-lived process on some server.
For a while, the answer to this was adding “don’t reboot this server kthx” to
the MotD, but eventually we did some magic nonsense to make certain variables
persistent:

```
let persistent = {};
function writePersistent() {
  let fd = std.open("persist.json", "w");
  fd.puts(JSON.stringify(persistent));
  fd.close();
}

let persist_handler = {
  set: (obj, prop, val) => {
    obj[prop] = val;
    writePersistent();
  },
};

let p = std.loadFile("persist.json");
if (p !== null) {
  persistent = JSON.parse(p);
  Object.keys(persistent).map(key => {
    let proxy = new Proxy(persistent[key], persist_handler);
    persistent[key] = proxy;
    exports[key] = proxy;
  });
}

exports.persist = (name, obj) => {
  let proxy = new Proxy(obj, persist_handler);
  persistent[name] = proxy;
  writePersistent();
  return proxy;
};
```

Anyway, there’s no moral to this story. We just have a silly IRC bot and I
thought I’d share that with you. If you want a stupid IRC bot for your own
channel,  [jsbot](https://git.sr.ht/~sircmpwn/jsbot)  is available on sourcehut. I
highly disrecommend it and disavow any responsibility for the consequences.
