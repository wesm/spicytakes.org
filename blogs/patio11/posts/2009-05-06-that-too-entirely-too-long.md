---
title: "That too ENTIRELY too long"
date: 2009-05-06
url: https://www.kalzumeus.com/2009/05/06/that-too-entirely-too-long/
slug: that-too-entirely-too-long
word_count: 435
---


Well, on the plus side, the last three days have probably been my most productive programming spring ever.  On the minus side, a lot of it was spinning my wheels fighting against problems rather than making forward progress.  I blame fatigue.


## What I Have Done:


**Bingo Card Creator 3.0**.  *Whee*.  It can interact with the server to save user’s word lists in *the* *cloooooooooooud*.  Which is apparently the $10 buzzword for a client-server application these days.  For extra bonus points I threw in PDF generation on the server — *How hard can it be?* – and then got to rediscover the joys of heavy duty fat client Java application development.  Did you know that there is no way in Java’s standard library to copy a file from point A to point B?  Or that if you open the desktop in a Java open/save window it will show you some GUIDs as possible folders?  Fun stuff.


## What I Have Mostly Working


**Delayed Job integration**.  If somebody tries to generate a thousand bingo cards on Prawn, that essentially takes one of my Mongrels and ties it up for a minute.  Behind that, requests start piling up and not getting executed.  Plus, should they have a connection hiccup, well, guess I lose.  So rather than generating PDFs in the request/response cycle, they get queued up for execution in the near future, using [Delayed Job](http://github.com/collectiveidea/delayed_job/tree/master).


Why is it only “mostly” working?  Well, following standard Linux best practices, the user that is supposed to execute the jobs has very little in the way of privileges.  Apparently too little to actually touch his directory.  I have tried everything I can think of to fix this, with no dice, so its time to walk away and come back fresh later.


## What Isn’t Even Started Yet


The web version of the software.  (Well, OK, technically the PDF-ification and most of the existing infrastructure will get reused, but I still have to actually make the screens for it, and then tie them into the purchasing pathway.)


I hope to get the web stuff mostly working this weekend and then open 3.0 up for beta testing.  If you’re interested in helping out, please drop a comment, particularly you Mac freaks out there.


You can see the newly redone PDFs and GIFs for most cards at http://staging.bingocardcreator.com .  Still got some bugs to iron out of that, though…  (Prawn + Imagemagick is literally fifty times faster than rendering through the Windows printer and then screenscraping Adobe Acrobat reader then pasting into Paint — automated, naturally — for cropping out a GIF screenshot, incidentally.)
