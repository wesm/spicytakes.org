---
title: "The British Airways position on various border disputes"
date: 2025-05-05
url: https://drewdevault.com/2025/05/05/2025-05-05-BA-on-border-disputes.html
slug: 2025-05-05-BA-on-border-disputes
word_count: 962
---

My spouse and I are on vacation in Japan, spending half our time seeing the
sights and the other half working remotely and enjoying the experience of living
in a different place for a while. To get here, we flew on British Airways from
London to Tokyo, and I entertained myself on the long flight by browsing the
interactive flight map on the back of my neighbor’s seat and trying to figure
out how the poor developer who implemented this map solved the thorny problems
that displaying a world map implies.

I began my survey by poking through the whole interface of this little in-seat
entertainment system 1  to see if I can find out anything about who
made it or how it works – I was particularly curious to find a screen listing
open source licenses that such such devices often disclose. To my dismay I found
nothing at all – no information about who made it or what’s inside. I imagine
that there  *must*  be some open source software in that thing, but I didn’t find
any licenses or copyright statements.

When I turned my attention to the map itself, I did find one copyright
statement, the only one I could find in the whole UI. If you zoom in enough, it
switches from a satellite view to a street view showing the OpenStreetMap
copyright line:

Given that British Airways is the proud flag carrier of the United Kingdom I
assume that this is indeed the only off-the-shelf copyrighted material included
in this display, and everything else was developed in-house without relying on
any open source software that might require a disclosure of license and
copyright details. For similar reasons I am going to assume that all of the
borders shown in this map are reflective of the official opinion of British
Airways on various international disputes.

As I briefly mentioned a moment ago, this map has two views: satellite
photography and a very basic street view. Your plane and its route are shown in
real-time, and you can touch the screen to pan and zoom the map anywhere you
like. You can also rotate the map and change the angle in “3D” if you have
enough patience to use complex multitouch gestures on the cheapest touch panel
they could find.

The street view is very sparse and only appears when you’re pretty far zoomed
in, so it was mostly useless for this investigation. The satellite map,
thankfully, includes labels: cities, country names, points of interest, and,
importantly, national borders. The latter are very faint, however. Here’s an
illustrative example:

We also have our first peek at a border dispute here: look closely between the
“Georgia” and “Caucasus Mountains” labels. This ever-so-faint dotted line shows
what I believe is the Russian-occupied territory of South Ossetia in Georgia.
Disputes implicating Russia are not universally denoted as such – I took a peek
at the border with Ukraine and found that Ukraine is shown as whole and
undisputed, with its (undotted) border showing Donetsk, Luhansk, and Crimea
entirely within Ukraine’s borders.

Of course, I didn’t start at Russian border disputes when I went looking for
trouble. I went directly to Palestine. Or rather, I went to Israel, because
Palestine doesn’t exist on this map:

I squinted and looked very closely at the screen and I’m  *fairly*  certain that
both the West Bank and Gaza are outlined in these dotted lines using the borders
defined by the 1949 armistice. If you zoom in a bit more to the street view, you
can see labels like “West Bank” and the “Area A”, “Area B” labels of the Oslo
Accords:

Given that this is British Airways, part of me was surprised not to see the
whole area simply labelled Mandatory Palestine, but it is interesting to know
that British Airways officially supports the Oslo Accords.

Heading south, let’s take a look at the situation in Sudan:

This one is interesting – three areas within South Sudan’s claimed borders are
disputed, and the map only shows two with these dotted lines. The border dispute
with Sudan in the northeast is resolved in South Sudan’s favor. Another case
where BA takes a stand is Guyana, which has an ongoing dispute with Venezuela –
but the map  *only*  shows Guyana’s claim, albeit with a dotted line, rather than
the usual approach of drawing both claims with dotted lines.

Next, I turned my attention to Taiwan:

The cities of Taipei and Kaohsiung are labelled, but the island as a whole was
not labelled “Taiwan”. I zoomed and panned and 3D-zoomed the map all over the
place but was unable to get a “Taiwan” label to appear. I also zoomed into the
OSM-provided street map and panned that around but couldn’t find “Taiwan”
anywhere, either.

The last picture I took is of the Kashmir area:

I find these faint borders difficult to interpret and I admit to not being very
familiar with this conflict, but perhaps someone in the know with the patience
to look more closely will  [email me](mailto:drew@ddevault.org)  their
understanding of the official British Airways position on the Kashmir conflict
(here’s the  [full sized picture](https://redacted.moe/f/70bc3338.jpg) ).

Here are some other details I noted as I browsed the map:

* The Hala’ib Triangle and Bir Tawil are shown with dotted lines
* The Gulf of Mexico is labelled as such
* Antarctica has no labelled borders or settlements

After this thrilling survey of the official political positions of British
Airways, I spent the rest of the flight reading books or trying to sleep.

1. I believe the industry term is “infotainment system”, but if you ever catch me saying that with a straight face then I have been replaced with an imposter and you should contact the authorities. ↩︎
