---
title: "Stylesheets for Print and Handheld"
date: 2007-01-30
url: https://blog.codinghorror.com/stylesheets-for-print-and-handheld/
slug: stylesheets-for-print-and-handheld
word_count: 489
---

A commenter recently noted that it was difficult to print the [Programmer’s Bill of Rights post](https://blog.codinghorror.com/the-programmers-bill-of-rights/). And he’s right. It’s high time I set up a print stylesheet for this website. I added the following link tag to the page header:

kg-card-begin: html

<link rel=“stylesheet” href=“[/blog/styles-site-print.css](https://blog.codinghorror.com/blog/styles-site-print.css)”
type=“text/css” media=“print” />


kg-card-end: html
The printer-specific CSS is very simple. On a modern site [using <div> based layout](https://blog.codinghorror.com/the-css-zen-garden-and-asp-net/), optimizing for printers is easy.Hide named <div>s on the page that aren’t relevant to printouts.
kg-card-begin: html


#links {
display: none;
}
#searchbox {
display: none;
}
#newcomment {
display: none;
}


kg-card-end: html
Adjust a few margins and widths, and set a default font.
kg-card-begin: html


body {
margin: 0; padding: 0;
font-family:calibri, tahoma, arial, sans-serif;
}
#content {
width: 100%;
margin: 0; padding: 0;
}
#container {
width: 100%;
position:relative;
margin: 0; padding: 0;
}
.blog {
padding: 0;
}



kg-card-end: html
The entire printer-friendly CSS file is a mere 35 lines including generous whitespace. Testing the print stylesheet is a piece of cake, too. Just use the **File, Print Preview** menu:Looks good to me.Once you’ve set up a print stylesheet, you might as well set up a mobile stylesheet, too, because they’re almost identical. We just add another link tag to the page header:
kg-card-begin: html


<link rel=“stylesheet” href=“[/blog/styles-site-mobile.css](https://blog.codinghorror.com/blog/styles-site-mobile.css)”
type=“text/css” media=“handheld” />


kg-card-end: html
The CSS is a subset of the printer CSS, so I won’t reprint it here. I only hide the links <div>. Testing rendering on a mobile device is a bit more difficult, but it is possible. Here’s what it looks like on the new Samsung Blackjack phones we received at work:If you’re wondering what your website looks like on a mobile device, wonder no longer. Try it yourself and see. **The Windows SmartPhone / PocketPC emulator was surprisingly easy to get up and running**. Here’s what you’ll need:A clean Windows XP SP2 virtual machineThe latest version of [ActiveSync](https://web.archive.org/web/20070202025319/http://www.microsoft.com/windowsmobile/activesync/default.mspx).[Standalone Device Emulator with Windows Mobile OS Images](https://web.archive.org/web/20070216021850/http://www.microsoft.com/downloads/details.aspx?FamilyID=c62d54a5-183a-4a1e-a7e2-cc500ed1f19a&DisplayLang=en) (download both items listed here)[Virtual Machine Network Driver for Microsoft Device Emulator](https://web.archive.org/web/20070211174047/http://www.microsoft.com/downloads/thankyou.aspx?familyId=DC8332D6-565F-4A57-BE8C-1D4718D3AF65&displayLang=en)Once you’ve downloaded it all, install it in this order:Install ActiveSyncUnzip and install V1Emulator (standalone_emulator_V1.exe)Install the Virtual Network Driver (netsvwrap.msi)Install the Emulator Images for Windows Mobile 5.0 (efp.msi)I chose to launch the “Smartphone QVGA - Coldboot” emulator. Once it’s running, the only tricky part is enabling internet connectivity. This post [describes how to enable internet connectivity in the emulator](https://web.archive.org/web/20070202220312/http://blogs.msdn.com/akhune/archive/2005/11/16/493329.aspx); you place the emulated smartphone in the virtual “cradle” so it can access the network through ActiveSync. Note that you’ll also need to set “Allow connections to one of the following” to “DMA” in the File, Connection Settings menu of ActiveSync.Setting up proper print and handheld stylesheets was fun. And easy. I truly regret not doing it sooner. Don’t make the same mistake I did. **If you don’t have print and handheld stylesheets set up on *your* website, what are you waiting for?**

[css](https://blog.codinghorror.com/tag/css/)
[print stylesheet](https://blog.codinghorror.com/tag/print-stylesheet/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[css styling](https://blog.codinghorror.com/tag/css-styling/)
[frontend development](https://blog.codinghorror.com/tag/frontend-development/)
