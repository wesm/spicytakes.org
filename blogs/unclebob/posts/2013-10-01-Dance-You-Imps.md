---
title: "Dance you Imps!"
date: 2013-10-01
url: https://blog.cleancoder.com/uncle-bob/2013/10/01/Dance-You-Imps.html
slug: Dance-You-Imps
word_count: 1559
---

There are several tools out there that promise to bridge the divide between objects and relational tables.  Many of these tools are of high quality, and are very useful.  They are collectively known as ORMs, which stands for  *Object Relational Mappers* .  There’s just one problem.  There ain’t no such beast!

### The Impedance Mismatch

It all started long ago, in the hinter-times of the 1980s.  Relational databases were the big kids on the block.  They had grown from their humble beginnings, into adventurers and conquerors.  They had not yet learned to be:  *THE POWER THAT DRIVES THE INTERNET (TM)* ; but they were well on their way.  All new applications, no matter how humble,  *had to have*  a relational database inside them.  The marketing people didn’t know  *why*  this was true; but that knew that is  *was*  true.

And then OO burst forth upon the land.  It came as Smalltalk.  It came as Objective-C, and it came, most importantly, as C++, and then Java and C#.  OO was new.  OO was shiny.  OO was a mystery.

Most creatures at the time feared new things.  So they hid in caves and chanted spells of protection and exorcism.  But there were imps in the land, who thrived by embracing change.  The imps grabbed for the shiny new OO bauble and made it their own.  They could  *feel*  its power.  They could  *sense*  that it was good – very, very good; but they couldn’t explain  *why* .  So they invented reasons.  Reasons like:  *It’s a closer way to model the real world!*  (What manager could say no to  *that* ?)

Then one day, when the OO imps were just minding their own business, doing their little dance of passing messages back and forth to each other, the RDBMS gang (pronounced  *Rude Bums* ) walked up to them and said: “If you imps want to do your impy little dance of passing your stupid messages back and forth in  *our*  neighborhood, then your bits are ours.  You’re going to store them with us.  Capisce?”

What could the OO imps say?  The  *Rude Bums*  ruled the roost; so, of course, they agreed.  But that left them with a problem.  The  *Rude Bums*  had some very strict,  *and very weird* , rules about how bits were supposed to be stored.

These rules didn’t sit well with the imps.  When the imps did their impy message passing dance, they just sort of threw the bits back and forth to each other.  Sometimes they’d hold the bits in their pockets for awhile, and sometimes they’d just toss them over to another impy dancer. In a full fledged impy dance, the bits just zoomed around from dancer to dancer in a frenzy of messages.

But the  *Rude Bums*  demanded that the bits be stacked up on strictly controlled tables, all kept in one big room.  They imposed very strict rules about how those bits could be arranged, and where they had to be placed.  In fact, there were forms to fill out, and statements to make, and transactions to execute.  And it all had to be done using this new street banter named SQL (pronounced  *squeal* ).

So all the OO imps had to learn  *squeal* , and had to stack their bits on the  *Rude Bums*  tables, and had to fill out the forms and do the transactions, and that just didn’t match their dancing style.  It’s  *hard*  to throw your bits around in the impy dance when you’ve got to stack your bits on tables while speaking  *squeal* !

This was the beginning of the Impy Dance Mismatch between OO and the  *Rude Bums* .

### ORMs to the rescue,  *Not!*

The next decade saw a huge increase in the political power of the  *Rude Bums* .  They grabbed more and more territory, and ruled it with an iron fist.  The imps also gained territory; possibly more than the  *Rude Bums* ; but they never managed to break free of the  *Rude Bums’*  rules.  And so they forgot how to dance.  The free and lively OO dance they had done at the very beginning faded from their memory.  It was replaced by a lock-step march around the  *Rude Bum’s*  tables.

Then, one day, some strangers appeared.  They called themselves ORM (the  *OutRaged Mongrels* ).  The  *Mongrels*  had seen the free OO dancing of the imps before the  *Rude Bums’*  took control of them; and the  *Mongrels*  longed to see the imps dance free again.

