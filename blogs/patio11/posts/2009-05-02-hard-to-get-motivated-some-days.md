---
title: "Hard to get motivated some days"
date: 2009-05-02
url: https://www.kalzumeus.com/2009/05/03/hard-to-get-motivated-some-days/
slug: hard-to-get-motivated-some-days
word_count: 386
---


I’m wrapping up day two out of the five-day vacation I have for Golden Week, and have not quite gotten as much accomplished on getting the new version out as I had hoped.


Task list to embarass myself into working hard tomorrow:


Bingo Card Creator 3.0

- Client connects to server, validates license key
- Server accepts connection from client, validates and if necessary reissuses license key
- Client contacts server, server saves word list to database
- Client-side GUI for saving word list to server
- Client contacts server, server responds with word list
- Client-side GUI for loading word list from server
- Client contacts server, server responds with list of client’s word lists
- Client-side GUI for loading word list from server
- Client contacts server, server responds with PDF of specified word list
- Client-side GUI for configuring PDF
- Client-side GUI for saving PDF
- Update license agreement to clarify usage of server
- Client requires acceptance of updated agreement to use server
- Set e-junkie to use automatically generated license keys instead of saved ones to stop reissuing the same key (sidenote: my fault, not theirs — I used the same key list for the CD version and download version)
- Update PAD file to reflect Bingo Card Creator 3.0
- Recruit Mac testers for BCC 3.0


Bingo Card Creator.net (my internal name for the web app version)

- Set up staging.bingocardcreator.com for testing
- User account page — edit name, email, password, Registration Key, etc
- User dashboard — display existing lists, printouts
- Word list editing workflow
- Printing workflow
- Generation of bingo cards PDFs
- Cache saved PDFs to disk
- Rewrite content publication to use Prawn & ImageMagick instead of laptop automation
- DelayedJob integration to remove PDF generation from HTTP request/response cycle
- Lightbox to present download BCC or sign up for BCC.net choice
- Lazy logins (no login for guest mode, upsell to free trial)
- Free trial upsells to $$$


Random tasks

- Integrate signup with MailChimp API to do autoresponder series for hints & tricks
- Set up mailing list for newsletter
- Resize Slicehost slice to 512MB to accomodate anticipated need for DelayedJob instances and extra Mongrels
- Blog about why I’m finally spending time to make a web version
