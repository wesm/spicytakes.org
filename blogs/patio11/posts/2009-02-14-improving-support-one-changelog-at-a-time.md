---
title: "Improving Support One Changelog At A Time"
date: 2009-02-14
url: https://www.kalzumeus.com/2009/02/14/improving-support-one-changelog-at-a-time/
slug: improving-support-one-changelog-at-a-time
word_count: 112
---


sales.rb Revision 539:


Unanticipated behavior: Some customers put Registration Key into Lookup My Registration Key form.  This looks up transactions by order number and email address, thus failing to find any matching records, then informs customer to email me to find their Registration Key.  This is suboptimal.


Fix: If input into LMRK form resembles a Registration Key, search for a line item which had that Registration Key assigned.  If one exists, then it was actually issued to a customer — redirect them to explanatory text with pictures on how to enter a Registration Key into the application, not the website.


If Registration Key does not exist, then tell customer to email me.