So they came up with a plan.   *They*  would do the  *squealing* !   *They*  would arrange the bits on the tables.   *They*  would fill out the forms and execute the transactions.   *They* , the  *Mongrels* , would stand between the imps and the  *Rude Bums*  and free the imps to dance once again.

“Oh  *dance free*  you imps,  *dance free!* ”

But the imps  *didn’t*  dance free. They kept right on doing their lock-step march.  Oh they were happy to have someone else take care of the nasty job of speaking  *squeal*  and arranging bits on the tables.  They were happy that they didn’t have to deal directly with the  *Rude Bums* .  But now, instead of marching around the  *Rude Bum’s*  tables, they marched around the “Mongrels’” cabinets (which looked an awful lot like the  *Rude Bums’*  tables).

The Impy Dance Mismatch between OO and the  *Rude Bums*  had simply changed to the Impy Dance Mismatch between OO and ORMs.

### Their ain’t no such mapping.

An object is not a data structure.  Repeat after me:  *An Object Is Not A Data Structure.*   OK, you keep repeating that while I keep talking.

An object is not a data structure.  In fact, if you are the consumer of an object, you aren’t allowed to see any data that might be inside it.  And, in fact, the object might have no data inside it at all.

What do you see when you look at an object from the outside?  You see  *methods!*   You don’t see any data; because the data (if any) is kept private.  All you are allowed to see, from the outside looking in, are methods.  So, from the outside looking in, an object is an abstraction of behavior, not an abstraction of data.

How do you store an abstraction of behavior in a database?  Answer:  *You don’t!*   You can’t store behavior in a database.  And that means  *you can’t store objects in a database.*   And that means there’s no Object to Relational mapping!

### OK, now wait!

Yeah?  Wait for what?  You want to argue that point?  Really?  You say you’ve got an  *account*  object stored in the database, and you use hibernate to bring it into memory and turn it into an object with methods?

*Balderdash!*   Hibernate doesn’t turn  *anything*  into an object.  All Hibernate does is to migrate data structures that are stored on a disk (a what?  You still using disks?  No wonder you’re confused.) to data structures stored in RAM.  That’s all.  Hibernate changes the form and location of data structures.  Data structures, not objects!

What is a data structure?  It’s a bunch of public data with no methods.  Compare that to an object which is a bunch of public methods with no visible data.  These two things are the exact opposites of each other!

I could get into a whole theoretical lecture on the nature of data structures and objects, and polymorphism, and switch statements, and…   But I won’t.  Because the point of this article is simply to demonstrate that ORMs aren’t ORMs.

###What are ORMs?

ORMs are data structure migrators.  That’s all.  They move data from one place to another while making non-semantic changes to the form of that data.  They do  *NOT*  create objects out of relational tables.

### Why is this important?

It’s important because the imps aren’t dancing free!  Too many applications are designed such that the relational schema is bound, in lock-step, to the business objects.  The methods on the business objects are partitioned according to the relational schema.

Think about that for a minute.  Think about that, and then weep.  Why should the message pathways of an application be bound to the lines on a E-R diagram?  What does the behavior of the application have to do with the structure of the data?

Try this thought experiment.  Assume that there is no database.  None at all.  There are no tables.  No schema.  No rows.  No SQL.  Nothing.

Now think about your application.  Think about the way it behaves.  Group similar behaviors together by responsibility.  Draw lines between behaviors that depend on each other.  Do you know what you’ll wind up with?  You’ll wind up with an object model.  And do you know what else?  It won’t look much like a relational schema.

*Tables are not business objects!*   Tables aren’t objects at all.  Tables are just data structures that the true business objects use as a resource.

###Moral

So, designers, feel free to use ORMs to bring data structures from the disk (the disk?  You still using one?) into memory.  But please don’t think of those data structures as your business objects.  What’s more, please design your business objects without consideration for the relational schema.  Design your applications to  *behave*  first.   *Then*  figure out a way to bind those behaviors to the data brought into memory by your ORM.
