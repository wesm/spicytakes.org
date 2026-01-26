---
title: "Creating an integrated business and technology strategy"
description: "To make fruitful use of technology, we need to align our technology   thinking with underlying business plans. A technology strategy can drive this   alignment, providing it properly integrates busine"
date: 2023-08-24T00:00:00
tags: ["enterprise architecture", "technical leadership"]
url: https://martinfowler.com/articles/creating-integrated-tech-strategy.html
slug: creating-integrated-tech-strategy
word_count: 4880
---


## Creating an integrated business and technology strategy


How do you create a technology strategy? The conventional approach suggests you start with your current state, determine your future state and build the roadmap to get there. But there is a nuance in that approach that isn't quite right. What often results from following this is a big wish list of all the things that could be done. A powerful technology strategy is as much about what is left out as it is about what is included. Furthermore, technology strategies are often created in isolation, separate from business or product strategies. They are commonly created after the business strategy has been agreed upon. The result being infeasible business strategies which can not be achieved without considerable cost or time.


The challenges with this conventional approach shouldn't be too surprising. After all, if you were to build a health strategy your doctor wouldn't start with a full body scan and tell you how to fix all the symptoms. They would start with your health objectives and the outcomes that you are after, then investigate if your body was capable of achieving your goals, and if not put a remediation plan in place.


I would like to challenge this conventional approach to creating technology strategies, and offer up a different way to create yours. Start with the objectives and outcomes of your organisation. As the organisation considers the different strategic directions that they could traverse to achieve the goals, follow specific lines of inquiry to investigate if your current environment is capable of achieving the proposed strategic direction. The recommendations that result from the different investigations inform the feasibility of that direction, and can be used to formulate a remediation plan. Additionally, because technology is considered as the business strategy is being formed, technology itself can be the driving force behind ideas for new revenue streams. In doing so, your technology strategy will be integrated with the business strategy because it is born together with the business strategy.


### How to use this article


In this article, we look at eleven prevalent strategic directions that organisations traverse, grouped into four broad categories.



| Section | Strategic Direction |
| Growing the business | Expand to complementary products |
| Expand to new markets or regions |
| Expand customer segments |
| Inorganic growth |
| Building a strong foundation | Accelerate time to value with improved efficiency and productivity. |
| Increase customer satisfaction with improved product quality |
| Reduce Cost and Minimize Operational Risk |
| Enhanced competitive advantage by enabling data driven decision making |
| Supporting the people | Culture |
| Internal and back office systems |
| Responding to the ever changing future | Emerging technologies and market trends |



For each strategic direction identified, we provide examples of the lines of inquiry that you can use to investigate how feasible the strategic direction is. We also provide activities that you can do to help answer the lines of inquiry. Many activities span across many lines of inquiry, which allow you to concentrate your efforts into the synthesis of the activity rather than the activity itself.


Here's the format we use for these directions:


### Direction


This is the implication on technology for this strategic direction


#### Key Business Questions

- Any questions that you should ask the business to inform the decisions you make


##### Name of the line of inquiry


Description of the investigation


By selecting the relevant line of inquiry, and using the example questions as a springboard to guide your investigation, you will be one the right tack to creating your own integrated business and technology strategy.


## Growing the business


There are just a few key avenues for business growth:

- Offering complementary products: This involves selling additional products or services to your existing customers. This can be a great way to increase revenue and customer loyalty.
- Expanding into new markets: This involves selling your products or services in new geographic regions or to new customer segments. This can be a great way to grow your business, but it can also be a challenge. It is important to carefully research new markets before expanding into them.
- Attracting new customer segments: This involves identifying new groups of people who could be interested in your products or services. You can do this by conducting market research, analyzing customer data, and identifying trends in your industry.


Organizations typically focus on one or two of these growth strategies at a time, while maintaining and growing their existing business. This is often achieved through organic growth, but at times, the growth is accelerated through mergers and acquisitions, joint ventures or other strategic alliances (ie inorganic growth), which accelerates value realization along one or more of these growth strategies.


