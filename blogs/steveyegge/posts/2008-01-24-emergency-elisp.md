---
title: "Emergency Elisp"
date: 2008-01-24
url: https://steve-yegge.blogspot.com/2008/01/emergency-elisp.html
word_count: 5119
---

Are you an Emacs user but don't know Lisp?  Welcome to my first Emacs Lisp primer!  This should hopefully help get you over the hurdle so you can have more control over your Emacs sessions.
There are lots of ways to do things in Lisp, and some are "Lispier" than others.  I'm going to focus on how to do things you probably already know how to do from C++ or Java.
I'm mostly focusing on the language itself, since that's arguably the hardest part.  There are tons of Emacs-specific APIs that you can learn how to use from the documentation.
Lisp is good at some things (like code that generates code) and not so good at others (like arithmetic expressions).  I will generally avoid talking about good vs. bad, and just talk about how to do things.  Emacs Lisp is like any other language – you get used to it eventually.
Most Lisp introductions try to give you the "Tao of Lisp", complete with incense-burning, chanting, yoga and all that stuff.  What I really wanted in the beginning was a simple cookbook for doing my "normal" stuff in Lisp.  So that's what this is.  It's an introduction to how to write C, Java or JavaScript code in Emacs Lisp, more or less.
Here goes.  Let's see how short I can make it.  I'll start with the boring (but hopefully familiar) lexical tokens and operators, then move on to how to implement various favorite statements, declarations and other programming constructs.
**Quick Start**
Lisp is written as nested parenthesized expressions like
.  These expressions are sometimes called
*forms*
(in the sense of "shapes".)
There are also "atoms" (leaf nodes, basically) that are not parenthesized:  strings, numbers, symbols (which must be quoted with apostrophe for use as symbols, like
), vectors, and other miscellany.
There are only single-line comments:  semicolon to end of line.
To set a variable named
to the value "bar":

```
(setq foo "bar")  ; setq means "set quoted"
```

To call a function named
with arguments "flim" and "flam":

```
(foo-bar "flim" "flam")
```

To compute the arithmetic expression (0x15 * (8.2 + (7 << 3))) % 2:

```
(% (* #x15 (+ 8.2 (lsh 7 3))) 2)
```

In other words, arithmetic uses prefix notation, just like lisp function calls.
There's no static type system; you use runtime predicates to figure out the type of a data item.  In elisp, predicate functions often end with "p".  I'll let you figure out what it stands for.
*Important:*
You can (and should) experiment with Lisp in the
buffer.  You can evaluate an expression and see its result in any of several ways, including:
1. Put your cursor after the last close-paren and type `C-j` (control + j)
2. Put your cursor inside the expression and type `M-C-x` (alt + control + x)
3. Put your cursor after the last close-paren and type `C-x C-e`

The first approach spits the result into the
buffer, and the next two echo it into the minibuffer.  They all also work for atoms – expressions not in parens such as numbers, strings, characters and symbols.

## Lexical Stuff

Lisp has only a handful of lexical tokens (i.e. atomic program elements).
**Comments**
:
Single-line only.  They start with a semicolon:

```
(blah blah blah)   ;  I am a comment
```

**Strings**
:
Double-quoted only.

```
"He's said: \"Emacs Rules\" one time too many."
```

You can embed newlines in strings, like so:

```
"Oh Argentina!Your little tin of pink meatSoars o'er the Pampas"
```

**Characters**
:
- ?x is the syntax for an ASCII character:  ? followed by the character.
- e.g.:  ?a is ascii 97 ('a'), ? (that is, question-mark space) is ascii 32 (' ').
- Some need to be escaped, such as ?\(, ?\) and ?\\
- Emacs 22+ has unicode support.  Out of scope for this primer.

Characters are just int values internally, so you can use arithmetic operations on them (for instance, to iterate through ?a to ?z).
**Numbers**
:
- Integers are 29 bits of precision (not the usual 32).  `-32, 0, 157`, etc.
- Binary:  start with #b, e.g. `#b10010110`
- Octal:  #o[0-7]+,  e.g. `#o377`
- Hexadecimal:  start with #x, e.g. `#xabcd, #xDEADBEE`
- Floating-point:  the usual.  `-10.005, 0.0, 3.14159265`  (64 bits of precision.)
- Scientific:  the usual.  `6.02e23`, `5e-10`

