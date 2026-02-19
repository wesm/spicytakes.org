---
title: "Safari Source in BBEdit"
date: 2003-01-21
url: https://daringfireball.net/2003/01/safari_source_in_bbedit
slug: safari_source_in_bbedit
word_count: 532
---


[Zeldman complained](http://www.zeldman.com/daily/0103b.shtml#viewy2), rightly, that recent browsers no longer provide the ability to choose an external editor in which to display web page source code:


> While we’re being honest, here’s an update on that whole “[view source in your HTML editor](https://daringfireball.net/daily/0103b.shtml#source)” problem. You can’t view source in your editor of choice in Chimera. You can’t view source in your editor of choice in Safari. You *could* view source under your editor of choice in IE5/Mac under OS 9, but you can’t in OS X, and no one can tell us why the browser no longer supports this function….
> This would be great: a site offering downloadable Apple Scripts that tell specific OS X browsers to open source in BBEdit or PageSpinner.


Today, Zeldman points to [Russell Harlan](http://homepage.mac.com/russh/), who has written such scripts (for IE and Safari) and made them available.


Nifty. I have a few suggestions, however.


In his IE scripts, Harlan gets the source code thusly:


```

tell application "Internet Explorer"
    set my_source to GetSource of document 1
end tell    

```


But for Safari, he resorts to using the command line curl utility (possibly inspired by my [“Grab HTML” script for BBEdit](http://daringfireball.net/2002/08/grab_html_script_for_bbedit.html)):


```

tell application "Safari"
    set my_url to URL of document 1
end tell
-- "-i" tells curl to include the headers
set my_text to do shell script ("curl -i " & my_url)

```


This isn’t necessary, however, because Safari’s `document` object has a `source` property. Thus, we can simply get the source for the frontmost Safari document thusly:


```

tell application "Safari" to set my_text to source of document 1

```


Of course, maybe you *do* want to use curl, because curl can be told to return HTTP headers in addition to the source code (which is precisely what Harlan’s script tells curl to do). HTTP headers look like this:


```

HTTP/1.1 200 OK
Date: Tue, 21 Jan 2003 17:43:36 GMT
Server: Apache/1.3.27
Last-Modified: Wed, 13 Nov 2002 05:19:42 GMT
ETag: "52f360-19c0-3dd1e0ee"
Accept-Ranges: bytes
Content-Length: 6592
Content-Type: text/html

```


If that info is interesting to you, then by all means, use curl. But if you just want the source, you can ask Safari for it.


However, if you do ask Safari for the source, it will be returned with Unix-style line breaks (`\n`), whereas BBEdit expects Mac line breaks (`\r`). Easily fixed using BBEdit’s `replace` command, giving us this script:


```

tell application "Safari" to set s to source of document 1

tell application "BBEdit"
    activate
    make new text window with properties ¬
        {contents:s, source language:"HTML"}
    -- fix the \n that Safari sent over
    replace "\\n" using "\\r" searching in text 1 of text window 1 ¬
        options {search mode:grep, starting at top:true}
    select insertion point before character 1 of text window 1
end tell

```


The above script was cribbed from a [post to the BBEdit-Talk list by Jim Correia](http://search.barebones.com/action.lasso?-database=lists.fp3&-layout=import&-response=detail.html&-recid=12608005&-search). Note that this script explicitly tells BBEdit to set the source language to HTML. In most cases, this isn’t necessary, as BBEdit (6.5 or later) is pretty smart about guessing the language when it isn’t specified. But it seldom hurts to be explicit.



| **Previous:** | [Ocean’s X11](https://daringfireball.net/2003/01/oceans_x11) |
| **Next:** | [Scripting Safari URLs](https://daringfireball.net/2003/01/scripting_safari_urls) |


PreviousNext