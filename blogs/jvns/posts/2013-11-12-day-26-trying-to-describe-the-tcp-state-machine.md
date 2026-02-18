---
title: "Day 26: Trying to describe the TCP state machine in a readable way. Failing."
date: 2013-11-12
url: https://jvns.ca/blog/2013/11/12/day-26-trying-to-describe-the-tcp-state-machine/
slug: day-26-trying-to-describe-the-tcp-state-machine
word_count: 554
---


Today I made a bunch of progress (I can now be a TCP server, kinda!), but I want to
talk about problems instead.


The main function right now in this TCP stack is called `handle()`, and
it’s responsible for moving from one part of the
[state machine](http://www.tcpipguide.com/free/t_TCPOperationalOverviewandtheTCPFiniteStateMachineF-2.htm)
to another.


In particular, it has to

- Drop inappropriate packets
- Increment the current ACK number
- Make state transitions
- Send out ACKs and SYNs and FINs and FIN-ACKs when appropriate


It is kind of a mess and I am finding it pretty hard to reason about and
test.


Yesterday it looked like this:


```
def handle(self, packet):
    # Update our state to indicate that we've received the packet
    self.ack = max(self.next_seq(packet), self.ack)
    if hasattr(packet, 'load'):
        self.recv_buffer += packet.load

    recv_flags = packet.sprintf("%TCP.flags%")
    send_flags = ""

    # Handle all the cases for self.state explicitly
    if self.state == "ESTABLISHED" and 'F' in recv_flags:
        send_flags = "F"
        self.state = "TIME-WAIT"
    elif self.state == "ESTABLISHED":
        pass
    elif self.state == "SYN-SENT":
        self.seq += 1
        self.state = "ESTABLISHED"
    elif self.state == "FIN-WAIT-1" and 'F' in recv_flags:
        self.seq += 1
        self.state = "TIME-WAIT"
    else:
        raise BadPacketError("Oh no!")

    self._send_ack(flags=send_flags)

```


In particular, I thought this `_send_ack()` call at the end was a great idea,
because you always want to send an ACK! Except when you don’t!


In fact, I have just remembered that my primary insight from yesterday was that
I always wanted to send an ACK. But it turns out that actually there are a
couple of of cases where you *don’t* want to send an ACK:

- The packet you’re receiving was itself an ACK
- You’ve just received a RST packet and are closing the connection


and then I found the `_send_ack()` call at the bottom confusing, because it
wasn’t clear under what conditions the code actually go there.


So now I have, after some suggestions from Allison:


```
def handle(self, packet):
    if self.last_ack_sent and self.last_ack_sent != packet.seq:
        # We're not in a place to receive this packet. Drop it.
        return

    self.last_ack_sent = max(self.next_seq(packet), self.last_ack_sent)

    recv_flags = packet.sprintf("%TCP.flags%")

    # Handle all the cases for self.state explicitly
    if self._has_load(packet):
        self.recv_buffer += packet.load
        self._send_ack()
    elif "R" in recv_flags:
        self._close()
    elif "S" in recv_flags:
        if self.state == "LISTEN":
            self.state = "SYN-RECEIVED"
            self._set_dest(packet.payload.src, packet.sport)
            self._send_ack(flags="S")
        elif self.state == "SYN-SENT":
            self.seq += 1
            self.state = "ESTABLISHED"
            self._send_ack()
    elif "F" in recv_flags:
        if self.state == "ESTABLISHED":
            self.seq += 1
            self.state = "LAST-ACK"
            self._send_ack(flags="F")
        elif self.state == "FIN-WAIT-1":
            self.seq += 1
            self._send_ack()
            self._close()
    elif "A" in recv_flags:
        if self.state == "SYN-RECEIVED":
            self.state = "ESTABLISHED"
        elif self.state == "LAST-ACK":
            self._close()
    else:
        raise BadPacketError("Oh no!")

```


This solves a bunch more problems than the first function. In particular, it

- Ignores packets with the wrong sequence number
- Updates the `last_ack_sent` with the next sequence number that we’re expecting


**Good things:**

- If I’m in “ESTABLISHED” and get a “FA”, it’s fairly easy to see what’s going to
happen in the giant if statement


**Bad things:**

- The cases aren’t all mutually exclusive, so the order matters. `:[`
- Each one is a seemingly random combination of `self.seq += 1`,
`self._send_ack()`, `self._close()`, and a change to `self.state`. It’s hard to
make sure the whole thing is right without a ton of unit testing.


My confusion about this function largely reflects my confusion about TCP at
this point, I think.
