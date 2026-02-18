---
title: "How to Create an ‘App of the Year’"
date: 2005-02-18
url: https://daringfireball.net/2005/02/how_to_create_an_app_of_the_year
slug: how_to_create_an_app_of_the_year
word_count: 1236
---


When I made my selections for [apps of the year for 2004](https://daringfireball.net/2005/02/apps_of_the_year_2004), my
only criterion was to choose the apps released last year that I liked
best. But after making my selections, it was obvious that the apps I
chose shared some general characteristics.


The apps I chose were:

1. [Interarchy 7](http://www.interarchy.com/)
2. [Affrus 1.0](http://latenightsw.com/affrus/)
3. [SpamSieve 2.2](http://c-command.com/spamsieve/)
4. [BBEdit 8.0](http://www.barebones.com/products/bbedit/)


And my honorable mentions:

- [OmniWeb 5](http://www.omnigroup.com/applications/omniweb/)
- [NetNewsWire 2.0](http://ranchero.com/netnewswire/)
- [Quicksilver](http://quicksilver.blacktree.com/)


## Documentation


My first observation is that all of these apps, with the exception
of Quicksilver, have good documentation. In fact, most of them have
excellent documentation.

- In my write-up for the ‘Apps of the Year’ article, I devoted an
entire section to Affrus’s outstanding help book and “Getting
Started With Affrus” PDF file.
- Interarchy has a user manual documenting all of its features,
available both as a help book and [on their web site](http://www.interarchy.com/documentation/7/).
- SpamSieve contains a complete and well-written user manual,
available both as a PDF and in HTML help book format ([also
available on the web](http://c-command.com/spamsieve/manual)).
- BBEdit ships with a [352-page indexed PDF user manual](http://www.barebones.com/support/bbedit/index.shtml),
and an HTML help book containing a subset of the user manual
emphasizing frequently-referenced topics such as the syntax for
grep and glossary files. (Full-disclosure: When I worked at Bare
Bones I contributed somewhat significantly to the user manual.)
- OmniWeb has a complete HTML user manual which displays within
OmniWeb itself.
- NetNewsWire has a complete HTML help book.


And even Quicksilver is at least [trying](http://docs.blacktree.com/); it’s
under-documented, not undocumented. But in my judgment, wikis seldom
produce complete documentation; they’re a good way to aggregate
user-contributed tips and tricks, but they’re a poor way to
completely document a complex app.


## Scripting and Extensibility


All of these apps are scriptable and/or extensible.

- Interarchy, Affrus, and BBEdit offer some of the best
AppleScript support of any apps ever built. All three are
recordable, for example, which, unfortunately, is quite rare.
BBEdit also lets you manipulate the contents of text windows
using Unix filter scripts (Perl, Python, Ruby, shell scripts,
etc.).
- SpamSieve pretty much does its whole thing by way of
AppleScript (or at a lower level, Apple events). This is how
SpamSieve works so well with so many different email clients:
Apple Mail, Mailsmith, Entourage, Eudora, PowerMail, GyazMail.
It even works with classic apps like Claris Emailer and Outlook
Express, because Apple events can pass between classic and
native Mac OS X apps.
- NetNewsWire offers pretty good scriptability. For example,
version 2 adds Web Kit-powered built-in web browsing, complete
with tabs. NetNewsWire offers scripting access to the titles and
URLs of those tabs; thus, NetNewsWire, which offers web browsing
as a secondary feature, provides better AppleScript access to tabs
than does Safari. Plus, NetNewsWire allows you to “subscribe” to
a script (AppleScript or Unix script), which it will execute and
read the output from as an RSS or Atom feed.
- OmniWeb 5 offers the best AppleScript support of any web browser.
- Quicksilver has its own scripting dictionary, but not key.
Quicksilver is not the sort of app that you want to control via
AppleScript; rather, it’s the sort of app you use to do things
that control other apps. You can use it to launch scripts, and using
its Triggers feature, you can assign keyboard shortcuts that
execute arbitrary scripts. Plus, Quicksilver is very much
extensible via [plug-ins](http://quicksilver.blacktree.com/plugins.php), which allow you to customize
the actions the app is capable of performing.


Customization is what it’s all about. Making an app scriptable isn’t
just a check-off feature — it’s about allowing users to check-off
their own individual customized features. I’ve written scripts for
my own use with these apps that I would never ask for as built-in
functions in the apps themselves, but which save me significant
amounts of time.


Most users don’t write their own scripts, even with apps which are
recordable, like Interarchy, BBEdit, and Affrus. But users who *do*
write scripts are almost always willing to share, posting scripts to
forums, mailings lists, and weblogs. It helps build a loyal
community of users around an app — even if most of them don’t write
their own scripts and plug-ins.


## Tabs


Interarchy, BBEdit, OmniWeb, and NetNewsWire all offer
multiple-documents-in-a-single-window tabbed interfaces. Affrus
doesn’t, but I don’t think it would be a good fit for Affrus. And
it’s not even applicable to SpamSieve, which doesn’t have (or need)
a document-window interface at all, let alone a tabbed one.


Two things are interesting here. One is that tabbed document-window
interfaces are new to the Mac, but are taking hold quickly. It
started with web browsers, but it has quickly spread to other
app categories. (E.g. [TextMate](http://macromates.com/) offers tabs in its project
windows, and [Transmit 3](http://panic.com/transmit/) just shipped with support for tabs.)


The second is that implementations vary widely. Interarchy uses a
very Safari-ish tab implementation. NetNewsWire’s tabs *work* pretty
much just like Safari’s, but they *look* quite different, using a
slightly larger size and a subtle gradient texture. Plus, unlike
Safari (and Interarchy), NetNewsWire’s tabs appear above the URL
location field, and attach from the bottom of the tab:


OmniWeb and BBEdit go a wholly separate route, using sidebar
drawers. Thus, they’re not really *tabs* at all, in the literal
sense. Bare Bones doesn’t even call them tabs, but simply refers to
the feature as the “documents drawer”. The Omni Group does call them
tabs, and theirs is by far the most thoughtful implementation of the
bunch. (I’m calling all of these features “tabs” here — even
BBEdit’s — simply because it’s easier to use one term, and even in
the cases where they’re not literal tabs, it’s pretty obvious what’s
meant by the term.)


Both BBEdit and OmniWeb allow you to drag tabs between windows.
Interarchy and NetNewsWire don’t (and neither does Safari,
unfortunately; tabs didn’t originate with Safari, but it’s by far
the highest-profile and most-used tabbed app, which makes it a de
facto reference implementation). OmniWeb goes further, and allows
you to drag URLs into the list to create a new tab for that URL, and
it allows you to use drag-and-drop to *reorder* tabs within the
list. None of these other apps allow you to reorder tabs, but it’s
something I love about OmniWeb, and I wish all these other
apps supported it.


Tabs are quite obviously here to stay, so it’d be nice to see Apple
take a leadership position here and provide developers with a
standardized set of widgets and interface guidelines on the matter.
Only Apple can prevent this from turning into a permanent
free-for-all of disparate and inconsistent appearances and
behaviors.


(**Worth noting**: I’m well aware that this is far from an
exhaustive list of tabbed Mac apps, and some of the other
implementation are really quite nice (e.g. [Adium](http://adiumx.com/) has
draggable Safari-style tabs). This isn’t a comprehensive look at
multi-document tab implementations, it’s just a cursory examination
of the implementations in these particular apps.)


## How to Create an ‘App of the Year’


So what’s the lesson? Looking at this bunch of apps, it would seem
to be:

- Produce great documentation
- Take scripting and extensibility seriously
- Allow for a tabbed interface


One last thing worth noting about these apps, by the way: none of
them came from Apple.



| **Previous:** | [Apps of the Year, 2004](https://daringfireball.net/2005/02/apps_of_the_year_2004) |
| **Next:** | [FireWire Hysteria](https://daringfireball.net/2005/02/firewire_hysteria) |


PreviousNext