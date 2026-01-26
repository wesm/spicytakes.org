---
title: "Gateway"
description: "Interesting software rarely lives in isolation. The software a team     writes usually has to interact with external systems, these may be     libraries, remote calls to external services, interaction"
date: 2021-08-10T00:00:00
url: https://martinfowler.com/articles/gateway-pattern.html
slug: gateway-pattern
word_count: 2811
---


![](gateway-pattern/gateway.png)


Interesting software rarely lives in isolation. The software a team
    writes usually has to interact with external systems, these may be
    libraries, remote calls to external services, interactions with a database,
    or with with files. Usually there will be some form of API for that external
    system, but that API will often seem awkward from the context of our
    software. The API may use different types, require strange arguments,
    combine fields in ways that don't make sense in our context. Dealing with
    such an API can result in jarring mismatches whenever its used.


A gateway acts as a single point to confront this foreigner. Any code
    within our system interacts with the interface of the gateway, which is
    designed to work in the terms that our system uses. The gateway then
    translates this convenient API into the API offered by the foreigner.


While this pattern is widely used (but should be more prevalent), the
      name âgatewayâ has not caught on. So while you should expect to see this
      pattern frequently, there is no widely-used name for it.


## How it Works


A gateway is typically a simple wrapper. We look at what our code needs
    to do with the external system and construct an interface that supports that
    clearly and directly. We then implement the gateway to translate that
    interaction to the terms of the external system. This will usually involve
    translating a familiar function call into what's required by the foreign
    API, adjusting parameters as needed to make it work. When we get the
    results, we then transform those into a form that's easily consumable in our
    code. As our code grows, making new demands on the external system, we
    enhance the gateway to continue to support its different needs.


Gateways should only include logic that supports this translation between
    domestic and foreign concepts. Any logic that builds on that should be in
    clients of the gateway.


