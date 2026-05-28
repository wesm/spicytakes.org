---
title: "The VibeSec Reckoning"
description: "âVibe codingâ - the practice of non-technical citizen builders using   generative AI tools to rapidly develop applications, this has significantly accelerated   software prototyping. However, beca"
date: 2026-05-27T00:00:00
tags: ["security", "generative ai"]
url: https://martinfowler.com/articles/vibesec-reckoning.html
slug: vibesec-reckoning
word_count: 2241
---


[Vibe coding](https://martinfowler.com/bliki/VibeCoding.html) is enabling non-technical users (or as we call them, citizen
    builders) to build applications with AI that they simply could not have
    built before. When our AI applications team in Global Marketing at
    Thoughtworks was asked to scale a vibe coded prototype built by one of our
    citizen builders in global marketing, we discovered serious cracks that
    prevent vibe coded applications from going into production safely.


Speed without guardrails is a risk no team can afford to ignore. What
    follows is the story of what we found, what it means for teams building with
    AI, and the steps we are taking to make sure every workflow, prototype, and
    app we ship is one we can stand behind.


## What we learned the hard way


The AI applications team within Global Marketing was asked to scale a video
      assembly prototype built with Gemini, Replit AI and Claude AI to create
      on-brand videos to be used across our 10,000 employees. The team ran into two
      moments that stopped work cold. In both cases, the AI suggested a path with
      serious security implications. In both cases, it took a human asking the right
      question to catch it.


Security risk # 1


#### Public storage access


The AI recommended making the storage
          bucket public, or setting cloud file storage to âanyone with the link.â When
          challenged, it justified this by saying every company does it. Only a firm
          rejection prompted a secure alternative.


This could have leaked sensitive
          unreleased brand assets and audience data to the public internet.


Security risk # 2


#### Excessive token permissions


A service account was assigned the Access
          Token Creator role, granting it the ability to create short-lived tokens and
          access databases and other resources far beyond what the task required. The team
          caught this before running the code.


This would have allowed a compromised
          service account to move laterally through an entire cloud workspace.


The key insight here is that AI tools often suggest the path of least
      resistance. That path is not always the secure one. Human judgment remains
      essential, but it should not be the only control. The goal is to give
      agents technical security rules as context from the first prompt, then
      validate their output through deterministic checks in the development
      workflow so insecure code, permissions, secrets, or infrastructure cannot
      pass unnoticed.


## The numbers behind the risk


44%


Rise in attacks exploiting application vulnerabilities, year on year


1 in 5


Enterprise breaches now caused by AI-generated code


50%


Organisations with no sensitive data policies for AI


25%


AI-generated code with confirmed vulnerabilities


These incidents are not isolated. Research published in 2026 confirms that
      AI-assisted coding at speed creates systemic security exposure. The same risks
      we encountered are playing out across the industry right now.



