---
title: "Setting up a ruby development VM with Vagrant, Chef, and   rbenv"
description: "Some notes from my experiences in setting up a Vagrant VM   to help collaborators use my web publishing toolchain. I used Chef   to provision the VM and rbenv to install and control the right   versio"
date: 2014-09-04T00:00:00
tags: ["tools"]
url: https://martinfowler.com/articles/vagrant-chef-rbenv.html
slug: vagrant-chef-rbenv
word_count: 3476
---


I have my own toolchain for building [martinfowler.com](https://martinfowler.com/). I
    started it back around 2000 when few similar tools existed. Static
    websites weren't fashionable in those days, but I rather liked
    deploying my website by rsyncing to a server that only needed apache. Over
    time the toolchain has grown more capable and complex, but I've
    liked the way it's developed and it's a comfortable home for me to
    work in and explore new ideas.


In recent years I've had more colleagues and friends write
    articles on my site using the toolchain. To work with them I set
    up a stripped down copy of my core website repo and we collaborate
    using git. Since my collaborators are mostly programmers this
    workflow is pretty effective.


To run all this, it's necessary to install some software. All
    the software I use for the toolchain is open-source, but recently
    there have been some installation issues. In particular you find
    that many basic ruby installations are elderly, so we need to
    install a newer version of ruby. Since the toolchain processes
    XML, I use [Nokogiri](http://nokogiri.org/). It's a
    fine tool, but can be fiddly to install. In recent months I've had
    a couple of collaborators waste hours trying to get it
    installed.


A year (or was it two) ago, Erik told me I should set up a VM
    instance with the toolchain all installed and ready to go. That
    way a collaborator could just fire up a VM and start working.
    Increasingly we're using tools like Vagrant to set up virtual
    development environments like this on our projects. Finally with
    these latest collaborator hassles, I decided to do just that.


All in all it was rather harder than I wished it to be, and
    often there wasn't much documentation I could find to help me. So
    I've written notes of my experiences here for anyone looking to do
    something similar. Remember that I don't write these notes as
    authoritative documentation - they just record what I did that
    worked. There may be a better way of doing things that I didn't
    encounter, I'm not very experienced with these tools (and indeed
    have little ambition to be). This is also very time-specific,
    later versions of these tools may well work differently so be wary
    of that if you are trying to follow my breadcrumbs much later than
    the date on the article.


## Setting up a simple VM with Vagrant


The first thing to do is get a simple VM up and running. The
      word from my colleagues was that [Vagrant](https://www.vagrantup.com/) was the best way to
      sort this out. For the guest I went for Ubuntu 14.04, since that
      seemed to be the popular choice for a guest system. As a handy
      coincidence the box I was working on to do this was also running
      14.04. But annoyingly the version of Vagrant that's packaged
      with Ubuntu 14.04 isn't set to run a 14.04 guest, so I had to
      download and install the latest copy of Vagrant (1.6.3)
      manually. It comes packaged as a deb file, so it was pretty
      straightforward, but I did flail around for a bit trying to get
      things to work with the earlier version before I realized I
      needed to do that.


To get a bare Vagrant box running, you need a control file
      called `Vagrantfile`. For a simple example this
      control file can just contain:


```
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
end

```


This tells Vagrant to create a VM based on 64 bit ubuntu
      trusty (which is 14.04). With this Vagrantfile in place, you can
      then create and start a VM with `vagrant up`. Once
      the machine has created itself and started up you can log into
      it with `vagrant ssh`. You'll notice that Vagrant has
      created a user called `vagrant` and logs you in using
      ssh keys. 1 The vagrant user is
      able to sudo without a password and is what Vagrant uses to
      control the administration of the machine.


1: 
      This is an insecure key, the private key ships with Vagrant. For
      a simple machine only accessible via host (as in this case) this
      is fine.


You can stop the machine with `vagrant halt` and
      destroy the machine completely with `vagrant
      destroy`. The `vagrant up` command will either
      start the existing machine or create one and start it if one
      isn't already created. Vagrant uses a default machine for this,
      there are ways to handle multiple machines, but I haven't
      explored them.


## Provisioning with Chef


Vagrant gets me a bare machine, but such a machine needs to
      be provisioned with software so I can do useful things with it.
      The whole point of this operation is to make it as automatic as
      possible, so a collaborator can just fire up a few commands and
      have the VM ready to go with no awkward installation
      instructions.


One way to do this might be to run an installation script in
      the VM, but generally a better way is to use software designed
      for provisioning machines, such as [Puppet](http://puppetlabs.com/), [Chef](http://www.getchef.com/chef/), or [Ansible](http://www.ansible.com/). I picked Chef, not due to
      any detailed evaluation, but because I know someone who works
      there, in case I need a Friend With Influence.


Unfortunately, Chef's documentation was pretty unhelpful at
      this point, because it's written for the case when you're
      managing hundreds of servers. There's little documentation on
      just setting up a single server like this and I had to hunt
      around for a while to figure out what I should do.


The key thing to google for is [chef-solo](https://docs.getchef.com/chef_solo.html), a
      version of Chef for handling this kind of single-server
      scenario. Vagrant has the necessary hooks to play in with
      chef-solo, so the two go well together. 2


2: 
      The Chef docs say that you should use the local mode of
      chef-client rather than chef-solo. However I could no
      documentation on how to use it and chef-solo seems to be what
      Vagrant likes, at least for the moment.


My folder for setting up the Vagrant VM contains two entries: the
      `Vagrantfile`  and
      `cookbooks` which is a directory that contains the
      instructions for Chef. (Chef does overegg its culinary
      metaphors.) To get a basic
      server up and provisioned with Chef I needed the following in the
      Vagrantfile.


Vagrantfile


```
  VAGRANTFILE_API_VERSION = "2"
  
  Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
  
    config.vm.provision :chef_solo do |chef|
      chef.add_recipe "mfweb"
    end
  end
```


This tells me to base my VM image on ubuntu trusty 64bit
      system and provision the new machine with chef-solo using the
      âmfwebâ recipe.


The mfweb recipe is inside the cookbooks folder, which
      expanded looks like this:


```
cookbooks
âââ mfweb
    âââ files
    â   âââ default
    â       âââ home-web
    â           âââ â¦
    âââ libraries
    â   âââ helpers.rb
    âââ recipes
        âââ default.rb

```


In Chef, a cookbook is a group of provisioning information.
      Various things can appear in a cookbook, but I needed three main
      sections:

- files: various files and directories that need to be
        copied over to the VM
- libraries: helper code for the recipes
- recipes: the code that specifies the configuration for the
        VM


Since I'm very familiar with ruby, it's handy that Chef (and
      Vagrant) both use ruby as their programming language. Chef
      recipes use a ruby internal DSL, which works out rather well for
      me.


On the less happy front, however, the overall structure for
      Chef is complicated - more than is needed for my
      single server example. The hardest part of working with Chef
      was to figure out which little bits of the system I actually needed
      to understand. The complexity isn't needless for Chef's primary
      audience, but it did make it tricksy for me.


Like many configuration tools, Chef works as much as possible
      in a declarative way. Rather than a configuration script which
      sequences various commands, a Chef recipe instead tries to
      describe the state of the machine. The Chef runtime then
      compares this desired state with the actual state of the machine
      and carries out whatever actions are needed to bring the machine
      to the desired state.


For example, let's imagine we want the file âhello.txtâ to
      appear in `/home/vagrant`. The fragment for this in
      the recipe file (`cookbooks/recipes/default.rb`) is


```
file "/home/vagrant/hello.txt" do
  content "hello world"
end

```


That fragment says that I want to have the file in the
      specified place with the given content. When I run the
      recipe, Chef looks to see if there's such a file in position, if
      not it creates it. It also looks to see if the content is correct
      and again changes it if necessary.


Such a declarative structure makes plenty of sense for
      provisioning a machine. However the downside is that should
      things go pear-shaped and you need to debug, then it can be very
      hard to figure out what is being executed in what order. Since I
      don't really want to be a Chef expert, but just to get my
      simple VM configured, that can be a problem. Overall, however, it
      does work well most of the time. Certainly if I was doing
      regular sysadmin work again, I'd want to get very familiar with
      a tool like this.


In the context of Vagrant, the act of provisioning can occur
      at various points. If you are creating a machine from scratch,
      it will be provisioned as it's made. If you have a running
      machine and want to re-provision it without rebooting it, you
      can do so with `vagrant provision`. To reboot in
      Vagrant you use `vagrant reload`, which also reloads
      any changes in the `Vagrantfile`. However a reload does not run
      the provisioning recipe unless you tell it to with `vagrant
      reload --provision`.


One of the important parts of provisioning is to load up
      software, and the primary way to do this with Ubuntu is with its
      packaging system. With Chef, you can install packages using the
      package command


```
package 'nodejs'
```


Since the Chef recipes are ruby, I can also use ruby's
      language features if I wish. So if I have multiple packages to
      install, I like using its ability to easily define and use word
      arrays


```
%w[build-essential openssl libreadline6 libreadline6-dev].each {|p| package p}

```


## Creating a new user


One of the tribulations of trying to get this VM working was
       dealing with the different ruby versions. The vagrant account
       is used for administration and I was concerned that having the
       different ruby versions inside it was causing complications
       with the provisioning. So I created a separate user to for the
       programming work. With hindsight I'm not sure all this was helpful
       and I may remove it in the future to simplify the VM's setup, but
       here's how I did it.


Creating a new user starts with defining the user in the
       recipe file.


cookbooks/mfweb/recipes/default.rb


```
  user "web" do
    home '/home/web'
    shell '/bin/bash'
  end
```


But all this does is create the user and specify its home
       directory, I need to do more to actually create the home
       directory.


default.rb


```
  remote_directory "/home/web" do
    user 'web'
    files_owner 'web'
    source 'home-web'
  end
```


I use the remote_directory resource in Chef to put
        the contents of the source directory 
       `cookbooks/mfweb/files/default/home-web` into the
       VM's home directory. Any file on
       the VM that isn't in the source directory won't be touched
       (there is an option to purge such files). I can then put things
       like `.bashrc` and other handy files into the source
       directory and have them copied over to the machine whenever I
       provision it.


These steps create the user and a home directory, but give
       us no way to log in. It makes sense to use the same ssh
       mechanism as the vagrant user has, so it seems sensible to copy
       the vagrant user's `.ssh` directory to do so. I considered using
       Chef's file resource (since it's non-secure key), but whatever
       approach I used there's fiddling with ownership and permission
       modes to do, so I resorted to Chef's ability to execute a shell
       command.


default.rb


```
  execute "copy-ssh" do
    command "cd ~web ; cp -r ~vagrant/.ssh . && chmod 700 .ssh && chown -R web .ssh"
  end
```


With that done I can now log into the new account with


```
vagrant ssh -- -l web
```


## Using a helper to remove duplication


This creates the user and directory pretty well, but there
       is duplication in the user and folder names, duplication that
       will get worse as I write more of the recipe file. I could
       avoid much of this by using constants, something like:


```
USER = 'web'
HOME_DIR = File.join('/home', USER)
user USER do 
  home HOME_DIR
  shell '/bin/bash'
end

```


but I decided to go a different route and define a helper
       object instead. I set the helper object up with bits of data
       that it needs and then use it whenever I see repetitive code in
       the configuration. The helper lives in
       `cookbooks/mfweb/libraries` - it seems any ruby file
       there is automatically required and available to the
       recipe.


helper.rb


```
  module Mfweb
    class Helper
      attr_reader :user, :ruby_version
  
      def initialize ruby_version, user
        @ruby_version = ruby_version
        @user = user
      end
      def home *args
        File.join("/home", @user, *args)
      end
```


I can then use it like this


default.rb


```
  helper = Mfweb::Helper.new("2.1.2", 'web')
  
  user helper.user do
    home helper.home
    shell '/bin/bash'
  end
  remote_directory helper.home do
    user helper.user
    files_owner helper.user
    source 'home-web'
  end
  execute "copy-ssh" do
    command  "cd #{helper.home} ; cp -r ~vagrant/.ssh . && chmod 700 .ssh && chown -R #{helper.user} .ssh"
  end
```


Using helpers rather than constants has become a habit for
       me now. I prefer to keep any string manipulation in a function
       and prefer using functions to constants so I can easily replace
       a simple constant with a function at will. Bundling the
       functions into an object allows me to keep the state together
       with the functions in a clear namespace. I usually dislike âhelperâ as
       the name of a class, since it implies nothing more than an
       arbitrary collection of functions and data, but in this kind of
       context that describes it's role perfectly well.


## Syncing the development tree


In order to be able to build anything, we need to get the
       various sources into the VM. Since I keep the sources in git,
       one way to do this would be to use git to clone the repository
       in the VM. But although I want to use the VM to run the build,
       I'd rather do all the editing on my host machine. Fortunately
       Vagrant makes it easy to share a directory between the host and
       VM, syncing them up whenever you make a change. To do this you
       put declare the synced files in the Vagrantfile.


Vagrantfile


```
  Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.synced_folder("..", "/home/web/mfcom", :owner => 'web')
    # other steps in configuration â¦
```


I made the sources for the vagrant work a folder inside the
       overall project repo, so the synced folder is the parent.


In doing this, I ran into an annoying problem. The first
       time I create a new machine, it refuses to create the synced
       folder, giving me an error saying 'the âvboxsfâ file system is
       not available'. But if I then do `vagrant reload` it
       brings up the machine just fine. I can work around this by
       first running a new machine with the synced_folder config
       commented out, then reloading with it present.


## HTML Output


The output of the build is a website, so it makes sense to add
       apache to the VM so we can see the results.


default.rb


```
  package "apache2"
  
  execute "set-html_dir" do
    command "rm -r /var/www/html; ln -s #{helper.html} /var/www/html"
  end
```


Sadly I have to use the execute resource here. Chef has a
       link resource to setup links, but won't overwrite the existing
       directory entry made by the apache installation.


With that, I can then map port 80 on the VM to a port on the
       host.


Vagrantfile


```
  Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
      # other config â¦
      config.vm.network :forwarded_port, guest: 80, host: 2929
  end
```


## Using rbenv to install Ruby 2.1.2


Like many users of ruby I use a switcher on my laptop to
       switch between ruby versions. I prefer [rbenv](https://github.com/sstephenson/rbenv) as I dislike
       the way rvm manipulates my shell (replacing cd with a shell
       function). Since the VM is only used for a single purpose,
       there's a good argument for not using a switcher at all on it -
       I could just install the appropriate ruby version as the system
       ruby, as you would for a production system. But I decided to
       use rbenv as that way it would mirror the systems being used by
       those like me who are running tools directly on their machine
       without a VM in the picture.


My first approach to installing rbenv, and its associated
       ruby-build, was to use the Chef cookbooks 3. But after wrestling with them for several
       hours I couldn't get them to work properly. I couldn't figure
       out how to install the rubies into `~/rbenv` instead
       of `/usr/local` and I got into a tangle where I
       would install a gem and it wouldn't show up with `gem
       list`. So I abandoned the Chef cookbooks.


3: 
      These were [chef-rbenv](https://github.com/fnichol/chef-rbenv) and [chef-ruby_build](https://github.com/fnichol/chef-ruby_build)


My next try was to use the Chef execute resource so the
       installation could run during provisioning. But there I got
       tangled up in getting the scripts to run with the correct
       versions. I couldn't get the execute commands to work with an
       environment such that it would pick up the correct set of rbenv
       shims to run the right version of ruby. So ended up giving up
       on doing the ruby install during provisioning, instead I did as
       much as I could during provisioning and then used a bootstrap
       script that needed to be run manually within the VM.


The first step in all this is to use git to download the
       rbenv repository.


default.rb


```
  package 'git'
  
  git(helper.rbenv_home) do
    repository 'https://github.com/sstephenson/rbenv.git'
    user helper.user
    revision 'v0.4.0'
  end
```


A couple of things about that fragment. First you'll notice
       that I specified a particular tag to check out and use. I do
       this because it's important to have a [Reproducible Build](https://martinfowler.com/bliki/ReproducibleBuild.html). That way if trouble strikes, I can
       use the git history of my Vagrant setup to help track
       problems. Secondly I've written another method on my helper
       object for the rbenv installation location.


helper.rb


```
  class MfCom::Helper
      def rbenv_home *args
        home('.rbenv', *args)
      end
      â¦
```


I also want to install ruby-builder, which is rbenv's sister
       project that installs new rubies. I install it into the plugins
       directory in rbenv so I can use rbenv's install command.


default.rb


```
  directory(helper.rbenv_home('plugins')) do
    user helper.user
  end
  
  git(helper.rbenv_home('plugins/ruby-build')) do
    repository 'https://github.com/sstephenson/ruby-build.git'
    user helper.user
    revision 'v20140702'
  end
```


Chef can also install various libraries needed for ruby to
       compile. I got this list from Somewhere On The Internet, and it may
       be that some of them aren't needed.


default.rb


```
  %w[build-essential bison openssl libreadline6 libreadline6-dev
  zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0
  libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev autoconf
  libc6-dev ssl-cert subversion].each do |p|
    package p
  end
```


All of this prepares the ground for installing the correct
       Ruby. To finish the job I include a bootstrap script in
       `cookbooks/mfweb/files/default/home-web`


```
read -r VERSION < mfcom/.ruby-version
if [ -f .rbenv/versions/${VERSION}/bin/ruby ]; then
  echo "ruby ${VERSION} is already installed"
else
  rbenv install $VERSION
fi
cd mfcom
gem install bundler --no-rdoc --no-ri
rbenv rehash
bundle install --without=mac

```


To run it, the user of the VM needs to login to the web
       account and run


```
sh bootstrap
```


The bootstrap takes a while to run as it compiles and
       installs the correct ruby version to be managed by rbenv. It
       then also installs bundler and uses it to install all the gems
       needed for development.


## Installing coffeescript


As well as ruby, I also need coffeescript in the development
       environment. Fortunately this is easy to install.


default.rb


```
  %w[nodejs npm].each {|p| package p}
  
  execute "node-packages" do
    command "npm install -g coffee-script@1.6.3"
  end
  
  # annoyingly mac and ubuntu use different commands for node
  link "/usr/bin/node" do
    to  "/usr/bin/nodejs"
  end
```


I didn't look for a Chef cookbook for npm, the execute
       option seems to work well-enough. The version of coffee is the
       one currently on my laptop, I should probably look at upgrading
       it.


## Was it worth it?


On the whole all this took much longer than I'd hoped, and
       sucked up about a week's worth of writing time. It will be
       worthwhile iff it saves my collaborators time in the future, or
       this article saves other people some time when doing something
       similar. I would certainly have done it much quicker if I knew
       what's in this article before I started.


Do let me know if any of things I talk about here are
       wrong-headed. It may not be worth updating the setup I now
       have, but I can at least put some warnings and pointers to other approaches
       into this article.


---
