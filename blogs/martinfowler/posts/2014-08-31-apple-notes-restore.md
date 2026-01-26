---
title: "Restoring a deleted note in Apple's notes app"
description: "I recently deleted a note on my Notes app on my apple laptop.     As someone who is a paranoid keeper of backups, and usually     commits all my work to a repository like git, I don't worry much     a"
date: 2014-08-31T00:00:00
tags: ["tools"]
url: https://martinfowler.com/articles/apple-notes-restore.html
slug: apple-notes-restore
word_count: 391
---


I recently deleted a note on my Notes app on my apple laptop.
    As someone who is a paranoid keeper of backups, and usually
    commits all my work to a repository like git, I don't worry much
    about accidental deletion. But Apple's notes app doesn't have any
    form of version control, and it's all too easy to delete something
    by accident. I have a daily rsync backup and run time machine, but
    googling couldn't uncover a simple way of getting the note back.
    So in case someone else needs to do this, here's what I did.


First I needed to find where Notes stores its data, googling
    around told me that it was in
    `~/Library/Containers/com.apple.Notes/Data/Library/Notes/`1.
    However doing a restore from Time Machine didn't help, because
    iCloud helpfully overwrote the restored version with one that was
    up to date. The data is also really mangled, so I couldn't easily
    just find the text I needed with a text editor.


1: [This stack exchange](http://apple.stackexchange.com/questions/111633/where-do-my-notes-written-in-the-notes-application-on-my-mac-get-saved) implies that some data may be elsewhere too,
      although I found what I wanted in the path I gave.


So I did this:

- I grabbed my old apple laptop which I rarely use
- I went to my daily backups and extracted the notes data
      folder from the path above and put it on the old laptop
- I disconnected the laptop from the internet (so iCloud
      wouldn't jump in and try to be helpful)
- I moved the existing notes data folder to the desktop and
      replaced it with the one from my backup
- I fired up the notes app, copied the text I needed, emailed it
      to myself, and quit the notes app.
- I restored the original notes data folder, and put the laptop
      back on the network.


In hindsight, however, it may have been easier to just
    disconnect my main laptop from the internet, restore from time
    machine, copy the text I needed from the notes app, and then
    reconnect. But I don't have the inclination to try to see if that works.


I don't store anything important in the notes app, preferring
    Evernote, or files in the safety of a git repository. I wish
    people who build software applications would make versioning a
    regular part of their feature set, once you get used to it, it's
    hard to live without it.


---
