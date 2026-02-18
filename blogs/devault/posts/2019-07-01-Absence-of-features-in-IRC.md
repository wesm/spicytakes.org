---
title: "Absence of certain features in IRC considered a feature"
date: 2019-07-01
url: https://drewdevault.com/2019/07/01/Absence-of-features-in-IRC.html
slug: Absence-of-features-in-IRC
word_count: 1030
---

The other day a friend of mine (an oper on Freenode) wanted to talk about IRC
compared to its peers, such as Matrix, Slack, Discord, etc. The ensuing
discussion deserves summarization here. In short: I’m glad that IRC doesn’t have
the features that are “showstoppers” for people choosing other platforms, and
I’m worried that attempts to bring these showstopping “features” to IRC will
worsen the platform for the people who use it now.

On IRC, features like embedded images, a nice UX for messages longer than a few
lines (e.g. pasted code), threaded messages, etc; are absent. Some sort of
“graceful degradation” to support mixed channels with clients which support
these features and clients which don’t may be possible, but it still  *degrades* 
the experience for many people. By instead making everyone work within the
limitations of IRC, we establish a shared baseline, and expressing yourself
within these limitations is not only possible but makes a better experience for
everyone.

Remember that [not everyone is like you][old hardware]. I regularly chat with
people on ancient hardware that slows to a crawl when a web browser is
running 1 , or people working from a niche operating system for which porting a
graphical client is a herculean task, or people with accessibility concerns for
whom the “one line of text per statement” fits nicely into their TTS 2  system
and screenreading Slack is a nightmare.

Let’s consider what happens when these features are added but non-uniformly
available. Let’s use rich text as an example and examine the fallback
implementation. Which of these is better?

(A) <user> check out [this website]([[https://example.org](https://example.org)](https://example.org))

(B) <user> check out this website: [[https://example.org](https://example.org)](https://example.org)

Example B is what people naturally do when rich text is unavailable, and most
clients will recognize it as a link and make it clickable anyway. But many
clients cannot and will not display example A as a link, which makes it harder
to read. Example A also makes phishing  *much*  easier.

Here’s another example: how about a nice UI for long messages, such as pasted
code snippets? Let’s examine how three different clients would implement this:
(1) a GUI client, (2) a TUI 3  client, and (3) a client which refuses to
implement it or is unmaintained 4 .

The first case is the happy path, we probably get a little scrollbox that the
user can interact with their mouse. Let’s say  [Weechat](https://weechat.org/) 
takes up option 2, but how do they do that? Some terminal emulators have mouse
support, so they could have a similar box, but since Weechat is primarily
keyboard-driven (and some terminal emulators do not support mice!), a
keyboard-based alternative will be necessary. Now we have to have some kind of
command or keybinding for scrolling through the message, and picking which of
the last few long messages we want to scroll through. This will have to be
separate from scrolling through the backlog normally, of course. The third
option is the worst: they just see a hundred lines pasted into their backlog,
which is already highly scorned behavior on most IRC channels. Only the GUI
users come away from this happy, and on IRC they’re in the minority.

Some IRC clients (Matrix) have this feature today, but most Matrix users don’t
realize what a nuisance they’re being on the chat. Here’s what they see:

And here’s what I see:

Conservative improvements built on top of existing IRC norms, such as  [The
Lounge](https://thelounge.chat/) , are much better. Most people post images on
IRC as URLs, which clients can do a quick HEAD request against and embed if the
mimetype is appropriate:

For most of these features, I think that people who have and think they need
them are in fact unhappier for having them. What are some of the most common
complaints from Slack users et al? “It’s distracting.” “It’s hard to keep up
with what people said while I was away.” “Threads get too long and hard to
understand.” Does any of this sound familiar? Most of these problems are caused
by or exacerbated by features which are missing from IRC.  It’s distracting
because your colleagues are posting gifs all day. It’s hard to keep up with
because the infinite backlog encourages a culture of catching up rather than
setting the expectation that conversations are ephemeral 5 . Long conversations
shouldn’t be organized into threads, but moved into email or another medium more
suitable for that purpose.

None of this even considers what  *is*  good about IRC. It’s a series of
decentralized networks built on the shoulders of volunteers. It’s venerable and
well-supported with hundreds of client and server implementations. You can
connect to IRC manually using telnet and have a pretty good user experience!
Accordingly,  [a working IRC bot can be written in about 2
minutes](https://drewdevault.com/2018/03/10/How-to-write-an-IRC-bot.html) . No one is trying to monetize you on IRC.
It’s free, in both meanings, and nothing which has come since has presented a
compelling alternative. I’ve used IRC all day, every day for over ten years, and
that’s not even half of IRC’s lifetime. It’s outlived everything else by years
and years, and it’s not going anywhere soon.

In summary, I like IRC the way it is. It has problems which we ought to address,
but many people focus on the wrong problems. The culture that it fosters is good
and worth preserving, even at the expense of the features users of other
platforms demand - or those users themselves.

P.S. A friend pointed out that the migration of non-hackers away from IRC is
like a reverse  [Eternal September](https://en.wikipedia.org/wiki/Eternal_September) , which sounds  *great*  😉

1. Often, I *am* this person. ↩︎
2. Text to speech.
[old hardware]: [https://drewdevault.com/2019/01/23/Why-I-use-old-hardware.html](https://drewdevault.com/2019/01/23/Why-I-use-old-hardware.html) ↩︎
3. Text user interface ↩︎
4. IRC is over 30 years old and has barely changed since - so using unmaintained or barely-maintained clients is not entirely uncommon nor wrong. ↩︎
5. Many people have bouncers which allow them to catch up the last few lines, and keep logs which they can reference later if necessary. This is nice to have but adds enough friction to keep the expectation that discussions are ephemeral, which has a positive effect on IRC culture. ↩︎
