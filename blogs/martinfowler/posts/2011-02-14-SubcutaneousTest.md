---
title: "Subcutaneous Test"
description: "I usesubcutaneous testto mean a test that operates just under   the UI of an application. This is particulary valuable when doing   functional testing of an application: when you want to test   end-to"
date: 2011-02-14T00:00:00
tags: ["test categories"]
url: https://martinfowler.com/bliki/SubcutaneousTest.html
slug: SubcutaneousTest
word_count: 93
---


I use *subcutaneous test* to mean a test that operates just under
  the UI of an application. This is particulary valuable when doing
  functional testing of an application: when you want to test
  end-to-end behavior, but it's difficult to test through the UI
  itself.


Subcutaneous testing can avoid difficulties with
  hard-to-test presentation technologies and usually is much faster
  than testing through the UI. The big danger is that, unless you are
  a firm follower of keeping all useful logic out of your UI,
  subcutaneous testing will leave important behavior out of its test.
