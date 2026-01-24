---
title: "Does Anyone Actually Read Software EULAs?"
date: 2007-06-21
url: https://blog.codinghorror.com/does-anyone-actually-read-software-eulas/
slug: does-anyone-actually-read-software-eulas
word_count: 1043
---

If you’ve used a computer for any length of time, you’ve probably clicked through hundreds of **End User License Agreement (EULA) dialogs**. And if you’re like me, you haven’t read a single word of any of them.


![Windows XP EULA text in German](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b012877700f72970c-pi.png)


Who can blame you? They’re mind-numbing legalese. As a software developer, I understand that [choosing a software license](https://blog.codinghorror.com/pick-a-license-any-license/) for my code is helpful to my fellow developers. But who, exactly, benefits from an *end-user* license agreement?


![Firefox 2 EULA dialog](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b012877700f80970c-pi.png)


I’m an end user, and I don’t recall anything good ever coming from clicking that “I accept” option. It’s just another meaningless hoop I have to jump through before I can actually use the software. For all I know, the EULA could specify that the software is going to install a keylogger, steal all my passwords and financial information, send incriminating emails threatening the president, format my hard drive, and then sleep with my wife. How would I know? I blindly clicked that big, fat accept button, same as I always have.


Short of [writing software to read the EULA](http://www.javacoolsoftware.com/eulalyzer.html) and automatically flag such problems – a conceptually brilliant solution to an intractable problem – what’s a poor “end user” to do?

kg-card-begin: html
kg-card-end: html

The EFF points out a few [common problems with EULA agreements](https://www.eff.org/wp/dangerous-terms-users-guide-eulas) you might want to watch out for:

1. **“Do not criticize this product publicly.”**
Hidden within the terms of many EULAs are often serious demands asking consumers to sign away fundamental rights. Many agreements on database and middleware programs forbid the consumer from comparing his or her product with another and publicly criticizing the product. This obviously curtails free speech, and makes it more difficult for consumers to get accurate information about what they’re buying by inhibiting professional watchdog groups like Consumer Reports from conducting independent reviews.
2. **“Using this product means you will be monitored.”**
Many products come with EULAs with terms that force users to agree to automatic updates – usually by having the computer or networked device contact a third party without notifying the consumer, thus potentially compromising privacy and security.
3. **“Do not reverse-engineer this product.”**
Some EULA terms harm people who want to customize their technology, as well as inventors who want to create new products that work with the technology they’ve bought. “Reverse-engineering,” which is often forbidden in EULAs, is a term for taking a machine or piece of software apart in order to see how it works. This kind of tinkering is explicitly permitted by federal law – it is considered a “fair use” of a copyrighted item. Courts have held that the fair use provisions of the US Copyright Act allow for reverse-engineering of software when the purpose is to create a non-infringing interoperable program.
4. **“Do not use this product with other vendor's products.”**
Vendors use EULAs to make consumers agree that they won’t use products that evaluate the performance of the software they’ve bought, or that can be used to uninstall all or part of the program. Essentially, clicking “I Agree” to such a EULA means that you’re not supposed to reconfigure your computer to touch or remove the software you’ve just installed. These kinds of EULA terms have become popular lately because many vendors support free versions of their products by packaging them with third-party programs that serve ads or gather information about consumer habits for marketing companies. If users uninstalled such ride-along programs at will, the vendors might lose revenue. For example, Claria (formerly Gator) is a company that delivers pop-up ads and pays to have its GAIN software bundled in free versions of popular file-sharing program Kazaa.
5. **“By signing this contract, you also agree to every change in future versions of it. Oh yes, and EULAs are subject to change without notice.”**
Put simply, this means that when you install iTunes, you are not only agreeing to all the onerous terms in the box, but you are also agreeing to future terms that may appear in the iTunes Terms of Service months or years from now. These terms are subject to change without notice, and you don’t even get a chance to click through this future “contract” and agree. Mere “continued use of the iTunes Music Store” constitutes your agreement to contractual terms that you may not be aware exist. These kinds of terms are ubiquitous in EULAs and in Terms of Service for countless products.
6. **“We are not responsible if this product messes up your computer.”**
The disclaimer of liability for faulty software is perhaps the most important function of a EULA from the manufacturer’s perspective. And it’s bad news for the consumer. This term purports to supplant traditional consumer protection and products liability law. Clicking yes on EULAs containing this common clause means that the consumer cannot file class-action lawsuits against the vendor for faulty products, or for products that do not do all the things that the company advertised they would.


I’ve presented only the summary highlights; I highly recommend reading [the rest of the EFF article](https://www.eff.org/wp/dangerous-terms-users-guide-eulas) for much more detail. Unfortunately, following any of the EFF’s advice requires reading the EULA in minute detail, a time commitment that few are willing to make.


What I’ve pictured above are known as [click-wrap licenses](http://en.wikipedia.org/wiki/EULA#Shrink-wrap_and_click-wrap_licenses). Clicking through indicates assent to the license. But did you know that **the physical act of opening some software can subject you to shrink-wrap license terms**? Cory Doctorow calls shrinkwrap licenses [an epidemic of lawsuits waiting to happen](http://www.informationweek.com/shrinkwrap-licenses-an-epidemic-of-lawsuits-waiting-to-happen/d/d-id/1051535). I’m not sure about the lawsuit epidemic, but the jury is definitely still out on whether or not clickwrap and shrinkwrap EULAs are enforceable – or even meaningful.

kg-card-begin: html

> Clickwrap and shrinkwrap agreements all start with the phrase [READ CAREFULLY](http://reasonableagreement.org/), in caps. The phrase means, “IGNORE THIS.” That’s because the small print is unchangeable and outrageous.
> Why read the “agreement” if you know that:
> No sane person would agree to its text, and
> Even if you disagree, no one will negotiate a better agreement with you?

kg-card-end: html

Given the insanity of our current predicament, *not* reading the EULA could very well be the most rational course of action.

[legalese](https://blog.codinghorror.com/tag/legalese/)
[end-user license agreement](https://blog.codinghorror.com/tag/end-user-license-agreement/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[security](https://blog.codinghorror.com/tag/security/)
