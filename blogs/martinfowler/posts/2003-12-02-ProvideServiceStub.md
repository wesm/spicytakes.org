---
title: "Provide Service Stub"
description: "An important thought for anyone building services for a service 	oriented architecture. When you build your service, also build aservice stubthat your clients can use to test against. Such a stub 	sho"
date: 2003-12-02T00:00:00
tags: ["application integration"]
url: https://martinfowler.com/bliki/ProvideServiceStub.html
slug: ProvideServiceStub
word_count: 98
---


An important thought for anyone building services for a service
	oriented architecture. When you build your service, also build a
	[service stub](https://martinfowler.com/eaaCatalog/serviceStub.html) that your clients can use to test against. Such a stub
	should provide canned responses to a fixed set of requests, simulate
	error conditions, and be runnable on a client's machine. You'll need
	to ensure that the stub mimics the true systems behavior
	properly. By providing a stub for your clients, you make it much
	easier for your clients to use your service; which of course means
	that your service is more likely to be used.
