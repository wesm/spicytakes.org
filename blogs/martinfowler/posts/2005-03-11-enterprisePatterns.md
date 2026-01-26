---
title: "Patterns in Enterprise Software"
description: "A personal survey of various efforts to catalog patterns  for enterprise software development."
date: 2005-03-11T00:00:00
url: https://martinfowler.com/articles/enterprisePatterns.html
slug: enterprisePatterns
word_count: 1154
---


In recent years there's been a small but useful growth in
		describing patterns for the development of enterprise systems. On
		this page I keep a list of the most notable catalogs on these
		patterns and some thoughts on the broad interrelationships between them.


There's no formal organization tying these writers together,
		but we do have a strong informal connection - frequently reviewing
		each others' work. We've often wondered if we should set up some
		more organized group, but haven't really summoned up enough energy
		around it to actually make anything happen. Just writing our own
		work is quite hard enough!


Different people have different expectations about what
		patterns are good for and why they are interesting. I described my
		view of this in a [column for IEEE Software](https://martinfowler.com/ieeeSoftware/patterns.pdf).


I'm listing the catalogs here, because these are ones I know at
		least fairly well and am comfortable with. I don't intend this as a complete list of pattern catalogs in this space.


## Catalogs



| [Patterns of Enterprise Application
Architecture](https://martinfowler.com/eaaCatalog/) | Concentrates on Enterprise Application Architecture in the
context of a layered architecture. Main sections cover domain logic,
web presentations, database interaction, offline concurrency (by David
Rice) and distribution. Database interaction is the largest section
with many patterns on object-relational mapping issues. |
| (Fowler) |
| [Core J2EE Patterns](http://www.corej2eepatterns.com/) | Enterprise Application Architecture patterns in the context
of the Java J2EE platform. Although the patterns are focused around
the J2EE platform, the patterns are usually equally applicable (albeit
with a twist) to other enterprise application platforms. |
| (Alur, Crupi, and Malks) |
| [Enterprise Integration Patterns](http://www.enterpriseintegrationpatterns.com/) | I've increasingly come to the view that integration through
asynchronous messaging is one of the most effective ways to integrate
disparate enterprise applications. EIP is a foundation collection of
patterns for this approach. |
| (Hohpe and Woolf) |
| [Microsoft Enterprise Solution
Patterns](http://msdn.microsoft.com/architecture/patterns/default.aspx?pull=/library/en-us/dnpatterns/html/esp.asp) | Microsoft's first collection of enterprise software patterns.
Sections include patterns on Web Presentation, Deployment, and
Distributed Systems. |
| (Trowbridge, Mancini, Quick, Hohpe, Newkirk, and
Lavigne) |
| [Microsoft Data Patterns](http://msdn.microsoft.com/architecture/patterns/default.aspx?pull=/library/en-us/dnpatterns/html/dp.asp) | A collection of patterns on data movement: replication and
synchronization. |
| (Teale, Etx, Kiel and Zeitz) |
| [Microsoft Integration Patterns](http://msdn.microsoft.com/en-us/library/ms978729.aspx) | Microsoft's take on integration patterns. Sections cover
strategies for an integration layer, approaches to system connections,
and topologies for integration. |
| (Trowbridge, Roxburgh, Hohpe, Manolescu and
Nadhan) |
| [Domain Driven Design](http://domainlanguage.com/) | Building an object-oriented Domain Model is a  popular
approach to organizing domain logic. It works particularly well with
complex domains. It's downside is that it is difficult to do well.
These patterns describe how to think about building and structuring a
rich domain model, as well as how to recognize and overcome the
real-world obstacles that too-often prevent people from employing the
modeling principles they know. |
| (Evans) |
| [Analysis Patterns](https://martinfowler.com/books/ap.html) | See enough domain models, and you see certain kinds of
			structures repeatedly. This book was my attempt to capture these
			commonalities in the form of patterns. In lots of ways it's very
			much in need of an update, but the basic ideas are still pretty
			sound. If find this material useful, do make sure you look at
			the newer supplementary material that I put on my website. |
| (Fowler) |
| [Data Model Patterns](http://www.amazon.com/exec/obidos/ASIN/0932633293) | Common patterns in data models. Since these are developed
			from a very conceptual approach, the patterns are useful for
			object modeling as well as data modeling. |
| (Hay) |
| [Gang of Four](http://www.amazon.com/exec/obidos/ASIN/0201633612/) | The first, and most used, patterns book. These are
			mostly fundamental patterns which are not specifically for
			enterprise software development, but the enterprise patterns
			reference them widely. |
| (Gamma, Helm, Johnson, and Vlissides) |
| [POSA](http://www.amazon.com/exec/obidos/ASIN/0471958697) | Particularly influential for its work on architectural
			patterns. Layers (for enterprise applications) and pipes and
			filters (for messaging) are foundations for much enterprise
			patterns work. |
| (Buschmann,  Meunier,  Rohnert, Sommerlad, and
			Stal) |



## Aspects of Enterprise Software


The catalogs cover various different aspects of enterprise
		software development. Here's another view of the catalogs,
		starting from these various aspects.


### Enterprise Application Architecture


Enterprise Application is the name I give to a certain
				class of software systems: the data intensive software systems
				on which so many businesses run. Another, and perhaps better,
				name for them is Information Systems since these are systems
				that process and manipulate information.


Most books on EAA begin by breaking an enterprise
				application into logical layers. This layering structure then
				drives other design decisions within and between the
				layers. As such it's no surprise that patterns tend to be
				similarly organized through layers. Each author has their own
				layering structure, but there are recognizable similarities
				between the layering structures.


It's surprisingly common that people confuse the term
				Enterprise Architecture with Enterprise Application
				Architecture. That second A-word is all important. EAA is
				about building a single application. [Enterprise Architecture](https://martinfowler.com/bliki/EnterpriseArchitecture.html)
				is a quite different animal.



| [Patterns of Enterprise Application
Architecture](https://martinfowler.com/eaaCatalog/) | Looks at EAA from a technology independent view. |
| [Core J2EE Patterns](http://www.corej2eepatterns.com/) | This was the first book to concentrate on EAA and does so
				from the context of the J2EE platform. |
| [Microsoft Enterprise Solution
Patterns](http://msdn.microsoft.com/architecture/patterns/default.aspx?pull=/library/en-us/dnpatterns/html/esp.asp) | Looks at EAA from the angle of .NET. |



### Enterprise Integration


Enterprise Applications are somewhat independent beasts,
				but to function they do need to work together. Stitching
				together independently developed EAs is the work of
				integration. Often you need to integrate applications that
				weren't design with any integration in mind, let alone the
				specific one that you are using, or they expect to integrate
				using a technology that you're no using.



| [Enterprise Integration Patterns](http://www.enterpriseintegrationpatterns.com/) | Patterns for messaging, which the authors (and I) see as
				the most promising way to do integration. |
| [Microsoft Integration Patterns](http://msdn.microsoft.com/en-us/library/ms978729.aspx) | Strategies for doing integration using Microsoft's technology. |
| [Microsoft Data Patterns](http://msdn.microsoft.com/architecture/patterns/default.aspx?pull=/library/en-us/dnpatterns/html/dp.asp) | Patterns for data replication and synchronization, which
				are two valuable techniques for integration. |



### Domain Logic


One of the most important, yet often forgot, aspects of
				enterprise applications is the domain logic. These are the
				business rules, validations, and calculations that operate on
				the data as it is brought into an information system or
				displayed by it. For simple database filing systems there is
				often little or no domain logic. However for many systems
				there is often quite complex domain logic, and this logic is
			subject to regular change as business conditions change.



| [Patterns of Enterprise Application
Architecture](https://martinfowler.com/eaaCatalog/) | One section outlines principal patterns for organizing
				domain logic. |
| [Domain Driven Design](http://domainlanguage.com/) | Goes into detail on using Domain Models: the most
				sophisticated domain logic pattern and the one that's the most
				suitable for complex logic. |
| [Analysis Patterns](https://martinfowler.com/books/ap.html) | Patterns that show examples of domain models. |
| [Data Model Patterns](http://www.amazon.com/exec/obidos/ASIN/0932633293) | More patterns that show examples of domains, from a data
				modeling approach. |



---
