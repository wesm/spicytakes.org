---
title: "An RNG that runs in your brain"
date: 2024-01-22
url: https://www.hillelwayne.com/post/randomness/
slug: randomness
word_count: 2543
---

Humans are notoriously bad at coming up with random numbers. I wanted to be able to quickly generate “random enough” numbers. I’m not looking for anything that great, I just want to be able to come up with the random digits in half a minute. Some looking around brought me to [an old usenet post](https://groups.google.com/g/sci.math/c/6BIYd0cafQo/m/Ucipn_5T_TMJ?hl=en) by George Marsaglia:


> Choose a 2-digit number, say 23, your “seed”.
> Form a new 2-digit number:
> the 10’s digit plus 6 times the units digit.
> The example sequence is
> 23 –> 20 –> 02 –> 12 –> 13 –> 19 –> 55 –> 35 –> …
> and its period is the order of the multiplier, 6, in the group of
> residues relatively prime to the modulus, 10. (59 in this case).
> The “random digits” are the units digits of the 2-digit numbers,
> ie, 3,0,2,2,3,9,5,… the sequence mod 10.


Marsaglia is most famous for the [diehard suite](https://en.wikipedia.org/wiki/Diehard_tests) of RNG tests, so he knows his stuff.1 I’m curious why this works and why he chose 6.


We’re going to use [Raku](https://www.raku.org), the [language for gremlins](https://buttondown.email/hillelwayne/archive/raku-a-language-for-gremlins/).2 I’ll be explaining all the weird features I use in dropdowns in case you’re a bit of a gremlin, too.


# Intro


The sequence is periodic, meaning that if we iteratively apply it we’ll eventually get the same element. Let’s start with a function (“subroutine”) that produces the whole sequence:


```
my sub next-rng(Int $start, Int $unitmult = 6, --> List) {
    my @out;
    my $next = $start;
    repeat while $next !(elem) @out {
        @out.append($next);
        $next = sum($next.polymod(10) Z* $unitmult,1);
    };
    return @out;
}

```


Explanation
  
Raku is an extremely weird language but I’ll keep it as straightforward as I can.

`@` and `$` are [sigils](https://docs.raku.org/language/variables#Sigils) for “positional” (listlike) and “scalar” respectively. Defining a positional without assigning anything defaults it to the empty array.
`(elem)` checks for membership, and `!` can be applied to negate any infix operator. `(elem)` is the ASCII version— Raku also accepts ∈.
[polymod](https://docs.raku.org/type/Int#method_polymod) splits a number into a remainder and dividend, ie `346.polymod(10) = (6 34)`. It takes multiple parameters, so you can do things like `num.polymod(60, 60, 24)` to get hours-minutes-seconds.
[Z](https://docs.raku.org/language/operators#Zip_metaoperator) is the “zip” metaoperator, applying a infix op elementwise between two lists. `(4, 6) Z* (6, 1)` = `(4*6, 6*1)`.


show all


Once we have a sequence we can print it with the `put` or `say` commands, which have [subtly different behaviors](https://docs.raku.org/language/faq#How_and_why_do_say,_put_and_print_differ%3F) I’m not going to get into.


```
put next-rng(1);

```


```
01 06 36 39 57 47 46 40 04 24 26 38 51 11 07 42 16 
37 45 34 27 44 28 50 05 30 03 18 49 58 53 23 20 02 
12 13 19 55 35 33 21 08 48 52 17 43 22 14 25 32 15 
31 09 54 29 56 41 10 01

```


Remember, the random numbers are the *last* digit. So the RNG goes 1 -> 6 -> 6 -> 9 -> 7 -> 7 -> …


## Investigating Properties


If the RNG is uniform then each digit should appear in the sequence the same number of times. We can check this by casting the last digits to a multiset, or “bag”.


```
say bag(next-rng(1) <<%>> 10);

```


Explanation
  

`<<op>>` is the [hyper metaoperator](https://docs.raku.org/language/operators#Hyper_operators) and “maps” the inside operator across both lists, *recursively going into list of lists too*. IE `((1, 2), 3) <<+>> 10` is `((11, 12), 13)`! Hyperoperators have a lot of other weird properties that make them both useful and confusing.
Bags count the number of elements in something. `bag((4, 5, 4)){4} = 2`. Confusingly though they can only contain scalars, not arrays or lists or the like.


show all


```
Bag(0(5) 1(6) 2(6) 3(6) 4(6) 5(6) 6(6) 7(6) 8(6) 9(5))

```


That seems to be a uniform-enough distribution, though I’m a bit less likely to get a 0 or a 9.


My next idea comes from the diehard tests. From [the wiki](https://en.wikipedia.org/wiki/Diehard_tests#Test_overview):


> **Overlapping permutations**: Analyze sequences of five consecutive random numbers. The 120 possible orderings should occur with statistically equal probability.


There are only 54 5-number sequences in the dataset, so I’ll instead apply this to 2-number “transitions”. I’ll do this by outputting a 10-by-10 grid where the (i, j)th index (from 0) is the number of transitions from last-digit `i` to `j`. For example, the sequence includes the transition `28 -> 50`, and no other transitions of form `X8 -> Y0`, so cell (8, 0) should be a `1`.


```
sub successions-grid(@orbit) {
  my @pairs = (|@orbit , @orbit[0]).map(* % 10).rotor(2 => -1);
  for ^10 -> $x {put ($x X ^10).map({@pairs.grep($_).elems})}
}

```


Explanation
  

`| @f, $x` concats `$x` directly onto `@f`. Without the `|` it’d be a two-element list instead.
The `*` in ``* % 10`` is a [whatever](https://docs.raku.org/type/Whatever), a weird little operator that does a lot of things in a lot of different contexts, but usually in this case lifts the expression into a closure. *Usually*. It’s the same as writing `map({$_ % 10})`.1
[rotor](https://docs.raku.org/type/List#routine_rotor)`(2 => -1)` gets two elements, then goes one element back, then gets two more, etc. `[1, 2, 3, 4].rotor(2 => -1)` is `[(1, 2), (2, 3), (3, 4)]`. You could also do `rotor(2)` to get `[(1, 2), (3, 4)]`, or `rotor(1 => 1)` to get `[1, 3]`. Rotor is really cool.
`^10` is just `0..9`. For once something easy!
[X](https://docs.raku.org/language/operators#Cross_metaoperators) is the cross product [metaoperator](https://docs.raku.org/language/operators#Metaoperators). So if `$x = 2`, then `$x X ^4` would be `((2 0), (2 1), (2 2), (2 3))`. And yes, the operator can get much, much stranger.
`grep(foo)` returns a list of all elements [smart-matching](https://docs.raku.org/language/operators#infix_~~) `foo`, and `.elems` is the number of elements in a list. So `@pairs.grep($_).elems` is the number of elements of the list matching `$_`. This took me *way* too long to figure out




Actually `-> $x {$x % 10}` but close enough
 [return]



show all


```
> successions-grid(next-rng(1, 6))

0 1 1 1 1 1 0 0 0 0
1 1 0 0 0 0 1 1 1 1
0 0 1 1 1 1 1 1 0 0
1 1 1 1 0 0 0 0 1 1
0 0 0 0 1 1 1 1 1 1
1 1 1 1 1 1 0 0 0 0
1 1 0 0 0 0 1 1 1 1
0 0 1 1 1 1 1 1 0 0
1 1 1 1 0 0 0 0 1 1
0 0 0 0 1 1 1 1 1 0

```


We can see from this table that some transitions are impossible. If I generate a 0, I can’t get a 6 right after. Obviously not a great RNG, but my expectations were pretty low anyway.


## Why 6?


What if instead of multiplying the last digit by 6, I multiply by 4?


```
> say next-rng(1, 4);
01 04 16 25 22 10 

```


I dunno, I kinda like an RNG that never gives me 3. The distinct sequences are called orbits and their lengths are called periods. Let’s see all the possible orbits we can get by using 4 as the multiplier:


```
sub orbits-for-mod(int $mult, $top = 20) {
  my &f = &next-rng.assuming(*, $mult);
  (1..$top).map(&f).unique(as => &set)
}

```


Explanation
  

`&` is the [sigil](https://docs.raku.org/language/variables#Sigils) for “callable” or function subroutine. The `.assuming` method does a partial function application, and passing a `*` makes it partially apply the *second* parameter.1
The `map` returns a sequence of lists, which we pass to [`unique`](https://docs.raku.org/type/independent-routines#routine_unique). `as => &set` converts every sequence in the `map` to a set and compares *those* for uniqueness, instead of the original lists. But the final result uses the elements prior to conversion.
If that’s confusing, a simpler example is that `[-1, 1].unique(as => &abs)` returns `[-1]`, while `[1, -1].unique(as => &abs)` is `[1]`.




[Daniel Sockwell](https://www.codesections.com/) (aka codesections) kindly agreed to read a first draft of this post, and he told me about `assume`. Thanks Daniel!
 [return]



show all


```
> say orbits-for-mod(4, 38).map(*.gist).join("\n");
[1 4 16 25 22 10]
[2 8 32 11 5 20]
[3 12 9 36 27 30]
[6 24 18 33 15 21]
[7 28 34 19 37 31]
[13]
[14 17 29 38 35 23]
[26]

```


Explanation
  
Quoting [Daniel Sockwell](https://www.codesections.com/):

The `.map(*.gist).join("\n")` is just there to prettify the output. `cycles-for-mod` returns a `Seq` of `Array`s; mapping over each `Array` with `.gist` converts it into a string surrounded by square brackets and `.join("\n")` puts a newline between each of these strings.


show all


If you picked 13 as your starting value, your random digits would be 3, 3, 3, 3, 3, 3.


Preempting 50,000 emails[(source)](https://xkcd.com/221/)


For obvious reasons, 4 should never be our multiplier. In fact for a multiplier to give a “good” RNG, it needs to have exactly one orbit. As we’ll see later, this guarantees a(n almost) uniform distribution.


```
> say (1..30).grep(*.&orbits-for-mod == 1)
(3 6 11 15 18 23 27)

```


Explanation
  

`.&` applies a top-level routine as a method. `grep(*.&f)` is the equivalent of `grep({f($_)})`.
`&orbits-for-mod` returns a list. `==` coerces both inputs to numbers, and coercing a list to a number returns the number of elements. So we’re testing if the returned list has one element, ie there’s exactly one orbit. (If you don’t want to compare without coercion, use either [===](https://docs.raku.org/language/operators#infix_===,_infix_%E2%A9%B6) or [eqv](https://docs.raku.org/language/operators#infix_eqv).)

This way of doing things is pretty slow and also only looks for orbits that *start with* a number up to 20. So it would miss the `26 -> 26` orbit for `x=4`. We’ll fix both of these issues later.

show all


So some “good” choices for `n` are 6, 11, and 18.


Note that if you end up with a three digit number, you treat the first two digits as a single number. For `n=11`, `162` leads to `16 + 22`, not `6 + 22` (or `6 + 1 + 22`).


## Why does this work?


Here’s a part of the explanation that really confused me:


> and its period is the order of the multiplier, 6, in the group of
> residues relatively prime to the modulus, 10. (59 in this case).


After talking with some friends and a lot of reading Wiki articles, it started making more sense. I’m mentally computing a “[multiply with carry](https://en.wikipedia.org/wiki/Multiply-with-carry_pseudorandom_number_generator)” RNG with constants `a=x` and `c=10`. This choice has a cool property: if `MWC(x) = y`, then `10y mod (10mult-1) = x`!


```
MWC:    01 -> 06 -> 36 -> ... -> 41 -> 10 -> 01
10y%59: 01 -> 10 -> 41 -> ... -> 36 -> 06 -> 01

```


That’s pretty neat! It’s easier for me to mathematically reason about `10y mod 59` than “multiply the last digit by six and add the first digit”. For example, it’s clear why the RNG generates 0 and 9 slightly less often than the other digits: no matter which multiplier we pick, the generated sequence will go from 1 to 10n-2, “leaving out” 10n-1 (which ends with 9) and 10n (ends with 0).


“Multiply and modulo” is also known as the [Lehmer RNG](https://en.m.wikipedia.org/wiki/Lehmer_random_number_generator).


## Finding better RNGs


So what other numbers work? We already know that a good multiplier will produce only one orbit, and I showed some code above for calculating that. Unfortunately, it’s an O(n²) worst-case algorithm.3 Thinking about the MWC algorithm as “Lehmer in reverse” gives us a better method: if `n` is a good multiplier, then the period of the orbit starting from 1 should be `10n-2`.


The Lehmer approach also gives us a faster way of computing the orbit:


```
sub oneorbit(\x) {
  10, * *10% (10*x - 1) … 1
}

```


Explanation
  



[(source)](http://howfuckedismydatabase.com/nosql/)






    Real Explanation
  

Writing `\x` instead of `$x` as a param lets use use `x` instead of `$x` in the body.
`...` is the [sequence operator](https://docs.raku.org/language/operators#infix_...). It can do a *lot* of different things, but the important one for us is that if you write `10, &f … 1`, it will start with 10 and then keep applying `&f` until it eventually generates `1`.
In `* *10%[etc]`, the first `*` is a Whatever and the second `*` is regular multiply. This then lifts into the function `-> $a {$a * 10 % (10*x - 1)}`.

This actually produces the orbit in reverse but we’re only interested in the period so nbd.

show all


Then we check the period using the same “`==` coerces lists to lengths” trick as before.


```
> say (1..100).grep({oneorbit($_) == 10*$_-2});

(2 3 6 11 15 18 23 27 38 39 42 50 51 62 66 71)

```


I can see why Marsaglia chose 6: most programmers know their 6 times-table and it never returns a 3-digit number, so the addition step is real easy. The orbit has only 58 numbers and you won’t get some digit sequences, but if you need to pull out a few random digits quickly it’s totally fine.


If you want more randomness, I see a couple of candidates. 50 has a period of 498 and is incredibly easy to compute. If the final digit is even then you don’t need to do any carries: **23**8 -> 4**23**!


That said, the 50-sequence doesn’t *seem* as random as other sequences. There’s a point where it generates 9 even numbers followed by 8 odd ones. Don’t use it to simulate coin flips.


The last interesting number is 18. It has a respectable period of 178 and has every possible digit transition:


```
> successions-grid(next-rng(1, 18))

1 2 2 2 2 2 2 2 1 1
2 2 2 2 2 2 1 1 2 2
2 2 2 2 1 1 2 2 2 2
2 2 1 1 2 2 2 2 2 2
1 1 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 1 1
2 2 2 2 2 2 1 1 2 2
2 2 2 2 1 1 2 2 2 2
2 2 1 1 2 2 2 2 2 2
1 1 2 2 2 2 2 2 2 1

```


The downside is that you have to learn the 18 times-table. This isn’t too bad: I internalized it with maybe 10 minutes of practice. I’m still not *great* at doing the whole MWC step but I can consistently produce another random digit every five seconds or so. That’s good enough for me.


You can see the Raku code I used to research this [here](./src/rng.raku). It’s set up [as a CLI](https://buttondown.email/hillelwayne/archive/raku-is-surprisingly-good-for-clis/) so you can use it in a few different ways; see the file for more info.


*Thanks to [Codesections](https://www.codesections.com/) for feedback and [Quinn Wilton](https://twitter.com/wilton_quinn) and [Jeremy Kun](https://jeremykun.com/) for helping me understand the math.*


---

1. Assume that every time I say “RNG” I mean “PRNG”.
 [return]
2. Also full disclosure the code I’m showing is *less gremliny* than the code I originally wrote. So just know it can be *more gremlins* than this.
 [return]
3. if multiplier `n` has a single orbit, then we’ll run `next-rng` on ~10n-2 numbers, and the function will iterate 10n-2 times (since it has to go through every number in the orbit). If I bothered to skip numbers I’d already seen in an orbit then the runtime would collapse to O(n).
 [return]
