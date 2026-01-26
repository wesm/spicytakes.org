---
title: "Dynamic Type Check"
description: "Recently some of our developers ran into the accusation that with a   dynamic language like ruby you use so many dynamic type checks that   you end up effectively writing your own type system. So they"
date: 2009-06-02T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/bliki/DynamicTypeCheck.html
slug: DynamicTypeCheck
word_count: 415
---


Recently some of our developers ran into the accusation that with a
  dynamic language like ruby you use so many dynamic type checks that
  you end up effectively writing your own type system. So they
  thought, since we've written a lot of real ruby code - how often do
  we make dynamic type checks? Michael Schubert gathered up the data.


The table below contains the data. We define a dynamic type check
  as the use of the methods `is_a?`, `kind_of?`,
  and `instance_of?`. The lines of code come from the
  standard rake stats command in rails.



| Project ID | Code type checks | Code LOC | Test type checks | Test LOC | LOC / type check | test LOC / code LOC |
| A | 16 | 13318 | 0 | 9856 | 1448 | 0.7 |
| B | 14 | 19138 | 0 | 17123 | 2590 | 0.9 |
| C | 0 | 2607 | 0 | 2981 | ∞ | 1.1 |
| D | 7 | 4265 | 3 | 4069 | 833 | 1.0 |
| E | 32 | 29619 | 60 | 97688 | 1384 | 3.3 |
| F | 18 | ~9500 | N/A | N/A | 528 | N/A |
| G | 0 | 2455 | 0 | 3290 | ∞ | 1.3 |
| H | 9 | 2220 | 6 | 6404 | 575 | 2.9 |
| I | 23 | 10633 | 2 | 12331 | 919 | 1.2 |
| J | 196 | 40461 | 24 | 88511 | 586 | 2.2 |
| K | 17 | 5769 | 6 | 9848 | 679 | 1.7 |



The moral of this data is that you shouldn't expect to see a lot of
type check calls in your ruby code base. This, of course, is true of
any dynamic language. It was generally considered bad form in
Smalltalk circles I inhabited too.


The methods that were checked for in this data aren't the only ones
that can be considered a dynamic type check. Other cases are
`respond_to?` and `aClass === anInstance`. Our
folks felt that these cases were no more common than the ones they
checked for.


Most uses are those of dealing with liberal input - eg where a method
parameter can be a string, symbol, or array. These crop up in DSLish
situations where you want liberal input for the high readability.
