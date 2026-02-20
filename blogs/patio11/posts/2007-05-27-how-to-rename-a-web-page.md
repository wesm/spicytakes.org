---
title: "How To Rename A Web Page"
date: 2007-05-27
url: https://www.kalzumeus.com/2007/05/27/how-to-rename-a-web-page/
slug: how-to-rename-a-web-page
word_count: 374
---


I renamed my Free Resources page, which is the #3 most popular page on my site, to [Printable Bingo Cards](http://www.bingocardcreator.com/printable-bingo-cards.htm), which both more accurately describes what is available there and is a much better title for SEO purposes.  This required some slicing and dicing in all of my HTML files because that is a link which appears in my navigation bar.  Luckily, bash was adequate for the task as always.


> for htmlFile in *.htm


> do


> sed s/free_resources.htm/printable-bingo-cards.htm/ $htmlFile > temp1.txt


> sed “s/Free Resources/Printable Bingo Cards/” temp1.txt > temp2.txt


> mv temp2.txt $htmlFile


> rm -rf temp?.txt


> done


I also redid the title tag (“Free Resources from Bingo Card Creator” to “Printable Bingo Cards from Bingo Card Creator”), updated the site map with the new URL, and added a RewriteRule for the old URL to my .htaccess so that I don’t break any links from the blogs and schools who linked to it.  This is a **fairly key step** for any change you make that affects a popular page.  If you do not do it, not only are you hurting user experience on third party sites which trusted you with a link, you’re squandering PageRank that you’ve worked so hard to gain.  Adding in another rewrite rule takes like 5 seconds, so do it!


> ## put me somewhere near the top
> RewriteEngine on
> ## put me in the big block of rename rules you’ll be creating


> RewriteRule ^thanks-for-downloading.htm$   [http://www.bingocardcreator.com/thanks_for_downloading.htm](http://www.bingocardcreator.com/thanks_for_downloading.htm) [R=301,L]


printable-bingo-cards.htm is, by the way, pushing it on how many words I would suggest you have in a filename.  I’m fairly sure that is under the threshold to get penalized because one or two of my competitors use three word filenames, sometimes after having the same three words in a directory listing.  That is a bridge too far in my book, and I expect Google will smackify it sometime soon.  Repetition in the URL gives no useful information to human users, and it is not a “natural” design technique for a website either, so I suspect that Google will eventually toss it out as a useless SEO technique, the same way they habitually ignore overly-long-file-names-stuffed-with-keywords-like-this-one.htm .


Finally, don’t forget to resubmit your updated sitemap to Google.
