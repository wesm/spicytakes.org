---
title: "The Learning Loop and LLMs"
description: "LLMs are useful because they lower the threshold for   experimentation. But we have to beware that we don't use them to try to   shortcut the learning loop that's an essential part of a software devel"
date: 2025-11-04T00:00:00
tags: ["productivity", "generative ai"]
url: https://martinfowler.com/articles/llm-learning-loop.html
slug: llm-learning-loop
word_count: 1793
---


Software development has always resisted the idea that it can be turned into an
                assembly line. Even as our tools become smarter, faster, and more capable, the
                essential act remains the same: we learn by doing.


An Assembly Line is a poor metaphor for software development


In most mature engineering disciplines, the process is clear: a few experts design
                the system, and less specialized workers execute the plan. This separation between
                design and implementation depends on stable, predictable laws of physics and
                repeatable patterns of construction. Software doesn't work like that. There are
                repetitive parts that can be automated, yes, but the very assumption that design can
                be completed before implementation doesn't work. In software, design emerges through
                implementation. We often need to write code before we can even understand the right
                design. The feedback from code is our primary guide. Much of this cannot be done in
                isolation. Software creation involves constant interaction—between developers,
                product owners, users, and other stakeholders—each bringing their own insights. Our
                processes must reflect this dynamic. The people writing code aren't just
                'implementers'; they are central to discovering the right design.


LLMs are
            reintroducing the assembly line metaphor


Agile practices recognized this over two decades ago, and what we learnt from Agile
                should not be forgotten. Today, with the rise of large language models (LLMs), we're
                once again tempted to see code generation as something done in isolation after the
                design structure is well thought through. But that view ignores the true nature of
                software development.


I learned to use LLMs judiciously as brainstorming partners


I recently developed a framework for building distributed systems—based on the
                patterns I describe in my book. I experimented heavily with LLMs. They helped in
                brainstorming, naming, and generating boilerplate. But just as often, they produced
                code that was subtly wrong or misaligned with the deeper intent. I had to throw away
                large sections and start from scratch. Eventually, I learned to use LLMs more
                judiciously: as brainstorming partners for ideas, not as autonomous builders. That
                experience helped me think through the nature of software development, most
                importantly that writing software is fundamentally an act of learning, 
                and that we cannot escape the need to learn just because we have LLM agents at our disposal.


LLMs lower the threshold for experimentation


Before we can begin any meaningful work, there's one crucial step: getting things
                set-up to get going. Setting up the environment—installing dependencies, choosing
                the right compiler or interpreter, resolving version mismatches, and wiring up
                runtime libraries—is sometimes the most frustrating and necessary first hurdle.
                There's a reason the âHello, Worldâ program is legendary. It's not just tradition;
                it marks the moment when imagination meets execution. That first successful output
                closes the loop—the tools are in place, the system responds, and we can now think
                through code. This setup phase is where LLMs mostly shine. They're incredibly useful
                for helping you overcoming that initial friction—drafting the initial build file, finding the right
                flags, suggesting dependency versions, or generating small snippets to bootstrap a
                project. They remove friction from the starting line and lower the threshold for
                experimentation. But once the âhello worldâ code compiles and runs, the real work begins.


There is a learning loop that is fundamental to our work


As we consider the nature of any work we do, it's clear that continuous learning is
                the engine that drives our work. Regardless of the tools at our disposal—from a
                simple text editor to the most advanced AI—the path to building deep, lasting
                knowledge follows a fundamental, hands-on pattern that cannot be skipped. This
                process can be broken down into a simple, powerful cycle:


Observe and Understand


This is the starting point. You take in new information by watching a tutorial,
                    reading documentation, or studying a piece of existing code. You're building a
                    basic mental map of how something is supposed to work.


Experiment and Try


Next, you must move from passive observation to active participation. You don't
                    just read about a new programming technique; you write the code yourself. You
                    change it, you try to break it, and you see what happens. This is the crucial
                    âhands-onâ phase where abstract ideas start to feel real and concrete in your
                    mind.


Recall and Apply


This is the most important step, where true learning is proven. It's the moment
                    when you face a new challenge and have to actively recall what you learned
                    before and apply it in a different context. It's where you think, âI've seen a
                    problem like this before, I can use that solution here.â This act of retrieving
                    and using your knowledge is what transforms fragmented information into a
                    durable skill.


AI cannot automate learning


This is why tools can't do the learning for you. An AI can generate a perfect
                    solution in seconds, but it cannot give you the experience you gain from the
                    struggle of creating it yourself. The small failures and the âaha!â moments are
                    essential features of learning, not bugs to be automated away.


â£Â Â Â Â Â â£Â Â Â Â Â â£


There Are No Shortcuts to Learning


â£Â Â Â Â Â â£Â Â Â Â Â â£


Everybody has a unique way of navigating the learning cycle


