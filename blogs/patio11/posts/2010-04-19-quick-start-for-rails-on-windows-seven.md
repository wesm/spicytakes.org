---
title: "Quick Start For Rails on Windows Seven"
date: 2010-04-19
url: https://www.kalzumeus.com/2010/04/19/quick-start-for-rails-on-windows-seven/
slug: quick-start-for-rails-on-windows-seven
word_count: 247
---


Today I killed a few hours getting my Rails environment working on my brand new shiny 64 bit Windows Seven laptop.  These instructions should also work with Windows Vista.  I’m assuming you’re a fairly  experienced Rails developer and just ended in dependency purgatory like I did for the last few hours.

1. Grab the MySQL developer version for your architecture (32 bit or 64 bit as appropriate) [here](http://www.mysql.com/downloads/mysql/).
2. Grab Ruby [here](http://rubyforge.org/frs/?group_id=167).  I used the 1.8.6 RC2 installer for my 64 bit architecture.
3. Add C:\Ruby\bin to your path.  You can do this on Windows by opening the Start Menu, right clicking My Computer, clicking Properties, clicking Advanced / System Settings, and then adding it to the end of the PATH variable on the lower of the two dialogs.  Apologies for inexact setting names, my computer is Japanese so I’m working from memory.
4. Verify that your path includes C:\Ruby\bin by opening a new command line and executing “path”.
5. Good to go?  OK, execute:


```
gem install --no-rdoc --no-ri rails
gem install mysql
```


You’ll get all manner of errors on that MySQL installation. That is OK.

1. Here’s the magic: copy libmySQL.dll from [here](http://instantrails.rubyforge.org/svn/trunk/InstantRails-win/InstantRails/mysql/bin/) to C:\Ruby\bin . **If you do not do this**, you will get ugly errors on Rails startup about not being able to load mysql_api.so.


You should now be able to successfully work with Rails as you have been previously, even from your Windows machine, and you will amaze your Mac-wielding friends.
