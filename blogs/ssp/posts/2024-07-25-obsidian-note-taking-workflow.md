---
title: "My Obsidian Note-Taking Workflow07-25"
date: 2024-07-25
url: https://www.ssp.sh/blog/obsidian-note-taking-workflow/
slug: obsidian-note-taking-workflow
word_count: 2974
---

![My Obsidian Note-Taking Workflow](https://www.ssp.sh/blog/obsidian-note-taking-workflow/featured-image.jpg)

Contents
ð¶
Featured on Hacker News.
[Read the comments](https://news.ycombinator.com/item?id=41092928)

Iâm currently on vacation, and it is time to dive into one of my favorite topics:Â **knowledge workflow management**. As Iâm sharing most of [my notes](https://brain.ssp.sh/)Â and even [my book](https://dedp.online) publicly, it might be interesting to see my knowledge management workflow. I’m also journaling, reflecting, and connecting all my notes, sparking most of my insights into my sharing. All of it happens in plain text in my note-taking app. This article will detail my [Obsidian](http://ssp.sh/brain/obsidian) workflow, which many of you have requested. That’s why I’m sharing some more details here.


As you might guess, I have a very dedicated workflow. Sometimes, I even get jokes about how organized or methodical I am. I’m not shy about spreading the word about why you should use a second brain and store all information in a central place.


But once at a time. Besides my deep dives, I wrote aboutÂ [Personal Knowledge Management Workflow for a Deeper Life](https://www.ssp.sh/blog/pkm-workflow-for-a-deeper-life/),Â [My Vim-verse](https://www.ssp.sh/blog/my-vimverse/), orÂ [Why Vim Is More Than Just An Editor](http://ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/); this article focuses more on the Obsidian and my workflow and how it ultimately led me to more clarity and genuine insights. Key Takeaways are why I use Obsidian for note-taking, the role of Markdown in my note management and essential plugins I use.

Check out the YouTube Video
Update: I added a
[YouTube Video](https://youtu.be/myHKHM2mIis)
to showcase my Obsidian workflow visually. If you prefer watching over reading, check it out below. You can also check out the shorter five-minute version of
[Vim with Obsidian (No Mouse ð±ï¸)](https://youtu.be/LQasaw4MkqE?si=UKRpxwnzGKFHVPlN)
.
Itâs Not about the Tool
Obsidian is the tool I use, and I will share a bit more about it. Itâs not about which tool you use, as you can achieve the same with any other.

## My Workflow for a Deeper Life


Everything in my workflow and note-taking approach isÂ [Plaintext Files](http://ssp.sh/brain/plaintext-files)Â files with some formatting sugar calledÂ [Markdown](http://ssp.sh/brain/markdown). I use Vim-motions heavily to make creating notes second nature for me (on a computer, at least). Everything is optimized to improve my workflow and with the lowest barriers possible.


At a high level, weâll talk about how my workflow ultimately provides me a â[Deeper Life](http://ssp.sh/brain/deep-life)â, which Iâd like to call it, as it is less about business or any other specific use cases but all about your life andÂ [Second Brain](http://ssp.sh/brain/second-brain). Although it will eventually lead to better careers, studies, and life too, as I have noticed for myself over the years, therefore the termÂ deep life.


## My Note-Taking Path


Again, all this didnât happen in a couple of months or a year. This happened over many years, even the over two decades of my professional career, starting withÂ [Microsoft OneNote](http://ssp.sh/blog/tools-i-use-onenote-part-ii/)Â and constantly improving file structures on my computer.


To give you some perspective, below you see how my path with note-taking proceeded to this day:

1. Forgetting everything
2. Taking scattered and very detailed notes on multiple devices, apps, and paper
3. Improving during my studies with OneNote, where notes related to work or study go into separate notebooks.
4. Starting to create a personal notebook for travels, research related outside of work, etc.  But there is still a lot of confusion about:
5. Switching toÂ **Obsidian**Â with a new open format and a different spirit and capabilities.
6. Starting myÂ **[Second Brain](http://ssp.sh/brain/second-brain)**
7. Start usingÂ [Vim](http://ssp.sh/brain/vim)Â and, more importantly, itsÂ **[motions](http://ssp.sh/brain/vim-language-and-motions)**Â for fast and effortless note-taking.
8. Sharing them publicly withÂ [Quartz](http://ssp.sh/brain/quartz-publish-obsidian-vault).
9. Writing a [book](https://www.dedp.online/) with [MdBook](https://github.com/rust-lang/mdBook) on plain Markdown, sharing as I go as website.


## Why I Choose Obsidian?


Iâve written aboutÂ [how to take notes](https://ssp.sh/blog/how-to-take-notes-in-2021/)Â and why I chose Obsidian over apps like Notion, Joplin, and Roam. The main reasons at that time were to have an open file format, coming from OneNote where the file format was proprietary, feeling the pain to getÂ *my*Â notes out of that system (exporting it to HTML and converting them to Markdown, …, see my scripts in [Python](https://github.com/sspaeti/second-brain-public/blob/hugo/utils/find-publish-notes.py), [Rust](https://github.com/sspaeti/second-brain-public/blob/hugo/utils/obsidian-quartz/src/main.rs)), that was very important to me. I also mentioned how collaborating was a non-requirement for me.


If I reflect, Iâm super happy about these choices, and Iâm still confident, to this day, that my notes will forever grow with me. Even after Obsidian might die one day, as they are just simple text files with Markdown, they can be opened by any text editor in the past and future.


### Why Would I Still Choose It Today?


Today, Iâd add the ability toÂ **find knowledge whenever needed**. Confidentially storing some ideas or notes, knowing Iâll see them when needed, even years later.


The ability toÂ **search based on a thought**. E.g., I forgot the note or a place, but I know the person who told me, so I searched for the person and found the backlink to the place. As this is so close to how our brains work, this works so well for me, and I rarely search through the folder structure, except for recurring âarea notesâ based on theÂ [PARA](http://ssp.sh/brain/para)Â method, which are constant notes such as family, house, health, etc.


**PARA andÂ [Zettelkasten](http://ssp.sh/brain/zettelkasten)**Â are two more key players in my knowledge workflow. PARA that I have a minimal file structure that makes sense to me (it was already almost the one I optimized for myself over the year, but it added more sense and explained it more sophisticated). And the Zettelkasten way, that I do not need to spend a thought on where to store my note as one note can potentially belong to many different areas of my life, work, studies, therefore spending time where to store so I can find it later, took a lot of effort. But nowadays, I create a note in my Zettelkasten, which I can easily find with the above-mentioned search.


If I canât find a note with one search or itâs missing a keyword, I add that searched keyword to the note, and Obsidian will update all links automatically. Next time I search and use the same initial keyword, I will find that note immediately. Also, for notes that appear highly searched, I will make them easier to search by updating them with more connections or adding more keywords to the title to find them immediately.


Moreover, Obsidian gives me the power toÂ **use [Vim motions](http://ssp.sh/brain/vim-language-and-motions)**. This means I can use the shortcuts and mouse-free navigation that I learned and optimize it for coding and writing, spending almost no effort in clicking around and navigating through my notes. Obsidian also makes it super easy to add shortcuts to any of the available commands. I am optimizing Obsidian-specific shortcuts and integrating them into my existing workflow.


Lastly, everything is based onÂ [Plaintext Files](http://ssp.sh/brain/plaintext-files)Â andÂ [Local First](http://ssp.sh/brain/plaintext-files), with an additional hidden folder calledÂ `.obsidian`, which is used for Obsidian to store some metadata.


## How I Create Initial Notes (Templates)


It always starts with a template. WithÂ `cmd+t`Â on Mac, I choose a Template. My default isÂ `ð³ Permanent Note Template`, which contains the following content:



| `1
2
3
4
5
6
7
` | `# <% tp.file.title %>

---
Origin: 
References: 
Tags: #ð/ð» 
Created <WIKILINK_TEMP><% tp.date.now("YYYY-MM-DD") %></WIKILINK_TEMP>
` |



It will automatically file the title and the created date. I will then add theÂ `Origin`Â so I know what triggered this note. I will addÂ `References`Â if they connect to an existing note that immediately comes to mind. Usually, I leave this empty in the beginning but add at least one link withÂ `[[]]`Â within the text.


For example, I will explain the term or the note I started, and add some rapid thought that might started that note.


Letâs say I write about a new open-source data ingestion tool. I will say something like, `This is similar toÂ <a href="https://ssp.sh/brain/airbyte/">Airbyte</a>`, and add the ingestions tool and its definition and features to the text. Usually, I will also add aÂ [Map of Content (MOC)](http://ssp.sh/brain/map-of-content-moc)Â with all tools listed (e.g., [BI-Tools](https://ssp.sh/brain/bi-tools)), but if not, I can also find it via the backlink of Airbyte in case I need to remember the name of it. As Airbyte is the most significant open-source ingestion tool, this will always come to mind, and I know I have connected it to it.


Tags can have these different levels:

- `ð¬`Â Start any note, idea, something I read, or anything that comes to mind. Just some fleeting notes. This can also be deleted after a while
- `ð/ð»`Â I worked on it a bit. I added many fleeting notes, brainstormed, elaborated a bit, and made some references.
- `ð/ð`Â literature notes written and not ready for theÂ [Permanent Notes](http://ssp.sh/brain/permanent-notes)Â /Â Evergreen Notes. Still,Â [Literature Notes](http://ssp.sh/brain/literature-notes)Â are formulated in whole sentences and have already worked, or Iâm just happy with the content.
- `ð/ð³`Â Evergreen / Permanent Notes. These long-running notes will end up inÂ [Zettelkasten](http://ssp.sh/brain/zettelkasten)Â core with my own words. Here, I separated the literature notes into different ideas to follow the zettelkasten principle and link them together.


This way, I can easily find different levels and quality of my notes, Evergreen being the best, in case I want only well-edited and long-running notes and hide freshly generated ones. See all of my tags inÂ [Taxonomy of note types](http://ssp.sh/brain/taxonomy-of-note-types).


Although I have started updating the tags less lately, as I have gotten less of this specific need, it would still be there. I also donât take much time to review my notes and process them fromÂ [Literature Notes](http://ssp.sh/brain/literature-notes)Â toÂ [Permanent Notes](http://ssp.sh/brain/permanent-notes), as I start every note as if they were a permanent note and then add as I go, except for some unique templates like journal, book, or reflection templates.


See a complete list of my templates:


[

](https://www.ssp.sh/blog/obsidian-note-taking-workflow/images/my-template-list.png)List of my Markdown Templates in Obsidian


I can use every template at my fingertips if I read another book. I hitÂ `cmd+t`, typeÂ `book`, and hitÂ `enter`. Type the name of the book and typeÂ `enter`Â again. Now, I have a note prepared with my book with all the relevant tags and information I want to add, but most importantly, I can immediately take notes of insights and keep them for later.


This is what theÂ `ð Book Template`Â looks like:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
` | `# <% tp.file.title %>
- Tags / Categories: #ð¬ #ð #reading 
- Date: <WIKILINK_TEMP><% tp.date.now(format="YYYY-MM-DD") %></WIKILINK_TEMP>
- Author: <a href="https://ssp.sh/brain/author-name/">Author Name</a>
- Type: <a href="https://ssp.sh/brain/books/">Books</a>
- Genre: #self-help
- Related: 
- Started reading: <WIKILINK_TEMP><% tp.date.now(format="YYYY-MM-DD") %></WIKILINK_TEMP>
- Finished reading: 
- Origin:
> [!summary]
> 
> Write a summary of what you are reading. This is where your thinking happens, where you get something out of your book.

## Notes During Reading
- ...
- 
` |



## Plugins I Use


Some of my main plugins I use often in alphabetical order:

- **dataview**: Database features for within Markdown. Like SQL for notes, you can query lists of open todos, backlinks, and almost anything.
- **excalibrain**: This is used to get insights into particular notes and their connections. Visualize its connections and highlight notes that have links both ways.
- **note-folder-autorename**: Used initially when you have lots of images and want them to be inside a folder; this creates a folder with the name of the note and adds your note to that folder. There is no need to do all of it manually; configure a shortcut.
- **obsidian-admonition**: These areÂ [Admonition (Call-outs)](http://ssp.sh/brain/admonition-call-outs)Â I use all the time. This makes articles or notes look excellent without breaking the reading flow. For example, add a summary, a quick note, or insight you donât necessarily want to put inside the text.
- **obsidian-auto-link-title**: If you paste a link, it will automatically add the linkâs title as the name.
- **obsidian-excalidraw-plugin**: Drawing within Markdown
- **obsidian-list-callouts**: The same as Admonitions, but with lists. I added one late, but itâs super powerful as I use a lot of lists.
- **obsidian-pandoc**: Used for exporting it to a Word document, PDF, or others when I want to share it with other people.
- **obsidian-projects**: Notion-like database views with Kanban, Table view, calendar, and gallery, all nicely integrated into Markdown.
- **obsidian-reading-time**: Shows the reading time of each note.
- **obsidian-vimrc-support**: Additional Vim shortcuts from my Vim configs. See also in myÂ [dotfiles](https://github.com/sspaeti/dotfiles/blob/master/obsidian/.vimrc).
- **ollama**: My initial play used for local LLM on my notes.
- **omnisearch**: Default fuzzy search when I open or search new notes withÂ `cmd+o`.
- **readwise-official**:Â [ReadWise](http://ssp.sh/brain/readwise)Â integration that syncs all my comments and highlights from articles I read online or on Kindle.
- **remember-cursor-position**: A simple plugin that stores my cursor position for each note.
- **settings-search**: Simply search all obsidian settings instead of clicking through them.
- **templater-obsidian**: Extended feature for templates.


You can find all plugins, hotkeys, and Obsidian settings on myÂ [dotfiles](https://github.com/sspaeti/dotfiles/blob/master/obsidian/).


## How I Share Notes Publicly


If you click on my â[brain](http://ssp.sh/brain/)â on this website, youâll see all the notes I share publicly. These are the same notes I have in my personal Obsidian Vault, with the only difference being an added hashtagÂ `#publish`.


I share the notes withÂ [Quartz](http://ssp.sh/brain/quartz-publish-obsidian-vault), an [open-source alternative](https://www.ssp.sh/brain/open-source-obsidian-publish-alternatives/) to [Obsidian Publish](https://obsidian.md/publish). If you havenât seen it, please check it out; itâs outstanding.


I have an additional script that processes all my notes, copies the ones with the hashtags #publish into Quartz, and then deploys them on my website. I wrote more about that process and included my script onÂ [Public Second Brain with Quartz](http://ssp.sh/brain/public-second-brain-with-quartz).


The nice thing about Quartz is that it showcases the Obsidian graph and its backlinks. This makes it a powerful tool to explore notes and articles exploitatively, also called aÂ [Digital Garden](http://ssp.sh/brain/digital-garden). Instead of having one-dimensional blogs or glossaries, you can go inward and click on each link you like. The longer you write, the more links you have, and you can link to your vault instead of external pages.


I wrote a little more about it on theÂ [Future of Blogging](http://ssp.sh/brain/future-of-blogging), as I believe this should be the next step for personal blogs and to grasp dense information. Also, instead of creating copies of the same articles and adding a new year to the title, we can update the actual notes, leading toÂ [continuous notes](http://ssp.sh/brain/continuous-notes)Â that get constantly updated and improve over time. You do not start from a blank page.


Imagine if everyone would update their articles or notes instead of creating copies repeatedly; the internet would get a web of remarkable, highly valuable notes. This is one aspect I try with myÂ [Public Second Brain](https://brain.ssp.sh/).


### Feedback Loop: How Sharing and feedback helps me to learn more


A side effect of sharing publicly is that I get lots of feedback. ThisÂ feedback loopÂ is the most essential thing that has led me to write to this day. The satisfaction I get from you guys giving me feedback, telling me that it was helpful pointing out some alternatives or just making friends online, is something you canât replicate in the real world and is hard to conceive until you’ve experienced it.


Sharing my passion and finding like-minded people as a side effect will make me want to share more. Some call itÂ **Learn in Public**, which I suggest to anyone, even when starting.


## In Summary


In conclusion, Obsidian and the Second Brain gave me everything I ever dreamed of when I started taking notes. Even things I didnât know would help me or that I would need. E.g., a graph-based approach. Never would I have thought, as an organized Swiss person, that I would leave the path of putting everything into folder structures to find easily


The result is more clarity and peace of mind, as I can quickly put down an insight or an exciting thought in my Obsidian Vault and go on with life. For example, at a doctor’s appointment or when you get an allergy test, wouldn’t it be handy to pull up at any time? Exactly! As well as finding that any note intuitively later when needed.


Another big one is the offline accessibility of all my knowledge. When writing or being somewhere remote, you will have all your (second) brain and can search for something quickly. It also allows [deep work](https://www.ssp.sh/brain/deep-work) to turn off all internet for a more extended period and go into focus mode.


This happens more often lately that I do google less, but instead search my second brain as I have written it down as I googled it already more than once and just added it to my Obsidian.


This was a quick rant that I jotted down fast, but I hope it is still attractive to some of you. And please ask me any questions you might have; I’m super passionate about it and happy to share more or learn from your workflow.


## Follow-ups


If you want a deeper dive into PKM with Smart Note Taking, Second Brain, Zettelkasten, Getting Things Done (GTD), and Deep Life, check out my 6.5k words article aboutÂ [Personal Knowledge Management Workflow for a Deeper Life â as a Computer Scientist](http://ssp.sh/blog/pkm-workflow-for-a-deeper-life/).


To know more about my Vim workflow, check out my two articles, [My Vim-verse](https://www.ssp.sh/blog/my-vimverse/)Â andÂ [Why Vim Is More Than Just An Editor](http://ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/). I also created a shortÂ [Video on YouTube](https://youtu.be/LQasaw4MkqE?si=awDwQt160Wd4COGv)Â and wrote aboutÂ [Vim for Obsidian](http://ssp.sh/brain/vim-for-obsidian).


[Markdown vs Rich Text](http://ssp.sh/brain/markdown-vs-rich-text)Â orÂ [Local First](http://ssp.sh/brain/plaintext-files)Â are two other rabbit holes I went down. YouTube videos I enjoyed showcasing Obsidian:

- [Optimal Note Taking Framework for all subjects using Obsidian](https://youtu.be/LyOIvoHtRCM)
- [The Rise of Obsidian as a Second Brain](https://youtu.be/nz99I7apNLI)
- [Hack Your Brain With Obsidian.md](https://youtu.be/DbsAQSIKQXk)


Or of check my efficient Markdown collaboration via HackMD and Obsidian, Neovim, VSCode video.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/obsidian-note-taking-workflow/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Obsidian](https://www.ssp.sh/tags/obsidian/)
[Notetaking](https://www.ssp.sh/tags/notetaking/)
[Markdown](https://www.ssp.sh/tags/markdown/)
[Vim](https://www.ssp.sh/tags/vim/)
[Workflow](https://www.ssp.sh/tags/workflow/)
[Pkm](https://www.ssp.sh/tags/pkm/)
[Second Brain](https://www.ssp.sh/tags/second-brain/)
[Zettelkasten](https://www.ssp.sh/tags/zettelkasten/)
