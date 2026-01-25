---
title: "Why TDD Isn't Crap"
date: 2017-10-30
url: https://www.hillelwayne.com/post/why-tdd-isnt-crap/
slug: why-tdd-isnt-crap
word_count: 3014
---

After my recent vitriol about unit testing, a couple of people sent me [Why TDD is Crap](https://www.youtube.com/watch?v=DQBf6li1hww) as a thorough debunking of TDD and unit testing. As someone [very interested](https://www.hillelwayne.com/post/how-do-we-trust-science-code) in software correctness, I ended up writing a debunking of his debunking. Transcriptions will be in quotes, my responses below. Some important notes:

- From what can tell, neither of us is using TDD in the “purest” possible sense of “write the bare minimum that makes the smallest unit test pass”. I’m definitely thinking about TDD as it’s commonly practiced and I believe Smith is, too.
- I really half-assed these transcriptions.
- While Eric Smith is attacking TDD and I’m defending it, keep in mind that he does [TDD Consulting](http://paytonrules.com/) and I [give talks on TLA+](https://www.youtube.com/watch?v=_9B__0S21y8). I don’t think this changes the validity of what either of us say, but it does mean that both of us care very deeply about writing good software, and **this isn’t an argument so much as both of us trying to improve engineering**. Civility is lacking in online debates and that’s a problem with our community.1


> [Mac and] Linux doesn’t use TDD, Linux doesn’t have unit tests either. So I guess you can all switch to Windows, because Windows has TDD built into Visual Studio. … TDD means being a professional as long as you use an unprofessional operating system and an unprofessional programming language.


There’s two ways to read this, and I’m guessing Smith means a little of each. The first is that “Some stellar programmers don’t use TDD, so you don’t have to use TDD to be a professional.” One of the toxic bits of programming culture is to mock anybody who doesn’t believe everything you do. Robert Martin [does this with TDD](https://news.ycombinator.com/item?id=10107156), while Amanda Laucher and Paul Snively do this with [static typing](https://www.youtube.com/watch?v=SWTWkYbcWU0). On the whole, we’d be a lot better off if we stopped this nonsense.


The less charitable way to read this is “These people didn’t need TDD, so you don’t either.” And this is a common argument many programmers make. But examples aren’t data. Just because Linus Torvalds didn’t need TDD doesn’t mean that you and I, who aren’t anywhere as good, don’t need it either. I mean, I could point at the [J codebase](https://github.com/jsoftware/jsource/blob/master/jsrc/af.c) and say “you don’t need whitespace.” Fact is, we’re all mediocre at best, and we should be choosing our techniques on what *we* need, not what programming legends need.


> Have you seen any studies comparing unit testing to other methods? There aren’t any. … We have no evidence that TDD produces fewer bugs, we just have people that think it does.


A lack of hard data on TDD is more a comment on our industry than it is on TDD. One frustrating thing about software engineering is that it’s really, *really* hard to study. For example, we [still](https://danluu.com/empirical-pl/) don’t know whether static typing reduces bugs!2 The best we have is a collection of pilots, case studies, and controlled experiments on students. I can’t give you anything that conclusively affirms or debunks the value of TDD, just like I can’t do that for *anything*. The best I have is intriguing papers.


So does TDD work? The best study I’ve seen on it is the [Dr. Nagappan case study](https://www.microsoft.com/en-us/research/wp-content/uploads/2009/10/Realizing-Quality-Improvement-Through-Test-Driven-Development-Results-and-Experiences-of-Four-Industrial-Teams-nagappan_tdd.pdf), where he compared TDD and non-TDD projects in Microsoft and IBM.3 Each pair of teams worked on different features in the same large project to avoid comparing “computer games and nuclear reactors”. He found the TDD projects had roughly a 60% decrease in defect density and took about 25% longer. That cautiously suggests that yes, TDD might be a useful correctness technique.


On the other hand, TDDers might not need to stick to a strict “red-green-refactor” cycle: [Fucci et. al](http://neverworkintheory.org/2016/10/05/test-driven-development.html) found that there was no difference between writing the tests before a chunk of code and writing them after. On the other-other hand, [George and Williams](https://collaboration.csc.ncsu.edu/laurie/Papers/TDDpaperv8.pdf) found that when people don’t have to write tests before the code, they often forget to write them at all…


Look, studying software is hard and we’re not very good at it. But if you put a gun to my head and asked if TDD worked, I’d probably say “yes”. I think most software engineering researchers are on the same page there.


> Most bugs are in the interaction level, and we know this.


[Agreed](https://www.hillelwayne.com/post/unit-tests-are-not-tests). Nonetheless, the studies (tentatively) show that TDD helps. Most bugs are at the interaction level, but having a shaky foundation certaintly doesn’t make things better.


> People who don’t write tests have fewer bugs because they have less code to debug. We say code is liability, but we continue to create liability with code nobody actually needed.


This is a real problem with testing and general software correctness. [One systems saying](https://www.youtube.com/watch?v=SM2uXpmyJmA) I’ve heard is “When your system gets large enough, most critical failures are caused by your failsafes”. However, that’s not an argument against failsafes; it’s an argument to be just as careful with our failsafes as we are with our production code. Everything you build is, by definition, part of the problem.


In the specific case of unit testing, we can “ask less” of tests than we do production code. It’s a common guideline that your tests should be as simple as possible, which reduces the defect surface for bugs. Additionally, the failure mode of unit tests is less dangerous than production code: either the test is a false positive, which guides us to fix it, or it’s a false negative, which reduces our coverage but doesn’t exactly make things *worse*. Of course it can give us false confidence, but every verification techniques does that. That’s why we need defense-in-depth.


Failsafes can cause critical failures in large systems, but the failsafes are the reason your system can afford to grow large in the first place.


> How are you going to be faster when you’re writing all these unit tests? When you go home, you write a spike because we know it’s faster. But that’s fine, what about production code? TDD evangelists ignore maintenance! Ever spend a day or a week trying to debug CI?


It’s a common argument that “TDD takes less time to write”, which doesn’t seem to be true. The Nagappan study suggests it reduces defects, but it *does* take longer. TDD takes less time overall”, though, is slightly different, because it includes post-release maintenance. The study explicitly does not factor this time in. Using a conservative estimate that the amount of time it takes to fix a bug is equal to the amount of time it took to code the bug, a 50% reduction for 25% longer time probably saves net time in the post-release maintenance. I haven’t been able to find any studies that give solid numbers.4


As for the “you have to debug CI” argument, that’s a common discussion mistake we make: comparing “something” to “nothing” when we really should be comparing it to “something else”. TDD has maintenance overhead, but so does every other correctness technique! You’ll need a server if you want to compile a statically-typed language. You’ll need a few servers if you want to run a staging environment. You’ll need a bunch of servers and a hug if you want to validate behavior across microservices. And you’ll need an [Aphyr](http://jepsen.io/) if you want to test a distributed system. If you’re doing any of that, adding unit tests isn’t going to be much of a marginal cost.


> Testing is about design! Good thing we put ‘testing’ in a title! Test driven development makes your designs better. Why? Because they’re more testable. That’s a circle. We don’t know what a good design is, we have some principles, principles we made up just like we made up TDD.


I’m honestly a little “meh” on the “TDD is about design.” Beck and Cunningham intended it that way, but in practice it’s better as a testing and scaffolding technique than a design technique. TDD does help mildly by forcing you to constantly be calling your functions, so you realize if they’re awkward sooner. But as much as we’d like to turn design into a coding project, design is much more fundamental than whatever makes up the implementation. Testing does not substitute for thinking.


I’ve read a few articles that suggest that testing does, in fact, lead to better designs, but for the life of me I can’t dig them up. If you have any, feel free to send them my way.


> Testing is more fun! … You know what’s not fun? Debugging tests. Paying for tons of machines so we can run tests.


This is a case of comparing something to nothing. Most existing correctness techniques are *miserable* to use.5 If you don’t hate it, you haven’t pushed it hard enough. My friends have stories of struggling to fit a program they *knew* was correct into the language’s type system. I once spent three hours trying to debug a broken TLA+ spec, eventually finding that I mixed up `=>` and `=>`. Debugging tests ain’t got shit on that.


---


At this point Smith talks about alternative techniques to TDD and unit testing to ensure software correctness. All of these approaches are very good and catch bugs TDD will miss, but all also have their tradeoffs. I’d like to go into them in detail.


> Design-by-contract has done some empirical studies and does really well for itself. With design-by-contract, you can prove it works.


Smith doesn’t explain what design-by-contract is, so here’s an example from the [Babel Contracts](https://github.com/codemix/babel-plugin-contracts) javascript library:


```
function withdraw (fromAccount, amount) {
  pre: {
    typeof amount === 'number';
    amount > 0;
    fromAccount.balance - amount > -fromAccount.overdraftLimit;
  }
  post: {
    fromAccount.balance - amount > -fromAccount.overdraftLimit;
  }

  fromAccount.balance -= amount;
}

```


Whenever you call `withdraw`, it checks every statement in the precondition. If any are false, the program errors. The same thing happens in the postcondition, which is called when the function ends. This makes it much easier to find bugs in development and testing because errors don’t “propagate” from where they originate. Additionally, since everything has contracts and calls other things with contracts, you get assurance on the integration level. EiffelStudio (the Eiffel IDE) can even generate tests that check your contracts.


There are two main problems with contracts, though. First, it provides *safety* that your program won’t do bad things, but it doesn’t confirm that it actually does what you want. It’s telling that EiffelStudio, in addition to providing world-class contract support, also comes with a unit testing library.  You combine both unit tests and contracts for better confidence.


The other problem is that contracts require first-class language support, while you can do simple unit testing pretty much anywhere. Babel Contracts got lucky with Javascript: there’s an unused feature called “labels” that they were easily able to hack into pre/postconditions. But even their system is crude compared to Eiffel. A toy example:


```
class
  ACCOUNT
feature
  balance: INTEGER
  -- Bunch of methods
invariant
  no_overdrafts: balance >= 0
end

```


`no_overdrafts` is a class invariant. It’s checked whenever any method on an account called or any kind of mutation happens, and EiffelStudio can compare it to all internal methods and all users of the object to generate extremely intricate tests. `no_overdrafts` can also be inherited, composed, or overridden like any other class property.6 In Eiffel, you can do incredible things with contracts. In Javascript, you just have pre/postconditions. In Ruby, you have a glorified [type checker](http://egonschiele.github.io/contracts.ruby/). But all three languages have solid unit testing frameworks.


> Haskell has property based testing. It throws tons of tests at your code, well more than you’ll ever think of.


PBT (also called *generative testing*) is where you give a generator some rules and ask it to make tests for you. While the first PBT library was Haskell Quickcheck, arguably the most sophisticated is the [Hypothesis](http://hypothesis.works/) Python library. Here’s what a property-based test in Hypothesis looks like:


```
from hypothesis import given
from hypothesis.strategies import text
from lexer import lex # str -> List[Lexeme]


@given(text("+-*/()123456789", max_size=10))
def test_lexes_properly(maths):
    lexeme_strings = map(str, lex(maths))
    assert "".join(lexeme_strings) == maths

```


Hypothesis grabs a random string, such as `10**2+3`. `lex` takes that and turns it into a list of lexeme objects, like `[NUM(10), POWER, NUM(2), PLUS, NUM(3)]`. We assert that it stringifies back into `10**2+3`. Hypothesis will keep throwing random and pathological strings into the test until it either finds an error or is satisfied that my `lex` function passes the test. This single property test replaced the original ten unit tests and had better coverage, too: it found a lexing error I hadn’t tested for.7


PBT vs TDD, though, is a false dichotomy. I don’t see TDD as meaning only unit tests. Sometimes, before writing code, I’ll write a few unit tests. Other times I’ll write a few property tests. The main benefit property tests have is they test a wider space. The main drawback they have is that they’re not very specific. With unit tests, you know exactly what input you’re giving in and exactly what output you want out. With property tests, you only know what *kinds* of inputs are going in and can’t provide the exact output you want. Instead, you have to be clever and look for patterns. `test_lexes_properly` is an example of an [encode/decode](http://hypothesis.works/articles/encode-decode-invariant/) invariant, where you test that some transformation is perfectly reversible. Another technique is using an [oracle](https://www.hillelwayne.com/post/hypothesis-oracles), where you find some trick to start out with the answer. Compare these to the simplicity of writing `assert foo(bar) == baz` as a unit test.


Unit tests and PBTs complement each other. You use the former to check a couple of cases work right, and then use PBTs to draw conclusions about the wider input space. There is no conflict with TDD here.8


> Hammock-driven development. We reject big design upfront … it’s important. It needs to be done sometimes.


I disagree very strongly with Eric Smith here. Upfront design does **not** “need to be done sometimes”. Agile was a response to how miserably BDUF is… and went too far the other way. We should **not** be thinking of careful design and planning as a niche thing. Design is fundamental and necessary to software correctness.


This does not mean going back to BDUF and 1,000 page requirements documents. But it’s [vastly](http://csse.usc.edu/TECHRPTS/1986/usccse86-501/usccse86-501.pdf) [harder](http://bitfunnel.org/strangeloop/) [to](https://www.safaribooksonline.com/library/view/making-software/9780596808310/ch10s02.html) fix a bug in development than it is to fix it in design. Before writing code, I try to draw a directed graph in [graphviz](http://www.linuxdevcenter.com/pub/a/linux/2004/05/06/graphviz_dot.html) or a sequence diagram in [mermaid](https://github.com/knsv/mermaid). The amount of errors I catch in the diagrams is a little embarrassing. If your only takeaway from this essay is “learn mermaid”, I’ve done my job.


If you want to go further than that, I’d recommend exploring *formal specification*, in particular the two “flyweight methods” languages. The first, [Alloy](http://alloy.mit.edu/alloy/), is used to verify data structures. I’ve not used it in production but have heard good things from people I trust. I *have* used [TLA+](http://lamport.azurewebsites.net/tla/tla.html) to find concurrency bugs in my designs, and it’s absolutely incredible. I genuinely believe it could revolutionize software, and have written a [comprehensive beginner’s guide](https://learntla.com/) to help that process along.


But does this replace TDD? No. Good design is critical, but then you need to code and test your design. And TDD is quite often a good technique to do that.9


> Every organization has a QA department. If TDD was a silver bullet, we wouldn’t need it.


I agree. We also have a bad habit of seeing software test engineers as being somehow “lesser” than the product engineers. Rigorous testing is as much as specialist skill, with specialist programming knowledge, as any other part of software. In fact, you *shouldn’t* have the QA department write unit tests any more than you should have the product department do pentests. TDD is a technique for developers. Testers should be busy writing more complex, more terrifying tests.


---


Here are my main takeaways:

- We don’t actually know that much about what good software engineering looks like.
- TDD is *likely* a good correctness technique and is *probably* useful in many projects.
- There are other correctness techniques that have different strengths and weaknesses relative to TDD. You should probably be using a mix, with the optimum ratio being dependent on the project, external constraints, and size of your correctness budget.
- Regardless of how you approach correctness, it’s definitely worthwhile to do some design in advance.
- We shouldn’t call people unprofessional just because they disagree with us.
- QA don’t get enough respect.


*Thanks to [Richard Whaling](http://twitter.com/richardwhaling) for their feedback.*


---

1. I’m not [blameless](https://www.hillelwayne.com/post/uncle-bob) here either.
 [return]
2. I’d be remiss without mentioning a [recent paper](http://ttendency.cs.ucl.ac.uk/projects/type_study/documents/type_study.pdf) that looks more rigorous than its peers. There’s a couple of threats to validity I want to look into, though.
 [return]
3. Surprisingly, Microsoft is probably the biggest investor in software engineering research in the world. I wouldn’t be surprised if they spent more on it than the rest of the Big Five combined. In terms of formal verification research, the only group that’s comparable is the [country of France](https://en.wikipedia.org/wiki/French_Institute_for_Research_in_Computer_Science_and_Automation). 
 [return]
4. Yes, I know about the “IBM Systems Science Institute” graph. It’s [probably](https://plus.google.com/+LaurentBossavit/posts/DZyraS7bWTE) not [real](https://plus.google.com/+LaurentBossavit/posts/aNKut1QV8pT).
 [return]
5. I think this is 20% “testing is intrinsically hard” problem and 80% “Nobody invests in software correctness UX”.
 [return]
6. I wonder if the reason OO languages are considered so buggy is because none of the popular ones went all-in on class contracts. It seems like a killer feature of classes that nobody’s heard of.
 [return]
7. Specifically, if the string ended with a multicharacter token followed by a multidigit number, it would leave off the last digit. For example, `2**10` would lex as `[NUM(2), POWER, NUM(1)]`.
 [return]
8. PBT also [synergizes really well](http://www.squarefree.com/2014/02/03/fuzzers-love-assertions/) with contracts.
 [return]
9. There are some *formal verification* languages, like [ACL2](https://www.cs.utexas.edu/users/moore/acl2/) and [Coq](https://coq.inria.fr/), where you can formally prove your code matches the design. In practice, though, they are much too difficult and expensive to use for 99% of projects. But I’ve heard [Idris](https://www.idris-lang.org/) is showing promise.
 [return]
