---
title: "Refactoring to an Adaptive Model"
description: "Most of our software logic is written in our programming     languages, these give us the best environment to write and evolve     such logic. But there are circumstances when it's useful to move     "
date: 2015-11-19T00:00:00
tags: ["refactoring", "domain specific language"]
url: https://martinfowler.com/articles/refactoring-adaptive-model.html
slug: refactoring-adaptive-model
word_count: 6437
---


I recently did some consulting for the Hellenic Potions
    Corporation based in Atlantis. They are developing software
    applications to help potion brewers make effective potions. One
    aspect of good potion brewing is to get the right varieties of
    ingredients in your potion recipe. For example a certain recipe of
    flying potion requires the wings of a cricket, but different
    breeds of cricket are best in different circumstances. The
    software can recommend which breeds are best in certain
    circumstances, but the question is how that logic should be
    encoded.


Since this software team is a cool team, their server-side
    software runs on node.js. But potion brewing is a messy industrial
    process - Stymphalian Birds really mess with
    the wifi. So they need to run the breed recommendation logic on
    the client, and support mobile apps for both IOS and Android. The
    trouble is that this led to awkward duplication - the same logic was
    duplicated between JavaScript, Swift, and Java. Changing it was a
    labor in its own right, not just does all the code need to be changed
    in sync, you also have to deal with the App store, and even a pet
    minotaur makes little impression in Cupertino.


