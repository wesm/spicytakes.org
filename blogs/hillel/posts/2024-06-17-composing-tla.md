---
title: "Composing TLA+ Specifications with State Machines"
date: 2024-06-17
url: https://www.hillelwayne.com/post/composing-tla/
slug: composing-tla
word_count: 3523
---

Last year a client asked me to solve a problem: they wanted to be able to compose two large TLA+ specs as part of a larger system. Normally you’re [not supposed to do this](https://www.hillelwayne.com/post/spec-composition/) and instead write one large spec with both systems hardcoded in, but these specs were *enormous* and had many internal invariants of their own. They needed a way to develop the two specs independently and then integrate them with minimal overhead.


This is what I came up with. Warning: this is a complex solution is aimed at advanced TLA+ users. For a much (much) gentler introduction, check out my website [learntla](https://learntla.com/).


## The example


Let’s start by giving a motivating system:
a **Worker** sends an authentication request to a **Server**. If the password matches the server’s internal password, the server responds “valid”, otherwise it responds “invalid”. If the worker receives “invalid” as a response, it goes into an error state. The worker can retry from that state and submit a new authentication request.


The worker and server have shared state via the request/response. As an additional complication, we’ll add internal state to the server, in the form of a request log that is hidden from the worker.


We can use this example to show the problems of composition and my solution (though I’ll say the example is a little too simple to make it worthwhile).


### The problem with composition


What we *want* is for the composition to be as simple and painless as possible. If our specs are `WorkerSpec` and `ServerSpec`, the easiest composition would just be


```
CombinedSpec == WorkerSpec /\ ServerSpec

```


I talk about the problems we have in-depth [here](https://www.hillelwayne.com/post/spec-composition/), but the gist is that if `ServerSpec` and `WorkerSpec` are “normal” specs, they’ll place contradictory constraints on the shared variables.


For example, `WorkerSpec` will likely read the server response, but not modify it. So to run `WorkerSpec` independently of the composition, we have to say the response never changes, which is equivalent to saying we *can’t* change it, which makes it impossible for `ServerSpec` to send a response!


The normal way around this is to break apart both `WorkerSpec` and `ServerSpec` into collections of actions, and then carefully stitch them together in non-contradictory ways. Which is about as complex as it sounds: composing two specs can be as much work as writing them in the first place.


This is why I’m trying to find a better way.


### The big idea


What we need to do is write specs intended to represent *part* of the world and then incorporate them into a “whole world” main spec. To do this, we’ll use one of TLA+’s most powerful features: we can use `x'` to both *assign the next value to x* and *constrain what the next value can be.* Say we have


```
VARIABLE x, y 

Foo == 
  /\ x' \in {0, 1}
  /\ y' \in {0, 1}

Bar == x' < y'

Next == Foo /\ Bar

```


When TLC
 evaluates `Next`, it reads `x'` and `y'` in `Foo` as *assignments*. There are four possible assignments, so the model checker evaluates them all.


Then, since `x'` and `y'` are already chosen, TLC reads the statement in `Bar` as a *constraint*. Three of the possible assignments break that constraint, so TLC eliminates those possibilities, leaving us with a unique next state.


This means that a Spec Q can take two specs, X and Y, and *constrain* them against each other. X can have an action `Inc` that increments `x_log`, and then Q says that `Inc` can only happen if `y_flag` is true. Similarly, Q can make one assignment trigger another:


```
Inc == 
  /\ x_log' = x_log + 1

Sync ==
  IF ~y_flag /\ y_flag' 
  THEN Inc 
  ELSE TRUE

Next == (X!Next \/ Y!Next) /\ Sync

```


Now, changing `y_flag` to true *forces* an increment in `x_log`. Q is using one spec to drive side-effects in the system.


This is just a state machine! Constraints on transitions are just [guard clauses](https://en.wikipedia.org/wiki/Guard_(computer_science)) and assignments on transitions are just effects. These can be enforced on *other specifications* that the state machine doesn’t know about.


Here’s how to make this idea work in practice:

1. Write an abstract state machine for all of the high-level state transitions of the core component
2. Write the other components as “open” specs that don’t fully describe their next states.
3. [Refine](https://www.hillelwayne.com/post/refinement/) the core component into the main spec, with a `Sync` action that adds guards and side-effects to the state transitions.


## The Solution


We’ll model this with three separate specs: `workerSM.tla`, `server.tla`, and `system.tla`.


### The state machine


Since the whole system is based around the worker’s state machine, let’s start with `workerSM.tla`. This won’t represent what *happens* when the worker transitions states, just what the transitions are.


```
------------------- MODULE workerSM -------------------
EXTENDS Integers

VARIABLES state

Transitions == {
    [from |-> "init", to |-> "ready"]
    , [from |-> "ready", to |-> "requesting"]
    , [from |-> "requesting", to |-> "done"]
    , [from |-> "requesting", to |-> "error"]
    , [from |-> "error", to |-> "ready"]
}

Init == state = "init"

Valid(t) == state = t.from
ValidTransitions == {t \in Transitions: Valid(t)}
ValidOutcomes == {t.to : t \in ValidTransitions}

Done ==
    state = "done"

Next ==
    \E t \in ValidOutcomes:
        state' = t

Fairness == 
    /\ WF_state(Next)
    /\ SF_state(state' = "done")

Spec == Init /\ [][Next]_state /\ Fairness
Liveness == <>Done

=========================================================

```


`Transitions` represents the set of valid transitions. The three `Valid-` operators are just helpers. Adding them is good practice; most TLA+ specs don’t have enough helpers.


The `Fairness` constraint is a little complex, but all it’s saying is that we can’t *always* transition from `requesting` to `error`. If we get there often enough, we’ll eventually transition to `done` instead.


Otherwise this spec doesn’t put any conditions on the transfers: we don’t need to “do anything” to go to `done`. That’s what `system.tla` is for.


show cfg
  
I used this to directly test the worker.
`SPECIFICATION Spec

PROPERTY Liveness
CHECK_DEADLOCK FALSE
`
It passes, meaning this spec guarantees `<>Done`.

show all


Next, the outside component we’ll integrate with the worker.


### The server


```
------------------- MODULE server -------------------
CONSTANTS Password, NULL

VARIABLE req, resp, log

internal == <<log>>             \* (a)
external == <<req, resp>>       \* (a)
vars == <<external, internal>>  \* (a)

Init == 
    /\ req = NULL
    /\ resp = NULL
    /\ log = {}

CheckRequest ==
    /\ req # NULL
    /\ log' = log \union {req}
    /\ IF req = Password THEN
         resp' = "valid"
       ELSE
         resp' = "invalid"
    /\ req' = NULL

Next == \* (b) 
  CheckRequest

Spec == Init /\ [][Next]_internal \* (c)
====

```


We’re doing three unusual things in this spec. First is that we split the variables into `internal` and `external` vars **(a)**. External vars represent state that’s shared with other parts of the composed specification, while internal only pertains to the `server`’s properties. Here we represent requests to the server with `req` and responses with `resp`.


Second, the spec will trivially deadlock **(b)**. `Next` only contains the `CheckRequest` action, `CheckRequest` is only enabled if `req` isn’t null, but nothing in the spec makes `req` not-null. This spec isn’t “self-contained”, and it needs to be used by another specification to be meaningful.


Third, Spec is only stuttering invariant with respect to `internal` variables. This is done by writing `[][Next]_internal` instead of `[][Next]_vars` **(c)**. This is the easiest part to miss but will make both spec composition and spec refinement easier down the line.


Now let’s put the server and the worker together.


### The system


This is by far the most complex part. Let’s start with the whole spec, and then cover a breakdown of the most important sections.


system spec
  
`---- MODULE system ----
EXTENDS TLC, Integers, Sequences
CONSTANT NULL
VARIABLES ws \* worker state
 , server_req \* requests to server
 , server_resp \* server response
 , server_log \* log (internal to server)

Strings == {"a", "b", "c"}

comm_vars == <<server_req, server_resp>>
vars == <<ws, server_log, comm_vars>>

Worker == INSTANCE workerSM WITH state <- ws

Server == INSTANCE server WITH 
  req <- server_req,
  resp <- server_resp,
  log <- server_log,
  Password <- "a"

Sync ==
    LET i == <<ws, ws'>> IN
    /\ CASE
            i = <<"ready", "requesting">> ->
            /\ \E x \in Strings:
                /\ server_req' = x
            /\ server_resp' = NULL
        []  i = <<"requesting", "error">> ->
            /\ server_resp = "invalid"
            /\ UNCHANGED comm_vars
        []  i = <<"requesting", "done">> ->
            /\ server_resp = "valid"
            /\ UNCHANGED comm_vars
        [] OTHER -> UNCHANGED comm_vars

Init ==
    /\ Worker!Init
    /\ Server!Init

Done == \* No deadlock on finish
    /\ Worker!Done
    /\ UNCHANGED vars

ServerNext ==
    /\ Server!Next
    /\ UNCHANGED ws

WorkerNext ==
    /\ Worker!Next
    /\ Sync
    /\ UNCHANGED server_log

Next == 
    \/ WorkerNext
    \/ ServerNext
    \/ Done

Fairness == 
    /\ WF_vars(Next) 

Spec == Init /\ [][Next]_vars /\ Fairness 

RefinesServer == Server!Spec
RefinesWorker == Worker!Spec

====
`

show all


```
VARIABLES ws \* worker state
 , server_req \* requests to server
 , server_resp \* server response
 , server_log \* log (internal to server)

Strings == {"a", "b", "c"}

comm_vars == <<server_req, server_resp>>
vars == <<ws, server_log, comm_vars>>

```


I like to group my `vars` by purpose and spec. Since both the server and the worker use `server_req` and `_resp`, I put them in a separate `comm_vars` grouping.


```
Worker == INSTANCE workerSM WITH state <- ws

Server == INSTANCE server WITH 
  req <- server_req,
  resp <- server_resp,
  log <- server_log,
  Password <- "a"

```


I hard-coded the server’s `Password` constant for pedagogical convenience. We don’t have to instantiate the `NULL` constant because it’s the same name in both `system.tla` and `server.tla`, so it propagates automatically.


```
Sync ==
  \* See next section

Init ==
    /\ Worker!Init
    /\ Server!Init

ServerNext ==
    /\ Server!Next
    /\ UNCHANGED ws

WorkerNext ==
    /\ Worker!Next
    /\ Sync
    /\ UNCHANGED server_log

Done == \* No deadlock on finish
    /\ Worker!Done
    /\ UNCHANGED vars

Next == 
    \/ WorkerNext
    \/ ServerNext
    \/ Done

```

- `Init` just shells out to both `Worker!Init` and `Server!Init` to set up their respective variables. It’s easy here because they don’t share any variables. *If* there was something that they both used or if `system` needed any extra booking variables, I’d handle them specially here.
- `ServerNext` just says “the server can handle its own state updates”, but accounts for `ws` stuttering (because every variable needs to be assigned a value on every step). The server is independently active in the system and its behavior doesn’t synchronously depend on the worker. Keeping the components separate isn’t always possible when composing, but it makes things more convenient when applicable.
- `WorkerNext` is the same: it behaves independently of `ServerNext`. But here’s where the “system” starts to play a role, in `Sync`.


#### Sync


`Sync` is where things get interesting.


```
Sync ==
    LET i == <<ws, ws'>> IN
    CASE
          i = <<"ready", "requesting">> ->
          /\ \E x \in Strings:
              server_req' = x
          /\ server_resp' = NULL
      []  i = <<"requesting", "error">> ->
          /\ server_resp = "invalid"
          /\ UNCHANGED comm_vars
      []  i = <<"requesting", "done">> ->
          /\ server_resp = "valid"
          /\ UNCHANGED comm_vars
      [] OTHER -> UNCHANGED comm_vars

```


To recap the earlier explanation, primed variables can be used in other expressions after being assigned. This means we can attempt a transition in one action and then check if the transition is valid in a later action. **This is the key to making this all work.** Without this, we’d have to put the guards and side effects in the same action as the transitions. For example, in this line:


```
      []  i = <<"requesting", "error">> ->
          /\ server_resp = "invalid"
          /\ UNCHANGED comm_vars

```


We are constraining the `requesting -> error` transition to only be possible *if* the server response was “invalid”. That’s only possible if `Server!Next` rejected the password. But *our worker doesn’t need to know this*. We can develop them independently and rely on the `Sync` to correctly compose their behaviors.


We can also use this to drive effects on the system:


```
      []  i = <<"ready", "requesting">> ->
          /\ \E x \in Strings:
              server_req' = x
          /\ server_resp' = NULL

```


This makes a `ready -> requesting` transition also trigger a request (and clear any outstanding response). This then enables `Server!CheckRequest`, which enables `ServerNext`, so the server can react to the system.


### Refinements


Remember, we added all of this machinery in first place in order to compose two complex specifications together. We need to make sure we’re composing them in a way that doesn’t violate either of their own properties. That’s handled by these lines:


```
RefinesServer == Server!Spec
RefinesWorker == Worker!Spec

```


These are [refinement properties](https://www.hillelwayne.com/post/refinement/). At a high level, these check that `system.tla` doesn’t make the `Server` or `Worker` do anything they’re not normally able to do. For example, this property would fail if we removed something from `log`, since that’s not possible in `Server!Spec`. 1


In TLA+, **refinements are transitive**. `workerSM.tla` had the [liveness property](https://www.hillelwayne.com/post/safety-and-liveness/) `<>Done`. Since I already verified it in `workerSM.cfg`, I don’t need to test it in `system.tla`. If `RefinesWorker` passes, then `Worker!Liveness` is guaranteed to pass, too!


Why refinement is transitive
  
When we test `RefinesWorker`, what we’re verifying is
`Spec => Worker!Spec 
(S)     (WS)
`
We already know from model checking `workerSM.tla` that
`Worker!Spec => Worker!Liveness (2)
(WS)           (WL)
`
Implication is transitive: if `S => WS` and `WS => WL`, then `S => WL`.

show all


And currently it *fails*:


show cfg
  
`SPECIFICATION  Spec

CONSTANTS
  NULL = NULL

PROPERTY
    RefinesServer
    RefinesWorker
`

show all


The problem is that the worker can keep picking the wrong password, so the server keeps rejecting it and the worker never completes. One fix is to say the system never retries the same password:


```
Sync ==
    \* ...
            /\ \E x \in Strings:
+               /\ x \notin server_log
                /\ server_req' = x

```


This makes the spec pass. If you’re concerned about leaking the server’s internal log to the system, you can add a log to the worker, too, either in `system.tla` or in a separate component that you include in the `Sync`.2 An alternative fix uses a [strong fairness constraint](https://www.hillelwayne.com/post/fairness/):


```
Sync ==
    \* ...
            /\ \E x \in Strings:
-               /\ x \notin server_log
                /\ server_req' = x

Fairness == 
    /\ WF_vars(Next) 
+   /\ SF_vars(WorkerNext /\ server_req' = "a")

```


This says that if it’s always-eventually possible to execute `WorkerNext` in a way that sends the right password, the spec eventually will. This makes the spec pass without changing the essential logic of the system.


### Closing the open world


One last thing we need to do: make `server.tla` model-checkable. We can’t test it directly because it’s not a “closed” specification: it relies on some other spec to send requests. For more complex specs we want to be able to test that spec’s properties independently of the composition.


Fortunately, this is an “already solved problem” in the TLA+ community: refine the open spec into a closed one. We do this with a new file `MCserver.tla`:


```
---- MODULE MCserver ----
EXTENDS TLC, server

Strings == {"a", "b", "c"}
ASSUME Password \in Strings

MCInit == Init

WorldNext ==
    /\ \E x \in Strings:
        req' = x
    /\ UNCHANGED <<log, resp>>

MCNext ==
    \/ Next
    \/ WorldNext

MCSpec == MCInit /\ [][MCNext]_vars
====

```


This augments the server with an external `World` that can send requests. Now we can test the behavior of `server.tla` by model checking `MCserver.tla`.


show cfg
  
`SPECIFICATION MCSpec
CONSTANT 
    NULL = NULL
    Password = "b"
`

show all


If you’re on the VSCode TLA+ extension nightly, running the “Check model with TLC” command on `server.tla` will automatically run the model checker with `MCserver.tla`. It also comes with a TLA+ debugger. The VSCode extension is great.


## Advantages and Drawbacks


This is a lot of work! So why do this instead writing one large spec?


The point of composing specs at all is so we can work on them independently. It’s not a big deal when each spec is ~30 lines, but when they’re each 200+ lines, you can’t just rewrite them as one spec.


So let’s compare it to a more conventional approach to composition. I’ll use the [MongoDB Raft composition](https://github.com/will62794/logless-reconfig), which [Murat Demirbas analyzes here](https://muratbuffalo.blogspot.com/2024/02/tla-modeling-of-mongodb-logless.html). The independent specs are  [MongoStaticRaft](https://github.com/will62794/logless-reconfig/blob/f7a89c745837ceadfe7149fa522e2d4504bb20a6/MongoStaticRaft.tla) and [MongoLoglessDynamicRaft](https://github.com/will62794/logless-reconfig/blob/f7a89c745837ceadfe7149fa522e2d4504bb20a6/MongoLoglessDynamicRaft.tla), which composed together in [MongoRaftReconfig](https://github.com/will62794/logless-reconfig/blob/f7a89c745837ceadfe7149fa522e2d4504bb20a6/MongoRaftReconfig.tla). The `Next` for `MongoStaticRaft` looks like this:


```
\* MongoStaticRaft

Next == 
    \* (a)
    \/ \E s \in Server : ClientRequest(s)
    \* etc
    \* (b)
    \/ \E s \in Server : \E Q \in Quorums(config[s]) : BecomeLeader(s, Q)
    \* etc

```


While the compositional `Next` looks like this:


```
\* MongoRaftReconfig
Next == 
    \/ OSMNext /\ UNCHANGED csmVars
    \/ CSMNext /\ UNCHANGED osmVars
    \/ JointNext

OSMNext == 
    \* (a)
    \/ \E s \in Server : OSM!ClientRequest(s)
    \* etc

JointNext == 
    \* (b)
    \/ \E i \in Server : \E Q \in Quorums(config[i]) : 
        /\ OSM!BecomeLeader(i, Q)
        /\ CSM!BecomeLeader(i, Q)
    \* etc

```


The actions under **(a)** must be manually repeated in `OSMNext`, while the actions under  **(b)** must be be carefully interlaced with the other spec under `JointNext`. This is the standard way of composing two specs, which gets progressively more difficult the more specs you need to integrate. It’s also hard to check refinements in this paradigm.


I’m trying to avoid both issues with my `Sync`-based approach. Each component already has its own `Next` that we can use without changes. Anything that affects shared variables is handled by the additional `Sync` operator.


Would *this spec* benefit from my approach? I don’t know. I designed the approach for a primary “machine” interacting with external components, where here the two specs are on equal footing. I have a sketch for what the conversion would look like, but I don’t know if it’s necessarily better.


Sketch of changes
  
This is all without adding an extra state machine. Pick one “primary” spec, say `CSM`. `Spec` then becomes
`Next == 
    \/ OSMNext
    \/ CSMNext

OSMNext ==
    /\ OSM!Next
    /\ UNCHANGED <<csmVars>>
    /\ UNCHANGED <<sharedVars>> \* new op

CSMNext ==
    /\ CSM!Next
    /\ Sync
    /\ UNCHANGED <<osmVars>>
`
We need to add `sharedVars` to `OSMNext` so it doesn’t call `OSM!BecomeLeader` on its own— that needs to happen through `Sync`. `sharedVars` will share some variables in common with with `csmVars` and `osmVars`.
`Sync` would look similar to `JointNext`:
`Sync ==
    \/ \E i \in Server : \E Q \in Quorums(config[i]) : 
        /\ OSM!BecomeLeader(i, Q)
        /\ CSM!BecomeLeader(i, Q)
    \/ \* ...
    \/ UNCHANGED <<sharedVars>>
`
It annoys me that we’re repeating `CSM!BecomeLeader` in both `CSMNext` *and* `Sync`, but it’s the most straightforward way to ensure that both `OSM` and `CSM` use the same values for `i` and `Q`. I figured out some ways to deduplicate this but they all rely on creative misuse of TLA+ semantics.

show all


My prediction is that conventional composition works for a wider variety of cases, but the `Sync` is more maintainable and scales better in the cases where it does work.


Neither approach handles the “one-to-many” case well. That’s where you have a spec for a single worker and try to use it to add N workers, where N is a model parameter. I discuss why this is so difficult in my article [Using Abstract Data Types in TLA+](https://www.hillelwayne.com/post/tla-adt/).


## Conclusion


This is a powerful technique, but also one that takes experience and adds complexity. It’s good if you need to write a very large specification or need a library of reusable components. For smaller specifications, I’d recommend the standard technique of putting all of the components in one spec.


This was developed for a consulting client and worked beautifully. I’m excited to share it with all of you! If you liked this, you can read other advanced TLA+ techniques [here](https://learntla.com/topics/index.html), like how to [make model-checking faster.](https://learntla.com/topics/optimization.html).


*Thanks to [Murat Demirbas](https://muratbuffalo.blogspot.com/) and [Andrew Helwer](https://ahelwer.ca/) for feedback. If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*


*I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/).*


---


### Appendix: `Sync` without primes


Some company styleguides forbid using primed variables as an expression in later actions. In that case, you can get the same effect like this:


```
-Sync ==
-   LET i == <<ws, ws'>> IN
+Sync(t) ==
+   LET i == <<t.from, t.to>> IN

+Do(t) ==
+    /\ ws = t.from
+    /\ ws' = t.to  

WorkerNext ==
-   /\ Worker!Next
-   /\ Sync
+   /\ \E t \in Worker!ValidTransitions:
+       /\ Do(t)
+       /\ Sync(t)
    /\ UNCHANGED server_log

```


`Do(t)` is effectively just emulating the behavior of `Worker!Next`, except it lets us “save” the transition we use and pass it into `Sync`.


This is also useful for preserving parameters passed into an action, which is sometimes necessary for composition.


---

1. This is why we needed to write `Server!Spec` as `[][Next]_internal` and not `[][Next]_vars`. `Server!Next` only needs to hold for the *internal* variables, not the shared ones!
 [return]
2. I had a long section on composition via multilayer refinement: `system.tla` refines `worker.tla` refines `workerSM.tla`. But it ended up being too complex to thoroughly explain. Maybe that’ll be a part 2! 
 [return]
