---
title: "Myth #4: Rails is a monolith"
date: 2008-11-15
url: https://dhh.dk/posts/33-myth-4-rails-is-a-monolith
slug: myth-4-rails-is-a-monolith
word_count: 1101
---


Rails is often accused of being a big monolithic framework. The charges usually contend that its intense mass makes it hard for people to understand the inner workings, thus making it hard to patch the framework, and that it results in slow running applications. Oy, let's start at the beginning.


Measuring lines of code is used to gauge the rough complexity of software. It's an easy but also incredibly crude way of measuring that rarely yields anything meaningful unless you apply intense rigor to the specifics. Most measurements of LOCs apply hardly any rigor and reduces what could otherwise be a somewhat useful indicator to an inverse dick measurement match.


**Applying rigor to measuring LOCs in Rails**

The measurements of LOC in Rails have not failed to live up to the low standards traditionally set for these pull-down-your-pants experiments. Let's look at a few common mistakes people commit when trying to measure the LOCs in Rails:


They count all lines including comments and whitespace in Ruby files, thus punishing well-documented and formatted codeThey count tests, thus punishing well-tested codeThey count bundled dependencies, thus punishing dependency-free code


Now let's take a simple example of committing all these mistakes against a part of Rails and see how misleading the results turn out to be. I'm going to use Action Mailer as an example here:


12,406 lines including comments, whitespace, tests, and dependencies7,912 lines including tests and dependencies6,409 lines including dependencies (t-mail and text-format)667 lines with none of the above


So the difference between committing all the mistakes and reality is a factor of 20. Even just the difference between committing the dependency mistake and reality is a factor of 10! In reality, if you were to work on Action Mailer for a patch, you would only have to comprehend a framework of 667 lines. A much less challenging task than digging into 12,406 lines.


Rails measured with all it's six major components without the mistakes is 34,097 lines divided across Action Mailer at 667, Active Resource at 878, Active Support at 6,684, Active Record at 9,295, Action Pack at 11,117 (the single piece most web frameworks should be comparing themselves to unless they also ship as a full stack), and Rail Ties at 5,447.


**Looking at the monolithic charge**

That Rails is big in terms of lines of code is just one of the charges, though. More vague and  insidious is the charge that Rails is monolithic. That is one giant mass where all the pieces depend on each other and are intertwined in hard-to-understand ways. That it lacks coherence and cohesion.


First, Rails can include almost as much or as little of the six major pieces as you prefer. If you're making an application that doesn't need Action Mailer, Active Resource, or Active Record, you can swiftly cut them out of your runtime by uncommenting the following statement in config/environment.rb:


# config.frameworks -= [ :active_record, :active_resource, :action_mailer ]


Now you've reduced your reliance on Rails to the 23,248 lines in Action Pack, Active Support, and Rail Ties. But let's dig deeper and look at the inner workings of Action Pack and how much of that fits the monolithic charge.


**Taking out the optional parts**

The Action Controller part of Action Pack consists of 8,282 lines which breaks down into two major halves. The essential, stuff that's needed to run the bare minimum of controllers, and the optional that adds specific features, which you could do without.


First the essentials of which there are 3,797 lines spread across these files and directories: base.rb, cgi_ext, cgi_ext.rb, cgi_process.rb, cookies.rb, dispatcher.rb, headers.rb, layout.rb, mime_type.rb, mime_types.rb, request.rb, response.rb, routing, routing.rb, session, session_management.rb, status_codes.rb, url_rewriter.rb.


The more interesting part is the optional parts of which there are 3,481 lines spread across these files and directories: assertions, assertions.rb, benchmarking.rb, caching, caching.rb, components.rb, filters.rb, flash.rb, helpers.rb, http_authentication.rb, integration.rb, mime_responds.rb, performance_test.rb, polymorphic_routes.rb, rack_process.rb, record_identifier.rb, request_forgery_protection.rb, request_profiler.rb, rescue.rb, resources.rb, streaming.rb, test_case.rb, test_process.rb, translation.rb, verification.rb.


All these optional parts can actually very easily be turned off as well, if you so please. If you look at actionpack/lib/action_controller.rb, you'll see something like the following:


ActionController::Base.class_eval do
    
  include ActionController::Flash
    
  include ActionController::Benchmarking
    
  include ActionController::Caching
    
  ...


This is where all the optional bits are being mixed into Action Pack. But they didn't need to be. If you really wanted to, you could just edit this 1 file and remove the optional bits you didn't need and you'd have some 3,500 lines of optional goodies to pick from.


For example, let's say you didn't need caching in your application. You comment the `include ActionController::Caching` line out and delete the associated files and that's 349 lines for the savings there. Or let's say that you don't like the flash, that's another 96 lines.


The reason many of these pieces can be optional is because of a wonderful part of Active Support called alias_method_chain. With alias_method_chain, you can latch on to a method to embellish it with more stuff. For example, the Benchmarking module uses alias_method_chain like this to hook into perform_action and render:


module Benchmarking
    
  def self.included(base)
    
    base.extend(ClassMethods)
    
 
    
    base.class_eval do
    
      alias_method_chain :perform_action, :benchmark
    
      alias_method_chain :render, :benchmark
    
    end
    
  end


ActionController::Base declares render and perform_action, but doesn't know anything about benchmarking (why should it?). The Benchmarking modules adds in these concerns when it's included similar to how aspects work. So as you can see, alias_method_chain is a great enabler for clearly defined modules in Rails.


All the other frameworks in Rails works in a similar fashion. There's a handful of essential parts and then a handful of optional parts, which can use alias_method_chain if they need to decorate some of the essential pieces. This means that the code is very well defined and you can look at just a single piece in isolation.


**But why on earth would you bother?**

The analysis above of how you can bring Action Controller down to some 3,500 lines carefully side-stepped one important question: Why would you bother? And that's an answer I don't quite have for you.


The important part about being modular is that the pieces are understandable in isolation. That the individual modules have coherence and cohesion. Not that they're actually handed to you as a puzzle for you to figure out how to put together.


I'd much rather give someone a complete picture, which they can then turn into a puzzle if they're so inclined. As I've shown you above, it's actually really simple to deconstruct the frameworks in Rails and you can make them much smaller really easily if you decide that's a good use of your time and energy.


*See the [Rails Myths](29-the-rails-myths.html) index for more myths about Rails.*

