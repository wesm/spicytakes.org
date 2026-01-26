---
title: "Threat Modeling Guide for Software Teams"
description: "Threat modeling is a systems engineering practice where teams examine how data    flows through systems to identify what can go wrong - a deceptively simple act   that reveals security risks that auto"
date: 2025-05-20T00:00:00
tags: ["security"]
url: https://martinfowler.com/articles/agile-threat-modelling.html
slug: agile-threat-modelling
word_count: 4841
---


Every software team should strive for excellence in building security into their application and infrastructure. Within Thoughtworks, we have long sought accessible approaches to threat modeling. At its heart, threat modeling is a risk-based approach to designing secure systems by identifying threats continually and developing mitigations intentionally. We believe effective threat modeling should start simple and grow incrementally, rather than relying on exhaustive upfront analysis. To demonstrate this in practice, we begin with outlining the core insights required for threat modeling. We then dive into practical threat modeling examples using the STRIDE framework.


## Breaking Down the Fundamentals


### Start from your Dataflows


Today’s cyber threats can seem overwhelming. Ransomware, supply chain
        attacks, backdoors, social engineering - where should your team begin?
        The attacks we read about in breach reports often chain together in
        unexpected and chaotic ways.


The key to cutting through complexity in threat modeling lies in tracing how data moves through your technology stack. Start with following where the data enters your boundary. Typically, it could be via user interfaces, APIs, message queues, or model endpoints. Dive into getting a deeper understanding of how it flows between services, through data stores, and across trust boundaries through integrated systems.


This concrete layout of the data flow between systems would transform vague worries, such as, âShould we worry about hackers?â into specific actionable questions. For example, âWhat happens if this API response is tampered with?â or âWhat if this model input is poisoned?â.


### The Crux to Identifying Threats


From there on, identifying threats can become deceptively simple: follow each one of the data flows and ask âWhat can go wrong?â. You'll find that this simple question will lead to complex technical and socio-behavioural analysis that will challenge your unconscious assumptions. It will force you to pivot from thinking “how system works” to “how system fails”, which in essence is the crux of threat modeling.


Let’s try it. We have an API for a messaging service that accepts two inputs: a message and the recipient’s ID, which then delivers the message to all internal staff. Follow through the carousel below to see how threats appear even this simple data flow.


Like illustrated in the carousel above, even a simple dataflow could warrant potential threats and cause havoc massively. By layering the question “What can go wrong?”, we have been able to expose this perspective that would otherwise remain hidden. The essence of doing this at this small scale leads to adding appropriate defense mechanisms incrementally within every data flow and therefore build a secure system.


### STRIDE as a Practical Aid


Brainstorming threats can become open-ended without structured frameworks to guide your thinking. As you follow key data flows through your system, use STRIDE to turbocharge your security thinking. STRIDE is an acronym and mnemonic to help remember six key information security properties, so you can methodically identify common security vulnerabilities. Mentally check each one off each time you consider a data flow:

- **S**poofed identity: *Is there Authentication? Should there be?* - Attackers pretending to be legitimate users through stolen credentials, phishing, or social engineering.
- **T**ampering with input: *What about nasty input?* - Attackers modifying data, code, or memory maliciously to break your system's trust boundaries.
- **R**epudiation: *Does the system show who is accountable?* - When something goes wrong, can you prove which user performed an action, or could they plausibly deny responsibility due to insufficient audit trails?
- **I**nformation disclosure: *Is sensitive data inappropriately exposed or unencrypted?* - Unauthorized access to sensitive data through poor access controls, cleartext transmission, or insufficient data protection.
- **D**enial of service: *What if we smash it?* - Attacks aiming at making the system unavailable to legitimate users by flooding or breaking critical components.
- **E**levation of privilege: *Can I bypass Authorization? Move deeper into the system?* - Attackers gaining unauthorized access levels, obtaining higher permissions than intended, or moving laterally through your system.


We use these [STRIDE cards](agile-threat-modelling/TW_STRIDE_Cue_Cards.pdf) internally during threat modeling sessions either as printed cards or have them on screen. Another great way to help brainstorm, is to use GenAI. You don't need any fancy tool just prompt using a normal chat interface. Give some context on the dataflow and tell it to use STRIDE- most of the time you'll get a really helpful list of threats to consider.


