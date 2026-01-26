---
title: "Refactoring a JavaScript video store"
description: "The simple example of calculating and formatting a bill for a video store opened my     refactoring book in 1999. If done in modern     JavaScript, there are several directions you could take the refa"
date: 2016-05-18T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/articles/refactoring-video-store-js/
slug: refactoring-video-store-js
word_count: 7668
---


Many years ago, when I was writing [the refactoring
    book](https://martinfowler.com/books/refactoring.html), I opened the book with a (very) simple example of refactoring some code
    that calculated a customer's bill for renting some videos (in those days we had to go to a
    store to do that). I was contemplating this
    refactoring example recently, in particular how it would look if it were written in
    modern JavaScript.


Any refactoring is about improving the code in a particular direction, one that
    suits a development team's coding style. In the book the example was in Java, and Java
    (particularly then) suggests a certain style of coding, an object-oriented style. With
    JavaScript, however, there is a lot more options about what kind of style to go for.
    While you can do a Java-like OO style, particularly with ES6 (Ecmascript 2015), not
    all JavaScript pundits favor that style, many indeed consider using classes to be a
    Bad Thing.


## This initial video store code


To explore further, I need to introduce some code. In this case a JavaScript
      version of the original example I wrote back at the turn of the century.


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      let movie = movies[r.movieID];
      let thisAmount = 0;
  
      // determine amount for each movie
      switch (movie.code) {
        case "regular":
          thisAmount = 2;
          if (r.days > 2) {
            thisAmount += (r.days - 2) * 1.5;
          }
          break;
        case "new":
          thisAmount = r.days * 3;
          break;
        case "childrens":
          thisAmount = 1.5;
          if (r.days > 3) {
            thisAmount += (r.days - 3) * 1.5;
          }
          break;
      }
  
      //add frequent renter points
      frequentRenterPoints++;
      // add bonus for a two day new release rental
      if(movie.code === "new" && r.days > 2) frequentRenterPoints++;
  
      //print figures for this rental
      result += `\t${movie.title}\t${thisAmount}\n` ;
      totalAmount += thisAmount;
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
  }
```


I'm using ES6 here. The code operates on two data structures, both of which are
      just lists of json records. A customer record looks like this


```
{
  "name": "martin",
  "rentals": [
    {"movieID": "F001", "days": 3},
    {"movieID": "F002", "days": 1},
  ]
}
```


The movies structure looks like this


```
{
  "F001": {"title": "Ran",                     "code": "regular"},
  "F002": {"title": "Trois Couleurs: Bleu",     "code": "regular"},
  // etc
}
```


In the original book, movies were just present as objects in the java object
      structure. For this essay I prefer passing in the json structure as a parameter. I
      will assume using some kind of global lookup, such as a [Repository](https://martinfowler.com/eaaCatalog/repository.html), is not appropriate for this application.


The statement method prints out a simple text output of a rental statement


```
Rental Record for martin
  Ran 3.5
  Trois Couleurs: Bleu 2
Amount owed is 5.5
You earned 2 frequent renter points
```


This output is crude, even by the standards of example code. Could I
      not even be bothered to format the numbers decently? Remember, however, that the book
      was written with Java 1.1, before String.format was added to the language. That may
      partially forgive my laziness.


The statement function is an example of the smell [Long
      Method](http://my.safaribooksonline.com/0-201-485672/ch03lev1sec2). Just its size is enough to make me suspicious. But just because code
      smells bad isn't enough of a reason on its own to refactor it. Poorly factored code is a problem because
      it's hard to understand. Code that's hard to understand is hard to modify, whether
      to add new features or to debug. So if you don't need to to read and understand some
      code, then its poor structure won't harm you and you can happily leave it alone for
      a while. So to trigger our interest in this code fragment, we need a reason for it
      to change. Our reason, as I used in the book, is to write an HTML version of the
      statement method, something that prints out something like this.


```
<h1>Rental Record for <em>martin</em></h1>
<table>
  <tr><td>Ran</td><td>3.5</td></tr>
  <tr><td>Trois Couleurs: Bleu</td><td>2</td></tr>
</table>
<p>Amount owed is <em>5.5</em></p>
<p>You earned <em>2</em> frequent renter points</p>
```


As I indicated earlier, in this essay I'm exploring a number of ways in which I
      can refactor this code to make it easier to add additional output renderings. All of
      these have the same start: breaking down the single method into a set of functions
      to capture different parts of the logic. Once I've done this break down, I'll
      explore four different ways these functions can be arranged to support alternative
      renderings.


![](video-js_main.png)


## Decomposing into several functions


Whenever I work with a overly long function like this, my first thought is to use
      to look for logical chunks of code and turn them into their own functions using 
      [Extract Method](http://refactoring.com/catalog/extractMethod.html). 1 The first such chunk
      that catches my eye is the switch statement.


1: 
     The refactoring catalog was written when object-oriented vocabulary was popular, so
     I used âmethodâ to refer to a function/sub-routine/procedure or similar. In
     JavaScript it would be sensible to use âfunctionâ instead, but I'm using the names of
     the refactorings from the book.


![](video-js_nest.png)


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      let movie = movies[r.movieID];
      let thisAmount = 0;
  
      // determine amount for each movie
      switch (movie.code) {
        case "regular":
          thisAmount = 2;
          if (r.days > 2) {
            thisAmount += (r.days - 2) * 1.5;
          }
          break;
        case "new":
          thisAmount = r.days * 3;
          break;
        case "childrens":
          thisAmount = 1.5;
          if (r.days > 3) {
            thisAmount += (r.days - 3) * 1.5;
          }
          break;
      }
  
      //add frequent renter points
      frequentRenterPoints++;
      // add bonus for a two day new release rental
      if(movie.code === "new" && r.days > 2) frequentRenterPoints++;
  
      //print figures for this rental
      result += `\t${movie.title}\t${thisAmount}\n` ;
      totalAmount += thisAmount;
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
  }
```


