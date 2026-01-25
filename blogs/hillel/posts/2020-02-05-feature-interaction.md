---
title: "Feature Interaction Bugs"
date: 2020-02-05
url: https://www.hillelwayne.com/post/feature-interaction/
slug: feature-interaction
word_count: 2816
---

In most testing frameworks, you’re expected to write a lot of low-level tests and few high-level tests. The reasoning is that end-to-end tests are slow and expensive and only cover a tiny amount of the program’s state space. It’s better to focus on testing all the parts in isolation versus testing that they all work together.


In practice, global correctness does not follow from local correctness. It’s possible for every part to be individually rock-solid but the system to be broken as a whole. One way this happens is with **feature interaction** (FI) bugs, where different features combine to break global properties.


## Example


*The TLA+ code snippets are supplementary: knowing TLA+ is not necessary to understand the example.*


At SoupOn we want to add a “track your soups” feature, which means people will need to register an account. At a high level, an account is representable by an email address. A given user starts with no account and gets one by registering.


```
CONSTANTS NULL, Addresses, AllStrings
VARIABLES account

vars == \* all our variables

Init ==
  /\ account = NULL

RegisterWith(addr)
  /\ account = NULL
  /\ account' = [
    address |-> addr
  ]

Next ==
  \/ \E s \in AllStrings:
    \/ RegisterWith(s)

Spec == Init /\ [][Next]_vars

```


We find that a lot of people register with the email address “asdljg”. We need to confirm that they register with a valid email address that they control. To do this, we require people validate their account. After they sign up, we send an email to their provided address.


```
- VARIABLES account
+ VARIABLES account, sent_validate_msg_to


Init ==
  /\ account = NULL
+ /\ sent_validate_msg_to = NULL

+ Some(a) = a /= NULL

+ SendValidateMsg ==
+   IF Some(account)
+   THEN sent_validate_msg_to' = account.address
+   ELSE UNCHANGED sent_validate_msg_to

RegisterWith(addr)
  /\ account = NULL
  /\ account' = [
    address |-> addr
+ , verified |-> FALSE  
  ]
+ /\ sent_validate_msg_to' = addr

```


If it’s a valid email (and they control it), they will be able to click the link in it to validate their account. We guarantee it’s a valid email by only allowing the user to take a `ConfirmValidate` action with an email address.1


```
ConfirmValidate(addr) ==
  /\ Some(sent_validate_msg_to)
  /\ addr = sent_validate_msg_to
  /\ addr = account.address
  /\ account' = [account EXCEPT !.verified = TRUE]
  /\ UNCHANGED sent_validate_msg_to

```


```
Next ==
  \/ \E s \in AllStrings:
    \/ RegisterWith(s)
+ \/ \E a \in Addresses:
+   \/ ConfirmValidate(a)

```


Next problem: anonymous email addresses. Some users register with throwaway domains, like `teleworm` or `yosmail` or whatnot. On these sites, they can give any string of characters and immediately get an email address, no hoops required. Some people value this, because it gives them anonymity. But we also see that many people are signing up with these emails to order to spam people. We want to ensure that you can only validate with a non-anonymous email. It’s okay if you later change to one, because then we know that you verified a real email first.


```
Spec == Init /\ [][Next]_vars
NoSpammers == [][~\E spam \in SpammerAddresses: ConfirmValidate(spam)]_vars
PROPERTY Spec => NoSpammers

```


We decide to enforce this at registration: if you try to register with a spammer address, we don’t even bother to let you try to validate.


```
- CONSTANTS NULL, Addresses, AllStrings
+ CONSTANTS NULL, Addresses, SpammerAddresses, AllStrings

RegisterWith(addr) ==
+ /\ addr \in AllStrings \ SpammerAddresses
  /\ account = NULL
  /\ account' = [
      address |-> addr,
      verified |-> FALSE
     ]
     
  /\ SendValidateMsg

\* ...

Spec == Init /\ [][Next]_vars
NoSpammers == [][~\E spam \in SpammerAddresses: ConfirmValidate(spam)]_vars
PROPERTY Spec => NoSpammers

```


