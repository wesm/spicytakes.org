---
title: "Marketing A Superhero Novel (Web Admin Hackery Galore)"
date: 2007-08-23
url: https://www.kalzumeus.com/2007/08/23/marketing-superhero-novel/
slug: marketing-superhero-novel
word_count: 1308
---


Around the same time I started Bingo Card Creator, my little brother got bitten by the Do A Cool Project bug and decided to become a published fiction author.  He is writing a [superhero novel](http://www.superheronation.com) and, aside from this post being a totally transparent attempt to give him some SEO juice to get him kicking, I’d like to recount what we’re doing to market a product that, strictly speaking, doesn’t exist yet.  This is mostly going to be a technical overview — if folks have interest, I’ll go over some of the softer side of marketing at a later date.


Keep in mind that I am a programmer, not a system administrator.  Don’t do these instructions on a production box without testing it first, OK?  They worked for me, but if they don’t for you my liability is limited to refunding the amount you paid for this blog post.


Priority #1 — Setup a website.  I’m sure you’re shocked.


Specifically, because my brother is more skilled in dialogue writing than in web server administration, I set him up with WordPress to make the barriers to content creation nothing.  He had already had a blog he used for writing on WordPress.com, so moving him to hosted WordPress wasn’t much work from his perspective (we could even import all the old posts).  From my perspective, it was a bit of work getting SuperheroNation.com to coexist peacefully with Kalzumeus’ Rails test site on a single 256 MB [Slicehost](http://www.slicehost.com) VPS, but after a night it was up and running.  (You can do this to **host Rails and WordPress on the same domain**, but the instructions are different and I’ll give them to you at a later date).** **


Why go with hosted WordPress rather than WordPress.com?  It gives the site room to grow, and gives my brother control — he can incorporate Google Analytics throughout via a plugin (ahem, **DO IT**), and when he is ready to start selling the book throwing up e-junkie’s Fat Free Cart, a nice custom skin, and other features is very easy.  If you’re just starting your own site, for SEO purposes if nothing else, put it on a domain you control rather than wordpress.com.  It is a pain in the butt to set up, but moving a blog OFF wordpress is infinitely harder than getting WordPress up and running somewhere else and then making the changes you want down the road.


Here’s what you need to do, assuming you’re serving Rails with Apache proxying to a Mongrel cluster (works like a beauty even at 256MB, incidentally, although I haven’t tested it under severe load):


1)  First, you’ll want to get WordPress installed.  If you’re hosting two domains on the same box, I’d recommend distinct directory structures for them — the non-Rails domain here resides in /var/www/superheronation/, and the Rails stuff is in a completely different path set automatically by deprec (see below).  After creating the directory, go over to wordpress.org, download the zip file, unzip it, and stick it in a subdirectory named wordpress (so, in my example, /var/www/superheronation/wordpress) .  We’re putting it in wordpress rather than in something descriptively named because if we change blogging platforms later we can do most of the job just by changing one line in a config file.  (By the way, wondering what to call your blog’s main user-visible directory?  I like “blog”, but a high value keyword works better for SEO… at least for now.)


1b) **Skip this step if not a Slicehost customer.**  There is a problem with installing WordPress.org on Slicehost — by default, Slicehost setups don’t come with a mail server, and for reasons only God knows WordPress.org dies with a silent error if PHP can’t mail you your password during an install.  Don’t ask me what the security rationale for that one is.  Happily, WordPress.org is open source and you can quickly hack together a solution — go to the wp-admin/upgrade-functions.php file, comment out (put a # sign in front of ) this line:


> wp_new_blog_notification($blog_title, $guessurl, $user_id, $random_password);


and this line:


> $random_password = substr(md5(uniqid(microtime())), 0, 6);


replacing it instead with


> $random_password = ‘for_love_of_little_apples_change_me’;


Now you can follow wordpress.org’s 5 minute install directions without blowing stuff up.  Or, you could, if your web server was actually serving up your blog yet.  Its not, since you haven’t told it that your second domain exists.


2)  Locate your Apache config file for your Rails installation.  If you did the setup for your Rails site using [deprec](http://www.deprec.org) (*highly* recommended — it will save your sanity and many days of tweaking config files, and it [works beautifully with Slicehost](http://wiki.slicehost.com/doku.php?id=automated_rails_install_and_deployment_with_deprec_capistrano)), this will be in /usr/local/apache2/conf/apps/nameOfYourApp.conf .  Copy it to another .conf file of your choice.


3)  Working on your second copy, edit the VirtualHost declaration to read


