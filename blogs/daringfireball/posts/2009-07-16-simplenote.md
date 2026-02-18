---
title: "Simplenote"
date: 2009-07-16
url: https://daringfireball.net/2009/07/simplenote
slug: simplenote
word_count: 1464
---


Back in November, I held up Apple’s own Notes app as a great example of iPhone software design. [I wrote](http://daringfireball.net/2008/11/iphone_likeness):


> I’ve looked at several note-editing apps available in the App
> Store, and most of them seem to have been designed without any
> recognition of just how clever and well-designed Apple’s Notes app
> is. Notes exposes its core functionality clearly and obviously,
> launches *very* quickly, requires very few taps to use, and uses
> just two simple levels of hierarchy (the flat list of notes, and
> the notes themselves).


But I noted three significant shortcomings:

1. Syncing
2. Search
3. Rotation


All three shortcomings were addressed in iPhone OS 3.0. In short, the updated version of Notes is emblematic of Apple’s steady, iterative approach to improving the iPhone — start with the basics, then add the most-requested new features over time. However, the one area I’m not satisfied by is syncing. Notes only sync via iTunes over USB, rather than over-the-air via MobileMe like calendars, contacts, and bookmarks. On the Mac, they sync to Apple Mail; on Windows, Outlook (which is part of Office, and therefore not free — Windows-using iPhone owners who don’t have Office can’t sync notes).


For me at least, over-the-air Internet syncing is an order of magnitude more appealing than USB or Bonjour syncing. For one thing, iPhone-to-iTunes USB syncing can be time consuming, especially when performing a backup. I often go several days without syncing my iPhone to iTunes. That means that if I were to use the built-in Notes app, my notes would only be in sync between my Mac and iPhone once or twice per week.


So I don’t use Notes. Since November, shortly after posting the aforementioned article, I’ve been using a splendid iPhone app called [Simplenote](http://simplenoteapp.com/). I’ve tried a slew of iPhone note editing apps, and not only is Simplenote my favorite, it might be my favorite third-party iPhone app, period. It’s that good.


First, unlike most of the other iPhone note apps I’ve tried, Simplenote shows an appreciation for just how good the built-in Notes app is. [Cloud Factory](http://www.cloud-factory.com/) (Simplenote’s developers) clearly studied what is good about Notes and thought about how to make something that is good in the same ways, but improves upon its major shortcomings.


Anyone who’s used the built-in Notes app will feel right at home in Simplenote. There are no folders, just a single, simple date-sorted list of notes. There are no fields associated with a note — just like with Apple’s, a note’s “title” is simply taken from the first line of the note. Simplenote launches quickly, offers full-text search, and supports horizontal screen rotation.


The list of all notes:


[
](https://daringfireball.net/misc/2009/07/simplenote-list.png)


An individual note:


[
](https://daringfireball.net/misc/2009/07/simplenote-note.png)


In short, Simplenote improves upon Notes in two significant ways:

1. Over-the-air syncing, which, in eight months of my use, works splendidly.
2. Helvetica.1


What Simplenote syncs to is [this simple web app](http://www.simplenoteapp.com/features/website.html), reminiscent in style and scope to the Mac app [Notational Velocity](http://notational.net/), which I wrote about [in a footnote](http://daringfireball.net/2009/02/untitled_document_syndrome#fn3-2009-02-20) to my “Untitled Document Syndrome” piece back in February. Several of the online-syncable iPhone note apps I’ve tried and discarded are designed to use existing web apps like Google Documents; but Google Documents offers all sorts of features and assumptions that don’t map well to a simple plain-text iPhone notes app. The Simplenote web and iPhone apps were designed to work with each other. They are of a piece.


The Simplenote web app is hosted on Google App Engine. In my eight months of using it, it has always been fast and syncing has been perfectly reliable. It just works.


## Regarding Basic Syncing Strategies


There are two main strategies for an iPhone app to sync data to your Mac or PC.


The first is direct client-to-client sync. iTunes’s USB syncing is an example of that. A third-party example is [Things](http://culturedcode.com/things/), from Cultured Code, which syncs directly between the iPhone and Mac version of Things over Wi-Fi. An example of an iPhone notes app that does this is Polar Bear Farm’s [Note Pad](http://www.polarbearfarm.com/notepad/index.html), which syncs to a native Mac and Windows desktop app named Sync, which Polar Bear Farm wrote specifically to serve as a syncing client for Note Pad.


The other strategy is to use a server on the Internet as a hub for syncing. That’s how MobileMe works, and that’s how Simplenote works.


There are several advantages to using a central web app/web service for syncing. One is that you can access your synced data from any computer with a web browser. Whereas with an app like Things, you can only access your data from your own Mac — and it must be a Mac, because there is no Windows client.


Another advantage for web-based syncing is that your data is always up to date everywhere, almost instantly. As with MobileMe, you don’t need to manually initiate a sync with Simplenote. When you launch it, Simplenote checks with the server for changes. When you make changes on the iPhone, they’re sent back to the server seconds later. The only way your data can get out of sync is if you make changes on the iPhone while there is no network available; in that case you simply need to relaunch Simplenote once network access is available.


With client-to-client syncing *a la* Things, you often need to initiate syncing manually. A scenario I’ve run into with Things is that I’ll jot a few shopping items using the Mac app, then, later on when I’m actually at the store, take out my iPhone and realize that I hadn’t synced. Every time you make changes, your data is out of sync until the next time you launch the iPhone and Mac clients together on the same Wi-Fi network.


The same goes for iTunes’s USB-based syncing for calendar events and contacts — if you don’t remember to manually initiate a sync (and wait for it to complete) before leaving the house, the data on your iPhone is out of date.


With Simplenote and MobileMe, so long as you have a network connection, your data is never out of sync.


To be clear, though, there are important trade-offs. The biggest downside to web-based syncing is the implicit lack of privacy. Your data resides on a server that someone else controls. I’m willing to accept this because the convenience is worth it, and the privacy issues with Simplenote are no different than with *any* web-based service. (It’s also worth pointing out that Simplenote uses HTTPS rather than regular HTTP, so network communication between the iPhone app and web site is encrypted. I would not use or recommend Simplenote if it didn’t use SSL to encrypt network traffic.)


With something like Things or Note Pad, your data exists only on your own machines. And with something like [OmniFocus](http://www.omnigroup.com/applications/omnifocus/), you can sync to your own WebDAV server, if you have one. It’s a trade-off between (a) convenience and universal access and (b) the privacy advantages of your data residing only on your own devices. (And even so, keeping your data private to your own machines is no panacea. Computers and phones — especially phones — get lost and stolen.)


## The Bottom Line


Amazingly, Simplenote costs just $2 — *including* ongoing access to the web app. On the one hand, yes, App Store prices tend to be very low, and Simplenote is very much competing against the free built-in Notes app from Apple. But when I bought Simplenote back in November, it cost $3, and I thought *that* price was crazy low.


What gives me pause about the low price is that I want Cloud Factory to thrive and for them to be able to maintain the web-based Simplenote component for the foreseeable future. The flawless syncing is central to Simplenote’s appeal. Yes, [Google App Engine hosting](http://code.google.com/appengine/docs/billing.html) is relatively inexpensive, and iPhone-sized text notes are by nature relatively *tiny* in terms of a service whose bandwidth quotas are measured in gigabytes, but Cloud Factory is only charging a one-time fee of $2. I’d feel better spending more — my thought back in November was that the low one-time fee was too good to be true.


On the other hand, though, the low price means there’s no reason not to try it. It’s hard for me to imagine how you could get more for $2 than you will by buying [Simplenote](http://simplenoteapp.com/).


---

1. Yes, there are [various](http://www.leancrew.com/all-this/2009/06/making-iphone-notes-look-better/) [workarounds](http://beausmith.com/blog/change-iphone-notes-font-to-helvetica.php) to get the iPhone’s built-in Notes app to use Helvetica. No, none of them are as nice as having the app just default to Helvetica like it should. ↩︎



| **Previous:** | [Putting What Little We Actually Know About Chrome OS Into Context](https://daringfireball.net/2009/07/chrome_os_context) |
| **Next:** | [Charging for Access to News Sites](https://daringfireball.net/2009/07/charging_for_access_to_news_sites) |


PreviousNext