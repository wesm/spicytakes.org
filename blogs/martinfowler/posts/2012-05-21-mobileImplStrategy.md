---
title: "Selecting a Mobile Implementation Strategy"
description: "The sudden and rapid explosion of mobile technology in the past five years offers huge opportunities. While it seems likely that a number of mobile platforms will continue to thrive, mobile customers "
date: 2012-05-21T00:00:00
tags: ["mobile"]
url: https://martinfowler.com/articles/mobileImplStrategy.html
slug: mobileImplStrategy
word_count: 4075
---


## Why does mobile matter?


Mobile is the new web: in 2000 businesses were realizing that the
future of commerce and customer relations was on the just-exploding
web. In a few years time, web commerce had eclipsed traditional
off-line commerce. Mobile commerce is currently a fraction of web
commerce. But in a few years time it will, in turn, eclipse
traditional web commerce.


Businesses, large and small, know this and are planning products to
prepare for and exploit the oncoming tide of mobile use. These products
are innovative and engaging. In fact, most businesses are planning
products that are still waiting for mobile technology to catch-up.


Because the explosion of mobile is for a good reason. People prefer
the engagement and immediacy of mobiles. Mobiles fit into a person's
lifestyle, moving with them, rather than demanding people meet them on
the technology's terms. And in this change are new opportunities, well
beyond selling the same things through a new channel.


However, the mobile market is fractured across several platforms. It
is no longer enough to have great product ideas. You must also have a
plan to implement these ideas. Your planning will need to take into
account a number of different factors. But to start, which is more
important, experience or platform coverage?


## Why Experience Matters


Over the last ten years, through the ascendency of the web,
advertising has been the accepted wisdom in sales. This has been
accurate and effective. The web has been an enormous morass of direct
connections and disintermediation. And while this is great for
consumers — to a degree — it has relied on vendors
finding a way to get their names in front of those consumers. The
result has been an arms-race of more targetted and more intrusive
advertising.


Mobile asks a question:


> If my store is your favorite store and it's always in your
> pocket, why do I need to know what you had for dinner last
> night?


That is, a high quality experience will draw customers and keep
them. After all, shopping is a leisure activity. Once kept, specific
tracking to advertise to these customers is less necessary. But,
maintaining a leading-edge user experience *is* necessary, because
that is what mobile customers are following.


The last five years of mobile explosion has been a story of a steady
increase in the fideility of user experience. Apple has established a
strong position in the mobile market almost exclusively based upon
providing a higher quality experience. In turn, app developers across
platforms have aimed to meet or exceed the higher expectations of
mobile users.


It is particularly telling that Microsoft's late entry in the mobile
world with Windows Phone 7 is attempting to gain market position
primarily by bettering Apple's iOS experience. They certainly appear
to have bettered Apple, but is it too little, too late?


## An Opening Gambit


While experience may be a prime goal, there are up to four or five
distinct mobile platforms that need to be considered: iOS, Android,
BlackBerry, Windows Phone 7 and Mobile Web. If more than one or two of
those platforms matter to you, delivering a high-fidelity experience
across all of those would be an extraordinarly expensive and lengthy
operation. That's not to say that a great experience across all
platforms that matter is not worth aiming for. Rather than trying to
get there immediately, treat this as a goal.


Instead, think about what your first move into mobile should be. A
first move will involve some degree of trade-off between platform
coverage and the fidelity of the experience. The nature of your app,
your business, your users and the market-place will guide you as to
what the trade-off should be. Given all these constraints, your
choices range across a number of options between supporting a single
platform with an ultra-high-fidelity experience and supporting all
platforms with a bare bones experience.


For convenience we name the two extremes the Laser strategy and the
Cover-Your-Bases strategy.


It is important to remember that the trade-off between platform
coverage and fidelity of experience only constitutes your opening
gambit when moving into the mobile space. Mobile apps and strategy
will evolve. Whatever position you start in, over time you will be
able to evolve towards the âZone of Awesomeâ where every platform is
supported with a high-fidelity user experience. But the techniques you
can use to evolve your app will vary based on which strategy you have
chosen for your opening gambit.


