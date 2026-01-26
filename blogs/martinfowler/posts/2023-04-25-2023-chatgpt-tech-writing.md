---
title: "Using ChatGPT as a technical writing assistant"
description: "An experienced technical author explores using ChatGPT to assist   with a number of writing projects. He finds ChatGPT can provide time-savings   through drafts and prompting for additional content, b"
date: 2023-04-25T00:00:00
tags: ["writing", "generative ai"]
url: https://martinfowler.com/articles/2023-chatgpt-tech-writing.html
slug: 2023-chatgpt-tech-writing
word_count: 3667
---


In recent weeks, I’ve been exploring the use of ChatGPT within a
    professional context. As a consultant I write extensively about technology
    and software, advise clients, and collaborate with internal teams. To avoid
    any potential intellectual property issues, I consulted both my boss and one
    of the company lawyers. I specifically avoiding using ChatGPT in any
    client-related context. Instead, I focused on employing ChatGPT for
    technical writing intended for public consumption, thereby minimizing the
    possibility of inadvertently exposing proprietary information to the AI.


![](2023-chatgpt-tech-writing/card.png)


We like to include an image for our twitter card, for
    this one, we naturally went to Stable Diffusion. We used the prompt
    “concept art of a human and an ai facing each other, collaborating using 
  an advanced holographic display, close up, mid-length framing” (Stable Diffusion v2-1_768-ema-pruned, model hash ad2a33c361, seed 564306172)


## Goals and expectations


