---
title: "Reddit: Language vs. Platform"
date: 2007-04-16
url: https://blog.codinghorror.com/reddit-language-vs-platform/
slug: reddit-language-vs-platform
word_count: 812
---

My previous entry, [Twitter: Service vs. Platform](https://blog.codinghorror.com/twitter-service-vs-platform/), was widely misunderstood. I suppose I only have myself to blame, so I’ll try to clarify with another example.


Consider Reddit. The Reddit development team switched from Lisp to Python late in 2005:


> If Lisp is so great, why did we stop using it? One of the biggest issues was the **lack of widely used and tested libraries**. Sure, there is a CL library for basically any task, but there is rarely more than one, and often the libraries are not widely used or well documented. Since we’re building a site largely by standing on the shoulders of others, this made things a little tougher. There just aren’t as many shoulders on which to stand.
> On that note, if you have been considering writing a web application in Lisp, go for it. It will be tough if you’re not already a Lisper, but you will learn a lot along the way, and it will be worth it I am sure. Lisp is especially great for projects where the end goal is unknown because it’s so easy to steer in different directions. **Lisp will never get in your way, although sometimes the environment will.**


Language performance is a red herring. That’s especially true when we’re comparing dynamic languages like Ruby, Lisp, and Python that will never be known for their high octane, nitro burnin’ performance levels. I assumed Alex Payne knew that when he chose to specifically [call out Ruby language performance](https://web.archive.org/web/20070506140525/http://www.radicalbehavior.com:80/5-question-interview-with-twitter-developer-alex-payne/), but maybe I assumed wrong.


When you choose a language, like it or not, you’ve chosen a *platform*. And as Steve so patiently and calmly explained to all the Lisp enthusiasts, the *platform around the language*, more than the language itself, sets the tone for your development experience. The availability of common, popular libraries and the maturity of the development environment end up trumping any particular significance the language holds.


That’s why the Reddit switch makes good business sense: **they didn’t change languages; they changed platforms**. At the point which your choice of platform starts to jeopardize your service, *you switch platforms*, exactly as Reddit did. Your users don’t give a damn what framework and language you’re using. The only people who care about that stuff are other software developers. And God help you if your users *are* software developers; then you’re really in trouble.


But things aren’t all roses in Python-land either. The Reddit developers initially used a Rails-like web application framework, with [decidedly mixed results](http://www.aaronsw.com/weblog/rewritingreddit):


> The framework that seems most promising is [Django](http://www.djangoproject.com/) and indeed the authors of reddit initially attempted to rewrite their site in it. I was curious about their experience, so I carefully followed them along, trying to help them out.
> Django seemed great from the outside: a nice-looking website, intelligent and talented developers, and a seeming surplus of nice features. The developers and community are extremely helpful and responsive to patches and suggestions. And all the right goals are espoused in their philosophy documents and FAQs. Unfortunately, however, they seem completely incapable of living up to them.
> While Django claims that it’s “loosely coupled,” using it pretty much requires fitting your code into Django’s worldview. Django insists on executing your code itself, either through its command-line utility or a specialized server handler called with the appropriate environment variables and Python path. When you start a project, by default Django creates folders nested four levels deep for your code and while you can move around some files, I had trouble figuring out which ones and how.
> Django’s philosophy says “Explicit is better than implicit,” but Django has all sorts of magic. Database models you create in one file magically appear someplace else deep inside the Django module with a different name. When your model function is called, new things have been added to its variable-space and old ones removed. (I’m told they’re currently working on fixing both of these, though.)


Note that any analogies I’m drawing between Rails and Django here are purely intentional.


Not that there’s anything wrong with adopting a web application framework. But **at least in Python you have a *choice* of web application frameworks**. Instead of investing in the Django worldview, the Reddit team decided that the lighter weight [web.py](http://webpy.org/) better suited their needs. Similarly, some ASP.NET developers reject the entire page lifecycle model, preferring to write their own HttpHandlers and HttpModules for finer-grained control over what’s happening on their website. And that’s fine; the ASP.NET platform accommodates both camps of developers.


It’s true that Twitter represents an extreme case, but it sure looks like the Twitter developers could benefit from a choice of [web application frameworks](https://blog.codinghorror.com/twitter-service-vs-platform/), too. In the end, it’s about choice and flexibility. Not just in the language, but in the platform that inevitably comes along with any language.

[lisp](https://blog.codinghorror.com/tag/lisp/)
[python](https://blog.codinghorror.com/tag/python/)
[reddit](https://blog.codinghorror.com/tag/reddit/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