### Work 'Little and Often'


Once you get the hang of identifying threats, it's tempting to organize a
        full-day workshop to “threat model” every dataflow in your entire syste 
        at once. This big-bang approach often overwhelms teams and rarely sticks as a consistent
        practice. Instead, integrate threat modeling regularly, like continuous integration for security.


The most effective threat modeling happens in bite-sized chunks,
        closely tied to what your team is working on right now. Spending fifteen
        minutes examining the security implications of a new feature can yield
        more practical value than hours analyzing hypothetical scenarios for
        code that isn’t written yet. These small sessions fit naturally into
        your existing rhythms - perhaps during sprint planning, design
        discussions, or even daily standups.


This âlittle and oftenâ approach brings multiple benefits. Teams
        build confidence gradually, making the practice less daunting. You focus
        on immediate, actionable concerns rather than getting lost in edge
        cases. Most importantly, threat modeling becomes a natural part of how
        your team thinks about and delivers software, rather than a separate
        security activity.


### It's a Team Sport!


Effective threat modeling draws strength from diverse perspectives.
        While a security specialist might spot technical vulnerabilities, a
        product owner could identify business risks, and a developer might see
        implementation challenges. Each viewpoint adds depth to your
        understanding of potential threats.


This doesn't mean you need formal workshops with the entire
        organization. A quick conversation by the team's whiteboard can be just
        as valuable as a structured session. What matters is bringing different
        viewpoints together - whether you're a small team huddled around a
        screen, or collaborating remotely with security experts.


The goal isn't just to find threats - it's to build shared
        understanding. When a team threat models together, they develop a common
        language for discussing security. Developers learn to think like
        attackers, product owners understand security trade-offs, and security
        specialists gain insight into the system's inner workings.


You don't need security expertise to start. Fresh eyes often spot
        risks that experts might miss, and every team member brings valuable
        context about how the system is built and used. The key is creating an
        environment where everyone feels comfortable contributing ideas, whether
        they're seasoned security professionals or completely new to threat
        modeling.


### Navigation from here


Now that we've established the core principles of threat modeling, it's time to put theory into practice. Like any skill worth mastering, threat modeling isn't something you can fully grasp through explanation alone—it requires hands-on experience. The concepts might make sense intellectually, but the real learning happens when you start applying them. In the following sections, we'll walk through practical exercises where you can actively identify threats alongside us, developing the mental frameworks that make effective threat modeling possible.


You'll see, every threat modeling exercise follows the same pattern as seen below in the table, where a set of structured activities,
          each leading to a specified outcome, is conducted within a team. We've also laid out a few different formats for the teams to run these activities.
          For example, as quick sessions at a whiteboard, or as a singular long-ish workshop.
          As with all agile ways of working, the key is finding what works in your team's context.



| Activity | Question | Outcome |
| Explain and explore | What are you building? | A technical diagram |
| Identify threats | What can go wrong? | A list of threats |
| Prioritize and fix | What are you going to do? | Prioritized fixes added to backlog |



The examples in this article are independent from each other. So you can pick and choose the one that which most suits your current needs, or feel free to stick through them all to gain varied perspectives.
          Once you've grasped the gist of it, we highly recommend you pick a suitable format that fits your team's ways of working
          and give it a headstart immediately. Nothing can beat learning from hands-on practice!


## Quick Team Threat Modeling


### Approach and Preparation


A quick whiteboard session within the team provides an accessible
        starting point for threat modeling. Rather than attempting exhaustive
        analysis, these informal 15-30 minute sessions focus on examining
        immediate security implications of features your team is currently
        developing. Let's walk through the steps to conduct one with an example.


Let's say, a software team is working on an order
        management system, and is planning an epic, where store assistants can
        create and modify customer orders. This is a perfect scope for a threat modeling session. It is focused on a single feature with
        clear boundaries.


![](agile-threat-modelling/story-card.png)


