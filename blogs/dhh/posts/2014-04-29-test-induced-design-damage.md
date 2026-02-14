---
title: "Test-induced design damage"
date: 2014-04-29
url: https://dhh.dk/2014/test-induced-design-damage.html
slug: test-induced-design-damage
word_count: 1413
---


"Code that's hard to test in isolation is poorly designed", goes a common TDD maxim. Isolation meaning free of dependent context and separated from collaborators, especially "slow" ones like database or file IO. The prevalent definition of "unit" in unit testing (though not everyone agrees with this).


This is some times true. Some times finding it difficult to test points to a design smell. It may be tangled responsibilities or whatever. But that's a far ways off from declaring that hard-to-unit-test code is always poorly designed, and always in need of repair. That you cannot have well-designed code that is hard to unit test.


It's from this unfortunate maxim that much of the test-induced design damage flows. Such damage is defined as changes to your code that either facilitates a) easier test-first, b) speedy tests, or c) unit tests, but does so by harming the clarity of the code through — usually through needless indirection and conceptual overhead. Code that is warped out of shape solely to accomodate testing objectives.


Faithful TDD'ers will reject the mere suggestion that this is possible. A true believer sees only good coming from the above-mentioned concessions to testing. It's under this cloud of judgment that TDD has been rammed down people's throats as the savior of professional programming. And it's under this regime that the current "TDD is dead" uprising is bred.


I think part of why we've been able to go so long with only murmurs of a debate about the value of TDD as a design principle, is post hoc rationalization. If you accept the premise that red-green-refactor is the true guiding light for all programming design, any sacrifices on its altar seem trivial. Who cares if you need two or three extra layers of indirection to unit test a controller? OF COURSE it's worth it.

**Hexagonal design damage**

A good illustration of this is the late Jim Weirich's [demonstration of the hexagonal architecture in Rails](https://www.youtube.com/watch?v=tg5RFeSfBM4). This presentation shows the fundamentals of the "decoupling from Rails" approach, without necessarily buying into it wholeheartedly as a general purpose approach (Jim was a pragmatic programmer, and I miss him dearly).


While you're watching the presentation, listen to the justifications for the design. They're all about testing! It's about having faster tests, without touching the database, and it's about being able to test controller logic without dependent context.


To achieve this, the simple controller is forbidden from talking directly to Active Record, now it has to go through the Repository. And the action itself is hollowed out to extract a Command object, which then has to call back into the controller through the Listener pattern.
This is not better.
The code has suffered tremendous design damage to achieve two testing goals: Faster tests and easy-to-mock unit tested controllers. This is the same rationalization that flows through other attempts to create boundaries between "your application" and Rails, as proponents of such divisions like to frame it.
The [hexagonal design pattern](http://alistair.cockburn.us/Hexagonal+architecture) is in itself not to blame. There may well be proper uses for it outside the domain of web apps. Maybe if you're making a system with regular GUI interfaces or voice controlling or whatever, where these cannot just go through a web API, you truly have the web interface as just one adapter amongst many on equal terms.
But that's not what's being sold. The hexagonal pattern is being misapplied to Rails applications, alongside it companions of boundaries and ports'n'adapter-like patterns, for the purpose of testing. This is test-driven pattern application.
The same is true for the other patterns enlisted to make this happen. Hiding access to Active Records behind a Repository serves only as a way to disconnect the application from the database for "fast test" purposes. It does not clarify the design of the application itself. If you did not look or care about the tests, you wouldn't look at the "after code" and say "BETTER!".
**Getting away from the "unit tests are best" mantra**
One conclusion of this is that I think it's a mistake to try to unit test controllers in Rails (or similar MVC setups). The purpose of the controller is to *integrate* the requests from the user with the response from the models within the context of session.
Mocking all that away to test just whether it'll send this redirect or that notice doesn't make the least bit of sense to me. Controllers are meant to be integration tested, not unit tested. But the testing pyramid prescribes that the unit level is where the focus should be, so people are sucked into that by default.
I think it's equally folly to unit test the view, which is a motivation that's driving a lot of interest in Presenters (though they too have occasional legitimate uses). The view is at the top layer of the MVC cake, the appropriate testing metaphor for the vast bulk of that is system testing: End-to-end.
Finally, the fear of letting model tests talk to the database is outdated. This decoupling is simply not worth it any more, even if it may once have been. Rails now runs a persistent console process, so Jim's example of the 1.2s overhead to booting the framework to run a unit test is gone. Additionally, the love-to-hate use of test fixtures within a test case transaction wrapping, also makes those tests incredibly fast to run (I'll do a separate post on "Effective test fixtures" soon).
If between those two turbos you're still having overly slow model tests, maybe you're simply [testing like the TSA](http://signalvnoise.com/posts/3159-testing-like-the-tsa). Could you delete some redundant or anemic tests? Probably. Just like your general code base, your testing base needs regular pruning too.
At this point BDD proponents might well argue that, yes, testing units is not what we should be doing. We should be going outside-in. But as long as that's also done under the test-first regime, I don't think it generally helps matters much. It still leads down a road of excessive mocking and artificial boundary installations. At least as far as I've seen its usage in the wild. (Although I am in general far more sympathetic to the goals of BDD).
The bottom line for Rails/MVC testing is imo this: 
Test models with intricate logic through model tests, but don't bother trying to separate them from the database. Use the power of testing fixtures and the case-transaction loop to avoid having to do expensive and excessive setup work for every case, and merely tailor your prototypical fixtures to the case at hand by changing the single state needed. (More on this technique in that promised future post).
Test controllers using integration tests. Don't even try to make it fit under the unit testing paradigm. Resist the urge to extract session logic, like checking permissions, or auxiliary views, [like emails](https://dhh.dk/2012/emails-are-views.html), into a command object just so you can mock boundaries and have "fast tests". It's skinny controllers, not anemic controllers, we're looking for. And private methods on controllers are not evil.
Test views through system/browser testing. This is particularly true if your view is powered in part by JavaScript. You have to make sure that all that stuff works too.
But the most important part is where to place the emphasis. If you have a very simple model layer, but your UI is complex, then you should indeed be system-test heavy, and model-test light! This is not a sin. If your controllers do very little interesting work, maybe you don't need to test drive them at all, if you're covered by the system tests. And if you hardly have any JavaScript of note, maybe integration tests are actually the place to be.
Above all, you do not let your tests drive your design, you let your design drive your tests! The design is going to point you in the right direction of what layer in the MVC cake should get the most test frosting.
When you stop driving your design first, and primarily, through your tests, your eyes will open to much more interesting perspectives on the code. The answer to how can I make it better, is how can I make it clearer, not how can I test it faster or more isolated.
The design integrity of your system is far more important than being able to test it any particular layer. Stop obsessing about unit tests, embrace backfilling of tests when you're happy with the design, and strive for overall system clarity as your principle pursuit.

