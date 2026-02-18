---
title: "Day 44: Building my VMs with Docker"
date: 2021-01-22
url: https://jvns.ca/blog/2021/01/22/day-44--got-some-vms-to-start-in-firecracker/
slug: day-44--got-some-vms-to-start-in-firecracker
word_count: 600
---


Another pretty short post today, still in Firecracker land.


### decided to build my VMs with Docker instead of cloud-init


I’ve been trying to figure out how to build my VMs for a while. Previously my
plan was to just run `cloud-init` when the VM started, because I already had
`cloud-init.yaml` files to launch VMs that I’d written previously.


It turned out that for some reason I couldn’t get `cloud-init` to start, and
also it felt like `cloud-init` was going to be really slow to run – even when
it was failing, it was already taking more than 10 seconds. I really wanted the
VM to boot in less than 2 seconds.


So I decided to instead build my containers with Docker, convert the Docker
filesystem to an ext4 image, and then start that image in Firecracker. Here’s
what creating the image looks like in a bash script.


```
IMG_ID=$(docker build -q .)
CONTAINER_ID=$(docker run -td $IMG_ID /bin/bash)
MOUNTDIR=mnt
IMAGE=ubuntu.ext4
mount $IMAGE $MOUNTDIR
qemu-img create -f raw $IMAGE 800M
mkfs.ext4 $IMAGE
docker cp $CONTAINER_ID:/ $MOUNTDIR

```


It seems to work fine, and actually building my VMs with Docker feels a lot
simpler than doing it with `cloud-init.yaml`, I think they might be easier to
develop this way.


### setting up Docker-Compose’s bridges


I kind of want to run my VM management software with `docker-compose`, but it
needs to make changes to the host network to set up the bridges / tap
interfaces.


I learned that Docker Compose by default creates a new bridge for every
`docker-compose` file with a random name.  I didn’t think this was going to
work for me, because I want to put my VMs on the same bridge as the `gotty`
container that needs to SSH into the VMs. So I needed to know the name of the
VM.


It turns out the Docker Compose is AMAZING and lets you explicitly set the name of the bridge for a network


So I set up a network in my `docker-compose.yml` file that looks like this, and
put my `gotty` container in the `firenet` network.


```
version: "3.3"
networks:
  firenet:
    driver: bridge
    ipam:
     driver: default
     config:
       - subnet: 172.101.0.0/16
    driver_opts:
      com.docker.network.bridge.name: firecracker0

```


I still haven’t tested this out because there are some other legos I need to
put together, but I think it should work.


### trying out fly.io


I got a bit frustrated with writing my own Firecracker VM service so later in the day, so I
asked on Twitter if anyone knew of a cloud service where I could run a
Firecracker VM. I was pretty sure the answer was no, but I’m happy I asked
because I was wrong!


It turns out that [https://fly.io](https://fly.io) supports a Docker container interface, but they
actually just unpack the Docker container’s files, convert it into an ext4
filesystem, and boot a Firecracker VM with it. They don’t support you picking
the init system or choosing a kernel and presumably the VMs are kind of locked
down, but it’s not a container!


I’d initially assumed it was a container because Fargate and Kata Containers
both run containers images in VMs by putting a container runtime inside the
Firecracker VM and running the container that way.


I got some VMs to run on fly.io using their Go API after a few hours, so we’ll
see how that goes! I’ll do a few more experiments today. It was pretty
straightforward except that their API isn’t documented yet. But their command
line management tool is open source so I could just read the source for
`flyctl` to figure out how it worked.
