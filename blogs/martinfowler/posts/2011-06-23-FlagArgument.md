---
title: "Flag Argument"
description: "A flag argument is a kind of function argument that tells the   function to carry out a different operation depending on its   value. Let's imagine we want to make booking for a concert. There   are t"
date: 2011-06-23T00:00:00
tags: ["bad things", "api design"]
url: https://martinfowler.com/bliki/FlagArgument.html
slug: FlagArgument
word_count: 713
---


A flag argument is a kind of function argument that tells the
  function to carry out a different operation depending on its
  value. Let's imagine we want to make booking for a concert. There
  are two ways to do this: regular and premium . To use a flag
  argument here we'd end up with a method declaration along these
  lines:


```

    //pseudo-code
    class Concert...
      public Booking book (Customer aCustomer, boolean isPremium) {...}
  
```


My general reaction to flag arguments is to avoid them. Rather
  than use a flag argument, I prefer to define separate methods.


```

    class Concert...
      public Booking regularBook(Customer aCustomer) {...}
      public Booking premiumBook(Customer aCustomer) {...}
  
```


My reasoning here is that the separate methods communicate more
  clearly what my intention is when I make the call. Instead of having
  to remember the meaning of the flag variable when I see
  `book(martin, false)` I can easily read
  `regularBook(martin)`.


## Tangled Implementation


My general dislike of flag arguments does have some subtleties
  and consequences, the first of which is how to deal with a tangled
  implementation.


In the simplest case, the reaction to the flag is effectively to
  call different methods.


```

    public Booking book (Customer aCustomer, boolean isPremium) {
      if(isPremium) 
       // logic for premium book
      else
       // logic for regular booking
    }
  
```


but sometimes the logic is more tangled


```

    public Booking book (Customer aCustomer, boolean isPremium) {
      lorem().ipsum();
      dolor();
      if(isPremium)
        sitAmet();
      consectetur();
      if(isPremium)
        adipiscing().elit();
      else {
        aenean();
        vitaeTortor().mauris();
      }
      eu.adipiscing();
  
```


In this situation it can be messy to try to extract the regular
  and premium book methods into separate methods without significant
  duplication between the two. In this case one option is to retain
  the method with the flag argument, but keep it hidden.


```

    class Order...
      public Booking regularBook(Customer aCustomer) {
        return hiddenBookImpl(aCustomer, false);
      }
      public Booking premiumBook(Customer aCustomer) {
        return hiddenBookImpl(aCustomer, true);
      }
      private Booking hiddenBookImpl(Customer aCustomer,  boolean isPremium) {...}
  
```


The point here is that only the regular and premium book methods
  should call `hiddenBookImpl`. I like to telegraph this
  by using an ugly name - which also has the bonus that, if you have to,
  you can easily add a regex probe to ensure nobody else is calling
  it.


## Deriving the flag


How about if the decision on whether to use a premium booking
    process depends upon the status of the customer. Let's assume an
    elite customer gets premium booking while a regular customer gets
    the regular treatment. In this case, of
    course, we shouldn't have a boolean flag - but is the customer
    object itself acting as a flag?


I would look at this as about capturing the intention of the
    caller. If how to book depends only on the status of the customer,
    then the caller has no business caring about the difference
    between premium and regular booking - and thus it's perfectly
    reasonable for the booking routine to derive it's true method
    based on the customer status. You only want different methods when
    the caller needs to specify which one she wants.


## Boolean Setting Method


Connected to this is the issue of how to name boolean setting
  methods. Here I agree with [Kent's
  advice](https://www.amazon.com/gp/product/0321413091/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321413091&linkCode=as2&tag=martinfowlerc-20) - I would rather see


```

    void setOn();
    void setOff();
  
```


than see


```

    void setSwitch(boolean on);
  
```


But again to agree with Kent, this does depend on how the method
  is used. If you pulling data from a boolean source, such as a UI
  control or data source, I'd rather have
  `setSwitch(aValue)` than


```

    if (aValue)
      setOn();
    else
      setOff();
  
```


This is an example that an API should be written to make it
  easier for the caller, so if we know where the caller is coming from
  we should design the API with that information in mind. This also
  argues that we may sometimes provide both styles if we get callers
  in both ways.


That same logic applies to `book`. If there is a
  check-box on the screen and we are just passing its value to
  `book` then a flag argument has some justification. In
  this example I wouldn't say it's a simple choice - most of the time
  I'd argue that the flag argument for `book` is much
  harder to understand than a simple boolean setter, and is thus worth
  the explicit methods.
