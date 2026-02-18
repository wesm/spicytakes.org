---
title: "Introducing the BARE message encoding"
date: 2020-06-21
url: https://drewdevault.com/2020/06/21/BARE-message-encoding.html
slug: BARE-message-encoding
word_count: 1176
---

I like stateless tokens. We started with state *ful*  tokens: where a generated
string acts as a unique identifier for a resource, and the resource itself is
looked up separately. For example, your sr.ht OAuth token is a stateful token:
we just generate a random number and hand it to you, something like
“a97c4aeeec705f81539aa”. To find the information associated with this token, we
query the database — our local  *state*  — to find it.

But, increasingly, we’ve been using stateless tokens, which are a bloody good
idea. The idea is that, instead of using random numbers, you encode the actual
state you need into the token. For example, your sr.ht login session cookie is a
JSON blob which is encrypted and base64 encoded. Rather than associating your
session with a record in the database, we just decrypt the cookie when your
browser sends it to us, and the session information is right there. This
improves performance and simplicity in a single stroke, which is a huge win in
my book.

There is one big problem, though: stateless tokens tend to be a lot larger than
their stateful counterparts. For a stateful token, we just need to generate
enough random numbers to be both unique and unpredictable, and then store the
rest of the data elsewhere. Not so for a stateless token, whose length is a
function of the amount of state which has been sequestered into it. Here’s an
example: the cursor fields on the new GraphQL APIs are stateless. This is one of
them:

```
gAAAAABe7-ysKcvmyavwKIT9k1uVLx_GXI6OunjFIHa3OJmK3eBC9NT6507PBr1WbuGtjlZSTYLYvicH2EvJXI1eAejR4kuNExpwoQsogkE9Ua6JhN10KKYzF9kJKW0hA_-737NurotB
```

A whopping 141 characters long! It’s hardly as convenient to lug this monster
around. Most of the time it’ll be programs doing the carrying, but it’s still
annoying when you’re messing with the API and debugging your programs. This
isn’t an isolated example, either: these stateless tokens tend to be large
throughout sr.ht.

In general, JSON messages are pretty bulky. They represent everything as text,
which can be 2x as inefficient for certain kinds of data right off the bat.
They’re also self-describing: the schema of the message is encoded into the
message itself; that is, the names of fields, hierarchy of objects, and data
types.

There are many alternatives that attempt to address this problem, and I
considered many of them. Here were a selected few of my conclusions:

* [protobuf](https://developers.google.com/protocol-buffers/) : too
complicated and too fragile, and I’ve never been fond of the generated code
for protobufs in any language. Writing a third-party protobuf implementation
would be a gargantuan task, and there’s no standard. RPC support is also
undesirable for this use-case.
* [Cap’n Proto](https://capnproto.org/) : fixed width, alignment, and so on
— good for performance, bad for message size. Too complex. RPC support
is also undesirable for this use-case. I also passionately hate C++ and I
cannot in good faith consider something which makes it their primary target.
* [BSON](http://bsonspec.org/) : MonogoDB implementation details have leaked into
the specification, and it’s extensible in the worst way. I appreciate that
JSON is a closed spec and no one is making vendor extensions for it —
and, similarly, a diverse extension ecosystem is not something I want to see
for this technology. Additionally, encoding schema into the message is wasting
space.
* [MessagePack](https://msgpack.org/) : ruled out for similar reasons: too much
extensibility, and the schema is encoded into the message, wasting space.
* [CBOR](https://cbor.io/) : ruled out for similar reasons: too much
extensibility, and the schema is encoded into the message. Has the advantage
of a specification, but the disadvantage of that spec being 54 pages long.

There were others, but hopefully this should give you an idea of what I was
thinking about when evaluating my options.

There doesn’t seem to be anything which meets my criteria just right:

* Optimized for small messages
* Standardized
* Easy to implement
* Universal — little to no support for extensions
* Simple — no extra junk that isn’t contributing to the core mission

The solution is evident.

## BARE: Binary Application Record Encoding

[BARE](https://baremessages.org)  meets all of the criteria:

* **Optimized for small messages** : messages are binary, not self-describing,
and have no alignment or padding.
* **Standardized & simple** : the specification is just over 1,000 words —
shorter than this blog post.
* **Easy to implement** : the first implementation (for Go) was done in a single
weekend (this weekend, in fact).
* **Universal** : there is room for user extensibility, but it’s done in a manner
which does not require expanding the implementation nor making messages which
are incompatible with other implementations.

Stateless tokens aren’t the only messages that I’ve wanted a simple binary
encoding for. On many occasions I’ve evaluated and re-evaluated the same set of
existing solutions, and found none of them quite right. I hope that BARE will
help me solve many of these problems in the future, and I hope you find it
useful, too!

The cursor token I shared earlier in the article looks like this when encoded
with BARE:

```
gAAAAABe7_K9PeskT6xtLDh_a3JGQa_DV5bkXzKm81gCYqNRV4FLJlVvG3puusCGAwQUrKFLO-4LJc39GBFPZomJhkyqrowsUw==
```

100 characters (41 fewer than JSON), which happens to be the minimum size of a
padded  [Fernet](https://github.com/fernet/spec/)  message. If we compare only the
cleartext:

```
JSON: eyJjb3VudCI6MjUsIm5leHQiOiIxMjM0NSIsInNlYXJjaCI6bnVsbH0=
BARE: EAUxMjM0NQA=
```

Much improved!

BARE also has an optional schema language for defining your message structure.
Here’s a sample:

```
type PublicKey data<128>
type Time string # ISO 8601

enum Department {
  ACCOUNTING
  ADMINISTRATION
  CUSTOMER_SERVICE
  DEVELOPMENT

  # Reserved for the CEO
  JSMITH = 99
}

type Customer {
  name: string
  email: string
  address: Address
  orders: []{
    orderId: i64
    quantity: i32
  }
  metadata: map[string]data
}

type Employee {
  name: string
  email: string
  address: Address
  department: Department
  hireDate: Time
  publicKey: optional
  metadata: map[string]data
}

type Person (Customer | Employee)

type Address {
  address: [4]string
  city: string
  state: string
  country: string
}
```

You can feed this into a code generator and get types which can encode & decode
these messages. But, you can also describe your schema just using your
language’s existing type system, like this:

```
type Coordinates struct {
    X uint  // uint
    Y uint  // uint
    Z uint  // uint
    Q *uint // optional<uint>
}

func main() {
    var coords Coordinates
    payload := []byte{0x01, 0x02, 0x03, 0x01, 0x04}
    err := bare.Unmarshal(payload, &coords)
    if err != nil {
        panic(err)
    }
    fmt.Printf("coords: %d, %d, %d (%d)\n", /* coords: 1, 2, 3 (4) */
        coords.X, coords.Y, coords.Z, *coords.Q)
}
```

Bonus: you can get the schema language definition for this struct with
 `schema.SchemaFor(coords)` .

## BARE is under development

There are some possible changes that could come to BARE before finalizing the
specification. Here are some questions I’m thinking about:

* Should the schema language include support for arbitrary annotations to
inform code generators? I’m inclined to think “no”, but if you use BARE and
find yourself wishing for this, tell me about it.
* Should BARE have first-class support for bitfield enums?
* Should maps be ordered?

[Feedback welcome](mailto:~sircmpwn/public-inbox@lists.sr.ht) !

**Errata**

* This article was originally based on an older version of the draft
specification, and was updated accordingly.
