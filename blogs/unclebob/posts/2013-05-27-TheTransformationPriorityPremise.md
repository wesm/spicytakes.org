---
title: "The Transformation Priority Premise"
date: 2013-05-27
url: https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html
slug: TheTransformationPriorityPremise
word_count: 4394
---

This blog poses a rather radical premise. It suggests that Refactorings have counterparts called  *Transformations* . Refactorings are simple operations that change the structure of code without changing it’s behavior.  *Transformations*  are simple operations that change the behavior of code. Transformations can be used as the sole means for passing the currently failing test in the  `red/green/refactor`  cycle.  *Transformations*  have a priority, or a preferred ordering, which if maintained, by the ordering of the tests, will prevent impasses, or long outages in the  `red/green/refactor`  cycle.

> **“As the tests get more specific, the code gets more generic.”**

Recently this mantra has taken on a new meaning for me.

I invented it as rule to prevent my TDD students from acquiring the nasty habit of writing production code that mirrored the tests:

```
@Test
public void primeFactorsOfFour() {
  assertEquals(asList(),    PrimeFactors.of(1));
  assertEquals(asList(2),   PrimeFactors.of(2));
  assertEquals(asList(3),   PrimeFactors.of(3));
  assertEquals(asList(2,2), PrimeFactors.of(4));
  ...
}

public class PrimeFactors {
  public static of(int n) {
    if (n == 1)
      return asList();
    else if (n == 2)
      return asList(2);
    else if (n == 3)
      return asList(3);
    else if (n == 4)
      return asList(2,2);
    ...
```

