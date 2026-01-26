---
title: "Syntactic Noise"
description: "A common phrase that's bandied about when talking aboutDomainSpecificLanguages(or indeed any computer language) is that of noisy syntax. People may say that Ruby is less noisy than Java, or that exter"
date: 2008-06-09T00:00:00
tags: ["language feature", "domain specific language"]
url: https://martinfowler.com/bliki/SyntacticNoise.html
slug: SyntacticNoise
word_count: 915
---


A common phrase that's bandied about when talking about
[DomainSpecificLanguages](https://martinfowler.com/bliki/DomainSpecificLanguage.html) (or indeed any computer language) is that of
noisy syntax. People may say that Ruby is less noisy than Java, or
that external DSLs are less noisy than internal DSLs. By Syntactic
Noise, what people mean is extraneous characters that aren't part of
what we really need to say, but are there to satisfy the language
definition. Noise characters are bad because they obscure the meaning
of our program, forcing us to puzzle out what it's doing.


Like many concepts, syntactic noise is both loose and subjective,
which makes it hard to talk about. A while ago Gilhad Braha tried to
illustrate his perception of syntactic noise during a talk at
JAOO. Here I'm going to have a go at a similar approach and apply it
to several formulations of a DSL that I'm using in my current
[introduction in my DSL book](https://martinfowler.com/dslwip/Intro.html). (I'm using a subset of the example state
machine, to keep the text a reasonable size.)


In his talk he illustrated noise by coloring what he considered to
be noise characters. A problem with this, of course, is this requires
us to define what we mean by noise characters. I'm going to side-step
that and make a different distinction. I'll distinguish between what
I'll call domain text and punctuation. The DSL scripts I'm looking at
define a state machine, and thus talk about states, events, and
commands. Anything that describes information about my particular
state machine - such as the names of states - I'll define as domain
text. Anything else is punctuation and I'll highlight the latter in
red.


I'll start with the custom syntax of an external DSL.


```
events
  doorClosed  D1CL
  drawOpened  D2OP
  lightOn     L1ON
end
   
commands
  unlockDoor D1UL
  lockPanel   PNLK
end
   
state idle
  actions {unlockDoor lockPanel}
  doorClosed => active
end
   
state active
  drawOpened => waitingForLight
  lightOn    => waitingForDraw
end
```


A custom syntax tends to minimize noise, so as a result you see
relatively small amount of punctuation here. This text also makes
clear that we need *some* punctuation. Both events and commands are
defined by giving their name and their code - you need the punctuation
in order to tell them apart. So punctuation isn't the same as noise, I
would say that the wrong kind of punctuation is noise, or too much
punctuation is noise. In particular I don't think it's a good idea to
try to reduce punctuation to the absolute minimum, too little
punctuation also makes a DSL harder to comprehend.


Let's now look at an internal DSL for the same domain information
in Ruby.


```
event :doorClosed, âD1CLâ  
event :drawOpened,  âD2OPâ  
event :lightOn, âL1ONâ  

command  :lockPanel,   âPNLKâ 
command  :unlockDoor,  âD1ULâ 

state :idle do 
  actions :unlockDoor, :lockPanel
  transitions :doorClosed => :active
end 

state :active do 
  transitions :drawOpened => :waitingForLight, 
              :lightOn => :waitingForDraw
end 

```


Now we see a lot more punctuation. Certainly I could have made some
choices in my DSL to reduce punctuation, but I think most people would
still agree that a ruby DSL has more punctuation than a custom
one. The noise here, at least for me, is the little things: the â:â to
mark a symbol, the â,â to separate arguments, the 'â' to quote
strings.


One of the main themes in my DSL thinking is that a DSL is a way to
populate a framework. In this case the framework is one that describes
state machines. As well as populating a framework with a DSL you can
also do it with a regular push-button API. Let's color the punctuation
on that.


```
Event doorClosed = new Event(âdoorClosedâ, âD1CLâ); 
Event drawOpened = new Event(âdrawOpenedâ, âD2OPâ); 
Event lightOn = new Event(âlightOnâ, âL1ONâ); 
 
Command lockPanelCmd = new Command(âlockPanelâ, âPNLKâ); 
Command unlockDoorCmd = new Command(âunlockDoorâ, âD1ULâ); 

State idle = new State(âidleâ); 
State activeState = new State(âactiveâ); 
 
StateMachine machine = new StateMachine(idle); 

idle.addTransition(doorClosed, activeState);
idle.addCommand(unlockDoorCmd);
idle.addCommand(lockPanelCmd);

activeState.addTransition(drawOpened, waitingForLightState);
activeState.addTransition(lightOn, waitingForDrawState);
```


Here's a lot more punctuation. All sorts of quotes and brackets as
well as method keywords and local variable declarations. The latter
present an interesting classification question. I've counted the
declaring of a local variable as punctuation (as it duplicates the
name) but it's later use as domain text.


Java can also be written in a fluent way, so here's the fluent
version from the book.


```
public class BasicStateMachine extends StateMachineBuilder { 
  Events doorClosed, drawOpened, lightOn; 
  Commands lockPanel, unlockDoor; 
  States idle, active; 

  protected void defineStateMachine() { 
    doorClosed. code(âD1CLâ); 
    drawOpened. code(âD2OPâ); 
    lightOn.    code(âL1ONâ); 

    lockPanel.  code(âPNLKâ); 
    unlockDoor. code(âD1ULâ); 
 
    idle 
        .actions(unlockDoor, lockPanel) 
        .transition(doorClosed).to(active) 
        ; 
 
    active 
        .transition(drawOpened).to(waitingForLight) 
        .transition(lightOn).   to(waitingForDraw) 
        ; 
 } 
 

```


Whenever two or three are gathered together to talk about syntactic
noise, XML is bound to come up.


```
<stateMachine start = "idle"> 
    <event name="doorClosed" code="D1CL"/>  
    <event name="drawOpened" code="D2OP"/> 
    <event name="lightOn" code="L1ON"/> 

    <command name="lockPanel" code="PNLK"/> 
    <command name="unlockDoor" code="D1UL"/> 

  <state name="idle"> 
    <transition event="doorClosed" target="active"/> 
    <action command="unlockDoor"/> 
    <action command="lockPanel"/> 
  </state> 

  <state name="active"> 
    <transition event="drawOpened" target="waitingForLight"/> 
    <transition event="lightOn" target="waitingForDraw"/> 
  </state>
</stateMachine> 

```


I don't think we can read too much into this particular example,
but it does provide some food for thought. Although I don't think we
can make a rigorous separation between useful punctuation and noise,
the distinction between domain text and punctuation can help us focus
on the punctuation and consider what punctuation serves us best. And I
might add that having more characters of punctuation than you
do of domain text in a DSL is a smell.


(Mikael Jansson has put out a [lisp
version](http://mikael.jansson.be/journal/2008/06/martin-fowlers-syntactic-noise) of this example. Mihailo Lalevic did one in [JavaScript](http://digitalmihailo.blogspot.com/2008/06/martin-fowlers-syntactic-noise-in.html).)
