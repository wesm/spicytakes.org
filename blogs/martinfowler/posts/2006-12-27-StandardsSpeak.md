---
title: "Standards Speak"
description: "If you read many standards documents, apart from the need for 	excessive amounts of coffee, you'll also need to be wary of the 	overloaded meaning of some words."
date: 2006-12-27T00:00:00
tags: ["writing"]
url: https://martinfowler.com/bliki/StandardsSpeak.html
slug: StandardsSpeak
word_count: 176
---


If you read many standards documents, apart from the need for
	excessive amounts of coffee, you'll also need to be wary of the
	overloaded meaning of some words.


Standards use **shall** to indicate something that is absolutely
	mandatory (or for 'shall not' absolutely forbidden). Violate a
	'shall' and you are not conforming to the standard. The words
	**required** or **must** are synonyms.


The word **should** is weaker. 'Should' indicates a
	recommendation. The standard would like to you to follow it, but
	you're not breaking the standard if you don't. **Recommended** is a synonym.


**May** indicates an optional feature. You should be able to work
	with an implementation gracefully if it's present or if it's missing.


You can find a more official version of the above as [RFC 2119](http://www.apps.ietf.org/rfc/rfc2119.html).


Things that are **normative** are part of the standard. Sections that
	are non-normative are things like background information and
	clarifications. Sometimes suggested implementation techniques are
	suggested in a non-normative section because they help clarify the
	concepts in the standard, but the writers rightly don't want to
	constrain implementers.
