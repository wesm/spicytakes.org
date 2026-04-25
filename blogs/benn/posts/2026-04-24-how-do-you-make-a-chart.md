---
title: "How do you make a chart?"
subtitle: "Answer like your job depends on it."
date: 2026-04-24T18:37:22+00:00
url: https://benn.substack.com/p/how-do-you-make-a-chart
slug: how-do-you-make-a-chart
word_count: 1874
---


![name a chart!](https://substackcdn.com/image/fetch/$s_!oyV3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fa30641-fc68-4e7b-b4ff-a434c760c142_836x460.jpeg)

*Draw a chart! Draw any chart!*


How do you make a chart, in the age of artificial intelligence? You have many choices:

1. Give an Excel file to an image model likeNano BananaorChatGPT Images, and tell it to make a picture. Have it read your data, squint at some imagined piece of paper in its head, and draw a bar chart, of the Charlotte Hornets 2025-26 season, in a nostalgic 1990s aesthetic.1
2. Make your chart directly in Excel. UseAI in Excel™, powered by Microsoft 365™ Copilot™. Or, other modelscan use computers now; tell them to take over your computer, open Excel, click “New chart,” and flip through all of Excel’s menus and dropdowns.2
3. Ask an AI to use a simple charting library to create the chart with code. There are so many: Matplotlib, Plotly, Seaborn, ggplot2, Bokeh, Highcharts, Observable, Vega, Vega-Lite, Apache ECharts, Google Charts, Fusioncharts, ZingChart, Chart.js,I could do this forever. The robots will create your chart with a few simple configurations, like defining which fields go on which axis, and let the charting library handle the exact details.3
4. Ask it to make the chart using a low-level charting framework liked3, “the JavaScript library for bespoke data visualization.” In other charting libraries, there are concepts like “bar charts” and “legends.” In d3, there are concepts like “rectangles” and “text.” It’s a collection of visual Lego bricks: Most of the bricks are shaped like things that might be useful for making charts, but you can make anything with the bricks.4
5. Make the chart using native Javascript. Javascript is the language that people use to createanywebsite—YouTube, Wordle, thehomepage for the originalSpace Jam. If Highcharts lets you draw charts, and d3 lets you draw shapes, Javascript lets you drawanything.5
6. Make the chart inC. C is a general-purpose programming language for creating programs and operating systems. If AI can do anything, why should it use Excel, a browser, or even Windows? That is generic software. It should create a program designed for making exactly the right chart. It should design anoperating systemdesigned for making exactly the right chart.6
7. Make the chart in a bespoke programming language. Design the language for exactly the chart you want. Is the languageTuring complete? It does not matter. It only needs to be “a bar chart, of the Charlotte Hornets 2025-26 season, in a nostalgic 1990s aesthetic” complete.7
8. Grow corn.Grow corn to feed the workers, who build the mine, which digs up the silicon, which goes into the semiconductor fabrication plant, which manufactures the chips, which assembles the computers, that create the operating system, that hosts the program, that draws the chart. Rebuild the entire global economy, literally from the ground up, to make the perfect chart.8


One way to think about this question is that it is dumb. Nobody needs to start a farm to make one chart. Nobody needs to even build a custom app to make a chart. There are a million charting programs out there already; just pick one, and tell a robot to make the chart. Use Excel;it will be there forever.


Another way to think about this question, though, is that all of our jobs andmoneydepend on its answer. A lot of the world—and nearly all of Silicon Valley—exists somewhere between “a polished software application like Excel making a complex task possible in a few clicks” and “grow corn.” There are conglomerates and research labs that design and maintain foundational programming languages; there are huge corporations like Apple and Microsoft that build operating systems that can run software programs; there are thousands of companies that build technical infrastructure like databases that runs in those operating systems; there are even more companies that build consumer products like Excel that make those technical applications accessible to the masses. Everything that is done on a computer passes through an entire supply chain of software, a supply chain that supports thousands of businesses and millions of jobs.


But, you know, AI. The faster and more capable the models get, the theory goes, the less of the supply chain needs to exist. AI can work directly with technical infrastructure; it can build its own software; it can generate charts. And the question—about charts, sure, but aboutevery software product and software company—is,where is the line?How far down the list can they go?


Here’s one answer:MotherDuckis a cloud data warehouse.9It is a technical application that is typically one step removed from charts, and from the business people who want to look at charts. Engineers set up MotherDuck and fill it with data; they connect it to a tool like Excel, or to a drag-and-drop business intelligence software likeOmni; business people use Excel or Omni or whatever to make charts of the data in MotherDuck.


But, you know, again, AI. So, two months ago, MotherDuck releasedDives:


> Dives are interactive visualizations you create with natural language, directly on top of your data in MotherDuck. Ask a question to your AI agent, and MotherDuck generates a persistent, interactive component that lives in your workspace alongside your SQL.


How does Dives build visualizations? With robots thatwrite JavaScript, the programming language that can create any website:


> [Instead ofclicking through a UI or writing visualization code,] just describe what you need. Interactive visualizations from a single prompt, built by your AI agents, living in your MotherDuck workspace. And the beauty of it: Dives is Javascript code. You can build anything you want, with any interactivity you’d like.


It’s the future of analytics, some say. There is no more visualization software. That’s what gets replaced. Don’t buy Tableau; instead, open Claude Code or Codex, andask it to make a custom dashboardin JavaScript or Python. And that’s better than using dedicated charting tool, because with JavaScript or Python,you can build anything you want:


> Fabi’s Python dashboards are faster to build (minutes vs weeks), more flexible for advanced analysis and custom visualizations, and fully transparent so you can see and edit the underlying code.


The idea has even leaked into the LLMs themselves. In a later post, MotherDuckasked Claudewhat would happen to BI tools as AI continued to advance, and it said the same thing:


> LLMs already draw better charts than Tableau from a simple prompt. … The “drag-and-drop dashboard” becomes a curiosity, like a fax machine with a particularly nice interface.


Maybe; I don’t know. If you’ve ever tried to create a chart from scratch, or even with a visualization library, you know the Rubik’s’ cube of frustrations: Overlapping axis labels; misplaced legends; colors that collide with one another; you move one thing to fix a problem over here and it creates a new problem over there. Software isn’t just a convenient shorthand for doing something; itsolves the very hard problemsthat you don’t realize exist until you have them. In that telling, while the entire software industry might pivot toward building user interfaces that LLMs can work with, software itself would remain as useful as ever, and the supply chain would remain intact.


Or, maybe LLMs really do get good enough towork through those edge cases and annoyances. But of course, if they can do that—why would they stop with making visualizations? If they can work around all of the headaches that Tableau has spent twenty years solving, could they not also work around the headaches that make it hard to host those visualizations? Could they not build a better database? Sure, the latter twoseemharder, but how many things did we once say were too hard for an LLM, and soon realize were not?


There are obvious reasons why an LLM probably shouldn’t grow corn. Nor, probably should it try to rebuild every piece of software. But how do you draw the line?


---


# Big vibes


Or, maybe the answer is tonot make a chart at all?


> …the future of business intelligence isn’t a better dashboard.A support leader at one of Omni’s customers went through 75 pages of conversation with an AI to identify 10 categories of rep mistakes. The system read support logs, cited specific examples per rep, & suggested concrete changes. Not just a dashboard.


We’ve talked about this anumberoftimesbefore: The real future of analytics might not be analytics, but vibes:


> If AI is good at anything, it is good at interpreting the vibes. It is good at aggregating massive amounts of text—and increasingly, of video and audio—into its approximate average. Give it your support tickets and customer communications, andask it questions about what it read. Don’t classify and categorize images;just ask an AI model what it thinks it sees. … Ask it for the vibes.


That’s another thing the vibes—there are no edge cases in how somethingfeels. There are no overlapping axes, or misplaced legends, or Rubik’s cubes full of frustrations. The vibes are much less of headache than the analytics.


---


# Cursor


See, maybe SpaceX isalsoa normal startup after all:

1. They started with big, fun ambitions: big rockets; colonize Mars; technology to save humanity; buildrobots; buyTwitter; buyTiktok?
2. They raised anabsolutely titanicamount of money.
3. They changed their mind. They are now pivoting to the enterprise.Time for some realism—they now want a robot thatmakes software and does business:Though [SpaceX CEO Elon Musk] once forecast that humans wouldtake off for Mars as early as 2024, he has de-emphasized reaching the planet.Instead, SpaceX on Tuesday said it hadstruck a dealwith the artificial intelligence start-upCursorthat could result in its acquiring the young company for $60 billion. …Mr. Musk appears eager to push SpaceX further into A.I. In the deal with Cursor announced Tuesday, SpaceX said the combination with the young A.I. company, which makes code-writing software, would “allow us to build the world’s most useful” A.I. models.


On one hand, the deal makesan uncanny amount of sense: SpaceX has aton of big computersand nobody to use them; Cursor has a bunch of customers and training data, and not nearly enough big computers.


On the other hand, man, what? In preparation for a huge IPO, SpaceX—a rocket company that is tryingto build a city on the moon—is marketing its huge ambitions, its technological prowess, and its enormous financial potential by…buying a SaaS product that helps people build websites. The literal rocket ship company is trying to prove to investors that it’s a corporate rocket ship by buying an app.


I don’t know AI coding agents are a technological singularity, but they are definitely the attention singularity.

[1](#footnote-anchor-1)

I mean, this is impressive, and thatlast losswas bad,but it wasn’tthatbad.

[2](#footnote-anchor-2)

Gemini was boring, andmean.

[3](#footnote-anchor-3)

ChatGPTignored every win, and Opus 4.7absolutely lost its mind.

[4](#footnote-anchor-4)

“The stinker,” saysClaude. “Fat outlines,” saysChatGPT.

[5](#footnote-anchor-5)

ChatGPT nowsays it explicitly: “Wins disappear into the background.” And yes, Claude, we knowit was the L of the season. Everyone knows it was the L of the season.

[6](#footnote-anchor-6)

Codex made an app. Itdoesn’t do much, but honestly, “final buzzer”is a pretty clever pun.

[7](#footnote-anchor-7)

First, yes, sure, if it’s a language that only does one thing, is that alanguage? Second, Codex made Starter, “a tiny domain-specific language for making loud sports-result posters from a CSV file.” Here is what Starterlooks like. Here is what Startermakes.

[8](#footnote-anchor-8)

There is whole lot going onhere.

[9](#footnote-anchor-9)

Disclosure: I’m asmall personal investorin MotherDuck.
