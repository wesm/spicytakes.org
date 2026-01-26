---
title: "Story Counting"
description: "Story counting is a technique for planning and estimation.   Similarly toStoryPointsit works withXpVelocityto help you figure out how many   stories you can deliver in a fixed period of time. It diffe"
date: 2013-07-16T00:00:00
tags: ["estimation"]
url: https://martinfowler.com/bliki/StoryCounting.html
slug: StoryCounting
word_count: 533
---


Story counting is a technique for planning and estimation.
  Similarly to [StoryPoints](https://martinfowler.com/bliki/StoryPoint.html) it works with
  [XpVelocity](https://martinfowler.com/bliki/XpVelocity.html) to help you figure out how many
  stories you can deliver in a fixed period of time. It differs,
  however, in that you just consider the number of stories per unit of
  time and (mostly) ignore their relative sizes.


The rationale for story counting comes from experience. I've
  heard several teams look at their history and find that over the
  course of the project, their estimates from using story points are
  no more accurate than if they had simply counted how many
  stories were in each iteration. Given that, the effort of
  calculating story points isn't worth doing.


Using story counting does not imply that all the stories are
  roughly the same size (although some teams do work that way).
  Stories can still vary in size, but over time the bigger and smaller
  stories will cancel each other out, hence a simple count ends up the
  same.


This doesn't mean that you discard all consideration of relative
  size. Teams usually put enough effort in to ensure that the stories
  are within an order of magnitude of each other in terms of effort
  (so if they were given story points, they would be in a 1-8 point
  range). 1


1: 
      There's still a danger that you can get into difficulty by
  doing all the small stories first, thus getting a false picture of
  progress. If you're concerned about this you can do a rough sizing
  of stories (such as âT-shirt sizingâ into Small, Medium, Large, and
  Extra Large). Unlike Story Points, don't worry about the proportions
  between the sizes, all you need is to look to see if there are
  imbalances in the distribution of stories over time, such as all the
  extra-large stories at the end.


With story counting, you use velocity in much the same way as usual,
  the only difference is that velocity is just a sum of stories rather
  than a sum of story points.


One of the benefits of estimating with story points is that it
  helps identify poorly understood stories. So when using story
  counting you need to ensure there is some mechanism to spot
  stories with hidden blobs of complexity.


So far the teams I've come across using story counting are teams
  that have already been good at using story points, so it may be that
  story counting is a technique for more advanced teams. I've found
  teams work well with both story points and story counting and have
  no preference between them.


## Further Reading


Josh
    Kerievsky has a [good
    explanation of his switch](http://www.industriallogic.com/blog/stop-using-story-points/) from story points to story
    counting.


## Notes


1: 
      There's still a danger that you can get into difficulty by
  doing all the small stories first, thus getting a false picture of
  progress. If you're concerned about this you can do a rough sizing
  of stories (such as âT-shirt sizingâ into Small, Medium, Large, and
  Extra Large). Unlike Story Points, don't worry about the proportions
  between the sizes, all you need is to look to see if there are
  imbalances in the distribution of stories over time, such as all the
  extra-large stories at the end.