### Expand to complementary products


Offering new products to your customers could result in significant changes throughout your systems, from the customer buying experience to shared-service backend systems such as payments and invoicing, distribution and warehouse management, and business reporting. How different the product is from your existing product suite will impact how large the change needs to be.


#### Key Business Questions

- How different are the two product types? Will business processes need to change?
- What business capabilities can be shared across products? Eg Payments, Distribution, Inventory.
- What are undifferentiated capabilities that require significant changes? What products exist on the market today that meet the needs of these undifferentiated capabilities?
- Do you need a single customer view over the products?
- What is the opportunity cost to the existing product with expansion a complementary area? Will investment dilute across the products, degrading the experience of the original product?


##### Product representation


The representation of product types in the code base can have a big effect on how easy it is to add new ones or adjust the categories as new products appear.


##### Changes to business processes


Business processes may not be suited for future products under consideration. As a result, expanding into complementary products might necessitate larger system changes. If the blast radius is wide, how easy is it to make large changes through the system?


##### Shared Capability


As you add complementary products to your offering, you will need to identify which capabilities should be shared across the products and what special treatment is required to shared capabilities. Moving toward a digital platform architecture will allow you to reuse shared capabilities if you expose them via APIs.


### Expand to new markets or regions


As you expand into new geographies, you will be faced with the challenges of running a global platform that needs to cater for regional differences brought about by different local integration's, differing buyer personas, and different processes. Some capabilities will need to be provided in a global platform, others need to have flexibility to allow for these regional differences.


You will also need to contend with government regulation requirements such as GDPR, data sovereignty and regulatory compliance like SOX and APRA. This impacts where your data is processed and where it is stored. It also might introduce new features to handle compliance requirements.


#### Key Business Questions

- What are the differences between the customers in each market?
- What are the regulatory compliance requirements for the new market?
- Do you need to change language, unit formats or factor in time zone conversions? Are there any cultural differences that require UI changes (eg the colour black has different interpretations in Korea than North America)?
- Do you need to introduce new tax calculations or additional reporting requirements?


##### Diversification or Rationalisation of capabilities


As you expand into new geographies, you will be faced with the challenges of running a global platform that needs to cater for regional differences brought about by different local integrations, differing buyer personas, different processes. Some capabilities will need to be provided in a global platform, others need to have flexibility to allow for these regional differences.


##### Regulation and compliance


You may need to contend with government regulation requirements such as GDPR, data sovereignty and regulatory compliance like SOX and APRA. This impacts where your data is processed and where it is stored. It also might introduce new features to handle compliance requirements.


##### Internationalisation


Expanding into new markets may introduce internationalisation changes such as languages, time, money and units. There may also be taxes to consider, and new timezone or daylight saving changes to be factored into.


### Expand customer segments


Ideally, offering your existing product to new customer segments should see little changes through your system. However, at times new customer segments could introduce new operational processes, new customer journeys or new channels experiences. For example, a bank that expands existing credit cards into the sub-prime market introduces completely new operational processes to manage increased risk around debt, regulatory issues due to responsible lending, new way of doing collections (due to higher numbers and earlier interventions) and new marketing strategies. Where as a move from B2C to B2B might mean introducing a new API customer channel. Expanding to more mobile customers might need move to a native mobile experience.


You might want to gather different customer insight as you move, including customer sentiment, adoption and usage so you might add new reporting requirements or alter existing reports to also report on the new segments.


#### Key Business Questions

- What are the differences between the customers segments?
- What operational process changes are required to support the new customer segment?
- Are you moving between B2C and B2B?
- What are the different expectations of interaction for the new customer segment?


##### Customer journey changes


A new customer base might need new customer experiences. If their customer journey differs from your existing customer journey, you will need to make changes to your system


##### Channel strategy


