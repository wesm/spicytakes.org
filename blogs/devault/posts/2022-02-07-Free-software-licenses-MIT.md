---
title: "Free software licenses explained: MIT"
date: 2022-02-07
url: https://drewdevault.com/2022/02/07/Free-software-licenses-MIT.html
slug: Free-software-licenses-MIT
word_count: 830
---

This is the first in a series of posts I intend to write explaining how various
free and open source software licenses work, and what that means for you as a
user or developer of that software. Today we’ll look at the MIT license, also
sometimes referred to as the X11 or Expat license.

The MIT license is:

* Both  [free software](https://www.gnu.org/philosophy/free-sw.en.html)  and  [open source](https://opensource.org/osd)
* Permissive (and thus non-copyleft and non-viral)

This means that the license upholds the four essential freedoms of free software
(the right to run, copy, distribute, study, change and improve the software) and
all of the terms of the open source definition (largely the same). Further more,
it is classified on the permissive/copyleft spectrum as a permissive license,
meaning that it imposes relatively few obligations on the recipient of the
license.

The full text of the license is quite short, so let’s read it together:

> The MIT License (MIT) 
>  Copyright (c) <year> <copyright holders> 
>  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 
>  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
>  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The first paragraph of the license enumerates the rights which you, as a
recipient of the software, are entitled to. It’s this section which qualifies
the license as free and open source software (assuming the later sections don’t
disqualify it). The key grants are the right to “use” the software (freedom 0),
to “modify” and “merge” it (freedom 1), and to “distribute” and “sell” copies
(freedoms 2 and 3), “without restriction”. We also get some bonus grants, like
the right to sublicense the software, so you could, for instance, incorporate it
into a work which uses a less permissive license like the GPL.

All of this is subject to the conditions of paragraph two, of which there is
only one: you must include the copyright notice and license text in any
substantial copies or derivatives of the software. Thus, the MIT license
requires  *attribution* . This can be achieved by simply including the full
license text (copyright notice included) somewhere in your project. For a
proprietary product, this is commonly hidden away in a menu somewhere. For a
free software project, where the source code is distributed alongside the
product, I often include it as a comment in the relevant files. You can also add
your name or the name of your organization to the list of copyright holders when
contributing to MIT-licensed projects, at least in the absence of a CLA. 1

The last paragraph sets the expectations for the recipient, and it is very
important. This  *disclaimer of warranty*  is ubiquitous in nearly all free and
open source software licenses. The software is provided “as is”, which is to
say, in whatever condition you found it in, for better or worse. There is no
expectation of warranty (that is to say, any support you receive is from the
goodwill of the authors and not from a contractual obligation), and there is no
guarantee of “merchantability” (that you can successfully sell it), fitness for
a particular purpose (that you can successfully use it to solve your problem),
or noninfringement (such as with respect to relevant patents). That last detail
may be of particular importance: the MIT license disclaims all liability for
patents that you might infringe upon by using the software. Other licenses often
address this case differently, such as Apache 2.0.

MIT is a good fit for projects which want to impose very few limitations on the
use or reuse of the software by others. However, the permissibility of the
license permits behaviors you might not like, such as creating a proprietary
commercial fork of the software and selling it to others without supporting
upstream. Note that the right to sell the software is an inalienable requirement
of the free software and open source definitions, but other licenses can level
the playing field a bit with strategies like copyleft and virality, on the other
end of the permissibility spectrum. I’ll cover some relevant licenses in the
future.

1. You should not sign a CLA which transfers your copyright to the publisher. ↩︎