My IDE (IntelliJ) offers to do this refactoring automatically for me, but it
      doesn't do it correctly - its JavaScript abilities aren't as solid or as mature as its
      Java refactoring. So I do this the manual way, which involves looking at the data used
      by the candidate extraction. There are three bits of data there:

- `thisAmount` is the value being calculated by the extracted code. I can initialize
        it within the function and return it at the end
- `r` is the rental being examined in the loop, I can pass that in as a parameter.
- `movie` is the movie for the rental, which is a temp made earlier on.
        Temporary variables like this usually get in the way when refactoring procedural
        code, so I prefer to first use [Replace Temp with Query](http://refactoring.com/catalog/replaceTempWithQuery.html) to turn them into
        a function that I can call within any extracted code.


Once I've done the [Replace Temp with Query](http://refactoring.com/catalog/replaceTempWithQuery.html) the code looks like this.


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      let thisAmount = 0;
  
      // determine amount for each movie
      switch (movieFor(r).code) {
        case "regular":
          thisAmount = 2;
          if (r.days > 2) {
            thisAmount += (r.days - 2) * 1.5;
          }
          break;
        case "new":
          thisAmount = r.days * 3;
          break;
        case "childrens":
          thisAmount = 1.5;
          if (r.days > 3) {
            thisAmount += (r.days - 3) * 1.5;
          }
          break;
      }
  
      //add frequent renter points
      frequentRenterPoints++;
      // add bonus for a two day new release rental
      if(movieFor(r).code === "new" && r.days > 2) frequentRenterPoints++;
  
      //print figures for this rental
      result += `\t${movieFor(r).title}\t${thisAmount}\n` ;
      totalAmount += thisAmount;
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
  
    function movieFor(rental) {return movies[rental.movieID];}
  }
```


Now I extract the switch statement.


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
  
    for (let r of customer.rentals) {
      const thisAmount = amountFor(r);
  
      //add frequent renter points
      frequentRenterPoints++;
      // add bonus for a two day new release rental
      if(movieFor(r).code === "new" && r.days > 2) frequentRenterPoints++;
  
      //print figures for this rental
      result += `\t${movieFor(r).title}\t${thisAmount}\n` ;
      totalAmount += thisAmount;
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
  
    function movieFor(rental) {return movies[rental.movieID];}
  
    function amountFor(r) {
      let thisAmount = 0;
  
      // determine amount for each movie
      switch (movieFor(r).code) {
        case "regular":
          thisAmount = 2;
          if (r.days > 2) {
            thisAmount += (r.days - 2) * 1.5;
          }
          break;
        case "new":
          thisAmount = r.days * 3;
          break;
        case "childrens":
          thisAmount = 1.5;
          if (r.days > 3) {
            thisAmount += (r.days - 3) * 1.5;
          }
          break;
      }
      return thisAmount;
    }
  }
```


I now turn my attention to calculating
      the frequent renter points. I can do a similar extraction of its code


```
function statement(customer, movies) {
  let totalAmount = 0;
  let frequentRenterPoints = 0;
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    const thisAmount = amountFor(r);
    frequentRenterPointsFor(r);

    //print figures for this rental
    result += `\t${movieFor(r).title}\t${thisAmount}\n` ;
    totalAmount += thisAmount;
  }
  // add footer lines
  result += `Amount owed is ${totalAmount}\n`;
  result += `You earned ${frequentRenterPoints} frequent renter points\n`;

  return result;
```


â¦


```
  function frequentRenterPointsFor(r) {
   //add frequent renter points
    frequentRenterPoints++;
    // add bonus for a two day new release rental
    if (movieFor(r).code === "new" && r.days > 2) frequentRenterPoints++;
  }
```


Although I've extracted the function, I don't like the way it works by updating the
      parent-scoped variable. Such side-effects make code hard to reason about, so I
      alter it so that it has no side-effects in its body.


```
function statement(customer, movies) {
  let totalAmount = 0;
  let frequentRenterPoints = 0;
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    const thisAmount = amountFor(r);
    frequentRenterPoints += frequentRenterPointsFor(r);

    //print figures for this rental
    result += `\t${movieFor(r).title}\t${thisAmount}\n` ;
    totalAmount += thisAmount;
  }
  // add footer lines
  result += `Amount owed is ${totalAmount}\n`;
  result += `You earned ${frequentRenterPoints} frequent renter points\n`;

  return result;
```


â¦


```
  function frequentRenterPointsFor(r) {
    let result = 1;
    if (movieFor(r).code === "new" && r.days > 2) result++;
    return result;
  }
```


I take the chance to clean up the two extracted functions a bit, while I understand
      them.


```
  function amountFor(rental) {
    let result = 0;
    switch (movieFor(rental).code) {
      case "regular":
        result = 2;
        if (rental.days > 2) {
          result += (rental.days - 2) * 1.5;
        }
        return result;
      case "new":
        result = rental.days * 3;
        return result;
      case "childrens":
        result = 1.5;
        if (rental.days > 3) {
          result += (rental.days - 3) * 1.5;
        }
        return result;
    }
    return result;
  }
```


```
  function frequentRenterPointsFor(rental) {
    return (movieFor(rental).code === "new" && rental.days > 2) ? 2 : 1;
   }
```


There is more I could do with these functions, especially
        `amountFor`, and that was something I did do in the book. But for this
        essay I won't examine the body of these functions any further.


