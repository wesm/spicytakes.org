---
title: "Time Zone Uncertainty"
description: "I was in Boston, about to fly out to our office in Calgary. I 	look at my calendar to see if I have a meeting. First one is at 	10.30am - cool no need to rush out of bed in the morning."
date: 2007-09-06T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/TimeZoneUncertainty.html
slug: TimeZoneUncertainty
word_count: 800
---


I was in Boston, about to fly out to our office in Calgary. I
	look at my calendar to see if I have a meeting. First one is at
	10.30am - cool no need to rush out of bed in the morning.


I turn up and am two hours late. What happened was that I was
	invited to the meeting that begun at 8.30am Calgary time. Lotus
	Notes saw my computer was set to Boston time, and helpfully
	converted the time zones for the two hour shift.


You could argue that this was my fault for not paying
	attention. After all I know this is how Notes works and was being
	careless when I read my diary. I don't buy this, Donald Norman noted
	a while ago that we tend to blame ourselves for errors that are due to
	bad usability - like a door with a handle that you should push.


Even though I'm now avoiding Notes calendars, I get the same
  basic problem with Mac's ical, google calendar, and my phone. I'm
  in Boston and arrange a meeting for 10am in London. I go to
  London. My inclination is to shift my laptop time zone to where I am
  - that way the clock makes sense. But if I do that this appointment
  time moves. All of these devices are trying to be clever with time
  zones - and I end up not sure what I'm looking at.


Time zones are particularly vulnerable to this kind of problem
	It's most notably a problem in calendaring
	applications, but you see this issue in enterprise software as
	well. There is a temptation to try to be clever with handling time
	zones, but this temptation leads to trouble if the software isn't
	quite clever enough, which is what happened in this case.


I'd prefer Notes ignore time zones completely. You set the time
	for the place the meeting occurs in and that's what it should show
	you. Who cares about the time zones? It's only the time on the
	ground that usually matters. When I look at my calendar for a day in
	Calgary, I want to see the Calgary times for that day - wherever I
	happen to be when I'm looking at it.


The exception, of course, is a phone meeting that spans time
zones. But here you should do something exceptional for a phone
meeting rather than complicate handling a physical one. It could be
something that allows you to set a flag for a phone meeting, and then
you get a different time display. Or it could be as simple as just
allowing you to put the timezone on the time display, and leaving the
conversion to the reader. With phone meetings you think more about
time-zones than you do for physical meetings (or at least I do).


The important lesson here is to make the most common case
	(physical meetings) simple and only do complicated things for less
	common cases as exceptions (quite possibly manual
	exceptions). Calendaring time zones get into trouble because they
	make the common and simple case be more complex. The problem occurs
	because the designers wanted to use the same data for both the
	simple and phone cases - but that just gets the simple case in trouble.


Usually when I hand out a prize for worst-user experience Lotus
	Notes is at the top of the queue. (Indeed I find it embarrassing to
	admit that Thoughtworks uses the damn thing.) But the worst
	time-zone experience award goes to Microsoft Office, although to be
	fair this was many years ago. I had recently bought a PDA (running
	Windows CE version 2). I had put some all day meetings into my
	calendar, flown to Chicago, and to get the PDA to alert me to
	meetings I changed the timezone of the PDA to one hour earlier.


Suddenly every  one of my all day meetings shifted to a day
earlier. This was due to a catalog of errors. First off they had
stored an all day meeting as a meeting from midnight to midnight -
that's the kind of representation error on a [TimePoint](https://martinfowler.com/eaaDev/TimePoint.html) that often gets
people into trouble. Then it was compounded by shifting the times of
meeting when I changed time zones - so all day meetings were now 11pm
to 11pm. This, of course, is due to putting the time zone into the
meeting so it looks like it shifted when I changed time zone on the
PDA. Then to cap it off, the software was clever enough to know that
an all day meeting should only show the day of the meeting, but the
day it chose was the day of the start of the meeting - that was now
one day earlier. That's the poor timepoint representation biting
back.
