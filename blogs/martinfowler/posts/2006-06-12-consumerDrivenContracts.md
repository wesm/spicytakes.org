---
title: "Consumer-Driven Contracts: A Service Evolution 	Pattern"
description: "This article discusses some of the challenges in evolving 	a community of service providers and consumers. It describes some of 	the coupling issues that arise when service providers change parts 	of "
date: 2006-06-12T00:00:00
tags: ["application integration", "web services"]
url: https://martinfowler.com/articles/consumerDrivenContracts.html
slug: consumerDrivenContracts
word_count: 5408
---


## Evolving a Service: An Example


To illustrate some of the problems we encounter while evolving services, consider a simple ProductSearch service, which allows consumer applications to search our product catalogue. A search result has the following structure:


![](consumerDrivenContracts/products1.gif)


Figure 1: Search result schema


An example search result document looks like this:


```
<?xml version="1.0" encoding="utf-8"?>
<Products xmlns="urn:example.com:productsearch:products">
  <Product>
    <CatalogueID>101</CatalogueID>
    <Name>Widget</Name>
    <Price>10.99</Price>
    <Manufacturer>Company A</Manufacturer>
    <InStock>Yes</InStock>
  </Product>
  <Product>
    <CatalogueID>300</CatalogueID>
    <Name>Fooble</Name>
    <Price>2.00</Price>
    <Manufacturer>Company B</Manufacturer>
    <InStock>No</InStock>
  </Product>
</Products>

```


The ProductSearch service is currently consumed by two applications: an internal marketing application and an external reseller's Web application. Both consumers use XSD validation to validate received documents prior to processing them. The internal application uses the *CatalogueID*, *Name*, *Price* and *Manufacturer* fields; the external application the *CatalogueID*, *Name* and *Price* fields. Neither uses the *InStock* field: though considered for the marketing application, it was dropped early in the development lifecycle.


One of the most common ways in which we might evolve a service is to add an additional field to a document on behalf of one or more consumers. Depending on how the provider and consumers have been implemented, even a simple change like this can have costly implications for the business and its partners.


In our example, after the ProductSearch service has been in production for some time, a second reseller considers using it, but asks that a *Description* field be added to each product. Because of the way the consumers have been built, the change has significant and costly implications both for the provider and the existing consumers, the cost to each varying based on how we implement the change. There are at least two ways in which we can distribute the cost of change between the members of the service community. First, we could modify our original schema and require each consumer to update its copy of the schema in order correctly to validate search results; the cost of changing the system is here distributed between the provider - who, faced with a change request like this, will always have to make some kind of change - and the consumers, who have no interest in the updated functionality. Alternatively, we could choose to add a second operation and schema to the service provider on behalf of the new consumer, and maintain the original operation and schema on behalf of the existing consumers. The cost of change is now constrained to the provider, but at the expense of making the service more complex and more costly to maintain.


## Interlude: Burdened With Services


Chief among the benefits of service-enabling an enterprise's application landscape are increased organizational agility and reduced overall cost of implementing change. An SOA increases organizational agility by placing high-value business functions in discrete, reusable services, and then connecting and orchestrating these services to satisfy core business processes. It reduces the cost of change by reducing the dependencies between services, allowing them to be rapidly recomposed and tuned in response to change or unplanned events.


A business can only fully realise these benefits, however, if its SOA enables services to evolve independently of one another. To increase service independence, we build services that share contracts, not types. Even so, we often end up having to evolve consumers at the same rate as the service provider, chiefly because we've made the consumers depend on a particular version of the provider's contract. In the end, service providers find themselves adopting a cautious approach to changing any element of the contract they offer their consumers; this, in part, because they cannot anticipate or gain insight into the ways in which consumers realise this contract. At worst, service consumers realise a provider contract and couple themselves to the provider by naively expressing the whole of a document schema within their internal logic.


Contracts enable service independence; paradoxically, they can also couple service providers and consumers in undesirable ways. Without introspecting the function and role of the contracts we implement in our SOA, we subject our services to a form of âhiddenâ coupling that we are rarely equipped to address in any systematic fashion. The absence of any programmatic insights into the ways in which a community of services has adopted a contract, and the lack of constraints on the implementation choices made by service providers and consumers, combine to undermine the purported benefits of SOA-enabling the enterprise. In short, the enterprise becomes burdened with services.