When I first considered using ChatGPT as a writing assistant, I had a
      few specific goals in mind. One of the main tasks I hoped it would help me
      with was crafting ‘blips’ for the Thoughtworks [Technology Radar](https://www.thoughtworks.com/radar). The
      radar covers over 100 individual technologies, and while our team engages
      in detailed discussions about each of them, translating those notes into a
      coherent paragraph can be challenging. I was hopeful that ChatGPT could
      streamline this process and make it more efficient.


In addition to the blips, I write an accompanying article called 
    “[Macro
      Trends in the Technology Industry](https://www.thoughtworks.com/insights/blog/technology-strategy/macro-trends-tech-industry-april-2023)” that delves into the broader themes and
      patterns we observe in the field. I was curious to see if ChatGPT could
      play a role in shaping this piece, providing insights or even contributing
      content.


Lastly, we also adapt the Technology Radar for a business context,
      aiming to make its high-level themes more accessible to a non-technical
      audience. This often involves simplifying complex concepts and presenting
      them in a more digestible format. I wanted to explore the potential of
      ChatGPT in assisting with this task, helping us create content that
      effectively communicates our ideas to a wider readership.


## Radar Blip: Casual management of webhooks - Hold


Mike


Hello. Please help me write a 'blip' in the style of the
        Thoughtworks technology radar, about the dangers of âCasual Management
        of Webhooksâ. Summarize the notes and discussion below:


With the rise of remote working we are continuing to see growing
        adoption of chat collaboration platforms (e.g. Slack, Google Chat,
        Microsoft Teams) and with it a rise in âChatOpsâ. Most chat
        collaboration platforms offer webhooks as a simple way to automate
        sending messages and notifications to channels, and much developer
        platform tooling (e.g. CI/CD software, monitoring software, etc) is
        building out first class support for utilising these webhooks. However
        there is a tendency to treat these webhooks as configuration, rather
        than as a secret/credential. We see this tendency manifesting in how
        chat tools present webhooks, how teams treat and store webhooks (e.g.
        committing them in plain text to a repo), and how integrated tooling
        treats webhooks (e.g. exposing them in plain text). This is a security
        smell that can open up an organisation to phishing attacks.


ChatOps webhooks are a credential: they offer privileged access to
        an internal space. In some cases, they directly contain API keys that
        can be extracted and utilised directly. Not treating them as secrets
        opens up the possibility that they can be used for phishing, and that
        phishing is more likely to be successful because of the lack of
        awareness of this type of attack. Webhooks in git repos can easily be
        extracted and used to craft and send a fraudulent payload, which the
        user may have no reason to doubt and no way to authenticate. There has
        not been major reported incidents of this type in the wild which only
        adds to the complacency. In order to mitigate this threat we need to
        see a shift, both in the culture of teams who are handling these
        webhooks, and in the culture of software developers who are building
        integrations with ChatOps platforms.


ChatGPT


Here’s a blip in the style of the Thoughtworks technology
        radar:


Dangers of Casual Management of Webhooks: A Security Smell


As remote work continues to rise, so does the adoption of chat
        collaboration platforms and ChatOps. These platforms often offer
        webhooks as a simple way to automate sending messages and
        notifications, but we are noticing a concerning trend of treating
        webhooks as configuration, rather than as a secret/credential. This
        can lead to phishing attacks and compromised internal spaces.


Webhooks are credentials that offer privileged access to an
        internal space and may contain API keys that can be easily extracted
        and utilized directly. Not treating them as secrets opens up the
        possibility of successful phishing attacks. Webhooks in git repos can
        easily be extracted and used to send fraudulent payloads, which the
        user may not have any way to authenticate.


To mitigate this threat, teams handling webhooks need to shift
        their culture and treat webhooks as sensitive credentials. Software
        developers building integrations with ChatOps platforms must also be
        mindful of this risk and ensure that webhooks are handled with proper
        security measures. Let’s not wait for a major incident to occur before
        taking action.


**Discussion**


This output was pretty good, especially the first paragraph that
        justifies the rise of ChatOps and explains how webhooks are related. The
        final paragraph is some kind of “call to action” which isn’t really
        right for a Radar blip, but it was easy enough to remove. Thoughtworks has 
    published the Technology Radar for more than ten years now, so simply asking
    for output “in the style of the Thoughtworks 
    Technology Radar” creates text that has more or less the right kind of
    style for a Radar blip. If I wanted something in a different style I would
    have needed to be more specific in my prompt. You can see the final 
  [casual
  management of webhooks](https://www.thoughtworks.com/radar/techniques/casual-management-of-webhooks) text on the Radar site, to see where we ended up 
  after editing, including a round of company-wide feedback.


## Radar Blip: Giskard - Assess


In the style of the thoughtworks technology radar, write a
        'blip' for âGiskardâ. Incorporate the following notes, and keep the
        resulting write up to two paragraphs.


Giskard is Quality Assurance for AI models, e.g. helps find
        biases


why


Seems like a new kind of tool, makes collaboration between data
        scientists and business stakeholders / SMEs easy. No real experience
        with the tool yet.


Person A: People I talked to highlighted the quality assurance
        part, you can write a variety of tests for it


Person B: The âwhyâ here is copied from website, but what IS it
        actually that makes the collab easier?


Person C: When we are reasoning about models, lots of business
        implications involved, so bias avoidance can be quality metrics for a
        model; you can codify acceptance criteria for your models, together
        with business


This one is most about data quality compared to other tools


Giskard emerges as a novel Quality Assurance solution for
        AI models, specifically designed to identify and mitigate biases. By
        focusing on data quality, Giskard distinguishes itself from other
        tools in the market. It fosters collaboration between data scientists
        and business stakeholders, enabling them to jointly establish
        acceptance criteria for AI models based on bias avoidance and other
        essential quality metrics. This ensures that the model outcomes are
        better aligned with business objectives, while also minimizing the
        risks associated with biased predictions.


Though we have limited hands-on experience with Giskard,
        conversations with users have emphasized its ability to support a wide
        range of tests for quality assurance. The tool’s unique value
        proposition lies in facilitating seamless collaboration between
        technical and non-technical stakeholders, making it easier to reason
        about models and their business implications. By allowing teams to
        codify their criteria, Giskard promotes transparency, streamlines the
        development process, and helps organizations build more robust and
        ethical AI models.


**Discussion**


The text is clearly way too optimistic for an ‘assess’
        blip on the Radar. The fact that ChatGPT has been trained on tons of
        marketing pages on the Internet, as well as fine tuned using human
        feedback, has led to the bot saying things that we never would. Words
        like ‘novel’ and ‘unique’ are something I’d edit and remove.


What was very interesting here though is the response from one of
        our machine learning experts in Finland. She said it sounded like the
        blip had been written by a junior person with very little
        understanding of the typical ML workflow, and she made some quite
        significant changes before the blip text was ready for
        publication. I’m not an expert in this particular
    tool — although I’ve used a few ML tool chains — and this critical feedback highlights the
    fact that ChatGPT output generally requires quite skilled experts to review and edit.
  Here's the [Giskard blip on 
  the Radar](https://www.thoughtworks.com/radar/tools/giskard) after human review and editing.


## Macro trends article


I'm the author of the Thoughtworks âmacro trendsâ series of
        articles. Are you familiar with those? Can you tell me what they are
        about?


As an AI language model, I'm familiar with a wide range of
        topics, including the Thoughtworks âmacro trendsâ series of articles.
        The series aims to identify and analyze the significant macro-level
        trends that are shaping technology, business, and society. These trends
        often have a global impact and are driven by factors such as
        technological advancements, changes in consumer behavior, economic
        shifts, and global events. By understanding these macro trends,
        organizations and individuals can better adapt to change and capitalize
        on emerging opportunities.


Some of the key topics covered in these articles may include (but are
        not limited to):


The rise of artificial intelligence and machine learning


The increasing importance of data privacy and security


The role of digital transformation in businesses


The growing impact of climate change and sustainability efforts


The expansion of the Internet of Things (IoT) and connected
        devices


The evolution of the workforce and the future of work


The development of new technologies, such as blockchain and quantum
        computing


The specifics of each article may vary depending on the time they
        were written and the trends relevant at that time.


OK, I think you have the idea. I would say it's not really
        about society, though, it's more of a tech industry focus.


I have made some notes on new trends for a new article. I'd like you
        to help me express my notes as sections of a macro trends article.


The first trend is around knowledge management for teams. We
        discussed interesting tools Logseq and Obsidian, and we wrote blips
        about them. For logseq we wrote:


Team knowledge management is a familiar concept with teams using
        tools such as wikis to store information and onboard new team members.
        Some of our teams now prefer to use logseq as a team knowledge base. An
        open-source knowledge-management system, loqsec is powered by a graph
        database, helps users organize thoughts, notes and ideas and can be
        adapted for team use with Git-based storage. Logseq allows teams to
        build a democratic and accessible knowledge base, providing each member
        with a personalized learning journey and facilitating efficient
        onboarding. However, as with any knowledge management tool, teams will
        need to apply good curation and management of their knowledge base to
        avoid information overload or disorganization.


While similar functionality is available in tools like Obsidian, the
        key difference lies in Logseq's focus on consumption, with
        paragraph-based linking enabling team members to quickly find the
        relevant context without having to read an entire article.


Can you turn this into a macro trends article section about knowledge
        management tools for teams? It should be about 3 paragraphs long.


Emerging Trend: Next-Generation Knowledge Management Tools
        for Teams


In today's fast-paced technology landscape, effective knowledge
        management is more crucial than ever for teams to stay competitive and
        agile. Traditional tools like wikis have been commonly used to store and
        share information, but recently there has been a surge of interest in
        more advanced and versatile knowledge management systems. These new
        tools, such as Logseq and Obsidian, offer innovative features that are
        transforming the way teams manage, access, and engage with their
        collective knowledge.


Logseq, an open-source knowledge-management system, is a prime
        example of this shift. Powered by a graph database, it helps users
        organize thoughts, notes, and ideas and can be adapted for team use with
        Git-based storage. Logseq's unique approach enables teams to build a
        democratic and accessible knowledge base, providing each member with a
        personalized learning journey and facilitating efficient onboarding. Its
        paragraph-based linking feature allows team members to quickly find the
        relevant context without having to read an entire article, emphasizing
        its focus on consumption. However, as with any knowledge management
        tool, teams will need to apply good curation and management practices to
        avoid information overload or disorganization.


Similarly, Obsidian offers robust knowledge management capabilities,
        but with a stronger emphasis on content creation. While both tools
        provide valuable features for managing and accessing information, their
        differences highlight the evolving nature of team knowledge management.
        As these tools continue to develop and gain traction, they are set to
        redefine the way teams collaborate and learn, ultimately driving
        innovation and productivity in the tech industry.


**Discussion**


Similar to the Radar blips drafted by ChatGPT, this text is overly
        ‘bubbly.’ Phrases like “more crucial than ever” just sound a little too
        hyperbolic. I found this was a common theme – ChatGPT is just way too
        optimistic and happy sounding, and almost ends up a little bit ‘bland’
        because of this. But a quick edit pass can fix this and introduce
        words that are more like the ones I would really use to describe this
        trend.


Additionally, ChatGPT seems to always structure its responses as
        introduction, information, summary. It seems to do this whether you have
        asked an open-ended question or are asking it to help you create a
        section of an article. I found I repeatedly needed to discard or
        condense the opening and closing paragraphs of ChatGPT’s output.


You can find the 
    [finished 
    macro trends article](https://www.thoughtworks.com/insights/blog/technology-strategy/macro-trends-tech-industry-april-2023) on the Thoughtworks website.


## Adapting the radar for a less-technical audience


I need to rewrite some stories that are told in a technical
        context, but for a less technical business audience.


Accessibility has been an important consideration for organizations
        for many years. Recently, we've highlighted the experiences of our teams
        with the ever-growing set of tools and techniques that add improved
        accessibility to development, and several regions our teams highlighted
        awareness of these techniques via awareness campaigns. We've featured
        accessibility-related blips on continuous integration pipeline
        development, [design
        playbooks](/radar/techniques/accessibility-annotations-in-designs),
        [intelligent guided accessibility
        testing](/radar/techniques/intelligent-guided-accessibility-tests),
        [linting](/radar/tools/axe-linter) and [unit
        testing](/radar/tools/ibm-equal-access-accessibility-checker). Growing
        awareness around this important topic is welcome; techniques that give
        more people access to functionality in improved ways can only be a good
        thing.


Can you rewrite this in the form âwhat is itâ (one or two sentences)
        and âbusiness contextâ (one paragraph) ?


What is it?


Accessibility has become increasingly important for organizations,
        with a growing set of tools and techniques available to improve it in
        development processes and awareness campaigns promoting its
        significance.


Business context:


As businesses prioritize accessibility, they are adopting various
        tools and techniques that make their products and services more
        inclusive. These include continuous integration pipeline development,
        design playbooks, intelligent guided accessibility testing, linting, and
        unit testing. Embracing accessibility not only benefits a wider range of
        users but also enhances a company's reputation for being socially
        responsible and inclusive, ultimately fostering positive outcomes for
        both the organization and its customers.


Can you describe 'accessibility' in one sentence?


Accessibility refers to the design of products, services,
        and environments that ensure people with disabilities can effectively
        and easily access, use, and interact with them.


Based on this, what advice would you give businesses around
        accessibility?


Businesses should prioritize accessibility by designing and
        adapting their products, services, and environments to be inclusive and
        user-friendly for people with disabilities, thereby demonstrating social
        responsibility, enhancing their reputation, and reaching a broader
        customer base.


**Discussion**


I was very happy with this output. ChatGPT provided a
        very good “business readable” version of the Radar theme and this
        definitely saved me some time. I thought the advice it generated
    was pretty good.


## Strengths and weaknesses of ChatGPT in technical writing


On balance, I’d say ChatGPT has proven to be a useful tool in the technical writing
      process, but it’s not without its foibles. Understanding its strengths and weaknesses
      can help you to get the most out of it.


Strengths:

- **Knowledge:** ChatGPT excels at instant recall of similar
        situations, facts, and ways others have discussed a subject. This allows
        it to bring up additional points that might be relevant to the topic at
        hand, prompting me as an author to write more or cover additional related
        information.
- **Time-savings:** Output from ChatGPT serves as a
        good starting point for writing, saving time by providing initial
        content that can be refined or expanded upon.
- **Suggested additions:** ChatGPT can offer suggestions for
        additional content or sections, and they are generally quite useful. 
    I fed it an outline for this article and it proposed “goals and
        expectations” and “strategies for improving ChatGPT’s output” as additional sections,
        both of which I liked and included in my writing process.


Weaknesses:

- **Accuracy and depth: **ChatGPT’s responses may not always be
        accurate or in-depth, requiring manual review and revision. It also has
    an “information cutoff” date, so recent events or updates won’t be reflected
    in its output.
- **Overly positive and optimistic:** The AI tends to produce
        content that is too positive and optimistic, which might not be suitable
        when a critical eye is needed, as with the Technology Radar blips.
- **Context limitations:** Both GPT-3.5 and GPT-4 have context
        limits, with GPT-4 having significantly larger limits. This constraint
        can lead to issues where ChatGPT only considers its most
        recent output or forgets context from earlier in the process.
- **Anchoring:** ChatGPT can sometimes get ‘stuck’ or ‘anchored’ at a
        local maximum. For example, I once asked it to expand some bullet point notes
    into a multi-paragraph article, which worked fine. I thought the output 
    could use more detail and asked it to expand on what it had written,
    but it produced essentially the same content again
    without actually adding detail as I had asked.
    In such cases, it might be necessary to start a new chat
        using the best output so far to overcome this issue.


## Strategies for improving ChatGPT’s output


ChatGPT can be a useful technical writing assistant, but the quality of
    the output depends heavily on how you use it. Here are some tips for
    refining ChatGPT’s responses:

- **Use a context-setting prompt:** Create, tweak, and reuse a
      context-setting prompt that outlines the style of writing, context, and
      target audience. This helps ensure that subsequent content has a
      consistent tone and is tailored to your requirements, even if you need
      to break up your work across multiple chat sessions.
- **Work iteratively:** Just like working with a human writer, it’s important to
      remember that ChatGPT might not get everything right on the first try.
      Be patient and take the time to steer the AI in the right direction,
      refining its output through iteration. If you find a particular
      instruction useful, incorporate it into your context-setting prompt.
- **Focus on smaller content:** GPT-3.5 works better with smaller content,
      such as individual sections of an article. GPT-4 is more adept at handling longer
      pieces, but it’s generally better to use separate conversations with the
      AI to create an outline and then tackle each major section individually.
- **Use a collaborative approach:** Treat ChatGPT as a valuable peer rather
      than a subordinate. Large language models tend to respond to users at
      their apparent level, so providing professional-looking prompts will
    increase your chances of receiving professional-looking output.


## Avoiding over-reliance on AI-generated content


I’ve also been experimenting with ChatGPT for coding purposes,
      specifically to assist me in learning new technology stacks (a subject I
      plan to explore in a future article). On a few occasions, GPT-4
      had downtime during a session, which left me feeling somewhat
      at a loss—my AI “companion” had suddenly vanished! 
      GPT-3.5 was still online but it isn’t quite as good;
    I much preferred to use GPT-4. This highlights the fact
      that it’s surprisingly easy to become dependent on these AI tools. Here
      are some tips to maintain a critical perspective and ensure high-quality
      output:

- **Evaluate AI-generated content: **Always scrutinize the AI’s
        output for accuracy and relevance. Consider whether you agree with the
        content, if there are any factual errors, or if there are implications
        you might not endorse.
- **Identify what’s missing: **Analyze the output
        for any missing nuances or specific points you would have made if you were
    writing the piece yourself. It can be challenging to spot these gaps once
    you have a seemingly complete piece of writing, but it’s an essential 
    step in maintaining the quality of your work.
- **Invest enough time: **Keep in mind that critically editing
        ChatGPT’s output will take time. The “AI productivity boost” might not
        be as substantial as one might initially think. If you’re unable to 
        invest the necessary effort, the content might not meet your standards.
- **Take ownership: **Remember that, ultimately, it’s your content and
        your name on the article. Treat ChatGPT as a helpful tool, but don’t
        forget your responsibility for the final output.


I would say my experiments with ChatGPT as a writing assistant were a success. I don’t think I saved time,
    overall, more that I was able to make steady progress by using the AI’s output as a starting point.
    I think this style of using LLMs—to create first drafts and to suggest additions—will work for a variety
    of tasks in the software world, from story writing, to acceptance testing, to documentation.
    I don’t think the AIs are here to take our jobs—you still need a human expert working with the output—but
    I do expect these kinds of tools will help humans produce higher quality results. Working effectively with
    AI tools has become a key skill for knowledge workers, starting right now.


---