You will have to choose between these strategies and this choice will
affect your app for the first two years or so of its life. It is
important to be intentional about the decision, to understand what
strengths and weaknesses the strategies have and what the evolution
paths for each strategy might look like.


## The Laser Strategy


The Laser strategy is to focus on a small set of features and just one
platform, but with a very polished and immersive user experience. You
would follow this strategy when experience is key to your app or
product. Often, the app would substantially be the product.


For example, your goal may be to provide a substantially new
approach to shopping for flights, as [Hipmunk](http://www.hipmunk.com) has. Or your app may be
attempting to reach a very specific niche of customers who might be
heavily design-influenced, as is the case with [Instagram](http://instagr.am).


Either way, experience is king. Select one platform and build a
very high fidelity experience app on just this platform.


### Evolution


One obvious option is to evolve horizontally: port the app to
another mobile platform. Adding another platform will see both build
and maintenance costs increase as a new development team is started
alongside the existing development team. At the end of the porting
effort, a new platform is supported, but no new features are
introduced: essentially, you're just getting the same app again. In
addition to missing out on a chance to expand the scope of your
product, the real loss is the opportunity to learn from and adapt the
feature set of your product.


An alternative approach is to use a new platform as an opportunity
to explore new product and feature ideas. This may result in a
different feature set with a lower fidelity experience. If the new
features are successful, these could be incorporated back into the
original app.


There is a specific evolution of the Laser strategy that we refer
to as Embracing the Differences. But before diving into more detail on
this approach, I would like to contrast the Laser strategy with a
strategy from the other extreme: Cover-Your-Bases.


## The Cover-your-bases Strategy


The Cover-Your-Bases strategy is to focus on building a lower
fidelity app across many, if not all, of the mobile platforms. This
app would provide a consistent feature set and experience across all
platforms. This strategy is most suitable when you already have a
large user base and the app would be a new channel to access your
existing product.


Due to your existing user base, what's most important is to get the
new channel in front of as many users as possible. Clearly, platform
coverage is king. However, as this is mobile, experience is still very
important. Instead of providing a degraded experience, provide a
simplified experience with a minimal feature set.


### Evolution


Evolution of this strategy is much more straight-forward than with the
Laser strategy. Evolve your app vertically by increasing the quality
of experience of the app across all platforms. There are two things to
consider, however.


Firstly, some platforms are simply more valuable than others. Find the
platforms that are most important to your product and users, and focus
your efforts there. Allow the experience on these platforms to creep
— or leap — ahead of the others.


Secondly, a Cover-Your-Bases strategy assumes some form of
cross-platform technology. Cross-platform frameworks and the like work
by offering a lowest-common denominator approach. This makes app
development consistent, but it places a ceiling on the quality of the
experience you can provide. It is important to consider this ceiling
when selecting a cross-platform toolkit, is the ceiling high enough
for your use? Is there a way to break through the ceiling, at least on
your most valuable platform? Without considering these questions, you
may discover that in a year or so you will be re-writing your app from
scratch.


An evolutionary strategy, known as Leverage the Similarity, can be
very effective when embarking down the Cover-Your-Bases
strategy. Before going into detail on this, I would like to return to
the evolutionary approach for the Laser strategy: embrace the
differences.


## Embrace the Differences


Once you have decided that the Laser strategy is your best opening
gambit, one approach to evolve from there to expanded platform
coverage is by embracing the differences between the platforms. Each
mobile platform and channel has different interaction patterns and
trends of use. Mobile embeds itself into people's lives, so while you
may offer the same product as an app to both iPhone and iPad users,
the different circumstances in which an iPad is used means that the
app will effectively be a different product to the user.


Rather than trying to pretend all platforms are basically the same,
exploit these differences as a means to experimenting with and
expanding the feature set of your app.


Consider Instagram, recently purchased by Facebook. They grew very
effectively with just an iPhone app, and two features: apply vintage
filters to your photos and share these with your friends. They are a
canonical example of the Laser strategy; to the point where they did
not even have a desktop web site.


Throughout their growth on iPhone, the repeated question was when
would they launch an Android app? The unspoken assumption was that
Instagram's best path to an even larger market share was to release an
equivalent Android app. But Instagram's market share wasn't a
problem. They were exploding faster than they could deal with. Their
problem was they actually had no idea how to capitalise on the value
of the huge user base and social network they had built.


For example, a regular Instagram user could only interact with their
social network using their iPhone. The iPhone interaction model is
built around pushing out a photo, or quickly dipping in to see what's
happening right now. It is not a good model for browsing, or exploring
deeper. If an Instagram user starts following another user, they can't
comfortably browse through that user's old photos. It's also
inconvenient to follow links from that new user: which photos do they
like, who else do they follow?


These are all tasks better suited to the, now unfashionable, desktop
web or, perhaps, a tablet.


Though Instagram did end up building an Android app — a direct
port of their iPhone app — there was another route they could
have taken.

1. Build a desktop web application to allow existing Instagram users
   to explore their social network. This would largely be a read-only
   app, except it would allow users to expand their social
   network. It's most compelling feature would have been various slide
   shows of already published photos.
   
   This desktop web application would have then offered a new feature
   that the iPhone app did not provide. Additionally, it would have
   encouraged their existing user base to flesh out their nascent
   social network, and reached out to other mobile users in a small
   degree by at least allowing them to browse the world of Instagram.
   
   The additional cost to Instagram of this step would have been
   minimal. It is a new platform to support, however it is a platform
   with readily and widely available skills. It is highly likely that
   the existing Instagram developers could have taken on this platform
   without any noticeable lag.
2. Tweak the desktop web application to be a first-class iPad
   experience. For a small amount of work, they would then have had a
   very high-experience app on a new platform with new features.
3. Take this iPad web app, and use a hybrid approach to embed this app
   within a native iPad application. Incorporate the existing iPhone
   photo sharing code to provide a native iPad app with a combination
   of the social network exploration and original photo sharing
   features.
   
   At this point, Instagram has expanded both their platform coverage
   and their feature set. They have done this in a way that allows
   them to correct for errors in direction quickly, and in a series of
   small steps that allowed them to maintain the high quality
   experience that has helped make them famous.


As I said above, Instagram did actually end up releasing an Android
app, rather than following this strategy. However, Instagram's
purchase by Facebook could be viewed as a variant on this approach. It
will be interesting to watch where they go next. While they are now
part of the world's biggest social network, Facebook has promised to
allow them to continue to operate independently. The obvious next move
would be augment their limited social networking features with the
might of Facebook.


This worked example is just that: an example. But it is quite
illustrative of the sort of alternatives that exist when opening with
the Laser strategy, beyond porting the same app to other platforms. A
hybrid web approach featured very strongly in this example. It is
expected that a hybrid web approach would feature strongly in many
evolutions of the Laser strategy, it's important to be careful if a
step needs to be taken that would rule this out as an option.


## Leverage the Similarity


Similarly to how embracing the differences is a powerful way to
evolve from a Laser strategy opening gambit, leveraging the
similarities between platforms can be an effective method of evolving
from a Cover-Your-Bases strategy. If you have chosen the
Cover-Your-Bases strategy, platform coverage is your primary goal
— meaning that as new features are introduced these new features
should be available over all the supported platforms.


But this is mobile, and user experience is critically
important. While the opening gambit may allow a bare-bones experience,
over time this experience should improve. Where the Laser strategy
evolved roughly horizontally, the Cover-Your-Bases strategy will
evolve roughly vertically. The only variation will be that as it is
determined which platforms are of the highest value, effort should be
made to accelerate the user experience on these platforms.


While a hybrid web approach could assist in evolving a Laser
strategy, we'd expect it to be foundational to any Cover-Your-Bases
strategy.


For this strategy, I'd like you to consider the example of [DemocracyNow!](http://www.democracynow.org/), a global TV and
radio news program operated out of New York and broadcasting over the
web. The goal of DemocracyNow!  has been to reach as many potential
listeners and viewers as possible. To achieve this, DemocracyNow!
realised that it is important to offer mechanisms that suit the
listeners and viewers, and hence they have started building mobile
apps. A mobile app should make it easy to watch a DemocracyNow!
program on a morning commute.


DemocracyNow! decided to tackle this by building a mobile web app. As
well as providing high-quality platform coverage, this also provides
some ability to deal with an experience glass ceiling that they may
run into. For example, given that DemocracyNow! episodes can be quite
substantial video files, how do you allow a viewer to download these
to be watched later? HTML5 does provide offline storage, but the
capacity is quite limited, and web pages have limited abilities to run
background download processes.


In this case, the experience requirements are not for a high quality
user interface.


This situation is very suited to a hybrid approach. Take the
DemocracyNow! web app and embed it in a native app. The native portion
of the app can then download videos in the background and make them
available to the HTML5 UI. This is a particularly powerful approach as
not only does HTML5 provide a very high quality experience on iOS and
Android devices, it can also degrade very gracefully on lower quality
devices, such as BlackBerry and Windows Phone 7.


Switching to a hybrid approach like this is an effective way to break
through the experience glass ceiling inherent in a cross-platform
approach. In truely sophisticated hybrid approaches, as well as
allowing background access to native device features, it would be
possible to alternate between cross-platform and native UIs. Preparing
for this does require careful consideration of the hybrid approach
selected. HTML5 has much to recommend it.


## Guiding Principles and Philosophy


At the core, there are only a small set of principles that guide
the selection of a mobile strategy. First, and foremost, we recommend
following the ideas coming out of the [Lean Startup](http://www.startuplessonslearned.com/)
movement. This movement encourages an obsessive focus on defining and
developing only the minimum required feature set. Mobile offers a
unique opportunity here. While mainline web development at most big
companies has grown into a huge organisation with a life and goals
unto itself, mobile is often started as a much smaller sibling. Over
time, it will of course grow. But while it is easy and people may not
be watching closely, trying running mobile development as a
startup.


The intention behind using startup ideas is that by releasing early
you'll learn more quickly what your product should actually
be. Learning is a critical principle. Mobile is new, the platforms are
evolving rapidly and people's relationship with mobile is evolving as
well. This means there will be many opportunities, but you will need
to be learning and moving fast to take advantage of them.


As mentioned earlier, there are advantages to choosing technologies
that are more open. Typically, open technologies will be less likely
to restrict your future movements. This is because an open technology
can be supported by multiple vendors. Each vendor may have a slightly
different take on where the technology should go. Switching between
vendors while using the same technology is significantly less
painful. More specifically, prefer the web and web technologies. As
well as being open it has the greatest degree of vendor support ever
seen.


Finally, avoid thinking in terms of releases of your app. That is,
rather than bundling together several features and a platform launch,
think in terms of the features and plan to release these
independently. While, for marketing reasons, you may choose to batch
features up, that should remain a choice entirely independent of
technology and implementation. Separating features from releases will
also allow you to move platform support independently.


## Dimensions to Measure


While we believe that user experience and platform coverage are the
two key dimensions to use when determining your mobile implementation
strategy there are numerous other variables to consider.


### You

- **Lifespan/lifecycle**: How often will you be going through the app
  development process? How long is the app intended to last? Will it
  be quite quickly replaced? A short-lived app would be better suited
  to a Laser strategy: if the app is not to be maintained, a quickly
  developed single-platform app could be most appropriate.
- **Budget**: you've decided to build an app, so clearly you can
  afford something, but how many updates can you afford? If your
  budget stretches to a release, but not many updates, then a Laser
  strategy would allow you to focus on the high value platforms
  effectively, with only a small number of releases.
- **Existing systems and in-house skills**: Do you have a large set of
  existing in-house systems that any app will have to be integated
  with? What are your available in-house skills for development? Do
  you have a large pool of Java developers keen to be re-trained? If
  you have large and complex existing systems, a mobile app is
  probably a new channel onto your existing product. Additionally,
  re-training your in-house skills will take a few releases to pay
  off. The Cover-Your-Bases strategy is likely suitable.


### Your Users

- **Who are they?** What drives them? What are their demographics?
  Their relationships with mobile technology? A narrowly focussed user
  base could be targetted well with a Laser strategy, while if your
  user base is broad your best bet is to attempt to reach as many as
  possible with Cover-Your-Bases.
- **What is the competition doing?** It is generally a bad idea to be
  responding to your competition but if mobile or user-experience is
  one of your key differentiators, it is important to be aware.
- **Marketing buzz**: Is the intent to create marketing buzz around
  this app? Will the buzz be for the app itself, or will it be an
  exercise to create brand buzz? A brand building exercise could go a
  couple of ways: if the app is intended to contribute to and expand
  your brand, then you should move quickly. However, if the app is to
  become a brand in itself, then the quality and long-term evolution
  are significantly more important.


### The App

- **Nature**: Is the app part of a branding exercise? Part of a
  competition? Something your users will use occasionally, or intended
  to be a long-lived workhorse that will substantially replace your
  customers existing communication channels with your product.
- **B2[ECB]**: Is it a business to employee, customer or business
  app? Each of these will have substantially different interaction
  models. The accepted wisdom is that employees will tolerate a much
  lower-quality experience. However, this is changing. As mobile has
  raised consumers' expectations of experience, it has also raised
  employees expectations. With the advent of bring-your-own-device it
  is no longer enough to regard your employees as a captive audience.
- **Native device features**: What degree of access to native device
  features does your app require?


## How do you make this happen?


This article has described the Laser and Cover-Your-Bases
strategies and how those strategies may evolve into a long-term,
viable mobile strategy, but how do you actually make any of this
happen?


Executing any implementation strategy involves decisions about
organisational structure and technical selection. For this article I
will be leaving the technical selection aside for now, other than to
say, as mentioned, above that hybrid web approaches have a lot of
potential.


### Making Laser Happen


If you have decided to follow a strategy close to the Laser strategy,
the development organisation should reflect this. The most important
aspect here is to set aside any notion of maintaining feature and
experience parity. Instead, allow each platform to evolve at a
different rate.


### Making Cover-Your-Bases Happen


When it comes to arranging your development organization for
delivering a mobile app, the primary goal will be to be able to grow
the feature-set and experience across all platforms. The best way to
achieve this is to develop and deliver features independently of each
other: arrange 'Y'-shaped feature teams responsibile for end-to-end
development of new features across all mobile platforms, and back-end
systems. The 'stem' of the Y develops any back-end and application
logic changes, and then the arms split to deliver the feature into the
various mobile platforms. A feature team arrangement like this will
allow the teams flexiblility to deliver the best experience possible
for each platform.


## Conclusion


In the end, everyone knows that mobile is the wave of the future. The
three biggest companies in technology are fighting over it right
now. But unlike the web before it, mobile is making user experience
*matter*. And it matters to the point where it could substantially
change the shape of online commerce. It is a rare business that can
safely ignore this for long.


However, mobile is also fragmented. And given the cost of building a
high quality user experience, how do you deal with this? Expect to
have to trade platform coverage and user experience off against each
other, at least initially. Over time you will be able to evolve to
provide a quality experience across a large number of platforms. But
to get here efficiently you will need to be intentional in how you
select your mobile implementation strategy.


Imagine how your app or product may evolve, prepare for the most
likely evolutionary paths. And pay especially close attention to what
HTML5 and mobile web technology can offer you.


Finally, take advantage of how new mobile is. Can you run your
mobile development group as a lean startup? Can you build a culture of
rapid pace and learning into this group? And then prepare your
development teams for this exciting new world.


---