| Finding | Stat | Source |
| AI-generated code with confirmed vulnerabilities | 25% | [AppSec Santa, 2026](https://www.paperclipped.de/en/blog/ai-generated-code-security-vulnerabilities/) |
| Rise in attacks exploiting application vulnerabilities, year on year | 44% | [SQ Magazine AI Coding Security Statistics, 2026](https://sqmagazine.co.uk/ai-coding-security-vulnerability-statistics/) |
| Codebases with high or critical severity vulnerabilities | 78% | [Black Duck OSSRA 2026](https://www.blackduck.com/blog/open-source-trends-ossra-report.html) |
| Organisations with no sensitive data policies for AI | 50% | [AppSec Santa, 2026](https://www.paperclipped.de/en/blog/ai-generated-code-security-vulnerabilities/) |
| Mean vulnerabilities per codebase increase year on year | +107% | [Black Duck OSSRA 2026](https://www.blackduck.com/blog/open-source-trends-ossra-report.html) |
| Enterprise breaches now caused by AI-generated code | 1 in 5 | [Aikido Security, 2026](https://www.aikido.dev/reports/2026-state-of-ai-in-security-development) |
| New CVEs from AI-generated code in March 2026 alone | 35 | [Georgia Tech Vibe Security Radar, SSLab, March 2026](https://www.infosecurity-magazine.com/news/ai-generated-code-vulnerabilities/) |
| AI systems with prompt injection exposure in 2026 audits | 73% | [SQ Magazine AI Coding Security Statistics, 2026](https://sqmagazine.co.uk/ai-coding-security-vulnerability-statistics/) |
| Share of all new enterprise software that is AI-generated | 42% | [Sonar developer survey, 2026](https://www.sonarsource.com/blog/state-of-code-developer-survey-report-the-current-reality-of-ai-coding) |
| Security teams say keeping up with AI-generated code volume is getting harder | 62% | [ProjectDiscovery AI Coding Impact Report, April 2026](https://www.prnewswire.com/news-releases/projectdiscoverys-2026-ai-coding-impact-report-reveals-ai-generated-code-is-outpacing-security-teams-ability-to-keep-up-302749706.html) |



## The real problem: prompts are not enough


After sharing these incidents with engineering and security colleagues, a
      clear message came back: telling an AI agent to be safe is not the same as
      enforcing that it is safe. Prompts can be overridden, misunderstood, or
      ignored. The moment a user pushes back on a restriction, or phrases a request
      differently, the constraint can evaporate.


“It is not sufficient to merely tell the LLM the desired behavior of your output artifacts. If you absolutely do not want something to be true, it must be codified in non-negotiable rules somewhere in your development lifecycle.” - Engineering leadership


Think of it this way: prompting for test-driven development is not the
      same as enforcing code coverage thresholds in your build tool. One is a
      suggestion. The other is a gate. [Birgitta
      Böckeler’s work on harness engineering](https://martinfowler.com/articles/harness-engineering.html) makes this concrete by
      outlining a mental model for building trust in coding agents. Instead of
      relying solely on prompts, developers wrap the agent in an outer âharnessâ
      structured along two axes:

- **Guides** (feedforward controls) anticipate unwanted
        behavior and steer the model before it acts, while **Sensors** (feedback controls)
        observe the code after the agent acts to flag errors.
- **Computational** controls are deterministic,
        fast, and CPU-run (like linters or test suites). **Inferential** controls rely on
        semantic analysis and AI-driven judgment (like specific system prompt
        constraints).


## Why business functions need to pay attention


Business functions like our marketing team, who are building with AI, are
      not exempt from the security obligations that apply to engineers building
      applications. Building security into software is a fundamental requirement for
      protecting customer and employee data. Even lightweight internal prototypes
      must comply with enterprise security standards. Without the right guardrails,
      AI-assisted development can expose sensitive data long before an application
      reaches production.


Client trust


#### Compliance is contractual


Adhering to standards like ISO 27001 ensures the protection of
          sensitive data. All applications, regardless of how quickly they are
          built, must meet these security benchmarks to maintain the trust of
          customers and employees.


Brand integrity


#### Brand assets need protection


Core work involves sensitive functional data (e.g., unreleased
          campaign assets, financial data, or audience insights).
          Over-permissioned service accounts put far more than code at
          risk.


Reputation


#### Business functions can set the standard


When business functions like marketing lead with security
          discipline, they signal responsible AI adoption to the wider
          organisation and to clients.


## Short-term habits


You do not need to be a security expert to start building responsibly.
      These three habits can get you started.


#### Feed your technical security rules into every
          session


Add your organisation's security guidelines as âRulesâ in Claude,
          Cursor, or Replit to begin with (later on invest in a shared sensible
          default layer across all tools). The AI agent uses them as guidance,
          making secure patterns more likely from the start. They still need to
          be backed by deterministic checks that fail unsafe code, exposed
          secrets, broad permissions, vulnerable dependencies or insecure
          infrastructure before anything is deployed.


#### Question every permission the AI suggests


If a tool recommends making something public or assigning a
          broad service account role, stop and ask why. The path of least
          resistance and the secure path are rarely the same thing.


#### Try the [red team prompt](https://www.confident-ai.com/blog/red-teaming-llms-a-step-by-step-guide)


Ask your AI to roleplay as a bad actor and pen test what it
          just built. This technique consistently surfaces vulnerabilities that
          forward-looking prompts miss, particularly around permissions and data
          exposure.


## Medium-term solutions


Reading about risk is one thing. Doing something about it is another. These
      incidents prompted two practical initiatives. The principles behind them are
      replicable by any team building with AI, regardless of technical
      background.


#### A security context file


We compiled our technical security rules into a structured context
          file loaded into every AI coding session before any code is written.
          It covers zero trust enforcement, secrets management, harness
          engineering and supply chain integrity. The key distinction from a
          casual prompt is operational discipline: the file is versioned, loaded
          by default, reviewed, and paired with automated checks. It acts as a
          comprehensive inferential guide telling the agent what good looks
          like; but it must be paired with computational sensors in the pipeline
          to validate whether the output is acceptable.


#### A daily security intelligence feed


Currently, this automated consolidation ensures we see supply chain
          alerts the day they are published. In the future, as we work toward an
          agentic enterprise, we envision agents proactively creating story
          cards and identifying and patching known vulnerabilities behind the
          scenes for human review, significantly reducing the Software
          Development Lifecycle (SDLC) cycle time.


## The security context file in practice


The idea behind this approach is straightforward: AI tools read context at
      the start of a session, so make that context your technical security rules.
      The file is the result of working through your organisation's security
      requirements and structuring them in a form the AI can act on, not just
      acknowledge.


What follows is the kind of coverage any such file should include. The
      specifics will differ by organisation, but the categories are consistent.



| Area covered | What good looks like | Why it matters |
| Zero trust and least privilege | Strict identity verification and minimum access rights on every service account and storage resource | Sets the inferential guide parameters to prevent the token permission risk directly. |
| Secrets management | AI refuses to generate or store API keys, passwords or tokens in code; always routes to environment variables or a secrets manager | Stops credential leakage before it reaches a repository. |
| Harness engineering gates | SAST scanning, credential scanning and infrastructure validation must pass before deployment; no reliance on prompt instructions alone | Backs up inferential instructions with deterministic, computational sensors. |
| Supply chain integrity | Only well-established libraries; regular audits of every dependency for known vulnerabilities | Reduces risk from AI suggesting obscure or unvetted packages. |
| AI accountability | All AI-generated code is flagged for peer review and automated security scanning before deployment; no unsanctioned AI usage | Required for compliance auditability. |



The key distinction from a prompt is that the file contains non-negotiable rules that force the AI agent to refuse requests that violate policy. If the AI agent is asked to bypass a check, disable logging or set something to public access, the rules should steer it to decline and explain why. But the important control is that deterministic checks and deployment gates should still catch the issue even if the agent fails to follow that guidance. That refusal is precisely what was missing in both of our near-miss incidents.


## The security intelligence feed in practice


Staying informed is its own form of defence. The workflow monitors the
      tools and languages your team actively uses and delivers a daily digest of new
      CVEs, platform advisories and security bulletins. The coverage areas that
      matter most are consistent across organisations: the languages they write in,
      the cloud platforms they deploy to, the AI coding tools themselves, and the
      CVE database as a whole.


The goal is simple: learn about a vulnerability on the day it is disclosed,
      not weeks later. At 42% of all new enterprise software now AI-generated or
      AI-assisted, the tools that accelerate development are also the tools most
      likely to appear in new CVE disclosures. Monitoring them actively is part of
      owning your security.


#### The Broader point


Neither of these approaches requires an engineering background to
        adopt. One is a policy document structured for AI consumption. The other
        is an automated search. What they share is the recognition that passive
        security awareness is not enough when AI is generating code at
        speed.


## Long-term organisational changes


#### From prompts to pipelines


Integrate harness engineering into your standard prototyping
          templates. Move from probabilistic prompts to explicit feedback loops.
          If a computational sensor (like an automated security scanner)
          triggers, the agentic loop must structurally force the model to
          self-correct until it passes.


#### Feed security rules into the application builder (Cursor, Claude etc)


Compile your organisation's technical security rules into a
          structured context markdown file and load it as “Rules” which the
          model will have to adhere to. It catches the most common missteps at
          the point where they are cheapest to fix, before any code is
          committed.


#### Make the secure path the easy path


Give builders a secure-by-default starting point. Templates that
          pre-configure authentication patterns, private storage defaults,
          secrets handling and dependency scanning reduce the chance that anyone
          takes a shortcut under deadline pressure.


#### Define a starter harness across functions


A shared starter harness built together by business functions,
          engineering and security gives every builder a secure foundation from
          day one, rather than each team independently rediscovering the same
          mistakes.


## Conclusion: Scaling Beyond the Prototype


This journey started when we were brought in to support another team
      building a video assembly platform for a Global Marketing hackathon. As we
      helped scale the solution, it became clear that “vibe coding” without
      enterprise-grade guardrails can introduce risks that organizations simply
      cannot overlook.


By embedding our technical security rules directly into the agent workflow,
      we transformed those early near-misses into a secure, production-ready
      platform that was successfully rolled out to 150 users during the
      hackathon.


That shift - from depending on humans to catch issues, to building
      technical security rules, automated checks and human accountability into the
      workflow has become our blueprint for moving fast while maintaining
      engineering rigor in the agentic era.


---
