---
title: "OmniWeb 5 Public Beta"
date: 2004-02-02
url: https://daringfireball.net/2004/02/omniweb_5_public_beta
slug: omniweb_5_public_beta
word_count: 4192
---


Today the Omni Group released the first [public beta of OmniWeb 5.0](http://www.omnigroup.com/applications/omniweb/5/beta/). Based on today’s beta, and the two alpha releases I’ve used for the last week, OmniWeb 5 has the potential to be a very big deal.


With a rendering engine based on WebCore and JavaScriptCore — the same underlying technologies Safari is built around — OmniWeb 5 renders pages beautifully, and, more importantly, offers robust support for web standards.


But the current version of OmniWeb — version 4.5 — also uses WebCore, and it’s an also-ran browser. OmniWeb 5 is important because it offers an abundance of major new features, including two that are revolutionary. OmniWeb 4.5 was a stop-gap, the first release of the browser that used WebCore instead of the Omni Group’s home-grown (and terribly outdated) rendering engine. OmniWeb 5 is the first release where Omni has been able to focus almost solely on the browser application, rather than the rendering engine.


Here’s an overview of the big new features. Keep in mind, if you download the public beta, that it is very much beta software, replete with crashers and other show-stopping bugs.


## Tabbed Browsing


OmniWeb 5 supports tabbed browsing. The idea of which is much the same as it is in Safari and Mozilla-based browsers, but the visual presentation is quite different. In fact, visually, they’re not really *tabs* at all, but rather thumbnails in a drawer on the side of the window. The thumbnails are scaled representations of the page displayed in the tab. Tabs can also be shown in a list view, sans thumbnails, to fit more tabs in the drawer without needing to scroll.


I like tabbed-browsing in general, and I like the Omni Group’s implementation, but it’s not even close to being the best or most important new feature in OmniWeb 5. I’m listing it first in this review, however, because I anticipate it being the most controversial feature — it’s the most visually distinct new feature, and when the peanut gallery gripes about “the interface”, they tend to focus on what an app looks like.


The argument against OmniWeb’s tab implementation is that it uses up a lot more screen space than does Safari’s (and Mozilla-based browsers). Safari’s tabs are displayed in a wide but short strip, across the top of the browser window. In terms of screen area, Safari comes out way ahead.


But in every other regard than screen area, OmniWeb’s presentation is superior. I agree that screen space is precious (I spend my days in front of a 12” iBook), but I’m willing to give this extra space to OmniWeb. The advantage to OmniWeb’s presentation is when you use the thumbnail view:


The scaled-down thumbnails of the pages in the tabs are easily identifiable, with just a glance. In Safari (and in OmniWeb’s list view for tabs), tabs are only identifiable by their names. And the more tabs you add to a Safari window, the more truncated the titles get. The only case where OmniWeb’s thumbnails aren’t all that useful is when you have several tabs open to pages on the same site, in which case the scaled thumbnails are indistinguishable. But OmniWeb still includes the page titles, so you’re no worse off than you would be in Safari.


I’m quite happy with OmniWeb’s tab drawer. Yes, it uses more screen space, but it uses *horizontal* space, which works well with Apple’s move toward widescreen displays, and strikes me as loosely analogous to the context-switching sidebars in other apps — like iTunes, iPhoto, the Finder, and three-pane readers like email clients and NetNewsWire.


But even if you don’t like *where* OmniWeb displays its tabs, you’ve got to love what it allows you to do with them. Most importantly, you can drag tabs from one window to another; you can even shift-click to select multiple tabs in one window and drag them all to another window at once. You can explode tabs into separate individual windows. If you try to close a window that contains more than one tab, OmniWeb asks if that’s really what you want to do (but if you don’t like the warning, you can turn it off). These features are all sorely missing from Safari.


My three niggling gripes about OmniWeb’s tab drawer:

- When you create so many tabs in a window that the thumbnails no
longer all fit in the sidebar, OmniWeb uses a scrollbar to display
them all. I’d prefer it if OmniWeb instead shrunk all the
thumbnails, attempting to keep them all visible at once.
Obviously, at some point, the thumbnails would become too small, but
for a couple of extra tabs, I think it’d be usable.
- Because of the way drawers are drawn in Aqua, if you have a window
with no tabs directly in front of a window with tabs, it looks like
the second window’s tab drawer is sliding out of the front window. This
isn’t the Omni Group’s fault; it’s Apple’s.
- The little “X” button you click to close a tab is a bit too small.
Plus, it doesn’t have a rollover state to indicate when the pointer
is within its clickable area.


## Workspaces


Workspaces are simply the best new feature in OmniWeb 5. The way its preferences are configured out of the factory, however, you might not notice them (other than the new Workspace menu).


Here’s the gist. A workspace is a collection of browser windows, including the position and size of the windows, tabs, and the pages displayed in each tab. When you switch from one workspace to another, the existing workspace’s windows go away, and the new workspace’s windows appear. So, let’s say you’re a web developer. You can create a workspace for each of the web sites you’re working on, with browser windows (and/or tabs) pointing to your staging server, your production server, your CMS admin interface, the W3C HTML validator, etc. When you want to switch to another site, simply switch workspaces; the old windows go away, replaced by the new ones.


You create these workspace states by taking *snapshots*. Set up your windows and tabs just the way you want them. Create a new workspace, name it, and take a snapshot. Now you can switch to that snapshot by choosing it from the Workspace menu.


Pretty cool, but I haven’t even gotten to the best part yet.


What’s *really* cool about workspaces is their ability to save state automatically. Each workspace has a “Save windows” checkbox (in the Workspaces window); when turned on, a workspace remembers its entire state when closed. This not only kicks in when you switch from one workspace to another, but also when OmniWeb quits.


Thus, even if you never use multiple workspaces, you can still love the feature. If you’ve got multiple windows and dozens of tabs open, you can quit OmniWeb, and when you relaunch it, *the windows and tabs will be restored, exactly how they were when you quit*.


Inexplicably, this feature is turned off for the default workspace in a factory fresh set of prefs for OmniWeb 5. Well, *inexplicably* isn’t the right word — it’s off by default so as to behave exactly like other browsers (including previous versions of OmniWeb) — when you quit the browser, you lose all your open windows and tabs. To turn it on, choose Show Workspaces from the Workspace menu, then click the “Save windows” checkbox.


I’ve wanted this behavior in a web browser for years. I even used AppleScript to write a snapshot-like feature to [save and restore URLs in Safari](https://daringfireball.net/2003/02/save_and_restore_safari_urls). But my scripted solution for Safari suffered a major problem: You had to invoke it explicitly to save state. If you accidentally quit Safari (which has happened to me several times when I’ve OK’d the installation of software that requires a restart, which in turn sends a quit Apple event to all running apps), any windows you’ve left open are gone. With OmniWeb’s workspaces, saving can be automatic.


Thus, OmniWeb 5 is the first and only web browser I’ve ever seen that places any value whatsoever on your state — the position, placement, and content of your open browser windows. Every browser should work this way, and OmniWeb should work this way by default.


As a beta-testing bonus, the feature even kicks in when OmniWeb *crashes*. When you relaunch, OmniWeb restores the state you were in before the crash occurred. It actually makes the beta-cycle crashiness tolerable.


## AppleScript Support


Speaking of my “Save and Restore URLs” script for Safari, there was one other flaw with it — Safari provides [no scripting access to tabs](https://daringfireball.net/2003/05/safaris_unscriptable_tabs).


OmniWeb 5 *does*, and it’s pretty sweet.


The dictionary terminology is good: browser windows are `browsers`, which can contain multiple `tabs`. Each `tab` has an `address` property. The release notes state that scripting support is incomplete (e.g., tabs lack a `title` property, alas), but what’s already implemented in beta 1 is more than Safari 1.2 offers.


In fact, it’s enough to rewrite another of my Safari scripts that suffered greatly from Safari’s unscriptable tabs — a [script to insert a URL](https://daringfireball.net/2003/01/scripting_safari_urls) from any open browser window into the front BBEdit text window. The idea is that when you’re already in BBEdit, you can invoke the script to pop up a dialog box listing every URL open in OmniWeb. Choose the one you want, and the URL gets inserted in the front text window.


(Blank lines separate the URLs from different browser windows.)


You simply can’t do this in Safari, unless you avoid using tabs, because Safari only offers scripting access to the URL of the frontmost tab in each window. Mac OS X’s GUI Scripting is not an acceptable workaround — even if you ignore the fact that the syntax is horrendous, it requires taking over your actual GUI to do its thing. The whole point of the script is that you don’t want to leave BBEdit — you just want to insert a URL. A script that gets the URLs from each Safari tab using GUI Scripting needs to pop Safari to the front, then flip through each window and each tab. Epileptics, be warned.


With OmniWeb 5, all you need is this::


```
set url_list to {}

tell application "OmniWeb"
   repeat with b in every browser
      repeat with t in every tab of b
         copy address of t to end of url_list
      end repeat
      -- insert a blank line to separate windows:
      copy "" to end of url_list
   end repeat
end tell

tell application "BBEdit"
   set the_url to choose from list url_list ¬
      with prompt ¬
      "Insert URL from OmniWeb:" OK button name "Insert"
   if the_url is not false then
      set selection of window 1 to the_url
   end if
end tell

```


(Simply change the BBEdit tell target to Mailsmith or TextWrangler, and you’ve got a version for pasting URLs into those apps too.)


## Site Preferences


OmniWeb has always supported a large assortment of application preferences. OmniWeb 5, however, introduces something revolutionary: *per-site* preferences.
Site Preferences are more than just great. They’re *fucking* great.


Here’s how it works. For any web page that doesn’t display the way you like based on your default OmniWeb application preferences, simply invoke the Site Preferences panel. You can change your font settings, the user-agent string OmniWeb uses to identify itself, your JavaScript settings, and more. Thereafter, OmniWeb applies those custom prefs when you visit that particular site.


So, for example, let’s say you’ve set your default browser font to 11px Verdana — a good screen font at a slightly small, but still quite readable size. Unfortunately, it’s common practice for web designers to assume that you’re a moron who has never changed from the ridiculously-large 16px default font size your browser started with, and thus to specify body text at 75 or 85 percent of your browser’s default, which, in this example, results in text which is way too small.


When faced with this display problem in Safari, Mac IE, or the various Mozilla offshoots, you can either (a) click the “larger text” button on the toolbar once or twice, or (b) capitulate and revert your preferences to the default of 16px. The problem with (a) is that you’ve got to do it *every time* you visit a site that uses this text-sizing technique. The problem with (b) is that you end up with text that’s too large when you visit sites that use your default text size as-is. You can’t win. What’s the point of having a default text size preference if web designers are going to assume you’re too stupid to know about it?


With OmniWeb 5, you only need to change your text size for each site once, and it sticks. I’ve found that I no longer need the toolbar buttons for smaller and bigger text — I set it once in Site Preferences, and each site looks perfect thereafter.


The same goes for other prefs, like telling OmniWeb to identify itself as IE to access sites that block visitors by user-agent.


The only minor gripe I have about Site Preferences is the default keyboard shortcut,  Cmd-Opt-P. I think Cmd-Opt-Comma would be a much more intuitive shortcut: Cmd-Comma for application-wide prefs, Cmd-Opt-Comma for per-site prefs. Plus, any shortcut involving Cmd and P feels like it ought to have something to do with printing (and in fact, many apps use Cmd-Opt-P for Page Setup).


## OmniWeb’s Core Problem


To this point, OmniWeb 5 sounds like an unequivocal winner over Safari — a better user interface with the exact same rendering engine. Except that it *isn’t* the same rendering engine.


OmniWeb 5.0’s rendering engine is derived from WebCore v85, which corresponds to Safari 1.0, [which shipped last June](http://www.web-graphics.com/mtarchive/000919.php). By what I can only assume is coincidence, Apple today shipped Safari 1.2, which updates WebCore to v125.
Thus, OmniWeb’s rendering engine is about eight months behind Safari’s, missing out not only on the improvements and fixes included in today’s 1.2 update, but also the version 1.1 update that shipped as part of Panther.


[Web Kit](http://developer.apple.com/internet/safari.html) is a built-in component in Panther (also available under Jaguar if Safari is installed), and provides third-party developers access to the *exact same rendering engine* used by Safari. Apps that use Web Kit gain access to improvements in the rendering engine at the same time Safari does.


But OmniWeb 5.0 isn’t using Web Kit, nor does the Omni Group plan to in the future. Instead, OmniWeb uses a baked-into-the-app customized version of [WebCore](http://developer.apple.com/darwin/projects/webcore/), the lower-level open source rendering code at the heart of the Web Kit. The question, of course, is *Why?*


It’d be easy to shoot my mouth off, decrying this as a bad decision. But experience has taught me not to second-guess engineering decisions from the other side of the source code. From where I stand, I can’t see OmniWeb’s internals, thus making it impossible to intelligently speculate on them.


So, I asked someone who *does* understand OmniWeb’s internals. Omni Group engineer Tim Omernick sent me the following answer:


> Omni has added features, fixed bugs, and performed optimizations on 
> WebCore which would not otherwise be available if we used Web Kit.  We 
> considered using Web Kit, but decided not to since it would mean that 
> OmniWeb would lose its distinct nutty flavor.
> Here are some reasons why we went with WebCore instead of Web Kit:
> It gave us several extra months of development time.  Apple was
> required to release WebCore as soon as Safari was made public, as is
> required by the LGPL.  We weren’t willing to wait until Apple
> released Web Kit to get started on integrating the technology into
> our browser.
> Web Kit was made for Safari, and thus prevents a browser developer
> from adding any significant features which Safari does not already
> possess.
> By using WebCore, we were able to build in several features which
> Safari/Web Kit does not have.  Examples include Site Preferences,
> the Pop-up Trap (loading of popups off-screen), min/max font size,
> the zoomed text editor, HTTP/JavaScript spoofing, etc.  These would
> have been simply impossible (or prohibitively difficult) to do using
> Web Kit.
> Our version of WebCore has fixes for several crashers still present
> in Safari.  Now, we do have our own crashers, but that’s beside the
> point ;-)
> Web Kit uses its own networking and HTTP layers (now part of the
> Foundation framework).  We already had ten years of well-tested
> networking and HTTP architecture in place, and we consider ours to
> be far superior in many ways to theirs.  We have spent a long time
> working around buggy HTTP servers, cleaning up dirty URL strings,
> and the like.  Let’s not even go into cookie handling (remember the
> security hole which affected Safari, but not OmniWeb?).
> The source editor.  It was already written, and we didn’t want to
> figure out how to rewrite it in a Web Kit-friendly way.
> As you can see, it made (and still makes) perfect since to use WebCore 
> over Web Kit.  We might take a couple of months to integrate Apple’s 
> WebCore changes, but IMO it’s worth it for the features you get in 
> OmniWeb.


An eminently reasonable answer. Like any hard design decision, either choice — WebCore or Web Kit — involves trade-offs. (If there weren’t any trade-offs, and one choice was clearly superior to the others, there is no decision.)


Web Kit offers an easy-to-implement API, and by linking to the rendering engine as a component of the OS, allows apps to remain current with the latest version without revising the apps themselves. How easy is Web Kit? Andrew Anderson’s recent article for O’Reilly’s Mac DevCenter, “[Build Your Own Browser](http://www.macdevcenter.com/lpt/a/4570)”, shows how to build a new web browser without writing a single line of code.


WebCore provides a complete standards-compliant rendering engine, but without an easy-to-use API. [Apple.com’s WebCore page](http://developer.apple.com/darwin/projects/webcore/) states:


> It is not a good idea to use WebCore directly for browser development
>   or HTML display on Mac OS X. The WebCore APIs are fragile, incomplete
>   and bound to change.


What it lacks in ease-of-use, however, it makes up for in flexibility. The entire source code to WebCore is available, whereas Web Kit is a private framework; you can link to Web Kit, but only Apple has the source to the Web Kit layer itself. This makes it easy to use Web Kit in ways Apple planned for (hence the no-lines-of-lines browser in Anderson’s article), but hard to use Web Kit in ways Apple did not plan for (like OmniWeb 5’s per-site preferences).


So in effect, the Omni Group has written their own Web Kit-like layer on top of WebCore, customized for the features and interface of OmniWeb. That’s a significant undertaking, and it’s why they can’t simply drop in new versions of WebCore as soon as Apple releases them.


OmniWeb 5.0’s rendering engine is indeed very good — but Safari 1.2’s is quite a bit better. It’s been a productive eight months in the Safari development labs. One site where you can see the difference clearly is Safari engineer [Dave Hyatt’s Surfin’ Safari weblog](http://weblogs.mozillazine.org/hyatt/) — his style switcher works great in Safari 1.2, works OK in Safari 1.1, and but doesn’t work at all in OmniWeb 5.0b1.


Now you might think it’s ironic that it’s a Safari engineer’s weblog that best illustrates the rendering deficiencies in OmniWeb, but to a web developer, this isn’t funny at all. Sure, the 95+ percent of the world that uses IE can’t see *any* of the neat new CSS tricks Safari 1.2 supports, making these techniques unfeasible for widespread deployment. WebCore v85 is certainly “good enough”, and also certainly better than any version of IE from a web standards perspective. But the fact that Safari is on the leading edge of web standards support makes it an excellent first choice for leading-edge web development. The same cannot be said for OmniWeb.


It’s a shame not just for web developers, who will need to use Safari itself for leading-edge web development, but also for the Omni Group — the market for non-free web browsers is relatively tiny, and I’d wager that professional web developers comprise a significant percentage of the people who take browsers seriously enough to consider paying $30 for one. That’s not to say web developers *won’t* love OmniWeb — but they’d love it a little more if its rendering engine were up-to-date with Safari’s.


In the long run, two or three years down the line, OmniWeb being a few months behind Safari won’t amount to much of a difference. But today, when the WebCore engine is still new, and still advancing at an incredible pace, a few months’ difference is significant.


## Miscellaneous Notes

- OmniWeb offers two options for displaying its Bookmarks window — in
its own standalone window, or inside the frontmost browser window.
Or as I like to call them, the Right Way and the Safari Way. Your
choice. Oh, and if you choose to display bookmarks inside your
browser window, it shows up in your history, which is the right way
to do it the wrong way.
- The Bookmarks window contains a damn good search feature, which you
can use not only to search your bookmarks, but also your history.
History searches can be based on URLs, page titles, and most
interestingly, *page content*. So if you remember reading a web page
mentioning “foo”, but you don’t remember exactly where, you can
search your history page content for “foo”. This is so cool, it
probably deserves more than a bullet point in this list.
- OmniWeb’s Shortcuts feature has been around for a long time, and
prior to the impressive new features in version 5, was one of its
most distinguishing features. Shortcuts are still supported, and
still good. In a nutshell, Shortcuts allow you to define shorthand
notations for the location bar; for example, you can type “google
foo” to perform a Google search for “foo”. You can customize
Shortcuts and add new ones; so if you don’t like typing “google
foo”, you can change it so that you just need to type “g foo”.
OmniWeb also supports a separate Safari-style search box, which not
only allows for searching Google, but other sites like the Internet
Movie Database. In fact, OmniWeb’s search field is hooked up to its
Shortcuts feature; any site you make a shortcut for, you can select
from the search field pop-up menu. This is nice if you like having a
separate search field, but I prefer using just the location field
alone and single-character shortcuts like “g” for Google. Not only
is it easier to invoke, but it frees up space in the toolbar.
- OmniWeb 5.0b1 feels a bit slower than Safari. Not too slow, but
slow enough to be noticable. I’m hopeful this will improve by the
end of the beta cycle — but there’s something to be said for the
Safari engineering team’s policy of not allowing for speed
regressions at any point in the development process.
- OmniWeb 5 supports RSS, but not well. It auto-detects
RSS feeds, which is great, but it doesn’t allow you to subscribe to
them in standalone newsreaders like NetNewsWire, which is wrong.
Instead, you can subscribe to RSS feeds as a collection within
OmniWeb’s Bookmarks window. It’s an interesting trick, but the right
way to do this is to support standalone clients (probably via the
[feed:// URL protocol](http://www.brindys.com/winrss/feedformat.html)). To me, this is analogous to a web browser
handling mailto: URLs on its own, instead of passing them off to
your email client.


## Conclusion


OmniWeb 5 has the potential to be one of the biggest software hits of the year. I say this as someone who has disliked every single previous release of OmniWeb. The last time I felt this way about beta software was before NetNewsWire shipped; OmniWeb 5 is that good.


The market for commercial web browsers is small — maybe even smaller than the market for commercial email clients. No matter how good OmniWeb is, the vast majority of Mac users are going to use Safari. There’s nothing wrong with that, and there’s nothing wrong with Safari. Safari itself is a very good browser.


But different users have very different needs, and it’s unreasonable to expect any one browser, no matter how good, to serve everyone well. You simply can’t expect one browser to work as well for grandmothers as it does for web programmers. OmniWeb is clearly targeted at high-functioning users; people who read more web sites, open more windows, and use more tabs. OmniWeb is to Safari as Final Cut Express is to iMovie. Neither Safari nor iMovie are in any way “software for dummies” — they’re both very capable apps, suitable for the vast majority of users. But both can be stretched thin by high-end users, who are willing to forego a bit of simplicity to gain powerful features.



| **Previous:** | [Nudge](https://daringfireball.net/2004/01/nudge) |
| **Next:** | [Scripting File and Creator Types](https://daringfireball.net/2004/02/scripting_file_and_creator_types) |


PreviousNext