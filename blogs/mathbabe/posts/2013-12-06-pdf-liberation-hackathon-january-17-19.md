---
title: "PDF Liberation Hackathon: January 17-19"
date: 2013-12-06
url: https://mathbabe.org/2013/12/06/pdf-liberation-hackathon-january-17-19/
word_count: 728
---


*This is a guest post by Marc Joffe,* *the principal consultant at [Public Sector Credit Solutions](http://www.publicsectorcredit.org/), an organization that provides data and analysis related to sovereign and municipal securities. Previously, Joffe was a Senior Director at Moody’s Analytics.*


As Cathy has [argued](https://mathbabe.org/2012/01/11/open-models-part-1/), open source models can bring much needed transparency to scientific research, finance, education and other fields plagued by biased, self-serving analytics. Models often need large volumes of data, and if the model is to be run on an ongoing basis, regular data updates are required.


Unfortunately, many data sets are not ready to be loaded into your analytical tool of choice; they arrive in an unstructured form and must be organized into a consistent set of rows and columns. This cleaning process can be quite costly. Since open source modeling efforts are usually low dollar operations, the costs of data cleaning may prove to be prohibitive. Hence no open model – distortion and bias continue their reign.


Much data comes to us in the form of PDFs. Say, for example, you want to model student loan securitizations. You will be confronted with a large number of PDF servicing reports that look like [this](https://www.salliemae.com/assets/about/investors/debtasset/SLM-Loan-Trusts/11-15/2013-1/131QT0913.pdf). A corporation or well funded research institution can purchase an expensive, enterprise-level ETL (Extract-Transform-Load) tool to migrate data from the PDFs into a database. But this is not much help to insurgent modelers who want to produce open source work.


Data journalists face a similar challenge. They often need to extract bulk data from PDFs to support their reporting. Examples include IRS Form 990s filed by non-profits and budgets issued by governments at all levels.


The data journalism community has responded to this challenge by developing software to harvest usable information from PDFs. Examples include [Tabula](http://tabula.nerdpower.org/), a tool written by Knight-Mozilla OpenNews Fellow Manuel Aristarán, [extracts data from PDF tables](http://source.opennews.org/en-US/articles/introducing-tabula/) in a form that can be readily imported to a spreadsheet – if the PDF was “printed” from a computer application. Introduced earlier this year, Tabula continues to evolve thanks to the volunteer efforts of Manuel, with help from OpenNews Fellow Mike Tigas and New York Times interactive developer Jeremy Merrill. Meanwhile, [DocHive](https://github.com/raleighpublicrecord/dochive/tree/master/dochive), a tool whose continuing development is being [funded](http://raleighpublicrecord.org/editors-notebook/2013/06/20/new-grant-to-support-dochive-project/) by a Knight Foundation grant, addresses PDFs that were created by scanning paper documents. DocHive is a project of Raleigh Public Record and is led by Charles and Edward Duncan.


These open source tools join a number of commercial offerings such as [Able2Extract](http://www.investintech.com/prod_a2e.htm) and [ABBYY Fine Reader](http://finereader.abbyy.com/) that extract data from PDFs. A more comprehensive list of open source and commercial resources is available [here](http://pdfliberation.wordpress.com/).


Unfortunately, the free and low cost tools available to modelers, data journalists and transparency advocates have limitations that hinder their ability to handle large scale tasks. If, like me, you want to submit hundreds of PDFs to a software tool, press “Go” and see large volumes of cleanly formatted data, you are out of luck.


It is for this reason that I am working with The Sunlight Foundation and other sponsors to stage [the PDF Liberation Hackathon from January 17-19, 2014](https://www.eventbrite.com/e/pdf-liberation-hackathon-2014-tickets-9111078481). We’ll have hack sites at [Sunlight’s Washington DC office](http://maps.google.com/maps?espv=210&es_sm=93&q=1818+N+Street+NW,+Suite+300+Washington,+DC+20036&um=1&ie=UTF-8&hq=&hnear=0x89b7b7b877b593e5:0x83b82edfc6b4df38,1818+N+St+NW+%23300,+Washington,+DC+20036&gl=us&sa=X&ei=FA2dUt2qG9jboATX14LwCQ&ved=0CC4Q8gEwAA) and at [RallyPad](https://www.facebook.com/Rally/info) in San Francisco. Developers can also join remotely because we will publish a number of clearly specified PDF extraction challenges before the hackathon.


Participants can work on one of the pre-specified challenges or choose their own PDF extraction projects. Ideally, hackathon teams will use (and hopefully improve upon) open source tools to meet the hacking challenges, but they will also be allowed to embed commercial tools into their projects as long as their licensing cost is less than $1000 and an unlimited trial is available.


Prizes of up to $500 will be awarded to winning entries. To receive a prize, a team must publish their source code on a GitHub public repository. To join the hackathon in DC or remotely, please sign up at [Eventbrite](https://www.eventbrite.com/e/pdf-liberation-hackathon-2014-tickets-9111078481); to hack with us in SF, please sign up via this [Meetup](http://www.meetup.com/Open-Source-Finance/events/145743722/). Please also complete our [Google Form survey](https://docs.google.com/forms/d/1rXggRHhlprYfHsB64dZ-zpVrhqMitcPkN1vEMD7_03k/viewform). Also, if anyone reading this is associated with an organization in New York or Chicago that would like to organize an additional hack space, please [contact](mailto:%20marc@publicsectorcredit.org) me.


The PDF Liberation Hackathon is going to be a great opportunity to advance the state of the art when it comes to harvesting data from public documents. I hope you can join us.
