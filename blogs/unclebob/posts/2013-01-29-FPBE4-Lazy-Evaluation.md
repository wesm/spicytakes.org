---
title: "FP Basics E4"
date: 2013-01-29
url: https://blog.cleancoder.com/uncle-bob/2013/01/29/FPBE4-Lazy-Evaluation.html
slug: FPBE4-Lazy-Evaluation
word_count: 1070
---

#### Lazy Evaluation

Remember my squares of integers program in clojure?

Remember that I showed you this program in Java too?

Well, that wasn’t a fair comparison.  Here’s a much fairer comparison program written in Java.

Notice that all I did was move the parentheses, add a comma, and use more conventional spelling.

Here’s a slighly larger context:

Can you write this Java program?  I’ll give you a hint: It uses lazy evaluation just like the Clojure program does.  That’s right.  That  `integers()`  function will return as many integers as you require.  The  `squaresOf`  function accepts an “infinite” list of integers and returns an “infinite” list of their squares.  Indeed, the  `squaresOf`  function calls a function named  `map`  which maps the values of one list into values of another by calling a specified function on each.

This squares of integers function, that I just wrote in Java, is a purely functional program.  (Well, almost.  I cheated in one place because it was convenient; but I needn’t’ve.)

So how’d I do it?   What’s the secret?  If you haven’t figured it out, you’re going to kick yourself when I tell you; because the trick is a trick that java programmers use every single day, and probably dozens of times each day.  It’s the lazy evaluator that all Java programmers know and love.  It’s the humble, lovable, iterator.

That’s right, Java programmers have been doing lazy evaluation of lists since the first days of Java.  Indeed, some of us were doing it back in the good ol’ C++ days before Java was even a gleam in Gosling’s eye.  You see, lazy evaluation is really all about the iterators.

OK, so here’s another hint about the implementation.  Here’s how you create an infinite list of integers without taking up any time or space:

Isn’t that cool?  You can loop through an infinite list of integers like this:

And the  `map`  function was even easier.  Look at this:

And that  `Func`  class is really simple.  We’ve always had a form of lambda in Java:

I’m sure you can work out the rest of the program for yourself now.  Once you know the trick, it’s really not that hard.  But if you’d like to see my version of all the code, you can check out my  [javasquint](https://github.com/unclebob/javasquint/tree/master/src/squint)  repo.

####Woah there Nellie!
From the above you might have gotten that idea that I was about to say that you can use Java as a functional language.  Uh… No.  Oh, little programs like  `squint`  are easy enough to make functional; but more interesting programs are harder.  You see the problem is that Java’s data structures are mutable, and are  *designed*  to be mutated.  So, in fact, writing functional programs in Java is quite difficult, and generally not practical.

So then why did I show you the iterator trick?  To impress upon you the fact that there’s no magic or mystery about lazily evaluated sequences in Clojure or other functional languages.  They’re just using iterators like Java would.

####Walking XML Trees
I’m sure you’ve written code that does a depth-first walk through XML documents.  Consider the following simple XML document:

```
	
<alpha>
	<beta>
		<gamma> 1 </gamma>
		<gamma> 2 </gamma>
	</beta>
	<beta2>3</beta2>
</alpha>
```

If you walked this depth-first, you’d encounter the nodes in the following order  `[alpha, beta, gamma, gamma, beta2]` .  Indeed, you could consider the XML document to be a linear list of nodes in that order.   *Indeed*  you could easily construct an iterator that walked the XML nodes in that order and gave you the illusion that you were simply walking a linear list.   *INDEED*  if you integrated that interator into the XML document class you could do a depth-first search with the following code:

Now if you walked that XML document in that fashion, and printed each node as you encountered it as shown, then the printout might look something like this:

```
	
<alpha><beta><gamma>1</gamma><gamma>2</gamma></beta><beta2>3</beta2></alpha>
<beta><gamma>1</gamma><gamma>2</gamma></beta>
<gamma>1</gamma>
<gamma>2</gamma>
<beta2>3</beta2>
```

Now stand back and look at the code and the output.  Forget that you know that the iterator of XMLNode does a depth-first traversal.  Assume that it’s like any other iterator that just does a simply sequential walk.  It looks like your  `xmlDocument`  class is a list of nodes with an awful lot of duplication in it, doesn’t it?  You wouldn’t ever create a list that looks like that just to walk an XML document would you?  I mean, that would just waste a lot of storage – especially if the xml document was really big.

So if you think about it by considering the way it  *looks* , it appears foolish.  Yet if you think about it from the point of view of using an iterator, it makes perfect sense.  It’s not wasteful at all, because that absurd list simply does not exist.

####Clojure
So now check this out.  I have a file with that XML in it.  It’s named  `doc.xml` .  I can read it into Clojure using the  `parse`  function from  `clojure.xml` , and I can pretty print it with  `pprint` :

The  `attrs`  dictionaries are for the silly attributes that you can put into XML tags (who thought  *that*  was a good idea?).  The  `parse`  function converts the XML document into a pretty simple form.  It’s a dictionary of tags that have  `content`  elements that are lists of other dictionaries that contain tags.  A nice recursive tree structure.

Doing a depth first traversal of that structure would not be too hard, but it’d be more complicated than walking a linear list.  However, take a look what happens when I put this data structure through the  `xml-seq`  function:

Look closely. See the opening parenthesis?  Aha!  This is a list!  It’s a list of all the nodes in a depth first order!  Oh, and there’s all that duplication again!  Ugh!  How wasteful.  How awful!  How foolish to create such a bloated, redundant data structure.

Oh.  But wait.  `xml-seq`  returns a  *lazy*  sequence!  The nodes aren’t evaluated  *until they are asked for* .  The list of nodes  *does not*  take up extra space!  It’s just an efficient and convenient way to walk a depth-first traversal – rather like our Java iterator.

####Conclusion
So the moral of the story is simply this:  When you have lazy sequences at your disposal, you can design your data structures for convenience, without undo concern for time and space; because lazy sequences are really just a clever use of iterators.