## Schema Versioning


We can begin our investigations into the contract and coupling problems that bedevil our ProductSearch service by looking at the issue of schema versioning. The [WC3 Technical Architecture Group (TAG)](http://www.w3.org/2001/tag/doc/versioning) has described a number of versioning strategies that might help us evolve our service's message schemas in ways that mitigate our coupling problems. These strategies range from the excessively liberal *none*, which mandates that services must not distinguish between different versions of a schema, and must therefore tolerate all changes, to the exceedingly conservative *big bang*, which requires services to abort if they receive an unexpected version of a message.


Both extremes bring with them problems that inhibit the delivery of business value and exacerbate the total cost of ownership of the system. Explicit and implicit âno versioningâ strategies result in systems that are alike in being unpredictable in their interactions, fragile, and costly to change downstream. Big bang strategies, on the other hand, give rise to tightly coupled service landscapes where schema changes ripple through providers and consumers, disrupting uptime, retarding evolution and reducing revenue generating opportunities.


Our example service community effectively implements a big bang strategy. Given the costs associated with enhancing the business value of the system, it is clear that the providers and consumers would benefit from a more flexible versioning strategy - what the TAG finding calls a *compatible* strategy - which provides for backwards- and forwards-compatible schemas. In the context of evolving services, backwards-compatible schemas enable consumers of newer schemas to accept instances of an older schema: a service provider built to handle new versions of a backwards-compatible request, say, could nonetheless still accept a request formatted according to an old schema. Forwards-compatible schemas, on the other hand, enable consumers of older schemas to process an instance of a newer schema. This is the sticking point for the existing ProductSearch consumers: if the search result schema had been made forwards-compatible when first put into production, the consumers would be able to handle instances of the new version of the search result without breaking or requiring modification.


### Extension Points


Making schemas both backwards- and forwards-compatible is a well-understood design task, best expressed by the *Must Ignore* pattern of extensibility (see the papers by [David Orchard](http://www.pacificspirit.com/Authoring/Compatibility/ExtendingAndVersioningXMLLanguages.html) and [Dare Obasanjo](http://msdn.microsoft.com/library/en-us/dnexxml/html/xml07212004.asp)). The *Must Ignore* pattern recommends that schemas incorporate extensibility points, which allow extension elements to be added to types and additional attributes to each element. The pattern also recommends that XML languages define a processing model that specifies how consumers process extensions. The simplest model requires consumers to ignore elements that they do not recognize - hence the name of the pattern. The model may also require consumers to process elements that have a âMust Understandâ flag, or abort if they cannot understand them.


This is the schema on which we originally based our search results documents:


```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns="urn:example.com:productsearch:products" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  elementFormDefault="qualified" 
  targetNamespace="urn:example.com:productsearch:products" 
  id="Products">
  <xs:element name="Products" type="Products" />
  <xs:complexType name="Products">
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Product" type="Product" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="Product">
    <xs:sequence>
      <xs:element name="CatalogueID" type="xs:int" />
      <xs:element name="Name" type="xs:string" />
      <xs:element name="Price" type="xs:double" />
      <xs:element name="Manufacturer" type="xs:string" />
      <xs:element name="InStock" type="xs:string" />
    </xs:sequence>
  </xs:complexType>
</xs:schema>

```


Let's now roll back time and, from the outset of our service's lifetime, specify a forwards-compatible, extensible schema:


```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns="urn:example.com:productsearch:products" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  elementFormDefault="qualified" 
  targetNamespace="urn:example.com:productsearch:products" 
  id="Products">
  <xs:element name="Products" type="Products" />
  <xs:complexType name="Products">
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Product" type="Product" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="Product">
    <xs:sequence>
      <xs:element name="CatalogueID" type="xs:int" />
      <xs:element name="Name" type="xs:string" />
      <xs:element name="Price" type="xs:double" />
      <xs:element name="Manufacturer" type="xs:string" />
      <xs:element name="InStock" type="xs:string" />
      <xs:element minOccurs="0" maxOccurs="1" name="Extension" type="Extension" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="Extension">
    <xs:sequence>
      <xs:any minOccurs="1" maxOccurs="unbounded" namespace="##targetNamespace" processContents="lax" />
    </xs:sequence>
  </xs:complexType>
</xs:schema>

```


This schema includes an optional Extension element at the foot of each product. The extension element itself can contain one or more elements from the target namespace:


![](consumerDrivenContracts/products2.gif)


Figure 2: Extensible search result schema


Now when we receive a change request to add a description to each product, we can publish a new schema with an additional *Description* element that the provider inserts into the extension container. This allows the ProductSearch service to return results that include product descriptions, and consumers using the new schema to validate the entire document. Consumers using the old schema will not break, though they will not process the description. The new results documents look like this:


```
<?xml version="1.0" encoding="utf-8"?>
<Products xmlns="urn:example.com:productsearch:products">
  <Product>
    <CatalogueID>101</CatalogueID>
    <Name>Widget</Name>
    <Price>10.99</Price>
    <Manufacturer>Company A</Manufacturer>
    <InStock>Yes</InStock>
    <Extension>
      <Description>Our top of the range widget</Description>
    </Extension>
  </Product>
  <Product>
    <CatalogueID>300</CatalogueID>
    <Name>Fooble</Name>
    <Price>2.00</Price>
    <Manufacturer>Company B</Manufacturer>
    <InStock>No</InStock>
    <Extension>
      <Description>Our bargain fooble</Description>
    </Extension>
  </Product>
</Products>

```


The revised schema looks like this:


```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns="urn:example.com:productsearch:products" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  elementFormDefault="qualified" 
  targetNamespace="urn:example.com:productsearch:products" 
  id="Products">
  <xs:element name="Products" type="Products" />
  <xs:complexType name="Products">
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Product" type="Product" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="Product">
    <xs:sequence>
      <xs:element name="CatalogueID" type="xs:int" />
      <xs:element name="Name" type="xs:string" />
      <xs:element name="Price" type="xs:double" />
      <xs:element name="Manufacturer" type="xs:string" />
      <xs:element name="InStock" type="xs:string" />
      <xs:element minOccurs="0" maxOccurs="1" name="Extension" type="Extension" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="Extension">
    <xs:sequence>
      <xs:any minOccurs="1" maxOccurs="unbounded" namespace="##targetNamespace" processContents="lax" />
    </xs:sequence>
  </xs:complexType>
  <xs:element name="Description" type="xs:string" />
</xs:schema>

```


Note that the first version of the extensible schema is forwards-compatible with the second, and that the second is backwards-compatible with the first. This flexibility, however, comes at the expense of increased complexity. Extensible schemas allow us to make unforeseen changes to an XML language, but by the same token, they provide for requirements that may very well never arise; in so doing, they obscure the expressive power that comes from a simple design, and frustrate the meaningful representation of business information by introducing meta-informational container elements into the domain language.


We'll not discuss schema extensibility further here. Suffice to say, extension points allow us to make backwards- and forwards-compatible changes to schemas and documents without breaking service providers and consumers. Schema extensions do not, however, help us manage the evolution of a system when we need to make what is ostensibly a breaking change to a contract.


## Breaking Changes


As a value-add, our ProductSearch service includes in the search results a field indicating whether or not the product is currently in stock. The service populates this field using an expensive call into a legacy inventory system - a dependency which is costly to maintain. The service provider would like to remove this dependency, clean up the design, and improve the overall performance of the system - preferably without imposing any of the cost of change on the consumers. In speaking to the consumers' owners, the provider team discovers that none of the consumer applications actually do anything with this value; though expensive, it is redundant.


Unfortunately, with our existing setup, if we remove a required component - in this case, the *InStock* field - from our extensible schema, we will break existing consumers. To fix the provider, we have to fix the entire system: when we remove the functionality from the provider and publish a new contract, each consumer application will have to be redeployed with the new schema, and the interactions between services thoroughly tested. The ProductSearch service in this respect cannot evolve independently of its consumers: provider and consumers must all jump at the same time.


Our service community is frustrated in its evolution because each consumer implements a form of âhiddenâ coupling that naively reflects the entirety of the provider contract in the consumer's internal logic. The consumers, through their use of XSD validation, and to a lesser extent, static language bindings derived from a document schema, implicitly accept the whole of the provider contract, irrespective of their appetite for processing the component parts.


David Orchard provides some clues as to how we might have avoided this issue when he alludes to the Internet Protocol's Robustness Principle: âIn general, an implementation must be conservative in its sending behaviour and liberal in its receiving behaviourâ. We can augment this principle in the context of service evolution by saying that message receivers should implement âjust enoughâ validation: that is, they should only process data that contributes to the business functions they implement, and should only perform explicitly bounded or targeted validation of the data they receive - as opposed to the implicitly unbounded, âall-or-nothingâ validation inherent in XSD processing.


### Schematron


One way we can target or bound consumer-side validation is to assert pattern expressions along the received message's document tree axes, perhaps using a structural tree pattern validation language like [Schematron](http://www.schematron.com).  Using Schematron, each consumer of the ProductSearch service can programmatically assert what it expects to find in the search results:


```
<?xml version="1.0" encoding="utf-8" ?>
<schema xmlns="http://www.ascc.net/xml/schematron">

  <title>ProductSearch</title>
  <ns uri="urn:example.com:productsearch:products" prefix="p"/>
  
  <pattern name="Validate search results">
    <rule context="*//p:Product">
      <assert test="p:CatalogueID">Must contain CatalogueID node</assert>
      <assert test="p:Name">Must contain Name node</assert>
      <assert test="p:Price">Must contain Price node</assert>
    </rule>
  </pattern>

</schema>

```


Schematron implementations typically transform a Schematron schema such as this into an XSLT transformation that the message receiver can apply to a document to determine its validity.


Notice that this sample Schematron schema makes no assertions about elements in the underlying document for which the consuming application has no appetite. In this way, the validation language explicitly targets a bounded set of required elements. Changes to the underlying document's schema will not be picked up by the validation process unless they disturb the explicit expectations described in the Schematron schema, even if those changes extend to deprecating or removing formerly mandatory elements.


Here then is a relatively lightweight solution to our contract and coupling problems, and one that doesn't require us to add obscure meta-informational elements to a document. So let's roll back time once again, and reinstate the simple schema described at the outset of the article. But this time round, we'll also insist that consumers are liberal in their receiving behaviour, and only validate and process information that supports the business functions they implement (using Schematron schemas rather than XSD to validate received messages). Now when the provider is asked to add a description to each product, the service can publish a revised schema without disturbing existing consumers. Similarly, on discovering that the *InStock* field is not validated or processed by any of the consumers, the service can revise the search results schema - again without disturbing the rate of evolution of each of the consumers.


At the end of this process, the ProductSearch results schema looks like this:


```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns="urn:example.com:productsearch:products" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  elementFormDefault="qualified" 
  targetNamespace="urn:example.com:productsearch:products" 
  id="Products">
  <xs:element name="Products" type="Products" />
  <xs:complexType name="Products">
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Product" type="Product" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="Product">
    <xs:sequence>
      <xs:element name="CatalogueID" type="xs:int" />
      <xs:element name="Name" type="xs:string" />
      <xs:element name="Price" type="xs:double" />
      <xs:element name="Manufacturer" type="xs:string" />
      <xs:element name="Description" type="xs:string" />
    </xs:sequence>
  </xs:complexType>
</xs:schema>

```


## Consumer-Driven Contracts


The use of Schematron in the above example leads to some interesting observations about contracts between providers and consumers, with implications beyond document validation. In this section we draw out and generalize some of these insights and express them in terms of a pattern we call *Consumer-Driven Contract*.


The first thing to note is that document schemas are only a portion of what a service provider has to offer consumers to enable them to exploit its functionality. We call the sum total of these externalized exploitation points the *provider contract*.


### Provider Contracts


A provider contract expresses a service provider's business function capabilities in terms of the set of exportable elements necessary to support that functionality. From a service evolution point of view, a contract is a container for a set of exportable business function elements. A non-normative list of these elements includes:

- **Document schemas** We've already discussed document schemas in some detail. Next to interfaces, document schemas are the parts of a provider contract most likely to change as the service evolves; but perhaps because of this, they're also the parts we have most experience of imbuing with service evolution strategies such as extension points and document tree path assertions.
- **Interfaces** In their simplest form, service provider interfaces comprise the set of exportable operation signatures a consumer can exploit to drive the behaviour of a provider. Message-oriented systems typically export relatively simple operation signatures and push the business intelligence into the messages they exchange. In a message-oriented system, received messages drive endpoint behaviour according to semantics encoded in the message header or payload. RPC-like services, on the other hand, encode more of their business semantics in their operation signatures. Either way, consumers depend on some portion of a provider's interface to realise business value, and in consequence we must account for interface consumption when evolving our service landscape.
- **Conversations** Service providers and consumers exchange messages in conversations that compose one or more message exchange patterns such as request-response and fire-and-forget. Over the course of a conversation a consumer may expect the provider to externalize some state particular to the interaction in the messages that it sends and receives. For example, a hotel reservation service might offer consumers the ability to reserve a room at the outset of a conversation, and to confirm the booking and make a deposit in subsequent message exchanges. The consumer here might reasonably expect the service to ârememberâ the details of the reservation when engaging in these follow-on exchanges, rather than demand the parties repeat the entire conversation at each step in the process. As a service evolves, the set of conversational gambits available to provider and consumer might change. Conversations are thus candidates for being considered part of a provider contract.
- **Policy** Besides exporting document schemas, interfaces and conversations, service providers may declare and enforce specific usage requirements that govern how the other elements of the contract can be realised. Most commonly, these requirements relate to the security and transactional contexts in which a consumer can exploit a provider's functionality. The Web services stack typically expresses this policy framework using the [WS-Policy](http://www-128.ibm.com/developerworks/library/specification/ws-polfram/) generic model plus additional domain-specific policy languages such as [WS-SecurityPolicy](http://www-128.ibm.com/developerworks/webservices/library/specification/ws-secpol/), but in the context of our considering policies as candidates for being included in a provider contract, our definition of policy is specification and implementation agnostic.
- **Quality of service characteristics** The business value potential that service providers and consumers exploit is often evaluated in the context of specific quality of service characteristics such as availability, latency and throughput. We should consider these characteristics as likely constituents of a provider contract and account for them in our service evolution strategies.


The definition of contract here is a little broader than the one we might usually offer when talking about services, but from a service evolution perspective it usefully abstracts the significant forces that impact our problem domain. That said, the definition is not meant to be exhaustive in terms of the kinds of elements a provider contract might contain: it refers simply to a logical set of exportable business function elements that are candidates for including in a service evolution strategy. From a logical point of view, this set of candidate elements is open, but in practice internal or external factors, such as interoperability requirements or platform limitations, may constrain the type of elements a contract can contain. For example, a contract belonging to a service that conforms to the WS-Basic profile will likely not contain policy elements.


Notwithstanding any such constraints, the scope of a contract is determined simply by the cohesion of its member elements. A contract can contain many elements and be broad in scope, or focus narrowly on only a few, just so long as it expresses some business function capability.


How do we decide whether to include a candidate contractual element in our provider contract? We do so by asking ourselves whether any of our consumers might reasonably express one or more expectations that the business function capability encapsulated by the element continue to be satisfied throughout the service's lifetime. We've already seen how consumers of our example service can express an interest in parts of the document schema exported by the service, and how they might assert that their expectations regarding this contractual element continue to be met. Thus, our document schema is part of our provider contract.


Provider contracts have the following characteristics:

- **Closed and complete** Provider contracts express a service's business function capabilities in terms of the complete set of exportable elements available to consumers, and as such are closed and complete with respect to the functionality available to the system.
- **Singular and authoritative** Provider contracts are singular and authoritative in their expression of the business functionality available to the system.
- **Bounded stability and immutability** A provider contract is stable and immutable for a bounded period and/or locale (see the section âValidity of Data in Bounded Space and Timeâ in [Pat Helland's](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnbda/html/dataoutsideinside.asp) paper *Data on the Outside vs. Data on the Inside*).  Provider contracts typically use some form of versioning to differentiate differently bounded instances of the contract.


### Consumer Contracts


If we decide to account for consumer expectations regarding the schemas we expose when evolving our service - and consider it worth our provider knowing about them - then we need to import those consumer expectations into the provider. The Schematron assertions in our example look very much like the kinds of tests that, if implemented by the provider, might help ensure the provider continues to meet its commitments to its clients. By implementing these tests, the provider gains a better understanding of how it can evolve the structure of the messages it produces without breaking existing functionality in the service community. And where a proposed change would in fact break one or more consumers, the provider will have immediate insight into the issue and be better able to address it with the parties concerned, accommodating their requirements or providing incentives for them to change as business factors dictate.


In our example, we can say that the set of assertions generated by all consumers expresses the mandatory structure of the messages to be exchanged during the period in which the assertions remain valid for their parent applications. If the provider were possessed of this set of assertions, it would be able to ensure that every message it sends is valid for every consumer insofar as the set of assertions is valid and complete.


Generalizing this structure, we can distinguish what we have already called the *provider contract* from the individual contractual obligations that obtain in instances of provider-consumer relationships, which we will now call *consumer contracts*. When a provider accepts and adopts the reasonable expectations expressed by a consumer, it enters into a consumer contract.


![](consumerDrivenContracts/ConsumerDrivenContracts.jpg)


Figure 3: Consumer contracts


Consumer contracts have the following characteristics:

- **Open and incomplete** Consumer contracts are open and incomplete with respect to the business functionality available to the system. They express a subset of the system's business function capabilities in terms of the consumer's expectations of the provider contract.
- **Multiple and non-authoritative** Consumer contracts are multiple in proportion to the number of consumers of a service, and each is non-authoritative with regard to the total set of contractual obligations placed on the provider. The non-authoritative nature of the relationship extending from consumer to provider is one of the key features that distinguish a service-oriented architecture from a distributed application architecture. Service consumers must recognize that their peers in a service community are liable to consume the provider in ways quite different from their own. Peers may evolve at different rates and demand changes of the provider that potentially disturb the dependencies and expectations residing in other parts of the system. A consumer cannot anticipate how or when a peer will disturb the provider contract; a client in a distributed application has no such concerns.
- **Bounded stability and immutability** Like provider contracts, consumer contracts are valid for a particular period of time and/or location.


### Consumer-Driven Contracts


Consumer contracts allow us to reflect on the business value being exploited at any point in a provider's lifetime. By expressing and asserting expectations of a provider contract, consumer contracts effectively define which parts of that provider contract currently support the business value realized by the system, and which do not. This leads us to suggest that service communities might benefit from being specified in the first instance in terms of consumer contracts. In this view, provider contracts emerge to meet consumer expectations and demands. To reflect the derived nature of this new contractual arrangement, we call such provider contracts *consumer-driven contracts* or *derived contracts*.


The derivative nature of consumer-driven provider contracts adds a heteronomous aspect to the relationship between service provider and consumer. That is, providers are subject to an obligation that originates from outside their boundaries. This in no way impacts on the fundamentally autonomous nature of their implementations; it simply makes explicit the fact that services depend for success on their being consumed.


Consumer-driven contracts have the following characteristics:

- **Closed and complete** A consumer-driven contract is closed and complete with respect to the entire set of functionality demanded of it by its existing consumers. The contract represents the mandatory set of exportable elements required to support consumer expectations during the period in which those expectations remain valid for their parent applications.
- **Singular and non-authoritative** Provider contracts are singular in their expression of the business functionality available to the system, but non-authoritative because derived from the union of existing consumer expectations.
- **Bounded stability and immutability** A consumer-driven contract is stable and immutable in respect of a particular set of consumer contracts. That is to say, we can determine the validity of a consumer-driven contract according to a specified set of consumer contracts, effectively bounding the forwards- and backwards-compatible nature of the contract in time and space. The compatibility of a contract remains stable and immutable for a particular set of consumer contracts and expectations, but is subject to change as expectations come and go.


### Summary of Contract Characteristics


The following table summarizes the characteristics of the three types of contract described in this article:



| Contract | Open | Complete | Number | Authority | Bounded |
| Provider | Closed | Complete | Single | Authoritative | Space/time |
| Consumer | Open | Incomplete | Multiple | Non-authoritative | Space/time |
| Consumer-Driven | Closed | Complete | Single | Non-authoritative | Consumers |



### Implementation


The *Consumer-Driven Contract* pattern recommends building service communities using consumer and consumer-driven contracts. The pattern does not however specify the form or structure consumer and consumer-driven contracts should adopt, nor does it determine how consumer expectations are communicated to the provider and asserted during the provider's lifetime.


Contracts may be expressed and structured in several ways. In their simplest form, consumer expectations can be captured in a spreadsheet or similar document and implemented during the design, development and testing phases of a provider application. By going a little further and introducing unit tests that assert each expectation, we can ensure that contracts are described and enforced in a repeatable, automated fashion with each build. In more sophisticated implementations, expectations can be expressed as Schematron- or WS-Policy-like assertions that are evaluated at runtime in the input and output pipelines of a service endpoint.


As with the structure of contracts, we have several options when it comes to communicating expectations between providers and consumers. Since the *Consumer-Driven Contract* pattern is implementation agnostic we could, given the appropriate organizational setup, transmit expectations simply by talking to other teams, or using email. Where the number of expectations and/or consumers grows too large to manage in this manner, we may consider introducing a contract service interface and implementation into the connected systems' infrastructure. Whatever the mechanism, it is likely communications will be conducted out-of-band and prior to any conversations that exercise the business functionality of the system.


### Benefits


Consumer-driven contracts offer two significant benefits when it comes to evolving services. First, they focus the specification and delivery of service functionality around key business value drivers. A service is of value to the business only to the extent it is consumed. Consumer-driven contracts tie service evolution to business value by asserting the value of exportable service community elements - the things that consumers require of providers to do their job. As a result, providers expose a lean contract that is clearly aligned with the business goals that underpin their consumers. Change - service evolution - only emerges where consumers express a clear need.


Of course, our ability to start with a minimal set of lean requirements and evolve our service as and when consumers demand presupposes that we are in a position to evolve, deploy and operate the service in a controlled and efficient manner. This is where the *Consumer-Driven Contract* pattern provides a second key benefit. Consumer-driven provider contracts give us the fine-grained insight and rapid feedback we require to plan changes and assess their impact on applications currently in production. In practice, this allows us to target individual consumers and provide incentives for them to relinquish an expectation that is stopping us from making a change that is not currently backwards- and/or forwards-compatible. By deriving our service providers from consumer contracts, we imbue them with a repository of knowledge and a feedback mechanism that we can draw on during the operations part of the system lifecycle.


### Liabilities


In this article we've identified the motivation for introducing consumer-driven contracts into the service landscape, and thereafter described how the *Consumer-Driven Contract* pattern addresses the forces that determine service evolution. We will end by discussing the scope of the pattern's applicability, together with some of the issues that may arise while implementing consumer and consumer-driven contracts.


The *Consumer-Driven Contract* pattern is applicable in the context of either a single enterprise or a closed community of well-know services: more specifically, an environment in which providers can exert some influence over how consumers establish contracts with them. No matter how lightweight the mechanisms for communicating and representing expectations and obligations, providers and consumers must know about, accept and adopt an agreed upon set of channels and conventions. This inevitably adds a layer of complexity and protocol dependence to an already complex service infrastructure.


We've suggested that systems built around consumer-driven contracts are better able to manage breaking changes to contracts. But we don't mean to suggest that the pattern is a cure-all for the problem of breaking changes: when all's said and done, a breaking change is still a breaking change. We do believe, however, that the pattern provides many insights into what actually constitutes a breaking change, and as such may serve as the foundation for a service versioning strategy. Moreover, as we've already discussed, service communities that implement the pattern are better placed to anticipate the effects of service evolution. Provider development and operations teams in particular can more effectively plan their evolutionary strategies - perhaps by deprecating contractual elements for a specific period and simultaneously targeting recalcitrant consumers with incentives to move up to new versions of a contract.


Consumer-driven contracts do not necessarily reduce the coupling between services. Loosely-coupled services are relatively independent of one another, but remain coupled nonetheless. What the pattern does do, however, is excavate and put on display some of those residual, âhiddenâ couplings, so that providers and consumers can better negotiate and manage them.


We've discussed ways in which consumer and consumer-driven contracts express business value. But we should make clear that we do not regard such contracts as an index or measure of business value - they are not a business metric = and despite some superficial resemblances to specifications such as [WS-Agreement](http://www.gridforum.org/Meetings/GGF11/Documents/draft-ggf-graap-agreement.pdf) and [WSLA](http://www.research.ibm.com/journal/sj/431/dan.html), they are not intended to express Service Level Agreements.  The underlying assumption here is that services, by themselves, are of no value to the business; their value is in being consumed. By specifying services closer to where they are being used - by consumers - we aim to exploit business value in a lean, just-in-time fashion.


Finally, we should point out that there is a risk that allowing consumer contracts to drive the specification of a service provider may undermine the conceptual integrity of that provider. Services encapsulate discrete, identifiable, reusable business functions whose integrity should not be compromised by unreasonable demands falling outside their mandate.


---