The session requires participation from development team members, who can elaborate the technical implementation.
          It's great to get attendance from product owners, who know the business context, and security specialists, who can provide valuable input
          but don't have to be blocked by their unavailability. Anyone involved in building or supporting the feature, such as the testers or
          the business analysts too, should be encouraged to join and contribute their perspective.


The materials needed are straightforward:
          a whiteboard or shared digital canvas, different colored markers for drawing components, data flows, and sticky notes for capturing threats.


Once the team is gathered with these materials, they're ready to 'explain and explore'.


### Explain and Explore


In this stage, the team aims to gain a common understanding of the system from different perspectives before they start to identify threats.
          Typically, the product owner begins the session with an elaboration of the functional flows highlighting the users involved.
          A technical overview from developers follows after with them also capturing the low-level tech diagram on the whiteboard.
          Here might be a good place to put those colored markers to use to clearly classify different internal and external systems and their boundaries as it helps in identifying threats greatly later on.


Once this low-level technical diagram is up, the entities that lead to financial loss, reputation loss, or that results in legal disputes are highlighted as 'assets' on the whiteboard before
          the floor opens for threat modeling.


#### A worked example:


For the order management scope — create and modify orders — the product owner elaborated the functional flows and identified key business assets requiring protection. The flow begins with the customer service executive or the store assistant logging in the web UI, landing on the home page. To modify the order, the user will have to search the order ID from the home page, land on the orders page, and change the details required. To create a new order, the user will have to use the create order page by navigating from the home page menu. The product owner emphasized that customer data and order information are critical business assets that drive revenue and maintain customer trust, particularly as they are covered by GDPR.


The developers walked through the technical components supporting the functional flow.
            They noted an UI component, an authentication service, a customer database, an order service and the orders database.
            They further elaborated the data flows between the components.
            The UI sends the user credentials to the authentication service to verify the user before logging them in,
            and then it calls the order service to perform `/GET`, `/POST`,
            and `/DELETE` operations to view, create and delete orders respectively.
            They also noted the UI component as the least trusted since it's exposed to external access during these discussions.


The carousel below shows how the order management team went about capturing the low-level technical diagram step-by-step on the whiteboard:


Throughout the discussion, the team members were encouraged to point out missing elements or corrections.
          The goal was to ensure everyone understood the accurate representation of how the system worked before diving into threat modeling.


As the next step, they went on to identifying the critical assets that need protection based on the following logical conclusions:

- Order information: A critical asset as tampering them could lead to loss in sales and damaged reputation.
- Customer details: Any exposure to sensitive customer details could result in legal issues under privacy laws.


With this concrete layout of the system and its assets, the team went on to brainstorming threats directly.


### Identify Threats


In the whiteboarding format, we could run the blackhat thinking session as follows:

1. First, distribute the sticky notes and pens to everyone.
2. Take one data flow on the low-level tech diagram to discuss threats.
3. Ask the question, âwhat could go wrong?â while prompting through the STRIDE threat categories.
4. Capture threats, one per sticky, with the mandate that the threat is specific such as âSQL injection from
          Internetâ or âNo encryption of customer dataâ.
5. Place stickies where the threat could occur on the data flow visibly.
6. Keep going until the team runs out of ideas!


Remember, attackers will use the same data flows as legitimate users, but in unexpected ways.
          Even a seemingly simple data flow from an untrusted source can cause significant havoc, and therefore, its essential to cover all the data flows before you end the session.


#### A worked example:


The order management team opened the floor for black hat thinking after identifying the assets. Each team member was
          encouraged to think like a hacker and come up with ways to attack the assets. The STRIDE cards were distributed as a precursor.
            The team went ahead and flushed the board with their ideas freely without debating if something was really a threat or not for now,
            and captured them as stickies along the data flows.


Try coming up with a list of threats based on the system understanding you’ve so far.
          Recall the crux of threat modeling. Start thinking what can go wrong and
          cross-check with the list the team came up with. You may have identified
          more as well. 🙂


The carousel here shows how threats are captured along the data flows on the tech diagram as the team brainstorms:


The team flooded the whiteboard with many threats as stickies on the respective data flows similar to those depicted in the carousel above:



