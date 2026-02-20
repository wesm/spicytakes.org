---
title: "If One File On Your Web Server Gets Corrupted…"
date: 2006-10-28
url: https://www.kalzumeus.com/2006/10/28/if-one-file-on-your-web-server-gets-corrupted/
slug: if-one-file-on-your-web-server-gets-corrupted
word_count: 134
---


… it WILL be your trial executable, without fail.  Murphy’s law.  One freaking byte on disk got corrupted at some point within the last week and I just found out about it today, by someone who was kind enough to write in and say “Heya, this won’t install, says the file is corrupted.  And I downloaded it three times”).  One quick download later and I was able to reproduce the error, which is funny because I haven’t uploaded anything to that directory on the server in literally weeks.  Did a quick hex diff and, boom, one byte out of place, which called NSIS to say “Uh oh, checksums don’t match, I’m out of here”.  *sigh*  Well, better to know about it and be able to fix it than to not know about it, right?
