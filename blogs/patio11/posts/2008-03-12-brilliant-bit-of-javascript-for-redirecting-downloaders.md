---
title: "Brilliant Bit of Javascript for Redirecting Downloaders"
date: 2008-03-12
url: https://www.kalzumeus.com/2008/03/12/brilliant-bit-of-javascript-for-redirecting-downloaders/
slug: brilliant-bit-of-javascript-for-redirecting-downloaders
word_count: 648
---


One of my uISV buddies, Ethan (king of [language learning software](http://www.declan-software.com)), took me to task earlier today for spending so much time optimizing my [download page](http://www.bingocardcreator.com/free-trial.htm) when I could just eliminate it entirely and link the download direct to the download button in most cases.  I had always had these issues with that solution:

- My users don’t necessarily know what to do with a window that pops up
- If I do an HTTP Refresh or Javascript redirect, many browsers pop a security warning
- I have to discriminate between Mac and PC users somehow
- It is impossible to track that conversion for AdWords purposes, currently


Examining Ethan’s code made it really easy to avoid the first two issues:


> function SetUpRedirect()


> {


> var destination = “[http://www.bingocardcreator.com/free-trial.htm](http://www.bingocardcreator.com/free-trial.htm)“;


> setTimeout(“window.location=’”+destination+”‘”,3000);


> return true;


> }


If you stick that in the OnClick attribute of a link pointing at your favorite executable, three seconds after clicking the link and having the download initiate, the user’s browser goes to the download page in the background.  This causes no security warning, scores them as a download conversion with the appropriate code on the page, and presents graceful fallback behavior if they don’t know what to do with the window that just popped up, since you can give them instructions.


Ahh, but what to do about the difference between Windows and Mac computers, which need different installers?  First, we make a controller method to handle it in Rails:


> def free_trial_download


> if request.user_agent.downcase =~ /mac/


> send_file “public/files/BingoCardCreator.zip”, :type => “application/zip”


> else


> send_file “public/files/BingoCardCreatorInstaller.exe”, :type => “application/exe”


> end


> end


That essentially says “If I’m positive you’re using a Mac, initiate a download of the zip file.  Otherwise, initiate a download of the exe file.”  (Obviously since 92% of my downloads are PC users I want to err on the side of caution.)


Then, with a simple route added to routes.rb:


> map.downloadFreeTrial ‘free-trial/download’, :controller => ‘static’, :action => ‘free_trial_download’


we get a simple URL which is platform agnostic and which decides, on the server side, which version of the file to give them.  You can then decorate your links to the platform-agnostic URL with the code to redirect the page to the download page in the background, with Analytics click tracking, and what have you.  Easy peasy!  One less step in the conversion funnel, and instantaneous recovery of a large portion of the 20% of folks who bounce out of the funnel at the download page.


**WARNING**: send_file will cause your Rails process to **block** while that IO transfer takes place under certain older versions of Rails (not in 2.0 in my testing).  This will cause requests coming to the same Mongrel after the download to wait until the download completes to start, which if you have a 56k modem user could potentially cause your basic site access to be delayed for *minutes*.  **Not** good news!


My site has two Mongrels running, very few dynamic requests, and very small executables.  If your site doesn’t have this profile, instead of using send_file, 302 redirect the browser to the appropriate file and let your web server handle the request before Rails does.


**WARNING NUMBER TWO:** You don’t want bots hitting that action, so its time for a good-old robots.txt exclusion of it.  Note that deploying this sitewide will cause your free trial page to lose quite a bit of the juice you’re sending to it.  However, given that that page is typically linked far and wide on the Internet and doesn’t include much interesting content on it (which would distract from the conversion to the trial!), you can probably live with that tradeoff.


Quick request: if you run an obscure browser or a Mac, kindly use my [OS-agnostic link](http://www.bingocardcreator.com/free-trial/download) and tell me if it works for you.  (You should get a prompt to download BingoCardCreator.zip )
