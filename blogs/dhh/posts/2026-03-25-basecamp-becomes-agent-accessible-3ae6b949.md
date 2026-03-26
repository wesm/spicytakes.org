---
title: "Basecamp becomes agent accessible"
date: 2026-03-25
url: https://world.hey.com/dhh/basecamp-becomes-agent-accessible-3ae6b949
slug: basecamp-becomes-agent-accessible-3ae6b949
word_count: 440
---

In the past 18 months, we've experimented with a ton of AI-infused features at 37signals.
[Fizzy](https://fizzy.do/)
had all sorts of attempts. As did Basecamp. But
[as Microsoft](https://blogs.windows.com/windows-insider/2026/03/20/our-commitment-to-windows-quality/)
and many others have realized, it's not that easy to make something that's actually
*good*
and would welcomed by users. So we didn't ship.
In the meantime, agents have emerged has the killer app for AI. Not only are LLMs much smarter when they can check their thinking using tools, but the file system also gives them the memory implant they needed to learn between prompts. And now they can actually do stuff!
So while we keep cooking on actually-useful native AI features in
[Basecamp](https://basecamp.com/)
, we're
[launching a fully agent-accessible version today](https://basecamp.com/agents)
. We've
[revamped our API](https://github.com/basecamp/bc3-api)
, created
[a brand-new CLI](https://github.com/basecamp/basecamp-cli)
, and wrapped it all in
[a skill](https://github.com/basecamp/basecamp-cli/blob/main/skills/basecamp/SKILL.md)
to teach agents how best to use it all. It works remarkably well, and it's really fast too.
Not only can you have your agent look through everything in Basecamp, summarize whatever you need, but it can also set up to-do lists, post message updates, chat with humans and clankers alike, upload reference files, and arrange a project schedule. Anything you can do in Basecamp, agents can now do too.
This becomes extra powerful when you combine Basecamp with all the other tools you might be using that are also agent accessible. For software development, you can use the MCP from Sentry to trawl through major sources of bugs, then have the agent summarize that in a message for Basecamp. Or you have it download, analyze, and highlight key customer complaints by giving it access to your help desk system.
All this was possible in the past with APIs, hand-written integrations, and human data scientists. But it was cumbersome, slow, and expensive, so most people just didn't. A vanishingly small portion of Basecamp customers have ever directly interacted with our API. But agents? I think adoption is going to be swift.
Not because everyone is going to run
[OpenCode](https://opencode.ai/)
, Claude Code, or Gemini CLI. But because agents are going to be incorporated into ChatGPT, Gemini, Grok, and all the other mainstream interfaces who were collectively embarrassed by OpenClaw's meteoric ascent  and popularity very quickly. There's a huge demand out there for a personal agent that can act as your private executive assistant.
This is where the puck is going, and we're skating to meet it with agent accessibility across the board. Basecamp is first, Fizzy is next, and we'll hit HEY before long too. Revamped APIs, comprehensive CLIs, and the skills to use them whatever your harness or claws look like.
