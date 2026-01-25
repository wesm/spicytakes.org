---
title: "There's Always More History"
date: 2020-12-08
url: https://www.hillelwayne.com/post/always-more-history/
slug: always-more-history
word_count: 1427
---

Last month I researched two historical questions. I originally posted summaries on Twitter and am reproducing both here.1


### Why Vim Uses hjkl


**Question:** Why does Vim use hjkl and not the arrow keys for navigation?


**Common Explanation:** It keeps your fingers on the home row.


**Historical Explanation:** Bill Joy developed vi on the ADM-3A, which didn’t have dedicated arrow keys. If you look at the ADM keyboard, it put the arrow keys on the hjkl keys. So Joy used that same logic for vi, which led to Vim.


The ADM keyboard. [(source)](https://catonmat.net/why-vim-uses-hjkl-as-arrow-keys)


**Deeper History**: It’s odd, though, that the ADM used hjkl for arrow keys. Why *those* letters?


There’s a very good reason for this. Here’s the 1967 version of the ASCII table:


![1967 ASCII table](ascii-table.png)

*(source)*


Each character has 7 bits. The first 32 characters are “control characters”, which were important for communication but weren’t actual characters. Computer keyboards, patterned off of QWERTY typewriters, needed a way to input these characters while keeping the same layout. They solved this with an extra “control” key to change inputs from physical characters to control characters. Holding down the control key would zero the 6th and 7th highest bits of the pressed key. If you wanted to send a backspace control character, you’d hold down ctrl+H (or ^H).2 That would convert `100 1000` to `000 1000`. Similarly, for a line separator, you’d press ^J.


If we flip through [the ADM manual](http://www.bitsavers.org/pdf/learSiegler/ADM_3/DP2880486F_ADM3A_UM_Apr86.pdf), we see that the ADM used “backspace” to mean “move the cursor left” without deleting the current character.3 With ^H and ^J already being used as left and down, it made sense to turn ^K and ^L into up and right. This means that ADM users were already navigating with hjkl and Bill Joy just followed the precedent for vi.


### Why JavaScript months start from 0


**Question:** In the JavaScript date API, months go 0-11, not 1-12. Why?


**Common Explanation:** It makes array indexing easier. You want to show the name of the month, not the number. You’d have an array with all the month names and use `date.getMonth()` to index it.


**Historical Explanation:** It’s this way to be compatible with Java, which was that way to be compatible with C.


**Deeper History:** Then why did C do it? And why is every calendar time field in C 0-indexed *except* the day of the month?


The ANSI C89 standard first officially established the fields of the `tm_date` structure, which remained almost entirely unchanged to the present day.4 The standard came out 17 years after C did and formalized a lot of what was already standard for various Unixes. If we then look back in [Unix history](https://minnie.tuhs.org/cgi-bin/utree.pl), we find that the [earliest C example](https://www.tuhs.org/cgi-bin/utree.pl?file=V5/usr/source/s3/ctime.c) of `<ctime.c>` didn’t use a struct, but instead stored the time data in an array.


```
#define SEC   0
#define MIN   1
#define HOUR  2
#define MDAY  3
#define MON   4
#define YEAR  5
#define WDAY  6
#define YDAY  7
#define ISDAY 8

```


`ctime` stores the time of day as second-minute-hour (SMH), while it’s displayed as HMS. This peculiarity makes sense when we look at how the code is actually used. Unix 5 only used this data for showing users the time:


```
asctime(t)
int *t;
{
    register char *cp, *ncp;
    register int *tp;

    cp = cbuf;
    for (ncp = "Day Mon 00 00:00:00 1900\n"; *cp++ = *ncp++;);
    ncp = &"SunMonTueWedThuFriSat"[3*t[6]];
    cp = cbuf;
    *cp++ = *ncp++;
    *cp++ = *ncp++;
    *cp++ = *ncp++;
    cp++;
    tp = &t[4];
    ncp = &"JanFebMarAprMayJunJulAugSepOctNovDec"[(*tp)*3]; // (a)
    *cp++ = *ncp++;
    *cp++ = *ncp++;
    *cp++ = *ncp++;
    cp = numb(cp, *--tp); // (b)
    cp = numb(cp, *--tp+100); // (c)
    cp = numb(cp, *--tp+100);
    cp = numb(cp, *--tp+100);
    cp =+ 2;
    cp = numb(cp, t[YEAR]);
    return(cbuf);
}

```


I’ve annotated some interesting lines. We first used the stored month at (a). Instead of storing all of the months names in an array, the developers stored the three-character abbreviations of each month in a single string and then used the month number as part of the pointer arithmetic to get the exact three bytes they needed. They then get the day (b) and then the HMS (c) by decrementing the pointer address three times. So storing it as SMH saves them an extra explicit jump (since they iterate through it backwards). They took advantage of the fact that, because the fields are stored as elements of an array, they are right next to each other *in memory*.5


This all tells us that they were optimizing *everything*. This makes sense, as the first versions of Unix were developed on the PDP-7. A decent computer in the 1970s might have a few kilobytes of memory. If you tried to store all of the month names in memory, that could be almost 10% of your *total* RAM!


So the developers needed to use as little memory and CPU as possible, and they did pointer arithmetic to save both, and the arithmetic is easier with 0-indexed months than with 1-indexed. On the other hand, they never used day of month for anything except user display (b), so that was stored directly in the representable form.


This explanation also explains a small inconsistency in the structure: `MDAY` (day of month) starts from 1, while `YDAY` (day of *year*) starts from 0. This is consistent in the “computation vs display” dichotomy, as the day of year is never shown to the user. It’s only used to calculate when daylight savings starts (in `sunday` and `localtime`).


---


Both of those explanations are incomplete. We can go deeper than “just” two layers of history. For the hjkl question, we can ask why the [ASCII table is laid out that way](https://textfiles.meulie.net/bitsaved/Books/Mackenzie_CodedCharSets.pdf). For the `tm_date` question, we can hunt down earlier versions of Unix, see what they did in assembly, or talk to the developers directly. And even that’s not the only layer. We can always look further, peeling back more and more layers of the history.


But two layers is enough for this essay. With two layers, we can see a common pattern in studying history, the difference between answers and explanation. When asked why something is the way it is, most people will give a post-hoc rationalization. They’ll see the present and come up with reasons why it’s “better” for things to be that way. If you look a little into the past, you often see that “things are this way because they were this way”. And if you look deeper, you see the forces that lead to things *becoming* that way.


That difference between the first and second layers of history leads to an unfortunate trap. People see the first layer and assume that’s all there is. This makes history seem irrelevant. Even if you realize there’s more to the story, excavating each layer takes considerably more work than the layer before. You can learn that Bill Joy used an ADM-3A with a quick web search. Finding the reasons beyond that took me two hours.


Some other examples of layers of history: Why do modern languages use `=` for assignment? The first layer is “blame C”, the second layer involved [tracing the chain of languages from ALGOL to C](https://www.hillelwayne.com/post/equals-as-assignment/). Why do so many interviewers ask linked list questions? The first layer is *Cracking the Coding Interview*, the second layer involved [reading hundreds of old Usenet posts and interviewing retired programmers](https://www.hillelwayne.com/talks/software-history/).


But it’s all worth the effort. Digging into the second layer teaches us much more about the context and reasons for why things are the way they are. And I can’t deny the puzzle aspect of it all, the joy in solving a mystery. Lost knowledge found again.


*Thanks to Lito Nicolai and [Alex Koppel](http://alexkoppel.com/) for feedback. I shared the first draft of this essay on my [newsletter](https://buttondown.email/hillelwayne/). If you like my writing, why not subscribe?*


---

1. The original threads are [here](https://twitter.com/hillelogram/status/1326600125569961991) and [here](https://twitter.com/hillelogram/status/1329228419628998665), though this essay supercedes both.
 [return]
2. This is also why bash will delete a character when you press `^H`.
 [return]
3. Deletion was done via the RUBOUT button, which was physically present on the keyboard. So far as I can tell, early computers didn’t use the convention that backspace should delete the character, but I’ve done a comprehensive review.
 [return]
4. The main change is that the C89 standard allows [two leap seconds](https://groups.google.com/g/comp.dcom.telecom/c/Qq0lwZYG_fI/m/Ttieu9Vu3QIJ) in a minute, while all modern standards allow one.
 [return]
5. Interestingly, [Unix 7](https://www.tuhs.org/cgi-bin/utree.pl?file=V7/usr/src/libc/gen/ctime.c) switches over to structs, but uses the same algorithm to pull out HMS. My guess is that it worked because of Undefined Behavior. 
 [return]
