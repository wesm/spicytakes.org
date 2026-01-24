---
title: "The Difficulty of Dogfooding"
date: 2005-05-11
url: https://blog.codinghorror.com/the-difficulty-of-dogfooding/
slug: the-difficulty-of-dogfooding
word_count: 830
---

Joel, on the [merits of dogfooding](http://www.joelonsoftware.com/articles/fog0000000012.html):


> **Eating your own dog food is the quaint name that we in the computer industry give to the process of actually using your own product.**
> I had forgotten how well it worked, until a month ago, I took home a build of CityDesk (thinking it was about 3 weeks from shipping) and tried to build a site with it. Phew! There were a few bugs that literally made it impossible for me to proceed, so I had to fix those before I could even continue. All the testing we did, meticulously pulling down every menu and seeing if it worked right, didn’t uncover the showstoppers that made it impossible to do what the product was intended to allow. **Trying to use the product, as a customer would, found these showstoppers in a minute.**


![](https://blog.codinghorror.com/content/images/2025/05/image-89.png)


[Eating your own dogfood](http://en.wikipedia.org/wiki/Eat_one%27s_own_dog_food) is clearly a good idea, but it hasn’t worked out too well for me in practice, for the following reasons:

1. **Developers usually aren’t the intended audience**
Microsoft originally popularized the term “eating your own dogfood” during [the development of Windows NT](https://blog.codinghorror.com/showstopper/), when Dave Cutler insisted that the coding of the OS be performed under the current builds. If you’re writing software intended for other developers– or an operating system intended for the entire world– then dogfooding makes perfect sense. Who better to test Visual Studio than the developers writing Visual Studio? There’s no question that this results in a higher quality product, but you also have to be extremely careful. If the application you’re writing isn’t intended for expert users, having the developers dogfood it won’t necessarily buy you much, because developers are [highly unrepresentative of typical users](https://blog.codinghorror.com/the-rise-and-fall-of-homo-logicus/). Beyond fixing critical bugs, it could even hurt the application: developers tend to add advanced, complicated features that are useful to them.
2. **The application requires specialized business knowledge**
I’ve worked on a number of applications that I could barely test, much less use. I had no idea what valid inputs even looked like! Sure, I had the specifications, but there’s a huge difference between applications designed for general purpose use (ala Joel’s CityDesk example) and custom applications designed to be used internally. These internal apps are typically quite specialized; you’d need a lot of exposure to the target audience before you could begin to think like your users. Moreover, their job may be radically different than yours; expecting software developers to dogfood an app intended for stockbrokers is probably unrealistic.
3. **Dogfood tastes bad**
It is called dogfood, after all. And no sane person relishes popping open a can of Alpo for lunch. Aside from the frustrations of using alpha and beta software, I’ve also worked on a number of team projects where I was never comfortable with the quality and featureset of the product we were producing. I could barely bring myself to use our own software! Since I wasn’t the project manager, I had no formal authority to dictate the quality or features of the product I felt we should be building. On projects where I am the only developer, however, I can code to exactly the quality and feature level I’d like to see. **The only dogfood guaranteed to taste good is your own.** And even that is debatable. All other dogfood is unpleasant and often inedible.


Now, none of this is intended to discourage you from dogfooding. I just feel it’s difficult to achieve for typical development teams. Not every application is as easy to dogfood as Windows NT, Visual Studio, and CityDesk. But for every obstacle I listed, there are a half-dozen benefits you’ll derive if you manage to pull it off. It’s clearly a best practice and you should be aggressively [dogfooding your own software](https://web.archive.org/web/20060210225937/http://blogs.msdn.com/jledgard/archive/2004/02/14/73091.aspx) whenever possible:


> Do what you can to incorporate your product into your job. If you are developing a word processor you should be using it any chance you get to create your own documentation. If you are developing blog software, then blog about your progress. Do whatever you can to give yourself a different perspective of the software you intend to create. The more views of something you have the more defects you will find. **If you are developing a product that you can’t integrate into your day to day job then you should be creating a dogfooding test plan where you and interested customers spend dedicated time using the product the way it is meant to be used.** It’s especially important to get feedback from these different perspectives and incorporate it into your release. Because if 1 of 20 people find a problem with your software then you can imagine the issues that will be found when you have thousands of different perspectives on your product.


And if you can’t dogfood, consider working the help desk for a few days. I’m serious. There’s nothing quite as effective as [sharing the customer’s pain](https://blog.codinghorror.com/sharing-the-customers-pain/).

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[testing](https://blog.codinghorror.com/tag/testing/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[product management](https://blog.codinghorror.com/tag/product-management/)