Speaking of changing emails, let’s put that in. We want to prevent them from fat-fingering an address they don’t control. They need to confirm that their new email address is what they changed it to.


```
- VARIABLES account, sent_validate_msg_to
+ VARIABLES account, sent_validate_msg_to, sent_change_msg_to

TypeInvariant ==
  /\ account \in Accounts \union NULL
  /\ sent_validate_msg_to \in Addresses \union NULL
+ /\ sent_change_msg_to \in Addresses \union NULL

Init ==
  /\ account = NULL
  /\ sent_validate_msg_to = NULL
+ /\ sent_change_msg_to = NULL

+ ChangeTo(addr) ==
+   /\ Some(account)
+   /\ sent_change_msg_to' = addr
+   /\ UNCHANGED <<account, sent_validate_msg_to>> 

+ ConfirmChange(addr) ==
+   /\ Some(sent_change_msg_to)
+   /\ addr = sent_change_msg_to
+   /\ account' = [account EXCEPT !.address = addr]

+ ConfirmFor(a) ==
+   /\ Some(account)
+   /\ \/ ConfirmValidate(a)
+      \/ ConfirmChange(a)
+   /\ UNCHANGED <<sent_validate_msg_to, sent_change_msg_to>>

Next ==
  \/ \E s \in AllStrings:
    \/ RegisterWith(s)
+   \/ ChangeTo(s)
  \/ \E a \in Addresses:
-   \/ ConfirmValidate(a)
+   \/ ConfirmFor(a)

```


After a while, we find a new issue. Our email server is a box in the kitchen. Sometimes someone mistakes it for the microwave and pours their SoupOn all over it, frazzing the database. If this happens, people might not receive the activation email. So we need a “resend email feature”:


```
Next ==
  \/ \E s \in AllStrings:
    \/ RegisterWith(s)
    \/ ChangeTo(s)
+ \/ SendValidateMsg /\ UNCHANGED <<account, sent_change_msg_to>>

```


It takes us a year to discover that people are signing up with spammer emails again. However, the feature works: trying to sign up with `example@teleworm.us` still gives an error. The bug is a little more roundabout:

1. The spammer signs up with a regular email address, like “normal@person.here”. A confirmation email is send to this address.
2. They change their email to “spammer@teleworm.us”.
3. They click “resend confirmation”. A new confirmation email is sent to their spammer address.
4. They validate.


Where’s the root cause? The registration is working fine, so it’s not there. The “change email” is fine, since part of our requirements are that people can switch to anonymous emails. If the problem’s in the email verification, then we need to check for spammer accounts in two locations. That makes it likely they’ll fall out of sync over time, leading to more subtle issues in the future.


We can argue about which aspects should validate this. But there’s deeper issues here. There’s two features that cause this problem: resending confirmation emails, and changing the user email. If we remove just the resending feature then our system starts working again. If we remove just the changing email feature, our system still works. But with both of them in we have a bug.2


No part of our system is *obviously* broken. All of our unit tests pass. It’s only when the different parts combine does the bug emerge that’s not localizable to just one part failing. This is a feature interaction bug.


## Feature Interaction


