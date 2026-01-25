---
title: "The World and the Machine"
date: 2024-01-04
url: https://www.hillelwayne.com/post/world-vs-machine/
slug: world-vs-machine
word_count: 752
---

This is just a way of thinking about formal specification that I find really useful. The terms originally come from Michael Jackson’s [*Software Requirements and Specifications*](https://www.amazon.com/Software-Requirements-Specifications-Principles-Prejudices/dp/0201877120).


In specification, the machine is the part of the system you have direct control over and the world is all the parts that you don’t. Take a simple [transfer](https://learntla.com/intro/conceptual-overview.html#specifications) spec:


```
---- MODULE transfer ----
EXTENDS TLC, Integers
CONSTANTS People, Money, NumTransfers

(* --algorithm transfer
variables
  acct \in [People -> Money];

define
  \* Invariant
  NoOverdrafts ==
    \A p \in People:
      acct[p] >= 0
end define;

process cheque \in 1..NumTransfers
variable
  amnt \in 1..5;
  from \in People;
  to \in People
begin
  Check:
    if acct[from] >= amnt then
      Withdraw:
        acct[from] := acct[from] - amnt;
      Deposit:
        acct[to] := acct[to] + amnt;
    end if;
end process;
end algorithm; *)
====

```


The code that handles the transfer (represented by the `cheque` process) is the *machine*. It currently has a race condition that can break the invariant `NoOverdrafts`, where someone with $5 can submit two checks for $4 each and get them both past the guard clause.


One way you could solve this is by adding a lock so that the banking service only resolves one cheque at a time. One way you *can’t* solve it is by forcing people to deposit one cheque at a time. You don’t have any control over what people do with their chequebook! The people and their behavior is part of the *world*.


Whether something belongs to the world or the machine depends on your scope in the system. If you maintain one service and the other teams aren’t returning your calls, then their components are part of the world. If they’re sending you bad data, you need to faithfully model receiving that bad data in your spec as part of designing your machine.


### Some notes on this model


While you need to model the whole system, you’re only *designing* the machine. So the implementation details of the machine matter, but you don’t need to implement the world. It can be abstracted away, except for how it affects the machine. In the above example, we don’t need to model a person deciding to write a cheque or the person depositing it, just the transfer entering the system.


#### Observability and observable properties


Like in OOP, some system state is restricted to the world or machine.

1. The world can both read and write the `from` and `to` variables, but the machine can only read them. In most specifications these restrictions are implicit; you *could* write the spec so that the machine changes `from`, but your boss wouldn’t let you build it.
2. The “program counter”, or line each process is currently executing, isn’t readable or writable by the world. It’s an implementation detail of the machine.
3. `acct` can be written by the machine and read by the world. I call these observable.


We can divide properties into *internal* properties that concern just the machine and *external* (observable) properties that can be seen by the outside world. `NoOverdrafts` is observable: if it’s violated, someone will be able to see that they have a negative bank balance. By contrast, “at most one process can be in the withdraw step” (`OnlyOneWithdraw`) is internal. The world doesn’t have access to your transaction logs, nobody can *tell* whether `OnlyOneWithdraw` is satisfied or not.


Internal properties are useful but they’re less important than observable properties. An `OnlyOneWithdraw` violation might be the root cause of a `NoOverdrafts` violation, but `NoOverdrafts` is what actually matters to people. If a property isn’t observable, it doesn’t have any connection to the broader world, so nobody is actually affected by it breaking.


#### Misc

- If both the world and machine can write to a variable, generally the world should be able to do more with the variable than the machine can. IE the machine can only modify `acct` by processing transfers, while the world can also do deposits and withdrawals. It’s exceedingly hard to enforce [MISU](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/) on state the world can modify.
- If the world can break an invariant, it’s not an invariant. Instead you want “[resilience](https://buttondown.email/hillelwayne/archive/formalizing-stability-and-resilience-properties/)”, the ability to restore some system property after it’s been broken. See [here](https://www.hillelwayne.com/post/adversaries/) for more on modeling resilience.
- It’s not uncommon for a spec to break not because the machine has a bug, but because the surrounding world has changed.


*Thanks to [Andrew Helwer](https://ahelwer.ca/) and [Lars Hupel](https://lars.hupel.info/) for feedback. If you liked this, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*
