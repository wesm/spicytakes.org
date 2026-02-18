---
title: "Day 42: Writing a Go program to manage Firecracker VMs"
date: 2021-01-20
url: https://jvns.ca/blog/2021/01/20/day-42--writing-a-go-program-to-manage-firecracker-vms/
slug: day-42--writing-a-go-program-to-manage-firecracker-vms
word_count: 748
---


Hello! On Tuesday I spent more time working on figuring out how to run VMs with
Firecracker for my SSH game project. They still start super fast and I’m really
excited about them.


I got through 3 main things:

- learned 1 new thing about how linux bridges work
- figured out how to make my Ubuntu VMs boot fast
- wrote a small Go server to manage Firecracker VMs


### a linux bridge isn’t just a bridge


Every single time I say I’m confused about bridges someone will tell me “well,
you see julia, a bridge is like a virtual switch”. This has never made any sense to me
because I’ve never used a switch either, and also I felt like there was just
something off about that explanation and that it didn’t explain the behavior I
was seeing in a way I couldn’t articulate.


I think I finally learned something concrete about why bridges are confusing
though! On Linux, when you create a bridge you get an network interface (like
`docker0` for the Docker bridge). And that network interface has an ip address,
and you can use that network interface/ip address as a gateway for
containers/VMs you’re running.


But switches don’t have IP addresses! So if “a bridge is like a switch”, what’s
going on? A bridge doesn’t really seems like it’s a switch! This analogy really
seems to be breaking down. Someone on Twitter finally explained yesterday to me
that when you create a bridge on Linux by default, you actually get 2 things:

1. a bridge (the kind that’s “like a switch”, that doesn’t have an ip address and just forwards packets blindly)
2. a network interface with the same name as the bridge, which has an IP address that you can use as a gateway.


They said that if you want, you can delete the network interface part of the
bridge. I still haven’t experimented enough to work this out but I feel really
good about this piece of information and like I can use it to properly
understand what a Linux bridge is later.


Also I feel kind of vindicated in disbelieving this “a bridge is like a switch”
explanation because I guess it’s technically true but it’s definitely missing a
key piece of information for Linux bridges.


### fixed my Ubuntu VMs taking 2 minutes to boot


My Ubuntu Firecracker VMs had been taking 2-3 minutes to boot. They were
hanging on a systemd step called “Load/Save Random Seed”, which apparently has
something to do with kernel entropy.


I googled this and tried a lot of different things to fix it. Here are all the
things that I tried that did not work:

1. add random.trust_cpu=on  to kernel boot args
2. set SYSTEMD_RANDOM_SEED_CREDIT=true in systemd-random-seed.service
3. set SYSTEMD_RANDOM_SEED_CREDIT=force in systemd-random-seed.service
4. install & enable haveged
5. install rng-tools
6. systemctl disable systemd-random-seed (though this really SHOULD have worked, I think I did something wrong there)


Finally I changed the timeout in the systemd-random-service file to 2 seconds,
which worked! Now my VMs start fast. It’s extremely possible that I actually
need this entropy generation for some reason (maybe to give `sshd` enough
entropy so that it can generate session keys securely?) but I’ll cross that
bridge when I come to it.


So now I can start an Ubuntu virtual machine in like 5 seconds! It’s really
amazing. It’s probably possible to bring the boot time a bit more but I’m happy
with that.


### wrote a Go program to manage Firecracker VMs


So far I’ve been starting VMs with the DigitalOcean API. So I wanted to write
my own little API to create Firecracker VMs. It was pretty straightforward
because I mostly just copied a bunch of code from this Firecracker command line
tool called firectl:
[https://github.com/firecracker-microvm/firectl](https://github.com/firecracker-microvm/firectl)


Here’s a gist with my (pretty messy) code so far: [firecracker-manager.go](https://gist.github.com/jvns/bb0a93e3b84a5e8344c6b24b57b2b490).


### what my API looks like so far


It totally works! I can start a VM with:


```
echo '{
    "root_image_path":  "/images/ubuntu.ext4",
    "kernel_path":    "/images/vmlinux"
}' | http post http://localhost:8080/create

```


and I can stop it with:


```
echo '{"id": "DE52E8A0-C624-18CB-F948-0B50C77C8F4A"}'  | http post localhost:8080/delete

```


It’s still missing some things, like:

- I should probably use the firecracker jailer for better security (like firectl does)
- right now I’m still writing the VM’s serial output to stdout
- I might make it REST-y and use a DELETE request to stop a VM


and probably lots more things I’m not thinking of right now
