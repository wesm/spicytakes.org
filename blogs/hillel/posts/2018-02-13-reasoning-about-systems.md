---
title: "It's Hard to Reason About Systems"
date: 2018-02-13
url: https://www.hillelwayne.com/post/reasoning-about-systems/
slug: reasoning-about-systems
word_count: 1666
---

In programming arguments, such as static vs dynamic typing,1 people use their experiences and reason to frame these debates. However, reason is often a poor grounding for justifying complex positions. Usually warnings against using “reason” take the form of “it’s easy to be biased” or “we tend to make logical fallacies.” But this presupposes that if we were less biased we *could* answer the question by thinking really hard. I’d like to argue that this is actually impossible: we can’t understand something “static vs dynamic” with reason alone. Our minds are just not powerful enough.


First of all, it doesn’t make sense to talk about whether something is “better” or “worse”. We have to talk about what it’s better or worse “for”. In the case of static vs dynamic typing, it’s usually (*usually*) about software correctness: how closely the software’s behavior matches spec.2 We also need to talk about about whether it’s better or worse “in what context”. If I say “static typing is more correct than dynamic typing” the claim changes significantly if I am talking about shipping a commercial product vs making art vs munging logs and whether I have two people, a hundred people, etc. Usually (*usually*) it’s in the context of “shipping a generic business product where the manpower budget is finite.”


That context is a **system**, though: something with multiple conflicting goals, actors, and moving parts. You’re not just trying to maximize correctness: you’re also trying to maximize things like ‘productivity’ and minimize ‘complexity’.


This means we’re now dealing with **impacts** and everything goes to hell.


### Impacts


Generally, when we say “impacts”, we mean “indirect impacts”. Direct ones are what we’re actually intending to do when we do things, and I’ll explicitly call them “direct impacts”.


The simplest possible impact is **opportunity cost**: by doing X, you have fewer resources to do other things. If I write tests, I have less time remaining to write production code. The opportunity cost is less productivity.


“That’s now how testing works!” Of course it isn’t. Almost nothing in software engineering is just an opportunity cost. We most often think of impacts as **linear**: doing X to change A may also change B. I know users like cool UIs. I add a cool UI with lots of slick banners and CSS animations. That means I have to send more data to the client, leading to longer load times. Adding features has the direct impact of higher user satisfaction and the linear (indirect) impact of decreased performance.


But wait! That’s only the **first-order** impact, the effect A has on B. B can also have an impact on C, the **second-order** impact. Reducing performance reduces user satisfaction: people hate slow websites. The second-order impact of adding features is decreased user satisfaction. But remember, we added features to *increase* user satisfaction. The second order here is working against the direct impact! If the direct impact is marginal enough and the slowdown is serious enough, it could even reduce satisfaction more than the feature added it. Understanding second-order impacts is incredibly unintuitive.


Can it get worse? Of course it can get worse. Why stop at second-order? C could affect D, D could affect B and E, and so on. Distributed systems trade performance for scalability. Scalability requires orchestration, which increases complexity, which means more devops, who need more office space… Everything affects everything else. As the impacts bounce through your system it becomes harder to tease out cause and effect. Are your build times slow because you’re using Chef or because you bought the spinny office chairs? Who knows!


Finally, because things just aren’t quite bad enough yet, let’s add **nonlinear** impacts. That’s when doing X changes how much *doing Y* changes things. Consider how increasing complexity tends to decrease correctness and reliability in your system. If you have good documentation, then that linearly improves your correctness and productivity. But it also means that adding more complexity doesn’t reduce correctness as much as it would have if you didn’t have documentation. That change in the rate of change is a nonlinear impact.


