---
title: "'Interface' Considered Harmful"
date: 2015-01-08
url: https://blog.cleancoder.com/uncle-bob/2015/01/08/InterfaceConsideredHarmful.html
slug: InterfaceConsideredHarmful
word_count: 1165
---

What do you think of  `interface` s?

> *You mean a `Java` or `C#` interface?*

Yes, are  `interface` s a good language feature?

> *Of course, they’re great!*

Really.  Hmmm.  What is an interface?  Is it a class?

> *No, it’s different from a class.*

In what way?

> *None of it’s methods are implemented.*

Then is this an interface?

```
public abstract class MyInterface {
  public abstract void f();
}
```

> *No, that’s an abstract class.*

What is the difference?

> *Well, an abstract class can have functions that are implemented.*

Yes, but this one doesn’t.  So why isn’t it an interface?

> *Well, an abstract class can have non-static variables, and an interface can’t.*

Yes, but this one doesn’t.  So, again, why isn’t it an interface?

> *Because it’s not.*

That’s not a very satisfying answer.  How does it differ from an interface?  What can you do with an interface that you cannot do with that class?

> *A class that `extend`s another, cannot also `implement` your class.*

Why not?

> *Because, in Java, you cannot `extend` multiple classes.*

Why not?

> *Because the compiler won’t allow you to.*

That’s odd.  Well, then, why can’t I  `implement`  that class rather than  `extend`  it?

> *Because the compiler will only allow you to `implement` an `interface`.*

My that’s a strange rule.

> *No, it’s perfectly reasonable.  The compiler will allow you to `implement` many interfaces but only allow you to `extend` one class.*

Why do you suppose the Java compiler will allow you to  `implement`  multiple interfaces, but won’t allow you to  `extend`  multiple classes?

> *Because multiple inheritance of classes is dangerous.*

Really?  How so?

> *Because of the “Deadly Diamond of Death”!*

My goodness, that sounds scary.  Just what is the Deadly Diamond of Death?

> *That’s when a class extends two other classes, both of which extend yet another class.*

You mean like this:

```
class B {}
class D1 extends B {}	
class D2 extends B {}	
class M extends D1, D2 {}
```

> *Yes!  That’s bad!*

Why is that bad?

> *Because class B might have an instance variable!*

You mean like this?

```
class B {private int i;}
```

> *Yes!  And then how many `i` variables would be in an instance of `M`?*

Ah, I see.  Since both  `D1`  and  `D2`  have an  `i`  variable, and since  `M`  derives from both  `D1`  and  `D2` , then you might expect  `M`  to have two separate  `i`  variables.

> *Yes!  But since `M` derives from `B` which has only one `i` variable, you might expect `M` to have just one `i` variable too.*

Ah, so it’s ambiguous.

> *Yes!*

So Java (and therefore C#) cannot  `extend`  multiple classes because someone  *might*  create a Deadly Diamond of Death?

> *No, because everyone _would* create a Deadly Diamond of Death since all objects implicitly derive from `Object`._

Ah!  I see.  And the compiler writers couldn’t make  `Object`  a special case?

> *Uh… Well, they didn’t.*

Hmmm.  I wonder why?  Have other compiler writers solved this problem?

> *Well, C++ allows you to create diamonds.*

Yes, and I think Eiffel does to.

> *And, gosh, I think Ruby figured out a way to do it.*

Yes, and so did CLOS and – well, let’s just say that the deadly diamond of death is a problem that was solved decades ago and it isn’t deadly, and does not lead to death.

> *Hmmm.  Yeah, I guess that’s true.*

So then back to my original question.  Why isn’t this an interface?

```
public abstract class MyInterface {
  	  public abstract void f();
}
```

> *Because it uses the keyword class; and the language won’t allow you to multiply inherit classes.*

That’s right.  And so the keyword  `interface`  was invented as a way to prevent multiple inheritance of classes.

> *Yeah, that’s probably true.*

So why didn’t the authors of Java (and by extension C#) use one of the known solutions to implement multiple inheritance?

> *I don’t know.*

I don’t know either, but I can guess.

> *What’s your guess?*

Laziness.

> *Laziness?*

Yeah, they didn’t want to deal with the issue.  So they created a new feature that allowed them to sidestep it.  That feature was the  `interface` .

> *You are suggesting that the `interface` feature of Java was a hack that the authors used in order to avoid some work?*

I can’t explain it any other way.

> *Well I think that’s kind of rude.  I’m sure their intentions were better than that.  And anyway it’s kind of nice to have `interface`s isn’t it?  I mean, what harm do they do?*

Ask yourself this question:  Why should a class have to  *know*  that it is  `implement` ing an interface?  Isn’t that precisely the kind of thing you are supposed to hide?

> *You mean a derivative has to know in order to use the right keyword, `extends` or `implements`, right?*

Right!  And if you change a class to an interface, how many derivatives have to be modified?

> *All of them.  At least in `Java`.  They solved that problem in `C#`.*

Indeed they did.  The  `implements`  and  `extends`  keywords are redundant and damaging.  Java would have been better off using the colon solution of  `C#`  and  `C++` .

> *OK, OK, but when do you really need multiple inheritance?*

So, here is what I would like to do:

```
public class Subject {
	private List<Observer> observers = new ArrayList<>();
	private void register(Observer o) {
		observers.add(o);
	}
	private void notify() {
		for (Observer o : observers)
		    o.update();
	}
}

public class MyWidget {...}

public class MyObservableWidget extends MyWidget, Subject {
	...
}
```

> *Ah, that’s the Observer pattern!*

Yes.  That’s the  *Observer*  pattern – done  *correctly* .

> *But it won’t compile because you can’t extend more than one class.*

Yes, and that’s a tragedy.

> *A tragedy?  But why?  I mean you could just derive `MyWidget` from `Subject`!*

But I don’t want  `MyWidget`  to know anything about being observed.  I want to maintain the separation of concerns.  The concern of being observed is separate from the concern of widgets.

> *Well then just implement the `register` and `notify` functions in `MyObservableWidget`*

What?  And duplicate that code for every observed class?  I don’t think so!

> *Well then have `MyObservableWidget` hold a reference to `Subject` and delegate to it?*

What?  And duplicate the delegation code in every one of my observers?  How crass.  How degenerate.  Ugh.

> *Well, you’re going to have to do one or the other of those things.*

I know.  And I hate it.

> *Yeah, it seems that there’s no escape.  Either you’ll have to violate the separation of concerns, or you’ll have to duplicate code.*

Yes.  And it’s the language forcing me into that situation.

> *Yes, that’s unfortunate.*

And what feature of the language is forcing me into this bad situation?

> *The `interface` keyword.*

And so…?

> *The `interface` keyword is harmful.*
