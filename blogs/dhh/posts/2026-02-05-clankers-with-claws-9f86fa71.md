---
title: "Clankers with claws"
date: 2026-02-05
url: https://world.hey.com/dhh/clankers-with-claws-9f86fa71
slug: clankers-with-claws-9f86fa71
word_count: 508
---

With
[OpenClaw](https://openclaw.ai/)
you're giving AI its own machine, long-term memory, reminders, and persistent execution. The model is no longer confined to a prompt-response cycle, but able to check its own email, Basecamp notifications, and whatever else you give it access to on a running basis. It's a sneak peek at a future where everyone has a personal agent assistant, and it's fascinating.
I set up mine on a
[Proxmox](https://www.proxmox.com/en/)
virtual machine to be fully isolated from my personal data and logins. (But there are people out there running wild and giving OpenClaw access to everything on their own machine, despite the repeated warnings that this is more than a little risky!).
Then I tried to see just how little help it would need navigating our human-centric digital world. I didn't install any
[skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
, any
[MCPs](https://modelcontextprotocol.io/docs/getting-started/intro)
, or give it access to any APIs. Zero machine accommodations. I just started off with a simple prompt: "Sign up for Fizzy, so we have a place to collaborate. Here's the invite link."
Kef, as I named my new agent, dutifully went to
[Fizzy](https://fizzy.do/)
to sign up, but was immediately stumped by needing an email address. It asked me what to do, and I replied: "Just go to
[hey.com](https://www.hey.com/)
and sign up for a new account." So it did. In a single try. No errors, no steering, no accommodations.
After it had procured its own email address, it continued on with the task of signing up for Fizzy. And again, it completed the mission without any complications. Now we had a shared space to collaborate.
So, as a test, I asked it to create a new board for business ideas, and add five cards with short suggestions, including providing a background image sourced from the web to describe the idea. And it did. Again, zero corrections. Perfect execution.
I then invited it to
[Basecamp](https://basecamp.com/)
by just adding it as I would any other user. That sent off an email to Kef's new HEY account, which it quickly received, then followed the instructions, got signed up, and greeted everyone in the chat room of the AI Labs project it was invited to.

![image.png](https://world.hey.com/dhh/9f86fa71/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjQ0MDI4ODUyMSwicHVyIjoiYmxvYl9pZCJ9fQ--09074eb1dc1238265386e0a92143ea009f4e13cf31ab9eb6a5dfb15466aedd45/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/image.png)

I'm thoroughly impressed. All the agent accommodations, like MCPs/CLIs/APIs, probably still have a place for a bit longer, as doing all this work cold is both a bit slow and token-intensive. But I bet this is just a temporary crutch.
And while I ran this initial experiment on Claude's Opus 4.5, I later reran most of it on the Chinese open-weight model
[Kimi K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)
, and it too was able to get it all right (though it was a fair bit slower when provisioned through OpenRouter).
Everything is changing so fast in the world of AI right now, but if I was going to skate to where the puck is going to be, it'd be a world where agents, like self-driving cars, don't need special equipment, like
[LIDAR](https://www.thedrive.com/news/volvo-has-dropped-luminar-and-lidar-for-2026-models)
or MCPs, to interact with the environment. The human affordances will be more than adequate.
What a time to be alive.
