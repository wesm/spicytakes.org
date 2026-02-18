---
title: "Push Pop Press"
date: 2011-02-01
url: https://daringfireball.net/2011/02/push_pop_press
slug: push_pop_press
word_count: 1244
---


My general policy is not to link to teaser sites, on the grounds that there’s plenty of stuff that’s actually shipping to write about and draw attention to. But, there are exceptions.


[Push Pop Press](http://www.pushpoppress.com/) is an exception.


Their teaser site, which opened today, offers this description:


> Our team is bringing together great content and beautiful software
> to create a new breed of digital books. Books that let you explore
> photos, videos, music, maps, and interactive graphics, all through
> a new physics-based multi-touch user interface.


Their team has a track record of creating excellent, boundary-pushing software: designer Mike Matas (whose work includes Delicious Library, and, at Apple, work on the original iOS), and engineers [Kimon Tsinteris](http://kimtsi.com/) and [Austin Sarner](http://www.austinsarner.com/). While both were at Apple, Tsinteris and Matas collaborated on the iOS Maps app.


Last week in San Francisco, I got a hands-on demo (from Matas) of what they’re working on. It’s amazing.


What I saw (and used) was a multimedia-rich book running on an iPhone 4. There is no UI chrome. No status bar at the top or tab bar at the bottom. It’s just like you see in the still image on their teaser site. The entire screen is filled by content, not user interface elements. The screen is the book, the book is the screen.


You use it almost entirely by swiping and pinching. Typically in iOS, when you play an embedded video, the screen fades to black as you switch to full-screen mode for the video. Then, when you’re done watching the video, you tap a blue “Done” button at the top left corner to go back, at which point the screen fades *from* black back to the previous layout. In Push Pop’s books, that’s not how it works. To play a video, you just tap play and it plays in place. If you want to play it full-screen, you pinch it out. Pinch back in to go back to the book layout. There is no fade-to-black stuff. The video, playing live, simply grows or shrinks as you pinch, on top on the page.


And, as they say, there’s a physics engine in place, which gives all the elements on screen a certain heft as you swipe and pinch them. It doesn’t just feel like a game — it feels like an exquisitely crafted game.


Performance is achingly smooth. E.g., when you zoom out or in on a video, the zooming tracks the pinching of your fingers precisely and instantly. Do the pinch fast — more like a popping pinch-flick — and the zoom expansion will respond accordingly and pop the element into full-screen size. Think about how the standard iOS list controls have a momentum-based feel to them — like when you flick them to scroll quickly, or the bounce when you hit the top or bottom. That’s what Push Pop’s UI feels like, except it’s for *everything* — page-turning, image/video zooming, everything.


The closest comparison I can think of is to Flipboard’s iPad app, but Push Pop Press’s UI feels smoother than Flipboard’s. (That could be because I only saw Push Pop’s stuff on an iPhone 4, whereas Flipboard only runs on the iPad. The iPhone 4 feels faster to me, in general, than the iPad.) Also, Flipboard lets you open and close elements via pinch gestures, but also has UI chrome for the same things — a literal “Close” button, for example, that performs the same action as pinching to close. Push Pop’s UI lacks such chrome. It’s nothing but content on screen, and nothing but gestures for interaction.


The format of their “books” is not HTML or anything like [ePub](http://en.wikipedia.org/wiki/EPUB) (the format [Apple uses](http://support.apple.com/kb/ht4168) for iBooks books). Push Pop’s books are native Cocoa Touch iOS apps.1 I’ve seen some cool stuff rendered through WebKit, but never anything like this in terms of smoothness, precision, and the lack of latency between touch gestures and on-screen responsiveness. “Pages” look more like they were laid-out by a designer than randomly rendered by a web browser.


The better visual layout, smoother and more show-offy interaction, and proprietary native-to-iOS format are more what I expected Apple’s e-book platform to be. This thing just begs for a gushing look-at-how-awesome-this-thing-is on-stage demo from Steve Jobs. I think Apple went with the wrong type of show-offy-ness with iBooks. Apple went in the direction of skeuomorphically aping the paper book — a spine, the outline of paper pages rendered on screen, animation that mimics paper page turning.


I find iBooks’s design to be distracting. It demos well, but grows tiresome quickly. In a paper book, there is one layer of “chrome” surrounding the content of the book — the physical boundaries and binding of the paper itself. In iBooks, there are *two* layers of chrome: the physical black bezel and metal frame of the device (iPhone, iPad, iPod Touch), and the virtual paper book rendered on screen. And the fake paper book in iBooks doesn’t even offer useful visual context — the stack of “remaining” pages visible under the current page never changes in thickness, offering no clue, as in a paper book, how far along in the book you are.


Amazon has taken a more content-focused approach with the Kindle. No fake paper boundaries rendered on screen, and the paging animation looks like screens moving, not sheets of paper turning. The content in a Kindle book, as rendered on any device — iPhone, iPad, or Kindle hardware — is surrounded almost only by the device hardware itself. But there’s no joy in the Kindle experience. No one looks at the Kindle app and says, “Wow”. But that’s exactly what you’re going to say when you first see a Push Pop Press book.


Kindle’s minimalism is perhaps appropriate for books like novels, which are entirely (or almost entirely) text. (They could certainly stand to vastly improve their typography, however.) I suspect that Push Pop Press’s platform would be overkill for a purely-text book like a novel. The demo book from Push Pop that I played with was, content-wise, more like a textbook or [Taschen](http://www.taschen.com/)-style coffee table book — chock full of photographs, illustrations, and movies. I can’t imagine reading a book like that on a Kindle device or even in the Kindle app on an iPad, and I don’t think iBooks is capable of it either.


Kindle and iBooks seem to have the goal of reproducing what is possible in paper books. Yes, iBooks supports embedded video and audio content, but it does so in a way that feels as though Apple pondered what it would be like if you could play video on a piece of paper. Push Pop’s concept strikes me as far more ambitious: What can we do with the idea of a “book” if we eliminate the limitations of ink and paper, rather than mimic them? E-books that aren’t merely rendered by software, but rather e-books that *are* software.


---

1. To that end, a Push Pop Press book will be sold as a standalone app in the App Store. It’s not the sort of platform like iBooks or Kindle where there is a single “player” app, and a store through which you populate that player app with book titles. Each title is its own app. ↩︎



| **Previous:** | [Oceania: We Have Always Required Books From the Eurasian E-Bookstore to Be Sold Through Our In-App Purchasing System](https://daringfireball.net/2011/02/oceania_in_app_purchases) |
| **Next:** | [The Verizon iPhone 4](https://daringfireball.net/2011/02/verizon_iphone_4) |


PreviousNext