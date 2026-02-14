---
title: "Think of emails as views delivered through SMTP"
date: 2009-11-09
url: https://dhh.dk/posts/43-think-of-emails-as-views-delivered-through-smtp
slug: think-of-emails-as-views-delivered-through-smtp
word_count: 486
---


ActionMailers has to deal with a bit of a split personality. On the one hand, their organization and flow structure is very much akin to controllers. They have multiple methods that all correspond to actions. They render views from templates. They can even have layouts. On the other hand, Rails by default puts them in app/models.


Looking at these two personalities, which would you consider the dominant one? Which of the two is more important? To me it's obviously the former. That ActionMailers have a much closer allegiance to the controller side of the MVC split than the model side. In fact, Rails 3 shares a lot of implementation between ActionController and ActionMailer through the new AbstractController class.


But it seems that [a fair number of people](http://www.robbyonrails.com/articles/2009/11/16/sending-email-controllers-versus-models) aligned themselves with the model view of ActionMailers instead. The primary argument seems to be that controllers really shouldn't have any logic and that models are better tested anyway. The no-logic controllers argument originally came from the theme of [Skinny Controller, Fat Model](http://weblog.jamisbuck.org/2006/10/18/skinny-controller-fat-model) that advocated you shouldn't have a bunch of model code in your controller. Sage advice, still very relevant, but taken too literally, you end up with the erroneous idea that controllers shouldn't have any logic at all.


Controllers are meant to have logic when it's required to glue together the actions of the interaction. The controller is the melting pot for putting the individual pieces of the application to work. We strive to make all other components of the application as encapsulated and free of entanglements together exactly because we know we can wire it all up in a controller.


With that responsibility comes the need for testing, though. Don't think you can get off the hook just because you made the controller completely anemic. It's not good for either your tests or the controller. So accept that controllers need testing love too and it won't seem unreasonable that they'll have a say in flow and composition either.


In some cases it can make sense to have ActionMailer triggered by observers (who themselves have a bit of a split personality as they can serve both controllers and models), but for the majority case I think using mixins and filters to trigger abstracted and shared mailer logic is the better way to go.


Of course you can do whatever you want with your mailers. Just like you can make your models trigger view rendering, you can certainly make it call your mailers. Maybe you have some minority-case concern that makes that exactly the right thing to do. I haven't seen your application.


But Rails should certainly encourage a standard way of doing things. The core flow shouldn't have mixed messages, so come Rails 3, I'll make sure that we don't continue to send those out by placing mailers in app/models. It's obviously confusing things. So accept my apologies for being sloppy with the organization there. My bad.

