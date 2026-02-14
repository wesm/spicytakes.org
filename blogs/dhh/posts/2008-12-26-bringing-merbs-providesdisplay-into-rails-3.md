---
title: "Bringing Merb's provides/display into Rails 3"
date: 2008-12-26
url: https://dhh.dk/posts/37-bringing-merbs-providesdisplay-into-rails-3
slug: bringing-merbs-providesdisplay-into-rails-3
word_count: 709
---


The flow of Merb ideas into Rails 3 is already under way. Let me walk you through one of the first examples that I've been working on the design for. Merb has a feature related to Rails' respond_to structure that works for the generic cases where you have a single object or collection that you want to respond with in different formats. Here's an example:


class Users < Application

  provides :xml, :json

  

  def index

    @users = User.all

    display @users

  end

end


This controller can respond to html, xml, and json requests. When running display, it'll first check if there's a template available for the requested type, which is often the case with HTML, and otherwise fallback on trying to convert the display object. So @users.to_xml in the result of a XML request.


The applications I've worked on never actually had this case, though. I always had to do more than just convert the object to the type or render a template. Either I needed to do a redirect for one of the types instead of a render or I need to do something else besides the render. So I never got to spend much time with the default case that's staring you in the face from scaffolds:


class PostsController < ApplicationController

  def index

    @posts = Post.find(:all)

 

    respond_to do |format|

      format.html

      format.xml  { render :xml => @posts }

    end

  end

 

  def show

    @post = Post.find(params[:id])

 

    respond_to do |format|

      format.html

      format.xml  { render :xml => @post }

    end

  end

end


**Cut duplication when possible, give full control when not**

But the duplication case is definitely real for some classes of applications. And it's pretty ugly. The respond_to blocks are repeated for index, show, and often even edit. That's three times a fairly heavy weight structure. This is where the provides/display setup comes handy and zaps that duplication.


For Rails 3, we wanted the best of both worlds. The full respond_to structure when you needed to do things that didn't map to the generic structure, but still have the generic approach at hand when the circumstances were available for its use.


**Dealing with symmetry and progressive expansion in API design**

There were a couple of drawbacks with the provides/display duo, though, that we could deal with at the same time. The first was the lack of symmetry in the method names. The words "provides" and "display" doesn't reflect their close relationship and if you throw in the fact that they're actually both related to rendering, it's gets even more muddy.


The symmetry relates to another point in API design that I've been interested in lately: progressive expansion. There should be a smooth path from the simple case to the complex case. It should be like an Ogre, it should have layers. Here's what we arrived at:


class PostsController < ApplicationController

  respond_to :html, :xml, :json

 

  def index

    @posts = Post.find(:all)

    respond_with(@posts)

  end

 

  def show

    @post = Post.find(params[:id])

    respond_with(@post)

  end

end


This is the vanilla provides/display example, but it has symmetry in respond_to as a class method, respond_with as a instance method, and the original respond_to blocks. So it also feels progressive when you unpack the respond_with and transform it into a full respond_to if you suddenly need per-format differences.


The design also extends the style to work just at an instance level without the class-level defaults:


class DealsController < SubjectsController

  def index

    @deals = Deal.all

    respond_with(@deals, :to => [ :html, :xml, :json, :atom ])

  end

 

  def new

    respond_with(Deal.new, :to => [ :html, :xml ])

  end

end


It's quite frequent that the index action has different format responsibilities than the new or the show or whatever. This design encompasses all of those scenarios.


Yehuda has also been interested in improving the performance of respond_to/with by cutting down on the blocks needed. Especially when you're just using respond_with that doesn't need to declare any blocks at all.


All in all, I think this is a great example of the kind of superior functionality that can come out of merging ideas from both camps. We're certainly excited to pull the same trick on many other framework elements. I've been exploring how a revised router that imports the best ideas from both could look and feel like. I'll do a write-up when there's something real to share.