The variables
and
are the largest and smallest integers representable in Emacs Lisp without bignum support.  Emacs 22+ comes with a fancy bignum/math library called
, if you need it.  Arithmetic operations overflow and underflow the way you'd expect (in, say, C or Java.)
**Booleans**
The symbol
(just a letter 't' by itself) is
.
The symbol
is
(and also means
).
In Emacs Lisp,
is the only false value; everything else evalutes to
in a boolean context, including empty strings, zero, the symbol 'false, and empty vectors.  An empty list, '(), is the same thing as
.
**Arrays**
Elisp has fixed-sized arrays called "vectors".  You can use square-brackets to create a pre-initialized literal vector, for instance:

```
[-2 0 2 4 6 8 10]["No" "Sir" "I" "am" "a" "real" "horse"]["hi" 22 120 89.6 2748 [3 "a"]]
```

Note that you do not (and cannot) use commas to separate the elements; use whitespace.
Vectors can have mixed-type elements, and can be nested.  You usually use the function
to create them, since literal vectors are singletons, which can be surprising.
**Lists**
Lisp makes heavy use of linked lists, so there's lexical syntax for them.  Anything in parentheses is a list, but unless you quote it, it will be evaluated as a function call.  There are various ways to quote things in Lisp:

```
(quote (1 2 3)) ; produces the list (1 2 3) with no list-element evaluation
```


```
'(1 2 3)  ; apostrophe is shorthand for (quote (...))          ; note that it goes _outside_ the left-paren
```


```
(list 1 (+ 1 1) 3) ; also produces (1 2 3), since it evaluates the elements first
```


