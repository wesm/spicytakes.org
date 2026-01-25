---
title: "Introduction to Contract Programming"
date: 2017-11-27
url: https://www.hillelwayne.com/post/contracts/
slug: contracts
word_count: 2082
---

I’ve namedropped contracts enough here that I think it’s finally time to go talk about them. A lot of people conflate them with class interfaces / dynamic typing / “your unit tests are your contract”, which muddies the discussion and makes it hard to show their benefits. So I’d like to build up the idea of contracts from first principles. We’re going to work in Python, up until the point where things get crazy.


---


We’re playing a game. It’s like battleship on a 1D grid, aka “guess the number”.


```
import random

class Game:
  def __init__(self, target):
    self.bounds = (0, 10)
    self.target = target
    self.over = False
    self.guessed = set()

  def make_guess(self, guess):
    if guess == self.target:
      self.over = True
    else:
      self.guessed.add(guess)

def ai_guess(game):
  return random.randint(*game.bounds)

if __name__ == "__main__":
  game = Game(3)
  while not game.over:
    guess = ai_guess(game)
    print(guess)
    game.make_guess(guess)

```


This is a really simple AI: our industrious idiot bot will keep making random guesses until it finds the answer. This works, but when I ran it, I got a weird pattern of guesses:


```
9 1 1 9 9 3

```


We already know 9 isn’t the answer, so why are we guessing it two more times and why does the game allow us to do that? The Game shouldn’t let the AI guess that again. Otherwise we get all sorts of weird bugs, like allowing a player to skip their turn by repeating a guess or something. Ideally we want to enforce that in the code. But whose responsibility is it: the game to stop duplicate plays, or the AI to not make them in the first place? There are some good argument to place it in the game:

- It’s conceptually simpler and DRYer
- The AI doesn’t have to know about the game logic, so it’s easier on the clients
- We can test the AI functions independently of the Game logic


In my opinion, though, there are better arguments to place it on the AI:

- The AI needs to know about the game logic anyway. Otherwise, how can it have strategy?
- You might need to know if a move is valid before making it. For example, if your strategy is to minmax several possible moves, you don’t want to waste time studying a move that’s illegal in the first place.
- The AI now has to know what to do if it makes a move and the game tells it that move is invalid, which is harder on the clients.
- In a more complex system, you might have several layers of abstraction. If we have to revalidate the behavior at the game level, those layers aren’t doing their job.
- What if you have human players? Their GUI is going to grey out invalid moves anyway, so you’d have to duplicate the logic.


I think in this case we’re better off telling the AI not to do anything dumb. How do we guarantee that? The game is still going to have to check that it’s a valid move before trying it, just in case the AI has a bug. I could use an early return or a raised exception, but both of these are ‘ambiguous’. They imply that it’s *okay* to call `make_guess` with an invalid guess because the game will handle it properly. We want a way to tell clients that no, it’s absolutely Not Okay to make an invalid guess, and if you do we won’t let you play anymore.


In Python, the best way to do that is with an `assert` statement. My favorite definition of `assert` is “a conditional which, if false, *indicates a bug in your program.*” There should be absolutely no circumstances where `make_guess` is called with a bad guess, and if you do, the program stops. No exceptions.1


```
  def make_guess(self, guess):
    assert guess not in self.guessed
    if guess == self.target:
      self.over = True
    else:
      self.guessed.add(guess)

7 4 7 AssertionError

```


Our assertion here is a **precondition**: something that the caller must guarantee for the program as a whole to work. There’s a lot of preconditions we could add to our toy: you can’t guess if the game is over. The guess must be inside the bounds. The *target* must be inside the bounds. Similarly, we can add a **postcondition**: something that must be true when the method call ends. Here’s one example:


```
  def make_guess(self, guess):
    assert guess not in self.guessed
    if guess == self.target:
      self.over = True
    else:
      self.guessed.add(guess)
    assert guess in self.guessed

7 8 3 AssertionError

```


