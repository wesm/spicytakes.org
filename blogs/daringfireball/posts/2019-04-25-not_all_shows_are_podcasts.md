---
title: "All Podcasts Are Shows; Not All Shows Are Podcasts"
date: 2019-04-25
url: https://daringfireball.net/2019/04/not_all_shows_are_podcasts
slug: not_all_shows_are_podcasts
word_count: 1864
---


Ashley Carman, writing last week for The Verge [on the launch of Luminary, a $100 million venture-backed “podcast” startup](https://www.theverge.com/2019/4/22/18510897/luminary-podcast-app-launch-the-daily-gimlet-media-spotify):


> But the industry hasn’t accepted Luminary or its impending launch.
> When it rolls out to the public on iOS, Android, and the web,
> Luminary’s podcast app will be missing some of the industry’s
> biggest shows, including The New York Times’ The Daily and Gimlet
> Media shows like Reply All and Homecoming. Shows by Anchor’s
> network of smaller creators won’t be on the app, nor will series
> from Parcast, both of which are owned by Spotify.


The first thing to understand is that Luminary is two things: (1) an $8/month subscription service for *exclusive* original audio shows, from some very well-known people; (2) a podcast app for iOS and Android that you use to listen to Luminary’s own shows *and* any real podcast. You can use Luminary’s podcast player to listen to regular podcasts without subscribing to Luminary’s service.


Luminary’s own shows are ad-free, and they’re pitching the whole service [on the idea that ads suck](https://podcastbusinessjournal.com/luminary-does-a-belly-flop-on-twitter/).


A podcast, to me, is a series of audio episodes available over the web. At a technical level, it’s an RSS feed, and the RSS feed has entries for each episode, and each episode has links to the actual audio file (in MP3 or AAC format, but usually MP3) and other metadata. RSS is an open format that can be used to serialize anything. If you read Daring Fireball in a feed reader, that’s RSS. When using RSS for podcasts, effectively all podcasts use extensions to RSS created by Apple for iTunes and the iOS Podcasts app. [RSS is extensible](https://cyber.harvard.edu/rss/rss.html) to enable just such things. Apple, which embraced podcasts very early on and continues to be the overwhelmingly dominant player in the podcast client market, has never done anything — anything at all — to try to lock podcasts in to the iTunes ecosystem. Quite the opposite — their extensions to RSS are parsed by all podcast players on all platforms, and, most generously, the iTunes podcast directory is open to all podcast players on all platforms. It’s the de facto central database of all podcasts that meet Apple’s standards for content.


No one who listens to podcasts needs to know any of those details. The key is that if you make a podcast player, the only thing your app needs to know about any particular podcast is the URL to the RSS feed for the podcast. If you want to read a particular website, you can enter the URL for that website into any web browser. In the same way, if you want to listen or subscribe to a podcast, you can enter the URL for that podcast’s RSS feed into any podcast client. And all popular podcast players make it easy to search for podcasts by name so that you, the user, don’t have to know the URL or even know what a URL is.


Would a website be a “website” if it only worked in one company’s browser? No one has ever really tried that.1 It’s hard to imagine a world where, say, Apple News+ wasn’t in its own app but instead was something you viewed in Safari and only Safari. Nobody calls the content in Apple News a “website”.


So is a podcast a “podcast” if it only works in one app? I’m going to say no.


I don’t think there’s anything wrong with subscription-only audio content and proprietary apps. Sirius XM has been doing it forever. But nobody calls The Howard Stern Show a “podcast”. Audible has a ton of exclusive original shows and they don’t call them podcasts — they just call them “Audible Originals”.


Being client-agnostic is the spirit of the open internet, and I think it’s implicitly part of being a “podcast”. Openness was certainly part of [how podcasting came to be](https://en.wikipedia.org/wiki/History_of_podcasting).


This thing with Luminary is a bit rich. On the one side, their own original shows are proprietary and they promote them for being ad-free. On the other, they want to be a podcast player for all regular podcasts, many of which (and most of the ones produced as professional endeavors) are funded by advertising. This spat with The New York Times and Gimlet Media is fascinating because The Times’s The Daily and Gimlet’s shows are indisputably podcasts — their RSS feeds and MP3 files are available for anyone or any client to download over the open web. Luminary isn’t being blocked technically from playing them, they’re being blocked because The Times and Gimlet asked them to, and Luminary agreed to comply. So putting aside (for the moment) whether Luminary’s own original shows qualify as “podcasts”, as a podcast *player*, Luminary’s app is in the incredibly bizarre position of not playing several very popular podcasts that every other podcast player in the world can subscribe to and play.


Is that even a podcast player? If so, it needs an asterisk: “podcast* player”.


Dave Winer — who, as the creator of RSS itself *and* [a pioneer in what he originally called “audioblogging”](http://threads2.scripting.com/2013/april/howPodcastingGotItsName), ought to be considered an authority on the term — [has thoughts](https://twitter.com/davewiner/status/1121106121610149888):


> We need a new name for podcast-like things that have no feeds, are
> locked behind a paywall, can’t be archived, cited or shared, and
> don’t create any kind of record.
> Something like “Dead-end-cast.”
> Or “Business-model-cast.”
> Or “VC-friendly-cast.”


Luminary is not alone in trying to usurp the term “podcast” for proprietary audio shows. Spotify has been at it for a year, [trying to pivot from subscription *music* to subscription *audio*](https://9to5mac.com/2019/02/24/spotify-podcasts-arpu/). Spotify made a splash a few months ago [when it acquired the Gimlet and Anchor podcast networks](https://www.recode.net/2019/2/1/18207198/spotify-gimlet-podcast-acquisition) — but Gimlet’s and Anchor’s existing shows remain regular podcasts, available in any app. Yesterday [Spotify announced a “podcast” by Mark Zuckerberg](https://techcrunch.com/2019/04/24/mark-zuckerberg-has-a-podcast/) which is exclusive to Spotify. You don’t have to pay for it or anything, because no one would, but there is no feed for it. It is audio, it is on the internet, but I don’t think it’s a podcast. [Neither does Marco Arment](https://twitter.com/marcoarment/status/1121120291860766721) (who admittedly, as the maker of the very popular podcast player Overcast, has some skin in this game):


> What would you call a CD-lookalike music disc that was
> incompatible with over 90% of CD players?
> Probably couldn’t call it a CD, right?
> Until this shows up as a public RSS feed, this isn’t a podcast.
> (Also, Zuck’s still a turd.)


Basically, just like how an email is a message you read in your email client of choice, and a web page is an HTML document you load in your web browser of choice, a podcast is a show you listen to in your podcast player of choice.


We already have a word for these things: *shows*. All podcasts are shows on the internet, but not all shows on the internet are podcasts.


These companies are trying to usurp the word *podcast* for one simple reason: people love podcasts. What I think and hope they are missing is that part of what people love about podcasts is the openness. It’s one of the last remaining areas of the internet that works exactly as the internet was intended to work.


---


As a side note, I think the $100 million in venture capital that Luminary raised is going to be $100 million flushed down the toilet.


[From a month-ago company profile in The New York Times](https://www.nytimes.com/2019/03/03/business/media/luminary-media-podcast-app.html):


> Luminary has 70 employees in New York and Chicago, about 40 of
> whom are engineers. The company is beginning a marketing campaign
> on Monday that includes outdoor advertising in New York, Los
> Angeles and Austin, Tex.


I downloaded and kicked the tires on the Luminary app. It seems like a fine iOS podcast player. It has zero standout features though. 40 engineers seems cuckoo, not just for this podcast app but for any podcast app.


Next paragraph in that Times piece:


> To some degree, of course, all media start-ups think they are
> going to be the next Netflix. The test for Luminary will come in
> the execution.


The test is not in the execution. The test is whether it makes any sense at all to try to be the “Netflix of audio shows”.


Modeling themselves after Netflix is why Luminary’s app isn’t just a paywall for its own original content. Netflix is Netflix because of its strong original content *and* its massive, effectively infinite, catalog of *non-original* content. And — bonus! — Luminary gets their huge catalog of non-original content — real podcasts — “for free”. Neither of these analogies to Netflix works.


On the original content front, the huge difference is that podcast content is really easy and cheap to make compared to video. And the type of original content people really love on Netflix, shows like *Stranger Things*, is many orders of magnitude more expensive than any podcast.


On the non-original content front, the fact that Luminary is a regular podcast client doesn’t really help them much, because it only gives them access to content *any* app can offer. You can’t watch old episodes of *Friends* anywhere but Netflix, or by paying for episodes elsewhere. Netflix’s non-original content is not freely available on the web without resorting to piracy.


It might be a great idea to start a company to produce podcasts with celebrity  hosts like Lena Dunham, Russell Brand, Trevor Noah, and whomever else Luminary has signed. Those shows, if done well, could be hugely popular and make tons of money — from ads. But a company bringing that talent together does not need $100 million in funding and will never be worth 1/100th of Netflix.


## Postscript


Here’s an interesting update. A friend who doesn’t want to install the Luminary app (you have to give them an email address and create an account just to get past the first screen) asked whether Luminary allows you to add podcasts using their RSS feeds. The answer, as far as I can see, is no. The only way to listen to podcasts in Luminary is by searching for them by name — and pasting a feed URL in the search field doesn’t work.


That means you can’t use Luminary to listen to podcasts that are banned from iTunes for content, or private podcasts like [Relay’s members-only shows](https://www.relay.fm/membership). And, perhaps most obviously, you can’t use the RSS feed URL as a backdoor to listen to shows from The New York Times or Gimlet.


This is like a web browser not allowing you to just paste in a URL, allowing you only to get to pages through a search engine. Again I say: if Luminary’s app is a podcast player, it needs an asterisk.


---

1. Back in the ’90s Microsoft worked to get web developers to use technologies that only worked in Internet Explorer. The open web standards movement successfully fought against that. But that was an attempt at technical lock-in, not subscription content lock-in. ↩︎



| **Previous:** | [The Drumbeat of Impeachment](https://daringfireball.net/2019/04/the_drumbeat_of_impeachment) |
| **Next:** | [Bloomberg Shits the Bed Again on Cybersecurity](https://daringfireball.net/2019/05/bloomberg_shits_the_bed_again_on_cybersecurity) |


PreviousNext