> <VirtualHost www.nameofyourdomain.com:80>


That is Apache speak for “If the web browser asks for anything under this domain, use the following options”.  You’re going to point the DocumentRoot to /var/www/superheronation/ or wherever you put this domain, and set the ServerName and ServerAlias from whatever your Rails domain is to whatever your WordPress domain is.  Now replace the catchall VirtualHost (VirtualHost *:80) with the same sort of name-based virtual host, in the nameOfYourApp.conf file.


4)  Now for the magic — we want Apache’s awesomely powerful rewrite engine to send the appropriate things to WordPress, while leaving the rest to Rails.  Here’s exactly what you need after RewriteEngine On for the seperate domain case:


> # Let apache handle the PHP files – all requests that get past this rule
>  # are routed to the mongrel cluster (aka Rails)
>  #  – wordpress installation assumeed to be in ‘public/wordpress’
>  #  – Options: NC – case insensitive
>  #  –          QSA – query string append
>  #  –          L – last rule, aka stop here if rewriterule condition is matched


> # Prevent access to .svn directories
>    RewriteRule ^(.*/)?\.svn/ – [F,L]
>    ErrorDocument 403 “Access Forbidden”
>     # Check for maintenance file and redirect all request
>    RewriteCond %{DOCUMENT_ROOT}/system/maintenance.html -f
>    RewriteCond %{SCRIPT_FILENAME} !maintenance.html
>    RewriteRule ^.*$ /system/maintenance.html [L]
>     # OMIT THIS LINE if you have don’t want to automatically redirect everything from the domain to the blog.
>    RewriteRule ^/$ %{DOCUMENT_ROOT}/wordpress/ [NC,QSA,L]
> RewriteCond %{REQUEST_FILENAME} !-f


> RewriteCond %{REQUEST_FILENAME} !-d


> RewriteRule . %{DOCUMENT_ROOT}/wordpress/index.php [L]
>     # Rewrite to check for Rails cached page
>    #RewriteRule ^([^.]+)$ $1.html [QSA]
>     # Redirect all non-static requests to cluster
>    #RewriteCond %{DOCUMENT_ROOT}/%{REQUEST_FILENAME} !-f
>    #RewriteRule ^/(.*)$ balancer://**deprec_will_fill_this_in**_cluster%{REQUEST_URI} [P,QSA,L]


5)  Cleanup tasks:


Make sure Apache knows that .php files are first class citizens by editing /usr/local/apache2/conf/httpd.conf and replacing the line with DirectoryIndex to read


> DirectoryIndex index.php index.html


And, at the way bottom of that file, comment out the Include statement and replace the NameVirtualHost directives with


> NameVirtualHost www.rails_domain.com:80
>  Include conf/apps/rails_application_name.conf
>  NameVirtualHost www.wordpress_domain_name.com:80
>  Include conf/apps/wordpress_config_file.conf


That should be it.  You can now restart Apache (“sudo /etc/init.d/httpd restart”), and you should be able to access your WordPress blog and complete installation of it.  I’d **HIGHLY** recommend changing your Admin password, creating another Admin user with a non-Admin name, and changing your Preferences -> Permalinks to a non-default option which includes your post title, for SEO purposes (the 3rd option works nicely).


6)  Don’t forget to update whoever holds your DNS records to point your domains to your slice’s IP address.  For me, this involves telling GoDaddy to use ns1.slicehost.net, ns2, and ns3 as DNS servers for superheronation.com, and then going into the Slicehost config and telling Slicehost to point superheronation.com and www.superheronation.com to the IP address of the slice I bought.  (Handily listed on the bottom of that screen.)


**And there you have it!  **Two websites running off of two very different technology stacks on a $20 a month VPS.  They’ll both perform marvelously under load, too…  I hope.
