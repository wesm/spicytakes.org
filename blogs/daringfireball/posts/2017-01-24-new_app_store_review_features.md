---
title: "Additional Details on the New App Store Review Features"
date: 2017-01-24
url: https://daringfireball.net/2017/01/new_app_store_review_features
slug: new_app_store_review_features
word_count: 659
---


[Jim Dalrymple, writing at The Loop](http://www.loopinsight.com/2017/01/24/apple-explains-the-new-app-reviews-api-for-developers/):


> When you are prompted to leave a review, customers will stay
> inside the app, where the rating or review can be left for the
> developer. It’s easier for customers and the developers still get
> their reviews.
> Apple is also limiting the amount of times developers can ask
> customers for reviews. Developers will only be able to bring up
> the review dialog three times a year. If a customer has rated the
> app, they will not be prompted again. If a customer has dismissed
> the review prompt three times, they will not be asked to review
> the app for another year.
> Customers will also have a master switch that will turn off the
> notifications for app reviews from all developers, if they wish to
> do that.


I spoke with Apple today about these features, too. A few questions I got answered:

- The replies that developers will be able to leave on App Store reviews will be attached to the user review to which they’re replying. It’s not a thread, per se, because users can only leave one review, and developers can only leave one response to each review, but they will be connected visually. Users can then edit their review, and developers can then edit their reply. Developers have been clamoring for something like this ever since the App Store opened in 2008.
- An individual app can prompt three times for a review per year, period. This counter does *not* get reset each time the developer updates their app. Good.
- The new APIs will eventually be the only sanctioned way for an iOS app to prompt for an App Store review, but Apple has no timeline for when they’ll start enforcing it. Existing apps won’t have to change their behavior or adopt these APIs right from the start.
- One reason developers prompt for reviews even after you’ve already reviewed a previous version of an app is that the average rating for an app gets reset with each update to the app — and a 4 or 5-star average rating can have a big effect on the number of downloads an app gets. From a developer’s perspective, it sucks when you replace a highly-rated version of your app with a minor bug-fix update and your average rating gets erased. It’s a tricky problem to solve, though — sometimes the latest update of an app really does deserve a *new* average rating, for better or for worse. I asked if this policy was changing, and Apple had nothing to announce — but they did acknowledge that they’re aware that the current policy is what led to the problem of apps badgering users too frequently for reviews.


I’ve long been a critic of apps begging for reviews (OpenTable, I’m looking in your direction). Three years ago, while linking to the excellent [Eff Your Review](http://effyr.tumblr.com/) website, [I wrote](http://daringfireball.net/linked/2013/12/05/eff-your-review):


> I’ve long considered a public campaign against this particular
> practice, wherein I’d encourage Daring Fireball readers, whenever
> they encounter these “Please rate this app” prompts, to go ahead
> and take the time to do it — but to rate the app with just one
> star and to leave a review along the lines of, “One star for
> annoying me with a prompt to review the app.”


It’s good to see Apple doing something about this. A limit of three prompts per year, and a system-wide switch to turn off *all* such prompts, go a long way toward fixing the problem from the user’s perspective. If Apple can figure out a fairer way to compute the average rating for apps across updates, they can help solve it from a developer’s standpoint too.



| **Previous:** | [On the Likelihood of Losing Your AirPods](https://daringfireball.net/2017/01/losing_airpods) |
| **Next:** | [Comparing the First Seven Years of the iPad and Mac](https://daringfireball.net/2017/02/comparing_first_seven_years_of_ipad_and_mac) |


PreviousNext