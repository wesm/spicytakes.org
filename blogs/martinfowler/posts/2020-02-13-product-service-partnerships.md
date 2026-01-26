---
title: "Product-Service Partnerships"
description: "When customer companies buy software products, they usually need   skilled staff to install them. This staff is usually provided by a service   provider company, since software product vendors don't f"
date: 2020-02-13T00:00:00
tags: ["enterprise architecture"]
url: https://martinfowler.com/articles/product-service-partnerships.html
slug: product-service-partnerships
word_count: 3390
---


If I'm a senior IT executive at a large enterprise (someone like Shell,
    United Airlines, or Walmart) I'll need to acquire some large software
    systems to manage my business. Often I may choose to buy these systems from
    a *product vendor* who sells this kind of thing to many such companies
    (someone like SAP, Oracle, or SalesForce). However buying these kinds of
    large-enterprise packages isn't as simple as popping over to the app store
    with a credit card. Such systems require a lot work to install, configure,
    and customize. I could train up my own staff, but that would probably take
    too long, so I'd rather have staff from another firm who have more
    experience. So for this I'd probably engage with a large software *service
    provider* (think Accenture, Wipro, or IBM).


In this article, I'm representing the business relationships
      as a simple three-role model. When I use these names in the article,
      they refer to these kinds of roles. The example companies are all large
      companies, since they are well-known, but smaller companies also play
      these roles.


Customer


The company buying the product and related services to
        improve their operational outcome


Walmart, Southwest Airlines, Citibank


Product Vendor


Builds and sells a software product


SAP, Oracle, SalesForce


Service Provider


Sells capability through skilled staff to build and
        configure software systems


Accenture, InfoSys, Thoughtworks


This interaction is so common that the product vendors and software
    services firms often agree to partnership deals, where they agree to work
    together to support a particular installation, or to pursue customers
    companies across a larger business segment.


Although these arrangements are common, I don't think they are well
    understood as well as they could be. As someone who works primarily in
    custom software development, where these are less significant, I include
    myself in the list of relative ignorance. That ignorance is one reason to explore them
    a bit. Another reason to better understand them is that these kinds of
    arrangements are becoming more significant in the custom software world with
    the shift to cloud computing. We're now seeing similar partnership
    arrangements with cloud vendors having a significant impact on companies
    like Thoughtworks that focus on custom software delivery.


The simplest case of a product-services partnership is where the
    partnership is formed for a single customer engagement. In this situation the
    partnership could be formed by the customer telling the product vendor to
    work with the customer's preferred service provider. Or the service and
    product companies might form the partnership when they see the opportunity,
    possibly in competition with a rival product-service match-up.


Things get more involved when a service provider and product company
    agree a longer term partnership arrangement. Here they agree a deal that
    will work for several customers, perhaps globally, or perhaps limited to a
    particular business sector (eg airlines, banks) or geography (eg East
    Asia).


A significant factor that leads to differences in these arrangements is
    the relative size of the companies involved. A small service provider is
    going to have a different relationship with SAP than Wipro does. I'll start
    by assuming two large companies, and then talk about how things differ when
    we get to varied sizes.


## Large organizations have divisions dedicated to partners


When both companies are large partnership arrangements will usually be
      non-exclusive. A company like Accenture will do ERP work with SAP and
      Oracle, and indeed do substantial work with both - each one involving
      multiple customers world-wide. The scale of these partnerships means that
      the service provider will often create whole organization structures just
      for a particular partner (in the mid 2000s, IBM Global Services had around
      20,000 staff dedicated to working with SAP).


So a service provider might have a banking division, that focuses on that
      sector, and an Oracle division that focuses on Oracle's business software
      platforms (which is a whole different animal to its database software). If a
      bank is looking at reforming its HR systems, it would talk to a contact in
      the banking division. Folks in that part of the service company try to be
      relatively independent of the software vendors. If the customer had decided
      to implement PeopleSoft (an Oracle subsidiary that does HR software) then
      the banking contact would introduce people from the service company's Oracle
      division as part of the work.


In the product vendor organization, large vendors will also have a
      dedicated organization dedicated to working with partners. These will
      provide education and product news, help with sales pursuits, and coordinate
      on delivery work.