```
`(1 ,(+ 1 1) 3)  ; another (1 2 3) via a template system called "backquote"
```

There's a lot more that could be said about lists, but other people have already said it.
**Pairs**
You can set the head and tail (also known as
and
) fields of a lisp link-list node struct (also known as a
cell) directly, using it as a 2-element untyped struct.  The syntax is
, and you have to quote it (see above).
A common lookup-table data-structure for very small data sets is an associative list (known as an
).  It's just a list of dotted pairs, like so:

```
'( (apple . "red")   (banana . "yellow")   (orange . "orange") )
```

Emacs Lisp has built-in hashtables, bit-vectors, and miscellaneous other data structures, but there's no syntax for them; you create them with function calls.

## Operators

Some operations that are typically operators in other languages are function calls in elisp.
**Equality**
Numeric equality:
Single-equal.  Yields
or
.  Works for floats too.
Not-numerically-equal:
I know, it looks like assign-divide-equal.  But it's not.
Value equality:
Like Java ==.  Works for ints, symbols, interned strings, and object references.  Use
for floating-point numbers (or just
).
Deep (structural) equality: use
, as in:

```
(equal '(1 2 (3 4)) (list 1 2 (list 3 (* 2 2))))  ; true
```

The equal function is like Java's
. Works for lists, vectors, strings, and just about anything else.
**String**
Strings don't have any operators, but there are lots of string functions.  Some common ones:

```
(concat "foo" "bar" "baz")  ; yields "foobarbaz"(string= "foo" "baz")  ; yields nil (false).  Can also use equal.(substring "foobar" 0 3) ; yields "foo"(upcase "foobar")  ; yields "FOOBAR"
```

Do
to see a list of functions related to strings.
**Arithmetic**
Easiest to show as a table...


| C/Java/JS Operator | Emacs Lisp | Example | Result |
| + | + | (+ 1 2 3 4 5) | 15 |
| - | - | (- 6 2 3) | 1 |
| * | * | (* 2 -1 4.2) | -8.4 |
| / | / | (/ 10 3) | 3 (use floats for float div) |
| % | % | (% 10 2) | 0 |
| << | lsh | (lsh 1 5) | 32 |
| >> | ash (negative amount) | (ash -32 -4) | -2 |
| >>> | lsh (negative amount) | (lsh 32 -4) | 2 |
| ++ | incf (requires 'cl library) | (incf x 6) | x+6 |
| -- | decf (ditto) | (decf x 5) | x-5 |
| ? : (ternary) | (if *test-expr then-expr else-expr*) | (if t 3 4) | 3 |
| && | and | (and t t t nil) | nil |
| || | or | (or nil nil nil t) | t |
| ! (logical-not) | not | (not 3) | nil |
| ~ (bit-not) | lognot | (lognot #b1001) | -10 |
| ^ (bit-xor) | logxor | (logxor 5 3) | 6 |
| & (bit-and) | logand | (logand 1 3) | 1 |
| | (bit-or) | logior | (logior 1 3) | 3 |
| < | < | (< 5 3) | nil |
| > | > | (> 5 3) | t |
| <= | <= | (<= 3 3) | t |
| >= | >= | (>= 5 3) | t |
| . (field access) | *see setf below* | n/a | n/a |
| [] (array access) | aref/aset | (aref [2 4 6] 1) | 4 |



## Statements

This section has some recipes for simple Java-like statements.  It's not comprehensive – just some recipes to get you going.
**if/else**
*Case 1:  no else clause*
:  (if
*test-expr*
*expr*
)
Example:

```
(if (>= 3 2)  (message "hello there"))
```

*Case 2:  else clause*
:  (if
*test-expr*
*then-expr*
*else-expr*
)

```
(if (today-is-friday)         ; test-expr    (message "yay, friday")   ; then-expr  (message "boo, other day")) ; else-expr
```

If you need multiple expressions (statements) in the
*then-expr*
, you wrap them with a call to
, which is like curly-braces in C or Java:

```
(if (zerop 0)    (progn      (do-something)      (do-something-else)      (etc-etc-etc)))
```

You don't need the
around the
*else-expr*
– everything after the
*then-expr*
is considered to be part of the
*else-expr*
.  Hence:

```
(if (today-is-friday)    (message "yay, friday")  (message "not friday!")  (non-friday-stuff)  (more-non-friday-stuff))
```

*Case 3:  else-if clause*
:  Just nest 'em.  Or use
(see below).

```
(if 'sunday    (message "sunday!")      ; then-expr  (if 'saturday              ; else-if      (message "saturday!")  ; next then-expr    (message ("weekday!")))) ; final else
```

*Case 4:  no else-if, multiple body expressions*
– use
:
If you don't have an
*else*
-clause, then you can use the
macro, which provides an implicit
:

```
(when (> 5 1)  (blah)  (blah-blah)  (blah blah blah))
```

You can also use
, which is like
but inverts the sense of the test:

```
(unless (weekend-p)  (message "another day at work")  (get-back-to-work))
```

**switch**
Elisp has two versions of the classic
statement:
and
.
Elisp does not have a table-lookup optimization for switch, so
and
are just syntax for nested if-then-else clauses.  However, if you have more than one level of nesting, it looks a lot nicer than
expressions.  The syntax is:

```
(cond  (test-1    do-stuff-1)  (test-2    do-stuff-2)  ...  (t    do-default-stuff))
```

The
parts can be any number of statements, and don't need to be wrapped with a
block.
Unlike classic
,
can handle any test expression (it just checks them in order), not just numbers.  The downside is that it doesn't have any special-casing for numbers, so you have to compare them to something.  Here's one that does string compares:

```
(cond ((equal value "foo")  ; case #1 – notice it's a function call to `equal' so it's in parens  (message "got foo")  ; action 1  (+ 2 2))             ; return value for case 1 ((equal value "bar")  ; case #2 – also a function call (to `+')  nil)                 ; return value for case 2 (t                    ; default case – not a function call, just literal true  'hello))             ; return symbol 'hello
```

The final
default clause is optional.  The first matching clause is executed, and the result of the entire
expression is the result of the last expression in the matching clause.
The 'cl (Common Lisp) package bundled with Emacs provides
, which works if you're comparing numbers or symbols, so in a sense it works more like standard
.  Example:

```
(case 12  (5 "five")  (1 "one")  (12 "twelve")  (otherwise   "I only know five, one and twelve."))  ; result:  "twelve"
```

With
you can use either
or
for the default case, but it must come last.
It's cleaner to use
when you can get away with it, but
is more general.
**while**
Elisp has a relatively normal
function:  (while
*test*
*body-forms*
)
Example, which you can evaluate in your
buffer:

```
(setq x 10      total 0)(while (plusp x)  ; while x is positive  (incf total x)  ; add x to total  (decf x))       ; subtract 1 from x
```

First we set two global variables,
and
, then run the loop.  Then we can evaluate the expression
to see that its value is 55 (the sum of the numbers 1 to 10).
**break/continue**
Lisp has a facility for upward control-flow transfers called
.  It's very similar to Java or C++ exception handling, albeit possibly somewhat lighter-weight.
To do a
from inside a loop in elisp, you put a
outside the loop, and a
wherever you want to break inside the loop, like so:


| Emacs Lisp | Java |
| (setq x 0 total 0)
(catch 'break
  (while t
    (incf total x)
    (if (> (incf x) 10)
        (throw 'break total)))) | var x = total = 0;
while (true) {
  total += x;
  if (x++ > 10) {
    break;
  }
} |


The symbol
is arbitrary, but is probably a nice choice for your readers.  If you have nested loops, you might consider
and
in your
expressions.
You can
if you don't care about the "return value" for the
-loop.
To
a loop, put a
expression just inside the loop, at the top.  For instance, to sum the numbers from 1 to 99 that are not evenly divisible by 5 (artificially lame example demonstrating use of
):


| Emacs Lisp | Java |
| (setq x 0 total 0)
(while (< x 100)
  (catch 'continue
    (incf x)
    (if (zerop (% x 5))
        (throw 'continue nil))
    (incf total x))) | var x = total = 0;
while (x < 100) {
  x++;
  if (x % 5 == 0) {
    continue;
  }
  total += x;
} |


We can combine these examples to show using a break and continue in the same loop:


| Emacs Lisp | JavaScript |
| (setq x 0 total 0)
(catch 'break
  (while t
    (catch 'continue
      (incf x)
      (if (>= x 100)
          (throw 'break nil))
      (if (zerop (% x 5))
          (throw 'continue nil))
      (incf total x)))) | var x = total = 0;
while (true) {
  x++;
  if (x >= 100) {
    break;
  }
  if (x % 5 == 0) {
    continue;
  }
  total += x;
} |


All the loops above compute the value 4000 in the variable
.  There are better ways to compute this result, but I needed something simple to illustrate
and
.
The
mechanism can be used across function boundaries, just like exceptions.  It's not intended for true exceptions or error conditions – Emacs has another mechanism for that, discussed in the
section below.  You should get comfortable using
for normal jumps and control transfer in your Elisp code.
**do/while**
Pretty much all iteration in Emacs Lisp is easiest using the
macro from the Common Lisp package.  Just do this to enable
:

```
(require 'cl)  ; get lots of Common Lisp goodies
```

The
macro is a powerful minilanguage with lots of features, and it's worth reading up on.  I'll use it in this primer to show you how to do basic looping constructs from other languages.
You can do a
like so:

```
(loop do      (setq x (1+ x))      while      (< x 10))
```

You can have any number of lisp expressions between the
and
keywords.
**for**
The C-style
-loop has four components:  variable initialization, the loop body, the test, and the increment.  You can do all that and more with the
macro.  For instance, this arbitrary JavaScript:

```
// JavaScriptvar result = [];for (var i = 10, j = 0; j <= 10; i--, j += 2) {  result.push(i+j);}
```

Could be done with
like so:

```
(loop with result = '()         ; one-time initialization      for i downfrom 10         ; count i down from 10      for j from 0 by 2         ; count j up from 0 by 2      while (< j 10)            ; stop when j >= 10      do      (push (+ i j) result)     ; fast-accumulate i+j      finally      return (nreverse result)) ; reverse and return result
```

It's a bit more verbose, but
has a
*lot*
of options, so you want it to be reasonably transparent.
Notice that this
declares the result array and then "returns" it.  It could also operate on a variable declared outside the loop, in which case we wouldn't need the
clause.
The
macro is astoundingly flexible.  Its full specification is
*way*
out of scope for this primer, but if you want to make Emacs Lisp your, uh, friend, then you should spend some time reading up on
.
**for..in**
If you're iterating over a collection, Java provides the "smart" for-loop, and JavaScript has
and
.  There are various ways to do it in Lisp, but you really might as well just learn how to do it with the
macro.  It's a one-stop shop for iteration.
The basic approach is to use
, and then do something with the individual results.  You can, for instance, collect them (or a function on them) into a result list like so:

```
(loop for i in '(1 2 3 4 5 6)      collect (* i i))           ; yields (1 4 9 16 25 36)
```

The
macro lets you iterate over list elements, list cells, vectors, hash-keys, hash-values, buffers, windows, frames, symbols, and just about anything else you could want to traverse.  See the Info pages or your Emacs manual for details.
**functions**
You
**de**
fine a
**fun**
ction with
.
Syntax:  (defun
*function-name*
*arg-list*
[
*optional docstring*
]
*body*
)

```
(defun square (x)  "Return X squared."  (* x x))
```

For a no-arg function, you use an empty list:

```
(defun hello ()  "Print the string `hello' to the minibuffer."  (message "hello!"))
```

The
*body*
can be any number of expressions.  The return value of the function is the result of the last expression executed.  You do not declare the return type, so it's useful to mention it in the documentation string.  The doc string is available from
after you evaluate your function.
Emacs Lisp does not have function/method overloading, but it supports optional and "rest" parameters similar to what Python and Ruby offer.  You can use the full Common Lisp specification for argument lists, including support for keyword arguments (see the
section below), if you use the
macro instead of
.  The
version also lets you
without having to set up your own
.
If you want your function to be available as a
command, put
as the first expression in the body after the doc string.
**local variables**
You declare function local variables with the
form.  The basic syntax is

```
(let ((name1 value1)      (name2 value2)      name3      name4      (name5 value5)      name6      ...))
```

Each
is either a single name, or
*(name initial-value)*
.  You can mix initialized and uninitialized values in any order.  Uninitialized variables get the initial value
.
You can have multiple
clauses in a function.  Code written for performance often collects all declarations into a single
at the top, since it's a bit faster that way.  Typically you should write your code for clarity first.
**reference parameters**
C++ has reference parameters, which allow you to modify variables from the caller's stack.  Java does not, so you have to work around it occasionally by passing in a 1-element array, or using an instance variable, or whatever.
Emacs Lisp does not have true reference parameters, but it has dynamic scope, which means you can modify values on your caller's stack anyway.  Consider the following pair of functions:

```
(defun foo ()  (let ((x 6))  ; define a local (i.e., stack) variable x initialized to 6    (bar)       ; call bar    x))         ; return x(defun bar ()  (setq x 7))   ; finds and modifies x in the caller's stack frame
```

If you invoke
the return value is 7.
Dynamic scoping is generally considered a bad design bordering on evil, but it can occasionally come in handy.  If nothing else, it's good to know it's what Emacs does.
**return**
A lisp function by default returns the value of the last expression executed in the function.  Sometimes it's possible to structure your function so that every possible return value is in a "tail position" (meaning the last expression out before the door closes, so to speak.)  For instance:


| Emacs Lisp | JavaScript |
| (require 'calendar)

(defun day-name ()
  (let ((date (calendar-day-of-week
               (calendar-current-date))))
    (if (= date 0)
        "Sunday"
      (if (= date 6)
          "Saturday"
        "weekday")))) | function dayName() {
  var date = new Date().getDay();
  switch (date) {
    case 0:
      return "Sunday";
    case 6:
      return "Saturday";
    default:
      return "weekday";
  }
} |


The return value is just the result of the last expression, so whatever our nested
produces is automatically returned, and there's no need here for an explicit
form.
However, sometimes restructuring the function this way is inconvenient, and you'd prefer to do an "early return".
You can do early returns in Emacs Lisp the same way you do
and
, using the
facility.  Usually simple functions can be structured so you don't need this – it's most often useful for larger, deeply-nested functions.  So for a contrived example, we'll just rewrite the function above to be closer to the JavaScript version:

```
(defun day-name ()  (let ((date (calendar-day-of-week               (calendar-current-date))))  ; 0-6    (catch 'return      (case date        (0         (throw 'return "Sunday"))        (6         (throw 'return "Saturday"))        (t         (throw 'return "weekday"))))))
```

Obviously using
here is slow and clunky compared to the alternatives, but sometimes it's exactly what you need to get out of a deeply nested construct.
**try/catch**
We've already discussed
, an exception-like facility for normal control flow transfers.
Emacs has a different facility for real error conditions, called the "conditions" system.  Going through the full system is out of scope for our primer, but I'll cover how to catch all exceptions and how to ignore (squelch) them.
Here's an example of a universal try/catch using the
construct, with a Java equivalent:


| Emacs Lisp | Java |
| (condition-case nil
    (progn
      (do-something)
      (do-something-else))
  (error
   (message "oh no!")
   (do-recovery-stuff))) | try {
  doSomething();
  doSomethingElse();
} catch (Throwable t) {
  print("uh-oh");
  doRecoveryStuff();
} |


If you want an empty catch block (just squelch the error), you can use
:

```
(ignore-errors  (do-something)  (do-something-else))
```

It's sometimes a good idea to slap an
around bits of elisp code in your startup file that may not always work, so you can still at least start your Emacs up if the code is failing.
The
means "Don't assign the error to a named variable."  Elisp lets you catch different kinds of errors and examine the error data.  You can read the Emacs manual or Info pages to learn more about how to do that.
The
is necessary if you have multiple expressions (in C/Java, statements) to evaluate in the
body.
will not catch values thrown by
– the two systems are independent.
**try/finally**
Emacs has a "finally"-like facility called
.


| Emacs Lisp | Java |
| (unwind-protect
    (progn
      (do-something)
      (do-something-else))
  (first-finally-expr)
  (second-finally-expr)) | try {
  doSomething();
  doSomethingElse();
} finally {
  firstFinallyExpr();
  secondFinallyExpr();
} |


Like
,
takes a single
*body-form*
followed by one or more cleanup forms, so you need to use
if you have more than one expression in the body.
**try/catch/finally**
If you make the
(which is basically
) the body-form of an
(which is basically
), you get the effect of
:

```
(unwind-protect                 ; finally    (condition-case nil         ; try        (progn                  ; {          (do-something)        ;   body-1          (do-something-else))  ;   body-2 }      (error                    ; catch       (message "oh no!")       ; { catch 1       (poop-pants)))           ;   catch 2 }  (first-finally-expr)          ; { finally 1  (second-finally-expr))        ;   finally 2 }
```


## Classes

Emacs Lisp is not object-oriented in the standard sense:  it doesn't have classes, inheritance, polymorphism and so on.  The Common Lisp package includes a useful feature called
that gives you some simple OOP-like support.  I'll walk through a basic example.
These two declarations are essentially equivalent:


| Emacs Lisp | Java |
| (require 'cl)  ; top of file  

(defstruct person
  "A person structure."
  name
  (age 0)
  (height 0.0)) | /* A Person class */
class Person {
  String name;
  int age;
  double height;
  public Person() {}
  public Person(String name) {
    this(name, 0, 0);
  }
  public Person(int age) {
    this(null, age, 0);
  }
  public Person(double height) {
    this(null, 0, height);
  }
  public Person(String name, int age) {
    this(name, age, 0);
  }
  public Person(String name, double height) {
    this(name, 0, height);
  }
  public Person(int age, double height) {
    this(null, age, height);
  }
  public Person(String name, int age, double height) {
    this.name = name;
    this.age = age;
    this.height = height;
  }
} |


Both create a "class" with three named fields, and constructors for initializing any subset of the fields.  With
you get one constructor with keyword parameters, so these are all valid:

```
(make-person)  ; new Person()(make-person :age 39)  ; new Person(39)(make-person :name "Steve" :height 5.83 :age 39)  ; new Person("Steve", 39, 5.83)
```

The
macro supports single-inheritance (to arbitrary depth):


| Emacs Lisp | Java |
| (defstruct (employee
            (:include person))
  "An employee structure."
  company
  (level 1)
  (title "n00b")) | /* An Employee class */
class Employee extends Person {
  String company;
  int level = 1;
  String title = "n00b";
  public Employee() {
  }
  public Employee(String name,
                  String company) {
    super(name);
    this.company = company;
  }
  public Employee(String name,
                  int age,
                  String company) {
    super(name, age);
    this.company = company;
  }
  public Employee(String name,
                  int age,
                  double height,
                  String company) {
    super(name, age, height);
    this.company = company;
  }
  public Employee(String name,
                  int age,
                  String company,
                  int level) {
    super(name, age);
    this.company = company;
    this.level = level;
  }
  public Employee(String name,
                  int age,
                  String co,
                  int lvl,
                  String title) {
    super(name, age);
    this.company = co;
    this.level = lvl;
    this.title = title;
  }
  // (remaining 150 overloaded constructors elided for brevity)
} |


The
macro provides a flexible default constructor, but also gives you a fair amount of control over your constructor(s) if you prefer.
The
macro creates an
-like predicate function named after the struct, so you can say:

```
(person-p (make-person))t(employee-p (make-person))nil(employee-p (make-employee))t(person-p (make-employee))  ; yes, it inherits from persont
```

Java may suck at declaring constructors, but Emacs Lisp makes up for it by sucking at setting fields.  To set a field in a struct, you have to use the
function, and construct the field name by prepending the structure name.  So:


| Emacs Lisp | Java |
| (setq e (make-employee))
(setf (employee-name e) "Steve"
      (employee-age e) 39
      (employee-company e) "Google"
      (employee-title e) "Janitor") | Employee e = new Employee();
e.name = "Steve";
e.age = 39;
e.company = "Google";
e.title = "Janitor"; |


The Lisp one doesn't look too bad here, but in practice (because Elisp has no namespace support and no
macro), you wind up with long structure and field names.  So your
-enabled elisp code tends to look more like this:

```
(setf (js2-compiler-data-current-script-or-function compiler-data) current-script      (js2-compiler-data-line-number compiler-data) current-line      (js2-compiler-data-allow-member-expr-as-function-name compiler-data) allow      (js2-compiler-data-language-version compiler-data) language-version)
```

So it goes.
To fetch the value of a field in a struct variable, you concatenate the struct name with the field name and use it as a function call:

```
(person-name steve)  ; yields "Steve"
```

There's more that
can do – it's a pretty decent facility, all things considered, though it falls well short of a full object system.
**Buffers as classes**
In Elisp programming it can often be useful to think of buffers as instances of your own classes.  This is because Emacs supports the notion of buffer-local variables:  variables that automatically become buffer-local whenever they are set in any fashion.  They become part of the scope chain for any code executing in the buffer, so they act a lot like encapsulated instance variables.
You can use the function
to declare a variable as buffer-local.  Usually it comes right after the
or
declaration (see below.)

## Variables

You can declare a variable, optionally giving it some runtime documentation, with
or
:

```
(defconst pi 3.14159 "A gross approximation of pi.")
```

The syntax is
.
Ironically,
is variable and
is constant, at least if you re-evaluate them.  To change the value of a
variable by re-evaluating its declaration you need to use
to unbind it first.  You can always change the value of any
or
variable using
.  The only difference between the two is that
makes it clearer to the programmer that the value is not intended to change.
You can use
to create brand-new variables, but if you use
, the byte-compiler will be able to catch more typos.

## Further reading

Emacs Lisp is a real programming language.  It has a compiler, a debugger, a profiler, pretty-printers, runtime documentation, libraries, I/O, networking, process control and much more.  There's a lot to learn, but I'm hoping this little primer has got you over the hump, as it were.
In spite of its various quirks and annoyances, Elisp is reasonably fun to program in once you get the hang of it.  As a language it's not that great, and everyone wishes it were Common Lisp or Scheme or some other reasonable Lisp dialect.  Some people even wish it weren't Lisp at all, if you can believe that!  (hee)
But it's really, really useful to be able to customize your editor, and also to be able to fix problems with elisp code you borrowed or inherited.  So a little Elisp goes a long way.
For those of you learning Emacs Lisp, please let me know if you found this useful.  If you try writing some Emacs extensions, let me know what you would like to see documented next; I can always do another installment of the Emergency Elisp series if there's enough interest.
Good luck!