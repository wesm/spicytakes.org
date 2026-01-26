---
title: "Legacy Seam"
description: "When working with a legacy system it is valuable to identify and create seams:   places where we can alter the behavior of the system without editing   source code. Once we've found a seam, we can use"
date: 2024-01-04T00:00:00
tags: ["testing", "legacy modernization"]
url: https://martinfowler.com/bliki/LegacySeam.html
slug: LegacySeam
word_count: 1070
---


When working with a legacy system it is valuable to identify and create seams:
  places where we can alter the behavior of the system without editing
  source code. Once we've found a seam, we can use it to break dependencies to
  simplify testing, insert probes to gain observability, and redirect program
  flow to new modules as part of legacy displacement.


Michael Feathers coined the term “seam” in the context of legacy systems in
  his book [Working Effectively with Legacy Code](https://www.amazon.com/gp/product/0131177052/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0131177052&linkCode=as2&tag=martinfowlerc-20). His definition: **“a seam is a place
  where you can alter behavior in your program without editing in that place”**.


Here's an example of where a seam would be handy. Imagine some code to
  calculate the price of an order.


```
// TypeScript
export async function calculatePrice(order:Order) {
  const itemPrices = order.items.map(i => calculateItemPrice(i))
  const basePrice = itemPrices.reduce((acc, i) => acc + i.price, 0)
  const discount = calculateDiscount(order)
  const shipping = await calculateShipping(order)
  const adjustedShipping = applyShippingDiscounts(order, shipping)
  return basePrice + discount + adjustedShipping
}

```


The function `calculateShipping` hits an external service, which is slow (and
  expensive), so we don't want to hit it when testing. Instead we want to
  introduce a [stub](https://martinfowler.com/bliki/TestDouble.html), so we can provide a canned and deterministic response for
  each of the testing scenarios. Different tests may need different responses
  from the function, but we can't edit the code of
  `calculatePrice` inside the test. Thus we need to introduce a seam around the call
  to `calculateShipping`, something that will allow our test to
  redirect the call to the stub.


One way to do this is to pass the function for
  `calculateShipping` as a parameter


```
export async function calculatePrice(order:Order, shippingFn: (o:Order) => Promise<number>) {
  const itemPrices = order.items.map(i => calculateItemPrice(i))
  const basePrice = itemPrices.reduce((acc, i) => acc + i.price, 0)
  const discount = calculateDiscount(order)
  const shipping = await shippingFn(order)
  const adjustedShipping = applyShippingDiscounts(order, shipping)
  return basePrice + discount + adjustedShipping
}

```


A unit test for this function can then substitute a simple stub.


```
const shippingFn = async (o:Order) => 113
expect(await calculatePrice(sampleOrder, shippingFn)).toStrictEqual(153)
```


Each seam comes with an **enabling point**: “a place where you can
  make the decision to use one behavior or another” [[WELC]](https://www.amazon.com/gp/product/0131177052/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0131177052&linkCode=as2&tag=martinfowlerc-20). Passing the function as
  parameter opens up an enabling point in the caller of 
  `calculateShipping`.


This now makes testing a lot easier, we can put in different values of
  shipping costs, and check that `applyShippingDiscounts` responds
  correctly. Although we had to change the original source code to introduce the
  seam, any further changes to that function don't require us to alter that
  code, the changes all occur in the enabling point, which lies in the test code.


Passing a function as a parameter isn't the only way we can introduce a
  seam. After all, changing the signature of `calculateShipping` may
  be fraught, and we may not want to thread the shipping function parameter
  through the legacy call stack in the production code. In this case a lookup
  may be a better approach, such as using a service locator.


```
export async function calculatePrice(order:Order) {
  const itemPrices = order.items.map(i => calculateItemPrice(i))
  const basePrice = itemPrices.reduce((acc, i) => acc + i.price, 0)
  const discount = calculateDiscount(order)
  const shipping = await ShippingServices.calculateShipping(order)
  const adjustedShipping = applyShippingDiscounts(order, shipping)
  return basePrice + discount + adjustedShipping
}

```


```
class ShippingServices {
  static #soleInstance: ShippingServices
  static init(arg?:ShippingServices) {
    this.#soleInstance = arg || new ShippingServices()
  }
  static async calculateShipping(o:Order) {return this.#soleInstance.calculateShipping(o)}
  async calculateShipping(o:Order)  {return legacy_calcuateShipping(o)}
  // ... more services

```


The locator allows us to override the behavior by defining a subclass.


```
class ShippingServicesStub extends ShippingServices {
  calculateShippingFn: typeof ShippingServices.calculateShipping =
     (o) => {throw new Error("no stub provided")}
  async calculateShipping(o:Order) {return this.calculateShippingFn(o)}
  // more services

```


We can then use an enabling point in our test


```
const stub = new ShippingServicesStub()
stub.calculateShippingFn = async (o:Order) => 113
ShippingServices.init(stub)
expect(await calculatePrice(sampleOrder)).toStrictEqual(153)
```


This kind of service locator is a classical object-oriented way to set up a
  seam via function lookup, which I'm showing here to indicate the kind of
  approach I might use in other languages, but I wouldn't use this approach in
  TypeScript or JavaScript. Instead I'd put something like this into a module.


```
export let calculateShipping = legacy_calculateShipping

export function reset_calculateShipping(fn?: typeof legacy_calculateShipping) {
  calculateShipping = fn || legacy_calculateShipping
}

```


We can then use the code in a test like this


```
const shippingFn = async (o:Order) => 113
reset_calculateShipping(shippingFn)
expect(await calculatePrice(sampleOrder)).toStrictEqual(153)
```


As the final example suggests, the best mechanism to use for a seam depends
  very much on the language, available frameworks, and indeed the style of the
  legacy system. Getting a legacy system under control means learning how to
  introduce various seams into the code to provide the right kind of enabling
  points while minimizing the disturbance to the legacy software. While a
  function call is a simple example of introducing such seams, they can be [much
  more intricate in practice](https://martinfowler.com/articles/uncovering-mainframe-seams.html). A team can spend several months figuring out how
  to introduce seams into a well-worn legacy system. The best mechanism for
  adding seams to a legacy system may be different to what we'd do for similar
  flexibility in a green field.


Feathers's book focuses primarily on getting a legacy system under test, as
  that is often the key to being able to work with it in a sane way. But seams
  have more uses than that. Once we have a seam, we are in the position to place
  probes into the legacy system, allowing us to increase the observability of
  the system. We might want to monitor calls to `calculateShipping`,
  figuring out how often we use it, and capturing its results for separate analysis.


But probably the most valuable use of seams is that they
  allow us to migrate behavior away from the legacy.
  A seam might redirect high-value customers to a different shipping calculator.
  Effective legacy displacement is founded on introducing seams into the legacy
  system, and using them to gradually move behavior into a more modern environment.


Seams are also something to think about as we write new software, after all
  every new system will become legacy sooner or later. Much of my design advice
  is about building software with appropriately placed seams, so we can easily test,
  observe, and enhance it. If we write our software with testing in mind, we
  tend to get a good set of seams, which is a reason why [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) is such a useful technique.
