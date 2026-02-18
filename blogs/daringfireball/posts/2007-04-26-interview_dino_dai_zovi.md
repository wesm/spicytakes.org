---
title: "Interview: Dino Dai Zovi"
date: 2007-04-26
url: https://daringfireball.net/2007/04/interview_dino_dai_zovi
slug: interview_dino_dai_zovi
word_count: 1784
---


*Dino Dai Zovi wrote the winning exploit in last week’s [CanSecWest MacBook Pro hacking contest](http://cansecwest.com/post/2007-04-20-14:54:00.First_Mac_Hacked_Cancel_Or_Allow). I interviewed Dai Zovi via email earlier this week.*


**Gruber:** What’s your background in computer security?


**Dai Zovi:**  My background is primarily on the “adversarial” or “offensive” side of security testing.  This typically involves playing the role of a determined and skilled attacker in order to compromise the security of a network, web application, software application, or operating system. This is done in order to test the security of the system in hostile conditions, find potential weaknesses, and improve the overall security of the system.  Most recently, I have made the jump to a more “defensive” role in security management.


**Gruber:** What were the rules of the CanSecWest contest, and how did you get involved?


**Dai Zovi:**  The contest involved the challenge to break into two Macs, a MacBook Pro 15-inch and 17-inch.  The laptops were both setup with default installations of Mac OS X 10.4 with all patches applied (including the security update released on April 19).  To win the 15-inch, the attacker had to remotely gain user-level access to the laptop.  To win the 17-inch, the attacker would have to remotely gain root-level access.  The laptops were setup on an open wireless network, allowing anyone to associate to the network and attack them.


The contest was set up in phases to progressively widen the attack surface.  In the first phase, the laptops would only be open to active remote attacks.  These are the types of attacks that may be launched at a machine remotely at any time.  For the second phase, the laptops would be opened up to web-based client-side remote attacks. These involved the laptop visiting potentially hostile web sites, created by the potential attackers.  The final phase would involve the laptops viewing mail in Mail.app as well.  In the end, only the first two phases were done.


I got involved later Thursday evening.  I got a phone call at around 9:30 pm ET and heard that no one had yet won the laptops, and that Friday was the last day of the conference.  It sounded like a great challenge, so I decided to work with Shane Macaulay to see if we could win this contest.  I sat down to begin looking for a web-based vulnerability at around 10 pm, had found one around 3 am, and had written a reliably working exploit around 7 am.


**Gruber:**  What did your exploit have to do on the Mac to prove it had user-level access?


**Dai Zovi:**  There were written instructions in a file in the home directory of the logged in user.  The attacker would have to compromise that user and follow the instructions contained there to prove that they had obtained that level of access.


**Gruber:**  I suspect some people might read this and think it’s good news that your exploit “only” gains user-level privileges. But an exploit like this is potentially catastrophic in the hands of an attacker. With user-level privileges, an exploit can read, delete, or corrupt anything in the user’s home directory — more or less all of the user’s own data. Technically, root exploits are harder and more powerful, but practically speaking, user-level privileges are all that an attacker needs. Correct?


**Dai Zovi:**  A remote root exploit is typically much harder to come by than a remote user privilege exploit.  However, in general, local user to root exploits are simpler to find than remote user-privilege exploits.  So, in general, it is reasonable to assume that once an attacker has local user access to a system, root is not difficult to obtain.  One should also point out, that if the user privileges are an admin user, it is possible to write to */Applications/* and */Library/*, and this access is quite damaging.  On a (primarily) single-user machine like a laptop or desktop, even non-admin user-level privileges are enough for most attacks (reading data, corrupting running applications, etc).


**Gruber:**  Right. You can replace your system software and apps with installer discs. If you don’t have backups — which is true for most people — you can’t replace your data.


How much can you say about the details of your exploit? Thomas Ptacek [reported](http://www.matasano.com/log/806/hot-off-the-matasano-sms-queue-cansec-macbook-challenge-won/) that, contrary to some initial reports, it isn’t specific to Safari, and that it can be defended against by disabling Java. Can you verify that? Is it specific to Intel-based Macs? Does it crash the browser?


**Dai Zovi:**  This vulnerability is a Java-based vulnerability in QuickTime.  QuickTime is installed by default on Mac platforms, so any web browser that uses Java on the Mac platform is vulnerable (Firefox and Safari have been confirmed to be vulnerable).  Firefox on Windows is also considered to be at risk. On all platforms, disabling Java would mitigate this vulnerability.


**Gruber:**  Do you think there’s any reason to believe this vulnerability is being taken advantage of in the wild? I’m not suggesting it leaked out from your successful exploit at CanSecWest — I’m curious whether you suspect others have previously discovered it independently.


**Dai Zovi:**  I do not know of any cases of this vulnerability being exploited in the wild.  I have personally kept very close controls on the information related to the vulnerability, and hope that this has been sufficient to limit independent rediscovery of the vulnerability after its existence had been announced last week.  I have been in this business, however, long enough to know the fallacy in believing that a vulnerability is only discovered by one person.  For example, the last vulnerability I reported to Apple, a local root exploit involving Mach exception ports, was independently discovered by a college student in Amsterdam.  This student had kept an exploit (an exploit more elegant than mine, I might add) for the vulnerability in a publicly accessible web directory.  It turns out that they had discovered the vulnerability before I had reported it to Apple.  Who knows what they, or anyone who had stumbled across their exploit, had done with it. And I know that this is not an isolated occurrence.


**Gruber:**  Do you use a Mac as your primary computer? If so, what security precautions do you take? I’m going to go out on a limb and predict you do not use any sort of commercial anti-virus package.


**Dai Zovi:**  I use a Mac as my primary, secondary, and tertiary computers :).  I take some extra security precautions such as always running as a non-admin account, using separate encrypted disk images and keychains for different purposes, and isolating data on different machines.  I also take some extra precautions that I’m not going to advertise publicly :).  I do not, however, run any commercial anti-virus packages.


**Gruber:**  Are there any precautions you think typical Mac users should take that they aren’t now?


**Dai Zovi:**  I would recommend they make their primary user account a non-admin user, I think that is a reasonable compromise between usability and security.  I would also recommend that more security-conscious users create a separate keychain with a 5 minute timeout for important passwords.  Even if the user is using FileVault, a separate encrypted disk image for sensitive financial or personal documents is another simple and prudent measure to protect your personal information.


**Gruber:**  Do you use FileVault? I don’t. I do store financial and private information on encrypted disk images, but I’m wary of storing my entire home directory on one. I feel like I’m far more likely to run into problems with my disk than I am to run into a security problem, and FileVault can make it harder to recover files if things go south with the drive.


**Dai Zovi:**  I had previously used FileVault on my laptops without much incident when I was traveling and doing consulting.  These days, I am no longer doing consulting and traveling less, so I am not using it.  I do still use separate encrypted disk images for different types of data.


**Gruber:**  I’ve heard claims that there exist a handful of known Mac OS X exploits amongst security experts. Do you believe — or know — this to be the case?


**Dai Zovi:**  Security experts quite often have exploits for vulnerabilities that they have discovered and the vendor is in the progress of addressing. Some others choose not to report the vulnerabilities that they find. So I would not be surprised if there were a number of OS X exploits floating around, I have already seen evidence of this in the past (i.e. the Mach exception ports exploit).


**Gruber:**  You weren’t at the CanSecWest conference, but the vulnerability discovery and exploit to take advantage of it were your work. You split the prize with your friend Shane Macaulay, who was attending. He gets the MacBook Pro, you get the $10,000. Would you have gotten involved if the cash hadn’t been added to the prizes?


**Dai Zovi:**  Yes.  For me, the challenge, especially with the time pressure, was the real allure.


**Gruber:**  $10,000 is a nice purse. Are you aware of any other similar contests with prizes this high? Is this common?


**Dai Zovi:**  In 2001, Argus offered $48,000 to anyone who was able to break into their PitBull operating system, a trusted operating system based on Solaris 7.  A Polish group called “Last Stage of Delirium”, made up of Michal Chmielewski, Sergiusz Fornrobert, Adam Gowdiak and Tomasz Ostwald won Argus’ hacking challenge.  While Argus publicly announced that LSD had won the challenge, after 18 months, they had only paid $5000 of the total prize amount and cut off communication with LSD.


TippingPoint has offered similar amounts of money for critical vulnerabilities in Microsoft Windows, but that was for any vulnerabilities submitted over a month’s time, not just three days as it was in this case.


**Gruber:**  You had nice things to say in your interview with Ryan Naraine about your experience reporting findings to Apple. Do you think there’s anything Apple should do different with Mac OS X itself that would improve security? (E.g. do you think Apple should change the first-run configuration UI so as to encourage users to create non-admin accounts?)


**Dai Zovi:**  I think Apple is to be commended for proactively releasing updates for internally identified security vulnerabilities, which is a stance that few other software vendors take.  Apple should implement some of the security defenses that other operating systems have adopted such as Address Space Layout Randomization and other stack and heap protections.  I think Apple should provide the option to create both admin and non-admin accounts in the first run as well as make it easier to store passwords in non-login keychains.



| **Previous:** | [Coda](https://daringfireball.net/2007/04/coda) |
| **Next:** | [Google Lucky Search Scripts for ThisService](https://daringfireball.net/2007/04/google_lucky_thisservice) |


PreviousNext