| Spoofed identity | 1. Social engineering tricks could be played on the customer service
                executive or store assistant to get their login credentials, or just shoulder
                surfing or malware might do the trick. They can use it to change the
                orders.
              

                2. The store assistant could forget to log out, and anyone in the store
                could use the logged-in session to change the delivery addresses of existing
                orders (e.g., to their own address) |
| Tampering with inputs | 3. The attacker could get hold of the order service endpoints from any open
                browser session and tamper with orders later, if the endpoints are not
                protected.
              

                4. Code injection could be used while placing an order to hijack customer
                payment details. |
| Repudiation of actions | 5. Developers with production access, when they find out there are no logs
                for their actions, could create bulk orders for their family and friends by
                directly inserting records in the database and triggering other relevant
                processes. |
| Information disclosure | 6. If the database is attacked via a back door, all the information it holds
                will be exposed, when the data is stored in plain text.
              

                7. Stealing passwords from unencrypted logs or other storage would enable
                the attacker to tamper with order data.
              

                8. The customer service executive or store assistant doesn’t have any
                restrictions on their operations—clarifying clear roles and responsibilities may
                be required as they could work with an accomplice to abuse their
                permissions.
              

                9. The /viewOrders endpoint allows any number of records to be returned.
                Once compromised, this endpoint could be used to view all orders. The team made
                a note to at least think of reducing the blast radius. |
| Denial of service | 10. The attacker could perform a Distributed Denial of Service (DDoS) attack and bring down the order
                service once they get hold of the endpoint, leading to loss of sales. |
| Elevation of privileges | 11. If an attacker manages to get hold of the credentials of any developer with admin rights, they could add new users or elevate the privileges of existing
                users to maintain an elevated level of access to the system in the future. They
                could also create, modify, or delete order records without anyone noticing, as
                there are no logs for admin actions. |



**NOTE**: This exercise is intended only to get you familiar with the
          threat modeling steps, not to provide an accurate threat model for an
          order management system.


Later, the team went on to discuss the threats one by one and added their points to each of them. They noticed several design flaws, nuanced
          permission issues and also noted to discuss production privileges for team members.
            Once the discussion delved deeper, they realized most threats seemed critical and that they need to prioritize in order to
          focus on building the right defenses.


### Prioritize and Fix


Time to turn threats into action. For each identified threat,
        evaluate its risk by considering likelihood, exposure, and impact. You
        can also try to come up with a dollar value for the loss of the
        respective asset. That might sound daunting, but you just need to think
        about whether you've seen this threat before, if it's a common pattern
        like those in the OWASP Top 10, and how exposed your system is. Consider
        the worst case scenario, especially when threats might combine to create
        bigger problems.


But we are not done yet. The goal of threat modeling isn't to
        instill paranoia, but to drive improvement. Now that we have identified the top
        threats, we should adopt day-to-day practices to ensure the appropriate defense is built for them.
        Some of the day-to-day practices you could use to embue security into are:

- Add security related acceptance criteria on existing user stories
- Create focused user stories for new security features
- Plan spikes when you need to investigate solutions from a security lens
- Update 'Definition of Done' with security requirements
- Create epics for major security architecture changes


Remember to take a photo of your threat modeling diagram, assign action items to the product owner/tech lead/any team member to get them into the backlog as per one of the above ways.
          Keep it simple and use your normal planning process to implement them. Just tag them as 'security-related' so you can track their progress consciously.


#### A worked example:


The order management team decided to address the threats in the following ways:
            1. adding cross-functional acceptance criteria across all the user stories,
            2. creating new security user stories and
            3. following security by design principles as elaborated here:



| Any unencrypted sensitive information in the logs, transit,              and the database at rest is vulnerable for attacks. | The team decided to address this threat by adding a cross-functional
                acceptance criteria to all of their user stories.
              

                “All sensitive information such as order data, customer data, access
                tokens, and development credentials should be encrypted in logs, in
                transit and in the database.” |
| Unprotected Order service APIs could lead to exposure of             order data. | Although the user has to be logged in to see the orders (is
                authenticated), the team realized there is nothing to stop unauthenticated
                requests direct to the API. This would have been a pretty major flaw if it
                had made it into production! The team had not spotted it before the
                session. They added the following user story so it can be tested
                explicitly as part of sign-off.
              

