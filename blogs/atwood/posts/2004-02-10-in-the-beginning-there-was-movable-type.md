---
title: "In the beginning, there was Movable Type"
date: 2004-02-10
url: https://blog.codinghorror.com/in-the-beginning-there-was-movable-type/
slug: in-the-beginning-there-was-movable-type
word_count: 388
---

Writing code all day sort of saps my will to come home and... write more code. With that in mind I set out to find existing blog software rather than rolling my own. Life’s just too short, and besides, never write what you can steal – right?


I experimented with some .NET solutions but oddly enough had the most success with the [PERL-based Movable Type solution](http://www.movabletype.org/), which is what you’re reading this on right now. I suspect the .NET solutions may have been more advanced (I’m writing this now in a glorified textbox, not some fancy DHTML-Word simulator, for example), but this is the one that was easiest to get running. Easy is good. Also, I’m really lazy.


Anyway, if you want to get Movable Type running on your Windows Server 2003 as I did, you’ll need to get PERL installed first. I used [ActiveState PERL](http://www.activestate.com/Products/ActivePerl/). Installs painlessly. Note that Server 2003 has enhanced “lockdown” security out of the box – meaning, it won’t run jack squat without manual intervention – so you must enable .CGI as an allowed “Web Service Extension” in the IIS console.


![](https://blog.codinghorror.com/content/images/2025/06/image-64.png)


You’ll also need to make index.html one of the default content pages, and don’t forget to set up the .CGI extension mapping for PERL:


![](https://blog.codinghorror.com/content/images/2025/06/image-65.png)


I opted to store the blog in a [MySQL database](http://www.mysql.com/), which I set up with the defaults. I configured MySQL to run as a service using the command line, and set the default root password:

kg-card-begin: html

```
c:mysqlbinmysqld-nt --install
net start mysql
c:mysqlbinmysqladmin -u root password new_password
```

kg-card-end: html

I then used the Mascon GUI tool to create a new database “mtype.”


The Movable Type documentation is pretty good, so you’ll do OK if you follow it closely from this point on. There is one caveat that was not mentioned in the documentation, however. The ASPN Perl doesn’t come with the **required DBI PERL module**, so I almost immediately got an error when setting up my site. I found a link that offered the following commands to download and install it:

kg-card-begin: html

```
C:>c:perlbinppm.pl
If you have not already done so, install DBI:
ppm> install DBI
If this succeeds, install the MySQL database driver:
ppm> install DBD-Mysql
```

kg-card-end: html

After that it was smooth sailing.

[perl](https://blog.codinghorror.com/tag/perl/)
[movable type](https://blog.codinghorror.com/tag/movable-type/)
[.net](https://blog.codinghorror.com/tag/net/)
[blogging](https://blog.codinghorror.com/tag/blogging/)
[windows server](https://blog.codinghorror.com/tag/windows-server/)
