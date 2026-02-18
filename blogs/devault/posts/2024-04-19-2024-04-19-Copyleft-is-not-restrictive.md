---
title: "Copyleft licenses are not “restrictive”"
date: 2024-04-19
url: https://drewdevault.com/2024/04/19/2024-04-19-Copyleft-is-not-restrictive.html
slug: 2024-04-19-Copyleft-is-not-restrictive
word_count: 1127
---

One may observe an axis, or a “spectrum”, along which free and open source
software licenses can be organized, where one end is “permissive” and the other
end is “copyleft”. It is important to acknowledge, however, that though copyleft
can be found at the opposite end of an axis with respect to permissive, it is
not synonymous with the linguistic antonym of permissive – that is, copyleft
licenses are not “restrictive” by comparison with permissive licenses.

*Aside: Free software is not synonymous with copyleft and open source is not
synonymous with permissive, though this is a common misconception. Permissive
licenses are generally free software and copyleft licenses are generally open
source; the distinction between permissive and copyleft is orthogonal to the
distinction between free software and open source.*

It is a common misunderstanding to construe copyleft licenses as more
“restrictive” or “less free” than permissive licenses. This view is predicated
on a shallow understanding of freedom, a sort of passive freedom that presents
as the absence of obligations. Copyleft is predicated on a deeper understanding
of freedom in which freedom is a  *positive guarantee of rights* . [[source]](https://plato.stanford.edu/entries/liberty-positive-negative/)

Let’s consider the matter of freedom, obligation, rights, and restrictions in
depth.

Both forms of licenses include obligations, which are not the same thing as
restrictions. An example of an obligation can be found in the permissive MIT
license:

> Permission is hereby granted […] to deal in the Software without restriction
> […] subject to the following conditions: 
>  The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.

This obliges the user, when distributing copies of the software, to include the
copyright notice. However, it does not  *restrict*  the use of the software under
any conditions. An example of a restriction comes from the infamous JSON
license, which adds the following clause to a stock MIT license:

> The Software shall be used for Good, not Evil.

IBM famously petitioned Douglas Crockford for, and received, a license to do
evil with JSON. 1  This kind of clause is broadly referred to in the free
software jargon as “discrimination against field of endeavour”, and such
restrictions contravene both the free software and open source definitions. To
quote the  [Open Source Definition](https://opensource.org/osd) , clause 6:

> The license must not restrict anyone from making use of the program in a
> specific field of endeavor. For example, it may not restrict the program from
> being used in a business, or from being used for genetic research.

No such restrictions are found in free or open source software licenses, be they
permissive or copyleft – all FOSS licenses permit the use of the software for
any purpose without restriction. You can sell both permissive and copyleft
software, use it as part of a commercial cloud service, 2  use the software
as part of a nuclear weapons program, 3  or do whatever else you want with
it. There are no restrictions on how free software is used, regardless of if it
is permissive or copyleft.

Copyleft does not impose restrictions, but it does impose obligations. The
obligations exist to guarantee rights to the users of the software – in other
words, to ensure freedoms. In this respect copyleft licenses are  *more free* 
than permissive licenses.

Freedom is a political concept, and in order to understand this, we must
consider it in political terms, which is to say as an exercise in power
dynamics. Freedom without obligation is a contradiction. Freedom  *emerges*  from
obligations, specifically obligations imposed on power.

Where does freedom come from?

Consider the United States as an example, a society which sets forth freedom as
a core political value. 4  Freedoms in the US are ultimately grounded in the US
constitution and its bill of rights. These tools create freedoms by guaranteeing
rights to US citizens through the imposition of  *obligations*  on the government.
For instance, you have a right to an attorney when accused of a crime in the
United States, and as such the government is  *obliged*  to provide you with one.
It is from obligations such as these that freedom emerges. Freedom of assembly,
another example, is guaranteed such that the police are prevented from breaking
up peaceful protests – this freedom emerges from a  *constraint*  (or
restriction, if you must) on power (the government) as a means of guaranteeing
the rights and freedom of those with less power by comparison (its citizens).

Who holds the power in the context of software?

Consider non-free software by contrast: software is written by corporations and
sold on to users with substantial restrictions on its use. Corporations hold
more power than individuals: they have more resources (e.g. money), more
influence, and, in a sense more fundamental to the software itself, they retain
in private the tools to understand the software, or to modify its behavior, and
they dictate the conditions under which it may be used (e.g. only if your
license key has not expired, or only for certain purposes). This is true of
anyone who retains the source code in private and uses copyright law to enforce
their will upon the software – in this way they possess, and exercise, power
over the user.

Permissive licenses do not provide any checks on this power; generally they
preserve  [moral rights](https://en.wikipedia.org/wiki/Moral_rights)  and little
else. Permissive licenses provide for relatively few and narrow freedoms, and
are not particularly “free” as such. Copyleft licenses constrain these powers
through additional obligations, and from these obligations greater freedoms
emerge. Specifically, they oblige reciprocity. They are distinguished from
permissive licenses in this manner, but where permissive licenses  *permit* ,
copyleft does not  *restrict*  per-se – better terms might be “reciprocal” and
“non-reciprocal”, but perhaps that ship has sailed. “You may use this software
 *if*  …” is a statement made both by permissive and copyleft licenses, with
different  *if* s. Neither form of license says “you cannot use this software  *if* 
…”; licenses which do so are non-free.

Permissive licenses and copyleft licenses are both free software, but only the
latter provides a guarantee of rights, and while both might be free only the
latter provides  *freedom* .

1. Strictly speaking this exception was for JSLint, not JSON. But I digress. ↩︎
2. This is even true if the software uses the AGPL license. ↩︎
3. Take a moment here to entertain the supposition that nuclear warheads
are legally obliged to include a copy of the MIT license, if they
incorporate MIT licensed code in their guidance systems, on board, as they
are “distributing” that software to the, err, recipients. As it were. ↩︎
4. The extent to which it achieves this has, of course, been the subject of
intense debate for centuries. ↩︎
