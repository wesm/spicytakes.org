---
title: "FizzBee, TLA+, and (Practical) Formal Software Verification with JP Kadarkarai"
subtitle: "JP, the creator of FizzBee, talks about formal methods, TLA+, distributed systems verification, and a better way forward."
date: 2024-09-18T11:24:30+00:00
url: https://materializedview.io/p/fizzbee-tla-and-formal-software-verification
slug: fizzbee-tla-and-formal-software-verification
word_count: 1873
---


I recently had the chance to interviewJayaprabhakar(JP) Kadarkarai. JP is the creator of FizzBee, a design specification language and model checker to specify distributed systems. Prior to FizzBee, JP worked at Clumio, Lyft, and was a tech lead at Google.


---


C.R.: Let's start with how you got into formal methods. It looks like you spent 12 years at Google before moving on to Lyft and Clumio. At what point did you first come across formal methods, what problem were you solving, and which tools did you use?


JP: Before joiningGoogle, the systems I worked with were relatively small-scale, and we managed consistency through centralized databases. However, at Google, everything we built had to be large-scale, highly available, and eventually consistent. This shift required a deep understanding of how to maintain data integrity and fault tolerance in a decentralized environment.


As I worked with systems likeGFS,Bigtable, andSpanner, and delved into their design papers, I saw firsthand the importance of ensuring system correctness, especially in scenarios involving data consistency and failure recovery. These papers often included rigorous proofs, highlighting the complexity of building robust systems. This experience sparked my interest in exploring more rigorous methods for verifying correctness.


After leaving Google, I noticed a gap in the broader industry, where microservices and NoSQL databases were often adopted without a solid theoretical foundation. At bothLyftandClumio, I encountered consistency issues that often led to customer escalations and the need for refunds.


Having a habit of reading papers on various topics, I explored distributed systems classics and came across works byLeslie LamportandNancy Lynch. This led me to discoverTLA+, which opened up a whole class of formal methods tools. Among these, TLA+ stood out as the most accessible and widely used.


My experience with formal methods, particularly TLA+, is relatively recent, spanning just a couple of years. The first project I used TLA+ for was at Clumio, where we needed to charge customers for their backups. The previous system had design issues, and fixing them with code changes like retries or locks didn't address the root cause—it often just moved the problem elsewhere. So, when I took over the project, I wanted to prove the system's correctness. Initially, I explained the design, but then I wrote the TLA+ specs as well. Unfortunately, I couldn't convince anyone to review the TLA+ specs.


C.R.: I think I can guess, but why didn’t anyone want to review the TLA+ spec?


J.P.: The main reason was the complexity of TLA+'s syntax and semantics. Its syntax isn't intuitive—it relies heavily on ASCII representations of mathematical symbols, which can feel alien to most programmers. The semantics also require a level of mathematical reasoning that many developers aren't used to.


Moreover, by the time I had learned TLA+ in my spare time and modeled the system, a few weeks had passed, and the spec was no longer a priority for the team. I did get my proposal accepted, but it wasn’t the smoothest process. If there had been a more accessible formal verification tool, I could have clearly demonstrated the advantages of my proposal without risking misunderstandings or tension.


C.R.: I suppose this is whereFizzBeeenters the picture. How did you get from TLA+ to FizzBee, and can you give a brief overview of your new project?


J.P.: While working with TLA+, I found myself instinctively translating its specs into a more familiar, Java-like syntax to make sense of them. This led me to realize that a tool with a syntax closer to programming languages would be more intuitive. I explored various options and ultimately decided on a Python-like syntax because it felt the most natural and concise for expressing complex ideas.


For these methods to be widely adopted—not just for mission-critical applications but for everyday software engineering—I believe they must be simpler and easier to use. When there’s a tradeoff between quality and time to market, time to market almost always takes precedence.


Our goal with FizzBee is to enable developers to ship high-quality software faster. It’s designed to make it easier for everyday software engineers to ensure system correctness and performance. FizzBee uses a Python-like syntax to make the process of modeling and verification more intuitive and concise. The time taken to model a system in FizzBee is often less than the time it takes to write a traditional design document.


Additionally, FizzBee automates the generation of visualizations, like block and sequence diagrams, directly from the model, making it easier to communicate and review designs. This approach not only simplifies the design process but also helps catch potential issues early, allowing teams to ship more quickly.


C.R.: What does FizzBee’s architecture look like? How is it implemented?


J.P.:FizzBee’s current implementation is fairly straightforward.


The parser built withAntlrconverts the specification into anabstract syntax tree (AST). The model checker is an interpreter implemented in Go, starting with a breadth-first search from the initial state, evaluating next states while following FizzBee-specific rules for forking, context switching, crashes, and more. It uses theStarlarkinterpreter to evaluate expressions, checks assertions, and eventually evaluates liveness.


Once the checking is complete, states are stored on disk, which we then use for performance modeling in Python. The online playground and visualizations are implemented inNode.js/JavaScript.


Currently, the model checker runs in a single process and thread, with all states kept in memory. Distributed model checking is in the plans, and I expect to start on it in a month. It will be exciting to make this the first project within FizzBee to use FizzBee itself to model its distributed design.


