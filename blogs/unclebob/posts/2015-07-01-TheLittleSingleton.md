---
title: "The Little Singleton"
date: 2015-07-01
url: https://blog.cleancoder.com/uncle-bob/2015/07/01/TheLittleSingleton.html
slug: TheLittleSingleton
word_count: 540
---

Do you recognize this:

```
public class X {
  private static X instance = null;

  private X() {}

  public static X instance() {
    if (instance == null)
      instance = new X();
    return instance;
  }

  // more methods...
}
```

> *Of course.  That’s the Singleton pattern from the GOF book.  I’ve always heard we shouldn’t use it.*

Why shouldn’t we use it?

> *Because it makes our systems hard to test.*

It does?  Why is that?

> *Because you can’t mock out a Singleton.*

You can’t?  Why not?

> *Well, because, the only class that can touch that private variable is the Singleton itself.*

Do you know the rule about encapsulation and tests?

> *Uh, no.  What rule is that?*

Tests trump Encapsulation.

> *What does that mean?*

That means that tests win.  No test can be denied access to a variable simply to maintain encapsulation.

> *You mean that if a test needs access to a private variable…*

…the variable shouldn’t be private.  Yes.

> *That just doesn’t sound right.  I mean, encapsulation is, er, important!*

Tests are more important.

> *Wait.  What?*

What good is encapsulated code if you can’t test it?

> *OK, OK, but what does this have to do with testing singletons.*

Look at this code.

```
public class X {
  static X instance = null;

  private X() {}

  public static X instance() {
    if (instance == null)
      instance = new X();
    return instance;
  }

  // methods.
}

class TestX {
  @Before
  public setup() {
    X.instance = new XMock();	
  }
}

class XMock extends X {
    // overide methods
}
```

> *Oh, you made the instance variable “package” scope.*

Right.

> *And that allows you to mock the singleton.*

Right.

> *And that means that singletons are easy to mock.*

Right.  Now consider this:

```
public class X {
  public static X instance = new X();

  private X() {}

  // methods.
}
```

> *Wait!  Where did the instance method go?*

I don’t need it.

> *Ah, the instance variable is public.  You can just use it directly.*

Right.

> *But… But…  Someone might over-write it?*

Who would do that?

> *I dunno.  Uh.  Someone bad.*

Do you have bad people on your team?

> *No.   But.   This just doesn’t feel safe.*

Well, if this were part of a public API, I’d agree with you.  But if this is just code that’s used by our team then…

> *We trust our team?*

Of course.

> *And this is pretty easy to mock, isn’t it?*

Of course.

> *So then I guess we could use Singleton if we wanted to.*

Sure.  Although most of the time I don’t want to.

> *After all this, and now you’re telling you you don’t want to use Singleton anyway?*

Well, I think it’s important to understand why.

> *OK, so why don’t you use Singleton?*

I do sometimes.  Especially in public APIs.

> *You mean it’s a trust issue again?*

Right.  In a public API if I want to ensure that only one instance is being created, then I’ll use a Singleton.

> *OK, but then what if it’s not in a public API, but you still just want one instance created?*

Well, then, I simply create one.
