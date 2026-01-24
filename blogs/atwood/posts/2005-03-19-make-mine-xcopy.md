---
title: "Make Mine XCOPY"
date: 2005-03-19
url: https://blog.codinghorror.com/make-mine-xcopy/
slug: make-mine-xcopy
word_count: 420
---

Steve “what the heck does furrygoat mean” Makofsky crystallized a lot of my thoughts in his recent [rant on software installers](https://web.archive.org/web/20051029000616/http://www.furrygoat.com/2005/03/rant_install_pr.html). One of the biggest advantages of using the .NET framework is the way it enables XCopy deployments for the first time.* Installing a program by copying it to a folder was an utter fantasy in the VB6 world. In addition to the VB6 runtime, It took multiple first and/or third party OCX controls to do anything useful in a real app. And each of those OCX controls had their own dependencies.


**XCopy is the gold standard for correctly architected .NET software projects.** We should always be working toward that goal – making our software deployment as simple as dropping a few files in a folder – not putting in processes that make it easy for us to backslide into the bad old days. That’s the whole point of Microsoft abandoning the registry, COM+, and all the other associated meta-dependencies that made our life hell for so many years. If the design of your .NET project precludes XCopy deployment, take a long, hard look at what you’re doing. Don’t just treat the symptoms of the disease.


Now, there are other reasons you may want an installer anyway. For one thing, **I’m not sure users are ready for XCopy deployment.** Do we really expect users to be able to unzip an archive to a folder? No, I’m not being sarcastic. There are other amenities users expect in a software install, such as creating start menu icons, desktop icons, and integration with the add/remove programs section of Control Panel. Honestly, do you really think your program would end up in the Program Files folder if you left it up to the user? I’ll tell you where it would go – [on the desktop](https://web.archive.org/web/20051026040454/http://neopoleon.com/blog/posts/13304.aspx). Along with every other piece of software and every other document.


The installer is a distraction, but a necessary one for users’ sanity. If someone can propose another workable alternative, I’m all ears. I think the real lesson here is to **keep your project dependencies to a minimum**, and to absolutely master the dependencies you must have. Can your app run from [a USB keychain?](https://web.archive.org/web/20050324082926/http://loosewire.typepad.com/blog/2005/03/a_directory_of_.html) I realize that it’s not practical for all real world projects, but it should always be one of the goals.


*Delphi has also offered this kind of dependency-free “install” for years. Which may be one reason why it’s so incredibly popular amongst win32 utility authors.

[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[xcopy deployment](https://blog.codinghorror.com/tag/xcopy-deployment/)
[software installation](https://blog.codinghorror.com/tag/software-installation/)
[software deployment](https://blog.codinghorror.com/tag/software-deployment/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