Newcomers to TDD often question why TDD does not lead this kind of code. I answer with the above rule. This explanation usually satisfies the students, especially when I demonstrate the idea with the  [Prime Factors Kata](http://butunclebob.com/ArticleS.UncleBob.ThePrimeFactorsKata) .

## Prime Factors

I invented that Kata ten years ago when my son, Justin, came home from school with homework. He had to calculate the prime factors of several integers. I told him to do his homework, and that I would write a program that allowed him to check his work. (He’d have to enter his answer, and the program would simply tell him whether he was right or wrong).

I sat at my kitchen table and, using this new discipline named  *TDD* , I wrote the algorithm in Ruby. It was one of those eye-opening events for me. As I went from test to test the algorithm assembled itself in a completely unexpected way. I was astounded that I could make the 3 case pass by changing just one character in the code from a ‘2’ to an ‘n’. I was thrilled when the 8 case was solved by changing the word ‘if’ to the word ‘while’. I could  *feel*  that there was something profound about that, but I couldn’t put my finger on exactly what it was. But now I think I know.

## Brainlessness

Over the years I have written lots and lots of tests. What’s more I’ve executed the various Kata many hundreds of times. From time to time I make subtle improvements in a kata. I refine the tests or the code to make them smoother, simpler, and more elegant. With all that repetition and refinement I’ve begun to notice something. It has to do with another complaint that people have about TDD:  *the brainlessness* .

Consider how the  [Bowling Game Kata](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata)  begins with the test for the gutter game:

```
@Test
public void gutterGame() {
  for (int i=0; i<20; i++)
    game.roll(0);
  assertEquals(0, game.score());
}
```

When we teach TDD was ask:  *“How should we make that pass?”*  Newbies are often confused by the question because they are expecting that they have to write the bowling algorithm. But we surprise them by making it pass this way:

```
public int score() {
  return 0;
}
```

At this point the programmers in the class roll their eyes and groan. They clearly think this is dumb and are frustrated that I would be telling them to write code that is clearly  *wrong* .

I used to go along with the gag. I used to agree with them that this was brainless, and that we were just deferring decisions until we have more information. I told them that it was also a good way to test the tests, since by returning zero we can clearly see that the test is passing and that therefore the test is correct.

## A Sequence of Transformations.

What I have begun to discover is that returning zero  *is not nearly so brainless as it looks* . Not when you put it in the appropriate context.

When we use TDD, our production code goes through a sequence of transformations. I used to think it was a transformation from stupid to intelligent. But I’ve begun to see that this is not the case at all. Rather, the code goes through a sequence of transformation  *from specific to generic* .

Returning zero from the  `score`  function is a specific case. But the case is in the correct form. It is an integer, and it has the right value. Therefore the  *shape*  of the algorithm is correct, it’s just hasn’t been generalized yet.

The next test in the bowling game is:

```
@Test
public void allOnes() {
  for (int i=0; i<20; i++)
    game.roll(1);
  assertEquals(20, game.score());
}
```

We make this pass by adding up all the pins in the  `roll`  function and storing the sum in a variable named  `score` . Then we change the  `score`  function to return that value:

```
public int score() {
  return score;
}
```

Notice that we have transformed the constant  `0`  into the variable  `score` . The algorithm has the same shape as before, (i.e. it returns an  `int` ) but it now has a more generic implementation. Why is this a more generic implementation? Because  *a variable is a generalization of a constant* .

In other words, the transformation that has taken place is a simple alteration of some part of the solution from a more specific form, to a more generic form!

I used to think that this was merely interesting. I was titillated by the fact  *sometimes*  you could perform these simple transformations from specific to generic. Lately I’ve begun to suspect that it is a  *rule* , that  *every*  change to the code is either a behavior changing transformation from specific to generic, or a refactoring. Indeed, I think this rule may provide some guidance in choosing the next test to write, and in the manner in which the production code should be implemented in order to pass that test.

But let’s not get ahead of ourselves. What about the next test in the Bowling Game?

```
@Test
public void oneSpare() {
  game.roll(5);
  game.roll(5); // spare
  game.roll(3);
  rollMany(20,0);
  assertEquals(16, g.score());
}
```

This test forces us to abandon the simple implementation of  `score`  for a much more complex one. The instance variable  `score`  which was updated in the  `roll`  function is removed and the  `score`  function computes the score from an array of rolls.

Once again we have transformed a specific implementation (an instance variable that holds a pre-computed score) to a more general form (a loop that computes the score from an array).

Another common transformation can be seen in the prime factors kata where, in order to get the  `2`  case to pass, we insert an  `if`  statement into the implementation. The code transforms from

```
List factors = new ArrayList();
return factors;
```

to

```
List factors = new ArrayList();
if (n>1)
  factors.add(2);
return factors;
```

In this case we are making the code more general by conditionally splitting the execution into two paths. One path makes all the old tests pass, and the new path makes the new test pass.

The prime factors kata is interesting because that transformation happens again in the  `4`  case where an if statement is added to handle the case where the input variable is divisible by 2;

```
List factors = new ArrayList();
if (n>1) {
  if (n%2 == 0) {
    factors.add(2);
    n %= 2;
  }
  if (n>1)
    factors.add(n);
}
return factors;
```

The new pathway handles the the  `4`  case by detecting that 4 is divisible by 2, adding 2 to  `factors` , and adjusting  `n`  so that the paths can rejoin.

More interesting still is that at the  `8`  case, the inner  `if`  statement is transformed into a  `while`  statement. And then for the  `9`  case the outer  `if`  is transformed into a  `while` . Clearly  `while`  is a general form of  `if` .

## The Transformations

So what are these transformations? Perhaps we can make a list of them:

* **({}–>nil)**  no code at all->code that employs nil
* **(nil->constant)**
* **(constant->constant+)**  a simple constant to a more complex constant
* **(constant->scalar)**  replacing a constant with a variable or an argument
* **(statement->statements)**  adding more unconditional statements.
* **(unconditional->if)**  splitting the execution path
* **(scalar->array)**
* **(array->container)**
* **(statement->recursion)**
* **(if->while)**
* **(expression->function)**  replacing an expression with a function or algorithm
* **(variable->assignment)**  replacing the value of a variable.

There are likely others.

Perhaps you noticed the resemblance that these transformations have to refactorings. However refactorings are used to transform the  *structure*  of code without altering its behavior. These transformations are used in order to change the  *behavior*  of code. In particular, we use these transformations to make failing tests pass.

It should be clear that each of the transformations has a direction. They all transform the behavior of the code from something specific to something more generic. In some cases it is a constant being transformed into a variable, or a variable being transformed into an array. In others it is an  `if`  statement being transformed into a  `while`  loop, or a simple sequence getting transformed into recursion.

It should also be clear that I have  *roughly*  ordered the transformations by their complexity. That is, the transformations at the top of the list are simpler, and less risky, than the transformations that are lower in the list.

## The Priority Premise

So the thing that has piqued my interest lately is the idea that transformations on the top of the list should be preferred to those that are lower. It is better (or simpler) to change a constant into a variable than it is to add an  `if`  statement. So when making a test pass, you try to do so with transformations that are simpler (higher on the list) than those that are more complex.

What’s more, when you pose a test, you try to pose one that allows simpler transformations rather than complex transformations; since the more complexity required by the test the larger the risk you take to get that test to pass.

### The Impasse Problem

It was the  [word wrap kata](http://thecleancoder.blogspot.com/2010/10/craftsman-62-dark-path.html)  that got me thinking about this. The kata starts out simply, but you quickly face a dilemma. There is one sequence of tests and implementation choices that forces you into an impasse, where there is no way to get the next text to pass without rewriting the whole algorithm. A different sequence of tests allows the algorithm to come together in the stepwise fashion that TDDers prefer. How can you choose the right sequence?

This is a relatively common problem faced by TDDers. We pose a test only to find that we don’t know how to solve it without changing a large amount of code. The more code we change, the longer it will be before we get back to green; and the  `red/green/refactor`  cycle breaks down.

My premise is that if you choose the tests and implementations that employ transformations that are higher on the list, you will avoid the impasse.

### Case Study: Word Wrap.

So let’s walk through the reasoning. First we’ll execute the word wrap kata and choose the path that leads to the impasse. Then we’ll do it again, but take the path that does not. In each case we’ll show the transformations.

The first test in the word wrap kata is pretty obviously the degenerate case. Note that this employs the very first transformation  **({}–>nil)** :

```
@Test
public void WrapNullReturnsEmptyString() throws Exception {
  assertThat(wrap(null, 10), is(""));
}
```

As we write this test, we also write the  *failing*  implementation which also employs  **({}–>nil)**

```
public static String wrap(String s, int length) {
  return null;
}
```

We can make it pass with  **(nil->constant)**

```
public static String wrap(String s, int length) {
  return "";
}
```

The next test is the empty string case. Notice that this is just  **(nil->constant)**  applied to the first test. This test passes without any modification to the implementation. I always take that as an indication that things are going well.

```
@Test
public void WrapEmptyStringReturnsEmptyString() throws Exception {
  assertThat(wrap("", 10), is(""));
}
```

The next test employs  **(constant->constant+)**

```
@Test
public void OneShortWordDoesNotWrap() throws Exception {
  assertThat(wrap("word", 5), is("word"));
}
```

Making this test pass forces us to use  **(unconditional->if)**  as well as  **(constant->scalar)**

```
public static String wrap(String s, int length) {
  if (s == null)
    return "";
  return s;
}
```

### The Impasse

At this point, if we were paying heed to the priority premise, we might wonder whether this was a wise step. After all,  **(unconditional->if)**  is pretty far down the list. But in this case I’m going to ignore the priority premise so that I can show you the impasse.

The next test once again employs  **(constant->constant+)**

```
@Test
public void TwoWordsLongerThanLimitShouldWrap() throws Exception {
  assertThat(wrap("word word", 6), is("word\nword"));
}
```

We can make this pass by using  **(expression->function)** .

```
public static String wrap(String s, int length) {
  if (s == null)
    return "";
  return s.replaceAll(" ", "\n");
}
```

This is one of those moves that feels  *clever* . We justify it by saying that we are doing the simplest thing that would work. But given the priority premise, this is no longer all that simple. The  **(expression->function)**  transformation is down at the bottom of the list.

The next test continues to employ  **(constant->constant+)**

```
@Test
public void ThreeWordsJustOverTheLimitShouldWrapAtSecondWord() throws Exception {
  assertThat(wrap("word word word", 9), is("word word\nword"));
}
```

But how do we make this pass? The current solution does not appear to be easily transformable into something that will pass the new test. If we had a function like  `replaceLast(" ", "\n")`  then perhaps it would be simple; but that wouldn’t help us for the next test case  `"word word word word"` .

This is the impasse. Now this is a simple problem, and it’s not really that difficult to find a solution. But that’s not the point. The current situation forces us to take a step that’s larger than we like. We’ve put ourselves in the position where we must now solve a large part of the problem rather than a small incremental part of the problem. We have to take a step that’s uncomfortably large.

### Breaking the Impasse

So not let’s go back to the point where we first ignored the priority premise. We had just posed the following test:

```
@Test
public void OneShortWordDoesNotWrap() throws Exception {
  assertThat(wrap("word", 5), is("word"));
}
```

There is nothing unusual about this test that would make us think it’s out of order. There is no obviously better test to pose. However, the implementation forces us to use the  **(unconditional->if)**  transformation, which has a pretty low priority.

```
public static String wrap(String s, int length) {
  if (s == null)
    return "";
  return s;
}
```

So now we should ask ourselves whether there is another test we could pose that could be passed with a higher priority transformation. At the moment the implementation is simply  `return "";`  so are there any other inputs that should return an empty string?

A column length that’s less than one is kind of nonsensical. We could return an empty string for that, or we could throw an exception. I think the exception is probably more appropriate; but the tests for that would also require the  **(unconditional->if)**  transformation. Still, it’s probably a good idea to to get all the invalid input cases done first.

```
@Test(expected = WordWrapper.InvalidArgument.class)
public void LengthLessThanOneShouldThrowInvalidArgument() throws Exception {
  wrap("xxx", 0);
}
```

Which is passed with:

```
public static String wrap(String s, int length) {
  if (length < 1)
    throw new InvalidArgument();
  return "";
}
```

But that just leaves us where we were before. So I guess there’s no better test to write:

```
@Test
public void OneShortWordDoesNotWrap() throws Exception {
  assertThat(wrap("word", 5), is("word"));
}
```

And after a  **(unconditionsl->if)**  and a  **(constant->scalar)**  the implementation is:

```
public static String wrap(String s, int length) {
  if (length < 1)
    throw new InvalidArgument();
  if (s == null)
    return "";

  return s;
}
```

So now we pose the  `word word`  test again. As before this is just a  **(constant->constant+)**  transformation.

```
@Test
public void TwoWordsLongerThanLimitShouldWrap() throws Exception {
  assertThat(wrap("word word", 6), is("word\nword"));
}
```

The last time we saw this test we passed it with a  **(expression->function)** . Can it be solved with a higher priority transformation? I don’t think so. Every solution I can think of involves some kind of algorithm.

Is there a different test we could pose that could be solved with a higher priority transformation? Yes, there is! So let’s  `@Ignore`  the current test and write one that uses a simpler transformation.

```
@Test
public void WordLongerThanLengthBreaksAtLength() throws Exception {
  assertThat(wrap("longword", 4), is("long\nword"));
}
```

This test can be passed with a  **(unconditional->if)** .

```
public static String wrap(String s, int length) {
  if (length < 1)
    throw new InvalidArgument();
  if (s == null)
    return "";

  if (s.length() <= length)
    return s;
  else {
    return "long\nword";
  }
}
```

This might look like a cheat; but it’s not. We have split the execution pathways, and the new pathway can be viewed as starting completely empty, and then transformed by  **({}–>null)**  and  **(null->constant)** . We could have written those transformations and seen them fail; but why bother?

The next test is completely obvious. We’ve got to get rid of that constant. We can do that by adding a new statement to the existing test with the  **(statement->statements)**  transformation.

```
@Test
public void WordLongerThanLengthBreaksAtLength() throws Exception {
  assertThat(wrap("longword", 4), is("long\nword"));
  assertThat(wrap("longerword", 6), is("longer\nword"));
}
```

That’s going to require a  **(expression->function)**  to pass. There’s no simpler transformation, and no simpler test.

```
else {
    return s.substring(0, length) + "\n" + s.substring(length);
  }
```

The next test is the plural of the last:

```
@Test
public void WordLongerThanTwiceLengthShouldBreakTwice() throws Exception {
  assertThat(wrap("verylongword", 4), is("very\nlong\nword"));
}
```

We can pass that with  **(statement->recursion)**

```
return s.substring(0, length) + "\n" + wrap (s.substring(length), length);
```

It is also possible to pass this test with  **(if->while)** . Indeed, you might question why I put  **(statement->recursion)**  above  **(if->while)** . So a bit later in this paper we’ll explore the iterative solution. Comparing the two may convince you that recursion is, in fact, simpler than iteration.

So now let’s go back to that  `@Ignored`  test and turn it back on. How would we pass it now?

```
if (s.length() <= length)
    return s;
  else {
    int space = s.indexOf(" ");
    if (space >= 0)
      return "word\nword";
    else
      return s.substring(0, length) + "\n" + wrap(s.substring(length), length);
  }
```

**(unconditional->if)**  followed by a  **(nil->constant)**  does the trick. What’s more there is no simpler test to pass, nor a simpler transformation to use.

Getting rid of the constant requires an additional test:

```
@Test
public void TwoWordsLongerThanLimitShouldWrap() throws Exception {
  assertThat(wrap("word word", 6), is("word\nword"));
  assertThat(wrap("wrap here", 6), is("wrap\nhere"));
}
```

Which is passed with  **(expression->function)** . Again, there is no simpler test or transformation. (For the sake of brevity, and to keep this paper from sounding like a broken record, I’m going to stop making that statement. You should assume it.)

```
int space = s.indexOf(" ");
    if (space >= 0)
      return s.substring(0, space) + "\n" + s.substring(space+1);
    else
      return s.substring(0, length) + "\n" + wrap(s.substring(length), length);
```

We can see that the new clause needs  **(statement->recursion)** . So we write a test that forces the issue:

```
@Test
public void ThreeWordsEachLongerThanLimitShouldWrap() throws Exception {
  assertThat(wrap("word word word", 6), is("word\nword\nword"));
}
```

Making it pass is simple.

```
if (space >= 0)
      return s.substring(0, space) + "\n" + wrap(s.substring(space+1), length);
    else
      return s.substring(0, length) + "\n" + wrap(s.substring(length), length);
```

Now we can refactor to eliminate the duplication.

```
public class WordWrapper {
  private int length;

  public WordWrapper(int length) {
    this.length = length;
  }

  public static String wrap(String s, int length) {
    return new WordWrapper(length).wrap(s);
  }

  public String wrap(String s) {
    if (length < 1)
      throw new InvalidArgument();
    if (s == null)
      return "";

    if (s.length() <= length)
      return s;
    else {
      int space = s.indexOf(" ");
      if (space >= 0) 
        return breakBetween(s, space, space + 1);
      else
        return breakBetween(s, length, length);
    }
  }

  private String breakBetween(String s, int start, int end) {
    return s.substring(0, start) + 
      "\n" + 
      wrap(s.substring(end), length);
  }

  public static class InvalidArgument extends RuntimeException {
  }
}
```

The next test makes sure we break on the  *last*  space before the limit.

```
@Test
public void ThreeWordsJustOverTheLimitShouldBreakAtSecond() throws Exception {
  assertThat(wrap("word word word", 11), is("word word\nword"));
}
```

This requires a  **(expression->function)** , but it’s so simple it seems obvious.

```
int space = s.lastIndexOf(" ");
```

Though this passes the new test, it breaks the previous test; but we can do one more  **(expression->function)**  transformation to fix it.

```
int space = s.substring(0, length).lastIndexOf(" ");
```

Wherever limits are used, the law of trichotomy must be considered. All the lengths used in the tests have been unambiguously beyond the position of the breaking space. But what happens if we break right on the space.

```
@Test
public void TwoWordsTheFirstEndingAtTheLimit() throws Exception {
  assertThat(wrap("word word", 4), is("word\nword"));
}
```

This fails, but can be made to pass with a  **(statement->function)**  transformation.

```
int space = s.substring(0, length+1).lastIndexOf(" ");
```

This may not look like a  **(statement->function)** , but it is. Adding is a function. We might as well have said  `add(length, 1)` .

### Iteration instead of Recursion

Now let’s wind back the clock and see how an iterative, rather than a recursive, solution might evolve. Remember that we introduced  **(statement->recursion)**  while trying to pass the following test:

```
@Test
public void WordLongerThanTwiceLengthShouldBreakTwice() throws Exception {
  assertThat(wrap("verylongword", 4), is("very\nlong\nword"));
}
```

The failing code looks like this:

```
if (s.length() <= length)
    return s;
  else {
    return s.substring(0, length) + "\n" + s.substring(length);
  }
```

We can make this pass by using the  **(if->while)**  transformation. If we are going to use a  `while`  then we need to invert the condition of the  `if` . This is a simple refactoring,  *not a transformation* .

```
if (s.length() > length) {
    return s.substring(0, length) + "\n" + s.substring(length);
  } else {
    return s;
  }
```

Next we need to create a variable to hold the state of the iteration. Once again, this is a refactoring, not a transformation.

```
String result = "";
  if (s.length() > length) {
    result = s.substring(0, length) + "\n" + s.substring(length);
  } else {
    result = s;
  }
  return result;
}
```

`While`  loops can’t have  `else`  clauses, so we need to eliminate the  `else`  path by doing less in the  `if`  path. Again, this is a refactoring.

```
String result = "";
  if (s.length() > length) {
    result = s.substring(0, length) + "\n";
    s = s.substring(length);
  }
  result += s;
```

And now we can employ  **(if->while)**  to make the test pass.

```
String result = "";
  while (s.length() > length) {
    result += s.substring(0, length) + "\n";
    s = s.substring(length);
  }
  result += s;
```

## The Process

If we accept the Priority Premise, then we should amend the typical red-green-refactor process of TDD with the following provision:

> When passing a test, prefer higher priority transformations.
> When posing a test choose one that can be passed with higher priority transformations.
> When an implementation seems to require a low priority transformation, backtrack to see if there is a simpler test to pass.

## Issues

There are a number of problems with this.

* Are there other transformations? (almost certainly)
* Are these the right transformations? (probably not)
* Are there better names for the transformations? (almost certainly)
* Is there really a priority? (I think so, but it might be more complicated than a simple ordinal sequence)
* If so, what is the principle behind that priority? (some notion of “complexity”)
* Can it be quantified? (I have no idea)
* Is the priority order presented in this blog correct? (not likely)
* The transformations as described are informal at best. Can they be formalized? (That’s the holy grail!)

As you can see from my parenthetic remarks, I have quibbles with nearly all these questions. What I am certain of is that there is a fundamental principle lurking somewhere in here. I think that there  *are*  a fixed and simple set of transformations, even if I have not enumerated them well. I  *hope*  they can be formalized. I also think that there is some criteria for selecting which transformations to employ, even if it is not quite as simple as a priority list.

## Implications

If my suspicions turn out correct, then a number of things become possible.

* Tool support for transformations similar to the current tool support for refactorings.
* Tool support for  *suggesting*  transformations that follow priority order.
* The sequence of tests, transformations, and refactorings may just be a formal proof of correctness.

### Formal Proof of Correctness

That last point requires a bit more amplification. If you can describe the desired behavior of a program with a suite of tests, and if you can show step by step how each test is passed by using formal transformations and refactorings, then you have created a proof.

Oddly, the proof is attained by  *constructing*  the algorithm in a stepwise fashion. It is interesting to compare this to Dijkstra’s approach of proving correctness by taking the algorithm apart.

## Conclusion

Given the typical TDD  `red/green/refactor`  process, it appears that the  `green`  phase can be achieved by employing a fixed set of behavior changing transformations to the code. These changes move the code from a  *specific*  form to a more  *generic*  form. It also appears that these transformations have a preferred order based on complexity. This ordering can be used in both the  `red`  and  `green`  phases of TDD. During the  `green`  we prefer simpler transformations. During the  `red`  phase we prefer tests that can be passed with simpler transformations. It is the premise of this blog that if tests are chosen and implemented in this preferred order of transformations, then TDD impasses will be reduced or eliminated.
