---
title: "New software for discussion groups"
date: 2007-05-03
url: https://www.joelonsoftware.com/2007/05/03/new-software-for-discussion-groups/
word_count: 242
---


As you may know already, the four main discussion groups on this site ([Joel on Software](http://discuss.joelonsoftware.com/?joel), [Business of Software](http://discuss.joelonsoftware.com/?biz), [Design of Software](http://discuss.joelonsoftware.com/?design), and [.NET Questions](http://discuss.joelonsoftware.com/?dotnet)) are implemented with [FogBugz](http://www.fogcreek.com/fogbugz), my company’s flagship project management system. The current shipping version of FogBugz is 5.0, but we’ve been developing 6.0 for a while now and want to do some testing of it under heavy load.


So, if you head on over to the discussion groups, what you’ll see is actually running an early, unreleased pre-alpha version of FogBugz 6.0. For now, you won’t notice any significant changes except for a slightly different font that matches the rest of FogBugz 6.0. Next week, if all goes well, we’ll turn on a new feature which lets you register for an account so you can get one of those green checkboxes that appears in the discussion group next to the names of people who are logged on to FogBugz. At some point, if all goes really well, we’ll try to turn on another new feature that makes FogBugz keep track of which posts you’ve already seen (as long as you’re logged on) and show them in a different color… this is a feature we used to rely on the browser to do. This is one of the scarier features since it’s kind of data-intensive for very large numbers of users. Which is why we’re using you as guinea pigs before we inflict it on our beta testers.