This learning cycle is unique to each person. It's a continuous loop of trying things,
                    seeing what works, and adjusting based on feedback. Some methods will click for
                    you, and others won't. True expertise is built by finding what works for you
                    through this constant adaptation, making your skills genuinely your own.


Agile methodologies understand the importance of learning


This fundamental nature of learning and its importance in the work we do is
                precisely why the most effective software development methodologies have evolved the
                way they have. We talk about Iterations, pair programming, standup meetings,
                retrospectives, TDD, continuous integration, continuous delivery, and 'DevOps' not
                just because we are from the Agile camp. It's because these techniques acknowledge
                this fundamental nature of learning and its importance in the work we do.


The need to learn is why high-level code reuse has been elusive


Conversely, this role of continuous learning in our professional work, explains one
                of the most persistent challenges in software development: the limited success of
                high-level code reuse. The fundamental need for contextual learning is precisely why
                the long-sought-after goal of high-level code âreuseâ has remained elusive. Its
                success is largely limited to technical libraries and frameworks (like data
                structures or web clients) that solve well-defined, universal problems. Beyond this
                level, reuse falters because most software challenges are deeply embedded in a
                unique business context that must be learned and internalized.


Low code platforms provide speed, but without learning,
            that speed doesn't last


This brings us to the
                Illusion of Speed offered by âstarter kitsâ and âlow-code platforms.â They provide a
                powerful initial velocity for standard use cases, but this speed comes at a cost.
                The readymade components we use are essentially compressed bundles of
                context—countless design decisions, trade-offs, and lessons are hidden within them.
                By using them, we get the functionality without the learning, leaving us with zero
                internalized knowledge of the complex machinery we've just adopted. This can quickly
                lead to sharp increase in the time spent to get work done and sharp decrease in
                productivity.


![](llm-learning-loop/graph.svg)


What seems like a small change becomes a
                time-consuming black-hole


I find this very similar to the performance graphs of software systems
                at saturation, where we see the 'knee', beyond which latency increases exponentially
                and throughput drops sharply. The moment a requirement deviates even slightly from
                what the readymade solution provides, the initial speedup evaporates. The
                developer, lacking the deep context of how the component works, is now faced with a
                black box. What seems like a small change can become a dead end or a time-consuming
                black hole, quickly consuming all the time that was supposedly saved in the first
                few days.


LLMs amplify this ephemeral speed while undermining the
            development of expertise


Large Language Models amplify this dynamic manyfold. We are now swamped with claims
                of radical productivity gains—double-digit increases in speed and decreases in cost.
                However, without acknowledging the underlying nature of our work, these metrics are
                a trap. True expertise is built by learning and applying knowledge to build deep
                context. Any tool that offers a readymade solution without this journey presents a
                hidden danger. By offering seemingly perfect code at lightning speed, LLMs represent
                the ultimate version of the Maintenance Cliff: a tempting shortcut that bypasses the
                essential learning required to build robust, maintainable systems for the long term.


LLMs Provide a Natural-Language Interface to All the Tools


So why so much excitement about LLMs?
            One of the most remarkable strengths of Large Language Models is their ability to bridge
            the many languages of software development. Every part of our work needs its own
            dialect: build files have Gradle or Maven syntax, Linux performance tools like vmstat or
            iostat have their own structured outputs, SVG graphics follow XML-based markup, and then there
            are so may general purpose languages like Python, Java, JavaScript, etc. Add to this 
            the myriad of tools and frameworks with their own APIs, DSLs, and configuration files.
            LLMs can act as translators between human intent and these specialized languages. They
            let us describe what we want in plain English—“create an SVG of two curves,” “write a
            Gradle build file for multiple modules,” “explain cpu usage from this vmstat output”
            —and instantly produce code in appropriate syntax inseconds. This is a tremendous capability. 
            It lowers the entry barrier, removes friction, and helps us get started faster than ever.
            But this fluency in translation is not the same as learning. The ability to phrase our
            intent in natural language and receive working code does not replace the deeper
            understanding that comes from learning each language's design, constraints, and
            trade-offs. These specialized notations embody decades of engineering wisdom. 
            Learning them is what enables us to reason about change—to modify, extend, and evolve systems
            confidently.
            LLMs make the exploration smoother, but the maturity comes from deeper understanding.


The fluency in translating intents into code with LLMs is not the same as learning


Large Language Models give us great leverage—but they only work if we focus
                on learning and understanding.
                They make it easier to explore ideas, to set things up, to translate intent into
                code across many specialized languages. But the real capability—our
                ability to respond to change—comes not from how fast we can produce code, but from
                how deeply we understand the system we are shaping.
                Tools keep getting smarter. The nature of learning loop stays the same.
                We need to acknowledge the nature of learning, if we are to continue to
                build software that lasts— forgetting that, we will always find
                ourselves at the maintenance cliff.


---