“GIVEN any API request is sent to the order service
WHEN there is no valid auth token for the current user included in the request
THEN the API request is rejected as unauthorized.”


                This is a critical architecture change as they need to implement a
                mechanism to validate if the auth token is valid by calling the
                authentication service. And the authentication service needs to have a
                mechanism to validate if the request is coming only from a trusted source.
                So they captured it as a separate user story. |
| Login credentials of store assistants and customer service           executives are prone to social engineering attacks. | Given that there are significant consequences to the loss of login
                credentials, the team realized they need to add an epic around
                multi-factor authentication, role based authorization restrictions, time
                based auto-logout from the browser to their backlog. This is a significant
                chunk of scope that would have been missed otherwise leading to
                unrealistic release timelines.
              

                Along with these specific actions, the team staunchly decided to follow
                the principle of least privileges where each team member will only be
                provided the least minimum required access to any and all test and
                production environments, repositories, and other internal tools. |



## Platform focussed threat model workshop


### Approach and Preparation


There are times when security demands a larger, more cross-programme, or
        cross-organizational effort. Security issues often occur at the boundaries
        between systems or teams, where responsibilities overlap and gaps are sometimes
        overlooked. These boundary points, such as infrastructure and deployment
        pipelines, are critical as they often become prime targets for attackers due to
        their high privilege and control over the deployment environment. But when multiple teams are involved,
          it becomes increasingly hard to get a comprehensive view of vulnerabilities across the
        entire architecture.


So it is absolutely essential to involve the right people in such cross-team threat modeling workshops. Participation from platform engineers, application developers, and security specialists is going to be crucial. Involving other roles who closely work in the product development cycle, such as the business analysts/testers, would guarantee a holistic view of risks too.


Here is a preparation kit for such cross team threat modeling workshops:

- **Collaborative tools:** If running the session remotely, use tools like Mural,
          Miro, or Google Docs to diagram and collaborate. Ensure these tools are
          security-approved to handle sensitive information.
- **Set a manageable scope:** Focus the session on critical components, such as
          the CI/CD pipeline, AWS infrastructure, and deployment artifacts. Avoid trying
          to cover the entire system in one session—timebox the scope.
- **Diagram ahead of time:** Consider creating basic diagrams asynchronously
          before the session to save time. Ensure everyone understands the diagrams and
          symbols in advance.
- **Keep the session concise:** Start with 90-minute sessions to allow for
          discussion and learning. Once the team gains experience, shorter, more frequent
          sessions can be held as part of regular sprints.
- **Engagement and facilitation:** Make sure everyone actively contributes,
          especially in remote sessions where it's easier for participants to disengage.
          Use icebreakers or simple security exercises to start the session.
- **Prioritize outcomes:** Refocus the discussions towards identifying actionable security stories as it is the primary outcome of the workshop.
            Prepare for documenting them clearly. Identify action owners to add them to their respective backlogs.
- **Breaks and timing:** Plan for extra breaks to avoid fatigue when remote, and ensure the session finishes on time with clear, concrete
          outcomes.


### Explain and Explore


We have a worked example here where we focus on threat modeling the infrastructure
          and deployment pipelines of the same order management system assuming it is hosted on AWS.
          A cross functional team comprising of platform engineers, application developers, and security
          specialists was gathered to uncover all of the localized and systemic vulnerabilities.


They began the workshop with defining the scope for threat modeling clearly to everyone. They elaborated on the various users of the system:

- Platform engineers, who are responsible for infrastructure management, have privileged access to the AWS Management Console.
- Application developers and testers interact with the CI/CD pipelines and application code.
- End users interact with the application UI and provide sensitive personal and order information while placing orders.


The team then captured the low-level technical diagram showing the CI/CD pipelines, AWS infrastructure components, data flows,
          and the users as seen in the carousel below.


The team moved on to identifying the key assets in their AWS-based delivery pipeline based on the following conclusions:

