---
title: "Myth #3: Rails forces you to use Prototype"
date: 2008-11-14
url: https://dhh.dk/posts/32-myth-3-rails-forces-you-to-use-prototype
slug: myth-3-rails-forces-you-to-use-prototype
word_count: 523
---


There are lots of great JavaScript libraries out there. [Prototype](http://prototypejs.org/) is one of the best and it ships along Rails as the default choice for adding Ajax to your application.


Does that mean you have to use Prototype if you prefer something else? Absolutely not! Does it mean that it's hard to use something else than Prototype? No way!


It's incredibly easy to use another JavaScript library with Rails. Let's say that you wanted to use [jQuery](http://jquery.com/). All you would have to do is add the jQuery libraries to public/javascripts and include something like this to the  in your layout to include the core and ui parts:


<%= javascript_include_tag "jquery", "jquery-ui" %>


Then say you have a form like the following that you want to Ajax:


<% form_for(Comment.new) do |form| %>
    
  <%= form.text_area :body %>
    
  <%= form.submit %>
    
<% end %>


By virtue of the conventions, this form will have an id of new_comment, which you can decorate with an event in, say, application.js with jQuery like this:


$(document).ready(function() {
    
  $("#new_comment").submit(function() {
    
    $.post($(this).attr('action') + '.js', 
    
      $(this).serializeArray(), null, 'script');
    
 
    
    return false;
    
  });
    
});


This will make the form submit to /comments.js via Ajax, which you can then catch in the PostsController with a simple format alongside the HTML response:


def create
    
  @comment = Post.create(params[:comment])
    
 
    
  respond_to do |format|
    
    format.html { redirect_to(@comment) }
    
    format.js
    
  end
    
end


The empty format.js simply tells the controller that there's a template ready to be rendered when a JavaScript request is incoming. This template would live in comments/create.js.erb and could look something like:


$('#comments').append(
    
  '<%= escape_javascript(render(:partial => @comment)) %>');
    
$('#new_comment textarea').val("");
    
$('#<%= dom_id(@comment) %>').effect("highlight");


This will append the newly created @comment model to a dom element with the id of comments by rendering the comments/comment partial. Then it clears the form and finally highlights the new comment as identified by dom id "comment_X".


That's pretty much it. You're now using Rails to create an Ajax application with jQuery and you even get to tell all the cool kids that your application is unobtrusive. That'll impress them for sure :).


**Rails loves all Ajax, not just the Prototype kind**

This is all to say that the base infrastructure of Rails is just as happy to return JavaScript made from any other package than Prototype. It's all just a mime type anyway.


Now if you don't want to put on the unobtrusive bandana and instead would like a little more help to define your JavaScript inline, like with remote_form_for and friends, you can have a look at something like [jRails](http://ennerchi.com/projects/jrails), which mimics the Prototype helpers for jQuery. There's apparently a [similar project underway for MooTools](http://github.com/pointcom/mootools-on-rails/tree/master) too.


So by all means use the JavaScript library that suits your style, but please stop crying that Rails happens to include a default choice. That's what Rails is. A collection of default choices. You accept the ones where you don't care about the answer or simply just agree, you swap out the ones where you differ.


**Update: ** Ryan Bates has created [a screencast](http://railscasts.com/episodes/136-jquery) that shows you how to do the steps I outlined above and more.


*See the [Rails Myths](29-the-rails-myths.html) index for more myths about Rails.*