Oops, we forgot to add to our set if the guess is *correct*. Both preconditions and postconditions are **contract clauses**: some check at the boundaries of our function to confirm everything is working properly. Together, they form the function’s **contract**, the requirements to use it correct and the guarantees it makes. Used well, contracts have a lot of advantages:

- It’s clear to other developers what the methods require, what they guarantee, and what you’re absolutely not allowed to do with them on pain of death.
- Contracts act on real-world dynamic behavior, as opposed to types (static behavior) and tests (simulated behavior).
- It conceptually separates anticipated bad behavior from impossible behavior. You handle the former with guard statements, and the latter with contracts.
- It simplifies OOP, as we’ll see later.
- Bugs are localized to the violated contract. If a precondition is broken, the program stops right there as opposed to twenty function calls later. If all the preconditions pass but a postcondition is broken, the bug is probably in that specific function body.
- It makes property-based testing a lot more powerful. Since “all contracts are obeyed” is a property of your program, you can point a battery of randomized inputs at your program and get a suite of integration tests for free. You can also use them at the unit level: generate inputs that pass the preconditions of a unit and test that they satisfy the postconditions.


Contracts are a useful correctness tool. You can probably also see that Python `assert` statements are a pretty crude way of shoehorning-in contracts. At the very least, they don’t provide much info when they fail. Can we do better? The good news is we can. The bad news is we kinda don’t.


