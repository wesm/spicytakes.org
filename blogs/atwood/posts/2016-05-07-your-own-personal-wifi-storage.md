---
title: "Your Own Personal WiFi Storage"
date: 2016-05-07
url: https://blog.codinghorror.com/your-own-personal-wifi-storage/
slug: your-own-personal-wifi-storage
word_count: 1471
---

Our kids have reached the age – at ages 4, 4, and 7 respectively – that taking longer trips with them is now possible without everyone losing what’s left of their sanity in the process. But we still have the same problem on multiple hour trips, whether it’s in a car, or on a plane – how do we bring enough stuff to keep the kids entertained without carting 5 pounds of books and equipment along, per person? And if we agree, like most parents, that the iPad is the general answer to this question, how do I get enough local media downloaded and installed on each of their iPads before the trip starts? And do I need 128GB iPads, because those are kind of expensive?


We clearly have a media sharing problem. I asked on Twitter and quite a number of people recommended the HooToo HT-TM05 TripMate Titan at $40. I took their advice, and they were right – **this little device is amazing!**


![](https://blog.codinghorror.com/content/images/2025/02/image-71.png)

- 10400mAh External Battery
- WiFi USB 3.0 media sharing device
- Wired-to-WiFi converter
- WiFi-to-WiFi bridge to share a single paid connection


The value of the last two points is debatable depending on your situation, but the utility of the first two is *huge!* Plus the large built in battery means it can act as a self-powered WiFi hotspot for 10+ hours. All this for only forty bucks!


It’s a very simple device. It has exactly **one button** on the top:

- Hold the button down for 5+ seconds to power on or off.
- Tap the button to see the current battery level, represented as 1-4 white LEDs.
- The blue LED will change to green if connected to another WiFi or wired network.


Once you get yours, just hold down the button to power it on, let it fully boot, and connect to the new `TripMateSith` WiFi network. As to why it’s called that, I suspect it has to do with the color scheme of the device and this guy.


![](https://blog.codinghorror.com/content/images/2016/05/darth-maul.jpg)


I am guessing licensing issues forced them to pick the ‘real’ name of TripMate Titan, but wirelessly, it’s known as `TripMateSith-XXXX`. Connect to that. The default password is `11111111` (that’s eight ones).


![](https://blog.codinghorror.com/content/images/2016/05/wifi-browser-hootoo-titan.png)


Once connected, navigate to `10.10.10.254` in your browser. Username is `admin`, no password.


![](https://blog.codinghorror.com/content/images/2016/05/hootoo-initial-connect.png)


This interface is totally smartphone compatible, for the record, but I recommend you do this from a desktop or laptop since we need to upgrade the firmware immediately. As received, the device has firmware 2.000.022 and you’ll definitely want to upgrade to the latest firmware right away:

- Make sure a small USB storage device is attached – it needs local scratch disk space to upgrade.
- You’d think putting the firmware on a USB storage device and inserting said USB storage device into the HooToo would work, and I agree that’s logical, but… you’d be wrong.
- Connect from a laptop or desktop, then visit the Settings, Firmware page and upload the firmware file from there. (I couldn’t figure out any way to upgrade firmware from a phone, at least not on iOS.)


#### Storage


For this particular use, so we can attach the storage, leave it attached forever, and kinda-sorta pretend it is all one device, I recommend a tiny $32 [128GB USB 3.0 drive](http://www.amazon.com/dp/B01BGTG2A0/). It’s not a barn-burner, but it’s fast enough for its diminutive size.


![](https://blog.codinghorror.com/content/images/2025/02/image-72.png)


In the past, I’ve recommended [very fast USB 3.0 drives](https://blog.codinghorror.com/a-ssd-in-your-pocket/), but I think that time is coming to an end. If you need something larger than 128GB, you could carry a USB 3.0 enclosure with a traditional inexpensive 2.5″ HD, but the combination of travel and spinning hard drives makes me nervous. Not to mention the extra power consumption. Instead, I recommend one of the new, budget compact M.2 SSDs in a USB 3.0 enclosure:

- [500GB M.2 2280 SATA SSD](http://www.amazon.com/dp/B00TGIW1XG/) ($150)
- [M.2 SATA to USB 3.0 Enclosure](http://www.amazon.com/dp/B019NNEA2I/) ($23)


![](https://blog.codinghorror.com/content/images/2025/02/image-73.png)


They run absolute *circles* around large USB flash drives in performance! The larger the drive, believe me, the more you need to care about this, like say you need to quickly copy a bunch of reasonably new media for the kids to enjoy before you go catch that plane.


Anyway, once you get this storage plugged into the HooToo it will automatically **set up a DLNA share** for you:


![](https://blog.codinghorror.com/content/images/2017/01/hootoo-auto-dlna-share.jpg)


However, you must explicitly move the files and folders into the Share folder created by the HooToo to browse them via DLNA.


In theory you could do this directly to the filesystem on the USB drive, but since we’re already *there*, I found it was just as easy to use the built in Explorer tool in the web browser, linked from the HooToo homepage:


![](https://blog.codinghorror.com/content/images/2017/01/hootoo-add-dlna-share-folders-1.jpg)

- Select the files and folders you want to move
- Tap the wrench icon, then Cut
- Tap to enter the Share folder
- Tap the wrench icon, then Paste


Anyway, once you get the folders and files you want into the **Share** folder, you’re good to go for DLNA!


#### Settings and WiFi


Let’s continue setting up our HooToo Tripmate Titan. In the web interface, under Settings, Network Settings, these are the essentials:

- In Host Name, first **set the device name to something short and friendly**. You will be typing this later on every device you attach to it. I used `van` and `airplane` for mine, since that’s where we plan to use them.
- In Wi-Fi and LAN


There’s more here, if you want to bridge wired or wirelessly, but this will get you started.


#### iOS


Update: since I originally wrote this, I’ve switched to [the Infuse app](https://firecore.com/infuse). It’s fantastic for media consumption, and although it is a little expensive at $9, there’s a reason: it supports *tons* of different audio and file formats, including the ones that your iPhone and iPad don’t understand, including Dolby and so on.


Infuse supports the [DLNA standard](http://www.techhive.com/article/2020825/how-to-get-started-with-dlna.html) built into the HooToo. So all you have to do is connect to the HooToo’s wireless network, press the add files plus button at upper right, and connect to the one that automatically appears — in this case, **DLNA-Van**, there at the bottom.


![](https://blog.codinghorror.com/content/images/2017/01/infuse-add-files-dlna-hootoo.png)


With DLNA, **no login is required!** Once connected, you can scan through videos easily, with rather nice thumbnail and summary support.


![](https://blog.codinghorror.com/content/images/2017/01/infuse-dlna-browse-videos-hootoo.jpg)


For more than just media, you can also use the [File Explorer app](https://itunes.apple.com/us/app/fileexplorer/id499470113?mt=8) for iOS (or similar). See the instructions below for Windows, as the process is very similar.


#### Windows / Mac


Connect to the HooToo’s WiFi network, then type in the name of the device (mine’s called `van`) in Explorer or the File Run dialog, prefixed by `\\`.


![](https://blog.codinghorror.com/content/images/2016/05/Screenshot--17-.png)


The default user accounts are `admin` and `guest` with no passwords, unless you set one up. Admin lets you write files; guest does not.


![](https://blog.codinghorror.com/content/images/2016/05/Screenshot--18-.png)


Once you connect you’ll see the default file share for the USB device and can begin browsing the files at `UsbDisk1_Volume1`.


![](https://blog.codinghorror.com/content/images/2016/05/Screenshot--19-.png)


I also figured out how to browse the HooToo filesystem from a Mac as well:

- Connect to the HooToo’s WiFi network
- Open a Finder Window
- On the “Go” menu select “Connect to Server...”
- Enter the HooToo device name, e.g. `van`
- When prompted enter admin or guest credentials


#### Caveats


For some reason, with a USB 3.0 flash drive attached, the battery slowly drains even when powered off. So you’ll want to remove any flash drive when the HooToo is powered off for extended periods. I have no idea why this happens, but I was definitely able to reproduce the behavior. Kind of annoying since my whole goal was to have “one” device, but oh well.


This isn’t a fancy, glitzy [Plex based system](http://www.howtogeek.com/252261/how-to-set-up-plex-and-watch-your-movies-on-any-device/), it’s a basic DLNA share. Devices that have previously connected to this WiFi network will definitely connect to it when no other WiFi networks are available, like say, when you’re in a van driving to Legoland, or on a plane flying to visit your grandparents. You will still have to train people to launch the Infuse app, and the right device name to look for...


![](https://blog.codinghorror.com/content/images/2017/01/infuse-dlna-select-server.jpg)


...or, if you’re on a desktop / laptop, create a desktop link to the proper share.


But in my book, simple is good. The HooToo HT-TM05 TripMate plus a [small 128GB flash drive](http://www.amazon.com/dp/B01BGTG2A0/) is an easy, flexible way to wirelessly share large media files across a ton of devices for less than 75 bucks total, and it comes with a large, convenient rechargeable battery.


I think one of these will live, with its charger cable and a flash drive chock full of awesome media, permanently inside our van for the kids. Remember, **no matter where you go, there your… files… are.**

[wifi storage](https://blog.codinghorror.com/tag/wifi-storage/)
[media sharing](https://blog.codinghorror.com/tag/media-sharing/)
[portable devices](https://blog.codinghorror.com/tag/portable-devices/)
[travel gadgets](https://blog.codinghorror.com/tag/travel-gadgets/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
