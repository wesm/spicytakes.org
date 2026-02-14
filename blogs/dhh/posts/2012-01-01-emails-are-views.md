---
title: "Keep email views out of the models"
date: 2012-01-01
url: https://dhh.dk/2012/emails-are-views.html
slug: emails-are-views
word_count: 632
---


The most basic pillar of a Model-View-Controller architecture is the separation between the three layers. We keep them separate to isolate change and to reason about the system in a coherent manner.


But somehow the idea that the model should be triggering the rendering of emails crept into the picture. I've been pretty horried to see code like this:


```
class Person < ActiveRecord::Base
  after_create :send_welcome_email

  private
    def send_welcome_email
      Notifier.welcome(self).deliver
    end
end
```


Why on earth would you have your model be responsible for generating HTML emails? Well, it turns there's at least an explanation for why this idea came to be: DRY. Don't Repeat Yourself is like holy water to programmers and mostly for good reason. In general, it's no good to repeat the same code in two places.


But, like anything, it can be taken too far. Here's the code that often lures people to take it too far:


```
class PeopleController
  def create
    @person = Person.create(params[:person])
    Notifier.welcome(@person).deliver
  end
end

class Admin::PeopleController
  def create
    @person = Person.create(params[:person])
    Notifier.welcome(@person).deliver
  end
end

```


Oh noes! The Notifier call is appearing twice in two separate controllers. That is a clear violation of DRY and this development must be arrested immediately.


No really, it musn't. Having a Notifier appear twice in two separate controllers is just fine. It's fine in the same way it's fine to reuse a partial twice. Or to call Person.create twice. The email generation code has already been abstracted — that's why the Notifier call is just that, a call, and not five lines of mail preparation code. It does not need further abstraction than that.


### When to extract a shared controller action


Now here comes some real heresy. If — AND ONLY IF — your welcome code actually grows to substantial size (and a call to a Notifier + saving a record does not even remotely qualify as substantial!), AND you're reusing *exactly* the same code, then you can indeed extract this shared functionality into an external action that can be reused.


I find that this rarely happens, though. What happens instead is that people will assume that it's going to be needed and prematurely extract the shared controller code into an external action. Then they'll realize that the steps needed when an admin invites a user versus when that user signs up on their own are actually not *quite* the same. So they'll introduce conditionals in the supposedly shared class and now we're back to being worse than where we came from.


(Or it happens under the banner of "fast tests" where mocking a controller is seen as too complex/slow, so the simplicity of the system is downgraded in order to ease the job of mocking. Terrible idea.)


Controller actions are supposed to do the work of finding the model, telling it what to do (mostly CRUD), and determining which views to render as a result. Emails are part of those views! There's a reason ActionMailer descends directly from AbstractController and that it calls ActionView. It's a co-collaborator to the controller handling the incoming request.


Oh, but what about import jobs? Same thing. Import jobs are a kind of controller as well. They receive parameters (list of emails to invite, say), then they interact with the model (creating the Users), and finally renders the views (sending emails). Having PeopleController and ImportPeopleJob both call Notifier.welcome(person) is not enough reason to create a separate shared CreateUser object.


Model-View-Controller is a pretty basic idea. Don't let my foods touch. DRY is a simple idea too: Don't write the same stuff twice. The part that seems to need guidance is how to balance the trade-off when both ideas are tugging at your code. So here's a simple bit of advice: When in doubt, keeping your foods from touching is more important.

