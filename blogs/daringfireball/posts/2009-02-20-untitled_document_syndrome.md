---
title: "Untitled Document Syndrome"
date: 2009-02-20
url: https://daringfireball.net/2009/02/untitled_document_syndrome
slug: untitled_document_syndrome
word_count: 2031
---


## 1.


Scenario: you have an idea for something, start a new document in an appropriate app, and then work for hours before realizing you haven’t yet saved the document? Typically, it’s a chuckle — *ha, guess I should save this thing*. Occasionally, it’s a disaster, because you only realize you hadn’t yet saved your work when the app crashes or the power goes out.


I’ve had the disastrous version happen a few times over the years. What strikes me as odd, though, is that I still catch myself doing it occasionally. I call it “Untitled Document Syndrome”, because when I catch myself doing it,  it’s almost always with a new untitled document window, not an existing file with unsaved changes. All subsequent saves after the first one require nothing more than a quick Command-S.


There’s [a great line in *Programming Perl*](http://books.google.com/books?id=ezqe1hh91q4C&pg=PA3&lpg=PA3&dq=larry+wall+say+what+you+want+to+say&source=bl&ots=juCBDtcRV0&sig=tD71B_oz1ffD_tbVR6YxmzOVvSM&hl=en&ei=-yWbSZX5DdLjtgeA6oiZCw&sa=X&oi=book_result&resnum=2&ct=result), the bible on the Perl programming language by Larry Wall (Perl’s creator), Tom Christiansen, and Jon Orwant, which sums up the entire appeal of modern scripting languages:


> One thing that’s easy about Perl is that you don’t have to say
> much before you say what you want to say.


In Perl, this is a complete working “Hello world” program:


```
print "Hello world\n";

```


That same simple example also works, without changing a character, in Python and Ruby. If you want to print a string, you just say “print”. The equivalent program in C, in contrast, requires you to say a bit before (and after) you say what you want to say:1


```
#include <stdio.h>
main() {
    printf("Hello, world\n");
    return 0;
}

```


The result is that programmers often wind up using syntactically efficient languages like Perl, Python, and Ruby to write little throwaway programs that they might never have written in the first place using, say, C, because it’s so much less of a hassle to get a simple working program off the ground. There’s simply less friction between the *idea* to write a little program and *actually doing it*.


You don’t have to be a programmer to see this. In fact, I suspect the above examples work even better for those of you who aren’t programmers — the frictiony bits of the C example surely stick out even more if you don’t understand what they mean.


Friction is a problem for software in general, not just programming languages specifically. There’s the stuff you want to do, and there’s the stuff you have to do before you can do what you want to do. People have a natural tendency to skip the *have to do* stuff to get right to the *want to do* stuff if they can get away with it. Friction is resistance. Hence untitled document windows containing hours of unsaved work — there’s an idea in your head that you want to express or explore, and the path of least resistance is to hit Command-N and just start working.


Saving a document for the first time is a minor chore, but it’s a chore nonetheless. The avoidance of such a minor chore is not rational; it is neither particularly complicated nor time consuming to hit Command-S and deal with the Save dialog. But we humans are not perfectly rational. We don’t always floss our teeth. We’ll pick the burger and fries instead of the salad. We’ll have one more beer. And sometimes we just don’t feel like dealing with the Save dialog box yet so we’ll put it off.


## 2.


So one conclusion to draw from this is that developers of document-based applications should protect users from themselves. Your *work* should be saved even if your document is not. Separate the management of items in the file system from the idea that what you’ve typed or drawn or edited should be “safe”. BBEdit 9 has a good implementation of such a feature. Once a minute, it silently and invisibly stores a copy of every open document window. If BBEdit crashes or otherwise exits abnormally (like, say, if the entire system goes down), when next you launch BBEdit, it restores your work to the last auto-saved state. The worst case scenario is that you lose 59 seconds of work. This is not about auto-saving your files in the file system — BBEdit’s auto-save will also restore untitled document windows that have never been saved as files. There’s no good reason why every application shouldn’t protect your work in a similar way.


But the more important conclusion is less obvious, which is that nearly everyone can benefit from the use of software that doesn’t require explicit file system management at all. Most of Apple’s iLife suite works this way, for example. There is no chore involved with adding music or video to your iTunes library, or importing a new batch of pictures to iPhoto. It’s rare to have, say, two songs with the same file name, but using iTunes you don’t have to worry about it. Just add them both and iTunes will figure out how to store them. iTunes became popular and useful before there was an iPod, and before there was an iTunes Store, because it absolved the user from managing music as discrete files in the file system. Instead of putting music files into a folder, all you had to do was *put it into iTunes*. Once you’ve added a song to iTunes you no longer need to worry about where it actually is in the file system.2


Everything on your computer is ultimately saved somewhere in the file system. But that doesn’t mean that you want to handle the actual filing by hand for everything. You don’t really want to know a lot of things about the specific technical details of how your data is saved, or if you did, you’d write your own app.


And those of you who object to these generalizations — those of you shaking your heads and saying to yourselves, *No, I very much do want to specify by hand the file name and location in the hierarchical directory structure for every bit of data on my system* — are almost certainly, I would wager, computer programmers. [To argue that users should embrace manual file system management](http://al3x.net/2009/01/31/against-everything-buckets.html) for every bit of data they wish to store is to argue against human nature.


## 3.


The obvious problem with Untitled Document Syndrome is in the rare cases where you lose data because you never saved it. The non-obvious problem is that the mental friction posed by the Save dialog often keeps you from ever even creating or saving small items of data in the first place.


This, I think, explains the relative popularity of Mac OS X’s included Stickies application. For years, Stickies’s popularity confounded me. Why would anyone use a note-taking utility that requires you to leave every saved note open in its own window on screen? The more you use it, the more cluttered it gets. But here’s the thing: cluttered though it may be, *you never have to save anything in Stickies*. Switch to Stickies, Command-N, type your new note, and you’re done. (And, yes, if you create a new sticky note, then force-quit Stickies, the note you just created will be there when next you launch the app. Stickies’s auto-save happens while you type, not just at quit time.) It feels easy and it feels safe. Stickies does not offer a good long-term storage design, but it offers a frictionless short-term jot-something-down-right-now design.


Let’s say, on the other hand, that your system for saving small text notes for future reference is to create them as individual files using a simple text editor. This, in fact, was *my* system for about four years. I kept a folder named “Misc.” and whenever I’d want to jot something down for future reference — movies I wanted to rent, the steps to go through to reboot a particular server, ideas for projects, anything — I’d create a new text file in that folder and jot the note down using BBEdit.


I started doing this at some point in 2001 and kept doing it until 2005, when I switched to [Yojimbo](http://www.barebones.com/products/yojimbo/).3 By the time I dropped my “folder full of text files” system, I had about 50 files in the folder — which works out to about one new file per month. As of this writing, I have 1,588 notes in Yojimbo — which works out to about one per day.


The single biggest advantage I’ve gained by switching to Yojimbo is that I actually use it. For any little thought or tidbit of information I want to remember, I create a new Yojimbo note. The result, now that I’ve accumulated several years worth of notes, occasionally amazes me. It’s like having a mind with an unfailing memory (which I most decidedly do not possess). Just one example, from earlier this week: I wear two-week disposable contact lenses, and, after making my first appointment with a new optometrist, realized that I threw away the box from my last pair without noting the exact brand and model. I check in Yojimbo with a search for “contact lens”, and, yes, there it is, from November 2007: *Bausch and Lomb Optima FW (SofLens 38)*.


Yojimbo is not alone in this category of utilities, and a detailed paean regarding the specific Yojimbo features I like best will require more space than even my generous standards for parenthetical digressions allow. But the key is that it minimizes friction. There’s little friction to create a new note, and little friction to search for existing ones. And you never have to explicitly save anything.


This is not an argument that *all* software should abstract the file system by using the library paradigm, but just that *more* software should. It’s like the aforementioned differences between the C and Perl “Hello world” programming examples. When you don’t have to do much before (or after) doing what you want to do, you do surprisingly more.


---

1. And “Hello world” is even more verbose in languages like [Java](http://www.javacoffeebreak.com/java101/java101.html) and [C#](http://msdn.microsoft.com/en-us/library/aa288463(VS.71).aspx). That’s not to say there’s anything wrong with either language; just that neither is particularly well-suited to writing quick little programs off the top of your head. ↩︎
2. But it’s worth noting that while apps like iTunes, iPhoto, and iMovie absolve the user from worrying about managing items in the file system, they don’t make it difficult to find the data you’ve stored within them in the file system if you really want to. Your data is all right there in obviously-named folders within the Music, Photos, and Movies folders in your home folder. ↩︎
3. Actually, about six months before switching to Yojimbo, I first started using an odd but extremely interesting little freeware program by Zachary Schneirov called [Notational Velocity](http://notational.net/). Notational Velocity hasn’t been updated since 2005, but it still works just fine. The premise behind Notational Velocity is almost preposterously simple: it offers [one window with three sections](https://daringfireball.net/misc/2009/02/notational-velocity.png): a title/search field at the top, a list of notes, and a text editing area. To search for a note, you type in the dual title/search field a substring matching the name or contents of any existing note; those that match appear in the list. To create a new note, you type a unique string in the same field and hit tab or return to switch focus to the text editing area. Sounds crazy but in practice it actually works just fine. [Merlin Mann wrote a nice review](http://www.43folders.com/2004/09/28/you-shall-know-us-by-our-notational-velocity) of Notational Velocity back in 2004.
There’s a famous design adage attributed to Albert Einstein, that everything should be as simple as possible but not simpler. Notational Velocity falls on just the wrong side of this. In November 2005 I imported all my notes from Notational Velocity into Yojimbo (which was then in private beta testing), and left Notational Velocity behind. The primary advantage I saw (and still see) in Yojimbo is that because its note format is RTF rather than plain text (like Notational Velocity), I could paste images into my notes. I’ve been using Yojimbo ever since. ↩︎



| **Previous:** | [Apple on the Mind at MWC](https://daringfireball.net/2009/02/apple_on_the_mind) |
| **Next:** | [Best Picture](https://daringfireball.net/2009/02/best_picture) |


PreviousNext