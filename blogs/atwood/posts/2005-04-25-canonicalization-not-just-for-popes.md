---
title: "Canonicalization: Not Just for Popes"
date: 2005-04-25
url: https://blog.codinghorror.com/canonicalization-not-just-for-popes/
slug: canonicalization-not-just-for-popes
word_count: 614
---

You may remember the [ASP.NET canonicalization vulnerability](https://web.archive.org/web/20050831020741/http://support.microsoft.com/?kbid=887459) from last year. And what exactly is canonicalization? From Microsoft’s [Design Guidelines for Secure Web Applications](https://web.archive.org/web/20100518120944/http://msdn.microsoft.com/en-us/library/ff648647.aspx):


> ***Data in canonical form is in its most standard or simplest form.** Canonicalization is the process of converting data to its canonical form. File paths and URLs are particularly prone to canonicalization issues and many well-known exploits are a direct result of canonicalization bugs. For example, consider the following string that contains a file and path in its canonical form.
> `c:\temp\somefile.dat`
> The following strings could also represent the same file.
> `somefile.datc:\temp\subdir\..\somefile.dat c:\temp\somefile.dat\ ..somefile.datc%3A%5Ctemp%5Csubdir%5C%2E%2E%5Csomefile.dat`
> In the last example, characters have been specified in hexadecimal form:*
> *• %3A is the colon character.*
> *• %5C is the backslash character.*
> *• %2E is the dot character.*
> *You should generally try to avoid designing applications that accept input file names from the user to avoid canonicalization issues. Consider alternative designs instead. For example, let the application determine the file name for the user. If you do need to accept input file names, make sure they are strictly formed before making security decisions such as granting or denying access to the specified file.*


Seems straightforward enough; there can be only one true representation of the data, just like there’s only one Pope. **And popes don’t canonicalize: they **[**canonize**](http://en.wikipedia.org/wiki/Canonize)**.** Which means the words “canonicalize” and “canonicalization” are *artificially fabricated technical mumbo-jumbo*. As if we didn’t have [enough of that](http://msdn.microsoft.com/en-us/magazine/cc163825.aspx) to go around already:


> *We are asking for your help in eradicating words that have been invented for no good reason. Sometimes, it’s too late to do anything about them. Look at the word “canonicalize,” for instance. It is used to mean “to create the canonical form” of something, like a URL (as in InternetCanonicalizeUrl from the WinINet API). It’s not English; it was invented because someone didn’t know that there was already a perfectly adequate word for this process: “canonize.” However, once this non-word has been created, the rules of the language suddenly apply again, so the process of “canonicalizing” something is “canonicalization” instead of “canonization.”
> More recently, we’ve seen the word “performant” start its crawl into the everyday vocabulary of devspace. It is used to mean “highly performing.” It’s also not a word. When something provides information, it’s informative. It’s not “informant.” The word “performant,” if it existed, would be a noun – not an adjective. But it doesn’t exist, so if you do see it in print, remember that it’s not really there.
> Any readers who have made it this far are probably rolling their eyes now, thinking to themselves, “Why are they being such sticklers here? Isn’t the language a wonderful, evolving thing?” Yes, our language is evolving. As there is a need for new words, new words enter the language. But **making up new words is just as bad as using fancy words in place of short ones.** Why say “This project’s goals are orthogonal to the company’s needs?” Admit it – if you were at home, you’d just say “different from” or “at odds with.”*


It’s one thing to use technical jargon excessively, but the perpetuation of *new* jargon for jargon’s sake is particularly Orwellian. Along those same lines, you may also be interested in Cyrus’ [list of commitments](https://web.archive.org/web/20051205091839/http://blogs.msdn.com/cyrusn/archive/2005/04/24/411418.aspx).

1. reinvent value-added markets
2. brand e-business technologies
3. benchmark value-added content
4. optimize one-to-many infrastructures
5. enable innovative niches
6. integrate real-time mindshare
7. aggregate collaborative content
8. repurpose transparent platforms
9. reinvent visionary solutions
10. visualize end-to-end initiatives


Is it clear? As an unmuddied lake, sir. As clear as an [azure sky of deepest summer](http://www.imdb.com/title/tt0066921/).

[security](https://blog.codinghorror.com/tag/security/)
[canonicalization](https://blog.codinghorror.com/tag/canonicalization/)
[vulnerability](https://blog.codinghorror.com/tag/vulnerability/)
[web applications](https://blog.codinghorror.com/tag/web-applications/)
