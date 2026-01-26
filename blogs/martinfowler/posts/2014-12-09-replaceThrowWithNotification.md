---
title: "Replacing Throwing Exceptions with Notification in Validations"
description: "If you're validating some data, you usually shouldn't be using     exceptions to signal validation failures. Here I describe how I'd     refactor such code into using the Notification pattern."
date: 2014-12-09T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/articles/replaceThrowWithNotification.html
slug: replaceThrowWithNotification
word_count: 3192
---


I was recently looking at some code to do some basic
    validation of some incoming JSON messages. It looked something like this.


```
public void check() {
   if (date == null) throw new IllegalArgumentException("date is missing");
   LocalDate parsedDate;
   try {
     parsedDate = LocalDate.parse(date);
   }
   catch (DateTimeParseException e) {
     throw new IllegalArgumentException("Invalid format for date", e);
   }
   if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
   if (numberOfSeats == null) throw new IllegalArgumentException("number of seats cannot be null");
   if (numberOfSeats < 1) throw new IllegalArgumentException("number of seats must be positive");
 }
```


The code for this example is Java


This is a common way to approach validation. You run a series
    of checks on some data (here just some fields within the class in
    question). If any of these checks fails, you throw an exception
    with an error message.


I have a couple of problems with this approach. Firstly I'm not
    happy with using exceptions for something like this. Exceptions
    signal something outside the expected bounds of behavior of the
    code in question. But if you're running some checks on outside input,
    this is because you expect some messages to fail - and if a
    failure is expected behavior, then you shouldn't be
    using exceptions.


if a failure is expected behavior, then you shouldn't
    be using exceptions


The second problem with code like this is that it fails with
    the first error it detects, but usually it's better to report all
    errors with the incoming data, not just the first. That way a
    client can choose to display all errors for the user to fix in a
    single interaction rather than give her the impression she's
    playing a game of whack-a-mole with the computer.