A new customer experience might also open the need for different customer channels. Moving from a B2C to a B2B offering may provide you with an opportunity to streamline your experience behind customer-centric APIs. Expanding into partner networks will require integration into the networks.


### Inorganic growth


Inorganic growth through mergers and acquisitions (M&A), joint ventures, or other strategic alliances is often a faster way to accelerate the growth of a business along the three aforementioned axes. It in itself drives a different line of investigation.


#### Key Business Questions

- What were the value drivers for the acquisition? How are you protecting these?
- What is the long term view of the acquisition - are you merging it into the business over time, or keeping it separate?
- What are the long term plans for the acquisition? Will you divest this asset once your company grows?


##### Independently run businesses


This is the case where the acquired businesses continues to run independently to the organisation. This might be the first phase of the acquisition, or it might be to enable an easy sale of the asset in the future. While the technology organisations and the systems remain separate, there is value in loose-coupling (e.g. via restful APIs) to integrate the two running systems.


##### Tight integration independently run


This is the case where you have two businesses running independently but you want tight integration between the two so that you can amplify the customer value created.


##### Complete merge


This is the case where the acquired systems will be first class systems within the ecosystem. This results in the rationalisation and consolidation of systems, migration of systems into the one system, integration into the runtime system, and merge of operational systems for observability and monitoring. It might also introduce different data archiving mechanisms


## Building a strong foundation


Any business that wants to grow needs to be built on strong and stable foundations. Oftentimes, technology strategies focus singularly on the ways that technology leaders can improve and continue to build a strong foundation, and so this section may feel familiar to technical readers. However for an integrated business and technology strategy to be successful, business leaders also need to understand how this focus will enable and support the business to grow. It is important that the improvements to the engineering organisation and the platforms they look after align with the themes that resonate with the rest of the organisation. These themes are:

- Accelerate time to value with improved efficiency and productivity. A good technology foundation can help businesses automate tasks, streamline processes, and improve communication. This can lead to significant improvements in efficiency and productivity, which can free up time and resources for other areas of the business.
- Increased customer satisfaction with improved product quality. A strong technology foundation can help businesses provide better customer service, offer more personalized experiences, and make it easier for customers to do business with them. This can lead to increased customer satisfaction, which can lead to increased sales and revenue.
- Reduce cost and minimize operational risk. A good technology foundation looks to reduce costs of the technology systems if the business need is to contain costs. Effective operational risk management helps companies prevent or minimize losses and safeguard their operations and reputation.
- Enhanced competitive advantage by enabling data driven decision making. A strong technology foundation can help businesses stay ahead of the competition by giving them access to new technologies, data, and insights. This can help them develop new products and services, improve their marketing and sales efforts, and gain a competitive edge in the market.


### Accelerate time to value with improved efficiency and productivity.


Accelerating time to value reduces the time it takes to deliver measurable benefits or achieve desired outcomes from a particular initiative, product, or project. It focuses on maximizing the efficiency and effectiveness of the value creation process. Three areas that negatively impact time to value include the inability to easily and confidently change code, poor developer experience and waste within the delivery process.


#### Key Business Questions

- Is the current pace of delivery keeping up with the pace of customer demand?


##### Code quality


Well written and structured code, supported by appropriate test coverage is easy to modify to new feature requests. Teams can go at a rapid pace when they are confident that changes they make will not inadvertently introduce hidden defects.


##### Developer experience