- AWS Management Console access:  Since it provides powerful capabilities for infrastructure management including IAM configuration,
            any unauthorized changes to core infrastructure could lead to system-wide vulnerabilities and potential outages.
- CI/CD pipeline configurations for both application and infrastructure pipelines:
            Tampering with them could lead to malicious code moving into production, disrupting the business.
- Deployment artifacts such as application code, infrastructure as code for S3 (hosting UI), Lambda (Order service), and Aurora DB:
            They are sensitive IP of the organization and could be stolen, destroyed or tampered with, leading to loss of business.
- Authentication service: Since it allows interaction with the core identity service,
            it can be abused for gaining illegitimate access control to the order management system.
- Order data stored in the Aurora database: Since it stores sensitive business and customer information, it can lead to loss of business reputation when breached.
- Access credentials including AWS access keys, database passwords, and other secrets used throughout the pipeline:
            These can be used for ill intentions like crypto mining leading to financial losses.


With these assets laid on the technical diagram, the team put on their âblack hatâ and started thinking about how an attacker might exploit the
        privileged access points in their AWS environment and the application-level components in their delivery pipeline.


### Identify Threats


The team once again adopted the STRIDE framework to prompt the discussion
        (refer worked example under 'Quick Team Threat Modeling' section above for STRIDE framework elaboration) and captured all their
        ideas as stickies. Here's is the list of threats they identified:



| Spoofed identity | 1. An attacker could use stolen platform engineer credentials to access the AWS
              Management Console and make unauthorized changes to infrastructure.
           

             2. Someone could impersonate an application developer in GitHub to inject
              malicious code into the CI/CD pipeline. |
| Tampering with inputs | 3. An attacker might modify infrastructure-as-code files in the GitHub
              repository to disable security protections.
            

              4. Someone could tamper with source code for the app to include malicious
              code. |
| Repudiation of actions | 5. A platform engineer could make unauthorized changes to AWS configurations
              and later deny their actions due to lack of proper logging in CloudTrail.
            

              6. An application developer could deploy ill-intended code, if there's no audit trail in the CI/CD pipeline. |
| Information disclosure | 7. Misconfigured S3 bucket permissions could expose the UI files and
              potentially sensitive information.
            

              8. Improperly written Lambda functions might leak sensitive order data through
              verbose error messages. |
| Denial of service | 9. An attacker could exploit the autoscaling configuration to trigger
              unnecessary scaling, causing financial damage.
            

              10. Someone could flood the authentication service with requests, preventing
              legitimate users from accessing the system. |
| Elevation of privilege | 11. An application developer could exploit a misconfigured IAM role to gain
              platform engineer level access.
            

              12. An attacker might use a vulnerability in the Lambda function to gain broader
              access to the AWS environment. |



### Prioritize and Fix


The team had to prioritize the threats to identify the right defense measures next. The team chose to vote on threats based on
        their impact this time. For the top threats, they discussed the defense measures as buying secret vaults,
          integrating secret scanners into the pipelines, building two-factor authentications, and buying specific off the shelf security related products.


Apart from the tools, they also identified the need to follow stricter practices such as the 'principle of least privileges' even within the platform team
          and the need to design the infrastructure components with well thought through security policies.
          When they had successfully translated these defense measures as security stories,
          they were able to identify the budget required to purchase the tools, and a plan for internal approvals and implementation, which subsequently
          led to a smoother cross-team collaboration.


## Conclusion


Threat modeling isn't just another security activity - it's a
      transformative practice that helps teams build security thinking into their
      DNA. While automated checks and penetration tests are valuable, they only
      catch known issues. Threat modeling helps teams understand and manage evolving
      cyber risks by making security everyone's responsibility.


Start simple and keep improving. Run retrospectives after a few sessions.
      Ask what worked, what didn't, and adapt. Experiment with different diagrams,
      try domain-specific threat libraries, and connect with the wider threat
      modeling community. Remember - no team has ever found this âtoo hardâ when
      approached step by step.


At minimum, your first session will add concrete security stories to your
      backlog. But the real value comes from building a team that thinks about
      security continuously, and not as an afterthought. Just set aside that first 30
      minutes, get your team together, and start drawing those diagrams.


---
