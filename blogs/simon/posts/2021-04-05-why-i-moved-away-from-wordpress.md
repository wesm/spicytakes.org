---
title: "Saying Goodbye to WordPress, a Homecoming04-05"
date: 2021-04-05
url: https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/
slug: why-i-moved-away-from-wordpress
word_count: 1328
---

![Saying Goodbye to WordPress, a Homecoming](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/website-2005.jpg)

Contents

## A brief of history


When I began my journey with websites, I started as many of us with HTML, CSS, HTML & MySQL running on an Apache Webserver. Those days I prepared all recurring code inside to include PHP files and had content either as HTML itself or dynamically pulled from the MySQL database. And how that looked you see in the featured image of this post 😉.


Later, I moved to [WordPress](https://wordpress.com/) to make the page more modern, chose a cool template, adding templates and automatise a lot. WordPress helped me a ton with plugins like [SEO Yoast](https://yoast.com/wordpress/plugins/seo/) to optimise for Google Search. As well could I quickly change my posts with the editor of WordPress.


![/blog/why-i-moved-away-from-wordpress/img/sspaeti-wayback-machine-2004-2021.jpg](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/sspaeti-wayback-machine-2004-2021.jpg)

*The history and snapshot of sspaeti.com byWaybackMachine*


Below you see how it looked before the update. Many hours were spent to find the right plugins, e.g. for showing a gallery in my [Today’s Office](https://www.ssp.sh/blog/the-location-independent-lifestyle/) post, or calculating the reading time, or that you can share marked text directly with Social Media with one click (I don’t think anyone ever used that 😉), finding the right widgets to put on the side, fiddling with CSS to make it look nice,   and so on!


![/blog/why-i-moved-away-from-wordpress/img/sspaeti-wp-dark-page.jpg](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/sspaeti-wp-dark-page.jpg)

*Page beginning of 2021*


## Why I was searching for alternatives?


Lately, I always crafted my blog post in OneNote or in [MarkText](https://marktext.app/) or other MarkDown- Editors. These made me always copy-pasting and converting it from the markdown format back to WordPress. At the same time, WordPress itself changed a lot with its new [Gutenberg Editor](https://wordpress.org/gutenberg/) and other updates. Unfortunately, my template didn’t support Gutenberg, meaning I always had to use the old classic editor. And that’s where things got complicated as I had to deactivate Gutenberg’s update; otherwise, I couldn’t edit my blog pages anymore. Some plugins started to produce errors, forcing me to check the website after every WordPress or plugin update. That was one reason why I invested in [Jetpack](https://wordpress.org/plugins/jetpack/), which gave me, to some extent a peace of mind with backups and other excellent features.

The struggle with managing all installed plugins on WP

Besides WordPress updates, Editors and others, the plugins I was constantly juggling.


![](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/wp-plugins.jpg)

*Latest installed Plugins for simple Blog Page*


Additionally, I didn’t have a local deployment running. I made every change in the production environment live on the website. If something happened, I had to revert from these backups.


Besides just wanting to upload text as markdown-code, the boiler code and its burdens made me lookout for alternatives. I always fancied something that works well with [git](https://en.wikipedia.org/wiki/Git) and treats the text as code.


## What I found


After searching for Python-based frameworks, I quickly found topics around [Static Site Generators (SSG)](https://www.netlify.com/blog/2020/04/14/what-is-a-static-site-generator-and-3-ways-to-find-the-best-one/) and with it [GoHugo](https://gohugo.io/). Without more extensive research, I just started using it and get a feeling for it. Below are the first steps which keep you going with GoHugo.



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
` | `brew install hugo
#load example blog
hugo new site quickstart
cd quickstart
git init
#adding a template
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo theme = \"ananke\" >> config.toml
#adding a new post
hugo new posts/my-first-post.md
` |



To start seeing your build website live on your local machine, you start the webserver, which automatically updates every change. And within seconds, that’s also where GoHugo seems to have an advantage over other SSGs, which are fast on production but not as quickly to render locally.



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
` | `hugo server -D
                   | EN
+------------------+----+
  Pages            | 10
  Paginator pages  |  0
  Non-page files   |  0
  Static files     |  3
  Processed images |  0
  Aliases          |  1
  Sitemaps         |  1
  Cleaned          |  0

Total in 11 ms
Watching for changes in /Users/bep/quickstart/{content,data,layouts,static,themes}
Watching for config changes in /Users/bep/quickstart/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For complete rebuilds on change: Hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind-address 127.0.0.1)
Press Ctrl+C to stop
` |



This produces this static website which can live opened and edited on `localhost:1313`.


## How the migration worked


I migrated as quick as I did because of how convenient it was to export the entire content I had written over time. I used [wordpress-to-hugo-exporter](https://github.com/SchumacherFM/wordpress-to-hugo-exporter), which is one of the provided [plugins](https://gohugo.io/tools/migrations/#wordpress) on GoHugo. After exporting, I had all my post as single markdown files and all images linked to them.


## What’s the Outcome?


As of today, migrated over to the next generation of blog pages:


![/blog/why-i-moved-away-from-wordpress/img/sspaeti_new_hugo_page_top.jpg](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/sspaeti_new_hugo_page_top.jpg)

*sspaeti.com as of today April 2021*


Or you can review also for yourself on the website you currently reading this 😉. One of the things I was curious about was the speed of the rendered webpage. That’s why I checked both the old WordPress page and this current one with [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/).


### Speed start site


Here you can see the main page’s speed where it shows all different posts on the blog. The site measured is before the update.


[

](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/wp-speed-home-desktop-mobile.jpg)Main Website before (left: Desktop, right: Mobile)


Now with GoHugo without optimising anything yet, especially the images, that’s how it looks now:


[

](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/gohugo-speed-home-desktop-mobile.jpg)Main Website after (left: Desktop, right: Mobile)


### Speed blog page


An effective blog page with lots of content I compared next. I compared my latest Blog post with lots of images, code snippets, YouTube and Twitter references. Below you see the result with WordPress:


[

](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/wp-speed-blog-post-desktop-mobile.jpg)Blog Post Website after (left: Desktop, right: Mobile)


After that as of today, again without [opimisinig the image size](https://web.dev/uses-webp-images/?utm_source=lighthouse&utm_medium=unknown) or any other problems:


[

](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/img/gohugo-speed-blog-post-desktop-mobile.jpg)Blog Post Website after (left: Desktop, right: Mobile)

Update SEO and Image Sizes

After moving images from `/static/images/` to the content folder of each blog e.g. `/content/posts/why-i-moved-away-from-wordpress/images/` with [wp-to-gohugo-image-mover.py](https://gist.github.com/sspaeti/eab0faa8674cf19d92bd4a344857b0ba), I could add [image reprocessing](https://gohugo.io/content-management/image-processing/) to add different sizes for different devices and display resolution. Also resized all images to max 1024px width and quality to 85%. As well optimised some minor SEO fixes and now it looks like this:


![/blog/why-i-moved-away-from-wordpress/img/sspaeti_new_hugo_page-optimised-de.jpg](img/sspaeti_new_hugo_page-optimised-de.jpg)

*Blog Post Website after some optimisation (left: Desktop, right: Mobile)*


Not really good still, but I have to say that this blog post has the most external content with YouTube, Twitter Clips etc., other Blog post with also a lot of images looking much better.


![/blog/why-i-moved-away-from-wordpress/img/sspaeti_new_hugo_page-optimised.jpg](img/sspaeti_new_hugo_page-optimised.jpg)

*An other Blog Post Website after the optimisation (left: Desktop, right: Mobile)*


## Conclusion


As seen, the speed is not that impressive for a specific blog post yet. But still, it’s an improvement. And anyway, the real power for me, at least, is having the text right in front of me as markdown same as code, easily pushable to git. Compared to before, where it was hidden away in a MySQL database with no real access.


It surprised me how much fun it can be to write and generate new content again! I guess only for that fact I will create more content in the future than I did lately.


The workflow of writing and updating content has drastically changed. I can edit anything, see the live output locally as it would on my server, generate the static HTML and deploy with one straightforward deploy-script. I feel like going back to where it started in 2005, where everything is small and simple in one (git) repo. The plugins and features are in one subfolder of my repo, nicely integrated and easy to understand and tweak existing templates.


If you’re thinking about similar things or getting frustrated with WordPress Pages’ overhead, I suggest you give GoHugo a try. The best part is that security, scale and performance are improved radically with static site generation. You could also host it on your NAS or any server laying around, in case you’re thinking to start your blog.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Wordpress](https://www.ssp.sh/tags/wordpress/)
[Website](https://www.ssp.sh/tags/website/)
[Gohugo](https://www.ssp.sh/tags/gohugo/)
[Notetaking](https://www.ssp.sh/tags/notetaking/)
