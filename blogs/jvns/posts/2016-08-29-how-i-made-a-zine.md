---
title: "How (and why) I made a zine"
date: 2016-08-29
url: https://jvns.ca/blog/2016/08/29/how-i-made-a-zine/
slug: how-i-made-a-zine
word_count: 1625
---


I just finished up a zine project (it will be up soon [here](https://wizardzines.com)! I will let you all know when it is up DO NOT WORRY).


A few people asked me how a zine is made so I thought I’d write down the
process.


### what’s a zine? why write zines?


A zine is a short informal publication, often handwritten or hand-assembled. I
have zines about a) someone’s life and what she thinks about stuff (a
“perzine”) b) star trek c) what it’s like for one person to be deaf and date a
non-deaf person d) french expressions for english speakers e) following a band
around Canada for a summer f) safer sex.


They’re often first-person and about a really specific thing. And delightful. You know what has a lot of really specific things? PROGRAMMING.


In 2014, I gave a talk at PyCon about debugging tools I loved. When I was preparing for that talk, Amelia Greenhall had just written this really excellent article [Start your own b(r)and: Everything I know about starting collaborative, feminist publications](https://geekfeminism.org/2015/01/28/cross-post-start-your-own-brand-everything-i-know-about-starting-collaborative-feminist-publications/). If you’re interested at all in publishing things you should read it – it has a lot of really practical advice.


I’ve always found stories of people starting their own publications compelling (that’s why I write a blog, after all!!), and I was like ME. I WANT TO START A MEDIA COMPANY.


I came down from that after about 30 seconds. But I still wanted to publish something! A paper thing! And this article was about feminist things, and I’d read this book [Girls to the Front: The True Story of the Riot Grrrl Revolution Paperback](https://www.amazon.ca/Girls-Front-Story-Grrrl-Revolution/dp/0061806366) about riot grrl and people making feminist zines and starting punk bands, and I was like ME. I WANT TO MAKE A ZINE ABOUT THINGS THAT I LIKE.


And I was giving this talk! I remembered hearing that Edward Tufte gave out
handouts in talks, and I thought that was a cool idea, so I figured I’d try
it. I tweeted something like


> omg guys i want to write a zine about strace


and everyone was like


> yes obviously this is a great idea


So I decided to write a zine and give it out as a handout in my talk.


### making things fun is a great way to teach


the reason I write zines is partly because I think they’re fun, but also for
practical reasons. Fun, accessible content *works*. People understand it. In
my most recent zine, I explain netstat, netcat, ngrep, tcpdump, wireshark,
strace, eBPF, dstat, and perf and a bunch of its subcommands. This is a lot of
stuff!! But because it’s presented in an adorable tiny zine people are like
“oh how interesting and cute!” and don’t hesitate to pick it up.


Some of the things I want to explain are traditionally considered kind of
advanced! I didn’t learn about any of these things until I’d been
programming for 10 years. But there’s no reason I couldn’t have
learned them earlier! It’s just that nobody told me.


What I end up finding is that people will read my zines who I wouldn’t expect.
People will read them even if they’re new to programming or new to Linux! And
they’ll often learn something and tell me “yeah, sure, I didn’t understand
100% of it but a lot of it made sense!” To me this is a HUGE WIN.


I spent years being scared of tcpdump. But it’s not really that scary, and if
I can help a few people be a little less intimidated by it, then I’ve done my
job.


### the tools


For the first zine I wrote I:

- cut pieces of letter paper in half
- wrote on them in sharpie and pen
- went to a photocopy shop and assembled the zine by hand with a photocopier
- gave the master copy to the print shop people to copy
- scanned it and put it on my blog


pretty basic, really cheap, pretty easy.


The first zine ([about strace](https://wizardzines.com/zines/strace)) looked like this:


![](https://jvns.ca/images/strace_zine.png)


I thought it looked great and I was delighted with it. I had been thinking
about feminist zines so I wrote a manifesto:


![](https://jvns.ca/images/drawings/manifesto.png)


Honestly I found sharpie got kind of old though – it worked well, but it
sucks to not be able to erase anything and  scanning is annoying. I thought
about buying a tablet and I tried out the ipad pro with an apple pen. That was
MAGICAL. It was also a thousand dollars and I am super clumsy so I was
definitely not buying a $1000 tablet to draw zines.


Then I discovered the **samsung galaxy tab a 9.7**, a super magical android tablet that was only $300 but let me draw super cool stuff. It comes with the Samsung “S pen” which works really well. If you’ve seen me post something that looks like this:


it comes from that tablet. This is way easier to work with (I can come up with something and just click “share -> Twitter”!)


So, I made a bunch of images and saved them. I used the Autodesk sketchbook
app. They have a pro version that costs $7 or something. It’s pretty awesome.


The second zine looks like this:


It was easier to edit and make improvements which meant less weird charming
mistakes but also I think I could put in more information! calling that a win.


So! if you have a bunch of pages for a zine, how do you get them into a PDF
you can bring to a print shop?


### making pictures into pdfs


This is possibly super boring to everyone but me but here is how I turn a
bunch of pictures into pdfs. There are a bunch of awesome tiny pdf utilities
out there. It took me a bunch of time to figure out how to put them together
to do what I wanted.


```
# start with a bunch of PNG images of your zine pages
# convert them all to PDF
for i in *.png
   do
   	  # imagemagick is the best thing in the world
      convert $i $i.pdf
   done

# pdftk is awesome for combining pdfs into a single pdf
pdftk *.pdf cat output zine.pdf

# pdfmod is a GUI that lets you reorder pages
pdfmod zine.pdf

# pdfcrop lets you add margins to the pdf. this is good because otherwise the
# printer will cut off stuff at the edges
pdfcrop --margin '29 29 29 29' zine.pdf zine-intermediate.pdf

# pdfjam is this wizard tool that lets you take a normal ordered pdf and turn
# it into something you can print as a booklet on a regular printer.
# no more worrying about photocopying machines
pdfjam --booklet true --landscape --suffix book --letterpaper --signature 12 --booklet true --landscape zine-intermediate.pdf -o zine-booklet.pdf

```


### printing!!!


This is the MOST FUN PART. You get to mass produce things and give them to people!!!!!!!!! Getting a huge stack of zines is like the best thing.


So! This was a surprise to me but *print shops know how to print booklets*.
They have MACHINES that can fold and staple zines! So if you want to print 200
zines, you can literally bring a pdf, leave it with them, and they will
produce a box of amazing zines that are ready to go.


This is always kind of heartening to me because I have trouble printing the
zine and so do the print shop employees! Everyone always gets it wrong the
first time and something is upside down. But then we fix it and it’s fine.
Printers are hard!!


It’s not super super cheap – I’ve paid between $0.75 and $1.50 per zine to
print them. But I would much rather pay $0.25 each to get it stapled than to
staple 400 zines myself, since I can afford it.


### distribution


Mostly I give away zines at conferences (“HELLO HAVE YOU HEARD THE GOOD WORD
ABOUT STRACE???”) and let people download the pdf on my website. This is
really fun and I think I have converted people to strace with a zine who would
not have taken the time to learn about it otherwise.


I mostly want to tell people about the stuff I think is cool, and I don’t
really want to make money right now (I have a job for that), so I don’t
usually try to sell them.


Also I found out at the Montreal zine fair that the Quebec national archives
will accept any publication for inclusion in their archives, so I filled out a
form and now my strace zine is part of the national archives of Quebec.


As for shipping things on the internet: the most promising site I’ve found so
far for selling small booklet-y things is
[magcloud.com](http://www.magcloud.com/). I haven’t used them yet so I don’t
know.


### bubblesort zines


I would be remiss not to mention @sailorhg’s amazing [bubblesort zines](https://bubblesort-zines.myshopify.com/pages/about-us) about computer science. she has a bunch of them! go buy them! Here’s how she describes them:


> BubbleSort Zines are a monthly zine series filled with stories and hand-
> drawn art and diagrams. They cover topics like circuits, sorting, memory,
> and tcp. Though the intended audience is high school students (think Hello
> Ruby’s teenage sister), I was surprised by how many adults are also
> subscribers!


### you could make a zine


I think it’s fun because I kind of want to write a book sometimes, but writing
a book takes like a YEAR or MORE and is a huge commitment. Writing a zine is a
lot easier and lower stakes and I get some of the fun rewards (“hey look at
this cool thing I made!”) without spending months editing a book.
