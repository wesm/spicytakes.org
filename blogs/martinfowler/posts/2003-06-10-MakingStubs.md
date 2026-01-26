---
title: "Making Stubs"
description: "A common problem with test-enhanced designs is how to create   Service Stubs in test mode while letting the real thing be there for   production (and for some tests). A couple of my colleagues have   "
date: 2003-06-10T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/MakingStubs.html
slug: MakingStubs
word_count: 494
---


A common problem with test-enhanced designs is how to create
  Service Stubs in test mode while letting the real thing be there for
  production (and for some tests). A couple of my colleagues have
  shared their ideas.


Jeremy Stell-Smith showed me an approach based on an Abstract
  Factory. All stubbable services are pulled from a single
  factory. This example shows such a Persistance class.


```

public abstract class Persistence...
  public static Persistence getInstance() {
    return (Persistence)Factories.get(Persistence.class);
  }

  public abstract void save(Object obj);
 
```


As well as the Abstract Factory capability the test factory also
  has the nice ability to have a stack of implementations - this makes
  setup of factories easier.


```

public class FooTest...
  public void setUp() {
    TestFactories.pushSingleton(Persistence.class, 
                                new MockPersistence());
  }

  public void tearDown() {
    TestFactories.pop(Persistence.class);
  }

  public void testSave() {
    Foo foo = new Foo();
    foo.save();
    ...
  }

public class Foo ...
  public void save() {
    Persistence.getInstance().save(this);
  }

```


In another project, Kraig Parkinson shows a slightly different
  take. Rather than use a single Abstract factory, those services that
  need stubbing use a prototype.


```
public class MyFacade {
  private static MyFacade prototype;

  /**
   * Sets the instance of the facade that will be returned by the getInstance method
   * used by all clients of the facade.
   */
  public static void setFacade(MyFacade newPrototype) {
    prototype = newPrototype;
  }

  /**
   * Returns an instance of the facade, using the prototype if set, 
   * otherwise an instance of the facade is used during normal operation.
   */
  public static MyFacade getInstance() {
    if (prototype != null)
      return prototype;
    else
      return new MyFacade();
  }

```


To use it in a test, you do something like this.


```

public class MyClientTest extends junit.framework.TestCase {
  private class Client {
    public String speak(String input) {
      return MyFacade.getInstance().echo(input);
    }
    public void dance() {
      return MyFacade.getInstance().move();
    } 
  }
  public void testSpeak() {
    final String expectedInput = âbarâ;
    final String expectedOutput = âfooâ;

    MyFacade.setPrototype(new MyFacade() {
      public String echo(String input) {
        assertEquals(expectedInput, input);
        return expectedOutput;
      }
    }

    //Invoke code that'd invoke the facade, but remember to remove 
    // the prototype reference once you're done with it....
    try {
      final String actualOutput = new Client.speak(expectedInput);
      assertEquals(expectedOutput, actualOutput);
    } finally {
      MyFacade.setPrototype(null);
    }
  }

  public void testDance() {
    final StringBuffer proof = new StringBuffer();

    MyFacade.setPrototype(new MyFacade() {
      public void move() {
        proof.append(âgâ);
      }
    }

    //Invoke code that'd invoke the facade, but remember to remove 
    // the prototype reference once you're done with it....
    try {
      new Client().move();
      assertTrue(âmove was not invokedâ, proof.length > 0);
    } finally {
      MyFacade.setPrototype(null);
    }
  }
```


In this case Kraig cleans up resources in a finally block as part
  of the test method. Another alternative (which I admit is how I
  would do it) is to put the clean up code in the tearDown.


The dance case is similar to what the Mock Objects folks do their
  idea of setting expectations on a mock object. You can think of this
  as a lightweight way of doing Mock Objects.
