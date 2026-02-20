---
title: "Practical Metaprogramming with Ruby: Storing Preferences"
date: 2009-11-17
url: https://www.kalzumeus.com/2009/11/17/practical-metaprogramming-with-ruby-storing-preferences/
slug: practical-metaprogramming-with-ruby-storing-preferences
word_count: 1578
---


All code in this article is copyright Patrick McKenzie 2009 and released under the MIT license. Basically, you can feel free to use it for whatever, but don’t sue me.


The other day on [Hacker News](http://news.ycombinator.com/item?id=943597), commenting on a recent [Yehuda Katz explanation of the nuts and bolts of metaprogramming](http://yehudakatz.com/2009/11/15/metaprogramming-in-ruby-its-all-about-the-self/), I mentioned that I though discussions of programming theory are improved by practical examples of how the techniques solve problems for customers.  After all, toy problems are great, but foos and bars don’t get me home from the day job quicker or convince my customers to pay me money.


My claim: **Metaprogramming allows you to cut down on boilerplate code, making your programs shorter, easier to write, easier to read, and easier to test. Also, it reduces the impact of changes.**


I’m going to demonstrate this using actual code from my PrintJob class, which encapsulates a single request to print out a set of bingo cards in [Bingo Card Creator](http://www.bingocardcreator.com).  PrintJobs can have any number of properties associated with them, and every time I implement a new feature the list tends to grow.  For example, when I added in the ability to print in color, that required adding five properties. **This pattern is widely applicable** among many times of one-to-many relationships where you never really look at the many outside of the context of their relationship to the one — user preferences would be an obvious example.


There are a few ways you can do this in Rails. The most obvious is **put each property as a separate column in your table**. This means that

1. you’d do a database migration (**downtime!** *breakage!* ***unnecessary work!***) every week you add a new property.


If you’re getting into the associations swing of thing, you might consider creating a has_many relationship between PrintJob and PrintJobProperties, with each PrintJobProperty having a property_name and a property_value.  Swell.  Now you need to:

1. Do twenty joins every time you inspect a single PrintJob.
2. Add a bunch of unique constraints (in your DB or via Rails validations — I hope you have earned the favor of the concurrent modification gods) to prevent someone from assigning two properties of the same name to the same print job.
3. Have very intensely ugly syntax for accessing the actual properties.  (Lets see, *print_job.options.find_or_create_by_name(“foo”).value = “bar”* ought to do it.)


**Instead of either of these methods**, I save the properties to an options hash, and then serialize that to JSON to save to and load from the database column.  Rails takes care of most of the details for me.


## Enter The Metaprogramming Magic


However, this means I would have to write code like print_job[:options][:background_color], which is excessively verbose, and every time I referred to it I would need to possibly provide a default value in the event it was nil.  **Too much work!**


Instead, we’ll use this Ruby code:


## What This Code Does


OK, what does this do? Well, first I define a bunch of default options, which are later used (code not shown) to initialize PrintJobs right before they’re fed into the actual printing code. Each default option is used to create a getter/setter pair for PrintJob, so that instead of typing print_job[:options][:background_color] I can just type print_job.background_color. You’ll notice that it also note that both setters and getters pre-initialize the options array if I haven’t done it already. This saves me from accidentally forgetting to initialize it and then winding up calling nil[:some_option].


## Why This Code Is Useful


Clearly this saves keystrokes for using getters/setters, but how does it actually save *work*? Well, because each of the properties are now methods on the ActiveRecord object (the PrintJob), all of the Rails magic which you think works on columns actually works on these options, too. This includes:

- validations
- form helpers
- various pretty printing things


Since card_count is just another property on the PrintJob ActiveRecord object, Rails can validate it trivially. Try doing that within a hash — it isn’t fun. I sanity check that card_count (the number of cards printed for this print job) is an integer between 1 and 1,000, and additionally check that, for users who aren’t registered, it is between 1 and 15. (I’ve omitted the message which tells folks trying to print more to upgrade.)


Here’s an example of a portion of the form helper from the screen where most of these options are set:


Ordinarily in the above code you’d expect card_count to correspond to a column in the database, and then the column would cause there to be card_count and card_count= methods on PrintJob, and this would be used to initialize the above text field. Well, Rails doesn’t really care how those methods came to be — they could be placed there by ActiveRecord magic, or attr_accessor, or defining by hand, or creative use of metaprogramming, as above. It takes about 7 lines to define a getter/setter pair in most languages. I have twenty properties listed up there. Instant savings: 140 lines of code.


Similarly, I’m saved from having to write a bunch of repetitive non-sense in the controller, too.


This walks over the param map for things being set to the PrintJob and, if they’re an option, sets them automatically. This saves about twenty lines of manual assignment. (Nota bene: PrintJob.new(param) will not work because the virtual columns are not real columns. In general, I hate mass assignment in Rails anyhow — sooner or later it will bite my hindquarters for security if I use it, so I assign only those columns which I know to be safe. Note that nothing in the options hash is sensitive — after all, they’re just user options.)


This controller is **extraordinarily robust against change**. When I added five extra options to the print jobs to accommodate my new features (font, color, and pattern selection), I didn’t change *one single line* of the associated controllers.


But wait, there’s more! You see, 200 lines of negacode (code that you don’t have to write) means 200 lines of code that you don’t have to read, test, maintain, or debug. I didn’t have to change the controller at all. I didn’t have to check to see if the new properties were automatically initialized to their starting values, since the code which performed the initialization was already known to work. I didn’t have to debug typos made in the accessors. It all *just worked*.


**This is the power of metaprogramming.** The less boilerplate code you have to write, understand, read, test, debug, and maintain, the more time you can spend creating new features for your customers, doing marketing, or doing other things of value for your business. The last three features I added caused five new properties to be added to my PrintJob model. I just diffed the pre- and post-commit code in SVN. Three features required required:

- *No change* to the schema.
- *No change* to the controller.
- 35 lines to implement three features in the model. (*Counting the white space.*)


(The view required about 25 lines of new code, mostly inline Javascript, because a good UI for picking colors is tricky. I ended up liberally borrowing from [this chap](http://myles.eftos.id.au/blog/2006/04/13/javascript-colour-picker-based-on-prototype/), who has an awesome color picker in Prototype that was amenable to quick adaptation to the needs of technically unsophisticated users to who wouldn’t think #F00F00 is a color.)


This is a much, much more effective use of my time than writing several hundred lines worth of boilerplate model code, then repeating much of it in XML configurations, just so that I can actually have access to the data needed to *begin* implementing the features. (*How did you guess I program in Java?*)


## A Note To DBAs In The Audience


Yeah, I hear you — stuffing preferences in JSON is all well and good, but doesn’t this ruin many of the benefits of using SQL? For instance, isn’t it true that I can no longer query for PrintJobs which are colored red in any convenient manner? That is absolutely true. However, it isn’t required by my use cases, at all.


PrintJobs are only ever accessed per user and per id, and since both of those have their own columns, having all the various options be stored in an opaque blob doesn’t really hurt me. I regret not being able to do “select sum(card_count) from print_jobs;” some times, but since I don’t have to calculate “total number of cards printed since I opened” all that frequently, it is perfectly adequate to just load the entire freaking table into memory and then calculate it in Ruby. (It takes about 5 seconds to count: 217,264 cards printed to date. Thanks users!)


## Note Regarding Security


**Programmatically instantiating methods is extraordinarily dangerous if you don’t know what you’re doing.** Note that I create the methods based on keys used in a constant hash specified in my code. You could theoretically do this from a hash created anywhere — for example, Ruby will happily let you create methods at runtime so you might decide, eh, PrintJob needs a method for everything in the params hash. **DO NOT DO THIS.** That would let anyone with access to your params (which is, well, anyone — just append ?foo=bar to the end of a URL and see what happens) create *arbitrarily named methods* on your model objects. That is just asking to be abused — setting is_admin? to 1 or adding can_launch_nuclear_weapons to role, for example.