My preferred way to deal with reporting validation issues like
    this is the [Notification
    pattern](https://martinfowler.com/eaaDev/Notification.html). A notification is an object that collects errors,
     each validation failure adds an error to the notification. A
    validation method returns a notification, which you can then
    interrogate to get more information. A simple usage looks
    has code like this for the checks.


```
private void validateNumberOfSeats(Notification note) {
  if (numberOfSeats < 1) note.addError("number of seats must be positive");
  // more checks like this
}
```


We can then have a simple call such as
    `aNotification.hasErrors()` to react if there are any
    errors. Other methods on the notification can drill into more
    details about the errors. 1


1: 
      Another common validation approach is just to return a boolean
      indicating if the input is valid or not. While this makes it
      easy for the caller to invoke different behavior, it doesn't
      give any way to provide diagnostics beyond the useless âan error
      has occurredâ.


![](replaceThrowWithNotification/sketch.png)


## When to use this refactoring


I need to stress here, that I'm not advocating getting rid of
      exceptions throughout your code base. Exceptions are a very
      useful technique for handling exceptional behavior and getting
      it away from the main flow of logic. This refactoring is a good
      one to use only when the outcome signaled by the exception
      isn't really exceptional, and thus should be handled through the
      main logic of the program. The example I'm looking at here,
      validation, is a common case of that.


A useful rule of thumb when considering exceptions comes
      from the Pragmatic Programmers:


> We believe that exceptions should rarely be used as part of
>         a program's normal flow: exceptions should be reserved for
>         unexpected events. Assume that an uncaught exception will
>         terminate your program and ask yourself, âWill this code still
>         run if I remove all the exception handlers?â If the answer is
>         ânoâ, then maybe exceptions are being used in nonexceptional
>         circumstances.
> -- [Dave Thomas and Andy Hunt](https://www.amazon.com/gp/product/020161622X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=020161622X&linkCode=as2&tag=martinfowlerc-20)


An important consequence of this is that whether to use
      exceptions for a particular task is dependent on the context.
      So, as the prags go on to say, reading from a file that isn't
      there may or may not be an exception depending on the
      circumstances. If you are trying to read a well known file
      location, such as `/etc/hosts` on a unix system, then
      it's likely you can assume the file should be there, so
      throwing an exception is reasonable. On the other hand if you
      are trying to read a file from a path that the user has typed in
      on the command-line, then you should expect that it's likely the
      file isn't there, and should use another mechanism - one that
      communicates the unexceptional nature of the error.


There is a case when it may be sensible to use exceptions
      for validation failures. This would be situations where you have
      data that you expect to have already been validated earlier in
      processing, but you want to run the validation checks again to
      guard against a programming error letting some invalid data slip
      through.


This article is about replacing exceptions for notification
      in the context of validating raw input. You may also find this
      technique useful in other situations where a notification is a
      better choice than throwing an exception, but I'm focusing on
      the validation case here, as it is a common one.


## Starting Point


I've not mentioned the example domain so far, since I was just
      interested in the broad shape of the code. But as we explore the
      example further, I'll need to engage with the domain. In this
      case it's some code that receives JSON messages booking seats at a
      theater. The code is in a booking request class that's populated
      from the JSON using the gson library.


```
gson.fromJson(jsonString, BookingRequest.class)

```


Gson takes a class, looks for any fields that match a key in
      the JSON document, and then populates the matching fields.


The booking request contains just two elements that we
      are validating here, the date of the performance and how many
      seats are being requested


class BookingRequestâ¦


```
  private Integer numberOfSeats; 
  private String date;

```


The validation checks are the ones I showed above


class BookingRequestâ¦


```
  public void check() {
     if (date == null) throw new IllegalArgumentException("date is missing");
     LocalDate parsedDate;
     try {
       parsedDate = LocalDate.parse(date);
     }
     catch (DateTimeParseException e) {
       throw new IllegalArgumentException("Invalid format for date", e);
     }
     if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
     if (numberOfSeats == null) throw new IllegalArgumentException("number of seats cannot be null");
     if (numberOfSeats < 1) throw new IllegalArgumentException("number of seats must be positive");
   }
```


## Building a Notification


In order to use a notification, you have to create the
      notification object. A notification can be really simple,
      sometimes just a list of strings will do the trick.


A Notification collects together errors


```
List<String> notification = new ArrayList<>();
if (numberOfSeats < 5) notification.add("number of seats too small");
// do some more checks

// then laterâ¦
if ( ! notification.isEmpty()) // handle the error condition

```


Although a simple list idiom makes a lightweight implementation of
      the pattern, I usually like to do a bit more than this, creating
      a simple class instead.


```
public class Notification {
  private List<String> errors = new ArrayList<>();

  public void addError(String message) { errors.add(message); }
  public boolean hasErrors() {
    return ! errors.isEmpty();
  }
  â¦

```


By using a real class, I can make my intention clearer - the
      reader doesn't have to perform the mental map between the idiom
      and its full meaning.


## Splitting the check method


My first step is to split the check method into two parts, an
      inner part that will eventually deal only with notifications and
      not throw any exceptions, and an outer part that will preserve
      the current behavior of the check method, which is to throw an
      exception is there are any validation failures.


My first step to do this is to use [Extract Method](http://refactoring.com/catalog/extractMethod.html) in an unusual way in that I'm extracting the
      entire body of the check method into a validation method.


class BookingRequestâ¦


```
  public void check() {
    validation();
  }

  public void validation() {
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
    if (numberOfSeats == null) throw new IllegalArgumentException("number of seats cannot be null");
    if (numberOfSeats < 1) throw new IllegalArgumentException("number of seats must be positive");
  }
```


I then adjust the validation method to create and return a
      notification.


class BookingRequestâ¦


```
  public Notification validation() {
    Notification note = new Notification();
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
    if (numberOfSeats == null) throw new IllegalArgumentException("number of seats cannot be null");
    if (numberOfSeats < 1) throw new IllegalArgumentException("number of seats must be positive");
    return note;
  }
```


I can now test the notification and throw an exception if it
      contains errors.


class BookingRequestâ¦


```
  public void check() {
    if (validation().hasErrors()) 
      throw new IllegalArgumentException(validation().errorMessage());
  }
```


I made the validation method public, because I'm expecting
      that most callers in the future will prefer to use this method,
      rather than the check method.


Splitting the original method allows me to separate the
      validation check from the decision about how to respond to failure.


At this point I haven't changed the behavior of the code at
      all, the notification won't contain any errors and any
      validation checks that fail will continue to throw an exception
      and ignore the new machinery I've put in. But I've now set
      things up ready to start replacing exception throws with
      manipulating the notification.


Before I go on to that, however, I need to say something
      about error messages. When we're doing a refactoring, the rule
      is to avoid changes in observable behavior. In situations like
      this, such a rule leads immediately to the question of what
      behavior is observable. Obviously the throwing of the correct
      exception is something the outer program will observe - but to
      what extent do they care about the error message? The
      notification will eventually collect multiple errors and could
      summarize them together into a single message with something
      like


class Notificationâ¦


```
  public String errorMessage() {
    return errors.stream()
      .collect(Collectors.joining(", "));
  }

```


But that would be a problem if the higher levels of the
      program was relying on only getting the message from the first
      error that's detected, in which case you'd need something like


class Notificationâ¦


```
  public String errorMessage() { return errors.get(0); }

```


You have to look not just at the calling function, but also
      any exception handlers to figure out what the right response is
      in this situation.


Although there's no way I should have introduced any problems
      at this point, I would certainly compile and test before making
      the next changes. Just because there's no chance any sensible
      person could have messed those changes up doesn't mean I can't
      mess it up.


## Validating the number


The obvious thing to do now is to replace the first
      validation


class BookingRequestâ¦


```
  public Notification validation() {
    Notification note = new Notification();
    if (date == null) note.addError("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
    if (numberOfSeats == null) throw new IllegalArgumentException("number of seats cannot be null");
    if (numberOfSeats < 1) throw new IllegalArgumentException("number of seats must be positive");
    return note;
  }

```


An obvious move, but a bad one, as this will break the code.
      If we pass a null date into the function, it will add an error
      to the notification, but then merrily attempt to parse it and
      throw a null pointer exception - which isn't the exception we
      were looking for.


So the non-obvious, but more effective thing to do in this
      case is to go backwards.


class BookingRequestâ¦


```
  public Notification validation() {
    Notification note = new Notification();
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
    if (numberOfSeats == null) throw new IllegalArgumentException("number of seats cannot be null");
    if (numberOfSeats < 1) note.addError("number of seats must be positive");
    return note;
  }

```


The previous check is a null check, so we need to use a
      conditional to avoid creating a null pointer exception.


class BookingRequestâ¦


```
  public Notification validation() {
    Notification note = new Notification();
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
    if (numberOfSeats == null) note.addError("number of seats cannot be null");
    else if (numberOfSeats < 1) note.addError("number of seats must be positive");
    return note;
  }

```


I see the next check involves a different field. Together
      with having to introduce a conditional with the previous
      refactoring, I'm now thinking this validation method is getting
      too complex and could do with being decomposed. So I extract the
      number validation parts.


class BookingRequestâ¦


```
  public Notification validation() {
    Notification note = new Notification();
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
    validateNumberOfSeats(note);
    return note;
  }

  private void validateNumberOfSeats(Notification note) {
    if (numberOfSeats == null) note.addError("number of seats cannot be null");
    else if (numberOfSeats < 1) note.addError("number of seats must be positive");
  }

```


Looking at the extracted validation for the number, I don't
      really like its structure. I don't like using if-then-else
      blocks in validation, since it can easily lead to overly nested
      code. I prefer linear code that aborts once it can't go on any
      further, which we can do with a guard clause. So I apply
      [Replace Nested Conditional with Guard Clauses](http://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html).


class BookingRequestâ¦


```
  private void validateNumberOfSeats(Notification note) {
    if (numberOfSeats == null) {
      note.addError("number of seats cannot be null");
      return;
    }
    if (numberOfSeats < 1) note.addError("number of seats must be positive");
  }

```


when we refactor we
      should always try to take the smallest steps we can that
      preserve behavior


My decision to go backwards in order to keep the code green
      is an example of a crucial element of refactoring. Refactoring
      is a specific technique to restructure code through a series of
      behavior-preserving transformations. So when we refactor we
      should always try to take the smallest steps we can that
      preserve behavior. By doing this we reduce the chances of an
      error that will trap us in the debugger


## Validating the Date


With the date validation, I think I'll start with [Extract Method](http://refactoring.com/catalog/extractMethod.html):


class BookingRequestâ¦


```
  public Notification validation() {
    Notification note = new Notification();
    validateDate(note);
    validateNumberOfSeats(note);
    return note;
  }

  private void validateDate(Notification note) {
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) throw new IllegalArgumentException("date cannot be before today");
  }

```


When I used the automated extract method
      in my IDE, the resulting code did not include the notification
      argument. So I had to add that in manually.


Now it's time to start rolling backwards through the date
      validation


class BookingRequestâ¦


```
  private void validateDate(Notification note) {
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      throw new IllegalArgumentException("Invalid format for date", e);
    }
    if (parsedDate.isBefore(LocalDate.now())) note.addError("date cannot be before today");
  }

```


With the second step, there is a
      complication in the error handling, since the thrown exception
      includes a cause exception. To handle that I need to change the
      notification to accept a cause exception. Since I'm in the
      middle of changing the throw to adding an error to the
      notification, my code is red, so I backout what I'm doing to
      leave the validateDate method at the state above, while I
      prepare the notification for including a cause exception.


I start modifying the notification by adding a new addError
      method that takes the cause, and adjusting the original method
      to call the new one. 2


2: 
      This is sometimes referred to as a chained constructor. You can
      also think of if as an example of partial application - not that
      functional programmers would countenance using such terminology
      in the slumlands of a Java program.


class Notificationâ¦


```
  public void addError(String message) {
    addError(message, null);
  }

  public void addError(String message, Exception e) {
    errors.add(message);
  }

```


This means we accept the cause exception, but ignore it. To
      put it somewhere I need to change the error record from a simple
      string to a only-slightly-less simple object.


class Notificationâ¦


```
  private static class Error {
    String message;
    Exception cause;

    private Error(String message, Exception cause) {
      this.message = message;
      this.cause = cause;
    }
  }

```


I usually dislike non-private fields in java, but since this
      is a private inner class, I'm ok with it. If I were to expose
      this error class outside the notification, I would encapsulate
      those fields.


Now I have the class, I need to modify the notification to
      use it rather than the string.


class Notificationâ¦


```
  private List<Error> errors = new ArrayList<>();

  public void addError(String message, Exception e) {
    errors.add(new Error(message, e));
  }
  public String errorMessage() {
    return errors.stream()
            .map(e -> e.message)
            .collect(Collectors.joining(", "));
  }

```


With the new notification in place, I can now make the change
      to the booking request


class BookingRequestâ¦


```
  private void validateDate(Notification note) {
    if (date == null) throw new IllegalArgumentException("date is missing");
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      note.addError("Invalid format for date", e);
      return;
    }
    if (parsedDate.isBefore(LocalDate.now())) note.addError("date cannot be before today");

```


Since I'm already in an extracted method, it's easy to abort
      the rest of the validation with a return.


And the last change is simple


class BookingRequestâ¦


```
  private void validateDate(Notification note) {
    if (date == null) {
      note.addError("date is missing");
      return;
    }
    LocalDate parsedDate;
    try {
      parsedDate = LocalDate.parse(date);
    }
    catch (DateTimeParseException e) {
      note.addError("Invalid format for date", e);
      return;
    }
    if (parsedDate.isBefore(LocalDate.now())) note.addError("date cannot be before today");
  }

```


## Moving up the stack


Once we have the new method, the next task is to look at the
      callers of the original check method and consider adjusting them
      to make use of the new validate method instead. This will entail
      a broader look at how validation fits into the flow of the
      application, so it's outside the scope of this refactoring. But
      the medium-term target should be to eliminate the use of
      exceptions in any circumstance where we might expect validation failures.


In many cases this should lead to being able to get rid of
      the check method entirely. In which case any tests on that
      method should be reworked to use the validate method. We might
      also want to adjust the tests to probe for proper collection of
      multiple errors using the notification.


---
