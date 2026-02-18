---
title: "Custom Music Syncing on Android"
date: 2013-08-24
url: https://drewdevault.com/2013/08/24/Music-syncing-on-Android.html
slug: Music-syncing-on-Android
word_count: 868
---

I have an HTC One, with CyanogenMod installed. I usually use Spotify, but I’ve been wanting to move away from it for a while.
The biggest thing keeping me there was the ease of syncing up with my phone - I added music on my PC and it just showed up
on my phone.

So, I finally decided to make it work on my phone without Spotify. You might have success if you aren’t using CyanogenMod,
but you definitely need to be rooted and you need to access a root shell on your phone. I was using  `adb shell`  to start with,
but it has poor terminal emulation. Instead, I ended up installing an SSH daemon on the phone and just using that. Easier to
use vim in such an enviornment.

The end result is that a cronjob kicks off each hour on my phone and runs a script that uses rsync to sync up my phone’s music
with my desktop’s music. That’s another thing - a prerequisite of this working is that you have to expose your music to the
outside world on an SSH server somewhere.

I’ll tell you how I got it working, then you can see if it works for you. It might take some effort on your part to tweak
these instructions to fit your requirements.

## Sanity checks

Get into your phone’s shell and make sure you have basic things installed. You’ll need to make sure you have:

* bash
* cron
* ssh
* rsync

If you don’t have them, you can probably get them by installing busybox.

## Setting up SSH

We need to generate a key. I tried using ssh-keygen before, but it had problems with rsync on Android. Instead, we use
dropbearkey. Generate your key with  `dropbearkey -t rsa -f /data/.ssh/id_rsa` . You’ll see the public key echoed to stdout.
It’s not saved anywhere for you, so grab it out of your shell and put it somewhere - namely, in the authorized_keys file
on the SSH server you plan to pull music from.

At this point, you can probably SSH into the server you want to pull from. Run  `ssh -i /data/.ssh/id_rsa <your server here>` 
to double check. Note that this isn’t just for fun - you need to do this to get your server into known_hosts, so we can
non-interactively access it.

## Making Android more sane

Now that this is working, we need to clean up a little before cron will run right. Android is only a “Linux” system in the
sense that  `uname`  outputs “Linux”. It grossly ignores the FHS and you need to fix it a little. Figure out how to do a
nice init.d script on your phone. For my CyanogenMod install, I can add scripts to  `/data/local/userlocal.d/`  and they’ll
be run at boot. Here’s my little script for making Android a little more sane:

```
#!/system/bin/sh
# Making /system rw isn't strictly needed
mount -o remount,rw /system
mount -o remount,rw /
ln -s /data/var /var
ln -s /system/bin /bin
ln -s /data/.ssh /.ssh
crond
```

## Update script and initial import

The following is the script we’ll use to update your phone’s music library.

```
#!/system/xbin/bash
# Syncs music between a remote computer and this phone
RHOST=<remote hostname>
EHOST=<fallback, I use this for connecting from outside my LAN>
RPORT=22
RUSER=<username>
ID=/data/.ssh/id_rsa
RPATH=/path/to/your/remote/music
# Omit the final directory. On my setup, this goes to /sdcard/Music, and my remote is /home/sircmpwn/Music
LPATH=/sdcard

echo $(date) >> /var/log/update-music.log

rsync -ruvL --delete --rsh="ssh -p $RPORT -i $ID" $RUSER@$RHOST:$RPATH $LPATH >> /var/log/update-music-rsync-so.log 2>&1
if [[ $? != 0 ]]; then
    rsync -ruvL --delete --rsh="ssh -p $RPORT -i $ID" $RUSER@$EHOST:$RPATH $LPATH >> /var/log/update-music-rsync-so.log 2>&1
fi
```

Save this script to  `/data/updateMusic` , make it executable with  `chmod +x /data/updateMusic` , then run the initial import
with  `/data/updateMusic` . After a while, you’ll have all your computer’s music on your phone. Now, we just need to make it
update automatically.

Note: I set up a couple of logs for you.  `/var/log/update-music.log`  has the timestamp of every time it did an update. Also,
 `/var/log/update-music-rsync-so.log`  has the output of rsync from each run.

## Cron

Finally, we need to set up a cronjob. If you followed the instructions so far (and if you’re lucky), you should have everything
ready for cron. The biggest pain in my ass was getting cron to coorperate, but the init script earlier should take care of
that. Run  `crontab -e`  and write your crontab:

```
0 * * * * /data/updateMusic
```

Nice and simple. Your phone will now sync up your music every hour, on the hour, with your home computer. Here are some
possible points for improvement:

* Check wlan0 and only sync if it’s up
* Log cron somewhere
* Alter the update script to do a little bit better about the “fallback”
* Sync more than just music

After all of this, I now have a nice setup that syncs music to my phone so I can listen to it with Apollo. I might switch
away from Apollo, though, it’s pretty buggy.  [Let me know](mailto:sir@cmpwn.com)  if you can suggest an alternative music
player, or if you get stuck working through this procedure yourself.