In both cases, it's important to remember that a partnership
      arrangement isn't just about negotiating and signing a deal. It's a
      on-going relationship that requires constant work to maintain.


## Why don't product vendors build their own services division?


From the product vendor's point of view, the service provider primarily
      acts as a delivery organization, providing the staff to do the installation,
      configuration, and customization which complex software products need.
      Product vendors don't tend to like building their own delivery organizations
      for several reasons. For a start the work tends to be have much lower
      margins compared to selling product - so the vendor would rather invest in
      improving its product and supporting sales and marketing. Secondly projects to
      install large software products tend to
      carry a lot of risk - so it's good for the product vendor to have an
      arms-length relationship with any delivery project. That way, when things
      wrong, it's the service provider that carries the responsibility.


A further financial reason is the knotty issue of revenue recognition.
      This is the legal and accounting principles that govern when you can
      recognize some revenue on your balance sheet. If you sell some software, you
      immediately count it as revenue. But if you sell services, then even if you
      sign a contract today to do some work in six months time, you can't show
      that revenue in your accounts until that work is done six long months away.
      If you sell a deal that bundles software services with the product sale,
      then it's hard to avoid the revenue from the software sale also not being
      recognized for six months. This is a considerable incentive to a product
      vendor to ensure there is a bright line between the software sale and any
      delivery work - having a separate services provider helps keep that line
      clear.


The complications of a growing a delivery arm compounds once that delivery
      organization has to integrate products from multiple companies. Now a
      product vendor finds that not just is there all the risks involved with
      their own familiar product, but extra risks from other companies, some of
      which may be involved in competitive relationships.


Certainly product vendor companies commonly make an attempt to build up a
      services arm, since that way they get a deeper relationship with the
      customer. And most customers would rather work directly with the product
      vendor, since that way they have a more direct line to the product vendor
      should things go wrong. But the common pattern seems to be that such efforts
      don't usually last long, as the product vendor runs into the problems I
      described earlier, and pulls the plug on the effort. (IBM would be a notable
      exception to this pattern.)


Service providers, of course, are used to the business model of billing
      for professionals' time, and are also used to the complications of managing
      projects and client relationships. The appeal of a partnership for them is
      more defensive. When competing for an product installation engagement, customers
      naturally look for expertise and connection with the software product. A
      partnership arrangement provides that assurance, and lacking it raises
      questions.


## Product vendors look for dedicated staff with certifications


The number of staff in the service provider that are dedicated to the
      product is an important part of the relationship. Most product vendors have
      some kind of certified training program in the product. The quality of these
      programs is often poor, thus acquiring a bunch of certifications often
      doesn't correspond with competence for the task at hand. Even a well-run
      training course will tend to focus on the quirks of an individual product,
      rather than broader technical principles which are usually more important.
      Building software requires lots of decisions and this kind of training is
      not likely to discuss superior approaches that don't involve the vendor's
      product. Certification targets often appear in partnership arrangements,
      indicating how many staff from the service provider have various levels of
      certification. Certified training is revenue for the product vendor, an
      indication of the commitment of the service provider to the relationship,
      and, even with all the common flaws, ensures that these staffers have at
      least a basic knowledge of the product features.


## Some partnerships involve commissions


Some partnership deals involve commissions - which can go either way. A
      service provider that sells work, either the initial project or follow-on
      work to install additional modules or projects, may earn a sales commission
      on the software sale. Similarly a product vendor that introduces a services
      company may earn a commission on the service company's billed hours. Some
      service providers make a commitment to not being paid commissions in order
      to preserve their client-focused advisory services. This is easier to
      sustain if they have significant work with several competing software
      vendors.


But financial incentives exist even without explicit commissions.
      Software vendors typically rank service providers by allocating revenues
      that they feel the provider has influenced. This ranking will play into their
      referrals and providing the service provider access to (and perhaps
      influence on) product plans and technical support. Similarly leaders of a
      service provider's division that works with a product vendor will be
      assessed on how much billable work they sell and the margins they sell that
      work for.


