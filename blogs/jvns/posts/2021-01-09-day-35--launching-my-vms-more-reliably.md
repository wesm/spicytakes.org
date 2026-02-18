---
title: "Day 35: Launching my VMs more reliably"
date: 2021-01-09
url: https://jvns.ca/blog/2021/01/09/day-35--launching-my-vms-more-reliably/
slug: day-35--launching-my-vms-more-reliably
word_count: 768
---


I’ve been having a problem for a while where my virtual machines (that I use to
set up the puzzles) don’t launch reliably – sometimes they work, and sometimes
they don’t.


I didn’t understand why this was before, and on Friday I think I figured it out!


### what was going wrong


When I started a puzzle, I’d:

- launch a VM (by giving `cloud-init` a `cloud-init.yaml` file), which would set up all the right files and run some commands
- wait until SSH was up
- ssh into the VM and run a script called `setup/run.sh`
- done!


I don’t know why it took me so long to remember this, but – just because
`ssh` is running, it doesn’t mean that the `cloud-init` is done running! So if I
`ssh` into the instance as soon as SSH is up, my setup script might not have
everything it needs to run.


I also found [this launchpad bug](https://bugs.launchpad.net/ubuntu/+source/cloud-init/+bug/1633453)
suggesting that at some point in the past cloud-init only brought up SSH when
it was finished running, but that that doesn’t happen anymore.


### solution: wait until `cloud-init` is done running


`cloud-init` makes this pretty easy: it creates a file at `/var/lib/cloud/data/result.json` when it’s done running.


I also made my puzzle setup code run as part of `cloud-init` (in the
`scripts/per-boot` stage), so I don’t need to do an extra SSH to run the last
stage of setup.


So now instead I’m doing:

- launch a VM (by giving `cloud-init` a `cloud-init.yaml` file)
- wait until SSH is up
- wait until the `result.json` file is present
- make sure that `cloud-init` succeeded
- done!


I’m not sure that this will solve all my problems, but it’s helped already and it’s a much better plan.


### how to make SSH ignore `.ssh/known_hosts`


Right now I’m testing my `cloud-init.yaml` files by spinning up a bunch of VMs
on my laptop with `qemu`. I had a problem where every instance had a different
randomly generated SSH key, so SSH was giving me these giant warnings about the
key for `ubuntu@localhost:2222` changing. These warnings were annoying me (and
providing no value in this case) so I wanted them to go away.


At first I tried to solve this with `ssh -o StrictHostKeyChecking=no` but,
while this let me SSH without typing “yes” to the prompt warning me about the
change in keys, it still displayed the warning.


I found out that I can do `ssh -o UserKnownHostsFile=/dev/null` instead, which
ignores my usual `.ssh/known_hosts` file.


### a script to run my `cloud-init` files locally with qemu


I also wrote a script to run my `cloud-init` files locally!


Here it is. Now I can just run `./scripts/start-vm PUZZLE-NAME` to start the VM
for a given puzzle. It takes about a minute to boot a VM and it made it WAY WAY
WAY faster to iterate on changes.


I’ve gotten a bit better at bash recently by writing the bash zine and I used
some of my newfound bash knowledge here (like using `trap` to kill the qemu
process when the script exits,  writing while loops, and `$(())` for
arithmetic.). I felt like this was a nice example of a good place for a bash script because:

- the logic is very simple (there’s just 1 while loop and a `trap`)
- it needs to run a bunch of processes (so bash is the right language)
- I’m the only person using it


```
#!/bin/bash
set -e
# kill qemu on exit
trap 'set -e; kill $(jobs -p)' exit

CLOUD_INIT_FILE=$(find . -path "*$1*cloud-init.yaml")
[ -f $CLOUD_INIT_FILE ] || exit

echo "instance-id: $(uuidgen || echo i-abcdefg)" > my-meta-data

IMG=/tmp/my-seed.img
FOCAL=/home/bork/work/images/focal-server-cloudimg-amd64.img
SNAPSHOT=/tmp/snapshot.qcow2
qemu-img create -b $FOCAL -f qcow2 -F qcow2 $SNAPSHOT

cloud-localds $IMG $CLOUD_INIT_FILE my-meta-data

qemu-system-x86_64 --enable-kvm -m 1024 \
    -drive file=$SNAPSHOT,format=qcow2 \
    -drive file=$IMG,format=raw \
    -net user,hostfwd=tcp::2222-:22 -net nic \
    -nographic > out 2>out &

SSH_OPTIONS="-p 2222 -i wizard.key -o UserKnownHostsFile=/dev/null -o ConnectTimeout=1 -o StrictHostKeyChecking=no"

start=$SECONDS
while ! ssh $SSH_OPTIONS wizard@localhost 'python3 /usr/local/bin/started_up'
do
    duration=$(( SECONDS - start ))
    echo "waiting for ssh.. $duration"
    sleep 1
done
# we're done! SSH into the VM.
ssh $SSH_OPTIONS wizard@localhost

```


### next up: see if it’s actually more reliable!


I’ve done a lot of testing locally and this setup seems more reliable, but I
still haven’t implemented it in production. My guess is that there are still a
few other problems I’ll need to work out.


Booting a VM is also still pretty slow – it takes almost 2 minutes sometimes!
Kamal suggested using `kexec` and I still haven’t fully understood what that is
or how I could use it.
