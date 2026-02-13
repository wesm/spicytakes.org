---
title: "Snowy day in New York"
date: 2008-12-19
url: https://www.joelonsoftware.com/2008/12/19/snowy-day-in-new-york/
word_count: 243
---


I’ve been debugging the new site. The first problem: hopelessly messed up rendering on IE6. The best way to fix CSS problems with IE6 is to generate random mutations on the style sheet until it looks fixed. That’s really the only way to approach these kinds of things; CSS is nondeterministic, and many better minds than mine have gone completely stark raving mad trying to understand the rhyme and reason of IE6 rendering bugs.


Once that was fixed, people who read this site in an RSS reader reported that included images with captions weren’t showing up correctly. To fix that one, I had to move the style information from the style sheet right into the tag, but only for the RSS feed. I think that should fix it for the most popular RSS readers (Bloglines and Google Reader) but many RSS readers strip out CSS aggressively and I can’t do anything about that.


Waffle Wednesday at Fog CreekTo test the fixes, I’ve thrown in a picture of Waffle Wednesday, showing our fabulous director of QA attacking a waffle iron with PAM in the company kitchen.


Finally—many readers noticed that the images appear slightly pixelated. This is a result of relying on the browser to scale images. In my testing, it seems that Firefox and Safari do a very nice job scaling the images and there’s no visible pixelation. Internet Explorer: not so much. If you use a better browser, you get better results.
