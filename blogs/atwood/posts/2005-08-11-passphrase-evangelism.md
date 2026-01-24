---
title: "Passphrase Evangelism"
date: 2005-08-11
url: https://blog.codinghorror.com/passphrase-evangelism/
slug: passphrase-evangelism
word_count: 674
---

The article [Passwords: The Weakest Link](https://web.archive.org/web/20061215105129/http://news.com.com/Passwords+The+weakest+link/2009-1001_3-916719.html) references a 25 year old research work on the efficacy of passwords:


> In the pre-Internet Age of 1979, when storage was measured in the number of bits that could fit on a foot of magnetic tape, a [seminal paper on password security](http://portal.acm.org/citation.cfm?id=359168.359172) found that **a third of users’ passwords could be broken in less than five minutes.**


This article was written in 2002, and the password security picture hasn’t improved at all in the intervening 23 years:


> When a regional health care company called in network protection firm Neohapsis to find the vulnerabilities in its systems, the Chicago-based security company knew a sure place to look.
> Retrieving the password file from one of the health care company’s servers, the consulting firm put “[John the Ripper](http://www.openwall.com/john/),” a well-known cracking program, on the case. While well-chosen passwords could take years – if not decades – of computer time to crack, **it took the program only an hour to decipher 30 percent of the passwords for the nearly 10,000 accounts listed in the file.**
> “Just about every company that we have gone into, even large multinationals, has a high percentage of accounts with easily (cracked) passwords,” said Greg Shipley, director of consulting for Neohapsis. “We have yet to see a company whose employees don’t pick bad passwords.”


When there’s no measurable improvement in password security between 1979 and 2005, clearly we aren’t dealing with a technology problem. We’re dealing with a people problem. **Passwords are fundamentally broken because they aren’t compatible with typical human behavior** :


> The only defense is to make passwords nearly impossible to guess, but such strength requires that the password be selected in a totally random fashion. That’s a tall order for humans, said David Evans, an assistant professor of computer science at the University of Virginia.
> “When humans make passwords, (they) are not very good at making up randomness,” he said. Furthermore, because people usually have several passwords to keep track of, locking user accounts with random, but difficult-to-remember, strings of characters such as “wX%95qd!” is a recipe for a support headache. “The idea is to make something that is easy to remember but that will make up a good password,” he said.
> Many security administrators focus their efforts on teaching users how to use various mnemonics to create strong, but memorable, passwords. A common technique takes the first or last letter of each word in a saying or phrase familiar to the user. For example, by using random capitalization and substituting some punctuation marks and digits for letters, “Friends don’t let friends give tech advice” might become “fD!Fg7a.”
> The education doesn’t seem to be sticking, and the password problem is getting worse as the percentage of less-tech-savvy computer users increases.


I don’t have a solution to the password problem, but there is one thing we can do to improve the usability and security of passwords dramatically.


We have to encourage users to **stop thinking of passwords as single words**, and start thinking of them as [pass phrases.](https://blog.codinghorror.com/passwords-vs-pass-phrases/) The worst imaginable pass phrase (e.g., “this is my secret password”) is many times more secure than an average single word password (e.g., “god123”). And it’s easier to remember.*


As a developer, you need to do your part, too:

1. Absolutely, positively **make sure your applications support a password field length of at least 128 unicode characters**.
2. In the user interface for defining the password, **remind the user that password doesn’t literally mean a word**. Give several examples of pass phrases directly alongside the entry field. It’s absolutely imperative that we educate the users – how else will they know there’s some other way to deal with that input box?


The greatest long term security threat isn’t hackers. It’s the perpetuation of the braindead 8-16 character password length limitation, and the idea that passwords are single words.


*Unfortunately, not easier to type, but neither is “X74@&z3!.” What are you gonna do?

[security](https://blog.codinghorror.com/tag/security/)
[password security](https://blog.codinghorror.com/tag/password-security/)
[network protection](https://blog.codinghorror.com/tag/network-protection/)
[password strength](https://blog.codinghorror.com/tag/password-strength/)
[cracking程序](https://blog.codinghorror.com/tag/crackingcheng-xu/)