One option would be to run the javascript version of the logic
    on each device and use the mechanisms to run code in web views.
    But another option is to refactor the recommendation logic to data
    - what I refer to as an [Adaptive Model](https://martinfowler.com/dslCatalog/adaptiveModel.html). This
    allows us to encode the logic in
    a JSON data structure, which can be easily moved around and loaded
    into different device software. Applications can check to see if
    the logic has been updated and download a new version quickly
    after every change.


## Starting Code


Here's the sample of recommendation logic I'll use as the
       example for refactoring.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    if (spec.atNight) result.push("whispering death");
    if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
    if (spec.seasons && spec.seasons.includes("summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    if (spec.minDuration >= 150) {
      if (spec.seasons && spec.seasons.includes("summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
```


This example is in JavaScript, EcmaScript 6


The function takes a spec, a simple object that contains
      information about how the potion will be used. The logic then
      interrogates the specification adding suggested cricket breeds
      to the returned result object.


This code has a lot of primitive obsession: cricket breeds,
      seasons, and countries are all represented with literal strings.
      I will want to refactor these strings into their own types, but
      that's a separate refactoring I'll leave for another
      day.


## The Production Rule System pattern


When I'm looking to represent some imperative code with a
      data structure, my first task is to figure out what kind of
      model I should use to structure that data. A good choice of
      model can do much to simplify the logic, indeed there are times
      when using an adaptive model is worth it when the only reason is
      to make the logic easier to follow.
      In the worst case, I have to come up with (and evolve)
      such a model from scratch, but more often I can start with an
      existing computational model.


A series of conditionals like this suggests using a
      [Production Rule System](https://martinfowler.com/dslCatalog/productionRule.html), which is a particular computational model
      that's well suited to being represented in an adaptive model. A
      production rule system organizes computation through a
      collection of Production Rules, each of which is structure with
      two main elements: a condition and an action. The production
      rule system runs through all the rules, evaluates the condition
      for each rule, and if the condition returns true, executes the
      action.


To show the basic way of doing this, I'll explore this
      approach for the first couple of conditions. Here's the two
      conditions in their imperative form:


recommender.es6â¦


```
  if (spec.atNight) result.push("whispering death");
  if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
```


I can encode these using a JavaScript data structure of a
      list of two production rule objects and execute the model with a
      simple function.


recommendationModel.es6â¦


```
  export default [
    {
      condition: (spec) => spec.atNight,
      action: (result) => result.push("whispering death")
    },
    {
      condition: (spec) => spec.seasons && spec.seasons.includes("winter"),
      action: (result) => result.push("beefy")
    }
  ];
```


recommender.es6â¦


```
  import model from './recommendationModel.es6'
  function executeModel(spec) {
    let result = [];
    model
      .filter((r) => r.condition(spec))
      .forEach((r) => r.action(result));
    return result;
  }
```


Here you can see the general form of an adaptive model. We
      have a data structure that contains the particular logic that we
      need (`recommendationModel.es6`) together with an
      engine (`executeModel` that takes that data structure and executes it.


This adaptive model is a general implementation of production
      rules. But our production rules are more constrained than that.
      For a start all of the actions
      just add the name of cricket breed
      to the result, so I can simplify to this.


recommendationModel.es6â¦


```
  export default [
    {
      condition: (spec) => spec.atNight,
      result: "whispering death"
    },
    {
      condition: (spec) => spec.seasons && spec.seasons.includes("winter"),
      result: "beefy"
    }
  ];
```


recommender.es6â¦


```
  import model from './recommendationModel.es6'
  function executeModel(spec) {
    let result = [];
    model
      .filter((r) => r.condition(spec))
      .forEach((r) => result.push(r.result));
    return result;
  }
```


With that, I can further simplify the engine by removing the collecting variable.


recommender.es6â¦


```
  import model from './recommendationModel.es6'
  function executeModel(spec) {
    let result = [];
    return model
      .filter((r) => r.condition(spec))
      .map((r) => r.result);
    return result;
  }
```


That obvious simplification is nice, but the conditions are
       still JavaScript code, which won't fit our needs for running in
       a non JavaScript environment. I'll need to replace the condition
       code with data I can interpret.


## Refactoring the first lines


I shall describe this refactoring episode in two sections. In this first one I'll
      take these first few (blue) lines and refactor them into production rules. In the second part I'll work on the more awkward nested condition
      (green).


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    if (spec.atNight) result.push("whispering death");
    if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
    if (spec.seasons && spec.seasons.includes("summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    if (spec.minDuration >= 150) {
      if (spec.seasons && spec.seasons.includes("summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
```


### Representing the night condition in JSON


I'll start with just the first condition, which in the
       imperative form looks like:


recommender.es6â¦


```
  if (spec.atNight) result.push("whispering death");
```


I'd like to represent that in JSON as


recommendationModel.jsonâ¦


```
  [{"condition": "atNight", "result": "whispering death"}]
```


The first part of making this work is to read the JSON
       file and make it available to the recommendation logic.


recommendationModel.es6â¦


```
  import fs from 'fs'
  let model;
  export function loadJson() {
    model = JSON.parse(fs.readFileSync('recommendationModel.json', {encoding: 'utf8'}));
  }
  export default function getModel() {
    return model;
  }
```


I call `loadJson` at some point during
         application initialization. I made `getModel` so this module can have
         a default export function, which suits its usage after initialization.


I then need to modify the engine to understand the
       condition.


recommender.es6â¦


```
  function executeModel(spec) {
    return getModel()
      .filter((r) => isActive(r, spec))
      .map((r) => r.result)
  }
  function isActive(rule, spec) {
    if (rule.condition === 'atNight') return spec.atNight;
    throw new Error("unable to handle " + rule.condition);
  }
```


Now that I can represent the first condition in JSON, I need
       to replace that first condition by replacing it with the
       newborn production
       rule system.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec));
    if (spec.atNight) result.push("whispering death");
    if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
    if (spec.seasons && spec.seasons.includes("summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    //â¦ rest of conditions
```


Like any refactoring episode, I want to take the smallest
       steps I can, so I shall replace the smallest chunks of imperative
       code at time. It's easy to keep the adaptive model and imperative
       code running side-by-side. With each replacement I run all the
       tests for this recommendation logic, this is also a good
       opportunity to review these tests to see how good a job they
       do. Even when I've moved my logic into data, I will still need
       tests. The JSON file is data, but should be treated as code:
       version controlled and tested the same way.


### Seasons condition


Next up is the second line of the logic:


recommender.es6â¦


```
  if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
```


The first thing to notice here is that we have a compound
      condition, but this compound condition is repeated many places
      in the overall code.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec));
    if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
    if (spec.seasons && spec.seasons.includes("summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    if (spec.minDuration >= 150) {
      if (spec.seasons && spec.seasons.includes("summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
```


Although this is a compound condition, it's only representing
      a single intention - the compound nature is because I have to check
      that the seasons property is present before I can test its
      contents. Whenever I see something like this, I convulsively
      reach for [Extract Method](http://refactoring.com/catalog/extractMethod.html).


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec));
    if (seasonIncludes(spec, "winter")) result.push("beefy");
    if (seasonIncludes(spec, "summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    if (spec.minDuration >= 150) {
      if (seasonIncludes(spec, "summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
  function seasonIncludes(spec, arg) {
    return spec.seasons && spec.seasons.includes(arg);
  }
```


With that refactoring done, the second line now becomes a
      single function with an argument. Representing a function name
      and arguments in the JSON is a good tactic, as it gives me
      plenty of flexibility, so I'll try out this.


recommendationModel.jsonâ¦


```
  [
    {"condition": "atNight", "result": "whispering death"},
    {"condition": "seasonIncludes", "conditionArgs": ["winter"], "result": "beefy"}
  ]
```


recommender.es6â¦


```
  function isActive(rule, spec) {
    if (rule.condition === 'atNight') return spec.atNight;
    if (rule.condition === 'seasonIncludes') return seasonIncludes(spec, rule.conditionArgs[0]);
    throw new Error("unable to handle " + rule.condition);
  }
```


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec));
    if (seasonIncludes(spec, "winter")) result.push("beefy");
    if (seasonIncludes(spec, "summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    if (spec.minDuration >= 150) {
      if (seasonIncludes(spec, "summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
  function seasonIncludes(spec, arg) {
    return spec.seasons && spec.seasons.includes(arg);
  }
    // remainder of functionâ¦
```


Strictly I could just use a single value for the
      `arg`, but functions usually need multiple arguments
      at some point and it's no great effort to start with an array.


### Extracting the country logic


The third condition to work on looks like this


recommender.es6â¦


```
  if (seasonIncludes(spec, "summer")) {
    if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
  }
```


This introduces a couple of things. Firstly there's a new
      property of the spec to probe: which country the potion will be
      used in. Secondly that country test is combined with the
      existing seasonal test.


I've been carrying out this refactoring by
      taking conditions one at a time from the top. But I'll now
      confess I contrived the conditions so that we get a
      progression of gradually increasing complexity in the
      conditions. This is good for pedagogic reasons, but it won't be
      the way typical code appears in the field. I do advocate
      refactoring one condition at time, gradually building up the
      expressive power of the adaptive model as I'm doing here.
      However the best thing is to look through the code and pick
      fragments of logic to work with, starting with something simple and
      gradually getting more complicated. This will usually mean that going
      from top to bottom isn't the easiest way.


With refactoring I like to do one thing at a time, so I'll
      begin with handling the test for the country. As with the
      seasons test earlier, I start by extracting the country testing
      logic into its own function.


recommender.es6â¦


```
  if (seasonIncludes(spec, "summer")) {
    if (countryIncludedIn(spec, ["sparta", "atlantis"])) result.push("white lightening");
  }
```


```
  function countryIncludedIn(spec, anArray) {
    return anArray.includes(spec.country);
  }
```


### Parameterizing the model


With the previous refactorings, my next step was to extend
      the JSON rules to incorporate the condition I'm about to move.
      But for this case I want to first try out handling this
      `countryIncludedIn` test on its own, then later
      combine it with the seasonal test. So far my tests have been
      similar to.


```
  it('night only', function() {
    assert.include(recommender({atNight: true}), 'whispering death');
  });
```


I'm using [mocha](https://mochajs.org) and [chai](http://chaijs.com) for my tests


Where I've passed in a spec and run it against the existing
      recommender logic. But to test the country logic on its own, I need to
      create and pass in a model that contains the country logic
      without any additional conditions. I'm not testing my actual
      recommender model here, but the semantics of some general
      recommender model. As the code stands, I need to use some kind
      of [Test Double](https://martinfowler.com/bliki/TestDouble.html) for the model that will allow
      me to put in a simplified test model.


recommender.es6â¦


```
  function executeModel(spec) {
    return getModel()
      .filter((r) => isActive(r, spec))
      .map((r) => r.result)
  }
```


Setting up such a test double is do-able, but fiddly, so I prefer to
      take a different tack. Firstly I'll use [Add Parameter](http://refactoring.com/catalog/addParameter.html) so that the model is passed into the
      engine.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    if (seasonIncludes(spec, "summer")) {
      if (countryIncludedIn(spec, ["sparta", "atlantis"])) result.push("white lightening");
    }
    //â¦ remaining logic
  }
```


```
  function executeModel(spec, model) {
    return model
      .filter((r) => isActive(r, spec))
      .map((r) => r.result)
  }
```


I can then write a test along the lines of this:


```
  it('night only', function() {
    assert.include(
      executeModel({atNight: true}, [{"condition": "atNight", "result": "expected"}]),
      'expected');
  });
```


With that in place I can now write a test to purely test for
     the country property.


```
  it("country", function () {
    const model = [{condition: 'countryIncludedIn', conditionArgs: ['sparta', 'atlantis'], result: 'expected'}];
    expect(executeModel({country: "sparta"}, model)).include("expected");
    expect(executeModel({country: "athens"}, model)).not.include("expected");
  });
```


And make it pass with


recommender.es6â¦


```
  function isActive(rule, spec) {
    if (rule.condition === 'atNight') return spec.atNight;
    if (rule.condition === 'seasonIncludes') return seasonIncludes(spec, rule.conditionArgs[0]);
    if (rule.condition === 'countryIncludedIn') return rule.conditionArgs.includes(spec.country);
    throw new Error("unable to handle " + rule.condition);
  }
```


### Adding a conjunction


Testing for the operating country in the spec isn't all I need
     to do to handle the third rule:


recommender.es6â¦


```
  if (seasonIncludes(spec, "summer")) {
    if (countryIncludedIn(spec, ["sparta", "atlantis"])) result.push("white lightening");
  }
```


I also need to deal with nesting of the conditionals. When
     working with an adaptive model like this, I like to keep the
     logic limited to simple expressions, nested statements lead to a
     much more complicated representation. With nested ifs, this is
     easy as I can refactor the nested ifs to a
     conjunction.


recommender.es6â¦


```
  if (seasonIncludes(spec, "summer") && countryIncludedIn(spec, ["sparta", "atlantis"]))
    result.push("white lightening");
```


So now all I need is a conjunction (âandâ) function in my
     engine and I can extend the rule base to cover this case.


recommendationModel.jsonâ¦


```
  [
    {"condition": "atNight", "result": "whispering death"},
    {"condition": "seasonIncludes", "conditionArgs": ["winter"], "result": "beefy"},
    {
      "condition": "and",
      "conditionArgs": [
        {"condition": "seasonIncludes",    "conditionArgs": ["summer"]},
        {"condition": "countryIncludedIn", "conditionArgs": ["sparta", "atlantis"]}
      ],
      "result": "white lightening"
    }
  ]
```


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    if (seasonIncludes(spec, "summer") && countryIncludedIn(spec, ["sparta", "atlantis"]))
      result.push("white lightening");
    //â¦ remaining logic
  }
```


â¦


```
  function isActive(rule, spec) {
    if (rule.condition === 'atNight') return spec.atNight;
    if (rule.condition === 'seasonIncludes') return seasonIncludes(spec, rule.conditionArgs[0]);
    if (rule.condition === 'countryIncludedIn') return rule.conditionArgs.includes(spec.country);
    if (rule.condition === 'and') return rule.conditionArgs.every((arg) => isActive(arg, spec));
    throw new Error("unable to handle " + rule.condition);
  }
```


I hope those three conditions give you a decent flavor of how
     to refactor imperative code into an adaptive model. I convert the
     logic one chunk at a time. If the model isn't able to handle the
     chunk I use a combination of extending the model (adding
     functions, adding the ability for function arguments) and
     refactoring the imperative code (replacing nested conditionals
     with conjunction).


## The complicated bit


Here's the current state of the main recommendation function


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    if (spec.minDuration >= 150) {
      if (seasonIncludes(spec, "summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
```


I've folded in the initial lines into the model, so I'm now
     left with the large conditional. This doesn't seem to fit the
     production rule style so well. This doesn't mean the underlying
     logic doesn't fit the model, it's just that the code requires
     some massaging that shape becomes clear.


But there's another issue here too. This code is probing a new
     property of the spec - recommending a variety depending on the
     minimum duration that you want the potion to last (rather
     important for a flying potion). The conditional code is somewhat
     obscuring a broader pattern.


### The Range Picker pattern


I often see conditional code testing a numeric value like this


```
  function someLogic (arg) {
    if      (arg <  5) return "low";
    else if (arg < 15) return "medium";
    else               return "high";
  }
```


The core intention of the code is to return values depending on a list of ranges
     of values. I can represent this same logic like this:


```
  function logicWithPicker(arg) {
    const range = [
      [5, "low"],
      [15, "medium"],
      [Infinity, 'high']
    ];
    return pickFromRange(range, arg);
  }
  function pickFromRange(range, value) {
    const matchIndex = range.findIndex((r) => value < r[0]);
    return range[matchIndex][1];
  }
```


You'll notice this is performing the same trick that I've been describing so far
     in this article - moving logic into data. I've come up with a simple semantic model -
     a table of breakpoints and return values, together with some behavior that executes
     that model.


As with many logic to data changes, I wouldn't do this all the time. The simple
     conditional logic is easy to read, especially if formatted neatly to emphasize its
     tabular aspect. However if the breakpoints are open to frequent change, then
     representing them as data often makes it easier to update. In this case representing
     this logic through a range picker fits better with my overarching need to represent the
     logic as data.


### Replacing conditionals with a Range Picker


So my first moves in refactoring this next batch of code will
     be to replace the minimum duration tests in the imperative code
     with a range picker. I'll start with the summer case.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    if (spec.minDuration >= 150) {
      if (seasonIncludes(spec, "summer")) {
        result.push(pickFromRange(summerPicks, spec.minDuration));
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
```


One of the ways this section of code is awkward is that the first band of the range of
     minimum durations is excluded by the outer conditional. I'll want to remove that,
     keeping its logic within the range picker, which means I'll need a value for no
     recommendation. Null seems the natural choice for this, although I always wince a bit
     when using nulls in this situation.


Next I'll do the other case


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, null],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (spec.minDuration >= 150) {
      if (seasonIncludes(spec, "summer")) {
        result.push(pickFromRange(summerPicks, spec.minDuration));
      }
      else {
        result.push(pickFromRange(nonSummerPicks, spec.minDuration));
      }
    }
    return _.uniq(result);
  }
```


### Removing the outer conditional


With those done, I now want to get rid of the outer conditional.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, null],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (spec.minDuration >= 150) {
      if (seasonIncludes(spec, "summer")) {
        result.push(pickFromRange(summerPicks, spec.minDuration));
      }
      else {
        result.push(pickFromRange(nonSummerPicks, spec.minDuration));
      }
    }
    return _.uniq(result);
  }
```


But if I do this, the tests fail. There's a couple of problems here, firstly the
     conditional isn't just checking that the minDuration isn't less than 150, it's also
     checking that it's there at all - such is the annoyingly forgiving nature of many
     javascript operations. This implies I need to check for this value before I call the
     range picker function.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, null],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (spec.minDuration >= 150) {
    if (seasonIncludes(spec, "summer")) {
      if (spec.minDuration)
        result.push(pickFromRange(summerPicks, spec.minDuration));
    }
    else {
      if (spec.minDuration)
        result.push(pickFromRange(nonSummerPicks, spec.minDuration));
    }
    }
    return _.uniq(result);
  }
```


That's duplication, so I apply [Extract Method](http://refactoring.com/catalog/extractMethod.html).


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, null],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (seasonIncludes(spec, "summer")) {
      result.push(pickMinDuration(spec, summerPicks))
    }
    else {
      result.push(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result);
  }
  function pickMinDuration(spec, range) {
    if (spec.minDuration) {
      return pickFromRange(range, spec.minDuration);
    }
  }
```


### Dealing with ranges without a recommendation


However I still have a couple of tests failing, because I return a null which
     sits in the result set. One way to fix this is to guard the result.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, null],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (seasonIncludes(spec, "summer")) {
      if (pickMinDuration(spec, summerPicks))
        result.push(pickMinDuration(spec, summerPicks))
    }
    else {
      if (pickMinDuration(spec, nonSummerPicks))
        result.push(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result);
  }
```


I could argue that this would then be part of the condition for the production
     rule, but I don't think it really fits with the semantics of the domain to do that.


Another choice is to filter out the nulls at the end


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, null],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, null],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (seasonIncludes(spec, "summer")) {
      result.push(pickMinDuration(spec, summerPicks))
    }
    else {
      result.push(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result).filter((v) => null != v );
  }
```


I use â!=â to catch both nulls and the undefined value that's returned by
         `pickMinDuration` when there isn't a `minDuration` property


While both of these work, I'm not keen on slinging nulls around like this. If
     there's nothing to return, I'd rather return nothing than some signal for nothing.
     There's a classic way to deal with this problem - rather than return a single value,
     return a list. Returning nothing then just means returning the
     empty list.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, []],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, []],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (seasonIncludes(spec, "summer")) {
      result = result.concat(pickMinDuration(spec, summerPicks))
    }
    else {
      result = result.concat(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result);
  }
  function pickMinDuration(spec, range) {
    if (spec.minDuration)
      return pickFromRange(range, spec.minDuration);
    else return []
  }
```


JavaScript defines concat so that a non-array value
         will be added to the array.


This throws a bit of a googly at my production rule code, which
    will have to handle getting arrays as well as values. Fortunately
    that's a common problem with a common solution - [the flatten function](https://martinfowler.com/articles/collection-pipeline/flatten.html).


recommender.es6â¦


```
  function executeModel(spec, model) {
    return _.chain(model)
      .filter((r) => isActive(r, spec))
      .map((r) => r.result)
      .flatten()
      .value()
  }
```


since regular es6 doesn't have flatten, I need to use underscore


### Removing the else


My production rules don't have any notion of an
   `else` so I'll replace that with an inverted if.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
      [150, []],
      [350, 'white lightening'],
      [570, 'little master'],
      [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, []],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (seasonIncludes(spec, "summer")) {
      result = result.concat(pickMinDuration(spec, summerPicks))
    }
    else {
    if (!seasonIncludes(spec, "summer")) {
      result = result.concat(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result);
  }
```


### Adding a result function


I've now refactored the imperative code into a shape that makes
   it easy to transform it into production rules. But it's still not
   going to be trivial to replace the imperative code with the
   production rule because my production rules so far expect to return
   simple values. This one will need to execute the
   `pickMinDuration` function. This makes it closer to the
   classic production rule structure, where both the condition and
   action are functions. A simple way to handle this is to add some
   processing to the engine to handle either a result function or a single result
   value. I'll do this in a bunch of little steps, first using
   [Extract Method](http://refactoring.com/catalog/extractMethod.html)


recommender.es6â¦


```
  function executeModel(spec, model) {
    return _.chain(model)
      .filter((r) => isActive(r, spec))
      .map((r) => result(r))
      .flatten()
      .value()
  }
  function result(r) {
    return r.result;
  }
```


`pickMinDuration` takes the spec, so I'll have to
   pass that in by using [Add Parameter](http://refactoring.com/catalog/addParameter.html)


recommender.es6â¦


```
  function executeModel(spec, model) {
    return _.chain(model)
      .filter((r) => isActive(r, spec))
      .map((r) => result(r, spec))
      .flatten()
      .value()
  }
  function result(r, spec) {
    return r.result;
  }
```


Now I'll add the handling for a minimum duration rule. Since
   this is a little tricksy, I'll write a specific test for it.


test.es6â¦


```
  describe('min duration rule', function () {
    const range = [
      [  5,        []      ],
      [  10,       'low'   ],
      [  Infinity, 'high'  ]
    ];
    const model = [{
      condition: 'pickMinDuration', conditionArgs: [range],
      resultFunction: 'pickMinDuration', resultArgs: [range]
    }];
    const testValues = [
      [  4.9, []        ],
      [  5,   ['low']   ],
      [  9.9, ['low']   ],
      [  10,  ['high']  ]
    ];
    testValues.forEach(function (v) {
      it(`pick for duration: ${v[0]}`, function () {
          expect(executeModel({minDuration: v[0]}, model)).deep.equal(v[1]);
        }
      )
    });
    it('empty spec', () => {expect(executeModel({}, model)).be.empty;})
  });
```


I'll then modify the result function in the rule engine to
   conditionally handle either a result value or a result
   function and the condition test to recognize the minimum duration case.


recommender.es6â¦


```
  function executeModel(spec, model) {
    return _.chain(model)
      .filter((r) => isActive(r, spec))
      .map((r) => result(r, spec))
      .flatten()
      .value()
  }
  function result(r, spec) {
    if (r.result) return r.result;
    else if (r.resultFunction === 'pickMinDuration')
      return pickMinDuration(spec, r.resultArgs[0])
  }
  function isActive(rule, spec) {
  
    if (rule.condition === 'atNight') return spec.atNight;
    if (rule.condition === 'seasonIncludes') return seasonIncludes(spec, rule.conditionArgs[0]);
    if (rule.condition === 'countryIncludedIn') return rule.conditionArgs.includes(spec.country);
    if (rule.condition === 'and') return rule.conditionArgs.every((arg) => isActive(arg, spec));
    if (rule.condition === 'pickMinDuration') return true;
    throw new Error("unable to handle " + rule.condition);
  }
```


Now all is in place, I can easily add a rule to the model and
   remove the first condition.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const summerPicks = [
    [150, []],
    [350, 'white lightening'],
    [570, 'little master'],
    [Infinity, 'wall']
    ];
    const nonSummerPicks = [
      [150, []],
      [450, 'white lightening'],
      [Infinity, 'little master']
    ];
    if (seasonIncludes(spec, "summer")) {
    result = result.concat(pickMinDuration(spec, summerPicks))
    }
    if (!seasonIncludes(spec, "summer")) {
      result = result.concat(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result);
  }
```


recommendationModel.jsonâ¦


```
  [
    {"condition": "atNight", "result": "whispering death"},
    {"condition": "seasonIncludes", "conditionArgs": ["winter"], "result": "beefy"},
    {
      "condition": "and",
      "conditionArgs": [
        {"condition": "seasonIncludes",    "conditionArgs": ["summer"]},
        {"condition": "countryIncludedIn", "conditionArgs": ["sparta", "atlantis"]}
  
      ],
      "result": "white lightening"
    },
    { "condition":"seasonIncludes",
      "conditionArgs": ["summer"],
      "resultFunction": "pickMinDuration",
      "resultArgs": [[
        [ 150,        []                  ],
        [ 350,        "white lightening"  ],
        [ 570,        "little master"     ],
        [ "Infinity", "wall"              ]
      ]]
    }
  ]
```


### Removing the simple result value


This works fine, but I don't like how I have either a result
   value or a result function and the conditional handling of it. I
   can make things more regular by having only result functions, and have a
   value function that just returns its arguments.


recommendationModel.jsonâ¦


```
  [
    {"condition": "atNight", "result": "value", "resultArgs":["whispering death"]},
    {"condition": "seasonIncludes", "conditionArgs": ["winter"], "result": "value", "resultArgs":["beefy"]},
    {
      "condition": "and",
      "conditionArgs": [
        {"condition": "seasonIncludes",    "conditionArgs": ["summer"]},
        {"condition": "countryIncludedIn", "conditionArgs": ["sparta", "atlantis"]}
      ],
      "result": "value",
      "resultArgs": ["white lightening"]
    },
    {
      "condition":"seasonIncludes",
      "conditionArgs": ["summer"],
      "result": "pickMinDuration",
      "resultArgs": [[
        [ 150,        []                  ],
        [ 350,        "white lightening"  ],
        [ 570,        "little master"     ],
        [ "Infinity", "wall"              ]
      ]]
    }
  ]
```


recommender.es6â¦


```
  function result(r, spec) {
    if (r.result === "value") return r.resultArgs[0];
    if (r.result === 'pickMinDuration')
      return pickMinDuration(spec, r.resultArgs[0]);
    throw new Error("unknown result function: " + r.result)
  }
```


This makes the model json more verbose but allows the
   engine to be more regular. In this situation I prefer a more
   regular model even if it is more verbose. I can fix the verbosity
   another way, which I'll talk about later.


### Adding the negated condition


To get the last leg of the condition into the model I need a
   negation function in my model.


recommender.es6â¦


```
  function isActive(rule, spec) {
    if (rule.condition === 'atNight') return spec.atNight;
    if (rule.condition === 'seasonIncludes') return seasonIncludes(spec, rule.conditionArgs[0]);
    if (rule.condition === 'countryIncludedIn') return rule.conditionArgs.includes(spec.country);
    if (rule.condition === 'and') return rule.conditionArgs.every((arg) => isActive(arg, spec));
    if (rule.condition === 'pickMinDuration') return true;
    if (rule.condition === 'not') return !isActive(rule.conditionArgs[0], spec);
    throw new Error("unable to handle " + rule.condition);
  }
```


And I can then remove the last bit of imperative logic.


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    result = result.concat(executeModel(spec, getModel()));
    const nonSummerPicks = [
    [150, []],
    [450, 'white lightening'],
    [Infinity, 'little master']
    ];
    if (!seasonIncludes(spec, "summer")) {
    result = result.concat(pickMinDuration(spec, nonSummerPicks));
    }
    return _.uniq(result);
  }
```


added to recommendationModel.jsonâ¦


```
  {
    "condition":"not",
    "conditionArgs": [{"condition":"seasonIncludes", "conditionArgs": ["summer"]}],
    "result": "pickMinDuration",
    "resultArgs": [[
      [150,        []                  ],
      [450,        "white lightening"  ],
      ["Infinity", "little master"     ]
    ]]
  }
```


## A model instead of code


With this all done, all the conditional logic has moved from
     this original imperative code


recommender.es6â¦


```
  export default function (spec) {
    let result = [];
    if (spec.atNight) result.push("whispering death");
    if (spec.seasons && spec.seasons.includes("winter")) result.push("beefy");
    if (spec.seasons && spec.seasons.includes("summer")) {
      if (["sparta", "atlantis"].includes(spec.country)) result.push("white lightening");
    }
    if (spec.minDuration >= 150) {
      if (spec.seasons && spec.seasons.includes("summer")) {
        if (spec.minDuration < 350) result.push("white lightening");
        else if (spec.minDuration < 570) result.push("little master");
        else result.push("wall");
      }
      else {
        if (spec.minDuration < 450) result.push("white lightening");
        else result.push("little master");
      }
    }
    return _.uniq(result);
  }
```


into this json model


recommendationModel.jsonâ¦


```
  [
    {"condition": "atNight", "result": "value", "resultArgs":["whispering death"]},
    {"condition": "seasonIncludes", "conditionArgs": ["winter"], "result": "value", "resultArgs":["beefy"]},
    {
      "condition": "and",
      "conditionArgs": [
        {"condition": "seasonIncludes",    "conditionArgs": ["summer"]},
        {"condition": "countryIncludedIn", "conditionArgs": ["sparta", "atlantis"]}
      ],
      "result": "value",
      "resultArgs": ["white lightening"]
    },
    {
      "condition":"seasonIncludes",
      "conditionArgs": ["summer"],
      "result": "pickMinDuration",
      "resultArgs": [[
        [ 150,        []                  ],
        [ 350,        "white lightening"  ],
        [ 570,        "little master"     ],
        [ "Infinity", "wall"              ]
      ]]
    },
    {
      "condition":"not",
      "conditionArgs": [{"condition":"seasonIncludes", "conditionArgs": ["summer"]}],
      "result": "pickMinDuration",
      "resultArgs": [[
        [150,        []                  ],
        [450,        "white lightening"  ],
        ["Infinity", "little master"     ]
      ]]
    }
  ]
```


with the following engine to interpret the json model


recommender.es6â¦


```
  export default function (spec) {
    return executeModel(spec, getModel());
  }
  
  function pickMinDuration(spec, range) {
    return (spec.minDuration) ? pickFromRange(range, spec.minDuration) : [];
  }
  function countryIncludedIn(spec, anArray) {
    return anArray.includes(spec.country);
  }
  function seasonIncludes(spec, arg) {
    return spec.seasons && spec.seasons.includes(arg);
  }
  
  function executeModel(spec, model) {
    return _.chain(model)
      .filter((r) => isActive(r, spec))
      .map((r) => result(r, spec))
      .flatten()
      .uniq()
      .value()
  }
  function result(r, spec) {
    if (r.result === "value") return r.resultArgs[0];
    if (r.result === 'pickMinDuration')
      return pickMinDuration(spec, r.resultArgs[0]);
    throw new Error("unknown result function: " + r.result)
  }
  function isActive(rule, spec) {
    if (rule.condition === 'atNight') return spec.atNight;
    if (rule.condition === 'seasonIncludes') return seasonIncludes(spec, rule.conditionArgs[0]);
    if (rule.condition === 'countryIncludedIn') return rule.conditionArgs.includes(spec.country);
    if (rule.condition === 'and') return rule.conditionArgs.every((arg) => isActive(arg, spec));
    if (rule.condition === 'pickMinDuration') return true;
    if (rule.condition === 'not') return !isActive(rule.conditionArgs[0], spec);
    throw new Error("unable to handle " + rule.condition);
  }
```


I've done some minor cleanups over the earlier code.


What have I gained and lost? For a start the code is now a
      good bit bigger, the JSON model and the engine are
      individually larger than the original code. On its own, that's a
      Bad Thing. The important gain, however, is that we now have a
      single representation of the recommendation logic that can be
      interpreted on a website, IOS, Android, or any other environment
      that can read a JSON file. That's a considerable plus,
      particularly if the logic is actually larger than what I've
      got here - you should see the recommendation logic for invisibility potions.


There's another question here: whether the adaptive model is
      easier to modify than the imperative code. Although it's larger,
      it is more regular. With a larger set of rules, imperative
      code's flexibility can let it get more tangled easily, while the
      limited expressivity of an adaptive model can help keep logic easier to
      follow. Many people favor adaptive models for this reason, even
      if they don't have the multiple execution environment issues
      that we faced in Atlantis.


I should also summarize the refactoring process. Once I realize I need to replace
      some imperative code with an adaptive model, I first sketch out a first draft of
      that adaptive model - hopefully using one that's well-known. Then I take small bits
      of the imperative code and replace them with populating the adaptive model. If the
      code doesn't clearly fit the model, I'll refactor it into a shape that does fit and
      then move it over. If the adaptive model doesn't quite work with the current
      fragment of code, I'll refactor the model so it does.


In this example I replaced all the imperative code with the model, but I don't
      have to do that. At any point I can stop and leave some logic in the model and some
      in imperative code. This can be useful for edge cases that would raise the
      complexity of the model too much to be worth extending the model to handle. In this
      case we'd then accept the duplication and app-store inconveniences for those edge
      cases, while being able to handle the majority of rule changes through a model update.


## Some further refactorings


As I've been writing this, a couple of further directions for
     refactoring are shouting at me. I may revisit this article to add
     those another day.


### Reorganizing the model


As I look at the JSON model I think would prefer to
       reorganize its structure a tad, so that instead of


```
{
  "condition": â¦
  "conditionArgs": â¦
  "result": â¦
  "resultArgs": â¦
}
```


I'd have


```
{
  "condition": {
    "name": â¦
    "args": â¦
  }
  "result": {
    "name": â¦
    "args": â¦
  }
}
```


That makes the structure a bit more regular. There's some
       interesting refactoring here in migrating this data
       structure gradually.


### Replace imperative dispatch with lookup


The engine currently dispatches the condition and
       result functions using the `isActive` and
       `result` functions. Essentially wiring up a case
       statement (of course if I were a cool functional programmer, I'd call it
       pattern matching). Another option is to replace the
       imperative code with a lookup system, where the
       condition `seasonIncludes` is matched automatically to a function via a
       lookup table or reflection.


### Representing the model with a DSL


The JSON model reads fairly well, but the JSON syntax limits
       how clearly I can represent the rules. Furthermore I've
       deliberately preferred regularity in the model even if it makes
       the model more verbose than it could be. If I were managing a
       lot of rules, I'd be inclined to introduce a [Domain-Specific
       Language](https://martinfowler.com/dsl.html) for this, either internal (using JavaScript) or
       external. This could make it much easier to understand, and
       thus modify, the recommendation rules.


### Remove primitive obsession


The code represents the concepts of cricket breeds, seasons,
       and countries all as strings. While this mimics how they are
       represented in JSON, it usually wise to make specific types for
       concepts like this. This clarifies the code as it is, and
       provides a home that can attract useful behavior.


### Validating the adaptive model


At the moment I can only detect an error in the adaptive
       model by executing it. As models get more complex it's useful
       to build a validation operation that can detect that the JSON
       is well-formed and follows implicit syntactic rules beyond the
       simple structure enforced by JSON. Such rules would indicate
       that every clause must have a condition and a result, and that
       the arguments to the `seasonIncludes` function must
       be a known season.


### The reverse refactoring


As with any refactoring, there is also the reverse motion: replacing an adaptive
       model with imperative code. This is also a worthwhile direction to go - an adaptive
       model may be difficult to maintain, particularly since it's a less familiar
       approach. I've often run into a situation where some experienced members of a team
       are really productive by manipulating the adaptive model, but everyone else on the
       team finds it very difficult to work with. In some situations, the extra
       productivity makes it worth living with, but sometimes there are no benefits to the
       adaptive model. It's common for people to get all excited with the possibilities of
       representing code as data when they first come across it, and consequently
       over-using it. That's not a problem, it's part of a natural learning process, but
       it is important to remove it once the team realizes they went too far.


Replacing an adaptive model with imperative code is a similar process to its
       inverse, in that you first set things up so you can compose the outcome of the
       model with imperative code, then move logic into the imperative code in small
       chunks, testing as you go. The big difference here is that you can, and almost
       always should, let the imperative code's structure mirror that of the adaptive
       model. Consequently there isn't any massaging of the model or code's structure that
       you get when moving from imperative code to model.


---