That done, I go back to the body of the function.


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      const thisAmount = amountFor(r);
      frequentRenterPoints += frequentRenterPointsFor(r);
  
      //print figures for this rental
      result += `\t${movieFor(r).title}\t${thisAmount}\n` ;
      totalAmount += thisAmount;
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
```


A general tactic I like to use is getting rid of mutable variables. There are three
      here, one is collecting up the final string, the other two calculate values that are
      being used in that string. I'm ok with the first, but would like to eradicate the
      other two. To start doing that I need to split the loop. First I simplify the loop and
      inline the const.


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      frequentRenterPoints += frequentRenterPointsFor(r);
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n` ;
      totalAmount += amountFor(r);
    }
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
```


I then split the loop into three parts.


```
  function statement(customer, movies) {
    let totalAmount = 0;
    let frequentRenterPoints = 0;
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      frequentRenterPoints += frequentRenterPointsFor(r);
    }
    for (let r of customer.rentals) {
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
    }
    for (let r of customer.rentals) {
      totalAmount += amountFor(r);
    }
  
    // add footer lines
    result += `Amount owed is ${totalAmount}\n`;
    result += `You earned ${frequentRenterPoints} frequent renter points\n`;
  
    return result;
```


Some programmers worry about the performance implications of refactorings
        like this, in which case take a look of an [old but pertinent article](https://martinfowler.com/ieeeSoftware/yetOptimization.pdf) on
        software performance


That split allows me to then extract functions for the calculations.


```
  function statement(customer, movies) {
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
    }
    result += `Amount owed is ${totalAmount()}\n`;
    result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
    return result;
  
    function totalAmount() {
      let result = 0;
      for (let r of customer.rentals) {
        result += amountFor(r);
      }
      return result;
    }
    function totalFrequentRenterPoints() {
      let result = 0;
      for (let r of customer.rentals) {
        result += frequentRenterPointsFor(r);
      }
      return result;
    }
```


Being a fan of [collection pipelines](https://martinfowler.com/articles/collection-pipeline/), I'll also adjust the loops to use them.


```
  function totalFrequentRenterPoints() {
    return customer.rentals
      .map((r) => frequentRenterPointsFor(r))
      .reduce((a, b) => a + b, 0)
      ;
  }
  function totalAmount() {
    return customer.rentals
      .reduce((total, r) => total + amountFor(r), 0);
  }
```


I'm not sure which of those two pipeline styles I prefer most.


## Examining the composed function


So now lets look at where we are. Here is all the code.


```
function statement(customer, movies) {
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
  }
  result += `Amount owed is ${totalAmount()}\n`;
  result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
  return result;

  function totalFrequentRenterPoints() {
    return customer.rentals
      .map((r) => frequentRenterPointsFor(r))
      .reduce((a, b) => a + b, 0)
      ;
  }
  function totalAmount() {
    return customer.rentals
      .reduce((total, r) => total + amountFor(r), 0);
  }
  function movieFor(rental) {
    return movies[rental.movieID];
  }
  function amountFor(rental) {
    let result = 0;
    switch (movieFor(rental).code) {
      case "regular":
        result = 2;
        if (rental.days > 2) {
          result += (rental.days - 2) * 1.5;
        }
        return result;
      case "new":
        result = rental.days * 3;
        return result;
      case "childrens":
        result = 1.5;
        if (rental.days > 3) {
          result += (rental.days - 3) * 1.5;
        }
        return result;
    }
    return result;
  }
  function frequentRenterPointsFor(rental) {
    return (movieFor(rental).code === "new" && rental.days > 2) ? 2 : 1;
  }
}
```


I now have a nicely composed function. The core code of the function is 7 lines,
      and is all concerned with formatting the output string. All the calculation code is
      moved to its own set of nested functions, each of which is small and clearly named to show
      its purpose.


But I'm still not quite in a position to write the html emitting function. The
      decomposed functions are all nested inside the overall statement function, this
      makes it easier to extract the functions as they can refer to names inside the
      function scope, which includes each other (such as `amountFor` calling
      `movieFor`) and the supplied parameters `customer` and
      `movie`. But I can't write a simple `htmlStatement` function
      that references those functions. To be
      able to support some different outputs using the same calculations, I need to do
      some further refactorings. Now I reach a point where I have several options of which
      refactorings to do depending on how I like to factor my code. I'll run through each
      of these approaches next, explaining how each one works, and then compare them once
      I'm done with all four.


## Using a parameter to determine the output


One route I could take is to specify the output format as an argument to the
      statement function. I would begin this refactoring by using [Add Parameter](http://refactoring.com/catalog/addParameter.html), extracting the existing text formatting code, and writing some
      code at the start to dispatch to the extracted function when the parameter indicates
      it.


![](video-js_dispatch.png)


```
function statement(customer, movies, format = 'text') {
  switch (format) {
    case "text":
      return textStatement();
  }
  throw new Error(`unknown statement format ${format}`);
```


```
  function textStatement() {
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
    }
    result += `Amount owed is ${totalAmount()}\n`;
    result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
    return result;
  }