Let’s start with the most popular library for python contracts: [pycontracts](https://andreacensi.github.io/contracts/). It does simple type checks on your function arguments and defines a DSL for simple comparisons, like “this list has at least three elements”. These can be very useful, but it demonstrates two tropes we see in a lot of contract implementations: using contracts as a type checker, and treating contract syntax as independent from the programming language. I believe the first has played a major role in keeping contracts from the mainstream: contracts make pretty bad type systems. You can dismiss it as “like a static type system, but worse” or as “I didn’t need types anyway, why bother with contracts?” I mean sure you can do this:


```
@contract(a='int,>0',b='list[N],N>0',returns='list[N]')
def my_function(a, b):
    ...

```


And that’s kind of neat but nothing to write home about. Especially if you can’t check the contract before runtime, it’s just a worse form of dependent typing. But just as contracts make for poor types, types make for poor contracts. For example, contracts can relate data between parameters.


```
def get_plane(p1, p2, p3):
  assert type(p1) == type(p2) == type(p3) == Point3D
  assert not colinear(p1, p2, p3)
  ...

```


The first precondition is just a type check and we can replace it with static typing. But the second precondition depends on both the runtime values of the three points and how they all relate to each other. Hard for a type system, but easy for a contract clause.


But to do that we need flexibility in defining our contracts. That’s where most libraries fail us. They use a DSL, which limits what you can actually do with them to what the DSL permits. While pycontracts has an escape hatch, it’s clunky and works against the language. JML for Java has all of those problems and also has a huge and complicated DSL you have to learn. Most other modern languages don’t get that far. Go doesn’t even *have* [assertions](https://golang.org/doc/faq#assertions).


Arguably the only popular “modern” implementation of contracts is [Clojure Spec](https://clojure.org/about/spec). I’m unfamiliar with Clojure so I don’t want to make too many comments, but the *impression* I get is that while it’s a step in the right direction, it’s not intended to be a contract system. It seems that Spec is more intended to help with runtime type checking, but could be wrong here. Their inspiration, [Racket Contracts](https://docs.racket-lang.org/guide/contracts.html), are a little better but still far from what we want, and I wouldn’t call Racket “popular”.


So what do powerful contracts look like? To find out, we have to look at somewhat-more niche languages. Let’s start with [D](https://dlang.org/spec/contracts.html):


```
long square_root(long x)
in
{
    assert(x >= 0);
}
out (result)
{
    assert((result * result) <= x && (result+1) * (result+1) > x);
}
do
{
    return cast(long)std.math.sqrt(cast(real)x);
}

```


`in` and `out` are actually core parts of the language! The writer is free to define contracts with the full power of D. Further, as an OO language, D can define **class invariants**: a contract clause that is checked before and after *every* method call. If anything interacts with our Date in such as way as to break the invariant, the contract is violated.


```
class Date
{
    int day;
    int hour;

    invariant
    {
        assert(1 <= day && day <= 31);
        assert(0 <= hour && hour < 24);
    }
}

```


Not only does this help enforce correctness, it simplifies the whole “inheritence vs composition” dilemma. Child classes have the same class invariants as the parent class, but their preconditions may be weaker and their postconditions may be stronger. If that’s what you want, use inheritance. Otherwise, use compositon.


[Ada 2012](http://www.ada-auth.org/standards/12rat/html/Rat12-2-3.html) goes even further than D. Postconditions can also refer to the states of variables *before* you mutated them, via `'Old`:


```
procedure Pinc(X: in out Integer)
   with Post => X = X'Old+1;
function Finc(X: Integer) return Integer
   with Post => Finc'Result = X'Old+1;

```


In other words, you place contracts on how specific functions change specific variables. If we go back to our python example, this would let us write postconditions like “either `guessed` changed or `over` changed, but not both.”


Finally… we’ve got [Eiffel](https://www.eiffel.org/doc/eiffel/ET%3A%20Design%20by%20Contract%20%28tm%29%2C%20Assertions%20and%20Exceptions).


```
class interface
    ACCOUNT
feature -- Access
    balance: INTEGER
    deposit_count: INTEGER
feature -- Element change
    deposit (sum: INTEGER)
        require
            non_negative: sum >= 0
        ensure
            one_more_deposit: deposit_count = old deposit_count + 1
            updated: balance = old balance + sum
invariant
    consistent_balance: balance = all_deposits.total
end

```


Bertrand Meyer designed Eiffel to be “the language with contracts”. In fact, he trademarked “Design By Contract”, which always struck me as a little weird. Nonetheless Eiffel sets of gold standard for contract support.2 Here’s just a few of the things Eiffel adds:

- “Loop Invariants” that check contracts on each iteration of a loop, and “loop variants” that ensure loops eventually terminate
- `check` contracts that formalize asserts in the middle of a procedure
- Contract clauses can be named to help with documentation and debugging. All classes have a “[contract view](https://www.eiffel.org/files/doc/static/17.05/libraries/base/list_flatshort.html)” for documentation purposes.
- Classes can be “deferred” akin to abstract base classes. Not only can concrete contracts can be placed on deferred methods, they can refer to unimplemented class attributes.
- Eiffel enforces that methods in child classes cannot have stronger preconditions or weaker postconditions than the corresponding methods in the parent class.
- The Eiffel IDE can use a program’s contracts to programmatically generate test cases.


If you want to see what’s possible with contracts, click around in the [Eiffel Standard Library](https://www.eiffel.org/files/doc/static/17.05/libraries/class_list.html). It’s pretty impressive.


Even without native language support, you can still get pretty far with assert statements and whatever libraries your language has. I’d recommend trying it out. Most large codebases have a lot of implicit contracts “enforced” through unit tests and guard statements. Might as well make them explicit.


*Thanks to [Richard Whaling](http://twitter.com/richardwhaling) and Nick P for their feedback.*


---

1. Like everything in Python, this is not guaranteed: you can catch the assertion error. But unlike catching any other kind of error it’s so obviously and unambiguously a fatal error that catching it is a war crime.
 [return]
2. Eiffel is also probably the best implementation of OOP I’ve ever seen. [Obsolete](https://www.eiffel.org/doc/eiffel/ET%3A%20Other%20Mechanisms#Obsolete_features_and_classes) keyword, anyone?
 [return]
