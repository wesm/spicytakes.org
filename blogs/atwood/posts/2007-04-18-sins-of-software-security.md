---
title: "Sins of Software Security"
date: 2007-04-18
url: https://blog.codinghorror.com/sins-of-software-security/
slug: sins-of-software-security
word_count: 1417
---

I picked up a free copy of [19 Deadly Sins of Software Security](http://www.amazon.com/exec/obidos/ASIN/0072260858) at a conference last year. I didn’t expect the book to be good because it was a free giveaway item from one of the the vendor booths. But I paged through it on the flight home, and I was pleasantly surprised. It’s actually quite good.


![19 Deadly Sins of Software Security](https://blog.codinghorror.com/content/images/uploads/2007/04/6a0120a85dcdae970b0128777009b0970c-pi.png)


Software security isn’t exactly my favorite topic, so holding my interest is no mean feat. It helps that the book is mercifully brief and to the point, and filled with practical examples and citations. It’s an excellent cross-platform, language-agnostic check sheet of common software security risks.


Here’s a brief summary of each of the 19 sins, along with a count of the number of vulnerabilities I found in the [Common Vulnerabilities and Exposures database](http://cve.mitre.org/cve/) for each one.

kg-card-begin: html


|  | **Affected Languages** |  | **Exploit count** |
| Buffer Overflows | C, C++ | A buffer overrun occurs when a program allows input to write beyond the end of the allocated buffer. Results in anything from a crash to the attacker gaining complete control of the operating system. Many famous exploits are based on buffer overflows, such as [the Morris worm](http://en.wikipedia.org/wiki/Morris_worm). | [3,326](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=buffer+overflow) |
| Format String Problems | C, C++ | The standard format string libraries in C/C++ include some potentially dangerous commands (particularly %n). If you allow untrusted user input to pass through a format string, this can result in anything from arbitrary code execution to spoofing user output. | [411](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=format+string) |
| Integer Overflows | C, C++, others | Failure to range check on integer types. This can cause integer overflow crashes and logic errors. In C/C++, integer overflows can be turned into a buffer overrun and arbitrary code execution, but all languages are prone to denial of service and logic errors. | [288](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=integer+overflow) |
| SQL Injection | All | Forming SQL statements with untrusted user input means users can "inject" their own commands into your SQL statements. This puts your data at risk, and can even lead to complete server and network compromise. | [2,225](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=sql+injection) |
| Command Injection | All | Occurs when untrusted user input is passed to a compiler or interpreter, or worse, a command line shell. Potential risk depends on the context. | [193](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=execute+arbitrary+code) |
| Failing to Handle Errors | Most | A broad category of problems related to a program's error handling strategy; anything that leads to the program crashing, aborting, or restarting is potentially a denial of service issue and therefore can be a security problem, particularly on servers. | [80](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=errors) |
| Cross-Site Scripting (XSS) | Any web-facing | A web application takes some input from the user, fails to validate it, and echoes that input directly back to the web page. Because this code is running in the context of your website, it can do anything your website could do, including retrieving cookies, modifying the HTML DOM, and so forth. | [2,996](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=xss) |
| Failing to Protect Network Traffic | All | Most programmers underestimate the risk of transmitting data over the network, even if that data is not private. Attackers can eavesdrop, replay, spoof, tamper with, or otherwise hijack any unprotected data sent over the wire. | [26](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=replay) |
| Use of Magic URLs and Hidden Form Fields | Any web-facing | Passing sensitive or secure information via the URL querystring or hidden HTML form fields, sometimes with lousy or ineffectual "encryption" schemes. Attackers can use these fields to hijack or manipulate a browser session. | [33](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=hidden+form) |
| Improper use of SSL and TLS | All | Using most SSL and TLS APIs requires writing a lot of error-prone code. If programmers aren't careful, they will have an illusion of security in place of the actual security promised by SSL. Attackers can use certificates from lax authorities, subtly invalid certificates, or stolen/revoked certificates, and it's up to the developer to write the code to check for that. | [123](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=ssl) |
| Use of Weak Password-Based Systems | All | Anywhere you are using passwords, you need to seriously consider the risks inherent to all password-based systems. Risks like phishing, social engineering, eavesdropping, keyloggers, brute force attacks, and so on. And then you have to worry about how users choose passwords, and where to store them securely on the server. Passwords are a necessary evil, but tread carefully. | [1,235](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=password) |
| Failing to Store and Protect Data Securely | All | Information spends more time stored on disk than in transit. Consider filesystem permissions and encryption for any data you're storing. And try to avoid hardcoding "secrets" into your code or configuration files. | [56](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=encrypted) |
| Information Leakage | All | The classic trade-off between giving the user helpful information, and preventing attackers from learning about the internal details of your system. Was the password invalid, or the username? | [26](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=leakage) |
| Improper File Access | All | 1) There is often a window of vulnerability between time of check and time of use (TOCTOU) in the filesystem, so an attacker can slip changes in, particularly if the files are accessed over the network.

2) The "it isn't really a file problem"; you may think you have a file, but attackers may substitute a link to another file, or a device name, or a pipe.

3) Allowing users control over the complete filename and path of files used by the program; this can lead to directory traversal attacks. | [5](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=toctou), [58](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=traversal) |
| Trusting Network Name Resolution | All | It's simple to override and subvert DNS on a server or workstation with a local HOSTS file. How do you really know you're talking to the real "secureserver.com" when you make a HTTP request? | [20](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=dns+name) |
| Race Conditions | All | A race condition is when two different execution contexts are able to change a resource and interfere with each other. If attackers can force a race condition, they can execute a denial of service attack. Unfortunately, writing properly concurrent code is incredibly difficult. | [139](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=race+condition) |
| Unauthenticated Key Exchange | All | Exchanging a private key without properly authenticating the entity/machine/service that you're exchanging the key with. To have a secure session, both parties need to agree on the identity of the opposing party. You'd be shocked how often this doesn't happen. | [1](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-1623) |
| Cryptographically Strong Random Numbers | All | Imagine you're playing poker online. The computer shuffles and deals the cards. You get your cards, and then another program tells you what's in everybody else's hands. Random numbers are similarly fundamental to cryptography; they're used to generate things like keys and session identifiers. An attacker who can predict numbers—even with only a slight probability of success—can often leverage this information to breach the security of a system. | [5](http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=insufficiently+random) |
| Poor Usability | All | Security is always extra complexity and pain for the user. It's up to us software developers to go out of our way to make it as painless as it can reasonably be. *Security only works if the secure way also happens to be the easy way.* | All |


kg-card-end: html

It’s true that C and C++ have a heavy cross to bear. But only 3 of the 19 sins can be completely lumped on the plate of K&R. The other 16 apply almost everywhere, to any developer writing code on any platform. It’s a sobering thought.


The usability sin is the one that’s most interesting to me. **Usability is tough under the best of conditions – and security is the *worst* of conditions, at least from the user’s perspective.** It’s quite a challenge. There are a few great links in the book on the topic of security usability:

- [10 Immutable Laws of Security](https://web.archive.org/web/20070913110634/http://www.microsoft.com/technet/archive/community/columns/security/essays/10imlaws.mspx?mfr=true)
- [The 10 Immutable Laws of Security Administration](https://web.archive.org/web/20070705100518/http://www.microsoft.com:80/technet/archive/community/columns/security/essays/10salaws.mspx?mfr=true)
- [Writing Error Messages for Security Features](http://msdn2.microsoft.com/en-us/library/ms995351.aspx)
- [Why Johnny Can’t Encrypt: A Usability Evaluation of PGP 5.0](https://web.archive.org/web/20070613194309/http://www.gaudior.net/alma/johnny.pdf) (pdf)
- [Usability of Security: A Case Study](http://reports-archive.adm.cs.cmu.edu/anon/1998/CMU-CS-98-155.pdf) (pdf)
- [Are Usability and Security Two Opposite Directions in Computer Systems?](https://web.archive.org/web/20070624001519/http://rozinov.sfs.poly.edu/papers/security_vs_usability.pdf) (pdf)


You can certainly find other books that go much deeper on particular aspects of software security. But if you’re looking for an excellent primer on the entire gamut of security problems that could potentially afflict your project, 19 Deadly Sins of Software Security is an excellent starting point.

[security](https://blog.codinghorror.com/tag/security/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[software security practices](https://blog.codinghorror.com/tag/software-security-practices/)
[common vulnerabilities](https://blog.codinghorror.com/tag/common-vulnerabilities/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