```


I can then write the html generating function and add a clause to the dispatcher.


```
  function statement(customer, movies, format = 'text') {
    switch (format) {
      case "text":
        return textStatement();
      case "html":
        return htmlStatement();
    }
    throw new Error(`unknown statement format ${format}`);
  
    function htmlStatement() {
      let result = `<h1>Rental Record for <em>${customer.name}</em></h1>\n`;
      result += "<table>\n";
      for (let r of customer.rentals) {
        result += `  <tr><td>${movieFor(r).title}</td><td>${amountFor(r)}</td></tr>\n`;
      }
      result += "</table>\n";
      result += `<p>Amount owed is <em>${totalAmount()}</em></p>\n`;
      result += `<p>You earned <em>${totalFrequentRenterPoints()}</em> frequent renter points</p>\n`;
      return result;
    }
```


I might fancy using a data structure for the dispatcher logic.


```
function statement(customer, movies, format = 'text') {
  const dispatchTable = {
    "text": textStatement,
    "html": htmlStatement
  };
  if (undefined === dispatchTable[format]) throw new Error(`unknown statement format ${format}`);
  return dispatchTable[format].call();
```


## Using top-level functions


The problem with writing a top-level html statement function is that the
      calculation functions are nested inside the text statement function. So an obvious
      way to proceed is to move them to the top context.


![](video-js_top.png)


To do this, I begin by looking for function that doesn't refer to any others, in
      this case `movieFor`


Whenever I move functions around, I like to do it by first copying the function
      to the new context, fitting it to that context, and then replacing the original
      function body with a call to the moved function.


```
function topMovieFor(rental, movies) {
  return movies[rental.movieID];
}
```


```
function statement(customer, movies) {
  // [snip]
```


```
  function movieFor(rental) {
    return topMovieFor(rental, movies);
  }
```


```
  function frequentRenterPointsFor(rental) {
    return (movieFor(rental).code === "new" && rental.days > 2) ? 2 : 1;
  }
```


I can compile and test at this point, which will tell me if the change in context
      has caused any trouble. Once that's done I can then inline the forwarding function.


```
function movieFor(rental, movies) {
  return movies[rental.movieID];
}
```


```
function statement(customer, movies) {
  // [snip]
```


```
  function frequentRenterPointsFor(rental) {
    return (movieFor(rental, movies).code === "new" && rental.days > 2) ? 2 : 1;
  }
```


There's a similar change inside `amountFor`


As well as the inline, I also renamed the top-level function to match the old
      name, so the only difference is now the `movies` parameter.


I then do that with all the nested functions


```
function statement(customer, movies) {
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    result += `\t${movieFor(r, movies).title}\t${amountFor(r, movies)}\n`;
  }
  result += `Amount owed is ${totalAmount(customer, movies)}\n`;
  result += `You earned ${totalFrequentRenterPoints(customer, movies)} frequent renter points\n`;
  return result;
}
function totalFrequentRenterPoints(customer, movies) {
  return customer.rentals
    .map((r) => frequentRenterPointsFor(r, movies))
    .reduce((a, b) => a + b, 0)
    ;
}
function totalAmount(customer, movies) {
  return customer.rentals
    .reduce((total, r) => total + amountFor(r, movies), 0);
}
function movieFor(rental, movies) {
  return movies[rental.movieID];
}
function amountFor(rental, movies) {
  let result = 0;
  switch (movieFor(rental, movies).code) {
    case "regular":
      result = 2;
      if (rental.days > 2) {
        result += (rental.days - 2) * 1.5;
      }
      return result;
    case "new":
      result = rental.days * 3;
      return result;
    case "childrens":
      result = 1.5;
      if (rental.days > 3) {
        result += (rental.days - 3) * 1.5;
      }
      return result;
  }
  return result;
}
function frequentRenterPointsFor(rental, movies) {
  return (movieFor(rental, movies).code === "new" && rental.days > 2) ? 2 : 1;
}
```


Now I can easily write the html statement function


```
function htmlStatement(customer, movies) {
  let result = `<h1>Rental Record for <em>${customer.name}</em></h1>\n`;
  result += "<table>\n";
  for (let r of customer.rentals) {
    result += `  <tr><td>${movieFor(r, movies).title}</td><td>${amountFor(r, movies)}</td></tr>\n`;
  }
  result += "</table>\n";
  result += `<p>Amount owed is <em>${totalAmount(customer, movies)}</em></p>\n`;
  result += `<p>You earned <em>${totalFrequentRenterPoints(customer, movies)}</em> frequent renter points</p>\n`;
  return result;
}
```


### Declaring some partially-applied local functions


When using a global function like this, parameter lists can get rather long. So
        sometimes it can be useful to declare a local function that calls the global
        function with some, or all, of the parameters filled in. That local function,
        which is a partial application of the global function,  can
        then be used later on. There's various ways to do this in JavaScript. One is to
        assign the local functions to variables.


```
  function htmlStatement(customer, movies) {
    const amount = () => totalAmount(customer, movies);
    const frequentRenterPoints = () => totalFrequentRenterPoints(customer, movies);
    const movie = (aRental) => movieFor(aRental, movies);
    const rentalAmount = (aRental) =>  amountFor(aRental, movies);
    let result = `<h1>Rental Record for <em>${customer.name}</em></h1>\n`;
    result += "<table>\n";
    for (let r of customer.rentals) {
      result += `  <tr><td>${movie(r).title}</td><td>${rentalAmount(r)}</td></tr>\n`;
    }
    result += "</table>\n";
    result += `<p>Amount owed is <em>${amount()}</em></p>\n`;
    result += `<p>You earned <em>${frequentRenterPoints()}</em> frequent renter points</p>\n`;
    return result;
  }
```


Another is to declare them as nested functions.


```
  function htmlStatement(customer, movies) {
    let result = `<h1>Rental Record for <em>${customer.name}</em></h1>\n`;
    result += "<table>\n";
    for (let r of customer.rentals) {
      result += `  <tr><td>${movie(r).title}</td><td>${rentalAmount(r)}</td></tr>\n`;
    }
    result += "</table>\n";
    result += `<p>Amount owed is <em>${amount()}</em></p>\n`;
    result += `<p>You earned <em>${frequentRenterPoints()}</em> frequent renter points</p>\n`;
    return result;
  
    function amount() {return totalAmount(customer, movies);}
    function frequentRenterPoints() {return totalFrequentRenterPoints(customer, movies);}
    function rentalAmount(aRental) {return amountFor(aRental, movies);}
    function movie(aRental) {return movieFor(aRental, movies);}
  }
```


Yet another approach is to use [`bind`.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
        I'll leave you to look up that one - it's not something I'd use here as I find
        these forms easier to follow.


## Using classes


Object-orientation is familiar to me, so it's a not surprise that I'm going to
      consider classes and objects. ES6 introduced good syntax for classical
      OO. Let's look at how I'd apply it to this example.


![](video-js_class.png)


My first step is to wrap the data in objects, starting with the customer.


customer.es6â¦


```
  export default class Customer {
    constructor(data) {
      this._data = data;
    }
  
    get name() {return this._data.name;}
    get rentals() { return this._data.rentals;}
  }
```


statement.es6â¦


```
  import Customer from './customer.es6';
  
  function statement(customerArg, movies) {
    const customer = new Customer(customerArg);
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
    }
    result += `Amount owed is ${totalAmount()}\n`;
    result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
    return result;
```


So far the class is just a simple wrapper over the original JavaScript object.
      I'll next do a similar wrapper with the rental.


rental.es6â¦


```
  export default class Rental {
    constructor(data) {
      this._data = data;
    }
    get days() {return this._data.days}
    get movieID() {return this._data.movieID}
  }
```


customer.es6â¦


```
  import Rental from './rental.es6'
  
  export default class Customer {
    constructor(data) {
      this._data = data;
    }
  
    get name() {return this._data.name;}
    get rentals() { return this._data.rentals.map(r => new Rental(r));}
  }
```


Now that I have classes wrapped around my simple json objects, I have a target
      for a [Move Method](http://refactoring.com/catalog/moveMethod.html). As with moving functions to the top level,
      the first function to work with is one that doesn't call any others -
      `movieFor`. But this function needs the list of movies as context, which
      will need to be made available to the newly created rental objects.


statement.es6â¦


```
  function statement(customerArg, movies) {
    const customer = new Customer(customerArg, movies);
    let result = `Rental Record for ${customer.name}\n`;
    for (let r of customer.rentals) {
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
    }
    result += `Amount owed is ${totalAmount()}\n`;
    result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
    return result;
```


class Customerâ¦


```
  constructor(data, movies) {
    this._data = data;
    this._movies = movies
  }
  get rentals() { return this._data.rentals.map(r => new Rental(r, this._movies));}
```


class Rentalâ¦


```
  constructor(data, movies) {
    this._data = data;
    this._movies = movies;
  }
```


Once I have the supporting data in place, I can move the function.


statement.es6â¦


```
  function movieFor(rental) {
    return rental.movie;
  }
```


class Rentalâ¦


```
  get movie() {
    return this._movies[this.movieID];
  }
```


As with the move I did earlier, the first step is to put the core behavior in the
      new context, fit it into that context, and adjust the original function to call the
      new one. Once this is working, it's relatively easy to inline the original function
      calls.


statement.es6â¦


```
function statement(customerArg, movies) {
  const customer = new Customer(customerArg, movies);
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    result += `\t${r.movie.title}\t${amountFor(r)}\n`;
  }
  result += `Amount owed is ${totalAmount()}\n`;
  result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
  return result;
```


```
  function amountFor(rental) {
    let result = 0;
    switch (rental.movie.code) {
      case "regular":
        result = 2;
        if (rental.days > 2) {
          result += (rental.days - 2) * 1.5;
        }
        return result;
      case "new":
        result = rental.days * 3;
        return result;
      case "childrens":
        result = 1.5;
        if (rental.days > 3) {
          result += (rental.days - 3) * 1.5;
        }
        return result;
    }
    return result;
  }
```


```
  function frequentRenterPointsFor(rental) {
    return (rental.movie.code === "new" && rental.days > 2) ? 2 : 1;
  }
```


I can use the same basic sequence to move the two calculations into the rental
      too.


statement.es6â¦


```
function statement(customerArg, movies) {
  const customer = new Customer(customerArg, movies);
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    result += `\t${r.movie.title}\t${r.amount}\n`;
  }
  result += `Amount owed is ${totalAmount()}\n`;
  result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
  return result;
```


```
  function totalFrequentRenterPoints() {
    return customer.rentals
      .map((r) => r.frequentRenterPoints)
      .reduce((a, b) => a + b, 0)
      ;
  }
  function totalAmount() {
    return customer.rentals
      .reduce((total, r) => total + r.amount, 0);
  }
```


class Rentalâ¦


```
  get frequentRenterPoints() {
    return (this.movie.code === "new" && this.days > 2) ? 2 : 1;
  }
  get amount() {
    let result = 0;
    switch (this.movie.code) {
      case "regular":
        result = 2;
        if (this.days > 2) {
          result += (this.days - 2) * 1.5;
        }
        return result;
      case "new":
        result = this.days * 3;
        return result;
      case "childrens":
        result = 1.5;
        if (this.days > 3) {
          result += (this.days - 3) * 1.5;
        }
        return result;
    }
    return result;
  }
```


I can then move the two totalling functions to the customer


statement.es6â¦


```
function statement(customerArg, movies) {
  const customer = new Customer(customerArg, movies);
  let result = `Rental Record for ${customer.name}\n`;
  for (let r of customer.rentals) {
    result += `\t${r.movie.title}\t${r.amount}\n`;
  }
  result += `Amount owed is ${customer.amount}\n`;
  result += `You earned ${customer.frequentRenterPoints} frequent renter points\n`;
  return result;
}
```


class Customerâ¦


```
  get frequentRenterPoints() {
    return this.rentals
      .map((r) => r.frequentRenterPoints)
      .reduce((a, b) => a + b, 0)
      ;
  }
  get amount() {
    return this.rentals
      .reduce((total, r) => total + r.amount, 0);
  }
```


With the calculation logic moved into the rental and customer objects, writing the
     html version of the statement is simple.


statement.es6â¦


```
  function htmlStatement(customerArg, movies) {
    const customer = new Customer(customerArg, movies);
    let result = `<h1>Rental Record for <em>${customer.name}</em></h1>\n`;
    result += "<table>\n";
    for (let r of customer.rentals) {
      result += `  <tr><td>${r.movie.title}</td><td>${r.amount}</td></tr>\n`;
    }
    result += "</table>\n";
    result += `<p>Amount owed is <em>${customer.amount}</em></p>\n`;
    result += `<p>You earned <em>${customer.frequentRenterPoints}</em> frequent renter points</p>\n`;
    return result;
  }
```


### Classes without the syntax


The class syntax in ES2015 is controversial, with some people feeling it isn't
       needed (often with a side of snark about Java developers). You can take exactly the same
       series of refactoring steps to come up with a result like this:


```
function statement(customerArg, movies) {
  const customer = createCustomer(customerArg, movies);
  let result = `Rental Record for ${customer.name()}\n`;
  for (let r of customer.rentals()) {
    result += `\t${r.movie().title}\t${r.amount()}\n`;
  }
  result += `Amount owed is ${customer.amount()}\n`;
  result += `You earned ${customer.frequentRenterPoints()} frequent renter points\n`;
  return result;

  
}
function createCustomer(data, movies) {
  return {
    name: () => data.name,
    rentals: rentals,
    amount: amount,
    frequentRenterPoints: frequentRenterPoints
  };

  function rentals() {
    return data.rentals.map(r => createRental(r, movies));
  }
  function frequentRenterPoints() {
    return rentals()
      .map((r) => r.frequentRenterPoints())
      .reduce((a, b) => a + b, 0)
      ;
  }
  function amount() {
    return rentals()
      .reduce((total, r) => total + r.amount(), 0);
  }

}

function createRental(data, movies) {
  return {
    days: () => data.days,
    movieID: () => data.movieID,
    movie: movie,
    amount: amount,
    frequentRenterPoints: frequentRenterPoints
  };

  function movie() {
    return movies[data.movieID];
  }

  function amount() {
    let result = 0;
    switch (movie().code) {
      case "regular":
        result = 2;
        if (data.days > 2) {
          result += (data.days - 2) * 1.5;
        }
        return result;
      case "new":
        result = data.days * 3;
        return result;
      case "childrens":
        result = 1.5;
        if (data.days > 3) {
          result += (data.days - 3) * 1.5;
        }
        return result;
    }
    return result;
  }

  function frequentRenterPoints() {
    return (movie().code === "new" && data.days > 2) ? 2 : 1;
  }


}
```


This approach uses the [Function As Object](http://www.cs.uni.edu/~wallingf/patterns/envoy.pdf) pattern.
       Constructor functions (`createCustomer` and `createRental`)
       return a JavaScript object (hash) of function references. Each constructor function
       contains a closure that holds the object's data. Because the returned object of
       functions are in the same function context they can access this data. I see this as
       exactly the same pattern as using the class syntax, but implemented a different
       way. I prefer to use the explicit syntax since it is more explicit - thus making my
       thinking clearer.


## Data Transformation


All of these approaches have involved the statement printing functions calling
     other functions to calculate the data they need. Another approach to do this is to
     pass this data to the statement printing functions in the data structure itself. In
     this approach the calculation functions are used to transform the customer data
     structure so that it has all the data the printing functions need.


![](video-js_transform.png)


In refactoring terms this is an example of not-yet-written Split Phase refactoring
     that Kent Beck described to me last summer. With this refactoring I split the computation
     into two phases that communicate using an intermediate data structure. I begin this
     refactoring by introducing the intermediate data structure.


```
  function statement(customer, movies) {
    const data = createStatementData(customer, movies);
    let result = `Rental Record for ${data.name}\n`;
    for (let r of data.rentals) {
      result += `\t${movieFor(r).title}\t${amountFor(r)}\n`;
    }
    result += `Amount owed is ${totalAmount()}\n`;
    result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
    return result;
  
    function createStatementData(customer, movies) {
      let result = Object.assign({}, customer);
      return result;
    }
```


For this case I'm enriching the original customer data structure with added
     elements, hence starting with a call to `Object.assign`. I could also make
     an entirely new data structure, the choice really depends on how different the
     transformed data structure is to the original.


I then do the same thing for each line of rental


function                                                                          statementâ¦


```
  function createStatementData(customer, movies) {
    let result = Object.assign({}, customer);
    result.rentals = customer.rentals.map(r => createRentalData(r));
    return result;

    function createRentalData(rental) {
      let result = Object.assign({}, rental);
      return result;
    }
  }
```


Notice that I nest `createRentalData` inside
     `createStatementData` since any caller of `createStatementData`
     won't need to know about how the inside is built up.


I can then start to populate the transformed data, beginning with the title of the
     rented movie.


```
function statement(customer, movies) {
  const data = createStatementData(customer, movies);
  let result = `Rental Record for ${data.name}\n`;
  for (let r of data.rentals) {
    result += `\t${r.title}\t${amountFor(r)}\n`;
  }
  result += `Amount owed is ${totalAmount()}\n`;
  result += `You earned ${totalFrequentRenterPoints()} frequent renter points\n`;
  return result;
```


```
  //â¦

  function createStatementData(customer, movies) {
    // â¦
```


```
    function createRentalData(rental) {
      let result = Object.assign({}, rental);
      result.title = movieFor(rental).title;
      return result;
    }
  }
```


I follow with the calculation for the amount, followed by the totals.


```
function statement(customer, movies) {
  const data = createStatementData(customer, movies);
  let result = `Rental Record for ${data.name}\n`;
  for (let r of data.rentals) {
    result += `\t${r.title}\t${r.amount}\n`;
  }
  result += `Amount owed is ${data.totalAmount}\n`;
  result += `You earned ${data.totalFrequentRenterPoints} frequent renter points\n`;
  return result;

  function createStatementData(customer, movies) {
    let result = Object.assign({}, customer);
    result.rentals = customer.rentals.map(r => createRentalData(r));
    result.totalAmount = totalAmount();
    result.totalFrequentRenterPoints = totalFrequentRenterPoints();
    return result;

    function createRentalData(rental) {
      let result = Object.assign({}, rental);
      result.title = movieFor(rental).title;
      result.amount = amountFor(rental);
      return result;
    }
  }
```


Now that I've made all the calculation functions put the result of their
     calculations as data, I can move the functions to separate them from the statement
     rendering function. First I move all the calculation functions inside
     `createStatementData`


```
function statement (customer, movies) {
  // body â¦
  function createStatementData (customer, movies) {
    // body â¦

    function createRentalData(rental) { â¦ }
    function totalFrequentRenterPoints() { â¦ }
    function totalAmount() { â¦ }
    function movieFor(rental) { â¦ }
    function amountFor(rental) { â¦ }
    function frequentRenterPointsFor(rental) { â¦ }
  }
}
```


Then I move `createStatementData` outside of
     `statement`.


```
function statement (customer, movies) { â¦ }

function createStatementData (customer, movies) {
  function createRentalData(rental) { â¦ }
  function totalFrequentRenterPoints() { â¦ }
  function totalAmount() { â¦ }
  function movieFor(rental) { â¦ }
  function amountFor(rental) { â¦ }
  function frequentRenterPointsFor(rental) { â¦ }
}
```


Once I've separated the functions like this, I can write the HTML version of the
     statement to use the same data structure.


```
function htmlStatement(customer, movies) {
  const data = createStatementData(customer, movies);
  let result = `<h1>Rental Record for <em>${data.name}</em></h1>\n`;
  result += "<table>\n";
  for (let r of data.rentals) {
    result += `  <tr><td>${r.title}</td><td>${r.amount}</td></tr>\n`;
  }
  result += "</table>\n";
  result += `<p>Amount owed is <em>${data.totalAmount}</em></p>\n`;
  result += `<p>You earned <em>${data.totalFrequentRenterPoints}</em> frequent renter points</p>\n`;
  return result;
}
```


I can also move `createStatementData` to a separate module to further
     clarify the boundaries between calculating the data and rendering the statements.


statement.es6


```
  import createStatementData from './createStatementData.es6';
  function htmlStatement(customer, movies) { â¦ }
  function statement(customer, movies) { â¦ }
```


createStatementData.es6


```
  export default function createStatementData (customer, movies) {
    function createRentalData(rental) { â¦ }
    function totalFrequentRenterPoints() { â¦ }
    function totalAmount() { â¦ }
    function movieFor(rental) { â¦ }
    function amountFor(rental) { â¦ }
    function frequentRenterPointsFor(rental) { â¦ }
  }
```


## Comparing the approaches


So now it's time to step back and take a look at what I've got. I have an initial
     body of code, written as a single inline function. I wished to
     refactor this code to enable an html rendering without duplicating the calculation
     code. My first step
     was to break this code up into several functions, living within the original function
     . From there, I explored four distinct
     paths:


![](video-js_main.png)


top-level-functions


write all functions as top-level functions


Â Â Â Â function htmlStatement(customer, movies)


Â Â Â Â function textStatement(customer, movies)


Â Â Â Â function totalAmount(customer, movies)


Â Â Â Â function totalFrequentRenterPoints(customer, movies)


Â Â Â Â function amountFor(rental, movies)


Â Â Â Â function frequentRenterPointsFor(rental, movies)


Â Â Â Â function movieFor(rental, movies)


[show code](top-level-functions.html)


parameter-dispatch


use a parameter to the top-level function to state what format of output
    to emit


Â Â Â Â function statement(customer, movies, format)


Â Â Â Â Â Â Â Â function htmlStatement()


Â Â Â Â Â Â Â Â function textStatement()


Â Â Â Â Â Â Â Â function totalAmount()


Â Â Â Â Â Â Â Â function totalFrequentRenterPoints()


Â Â Â Â Â Â Â Â function amountFor(rental)


Â Â Â Â Â Â Â Â function frequentRenterPointsFor(rental)


Â Â Â Â Â Â Â Â function movieFor(rental)


[show code](parameter-dispatch.html)


classes


move calculation logic to classes which are used by rendering functions


Â Â Â Â function textStatement(customer, movies)


Â Â Â Â function htmlStatement(customer, movies)


Â Â Â Â class Customer


Â Â Â Â Â Â Â Â get amount()


Â Â Â Â Â Â Â Â get frequentRenterPoints()


Â Â Â Â Â Â Â Â get rentals()


Â Â Â Â class Rental


Â Â Â Â Â Â Â Â get amount()


Â Â Â Â Â Â Â Â get frequentRenterPoints()


Â Â Â Â Â Â Â Â get movie()


[show code](classes.html)


transform


split calculation logic into separate nested function that produces an
    intermediate data structure for the rendering functions


Â Â Â Â function statement(customer, movies)


Â Â Â Â function htmlStatement(customer, movies)


Â Â Â Â function createStatementData(customer, movies)


Â Â Â Â Â Â Â Â function createRentalData()


Â Â Â Â Â Â Â Â function totalAmount()


Â Â Â Â Â Â Â Â function totalFrequentRenterPoints()


Â Â Â Â Â Â Â Â function amountFor(rental)


Â Â Â Â Â Â Â Â function frequentRenterPointsFor(rental)


Â Â Â Â Â Â Â Â function movieFor(rental)


[show code](transform.html)


I'll begin with the top-level-functions example as my baseline for comparison is
     it's the conceptually simplest alternative.2 It's
     simple because it divides the work into a set of pure functions, all of which are
     callable from any point in my code. This is simple to use and simple to test - I can
     test any individual function easily via either test cases or with a REPL.


2: 
     The parameter-dispatch makes a better first refactoring, as its structure is closer
     to the original set of nested functions. But when comparing alternatives the
     top-level-functions case is the better starting point.


The downside with top-level-functions is that there's a lot of repetitive
     parameter passing. Each function needs to be given the movies data structure and the
     customer level functions also to be given a customer structure. I'm not concerned about the
     repetitive typing here, but I am concerned about the repetitive reading. Each time I
     read the parameters I have to figure out what they are and check to see if the
     parameters are changing. For all these functions, the customer and the movies data
     are common context - but with top-level-functions that common context isn't made
     explicit. I infer it as I read the program and build the model of its execution in my
     mind, but I prefer things to be as explicit as possible.


This factor becomes more important as that context grows. I have only two data
     items here, but it's not uncommon to find many more. Using top-level functions alone
     I end up with large parameter lists on every call, each one adding to the load on my reading
     comprehension. This can lead to the trap of bundling all these parameters into a
     context parameter, which contains all context for many functions, and ends up
     obscuring what these functions do. I can reduce the pain of all this by defining
     local partially-applied functions, but that's a lot of extra function declaring to
     throw in the mix — which has to be duplicated with each bit of client code.


The advantage of the three other alternatives is that they each make the common
     context explicit, capturing it within the structure of the program. The
     parameter-dispatch approach does this by capturing the context in the top level
     parameter list, which is then available as common context to all nested functions.
     This works particularly well with the original code, making the refactoring from
     single function to nested functions simpler than a language that lacks nested
     functions.


But the parameter-dispatch approach starts to wobble when I need different overall
     behaviors from my context, such as an html format response. I need to write some kind
     of dispatcher to decide which function I want to invoke. Specifying a format to a
     renderer isn't too bad, but such dispatch logic is a distinct smell. However I write
     it, it's still essentially duplicating the core ability of the language to call a
     named function. I'm heading down a path that can quickly lead me to the nonsense of:


```
function executeFunction (name, args) {
  const dispatchTable = {
    //...
```


There is a context for this kind of approach, which is when the choice of output
     format does come to my caller as data. In that case there has to be a dispatch
     mechanism on that data item. However if my callers are calling the statement function
     like this…


```
const someValue = statement(customer, movieList, 'text');
```


…then there's no way I should be writing dispatch logic in my code.


The calling method is the key here. Using literal values to indicate choice of
     function is a smell. Instead of this API, let the caller say what they want as part
     of the function name, `textStatement` or `htmlStatement`. Then
     I can use the language's function dispatch mechanism and avoid cobbling together
     something else myself.


So with these two alternatives under my belt, where am I? I want some explicit
     common context for some logic, but need to call different operations using that
     logic. When I feel this kind of need, I immediately think of using object-orientation - which
     is in essence a set independently invokable operations on a common context. 3 This leads me to the classes version of the example,
     which allows me to capture the common context of the customer and movies within the
     customer and rental objects. I set the context once when I instantiate the objects, and
     then all further logic can use that common context.


3: 
     I rather like [Will Cook's
     proposal for a definition of âobjectâ](http://wcook.blogspot.com/2012/07/proposal-for-simplified-modern.html)


The object methods are like the partially applied local functions in the top-level
     case, except that here the common context is supplied by the constructor. I thus only
      write the local functions, not the top-level ones. The caller indicates the context
      with the constructor and then calls the local function directly. I can think of the
     local methods as partial applications of notional top-level functions on the common
     context of the object instance.


Using classes introduces a further notion - that of separating the rendering logic
     from the calculation logic. One of the faults of the original single function is that
     it mixes the two together. Splitting into functions separates them to some degree,
     but they all still exist in the same conceptual space. That's a touch unfair, I could
     put the calculation functions into one file and the rendering functions into another,
     linking them by appropriate import statements. But I find that a common context
     provides a natural hint for how to group logic into modules.


I've described the objects as a set of common partial applications, but there's
     another way to look at them. The objects are instantiated with an input data
     structure, but enrich this data with computed data exposed through their calculation
     functions. I've reinforced this way of thinking by making these getters, so a client treats them
     exactly the same as raw data - applying the [Uniform Access Principle](https://martinfowler.com/bliki/UniformAccessPrinciple.html). I can think of this as a transformation from the
     constructor argument to this virtual data structure of getters. The transform example
     is the same idea, but implemented by creating a new data structure that combines the
     initial data with all the calculated data. Just as the objects encapsulate the
     calculation logic inside the customer and rental classes, the transform approach
     encapsulates that logic inside `createStatementData` and
     `createRentalData`. This approach of transforming basic [List And Hash](https://martinfowler.com/bliki/ListAndHash.html) data structures is a common feature of much functional thinking.
     It allows the `create…Data` functions to share the context that they need and the
     rendering logic to use the multiple outputs in a simple manner.


One minor difference between thinking of the class as a transform and transform approach
     itself is when the transform computation happens. The transform approach here transforms all at
     once, while the classes make individual transforms with each call. I can easily
     switch when the computation happens to match the other. In the classes case I can
     perform all computation at once by doing it in the constructor. For the transform
     case I can recompute on demand by returning functions in the intermediate data
     structure. Almost always the performance differences here will be insignificant, if
     any of these functions is expensive my best bet is usually to use a method/function and
     cache the result after the first call.


So there are four approaches - what is my preference? I don't care for writing
     dispatcher logic, so I wouldn't use the parameter-dispatch approach. The
     top-level-functions are something I'd consider, but my taste for them plummets
     rapidly as the shared context increases in size. Even with only two arguments, I'd be
     inclined to reach for the other alternatives. Choosing between the classes and
     transform approach is harder, both provide a good way of making common context
     explicit and separating concerns well. I don't care for cage fights, so maybe I just
     make them play tiddlywinks and pick the winner.


## Further Refactorings


In this exploration, I've explored four ways of arranging the calculation and
     rendering functions. Software is a very malleable medium and there are more
     variations that could be done with this, but these are the four that I think are the
     most interesting to discuss.


There are also further refactorings than just the arrangement of these functions.
     In the book example I decomposed the `amount` and
     `frequentRenterPoint` calculations to support extending the model with new
     movie types. There are changes I'd make to the rendering code, such as pulling out a
     common pattern of header, lines, and footer. But I think the four paths are enough to
     think about for this article.


My conclusion, if I have one, is that there are different ways to sensibly arrange
     observably identical
     computation. Different languages encourage certain styles - the original book
     refactoring was done in Java, which greatly encourages the classes style. JavaScript
     handily supports multiple styles, which is good because it provides the programmer
     with options, and bad because it supplies the programmer with options. (One of the
     difficulties in programming in JavaScript is that there is little consensus on what
     is good style.) It's useful to understand these different styles, but more important
     to realize what ties them together. Small functions, providing they are well-named,
     can be combined and manipulated to support varied needs both at the same time and
     over time. Common contexts suggest grouping logic together, while much of the art of
     programming is deciding how to separate concerns into a clear set of such contexts.


---
