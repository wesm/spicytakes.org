---
title: "Grand Unification Theory"
date: 2004-07-27
url: https://blog.codinghorror.com/grand-unification-theory/
slug: grand-unification-theory
word_count: 525
---

We recently switched to VS.NET 2003 (.NET 1.1) at work, yet we’re still using third party assemblies compiled under .NET 1.0. Now, ideally, you’d want assemblies recompiled to be sure that they are running as .NET 1.1. We happen to have a source license to these controls, so that option is available to us. But what about assemblies that you *can’t* recompile?


What happens when you reference them from an application compiled under .NET 1.1? I hadn’t ever considered this scenario. To me, **the only thing that makes sense is that these referenced assemblies are forced to run under the same runtime as the main application, even though they were compiled under 1.0.** And as it turns out, that is [exactly what happens](https://learn.microsoft.com/en-us/archive/blogs/alanshi/unification-policy):


> *The .NET framework assemblies have both of these problems. During development of the v1.0 product, the CLR / FX test teams explicitly tested the v1.0 FX stack against the v1.0 CLR. The same testing occurred for the v1.1 CLR and the v1.1 FX stack. Side-by-side testing naturally results in an explosive matrix of test cases, and because of this, there was no explicit testing done for mixing and matching v1.0 and v1.1 frameworks assemblies. Furthermore, there are some FX assemblies (I believe winforms is one such example) that are not designed to be run-time side-by-side capable.
> A generalized solution for addressing the problems above is still not yet available. In the interim, a CLR v1.1 feature known as unification policy was developed that addresses these problems (albeit in a very limited way). **Unification** is a form of binding policy which occurs after application policy is evaluated, but before publisher policy is applied. A hard-coded table of assemblies which shipped in the v1.1 CLR product is consulted and references to any version of assemblies in that list are automatically redirected to the version of the assembly that shipped in the v1.1 product.
> Through unification policy, it is possible for a v1.0 application to be configured to run against the v1.1 CLR (via the or configuration tags), and automatically have the references to the v1.0 FX stack redirected to the appropriate versions for the v1.1 CLR, with no re-compilation, or manual authoring of binding redirects by the developer or end-user. Similarly, an app built against the v1.1 CLR can utilize shared components written for the v1.0 CLR, and again the v1.0 FX references will automatically be redirect to the v1.1 stack. Through unification policy, the v1.1 process will always use v1.1 FX assemblies, and there will not be any mix/match conditions which could cause problems at run-time.*


As a semi-related aside, it’s disgraceful the way the 1.0 runtime is treated like a third class citizen at Microsoft. For example, we ran into a massive bug in the (hotfixed!) 1.0 version of System.Data.OracleClient. This bug has another hotfix, but only for 1.1. Now, 1.0 is about two years old, which doesn’t seem that old to me. But **just try getting a hotfix for a 1.1 bug back-ported into the 1.0 runtime.** In the words of the [Smash TV](http://www.klov.com/S/Smash_TV.html) announcer: *good luck – you’re gonna need it!*

[.net](https://blog.codinghorror.com/tag/net/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[assembly](https://blog.codinghorror.com/tag/assembly/)
[compatibility](https://blog.codinghorror.com/tag/compatibility/)
[runtime](https://blog.codinghorror.com/tag/runtime/)
