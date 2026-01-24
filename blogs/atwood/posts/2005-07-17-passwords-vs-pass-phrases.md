---
title: "Passwords vs. Pass Phrases"
date: 2005-07-17
url: https://blog.codinghorror.com/passwords-vs-pass-phrases/
slug: passwords-vs-pass-phrases
word_count: 920
---

Microsoft security guru Robert Hensing hit a home run his first time at bat with his [very first blog post](https://web.archive.org/web/20051102035906/http://blogs.technet.com/robert_hensing/archive/2004/07/28/199610.aspx). In it, he advocates that passwords, as we traditionally think of them, should not be used:

kg-card-begin: html

> So here’s the deal - **I don’t want you to use passwords, I want you to use pass-PHRASES.**  What is a pass-phrase you ask? Let’s take a look at some of my recent pass-phrases that I’ve used inside Microsoft for my ‘password’.
> “If we weren’t all crazy we would go insane” (Jimmy Buffett rules)*
> “Send the pain below!”
> “Mean people suck!”
> So why are these pass-phrases so great?
> They meet all password complexity requirements due to the use of upper / lowercase letters and punctuation (you don’t HAVE to use numbers to meet password complexity requirements)
> They are so freaking easy for me to remember it’s not even funny.  For me, I find it MUCH easier to remember a sentence from a favorite song or a funny quote than to remember ‘xYaQxrz!’ (which b.t.w. is long enough and complex enough to meet our internal complexity requirements, but is weak enough to not survive any kind of brute-force password grinding attack with say LC5, let alone a lookup table attack).  That password would not survive sustained attack with LC5 long enough to matter so in my mind it’s pointless to use a password like that.  You may as well just leave your password blank.
> I dare say that even with the most advanced hardware you are not going to guesss, crack, brute-force or pre-compute these passwords in the 70 days or so that they were around (remember you only need the password to survive attack long enough for you to change the password).

kg-card-end: html

Windows 2k and higher support passwords of up to 127 unicode characters. So this will work on virtually every Windows network in existence. Reggie Burnett, however, [has some doubts](https://web.archive.org/web/20060106040544/http://www.bytefx.com/blog/PermaLink,guid,d89cd782-4b49-4202-8d9b-9bfd11004123.aspx):


> The reason I think that Robert’s logic is a bit flawed is that a pass phrase is likely to contain readable words (else it really isn’t a pass phrase) and therefore can be attacked not at the letter level but at the word level. According to various sites I visited, the average English speaker knows about 20,000 words but uses only about 2,000 of those in a given week. Since the user is likely to use words they are used to, we can safely say that most pass phrases will contain one of about 5,000 words. And, if a pass phrase contains 4 words, then our possibilities are 5000^4. I’ll spare you the math, but you’ll see that the cracker that is trying pass phrases has a lot fewer possibilities to try. Now, of course, using more words will increase the security, but we should also note that since the attack is at the word level, the length of the word would not matter. “Mean people suck” would be just as secure as “Extremely important password.” They are both 3 words and both use common words.


While I see his point, he’s completely ignoring the capitalization and punctuation in “Mean people suck!”. I do agree that for the best security, **your passphrase should include capitalization, punctuation, and possibly even numbers** if you can work them in there in a logical way. Andy Johns [elaborates](https://web.archive.org/web/20060426145029/http://geekswithblogs.net/ajohns/archive/2004/07/28/8955.aspx):


> As I’ve often mentioned, I’m a consultant and I see a lot of crap out in the wild. By far the most annoying crap I see is around passwords. The more paranoid the network admins (or security council, or board, or whoever sets the rules) the more obscure the passwords must be, and the more often they need to be changed. **What these people fail to realize is the average human worker just wants to do their job, and can’t remember Syz8#K3! as a password.** So what do they do... Out comes the post-it-note on the desk, or in the drawer, or under the keyboard, or the file on the desktop called “passwords.txt.” Some workers try and be smart by leaving out a letter, or writing it backwards... but still, if your password is so hard to remember that you have to write it down, then you have no security at all, and a significant portion of your support staff/costs must be spent dealing with resetting passwords.
> A pass-phrase of “this is my password and it’s for my eyes only” is far easier to remember than Syz8#K3! and also far more secure, and nearly takes the same amount of time to type. Need more security, throw in a few caps, or numbers: “My address is 1234 Main street” or “Jenny’s number is 867-5309.” Yes, I’m breaking rules about not including personal information in a password, but remember, 1) these are examples, and 2) a pass-phrase is different. A password of “Chris” because your son’s name is Chris is a bad password, but a password of: “My oldest son’s name is Chris and he is 10 years old” is a good password.


Passphrases are clearly more usable than traditional “secure” passwords. They are also highly likely to be more secure. Even naïve worst-case passphrases like “this is my password” aren’t all that hackable, at least when compared to their single word equivalents, e.g., “password.”


Easier on the user, harder for hackers: that’s a total no-brainer. I’ve adopted passphrases across the board on all the systems I use.


*ugh

[passwords](https://blog.codinghorror.com/tag/passwords/)
[pass-phrases](https://blog.codinghorror.com/tag/pass-phrases/)
[password security](https://blog.codinghorror.com/tag/password-security/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