As well as delivery work, partnerships often involve joint sales and
      marketing campaigns, attempting to take advantage of both companies' product
      positions to generate more sales for both. It seems, however, that these
      efforts usually don't lead to much. Nobody believes the go-to-market plan
      until the first deal is made. Even then there is often little trust between
      the organizations. If a deal like this works, it's usually due to an unusual
      circumstance, often based on a particularly good working relationship
      between the people involved. Both sides have to recognize that they are
      dealing with only one part of the partner organization. Other parts of the
      service provider will not want to jeopardize their client relationships just
      to sell some product-based delivery work, other parts of the product company
      don't want to damage their relationship with other service providers. As
      with so much in business, how smoothly the partnership works is primarily a
      function of the personal relationships of the leaders involved in the
      partner organizations.


## Is a service provider faced with conflict of interest?


Service providers are hired both to carry out implementation work and
      to give advice. This advice includes what modules of a complex system to
      implement, and which products should be chosen to support a business
      function. Whenever a provider gives this advice, they should consider the
      customer's best interests. But partnerships with product vendors introduce
      a conflict of interest. This conflict is most obvious when sales
      commissions are involved. It's hard for a consultant to advise against a
      product that brings in revenue if that forgone revenue comes up during
      annual performance reviews.


Even without an explicit sales commission, partnerships can have an
      influence. Vendors do rank their service partners based on how much
      revenue they are have influenced. Advising customers against a partner's
      product will lead to a reduced level of partnership, which may harm sales
      prospects elsewhere.


My sources who worked with large service providers felt that this was
      mostly a non-issue. They pointed out that most advisory work of this
      nature was done by different divisions the service provider to those that
      managed the partnership. If a service provider has partnerships with
      multiple competing product vendors, then the inclination to spin advice is
      much reduced.


## Large service providers look for exclusive deals with small product vendors


So far, I've concentrated on the case where we have large service
      providers partnering with large product vendors. Once we start looking at
      differently sized corporations, then some changes appear. The biggest
      shift is on exclusivity. The smaller partner matters less to the larger
      partner, and so often signs an agreement that they will work exclusively
      with that partner, at least for some subset of the overall market (a
      business sector, or geographical area).


The purpose of the deal changes as well, at least for the service
      provider. There's no market force that makes a small product vendor
      mandatory for the service provider. So the reason to partner with one is
      if they feel the product gives them an important edge in their services
      business. By having exclusive access to that edge, they can compete better
      against other service providers in that market segment. The service
      provider will often look to build a suite of smaller products and market
      their experience in integrating them with many customers.


The larger service provider can also wield more influence over product
      strategy, prioritizing features the service provider thinks are important
      for its clientele. They can also get a higher priority for technical
      support.


On the product vendor's side, the reasons for a partnership are similar
      to larger companies, but with a higher weighting to the sales and marketing
      side. Setting up a sales and marketing organization is expensive,
      especially if you are selling to large enterprises. A service
      provider already has the right contacts, so if you can impress them with a
      unique capability, then they will do this work for you. You lose direct
      access to these customers, and supporting the service provider can be a
      lot of work, but for most companies it's the better deal to do. Customers
      are often wary of small product vendors, as they are concerned that they
      may not last. Partnering with a large services firm reduces that risk (or at
      least the perception of it).


## Large product vendors similarly want exclusivity with small service providers


Unequal sizes work the other way too. While smaller service providers
      don't have the existing reach that the big companies do, the product
      vendor can gain by getting a much greater degree of alignment from the
      service company. This alignment often includes exclusivity ensuring the
      service company is a advocate for the product. It may include language
      that makes it a firing offense for employees of the service provider from
      criticizing the product. This close relationship is likely to lead to a
      more energetic sales effort from the service company and the ability for
      the product vendor to take a larger slice of their consulting fees for
      referring customers to them.


## The impact of the cloud


The rise of the big cloud vendors, (Amazon, Google, and Microsoft)
      extends the scope of partnerships with service providers. This is
      particularly relevant to those developing custom software. Partnership
      arrangements have been around in this sector for a while - notably
      partnership with Microsoft in the use of their development stack, and with
      the big database vendors. But there was also considerable scope for using
      open-source tools, which avoided any need for vendor partnerships around
      languages and frameworks.


