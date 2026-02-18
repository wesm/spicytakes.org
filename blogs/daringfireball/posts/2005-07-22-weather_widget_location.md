---
title: "Location Validation in the Dashboard Weather Widget"
date: 2005-07-22
url: https://daringfireball.net/2005/07/weather_widget_location
slug: weather_widget_location
word_count: 466
---


In my unofficial capacity as a [leading fan](http://daringfireball.net/2005/06/weather_widget_hacking) of Apple’s Weather
widget, I’ve received email from a slew of readers who say they’d like
to use the Weather widget, but can’t, because it shows them the
weather for some other city with the same name as theirs.


This problem is particularly acute for readers outside the U.S. — we
Americans can simply enter a postal Zip code rather than a city name.
In fact, the problem has led many residents of cities like London to
the mistaken conclusion that the Weather widget only works for U.S.
locations. Not so.


I’m pretty sure I know how to help, however. The trick is that after
you enter the name of your city in the Weather widget city name field,
*you have to hit the Return key*.1
Everyone who feels like they’re stuck with the weather for the wrong
city, I suspect, has simply typed the name of their city, then clicked
the Done button with the mouse.


Let’s say you live in Vancouver, British Columbia, for example.


If you just type “Vancouver” and then click Done, you’ll wind up
getting the weather for Vancouver, Washington. A lovely city, I’m
sure, but not the right weather for our Canadian friends.


But if you type Return after typing “Vancouver”, the widget will
validate your entry, and if it finds multiple cities matching that
name, it will prompt you to clarify your choice:


If you don’t use Return to invoke the widget’s input validation, it
seems to use whichever same-named city comes first in the list —
never giving you a hint that there might be other locations that match
the city name you’ve entered.


Needless to say, the confusion here is caused by a decidedly poor UI
design. The Weather widget provides absolutely no indication that you
need to hit return after typing your city name. And considering how
mouse-oriented the entire Dashboard UI is, it’s no surprise that many
people assume they just need to click the Done button after typing
their city name. And the Done button *has* to be clicked — which
means input validation has to be invoked by the keyboard, but
dismissing the configuration panel with the Done button has to be done
with the mouse. The right way to do something should be the obvious
way.


One of the core principles of UI design is that you should never allow
for invalid or ambiguous input. In the case of the Weather widget,
validation should happen as-you-type (*a la* [Google Suggest](http://www.google.com/webhp?complete=1&hl=en)),
and the Done button should only be enabled after the input field has
been validated.


---

1. Technically, you can use Return, Enter, or Tab to invoke validation. ↩︎



| **Previous:** | [About the Footnotes](https://daringfireball.net/2005/07/footnotes) |
| **Next:** | [Notes on Notes](https://daringfireball.net/2005/08/notes_on_notes) |


PreviousNext