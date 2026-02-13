---
title: "What is the Work of Dogs in this Country?"
date: 2001-05-05
url: https://www.joelonsoftware.com/2001/05/05/what-is-the-work-of-dogs-in-this-country/
word_count: 1730
---


How naive *were* we?


We had assumed that Bezos was just *reinvesting* the profits, that’s why they weren’t showing up on the bottom line.


Last year, about this time, the first big dotcom failures started to hit the news. Boo.com. Toysmart.com. The Get Big Fast mentality was not working. Five hundred 31-year-olds in Dockers discovered that just copying Jeff Bezos wasn’t a business plan.


The past few weeks have felt oddly quiet at Fog Creek. We’re finishing up CityDesk. I’d like to tell you all about CityDesk, but that will have to wait. I need to tell you about dog food.


Dog food?


Last month Sara Corbett told us about [the Lost Boys](http://www.nytimes.com/2001/04/01/magazine/01SUDAN.html?pagewanted=all), Sudanese refugees between 8 and 18 years old separated from their families and forced on a thousand mile march from Sudan, to Ethiopia, to Sudan, to Kenya. Half died on that trip, of hunger, thirst, alligators. A few of them were rescued and delivered to places like Fargo, North Dakota, in the middle of winter. “Are there lions in this bush?” one asked, riding in a car to his new home from the airport.


> Peter touched my shoulder. He was holding a can of Purina dog food. ”Excuse me, Sara, but can you tell me what this is?” Behind him, the pet food was stacked practically floor to ceiling. ”Um, that’s food for our dogs,” I answered, cringing at what that must sound like to a man who had spent the last eight years eating porridge. ”Ah, I see,” Peter said, replacing the can on the shelf and appearing satisfied. He pushed his grocery cart a few more steps and then turned again to face me, looking quizzical. ”Tell me,” he said, ”what is the work of dogs in this country?” [*New York Times Magazine, April 1, 2001*]


Dogs. Yes, Peter. Fargo has enough food, even for dogs.


It’s been a depressing year.


Oh, it started *out* so amusing, we all piled into B2B and B2C and P2P like a happy family getting in the Suburban for a Sunday outing to the Krispy Kreme Donut Shop. But wait, that’s not even the amusing part, the amusing part was watching the worst business plans fail, as their stock went from 316 to 3/16. Take that, new economy blabbermouths! Ah, the [schadenfreude](http://www.fuckedcompany.com/). Ah, the glee, when once again, Wired Magazine proves that as soon as it puts something on the cover, that thing will be proven to be stupid and wrong within a few short months.



|  |
| *Ooh, sorry, did you buy the Wired Index?* |



And with this New Economy thing, Wired *really* blew it, because they should have *known* by then what a death kiss their cover was for any technology or company or meme, after years of touting smell-o-rama and doomed game companies and how [PointCast was going to replace the web](http://www.wired.lycos.com/news/business/0,1367,35208,00.html), no, wait, PointCast *already* replaced the web, in March 1997.  But they tempted fate anyway, and didn’t just put the New Economy on the cover, they devoted the *whole goddamn issue* to [the New Economy](http://www.wired.com/wired/archive/5.07/), thus condemning the NASDAQ to plummet like a sheep learning to fly.


But joy at other’s misfortune can only entertain us for so long. Now it’s just getting depressing, and I know the economy is not *officially *in a depression, but I’m depressed, not because so many stupid startups went away, but because the zeitgeist is depressing. And now we have to eat dog food instead of Krispy Kremes.


Which is what we’re doing, because life goes on. Even though everybody’s walking around with their [chins glued to their chests](http://www.salon.com/tech/feature/2001/05/02/sacrifice/index.html), mourning about the *hours* they devoted, ruining their health and love lives for the sake of stock options in SockPuppet.com, life goes on. And the product development cycle must go on, and we at Fog Creek are getting towards the part in the product development cycle where you have to eat your own dog food. So for a while we’re Dog Creek Software.


Eating your own dog food is the quaint name that we in the computer industry give to the process of actually *using* your own product. I had forgotten how well it worked, until a month ago, I took home a build of CityDesk (thinking it was about 3 weeks from shipping) and tried to build a site with it.


Phew! There were a few bugs that literally made it impossible for me to proceed, so I had to fix those before I could even continue. All the testing we did, meticulously pulling down every menu and seeing if it worked right, didn’t uncover the showstoppers that made it impossible to do what the product was intended to allow. Trying to use the product, as a customer would, found these showstoppers in a minute.


And not just those. As I worked, not even exercising the features, just quietly trying to build a simple site, I found 45 bugs on one Sunday afternoon. And I am a lazy man, I couldn’t have spent more than 2 hours on this. I didn’t even try anything but the most basic functionality of the product.


Monday morning, when I got in to work, I gathered the team in the kitchen. I told them about the 45 bugs. (To be fair, many of these bugs weren’t actual defects but simply things that were not as convenient as they should have been). Then I suggested that everybody build at least one serious site using CityDesk to smoke out more bugs. That’s what is meant by eating your own dog food.


Here’s one example of the kind of things you find.


I expect that a lot of people will try to import existing web pages into CityDesk by copying and pasting HTML code. That works fine. But when I tried to import a real live page from the New York Times, I spent a whole day patiently editing the HTML, finding all the IMG links (referring to outside pictures), downloading the pictures from the web, importing those pictures into CityDesk, and adjusting the IMG links to refer to the internal pictures. It’s hard to believe, but one article on that web site contains about 65 IMG links referring to 35 different pictures, some of which are 1 pixel spacers which are very difficult to download using a web browser. And CityDesk has a funny compulsion to change the name of imported pictures internally into a canonical number, and it doesn’t even have a way to find out what that number is, so the long and the short of it was that it took me one full day to import a page into CityDesk.


It was getting a bit frustrating, so I went and weeded the garden for a while. (I don’t know *what *we’ll do to relieve stress when it’s all cleaned up. Thank God we can’t afford a landscaping service.) And that’s when it hit me. Hey, I’m a programmer! In the time it took me to import one page and adjust the pictures, I could write a subroutine that does it automatically! In fact, it probably took me *less* time to write the subroutine. Now importing a page takes about half a minute, instead of one day, and is basically error-free.


Wow.


That’s why you eat your own dog food.


And when Michael started importing some sites himself, he found about 10 bugs I had baked in by mistake. For example, we found web sites that use complicated names for pictures that cannot be converted to file names when you import them because they contain question marks, which are legal in URLs but not legal in file names.


Sometimes you download software and you just can’t believe how bad it is, or how hard it is to accomplish the very simple tasks that the software tries to accomplish. Chances are, it’s because the developers of the software don’t use it.


I have an even more amusing example of failing to eat dog food. Guess what email product was used internally at Juno Online Services? [If you’re just tuning in, I worked on the Juno client team for a few years].


Hmm, did you guess Juno? Since that was, uh, *our product*?


No. A couple of people, including the president, used Juno at home. The other 175 of us used Microsoft Outlook.


And for good reasons! The Juno client was just not such a great email client; for two years the only thing we worked on was better ways to show ads. A lot of us thought that if we *had to use the product*, we would have to make it better, if only to stop our own pain. The president was very insistent that we show popup ads at six different points in time, until he got home and got six popup ads, and said, “You know what? Maybe just two popups.”


AOL was signing up members at a furious rate, in part because it provided a *better user experience* than Juno, and we didn’t understand that, because we didn’t eat our own dog food. And we didn’t eat our own dog food, because it was disgusting, and management was sufficiently dysfunctional that we simply were not allowed to fix it, and at least make it tolerable to eat.


Anyway. CityDesk is starting to look a *lot* better. We’ve fixed all those bugs, found some more, and fixed them, too. We’re adding features we forgot about that became obviously necessary. And we’re getting closer to shipping! Hurrah! and thankfully, we no longer have to contend with 37 companies, each with $25 million in VC, competing against us by giving away their product for free in exchange for agreeing to have a big advertisement tattooed on your forehead. In the post-new economy, everybody is trying to figure out how much they can get away with charging. There’s nothing *wrong* with the post-new economy, if you’re smart. But all the endless news about the “dot coma” says more about the lack of creativity of business press editors than anything else. Sorry, fuckedcompany.com, it was funny for a month or so, now it’s just pathetic. We’ll focus on improving our product, and we’ll focus on staying in business, by listening to our customers and eating our own dog food, instead of flying all over the country trying to raise more venture capital.