With the big clouds, this is no longer the case. Custom software is
      increasingly designed to run on a cloud vendor's stack, requiring detailed
      knowledge of the services available and how to use them effectively. There
      is much to be gained by moving infrastructure management to companies that
      are specialized in doing it well, but their influence reaches
      everyone involved with software. It's almost impossible for a  service
      provider to avoid the need to engage in a partnership with at least one of
      these vendors.


The cloud business model adds an extra twist for the financial aspects
      of partner assessment. With software vendors, revenue comes primarily for
      licenses, once the license fee is paid, that settles the revenue aspect.
      But clouds offer a pay-for-usage model. Since, even without commissions,
      service providers are rated by how much revenue they generate, it sets up
      some tricky incentives. If I'm designing a system that processes alerts
      from lots of sensors, do I program the sensors to only send alerts to the
      cloud to reduce processing costs when my partnership with the cloud vendor
      encourages me to send all the signals there?


## What this means for the customer


If you're a customer of either service providers or product vendors,
      you'll need to understand how these partnership deals work. Indeed it's
      expected of you. I asked one source about the question of whether a
      service provider's partnership with a vendor was a conflict of interest
      when they gave advice to their customers. They answered by saying that
      since customer CTOs knew how this game was played, they didn't need to
      worry about any such conflict.


Transparency is a vital first step. Customers should insist that
      partners make the terms of their partnership clear, so the customer can
      judge how the partnership is in the customer's interest. If there are any
      sales commissions involved, these should be disclosed to the customer so
      they know how to interpret statements from the partners - this is
      essential if the service provider is working as an adviser that has
      influence over adoption and scope of the product vendor's wares.


My sources who've worked in large service providers didn't consider
      partnerships led to a conflict of interest since they partnered with
      several competing vendors. If I were a customer, I would be skeptical. In
      particular I would need to know the nature of their partnership deals with
      various product vendors, and be wary of any advice concerning non-partner
      product vendors that are competing with partners.


When partners are working on a project together, it's important that
      it's clear what each partner is responsible for and how they are going to
      resolve any disputes. This allocation of responsibilities should be clear
      to the customer, so the customer knows who to go to resolve any problems.
      If there aren't clear lanes of responsibility, that should be a red flag -
      if these things aren't sorted out early things will only get worse should
      the effort run into difficulties later.


The pressure from product companies to require service provider staff
      attend certified training can lead to staff who may be familiar with the
      surface features of the product, but not the underlying technical
      principles. This can lead to a surface competence, that in turn leads to a
      less effective delivery. Customers should be wary of judging competence
      via certifications, and instead probe for staff that understand technical
      issues in more depth - enough for them to be able to build alternatives to
      products in appropriate circumstances.


A wise service provider or product vendor realizes that to ensure
      long-term success for their work, they need to focus on improving the
      customer's performance in their work - not merely shipping product or
      selling people's time. As the current zeitgeist has it - they need to
      focus on [Outcome Over Output](https://martinfowler.com/bliki/OutcomeOverOutput.html). It is, however,
      difficult to set up organizations to do this. A service provider typically
      bills by the employee-hour (output) - which isn't very well aligned with a
      customer outcome. The reason this happens is because it's much harder to
      come up with any kind of financial measure that's tied to outcome, let
      alone to allocate the vendor's contribution to that. If this is a problem
      for direct customer relationships, it's even harder for product-service
      partnerships. The inevitable result is that the core assessment of the
      success of the partnership deal is based on product-service output, and
      customer outcome gets pushed even further into the background. Any energy
      that either of the partners might invest in understanding customer outcome
      is reduced as the partners worry about managing the partnership.


Service-product partnerships have been part of the IT world for
      decades, but the rise of cloud computing makes them more prominent. Any
      software service company has to figure out how to work with the major
      cloud vendors, and that will usually result in a partnership arrangement.
      Customers need to be aware of this, and demand transparency from both
      service providers and their cloud vendors. As the businesses become
      increasingly digital, they need a clear understanding of how their
      critical suppliers work.


---