Pamela Zave pioneered FI while working at AT&T. [In her words](http://www.pamelazave.com/faq.html):


> A feature interaction is some way in which a feature or features modify or influence another feature in defining overall system behavior. […] feature interactions have been a notorious source of runaway complexity, software bugs, cost and schedule overruns, and unfortunate user experiences.


FI bugs are especially insidious because they don’t map to any isolated components. The violated invariant is global or occurs in temporally-disconnected parts of the code.


The above example is a banal one, since there’s an obvious invariant that’s violated. Often, feature interaction happens when various requirements conflict. Consider the requirements

1. “If A forwards to B, then if somebody calls A, they receive B.”
2. “If someone calls B and B has Do Not Call enabled, then the call is dropped”.


So if a call to A is forwarded to B, should it go through or be dropped? This is something for the stakeholder to figure out. But to ask them, you need to realize that this could be a problem. And that “realizing” is where all the trouble lies. Because feature interaction is a global, emergent behavior of local software, it’s not something you can see while working at the feature level. You have to zoom out and see the behaviors of the system to see the hazard.


Safety and security concerns are especially vulnerable to FI, as there’s often no obviously-incorrect prior state. The system looks like it’s working fine up until the point that everything catches fire.


### Why feature interaction happens


FI is a measure of essential complexity: the more requirements you have, the more ways two requirements can conflict with each other. This also means that FI is more common in business domains than technical domains, as they are more likely to have edge cases and conflicting requirements.


That’s only a measure of how much FI is possible. A few things make projects more likely to actually have FI bugs in practice. One is poor communication. Consider an FI bug across two services. If the respective teams don’t communicate with each other, they won’t notice any potential problems with the interactions of their services. This also causes **boundary error**, where two groups each assume the other is responsible for the integration. Then nobody is paying attention to the integration and bugs freely happen.3


FI is more common when requirements are ambiguous or constantly changing. Customers “think locally” about changes to the system. They’re not thinking about how feature X would interact with something you implemented six weeks ago. This means that Agile teams have to be especially watchful for FI, as their highly iterative development style leaves a lot of space for cross-sprint bugs.


## Solving Feature Interaction


Sorry, you’re doomed.


There are two problems with detecting FI. First, since FI is a global property, unit tests cannot find feature interactions nor can they validate that you’ve solved them. We have to look at end-to-end behavior traces. This is a huge state space, though, and E2E tests can only cover a fraction of the space. Second, FI bugs are not “obvious” failures, in that they may not correspond to raised errors or corrupted data. The system still looks like it’s working fine even if there’s a FI bug. Most automated testing assumes you know what you want to test, meaning you have to come up with each case in advance.


This is an essential problem with implementation-level verification. We test locally out of necessity. It’s easier for us to reason about how small pieces of code work, it’s easier to connect failures to the errors, and it’s easier to come up with what an “error” is. The price for working at the machine level is that we are restricted to what we can express at the machine level. While something like “We never validate an anonymous address” is easy to express as a human requirement, we cannot express the general property to the machine. At best, we can express “this block of code, which accepts a valid email address, will not accept an anonymous address”. But we struggle to say “this is the only block of code involved with validation”.4


“This block of code will not accept an anonymous address” is only what we are aiming to implement. When it comes to actually validating, we can say even less. All a unit test can say is “this rejects this anonymous address when called with these parameters.” All an end-to-end test says is “this specific instance of this user action, if it eventually triggers this block of code, will cause it to reject this anonymous address.” Neither makes FI safe: knowing that `X` is safe for the codepath `A -> B -> C -> X` does not mean it’s safe for the codepath `A -> F -> G -> X`.


This is all assuming you can partially translate the requirement in the first place. You need to know the requirement and be able to localize it to a specific module in your code. If the property is broader or more vague, this becomes far more difficult, which makes finding FI that much harder.


### Coping with Feature Interaction


While we can’t trivialize FI bugs, there are some things we can do to make them more manageable.


The first is detecting potential FI issues earlier via better requirements gathering. The problem with the signup page happened because features were gradually added in stages, to address immediate needs. If we started the project by specifying “we need to 1) block spam email addresses, 2) resend verification emails, and 3) allow people to change their email address before validating”, there’s a good chance someone would have noticed the FI bug. This approach is the requirements equivalent of code review and has similar tradeoffs: it is very effective, it works best with domain experts, and it won’t catch everything.


The second is having a specification of any kind. If you don’t have designs, blueprints, or documentation, you have no way of knowing whether the observed system behavior is intended or not. Remember, many FI bugs aren’t obviously incorrect. In many cases an observed FI could be the actual intended behavior that satisfies the stakeholder’s needs. But to tell that, we need to know what those needs are in the first place.


Those two take care of the basics. Past that, Zave recommends two additional techniques.