[Developer Experience](https://martinfowler.com/articles/developer-effectiveness.html) and experience is key to engineering excellence leading to desired business outcomes and organisational performance. Developer experience (DX) encompasses all aspects of a developer’s interaction with an organisation, its tools and systems. Engineering platforms, that provide self-service capabilities help automate and streamline every stage of software development journey from ideation to go-live and collecting customer feedback leading to excellent developer experience


##### Delivery Process


Remove the waste that exists within your delivery process. The waste is negatively affecting your speed to market. Waste may be in handoffs between groups, approval boards that slow down continuous releases, or rework in the system.


### Increase customer satisfaction with improved product quality


Improving your product quality increases customer's satisfaction and can have a big impact on customer retention. Product quality is impacted by the build quality itself, but is also impacted by performance issues, technical debt and complexity which results in increased reliance on call centres. There are often dangerous parts of systems that teams are reluctant to change due to the technical debt and lack of a safety net around it. If any feature development needs to be done in those areas, it will be slower and deployment will be riskier unless you tackle that debt. Maybe now is the time.


#### Key Business Questions

- Why do customers stop using your product? What are customer retention rates?


##### Address build quality issues


Unfortunately, IT systems have notoriously been buggy which impacts the overall product quality. Modern agile software delivery practices have significantly increased the build quality of modern codebases. Nevertheless, systems continue to have areas which have defects, or are difficult and complicated to understand which makes changes in these parts risky.


##### System performance under increased load


It will increase the number of site visits to your website and increase your customer load. How capable is your system today of performing with the anticipated new load?
                Look for signs that your system is struggling under regular days as well as irregular events such as Black Friday sales. Identifying the breakpoints on these days gives you clues to what needs to be addressed for any additional load.


##### Call center complaints


To uncover areas for improving product quality that will make the biggest impact on your customers, consult your customer support team. They often hold valuable insights into where your systems are falling short of customer expectations. However, be cautious of survivorship bias, similar to the WW2 planes returning with bullet holes - it's important to consider not only customer complaints, but also where and why customers drop out of your funnel to get a comprehensive understanding of the issues.


##### Address technical debt


Technical debt is a metaphor for choosing an easy solution now that will make it harder to make changes or add new features later. It is often incurred when developers choose to use quick hacks or workarounds instead of taking the time to write clean, well-organized code. The technical debt that is building up in your system can have significant impact on the quality of the product.


### Reduce Cost and Minimize Operational Risk


Operational risk refers to the potential loss resulting from internal process failures, system issues, or external events. This includes errors, fraud, system failures, and other disruptions that can impact business operations and financial performance. Examples include cyber-attacks, employee errors, and supply chain disruptions, which can affect a company's reputation and regulatory compliance. Effective operational risk management helps companies prevent or minimize losses and safeguard their operations and reputation.


#### Key Business Questions

- What are the biggest risks relating to technology on the Risk Register?


##### Cloud cost optimization


Cloud is increasingly a major component of technology budgets. In a lot of cases, actual cloud costs are exceeding budgets and the savings that helped rationalize a move to the cloud are not materializing. Understanding a business's cloud spend and sizing it appropriately to reduce waste and optimize the rates paid requires cooperation across the whole organization, with finance, product and engineering teams working together to ensure that the cloud spend is in proportion to the value the assets bring in.


##### Data governance


Digital operation gives us the opportunity to capture data from  every aspect of the business, together with the opportunity to analyze this data to better understand how everything works. But this data also presents a risk, as privacy violations can undermine the benefits.


##### End of life software


The use of products or systems which have reached or are approaching the end of life (EOL) agreements with the supplier poses significant risks to an organization. The risks include security vulnerabilities for products that no longer receive security patches from the vendor, compliance and regulatory non-compliance which may result from using unsupported versions, business disruption from failure of the systems, data loss and recovery challenges, and increased concentration risk if the vendor goes out of business. To mitigate these risks, organizations must adopt proactive end-of-life management strategies. This includes regularly evaluating the product lifecycle of their technology stack, planning for timely upgrades and replacements, and ensuring compatibility with future systems.


##### Supply chain disruption


The SolarWinds hack, also known as the Sunburst hack, was a major cyberattack that occurred in 2020. The hackers targeted SolarWinds, a Texas-based company that provides IT management software to businesses and governments around the world. The hackers were able to insert malicious code into SolarWinds' Orion software, which is used by thousands of customers. This allowed the hackers to gain access to the networks of these customers, including government agencies, Fortune 500 companies, and think tanks.
The SolarWinds hack was a major security breach, and it has raised concerns about the security of supply chains. SolarWinds is a trusted supplier of software to businesses and governments, and the fact that it was hacked shows that no organization is immune to cyberattacks. How would your organisation respond to similar disruptions in the supply chain?


### Enhanced competitive advantage by enabling data driven decision making


Providing better access to data insights is a way to support internal staff in making data-based decisions. While many people claim to make data-driven decisions, in reality, they often make a decision first and then look for data to support their choice. This is what many data platforms and âbusiness intelligenceâ systems focus on. However, true data-driven decision-making involves sensing what is happening in your environment and using that information to understand what decisions need to be made. A sound technology strategy should prioritize creating meaningful decision-making capabilities within your organization through a robust data platform. This can be achieved by embedding intelligence and machine learning into every decision, customer touchpoint, service, and product you provide. This approach can lead to improved decision-making, streamlined operations, and better customer experiences based on new data-driven insights that go beyond intuition and gut feelings.


##### Enabling easy data access


Data Platforms enable data consumers to easily discover and access data they need in the right format at the right time, for effective decision-making and creating data solutions using the right set of tools to create maximum business value.


## Supporting the people


Technology leaders play a vital role in supporting the organisation and its employees by leveraging technology to improve business processes, enabling data-driven decision making that is required to drive innovation, efficiency, and strategic growth.


> Contrary to popular belief, digital transformation is less about technology, and more about people. You can pretty much buy any technology, but your ability to adapt to an even more digital future depends on developing the next generation of skills1
> 1: see [Digital Transformation Is About Talent, Not Technology](https://hbr.org/2020/05/digital-transformation-is-about-talent-not-technology)


Having a robust digital talent strategy is a competitive advantage in today’s fiercely competitive market. This enables businesses to have the right talent and have the right competencies to meet current and future demand to meet business goals or to stay on track for digital transformation aspirations.


### Culture


You might be thinking that culture is too touchy feely to go into a technology strategy. However,
                according to research by DevOps Research and Assessment (DORA),
                “organizational culture that is high-trust and emphasizes information
                flow is predictive of software delivery performance and organizational
                performance in technology”. The DORA research has also been backed up 
                with further research from [Google's Project Aristotle](https://rework.withgoogle.com/print/guides/5721312655835136/)


The DORA report cited research by sociologist Dr. Ron Westrum.
                Westrum's research noted that such a culture influences the way
                information flows through an organization. Westrum provides three
                characteristics of good information:

- It provides answers to the questions that the receiver needs answered.
- It is timely.
- It is presented in such a way that the receiver can use it effectively.


DORA research shows that changing the way people work changes
                culture; this is echoed in the work of John Shook, who spoke of his
                experiences in transforming culture: âThe way to change culture is not
                to first change how people think, but instead to start by changing how
                people behave—what they do.â DORA group [provides
                useful information](https://cloud.google.com/architecture/devops/devops-culture-westrum-organizational-culture) on how to implement better organizational
                culture.


##### Leadership


Leadership plays a pivotal role in establishing and shaping organizational culture. They set the tone and values, serve as role models, and communicate the organization's vision and values. By making hiring and promotion decisions aligned with cultural fit, empowering and holding employees accountable, recognizing and rewarding cultural alignment, and adapting the culture to changes, leaders foster a strong and sustainable culture. Their long-term vision and consistent efforts to embed cultural elements influence employee behavior and ultimately impact the organization's performance.


##### Knowledge sharing and learning


Knowledge sharing can take many forms, from wiki or confluence
                pages to lunch-and-learn weekly meetups. Human based knowledge systems
                often have key go-to people that know where all the information lives.
                A good technology strategy should outline a plan to replicate these
                people, break down any information silos that exist and provide the
                tooling and mechanism that is necessary to enable the right
                information to be shared to the right people, and at the right
                time.


##### Employer brand - attract and retain talent


Employer brand refers to the reputation and perception of an organization as an employer. It represents the collective attributes, values, and culture that the organization exhibits to attract and retain talent. Employer brand allows you to attract and retain top talent, build trust and credibility and support business goals.  It creates a positive image of the organization as an employer and helps in attracting the right people who align with the company's values and goals.


### Internal and back office systems


Technology leaders usually develop and support internal and back office systems. These systems directly contribute to the pleasure and satisfaction that workers derive from their job. Internal and back office systems or processes should offer employees a frictionless experience. But are your internal facing systems serving their purpose? We've all used back office systems that made us feel like we are running in treacle. Without focus on these systems for their delightful user experience, it's little wonder that CRM, ERM and timesheet systems feel like they are stuck in the 90s.


#### Key Business Questions

- What systems are key to the running of your business?
- What is lacking from the systems that your teams use?


##### Streamlining Business Processes


Technology can play an important role streamlining business processes, identifying and eliminating unnecessary steps or activities in a process in order to make it more efficient and effective. The goal of streamlining processes is to reduce waste, improve efficiency, and increase productivity.


##### User Sentiment


For any product, it's important to understand how your customers
            view the offering. The same kind of customer analysis needs to be
            made on internal systems, so that we can accurately judge how to
            better improve our employee's ability to help the enterprise and to
            identify impediments so that we can remove them.


## Responding to the ever changing future


In today's dynamic and fast-evolving business landscape, organisations need to proactively respond to changes by closely monitoring market trends and emerging technologies. By keeping a keen eye on the shifts in customer preferences, industry dynamics, and market demands, businesses can identify new opportunities and potential threats. Understanding emerging technologies and their potential impact on their industry allows organisations to stay ahead of the competition and foster a culture of innovation. Armed with this knowledge, they can develop robust strategic plans that encompass adaptation to market trends and the integration of cutting-edge technologies. This proactive approach empowers them to be agile in their decision-making, anticipate future challenges, and capitalize on new opportunities, ensuring their relevance and success in an ever-changing marketplace.


### Emerging technologies and market trends


A technology strategy should also consider a survey of the emerging
        technologies, market trends and broader economical, social and political
        changes which may impact the organization, its customers or its
        employees.


#### Key Business Questions

- What does the role of emerging technologies play on our industry or within our company
- What are the main trends that will effect our industry in the near term?
- What competitors are rising in market share and prominence and how do they differentiate from us?
- What is happening in the social, economical and political environment we live in?


##### Emerging technologies


In the rapidly evolving digital era, emerging technologies are profoundly reshaping industries, upending conventional business models, and offering unprecedented prospects for growth and innovation. Being at the forefront of emerging technologies empowers you to leverage their potential, leading to transformative changes that revolutionize how we live, work, and engage with the world.


##### Market trend analysis


Market trend analysis is the process of studying changes and patterns in a specific market over time. It involves collecting and analyzing data from various sources to identify significant trends and shifts that impact the market, such as consumer behavior, technological advancements, economic conditions, and competitor activities. By segmenting the market and forecasting future trends, businesses can make strategic decisions, adapt to changing market dynamics, and take advantage of emerging opportunities to remain competitive and successful in their industries.


##### Broader economic, social and political changes


You should also consider the broader economic, social and political
        changes that will impact you and your customers. Broader social, economic, and political changes encompass significant shifts that impact society at large. These changes are multifaceted and range from technological advancements like automation and digitization to demographic shifts, such as urbanization and aging populations. Additionally, the increasing awareness of climate change and income inequality, along with the effects of globalization and political instability, play pivotal roles in shaping the world we live in. Moreover, public health crises, changing work patterns, the digitization of information, and evolving social norms all contribute to the complex landscape of these transformative changes. Understanding and adapting to these interconnected trends are essential for individuals, businesses, and governments to thrive in a constantly evolving global environment.


---
