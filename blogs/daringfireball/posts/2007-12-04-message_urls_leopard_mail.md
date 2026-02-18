---
title: "‘message:’ URLs in Leopard Mail"
date: 2007-12-04
url: https://daringfireball.net/2007/12/message_urls_leopard_mail
slug: message_urls_leopard_mail
word_count: 1093
---


The new version of Mail in Leopard introduces a ‘message:’ URL handler that allows you to refer to individual messages in Mail from other applications. You can use a utility such as [RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/) to see that Mail registers as the default handler for the “message:” scheme. That Mail now supports these URLs does not seem to be documented by Apple anywhere, but it’s fairly simple, and very useful. It’s one of my favorite new features in Leopard Mail.1


The structure of these URLs is fairly simple: (1) the “message:” scheme,  followed by (2) the message-id of the message, enclosed in angle brackets (“<” and “>”). The message-id is specified in each message’s “Message-ID” header field, which is part of the [Internet email standard](http://www.faqs.org/rfcs/rfc2822.html). Every message-id should be universally unique, and every message should have a message-id. In my testing, the only messages I could find that didn’t have Message-ID headers were spam; such messages cannot be referred to by Mail’s “message:” URLs.2


The following formats all work:


`message:%3cMESSAGE-ID%3e`


In other words, the double slashes after the “message:” are optional, and the angle brackets surrounding the message-id value can be literal or URL-encoded. (“%3c” and “%3e” are the [URL-encoded values](http://en.wikipedia.org/wiki/Percent-encoding) for “<” and “>”, respectively.) If you omit the angle brackets completely, the URLs will *not* work.


There is no menu command in Mail to access these “message:” URLs; the only way I’ve found to reference one, other than creating them manually with AppleScript (see below), is by drag-and-drop. Most apps do not accept this URL data on the drag pasteboard, however. Three apps I’ve found that do are [Yojimbo](http://www.barebones.com/products/yojimbo/), [VoodooPad](http://flyingmeat.com/voodoopad/), and [DragThing](http://www.dragthing.com/). With Yojimbo, you can drag a message from Mail to Yojimbo’s main window, or to Yojimbo’s Drop Dock. When Yojimbo accepts the drop, it creates a new bookmark item with the title set to the email message’s subject, and the URL set to the “message:” URL. With VoodooPad, you can drop a message from Mail into a document window and VoodooPad will create an inline hyperlink; the text of the link is the message subject. With DragThing, dropping a message onto a palette creates a new URL clipping.


**Update:** They work in TextEdit, too. Simply drag a message from Mail to a TextEdit document window. **Update redux:** You can drag them into iCal, too. If you drop it into the URL field while editing an event, it’s an easy way to link an email message to an event.


With all these apps, dragging messages from Mail only works with one message at a time. If you drag multiple messages at once, the drop is rejected. I don’t think there’s anything these apps can do about this.


If you drag a message from Mail to the Finder, however, rather than getting a URL clipping file (such as when you drag a URL from Safari’s location bar to the Finder), you get an exported version of the entire message. (This matches the behavior of previous versions of Mac OS X.)


The first URL format listed above — *message:%3cMESSAGE-ID%3e* (no slashes) — is the one that Mail generates when you drag a message out of Mail. However, I have found that the second format — *message://%3cMESSAGE-ID%3e* (with slashes) — is better. Here’s why: if you paste the URL itself into a text field in any Cocoa app that uses NSTextView, you can then Control-click anywhere in the URL itself and use the Open URL and Make Link commands at the top of the contextual menu, because Cocoa will recognize the text as a URL.


What’s essential to note about this is that *you don’t have to select the entire URL first* — you can just Control-click anywhere in the text of the “message:” URL and the entire URL will be selected for you, and the top two items in the contextual menu will be the two most applicable to a URL. With the other three formats, Cocoa won’t recognize the “message:” URL as a URL even if you select it exactly before invoking the contextual menu. (In short, it seems to me that Cocoa’s URL guessing parser assumes that URLs contain slashes after the colon.3)


## AppleScript to Copy the ‘message:’ URLs for Selected Messages


I named the following AppleScript “Copy Message Link”. Select one or more messages in Mail, then invoke the script, and it will place “message:” URLs for each message, one per line, on the clipboard, ready to paste anywhere. It uses the “with slashes” format that works better in Cocoa NSTextViews.


```
tell application "Mail"
    set _sel to get selection
    set _links to {}
    repeat with _msg in _sel
        set _messageURL to "message://%3c" & _msg's message id & "%3e"
        set end of _links to _messageURL
    end repeat
    set AppleScript's text item delimiters to return
    set the clipboard to (_links as string)
end tell

```


Save it in your *~/Library/Scripts/Applications/Mail/* folder, and it will appear in Mac OS X’s [Script menu](http://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/as_related_apps.html) when Mail is frontmost. Or, better, use [Red Sweater’s FastScripts](http://www.red-sweater.com/fastscripts/) and you can assign it a keyboard shortcut.


---

1. [Mailsmith](http://www.barebones.com/products/mailsmith/) has supported a similar feature for quite some time, and many other apps offer something similar for referencing individual items inside a “library” database, e.g. [VoodooPad](http://flyingmeat.com/voodoopad/) and [Yojimbo](http://www.barebones.com/products/yojimbo/). It may sound trivial, but it’s one of the things I most missed about Mailsmith when I switched to Mail on Tiger back in June. ↩︎
2. The same goes for messages with malformed Message-ID headers, such as when the message-id is not enclosed within angle brackets in the header. Mail will produce “message:” URLs for such messages, but the URLs don’t actually resolve back to the original message. Again, however, in my cursory testing, the only messages with malformed Message-ID headers were spam. ↩︎
3. BBEdit’s URL parser is smart enough to identify either of the first two formats — so you can Command-click a “message:” URL in a BBEdit document whether it has slashes or not, so long as the angle brackets are encoded. ↩︎



| **Previous:** | [Anti-Aliasing on the iPhone](https://daringfireball.net/2007/12/anti_aliasing_on_the_iphone) |
| **Next:** | [Yet Another in the Ongoing Series Wherein I Examine a Piece of Supposedly Serious Apple Analysis From a Major Media Outlet and Dissect Its Inaccuracies, Fabrications, and Exaggerations Point-by-Point, Despite the Fact That No Matter How Egregious the Inaccuracies / Fabrications / Exaggerations, Such Pieces Inevitably Lead to Accusations That I’m Some Sort of Knee-Jerk Shill Who Rails Against Anything ‘Anti-Apple’ Simply for the Sake of Defending Apple, and if I Love Apple So Much Why Don’t I Just Marry Them?](https://daringfireball.net/2007/12/fastcompany) |


PreviousNext