Too bad everything we like is nonlinear. By having good tests you can move faster. That’s nonlinear. Types support better refactoring tools? Nonlinear. [Using Clojure will attract better developers](https://wesmorgan.svbtle.com/recruiting-software-developers-language-matters)? Nonlinear. Everything’s nonlinear. And, of course, they don’t have to be first-order. Changing the rate of impact on B can change the rate on C. We can also go deeper: Not only can we change the degree of impacts of actions, we can change *how much we change* the degree of impacts!


Hopefully you’re starting to see why we can’t reason our way to answers. Programming isn’t a set of isolated factors you can tackle separately. Everything impacts everything else. We can’t solve a complex system with thinking alone. If you disagree, consider physics: there’s no closed-form solution to the three body problem. Why would a 100-body problem be any different?


If software is so complicated, how do we get anything done? Humans are fantastic at rough heuristics. All these complexities soak into our brains and we build an intuition about how it all works. But heuristics are also intensely irrational. That’s not a bad thing! It just means that it depends as much on our experiences, emotions, and muscle memory as it does on our conscious thought. Good for getting stuff done. But the further we get from our narrow experiences, the less useful it becomes. That means it’s pretty bad for finding the objective truth. Just because TDD works for you doesn’t mean it’s the right choice for everyone else. Your intuition about *your* system may not apply to *their* system.


When we do communicate, we tend to simplify. This is necessary and practical. Second-order impacts tend to be smaller than first-order impacts, third-order smaller still. We can often disregard them as being small enough to be negligable. Adding tests takes up disk space, but you usually don’t care about that. Using up more disk space means pushing to remote takes slightly longer, but you care even less about that. On the other hand, you can’t always write off the second-order impacts: in fact, we often obsess over them.


So at what point do you call it negligable?

- Static Type Person: “With dynamic types you need to write more tests. That’s an opportunity cost: you could have spent that time doing something else. So static types are safer than dynamic types.”
- Dynamic Type Person: “With static types you need to fight the typechecker. That’s a linear impact: It increases the amount of boilerplate you write. We can complete the system faster and use the extra time to write more tests.”
- Static Type Person: “Until you have to refactor anything. Then you’ll have regressions everywhere that the static types will protect us from. In the long run, dynamic types have a nonlinear impact that reduces how maintainable your systems are, leading to buggier software. Static types are safer.”
- Dynamic Type Person: “Not as much as contorting your abstractions around the type system instead of problem domain. Dynamic typing can more faithfully reproduce the actual taxonomy, which reduces complexity, which increases extensibility and correctness. Dynamic types are safer.”


Where do you draw the line?


### Enter Empiricism


There’s something else we can do. We take a hundred teams and ask them to complete some large project. Then we find some way of comparing the various qualities of the different versions of the project, control for various factors, and look for patterns. Then we do it again. Enough times, and we’ll have some sense of whether some cause (eventually) has some effect.


“How does this solve the problem of impacts?” If done with a large enough project over a long enough timescale, all of the significant impacts will manifest. In the case of “do type systems improve correctness”, the end projects will be affected by the opportunity cost *and* fighting the typechecker *and* refactoring regressions *and* the taxonomy mismatch. If we then measure correctness, say by comparing the projects to a formal specification, we’d have a way to determine overall impact type systems have on correctness. It won’t tell us how *much* each chain of impacts affected things, but it’s better than nothing.


“That sounds really hard to do.” It is. I’m not going to pretend its easy or elegant. Hard problems have hard solutions.


“Wouldn’t this kind of study be expensive?” Amazon made 2 billion profit last quarter. If answering this cost 10 million and would improve their profits by 0.05%, then it’d pay for itself within three years. Software is the richest industry in the history of the world, and it’s absolutely crazy to think we can’t afford basic research on how to write software good.


“Does this even work?” Ever hear of N-version programming? It was supposed to be a revolution in safety engineering. Everybody thought it was obviously a good idea, I mean, just think about it! Then Nancy Leveson killed it with [empirical studies](http://sunnyday.mit.edu/papers.html#ft).


Basing decisions on research and evidence is known as **Empirical Software Engineering**, alternatively “Evidence-Based Software Engineering”. We use our reason and experience to guide what we choose to investigate, but ultimately trust the data over our own experiences. It’s a surprisingly small field and unknown in the wider industry, but I think it’s the only way we’re going to get actual answers to these questions.


PS: There’s some interesting work done on empirical evaluation of static vs dynamic typing, but again, I’m not listing it here because this is not a type systems post.


---

1. Necessary disclaimer: *this post is not about static vs dynamic typing*. I’m not taking any position on it here. I’m just using it as an example because the system impacts get particularly complicated.
 [return]
2. Software correctness isn’t quite the same thing as bugginess: you can make software more correct without making it less buggy, and vice versa. But the difference is subtle and deserves its own post.
 [return]
