---
title: "TLA+ Action Properties"
date: 2021-02-25
url: https://www.hillelwayne.com/post/action-properties/
slug: action-properties
word_count: 1312
---

There’s not a whole lot on TLA+ technique out there: all the resources are either introductions or case studies. Good for people starting out, bad for people past that. I think we need to write more intermediate-level stuff, what Ben Kuhn calls [Blub studies](https://www.benkuhn.net/blub/). Here’s an attempt at that.


Most TLA+ properties are **invariants**, properties that must be true for every state in the behavior. If we have a simple counter:


```
EXTENDS Integers
VARIABLES x

Init == 
  x = 1

Next == 
  /\ x < 3
  /\ x' = x + 1

Spec == Init /\ [][Next]_x

```


Then an invariant of this spec is `x \in 1..3`. One property that is *not* an invariant is that `x` is always increasing. Going from `x = 2` to `x = 1` would violate this, but those are both *individually* valid states. It’s only the *transition* that is invalid. This property on a transition is called an **action property** and is written `[][x' > x]_x`.


show syntax
  
`(x' > x)` is the statement that the value of x in the next state (`x'`) is greater than the value of x in the current state. `[](x' > x)` would say that this is *always true*: every state must have a greater value for x than the state before.
We cannot write that directly, since it would be violated by [stutter steps](https://www.hillelwayne.com/post/fairness/). Since TLA+ is stutter-invariant, we should be able to insert a stutter anywhere without breaking the property. We instead want `[](x' > x \/ UNCHANGED x)`, that *either* x is increasing *or* doesn’t change. TLA+ provides the shorthand `[][A]_x` syntax, finally giving us `[][x' > x]_x`.

show all


In the Toolbox, action properties go in the “Temporal Properties” box. If you’re running from the command line, they’re `PROPERTY`s in the config file.


## Use Cases


### Conditional Properties


Using `=>`, we can make “conditional” properties that only must hold if the precondition is true. For example, if our system has a “kill switch”, we can say some value should not change while system is disabled:1


```
[][disabled => UNCHANGED x]_<<disabled, x>>

```


Or we can say that certain things must change in lockstep:


```
\* If x changes, y must become the old value of x
[][x' /= x => y' = x]_<<x, y>>

```


We can also use actions as the preconditions for invariants, where we only need the invariant to hold under those specific actions. If [we split our spec](https://www.hillelwayne.com/post/adversaries/) into `Machine` and `World` actions, we might want that only `Machine` actions maintain the invariant:


```
\* Next == Machine \/ World
\* Inv is some invariant
[][Machine => Inv]_vars

```


We can use actions on both sides of the condition, such as to say that if a certain change happens, it must have been “because of” a certain action:


```
\* owner \in [Credit -> User]
\* offers \in SUBSET (User \X User \X Credit)

Accept(from, to, credit) ==
\*    (User, User, Credit)
  /\ <<from, to, credit>> \in offers
  /\ offers' = offers \ {<<from, to, credit>>}
  /\ owner' = [owner EXCEPT ![credit] = to]

\* If ownership changes from A to B
\* It's because B accepted an offer from A
ValidChange(credit) ==
  LET co == owner[credit]
  IN co /= co' =>
    Accept(co, co', credit)

\* All changes in the system are valid changes   
ChangeProp ==
  [][\A c \in Credits: ValidChange(c)]_owner 

```


### State Transitions


A server has three states: `Offline`, `Booting`, and `Online`. We can say the server cannot go directly from `Offline` to `Online`:


```
\* status \in {Offline, Booting, Online}
[][status = Offline => status' /= Online]_status

```


If we have many different possible state transitions, we can abstract the valid transitions into an operator:


```
\* States == {A, B, C, D}
\* state \in States
Transitions == {
  <<A, B>>, <<A, C>>
  <<B, D>>,
  <<C, A>>, <<C, B>>
}

[][<<state, state'>> \in Transitions]_state

```


We can combine transitions with conditional properties:


```
T == <<state, state'>>
[][T = <<A, B>> => x' > x]_<<state, x>>
[][x' < x => T = <<A, C>>]_<<state, x>>

```


And we can extend state transition properties to multiple concurrent state machines:


```
\* Machines == {M1, M2, M3}
\* state \in [Machines -> States]

ChangedState(m) == state[m] /= state'[m]
TransitionAction(m) == <<state[m], state'[m]>>
[][\A m \in Machines:
  ChangedState(m) => 
    TransitionAction(m) \in Transitions
]_state

```


### Other Uses

- We are sharing a lock between threads. If one thread holds the lock, it must release the lock before another thread can acquire it:2
`\* lock \in Threads \union {NULL}
[][lock /= NULL => lock' \in {lock, NULL}]_lock
`
- We have an event `log` that is append-only. Prior values of the log should never change. This means that `log` is a prefix of `log'`:
`[][SubSeq(log', 1, Len(log)) = log]_log 
`
- Once a predicate becomes true, it cannot become false again:
`\* flag \in BOOLEAN
[][flag => flag']_flag
`
Once a value is no longer NULL, it does not go back to NULL:
`[][val /= NULL => val' /= NULL]_val
`
Once a value is no longer NULL, it doesn’t change:
`[][val /= NULL => UNCHANGED val]_val
`
- If we’re processing messages from a client and there are still messages in their queue, we do not switch to another client:
`\* curr = current_client \in Clients
\* queue \in [Clients -> Seq(Msg)]
[][
  queue[curr] /= <<>> => UNCHANGED curr
]_<<curr, queue>>
`


## Notes

- In my experience, action properties are less common than invariants and more common than liveness properties. However, liveness properties are generally “more important” to a spec being valid than the action properties are.3 Action properties are very useful, but not critical in the same way.
- The `x` in `[A]_x` can be any state predicate, not just a variable. Usually people add a helper operator `vars == <<x, y, z, ...>>` and then write `[A]_vars`. The only requirement is that all variables appearing in `A` must also appear in the subscript.
- Action properties can only describe pairs of states. You can’t natively write a property that spans *three* states without adding an auxilary variable.
- There’s a second form of action syntax: `<<A>>_x` means `A /\ x' /= x`, or “A happens *and x changes*.” Just as we can check “eventually predicate P is true” with `<>P`, we can *express* “eventually action A happens” with `<><<A>>_x`. Unfortunately, TLC cannot *check* this. It can only check properties of the form `[]<><<A>>_x`, or “A happens infinitely often”.
- TLC can *also* check properties of the form `<>[][A]_x`, or “eventually, the action property `[][A]_x` always holds.” I used that to form a conditional property in [this](https://www.hillelwayne.com/post/adversaries/) post:
`Resilient == []<>Safe
RareWorldResilient == <>[][World => Safe]_x => Resilient
`
That property, in English, is “If it’s eventually the case that `World` actions only happen when `Safe` holds, then even if `World` breaks `Safe`, we will always eventually return to `Safe` holding.”
I don’t think I’ve actually used `<>[][A]_x` in a real world spec, though, just in examples.
- Most specs are written as `Init /\ [][Next]_vars`. TLC can check `[][Next]_vars` just like any other action property! This is the launching point into **refinement**, or using an entire specification as the checked property of another spec. That’ll have to be the topic of another post.


*Thanks to [Andrew Helwer](https://ahelwer.ca/) for feedback.*


---

1. `UNCHANGED x` is syntactic sugar for `x' = x`.
 [return]
2. I could have just written `lock' = NULL` instead of `lock' \in {lock, NULL}`. `[P]_lock` means `P \/ UNCHANGED lock`, which would have implicitly permitted the thread lock to not change. But that would “offload” spec logic to the syntax, which isn’t clear to readers.
 [return]
3. Invariants and action properties only cover bad states and transitions. They don’t cover “the system actually does what you need it to do.” That’s liveness. 
 [return]
