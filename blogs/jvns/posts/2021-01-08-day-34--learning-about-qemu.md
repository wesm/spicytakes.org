---
title: "Day 34: Learning about qemu"
date: 2021-01-08
url: https://jvns.ca/blog/2021/01/08/day-34--learning-about-qemu/
slug: day-34--learning-about-qemu
word_count: 943
---


On Thursday, I spent basically the whole day being confused about qemu.


### the goal: automatically test my `cloud-init.yaml` files


Right now I have these cloud-init.yaml files that I’m using to provision VMs,
and I got tired of spinning up DigitalOcean VMs and manually SSHing into them
to test things out.


So I figured: I can instead provision the VMs on my own computer!


### qemu is like ffmpeg


In RC daily checkins, I said that I was working on this and Alex mentioned that
he prefers qemu to virtualbox. I’ve never quite understood qemu, so I chatted
with him a bit about why he likes it and it was super helpful.


It seems that one of the main problems with Virtualbox is that it doesn’t have a command
line, so to use it you basically have to use it through something like Vagrant
(or by clicking things in a GUI). Also apparently Oracle doesn’t really
maintain it.


`qemu` is a command line tool in a similar style to ffmpeg, with a million
command line arguments that you can use to accomplish literally anything (which
means it’s very nontrivial to learn and is also an incredible tool).


The reason qemu is like ffmpeg is that they’re by the same person, Fabrice Bellard.


I also learned about
[ffmprovisor](https://amiaopensource.github.io/ffmprovisr/) (a list of FFmpeg
recipes) from Alex, which I’m definitely going to use the next time I need to
use ffmpeg.


Here are some of the ways I failed to get qemu to work, and what worked


### failure 1: google how to use cloud-init with qemu


I searched for something like “how to set up cloud-init with qemu” and found a
bunch of articles that explained how to set up a VM and run `cloud-init` with
qemu using a tool called `virt-install`.


Here’s what I know about `virt-install`:

1. it’s part of of a package called `libvirt`
2. `libvirt` is some sort of abstraction over qemu and other virtualization providers
3. I can’t get it to work


I spent a bunch of time trying to get various things using `virt-install` to
work – I added myself to the `libvirt` group, installed some more packages,
tried some random commands related to bridges that I found on the internet to
get the networking to work, and got very frustrated eventually gave up.


### failure 2: try to use Vagrant to set up a libvirt VM with cloud-init


Then I thought, ok, maybe I can use Vagrant! Vagrant has a `libvirt` backend
that you can use to run KVM virtual machines, and also Vagrant has some
experimental cloud-init support.


The main thing I learned is that you need to enable this
`VAGRANT_EXPERIMENTAL="cloud_init,disks"` environment variable to make this
work, but after I did that it I still couldn’t get it work.


There’s probably some way to get this to work but I didn’t find the
“experimental” state reassuring so I moved on.


### success: using qemu directly


I then decided to use the `qemu` command line directly.


I stumbled on this [getting started with qemu](https://drewdevault.com/2018/09/10/Getting-started-with-qemu.html) blog
post, which has some very unnecessary hostile language about how people who use
VirtualBox make “poor life choices and are an embarrassment to us all”, but you
take what you can get and it was the first thing I could get to work, which was
great! And it was really simple.


After looking some more and asking questions in RC internal chat, I got qemu to
do what I wanted!


### how to start an Ubuntu image with cloud-init and qemu


Here’s exactly how I ended up using qemu to start an Ubuntu image that runs
cloud-init, if anyone is Googling this in the future. I ran this exact script
and it worked for me.


```
# 1. Download a Focal image from Ubuntu's website
wget https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img
# 2. Create user-data and meta-data files
echo "#cloud-config
password: banana
chpasswd: { expire: False }
ssh_pwauth: True
write_files:
- content: "hello world!"
  path: /hello.txt
" > user-data.yaml
echo "instance-id: $(uuidgen || echo i-abcdefg)" > meta-data.yaml
# 3. Package the user-data and meta-data files into a drive image
cloud-localds meta-data.img  user-data.yaml meta-data.yaml
# 4. Create a qcow2 snapshot of the Focal image
qemu-img create -b focal-server-cloudimg-amd64.img -f qcow2 -F qcow2 snapshot.qcow2
# 5. Start qemu!
qemu-system-x86_64 --enable-kvm -m 2048 \
    -drive file=snapshot.qcow2,format=qcow2 \
    -drive file=meta-data.img,format=raw \
    -net user,hostfwd=tcp::2222-:22 -net nic

```


I needed to wait a minute for the machine to boot, and once it was done, I ran:


```
ssh -p 2222 ubuntu@localhost

```


It asked for the password (“banana”), and I was in a VM with the `/hello.txt`
file that I created in my `user-data.yaml` file! Hooray!


```
ubuntu@ubuntu:~$ cat /hello.txt 
hello world!

```


This felt way simpler to me than all `virt-install` examples I found.


Obviously it’s better to use ssh key authentication but I used a password in
this example just so that I could put the whole thing in a self-contained shell
script.


### things I still don’t understand


some questions I still have:

- what the two `-drive` options to qemu do – is the idea that cloud-init reads
from another “hard drive”?
- does the disk image with the metadata and userdata files have a filesystem?
what filesystem?
- how exactly is my qcow2 “snapshot” of the Focal image is only 11MB? I expected
the snapshot to make a copy of the data and be like 500MB. Obviously that’s
not true so I guess there’s a symlink or something but I’m still a bit
confused about this qcow2 format.


### that’s all!


Today I’m going to try to use my newfound qemu powers to automate testing my
cloud-init files!
