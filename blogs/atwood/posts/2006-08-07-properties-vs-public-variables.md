---
title: "Properties vs. Public Variables"
date: 2006-08-07
url: https://blog.codinghorror.com/properties-vs-public-variables/
slug: properties-vs-public-variables
word_count: 594
---

I occasionally see code with properties like this:

kg-card-begin: html

private int name;



public int Name

{

    get { return name; }

    set { name = value; }

}

kg-card-end: html
As I see it, there are three things to consider here.
kg-card-begin: html

**When is a property not a property? When it’s a glorified public variable.**
Why waste everyone’s time with a bunch of meaningless just-in-case wrapper code? Start with the simplest thing that works – a public variable. You can always [refactor this later](http://c2.com/xp/YouArentGonnaNeedIt.html) into a property if it turns out additional work needs to be done when the name value is set. If you truly *need* a property, then use a property. Otherwise, [KISS](http://en.wikipedia.org/wiki/KISS_Principle)!
Update: As many commenters have pointed out, there are valid reasons to make a trivial property, exactly as depicted above:


Reflection works differently on variables vs. properties, so if you rely on reflection, it’s easier to use all properties.
You can’t databind against a variable.
Changing a variable to a property is [a breaking change](https://web.archive.org/web/20060814171700/http://blogs.msdn.com/abhinaba/archive/2006/04/11/572694.aspx).


It’s a shame there’s so much meaningless friction between variables and properties; most of the time they do the exact same thing. [Kevin Dente](http://weblogs.asp.net/kdente/) proposed a bit of new syntax that would give us the best of both worlds:


public property int Name;


However, if the distinction between variable and property is such an ongoing problem, I wonder if a more radical solution is in order. **Couldn’t we ditch variables entirely in favor of properties?** Don’t properties do exactly the same thing as variables, but with better granular control over visibility?

**Distinguishing public and private using only case is an accident waiting to happen.**


The difference between name and Name is subtle at best. I don’t want to reopen [the whole case sensitivity debate](https://blog.codinghorror.com/the-case-for-case-insensitivity/), but using case to distinguish between variables is borderline irresponsible programming. Use a distinction that looks and reads different: m_name, _name. Or maybe eschew prefixes altogether and use fully qualified references: this.name. I don’t really care. But please, for the love of all that’s holy, don’t abuse us with even more meaningless case sensitivity.
**Is it a property or a method?**
In this case, we barely have a property. But if you are executing code in a property, make sure you’ve written a property and not a method. A property should do less work – a *lot* less work – than a method. Properties should be lightweight. If your property incurs significant effort, it should be refactored into an explicit method. Otherwise it’s going to feel like an annoying side-effect of setting a property. And if there’s any chance at all that code could spawn an hourglass, it *definitely* should be a method. Conversely, if you have a lot of simple, lightweight methods, maybe they ought to be expressed as properties. Just something to think about.

kg-card-end: html
The really important thing to take away here is to **avoid writing code that doesn’t matter**. And property wrappers around public variables are the very essence of meaningless code.As for the rest, I’ve learned to take a “live and let live” approach to code formatting, at least for cosmetic stuff like variable names. When in doubt, try to follow the Microsoft internal coding guidelines unless you have a compelling reason not to.But a few things still get under my skin. I’ve even seen .NET constants expressed in the old school all-caps way:
kg-card-begin: html

static const int TRIGGER_COUNT = 100;

kg-card-end: html
All style guidelines aside, *you know that ain’t right*.

[properties](https://blog.codinghorror.com/tag/properties/)
[variables](https://blog.codinghorror.com/tag/variables/)
[code structure](https://blog.codinghorror.com/tag/code-structure/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