While any kind of specification is better than no specification at all, some forms of spec are better than others. Some specs are formalized, meaning we can test them directly for FI bugs. Unlike with testing code, testing the spec works at the global level. For example, we can run a model checker on the email spec to immediately see the bug:


Show Trace
  
`Error: Action property NoSpammers is violated.
Error: The behavior up to this point is:
State 1: <Initial predicate>
/\ change_msg = NULL
/\ account = NULL
/\ verify_msg = NULL

State 2: <RegisterWith line 40, col 3 to line 48, col 25 of module Registration>
/\ change_msg = NULL
/\ account = [address |-> d, verified |-> FALSE]
/\ verify_msg = NULL

State 3: <ChangeTo line 35, col 3 to line 37, col 38 of module Registration>
/\ change_msg = b
/\ account = [address |-> d, verified |-> FALSE]
/\ verify_msg = NULL

State 4: <ConfirmFor line 63, col 3 to line 66, col 41 of module Registration>
/\ change_msg = b
/\ account = [address |-> b, verified |-> FALSE]
/\ verify_msg = NULL

State 5: <ChangeTo line 35, col 3 to line 37, col 38 of module Registration>
/\ change_msg = a
/\ account = [address |-> b, verified |-> FALSE]
/\ verify_msg = NULL

State 6: <Next line 72, col 6 to line 72, col 55 of module Registration>
/\ change_msg = a
/\ account = [address |-> b, verified |-> FALSE]
/\ verify_msg = b

State 7: <ConfirmFor line 63, col 3 to line 66, col 41 of module Registration>
/\ change_msg = a
/\ account = [address |-> b, verified |-> TRUE]
/\ verify_msg = b
`

show all


I wrote the spec in TLA+; the FI community generally prefers [Alloy](http://alloytools.org/). Zave used Alloy to [break the Chord protocol](http://www.pamelazave.com/chord.html) and to verify large telecomm systems.


Finally, we can architect our system with FI in mind, choosing a foundation which naturally isolates and localizes requirements. Pamela Zave and Michael “not the singer” Jackson designed a telecommunications architecture called [Distributed Feature Composition](http://www.pamelazave.com/dfc.html). While they claim it’s very effective, I haven’t seen anybody adapt it outside of telecomms. And I’ll admit I don’t fully understand it myself. Nonetheless it’s worth looking into.


Even though tools and processes help, they only work in the context of domain knowledge. Ultimately, dealing with FI bugs is a process of looping domain experts into your development process, keeping everyone in constant communication, and constantly reevaluating how local changes affect the big picture. It’s a technical problem with a social solution.


If you’re interested in reading more about FI, Zave has a good page [here](http://www.pamelazave.com/faq.html). Michael Jackson talks about this in his book [Problem Frames](https://www.amazon.com/Problem-Frames-Analysing-Structuring-Development/dp/020159627X). You can also look at research in the field of emergence and systems-thinking; my favorite book on this is [Engineering a Safer World](https://mitpress.mit.edu/books/engineering-safer-world), which approaches FI as a subtopic in general systems safety.


*If you’re interested in using better methods, I teach workshops! Formal specs save money and reduce time-to-market by catching FI bugs early. You can read more [here](https://www.hillelwayne.com/consulting/) and contact me [here](mailto:consulting@hillelwayne.com).*


*Thanks to [Kevin Riggle](https://free-dissociation.com/) and [Richard Whaling](http://twitter.com/richardwhaling) for feedback.*


---

1. “What if they don’t own that email address?” That’s something we could choose to model, but for the purposes of this problem it’s outside the space we care about.
 [return]
2. “In the real world they’d obviously do X instead!” But they didn’t. This is a real bug I found in a large tech product.
 [return]
3. Boundary error comes from Nancy Leveson’s work on STAMP. STAMP is a model for building safe systems, which includes feature interaction. I’ve written more about STAMP [here](https://www.hillelwayne.com/post/stamping-on-eventstream/).
 [return]
4. The big exception is database constraints. We can say “all data in the database must have these properties”. But this doesn’t work for everything, and it doesn’t work if we have multiple databases.
 [return]
