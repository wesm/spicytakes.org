---
title: "[VIDEO] Arch Linux with full disk encryption in (about) 15 minutes"
date: 2016-08-18
url: https://drewdevault.com/2016/08/18/Arch-Linux-with-full-disk-encryption-in-15-minutes.html
slug: Arch-Linux-with-full-disk-encryption-in-15-minutes
word_count: 389
---

After my  [blog post](/2016/06/29/Privacy-as-a-hobby.html)  emphasizing the
importance of taking control of your privacy, I’ve decided to make a few more
posts going over detailed instructions on how to actually do so. Today we have a
video that goes over the process of installing Arch Linux with full disk
encryption.

This is my first go at publishing videos on my blog, so please provide some
feedback in the comments of this article. I’d prefer to use my blog instead of
YouTube for publishing technical videos, since it’s all open source, ad-free,
and DRM-free. Let me know if you’d like to see more content like this on my
blog and which topics you’d like covered - I intend to at least release another
video going over this process for Ubuntu as well.

[Download video (WEBM)](https://sr.ht/archlinux.webm)

The video goes into detail on each of these steps, but here’s the high level
overview of how to do this. Always check the latest version of the  [Install
Guide](https://wiki.archlinux.org/index.php/Installation_guide)  and the
 [dm-crypt](https://wiki.archlinux.org/index.php/Dm-crypt)  page on the Arch Wiki
for the latest procedure.

1. Partition your disks with gdisk and be sure to set aside a partition for
/boot
2. Create a filesystem on /boot
3. (optional) Securely erase all of the existing data on your disks with  `dd if=/dev/zero of=/dev/sdXY bs=4096`  -  *note: this is a correction from the
command mentioned in the video*
4. Set up encryption for your encrypted partitions with  `cryptsetup luksFormat /dev/sdXX`
5. Open the encrypted volumes with  `cryptsetup open /dev/sdXX [name]`
6. Create filesystems on /dev/mapper/[names]
7. Mount all of the filesystems on /mnt
8. Perform the base install with  `pacstrap /mnt base [extra packages...]`
9. `genfstab -p /mnt >> /mnt/etc/fstab`
10. `arch-chroot /mnt /usr/bin/bash`
11. `ln -s /usr/share/zoneinfo/[region]/[zone] /etc/localtime`
12. `hwclock --systohc --utc`
13. Edit /etc/locale.gen to your liking and run  `locale-gen`
14. `locale > /etc/locale.conf`  - note this only works for en_US users, adjust if
necessary
15. Edit /etc/hostname to your liking
16. Reconfigure the network
17. Edit /etc/mkinitcpio.conf and ensure that the  `keyboard`  and  `encrypt`  hooks
run before the  `filesystems`  hook
18. `mkinitcpio -p linux`
19. Set the root password with  `passwd`
20. Configure /etc/crypttab with any non-root encrypted disks you need. You can
get partition UUIDs with  `ls -l /dev/disk/by-partuuid`
21. Configure your kernel command line to include
 `cryptdevice=PARTUUID=[...]:[name] root=/dev/mapper/[name] rw`
22. Install your bootloader and reboot!
