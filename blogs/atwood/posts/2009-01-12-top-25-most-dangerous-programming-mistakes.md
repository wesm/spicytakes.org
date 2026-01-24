---
title: "Top 25 Most Dangerous Programming Mistakes"
date: 2009-01-12
url: https://blog.codinghorror.com/top-25-most-dangerous-programming-mistakes/
slug: top-25-most-dangerous-programming-mistakes
word_count: 2064
---

I don’t usually do news and current events here, but I’m making an exception for the [CWE/SANS Top 25 Most Dangerous Programming Errors](http://cwe.mitre.org/top25/#Brief) list. This one is important, and deserves a wide audience, so I’m repeating it here – along with a brief hand-edited summary of each error.


**If you work on software in any capacity, at least skim this list.** I encourage you to click through for greater detail on anything you’re not familiar with, or that piques your interest.

1. [Client-Side Enforcement of Server-Side Security](http://cwe.mitre.org/data/definitions/602.html)


> Don’t trust the client to perform security checks on behalf of your server. Attackers can reverse engineer your client and write their own custom clients. The consequences will vary depending on what your security checks are protecting, but some of the more common targets are authentication, authorization, and input validation.

1. [Execution with Unnecessary Privileges](http://cwe.mitre.org/data/definitions/250.html)


> Your software may need special privileges to perform certain operations; wielding those privileges longer than necessary is risky. When running with extra privileges, your application has access to resources that the application’s user can’t directly reach. Whenever you launch a separate program with elevated privileges, attackers can potentially exploit those privileges.

1. [Use of Insufficiently Random Values](http://cwe.mitre.org/data/definitions/330.html)


> You may depend on randomness without even knowing it, such as when generating session IDs or temporary filenames. Pseudo-Random Number Generators (PRNG) are commonly used, but a variety of things can go wrong. Once an attacker can determine which algorithm is being used, he can guess the next random number often enough to launch a successful attack after a relatively small number of tries.

1. [Insecure Permission Assignment for Critical Resource](http://cwe.mitre.org/data/definitions/732.html)


> Beware critical programs, data stores, or configuration files with default world-readable permissions. While this issue might not be considered during implementation or design, it should be. Don’t require your customers to secure your software for you! Try to be secure by default, out of the box.

1. [Hard-Coded Password](http://cwe.mitre.org/data/definitions/259.html)


> Hard-coding a secret account and password into your software is extremely convenient – for skilled reverse engineers. If the password is the same across all your software, then every customer becomes vulnerable when that password inevitably becomes known. And because it’s hard-coded, it’s a huge pain to fix.

1. [Use of a Broken or Risky Cryptographic Algorithm](http://cwe.mitre.org/data/definitions/327.html)


> Grow-your-own cryptography is a welcome sight to attackers. Cryptography is hard. If brilliant mathematicians and computer scientists worldwide can’t get it right – and they’re regularly obsoleting their own techniques – then neither can you.

1. [Improper Access Control](http://cwe.mitre.org/data/definitions/285.html) (Authorization)


> If you don’t ensure that your software’s users are only doing what they’re allowed to, then attackers will try to exploit your improper authorization and exercise that unauthorized functionality.

1. [Incorrect Calculation](http://cwe.mitre.org/data/definitions/682.html)


> When attackers have control over inputs to numeric calculations, math errors can have security consequences. It might cause you to allocate far more resources than you intended – or far fewer. It could violate business logic (a calculation that produces a negative price), or cause denial of service (a divide-by-zero that triggers a program crash).

1. [Improper Initialization](http://cwe.mitre.org/data/definitions/665.html)


> If you don’t properly initialize your data and variables, an attacker might be able to do the initialization for you, or extract sensitive information that remains from previous sessions. If those variables are used in security-critical operations, such as making an authentication decision, they could be modified to bypass your security. This is most prevalent in obscure errors or conditions that cause your code to inadvertently skip initialization.

1. [Improper Resource Shutdown or Release](http://cwe.mitre.org/data/definitions/404.html)


> When your system resources have reached their end-of-life, you dispose of them: memory, files, cookies, data structures, sessions, communication pipes, and so on. Attackers can exploit improper shutdown to maintain control over those resources well after you thought you got rid of them. Attackers may sift through the disposed items, looking for sensitive data. They could also potentially reuse those resources.

1. [Download of Code Without Integrity Check](http://cwe.mitre.org/data/definitions/494.html)


> If you download code and execute it, you’re trusting that the source of that code isn’t malicious. But attackers can modify that code before it reaches you. They can hack the download site, impersonate it with DNS spoofing or cache poisoning, convince the system to redirect to a different site, or even modify the code in transit as it crosses the network. This scenario even applies to cases in which your *own* product downloads and installs updates.

1. [Failure to Control Generation of Code](http://cwe.mitre.org/data/definitions/94.html) (aka ‘Code Injection’)


> While it’s tough to deny the sexiness of dynamically-generated code, attackers find it equally appealing. It becomes a serious vulnerability when your code is directly callable by unauthorized parties, if external inputs can affect which code gets executed, or if those inputs are fed directly into the code itself.

1. [Untrusted Search Path](http://cwe.mitre.org/data/definitions/426.html)


> Your software depends on you, or its environment, to provide a search path (or working path) to find critical resources like code libraries or configuration files. If the search path is under attacker control, then the attacker can modify it to point to resources of the attacker’s choosing.

1. [External Control of File Name or Path](http://cwe.mitre.org/data/definitions/73.html)


> When you use an outsider’s input while constructing a filename, the resulting path could point outside of the intended directory. An attacker could combine multiple “...” or similar sequences to cause the operating system to navigate out of the restricted directory. Other file-related attacks are simplified by external control of a filename, such as symbolic link following, which causes your application to read or modify files that the attacker can’t access directly. The same applies if your program is running with raised privileges and it accepts filenames as input. Similar rules apply to URLs and allowing an outsider to specify arbitrary URLs.

1. [External Control of Critical State Data](http://cwe.mitre.org/data/definitions/642.html)


> If you store user state data in a place where an attacker can modify it, this reduces the overhead for a successful compromise. Data could be stored in configuration files, profiles, cookies, hidden form fields, environment variables, registry keys, or other locations, all of which can be modified by an attacker. In stateless protocols such as HTTP, some form of user state information must be captured in each request, so it is exposed to an attacker out of necessity. If you perform any security-critical operations based on this data (such as stating that the user is an administrator), then you can bet that somebody will modify the data in order to trick your application.

1. [Failure to Constrain Operations within the Bounds of a Memory Buffer](http://cwe.mitre.org/data/definitions/119.html)


> The scourge of C applications for decades, buffer overflows have been remarkably resistant to elimination. Attack and detection techniques continue to improve, and today’s buffer overflow variants aren’t always obvious at first or even second glance. You may think that you’re completely immune to buffer overflows because you write your code in higher-level languages instead of C. But what is your favorite “safe” language’s interpreter written in? What about the native code you call? What languages are the operating system API’s written in? How about the software that runs Internet infrastructure?

1. [Error Message Information Leak](http://cwe.mitre.org/data/definitions/209.html)


> Chatty error messages can disclose secrets to any attacker who misuses your software. The secrets could cover a wide range of valuable data, including personally identifiable information (PII), authentication credentials, and server configuration. They might seem like harmless secrets useful to your users and admins, such as the full installation path of your software – but even these little secrets can greatly simplify a more concerted attack.

1. [Race Condition](http://cwe.mitre.org/data/definitions/362.html)


> A race condition involves multiple processes in which the attacker has full control over one process; the attacker exploits the process to create chaos, collisions, or errors. Data corruption and denial of service are the norm. The impact can be local or global, depending on what the race condition affects – such as state variables or security logic – and whether it occurs within multiple threads, processes, or systems.

1. [Cross-Site Request Forgery (CSRF)](http://cwe.mitre.org/data/definitions/352.html)


> Cross-site request forgery is like accepting a package from a stranger – except the attacker tricks a user into activating a HTTP request “package” that goes to your site. The user might not even be aware that the request is being sent, but once the request gets to your server, it looks as if it came from the user – not the attacker. The attacker has masqueraded as a legitimate user and gained all the potential access that the user has. This is especially handy when the user has administrator privileges, resulting in a complete compromise of your application’s functionality.

1. [Cleartext Transmission of Sensitive Information](http://cwe.mitre.org/data/definitions/319.html)


> Information sent across a network crosses many different nodes in transit to its final destination. If your software sends sensitive, private data or authentication credentials, beware: attackers could sniff them right off the wire. All they need to do is control one node along the path to the final destination, any node within the same networks of those transit nodes, or plug into an available interface. Obfuscating traffic using schemes like Base64 and URL encoding offers no protection.

1. [Failure to Preserve OS Command Structure](http://cwe.mitre.org/data/definitions/78.html) (aka ‘OS Command Injection’)


> Your software acts as a bridge between an outsider on the network and the internals of your operating system. When you invoke another program on the operating system, and you allow untrusted inputs to be fed into the command string, you are inviting attackers into your operating system.

1. [Failure to Preserve Web Page Structure](http://cwe.mitre.org/data/definitions/79.html) (aka ‘Cross-site Scripting’)


> Cross-site scripting (XSS) is a result of combining the stateless nature of HTTP, the mixture of data and script in HTML, lots of data passing between web sites, diverse encoding schemes, and feature-rich web browsers. If you’re not careful, attackers can inject Javascript or other browser-executable content into a web page that your application generates. Your web page is then accessed by other users, whose browsers execute that malicious script as if it came from you – because, after all, it *did* come from you! Suddenly, your web site is serving code that you didn’t write. The attacker can use a variety of techniques to get the input directly into your server, or use an unwitting victim as the middle man.

1. [Failure to Preserve SQL Query Structure](http://cwe.mitre.org/data/definitions/89.html) (aka ‘SQL Injection’)


> If attackers can influence the SQL that you send to your database, they can modify the queries to steal, corrupt, or otherwise change your underlying data. If you use SQL queries in security controls such as authentication, attackers could alter the logic of those queries to bypass security.

1. [Improper Encoding or Escaping of Output](http://cwe.mitre.org/data/definitions/116.html)


> Insufficient output encoding is at the root of most injection-based attacks. An attacker can modify the commands that you intend to send to other components, possibly leading to a complete compromise of your application – not to mention exposing the other components to exploits that the attacker would not be able to launch directly. When your program generates outputs to other components in the form of structured messages such as queries or requests, be sure to separate control information and metadata from the actual data.

1. [Improper Input Validation](http://cwe.mitre.org/data/definitions/20.html)


> Ensure that your input is valid. If you’re expecting a number, it shouldn’t contain letters. Nor should the price of a new car be allowed to be a dollar. Incorrect input validation can lead to vulnerabilities when attackers can modify their inputs in unexpected ways. Many of today’s most common vulnerabilities can be eliminated, or at least reduced, with strict input validation.


Of course there’s nothing truly *new* here; I essentially went over the same basic list in [Sins of Software Security](https://blog.codinghorror.com/sins-of-software-security/) almost two years ago. The only difference is the relative priorities, as web applications start to dominate mainstream computing.


This list of software security mistakes serves the same purpose as McConnell’s [list of classic development mistakes](https://blog.codinghorror.com/escaping-from-gilligans-island/): to raise awareness. A surprisingly large part of success is recognizing the most common mistakes and failure modes. So you can – at least in theory – realize when your project is slipping into one of them. **Ignorance is the biggest software project killer of them all.**


Heck, even if you *are* aware of these security mistakes, you might end up committing them anyway. I know [I have](https://blog.codinghorror.com/protecting-your-cookies-httponly/).


Have you?

[security](https://blog.codinghorror.com/tag/security/)
[programming-errors](https://blog.codinghorror.com/tag/programming-errors/)
[software-development](https://blog.codinghorror.com/tag/software-development-2/)
[best-practices](https://blog.codinghorror.com/tag/best-practices-2/)
