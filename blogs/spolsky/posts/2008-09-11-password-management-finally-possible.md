---
title: "Password management finally possible"
date: 2008-09-11
url: https://www.joelonsoftware.com/2008/09/11/password-management-finally-possible/
word_count: 307
---


*[Editor’s Note: This article is almost a decade old. Today there are many password managers available which are fairly easy to use and well-integrated with modern tools. [Wirecutter has a good review](https://thewirecutter.com/reviews/best-password-managers/) of some modern options. No matter what you do, [don’t reuse passwords](https://pixelprivacy.com/resources/reusing-passwords/) from one site on another site!]*


Now that DropBox is shipping, there’s finally a good way to manage all your passwords. This system works no matter how many computers you use regularly; it works with Mac, Windows, and Linux; it’s secure; it doesn’t expose your passwords to any internet site (whether or not you trust it); it generates highly secure, random passwords for each and every site, it’s fairly easy to use once you have it all set up, it maintains an automatic backup of your password file online, and it’s free.

1. Sign up for [DropBox](http://dropbox.com/). This gives you a folder on your computer that can, magically, be synchronized onto every computer you use. Whenever you change a file on one computer, the change is automatically propagated to your other computers.
2. On all your Windows computers, install [PasswordSafe](https://pwsafe.org). This is a little program that maintains an encrypted password file for you for all the sites you visit regularly. It will even generate long, complicated passwords full of special characters. The file itself is encrypted… if someone gets their hands on it, it’s worthless without the master password you created for it. Store the file in your DropBox folder, of course.
3. On all your Macintosh and Linux computers, install [Password Gorilla](https://github.com/zdia/gorilla/wiki). This works just like PasswordSafe and uses the same file format.


That’s really all there is to it. There is one optional step:

1. Log on to all your bank accounts and change that “abcd” password to some long 16 digit, unique, secure password that PasswordSafe makes up for you.