It's often useful to add a connection object to the basic structure of
    the gateway. The connection is a simple wrapper around the call to the
    foreign code. The gateway translates its parameters into the foreign
    signature, and calls the connection with that signature. The connection then
    just calls the foreign API and returns its result. The gateway finishes by
    translating that result to a more digestible form. The connection can be
    useful in two ways. Firstly it can encapsulate any awkward parts of the call
    to the foreign code, such as the manipulations needed for a REST API call.
    Secondly it acts as a good point for inserting a [Test Double](https://martinfowler.com/bliki/TestDouble.html).


## When to Use It


I use a gateway whenever I access some external software and there is any
    awkwardness in that external element. Rather than let the awkwardness spread
    through my code, I contain to a single place in the gateway.


Using a gateway can make a system much easier to test by allowing the
    test harness to stub out the gateway's connection object. This is
    particularly important for gateways that access remote services, as it can
    remove the need for a slow remote call. It's essential for external systems
    that need to supply canned data for testing but aren't designed to do so. I
    would use a gateway here, even if the external API is otherwise okay to use
    (in which case the gateway would only be the connection object).


Another virtue of a gateway is that it makes much easier to swap out an
    external system for another, should that happen. Similarly should an
    external system change its API or returned data, a gateway makes it much
    easier to adjust our code since any change is confined to a single place.
    But although this benefit is handy, its hardly ever a reason to use a
    gateway, since just encapsulating the foreign API is justification
    enough.


A key purpose of the gateway is to translate a foreign vocabulary which
    would otherwise complicate the host code. But before doing that, we do need
    to consider whether we should just use the foreign vocabulary. I have come
    across situations where a team has translated a widely-understood foreign
    vocabulary into a particular one for their code base because âthey didn't
    like the namesâ. There's no general rule I can state for this decision, a
    team has to exercise its judgment on whether they should adopt the external
    vocabulary or develop their own. (In [Domain Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html)
    patterns this is the choice between Conformist and Anticorruption
    Layer.)


A particular example of this is where we are building on platform and
    considering whether we wish to isolate ourselves from the underlying
    platform. In many cases the platform's facilities are so pervasive that it's
    not worth going through the effort of wrapping it. I won't consider wrapping
    a language's collection classes, for example. In that situation I just
    accept that their vocabulary is part of the vocabulary of my software.


## Further Reading


I originally described [this
    pattern](https://martinfowler.com/eaaCatalog/gateway.html) in [P of EAA](https://martinfowler.com/books/eaa.html).
    At that time I struggled whether to coin a new pattern name as opposed to
    referring to the existing Gang of Four patterns: Facade, Adapter, and
    Mediator. In the end I decided that there was enough of a difference that it
    was worth a new name.


While Facade simplifies a more complex API, it's usually done by the
    writer of the service for general use. A gateway is written by the client
    for its particular use.


Adapter is the closest GoF pattern to the gateway as it alters an class's
    interface to match another. But the adapter is defined in the context of
    both interfaces already being present, while with a gateway I'm defining the
    gateway's interface as I wrap the foreign element. That distinction led me
    to treat gateway as a separate pattern. Over time people have used âadapterâ
    much more loosely, so it's not unusual to see gateways called adapters.


Mediator separates multiple objects so they don't need to know about each
    other, they just know about the mediator. With a gateway there's usually
    only one resource that's being encapsulated behind the gateway and that
    resource will not know about the gateway.


The notion of a gateway fits well with that of the [Bounded Contexts](https://martinfowler.com/bliki/BoundedContext.html) of [Domain Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html). I use a gateway when I'm dealing with something
    in a different context, the gateway handles the translation between the
    foreign context and my own. The gateway is a way to implement an
    Anticorruption Layer. Consequently some teams will use that term, naming
    their gateways with the sortof-abbreviation âACLâ.


A common use of the term âgatewayâ is the [API gateway](https://microservices.io/patterns/apigateway.html).
    According the principles I've outlined above, this is really more of a
    facade, since it's build by the service provider for general client usage.


## Example: Simple Function (TypeScript)


Consider an imaginary hospital application that monitors a range of
    treatment programs. Many of these treatment programs need to book a patient
    to have time with a bone fusion machine. To do this, the application needs
    to interact with the hospital's equipment booking service. The application
    interacts with the service via a library which exposes a function to list
    available booking slots for some equipment.


equipmentBookingService.tsâ¦


```
  export function listAvailableSlots(equipmentCode: string, duration: number, isEmergency: boolean) : Slot[]
```


Since our application only uses bone fusion machines, and never in an
    emergency, it makes sense to simplify this function call. A simple
    gateway here can be a function, named in a way that makes sense for the
    current application.


boneFusionGateway.tsâ¦


```
  export function listBoneFusionSlots(length: Duration) {
    return ebs.listAvailableSlots("BFSN", length.toMinutes(), false)
      .map(convertSlot)
  }
```


This gateway function is doing several useful things. Firstly its name
    ties it to the particular usage within the application, allowing many
    callers to contain code that is clearer to read.


The gateway function encapsulates the equipment booking service's
    equipment code. Only this function needs to know that to get a bone fusion
    machine, you need code âBFSNâ.


The gateway function does conversion from the types used within the
    application to the types used by the API. In this case the application uses
    [js-joda](https://js-joda.github.io/js-joda/) to handle time -
    a common and wise choice to simplify any kind of date/time work in
    JavaScript. The API however, uses an integer number of minutes. The gateway
    function allows callers to work with the conventions in the application,
    without concerning themselves about how to convert to the conventions of the
    external API.


All requests from the application are non-urgent, hence the
    gateway doesn't expose a parameter that's always going to be the same value


Finally, the return values from the API are converted from the context of
    the equipment booking service with a conversion function.


The equipment booking service returns slot objects that look like this


equipmentBookingService.tsâ¦


```
  export interface Slot {
    duration: number,
    equipmentCode: string,
    date: string,
    time: string,
    equipmentID: string,
    emergencyOnly: boolean,
  }
```


but the calling application finds it more useful to have slots like this


treatmentPlanningAppointment.tsâ¦


```
  export interface Slot {
    date: LocalDate,
    time: LocalTime,
    duration: Duration,
    model: EquipmentModel
  }
```


so this code performs the conversion


boneFusionGateway.tsâ¦


```
  function convertSlot(slot:ebs.Slot) : Slot {
    return {
      date: LocalDate.parse(slot.date),
      time: LocalTime.parse(slot.time),
      duration: Duration.ofMinutes(slot.duration),
      model: modelFor(slot.equipmentID),
    }
  }
```


The conversion leaves out fields that are meaningless to the
    treatment planning application. It converts from the date and time strings
    to js-joda. The treatment planning users don't care about the equipmentID
    codes, but they do care about what model of equipment is available in the
    slot. So `convertSlot` looks up the equipment model from its local
    store and enriches the slot data with a model record.


By doing this, the treatment planning application doesn't have to deal
    with the language of the equipment booking service. It can pretend that the
    equipment booking service works seamlessly in the world of treatment
    planning.


## Example: Using a replaceable connection (TypeScript)


Gateways are the path to foreign code, and often foreign code is the
    route to important data that resides in other places. Such foreign data can
    complicate testing. We don't want to be booking equipment slots every time
    the developers of the treatment application run our tests. Even if the
    service provides a test instance, the slow speed of remote calls often
    undermines the usability of a fast test suite. This is when it makes sense
    to use a [Test Double](https://martinfowler.com/bliki/TestDouble.html).


A gateway is a natural point to insert such a test double, but there are
    couple of different ways to do it, since its worth having a bit more
    structure to a remote gateway. When working with a remote service, the
    gateway fulfills two responsibilities. As with local gateways, it does the
    translation from the vocabulary of the remote service into that of the host
    application. But with a remote service, it also has the responsibility of
    encapsulating the remoteness of that remote service, such as the details of
    how the remote call is done. That second responsibility implies that a remote
    gateway should contain a separate element to handle that, which I call the
    connection.


![](gateway-pattern/remote-comp.png)


In this situation `listAvailableSlots` may be a remote call to
    some URL which can be supplied from configuration.


equipmentBookingService.tsâ¦


```
  export async function listAvailableSlots(equipmentCode: string, duration: number, isEmergency: boolean) : Promise<Slot[]>
  {
    const url = new URL(config['equipmentServiceRootUrl'] + '/availableSlots')
    const params = url.searchParams;
    params.set('duration', duration.toString())
    params.set('isEmergency', isEmergency.toString())
    params.set('equipmentCode', equipmentCode)
    const response = await fetch(url)
    const data = await response.json()
    return data
  }
```


Having the root URL in configuration allows us to test the system against
    a test instance or a stub service by supplying a different root URL. This is
    great, but by manipulating the gateway we can avoid a remote call at all,
    which can be a significant speedup for the tests.


The connection also takes care of hassles using the machinery for
    invoking the remote call, in this case JavaScript's fetch API. The outer
    gateway handles converting the gateway's interface to the remote signature in
    terms of the remote API, while the connection takes that signature and
    expresses it as an HTTP get. Breaking those two tasks apart keeps each one simple.


I then add this connection to the gateway class on construction. The
    public function then uses this passed in connection.


class BoneFusionGatewayâ¦


```
  private readonly conn: Connection
  constructor(conn:Connection) {
    this.conn = conn
  }

  async listSlots(length: Duration) : Promise<Slot[]> {
    const slots = await this.conn("BFSN", length.toMinutes(), false)
    return slots.map(convertSlot)
  }

```


Often gateways support several public functions on the same underlying
    connection. So if our treatment application later needed to reserve a blood
    filter machine, we could add another function to the gateway that would use
    the same connection function with a different equipment code. Gateways may
    also combine data from multiple connections into a single public
    function.


When a service call like this requires some configuration, it's usually
    wise to do it separately from the code that uses it. We want our
    treatment planning appointment code to be able to simply use the gateway
    without having to know about how it should be configured. A simple and
    useful way to do this is to use a service locator.


class ServiceLocatorâ¦


```
  boneFusionGateway: BoneFusionGateway

```


serviceLocator.tsâ¦


```
  export let theServiceLocator: ServiceLocator
```


configuration (usually run at application startup)


```
  theServiceLocator.boneFusionGateway = new BoneFusionGateway(listAvailableSlots)

```


application code using the gateway


```
  const slots =  await theServiceLocator.boneFusionGateway.listSlots(Duration.ofHours(2))

```


Given this kind of setup, I can then write a test with a stub for the
   connection like this


```
it('stubbing the connection', async function() {
  const input: ebs.Slot[] = [
    {duration:  120, equipmentCode: "BFSN", equipmentID: "BF-018",
     date: "2020-05-01", time: "13:00", emergencyOnly: false},
    {duration: 180, equipmentCode: "BFSN", equipmentID: "BF-018",
     date: "2020-05-02", time: "08:00", emergencyOnly: false},
    {duration: 150, equipmentCode: "BFSN", equipmentID: "BF-019",
     date: "2020-04-06", time: "10:00", emergencyOnly: false},
   
  ]
  theServiceLocator.boneFusionGateway = new BoneFusionGateway(async () => input)
  const expected: Slot[] = [
    {duration: Duration.ofHours(2), date: LocalDate.of(2020, 5,1), time: LocalTime.of(13,0),
     model: new EquipmentModel("Marrowvate D12")},
    {duration: Duration.ofHours(3), date: LocalDate.of(2020, 5,2), time: LocalTime.of(8,0),
     model: new EquipmentModel("Marrowvate D12")},
  ]
  expect(await suitableSlots()).toStrictEqual(expected)
});
```


Stubbing in this way allows me to write tests without having to do a
   remote call at all.


Depending on the complexity of the translation that the gateway is doing,
   however, I might prefer to write my test data in the language of the
   application rather than the language of the remote service. I can do that
   with a test like this that checks that `suitableSlots` removes
   slots with the wrong kind of equipment model.


```
it('stubbing the gateway', async function() {
  const stubGateway = new StubBoneFusionGateway()
  theServiceLocator.boneFusionGateway = stubGateway
  stubGateway.listSlotsData = [
    {duration: Duration.ofHours(2), date: LocalDate.of(2020, 5,1), time: LocalTime.of(12,0),
     model: new EquipmentModel("Marrowvate D10")}, // not suitable
    {duration: Duration.ofHours(2), date: LocalDate.of(2020, 5,1), time: LocalTime.of(13,0),
     model: new EquipmentModel("Marrowvate D12")},
    {duration: Duration.ofHours(3), date: LocalDate.of(2020, 5,2), time: LocalTime.of(8,0),
     model: new EquipmentModel("Marrowvate D12")},
  ]
  const expected: Slot[] = [
    {duration: Duration.ofHours(2), date: LocalDate.of(2020, 5,1), time: LocalTime.of(13,0),
     model: new EquipmentModel("Marrowvate D12")},
    {duration: Duration.ofHours(3), date: LocalDate.of(2020, 5,2), time: LocalTime.of(8,0),
     model: new EquipmentModel("Marrowvate D12")},
  ]
  expect(await suitableSlots()).toStrictEqual(expected)   
});
```


```


class StubBoneFusionGateway extends BoneFusionGateway {  
  listSlotsData: Slot[] = []

  async listSlots(length: Duration) : Promise<Slot[]> {
    return this.listSlotsData
  }
  
  constructor() {
    super (async () => []) //connection not used, but needed for type check
  }
}

```


Stubbing the gateway can make it clearer what the application logic inside
   `suitableSlots` is supposed to do - in this case filter out the
   Marrowvate D10. But when I do this, I'm not testing the translation logic
   inside the gateway, so I need at least some tests that stub at the connection
   level. And if the remote system data isn't too hard to follow, I might be able to
   get away with only stubbing the connection. But often it's useful
   to be able stub at both points depending on the test I'm writing.


My programming platform may support some form of stubbing for remote calls
   directly. For example the JavaScript testing environment [Jest](https://jestjs.io) allows me to stub all sorts of function calls
   with its mock functions. What's available to me depends on the platform
   I'm using, but as you can see, it's not difficult to design gateways to
   have these hooks without any additional tools.


When stubbing a remote service like this, it's wise to use [Contract Tests](https://martinfowler.com/bliki/ContractTest.html) to ensure my assumptions about the remote service stay
   in sync with any changes that service makes.


## Example: Refactoring code accessing YouTube to introduce a Gateway (Ruby)


A few years ago [I
   wrote an article](https://martinfowler.com/articles/refactoring-external-service.html) with some code that accesses YouTube's API to display
   some information about videos. I show how the code tangles up different
   concerns and refactor the code to clearly separate them - introducing a
   gateway in the process. It provides a step-by-step explanation of how we can
   introduce a gateway into an existing code base.


## Acknowledgements


(Chris) Chakrit
         Likitkhajorn, Cam Jackson, Deepti Mittal, Jason Smith, Karthik Krishnan, Marcelo de Moraes Leite, Matthew
         Harward, and Pavlo Kerestey 

         discussed drafts of this post on our internal mailing list.
