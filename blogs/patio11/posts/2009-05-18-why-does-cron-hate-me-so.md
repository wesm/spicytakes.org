---
title: "Why does cron hate me so?"
date: 2009-05-18
url: https://www.kalzumeus.com/2009/05/19/why-does-cron-hate-me-so/
slug: why-does-cron-hate-me-so
word_count: 92
---


Once *again*, cron decided that it would stop deleting my Rails cached files after I upgraded to Hardy. I’m totally stumped as to why it happened — the logs say that the rf -rm happened at the scheduled times for the last two weeks, and I was able to successfully do it by sudoing into the appropriate user, but the files were still on disk and being happily served by Nginx, oblivious to the fact that Mother’s Day and Cinco de Mayo had long since passed.


Argh, I hate computers some days…