C.R.: Did you consider writing a transpiler to convert FizzBee code to TLA+ so that you could leverage TLA+’s battle-testedproof system? Or do you have any other thoughts about TLA+ interoperability?


J.P.: Yes, I did consider writing a transpiler from FizzBee to TLA+, mainly to leverage its model checker. But I quickly realized that differences in syntax—like TLA+’s use of 1-indexed arrays—would make this impractical and error-prone. In fact, building a transpiler would have been more complex than just creating an interpreter directly.


Additionally, TLA+ wouldn’t support many of the features I wanted. For example, TLA+ tracks only state transitions, FizzBee needs to capture more detailed information, like decisions made during those transitions. This is essential to supporting features like performance modeling and interactive visualizations.


As for TLAPS, while it’s an impressive proof system, very few people actually use it. Even among TLA+ users, I don’t see it gaining widespread adoption. When I talk to other developers, they’re more focused on verifying that the implementation works correctly, rather than proving the design is flawless. So, a proof system isn’t a priority for FizzBee. If we ever do build one, it would more likely involve direct use of solvers, rather than relying on TLAPS.


C.R.: Given that you’re using Starlark, do you see any opportunity to somehow integrate the code in the design with the code that eventually gets shipped?


J.P.: That’s an interesting idea. I haven’t looked into it deeply yet, but I’m generally cautious about code generation systems where developers need to tweak the generated code. The gap between high-level models and actual implementation can be quite large, so keeping everything in sync is challenging.


However, embedding Starlark code snippets directly into the implementation could be feasible in some cases. I’d need to think through it more to identify where it might be practical. It’s definitely something worth exploring further.


C.R.:Let’s look to the future a little bit. Paint me a picture of what success looks like for FizzBee. You mentioned a distributed model checker. What other tools and integrations do you want to implement, and where do you see adoption coming from?


J.P.: FizzBee’s goal is to help teams ship high-quality software faster. By making formal methods practical and easier to use, we're addressing the stagnation in system design validation. Our recent release of interactive visualizations, for example, enhances communication of designs within teams. Ultimately, we aim to directly link these improvements to faster software delivery. Ensuring that the implementation matches the design is the critical missing link.


That’s our current focus. With FizzBee, from the model and its explored states and transitions, we can automatically generate comprehensive tests before any code is written. This approach delivers the benefits of Test-Driven Development without extra effort. We’re also exploring lightweight deterministic simulations to identify specific types of bugs. This would expand FizzBee to continuous builds.


As AI-assisted coding becomes more prevalent, validating that the code performs as intended will be essential for AI adoption. FizzBee will be instrumental in building that confidence.


C.R.: The AI angle is interesting; I hadn’t considered that. How do you envision FizzBee working with AI generated code? If an LLM generates code, how would a developer validate it using FizzBee. Have you thought at all about using an LLM to generate code from a FizzBee model?


J.P.: That’s a great question. When it comes to validating AI-generated code, FizzBee can provide value in two key ways: model-based testing and model-based monitoring.


First, with model-based testing, once a FizzBee model is built and validated, we can automatically generate comprehensive tests based on the model’s states and transitions. Whether the code is written by humans or AI, these tests ensure that the implementation behaves as expected, providing strong validation before deployment.


Second, FizzBee can enable model-based monitoring for post-production validation. FizzBee could monitor real-world behavior by analyzing databases, data lakes, logs, and other systems to detect anomalies. This would require developers to create a projection function that maps the runtime state of the application back to the model’s state. While this doesn’t prevent bugs from reaching production, it helps mitigate their impact by identifying them early on.


As for using an LLM to generate code from a FizzBee model, that’s trickier. FizzBee focuses on modeling complex, distributed systems logic, but a full application often includes a lot of business-specific logic that isn’t captured by the model. So, generating complete production code directly from a FizzBee model wouldn’t work—though it could generate basic scaffolding. We could introduce auxiliary structures to capture the additional requirements, but that’s beyond FizzBee’s current focus.


LLMs could, however, assist in other ways, such as helping generate FizzBee specs from natural language descriptions or enhancing FizzBee’s review platform by answering "what if" questions about system behavior.


Looking forward, LLMs have made tremendous progress in recent years, but for full code generation, they still need to handle intricate logic more reliably. I’m optimistic that future breakthroughs, perhaps in areas like reinforcement learning combined with LLMs, will bring us closer to that.


C.R.: Thank you so much for taking the time to talk with me. It’s been a really thought provoking conversation. There’s so much more to cover, but in the interest of time, let’s call it here. I’ll give you the final word. Anything you’d like to share?


J.P.: Thanks, Chris, I really enjoyed our conversation! I’m excited about the future of software development and the potential of formal methods.


We’re currently collaborating with early adopters and design partners through hands-on proof-of-concept projects. If you’re working on distributed systems and want to see how FizzBee can improve your development process, feel free to reach out atjp@fizzbee.io. You can also explore more atfizzbee.ioor check out our GitHub repo atgithub.com/fizzbee-io/fizzbee.
