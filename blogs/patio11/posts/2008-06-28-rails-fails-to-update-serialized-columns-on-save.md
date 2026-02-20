---
title: "Rails Fails To Update Serialized Columns On Save"
date: 2008-06-28
url: https://www.kalzumeus.com/2008/06/28/rails-fails-to-update-serialized-columns-on-save/
slug: rails-fails-to-update-serialized-columns-on-save
word_count: 416
---


One of the problems I hit earlier today, which literally cost 2.5 hours to resolve, was that I have a Rails model which uses a serialized column in it.  The column contains a hash of options for the object.  Fairly simple stuff.


As it turns out, after overwriting one of the parameters in the hash and saving it, the object in the database would be out of sync with the ActiveRecord object still in memory (even though save returned true), which lead to hilarity the next time someone grabbed the object from the DB and got partially out-of-date data.  (*Inconsistent* out-of-date data.  Failure.)


As it turns out, the issue is a new feature Rails 2.1 — partial updates of database records.  Rails keeps a list of which attributes are “dirty” and only updates those when you call ActiveRecord#save.  Unfortunately, touching the contents of a hash does not mark it as dirty.


I was absolutely clueless *how* this was happening (I stupidly upgraded to 2.1 on a whim, thinking that I hadn’t written any significant code yet so incompatibilities wouldn’t bother me — true enough, the only incompatibility was with my mental model of how ActiveRecord worked), but I successfully diagnosed the *why* — a dirty bit wasn’t getting set for the serialized object.  OK, no problem, the same thing happens at the day job with our Java system — which means I can use the same hacky solution to the problem.


def before_save


options_hash_clone = options.clone  #shallow copy of options hash


options = {} # sets dirty bit for options hash


options = options_hash_clone # restores options hash to original content, ensuring save updates it in DB


end


which will, indeed, set the dirty bit.


As it turns out, there is a cleaner way to do this if partial updates aren’t a requirement for your model:


#there are a number of places you could put this — the model class itself strikes me as decent


ModelNameGoesHere.partial_updates = false


A big thanks to [this post](http://ryandaigle.com/articles/2008/4/1/what-s-new-in-edge-rails-partial-updates) for putting me on the scent of the problem.  Seems I missed quite a bit of discussion on Google about it since I was not hitting the right keywords apparently.  The fact that this is on by default appears to be one of those *opinionated software* practices where “opinionated” means “it is our opinion that you should be as familiar with the change log as the core team before you install a new production release”.  (Sorry if I sound bitter.  2.5 hours.)
