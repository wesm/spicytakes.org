---
title: "The next billion programmers"
subtitle: "The next product I’d build? Excel, for everything."
date: 2022-02-11T17:18:09+00:00
url: https://benn.substack.com/p/the-next-billion-programmers
slug: the-next-billion-programmers
word_count: 2158
---


![](https://substackcdn.com/image/fetch/$s_!YOV2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa536b4-3f18-4a84-893c-c7a16deb2b6c_2400x1219.jpeg)

*Where millennials learned Excel.*


If you ask data folks what they think of Excel, there are two acceptable answers. The first is rank contempt. It’s a bloated bundle of bad practices and antipatterns, the disease that won’t go away, the interminable termites in the foundation, thecrumbling hookson which our entire society hangs. The second answer is that Excel is software’s greatest achievement. It’s the ultimate Swiss Army knife; a perfectly designed cockroach; antifragile, manifest.


There is no third answer. In some warped version of the midwit meme, savvy observers live on the extremes, and only fools—”I like Excel, but I don’t think there’s anything special about it”—occupy the seemingly reasonable middle ground.


In my view, Excel is an unqualified triumph, for one very particular reason: It’s given more than a billion people direct access to the profound power of computers.


Of course, it’s hardly controversial to say that computers are powerful tools. But to most people, myself included, that power is abstract and confusing. It’s the incomprehensible reach of Google,finding 4.9 billion recordsin less than a second. It’s the impossible precision of rocket science, blasting barn silos to the edge of space, and landing them, upright, on a tiny target in the desert. It’s the magic of hardware itself, which can somehow turn bits of metal and silicon scattered across my house into words on my screen, and then words on another screen in Thailand, milliseconds later.


In contrast, Excel shows us something much more relatable—the power of automating simple arithmetic.


Consider a simple everyday application of Excel: Planning a party for theSuper Bowlbig game. You might start by listing everyone who’s coming. Excel counts how many people are on your list, so you can immediately decide how many bags of chips to buy. If some people want to invite their friends, you can easily add them, and Excel updates the tally. You add what food people are bringing, and input how much money each person spent; Excel can now tell you how much money each person should chip in. If a few friends don’t drink, you can tweak the math to discount the cost of beer from their contributions. Last minute cancellations are no problem either; just remove people from the list, and all the numbers immediately get recomputed.


None of this math is hard to do; it could be done just as easily by a middle schooler as a sophisticated piece of software. But it’sirritatingto do. Excel provides a solution: Write a few formulas—a simple program—and have a computer do the arithmetic for us. In that, Excel isn’t valuable because it does something that’s incomprehensible; it’s valuable because it does something that’s easily understandable, over and over, at incomprehensible speed.


While we could write programs to do the same thing in any number of languages, the genius of Excel is in its interface. Excel doesn’t force people to learn an entire language, but it doesn’t discourage them from writing code either;instead,it makes the code they write remarkably efficient.By embedding all of the computational logic in spreadsheet cells, Excel’s users don’t have to worry about variable assignment or object definition, much less much knottier things like development environments or package dependencies. They just enter their numbers, and write simple formulas to manipulate them.


This efficiency disguises what Excel really is: An interface for writing programs. In doing so, hundreds of millions of people who wouldn’t call themselves programmers became programmers, and Excel formulas became themost widely used code in the world.And Excel, which at first glance is little more than a calculator running on a loop,1turned into a limitless platform for automation, capable of planning parties, creating personal budgets, and modeling entire businesses and industries.


# Automate anything


If Excel is for automating arithmetic, more traditional programming languages are for automating anything on the internet. You can collectdata from Twitter. You can clean up acentury of baseball box scores. You can send emails, reformat messy files, start yourvacuum cleaner, feed yourcat, order aRange Rover, check yourflight status, and digitally stamp your exclusive ownership of a reference to a link to a jpeg of asingle green pixel.2


There is, as a matter of both convenience and genuine influence, enormous power in doing these things automatically. By figuring out how to search for tweets programmatically, I was able to fix my strategy for playing Wordle.3By writing a script that would automatically find promising candidates and send them messages on LinkedIn, a friend of mine became many times more productive as a recruiter and changed the course of his career.4


These examples, unfortunately, are the exception. Both my friend and I work in the tech industry, and were surrounded by others who could inspire us to search for these sorts of automations. Most people aren't so lucky. They don't have the examples to emulate that we did, or teammates who they could learn from.


But what they do have, as Excel shows us, is the ability. Programming custom logic into an interface isn't some rare talent; it just has too many prerequisites. Setting up an environment to write, manage, and run code has too many complicated steps, and too much can go wrong during each one. In Excel, you can model the entire global economy without parsing a single stack trace; in general programming experiences, you can't get to "Hello, world" without doing so.


Which raises an obvious question: Could there be an Excel for generic scripting? Just as Excel made it possible for billions of people to write code to automate arithmetic, could there be a tool that makes it possible for billions of people to automate anything?


# Excel for Everything


This isn’t an entirely novel concept, and lots of popular tools solve adjacent problems. Nothing, however, quite hits the nail on the head.


Zapier is great for connecting different apps together, but it encourages people to follow prebuilt recipes and use code as a (still complicated) escape hatch. Excel, by contrast, simplifies the code necessary to do certain things, but embraces coding as part of its interface.


Airtable and Retool help people create lightweight applications with interactive widgets. Though these can be used for a wide range of problems, they aren’t really meant to automate generic tasks. Their success, however, shows how imaginative people can be once they’re given tools that make hard things easy.


Notebooks and hosted Python runtimes get closer, but tools like these aretooopen-ended. They solve the development environment problem, and create an interface that, if you really squint, looks like a series of linked cells like Excel. But they require people to write and debug raw Python, from start to finish. For example, when planning a party, you can simply type in attendees’ names into Excel, and then use Excel’s formula language to gradually add more complexity. In a notebook, that list has to be created in Python directly. It’s a pool with only a deep end.


What, then, would be better? How do we give people a shallow end, and let them swim into deeper waters?


In my view, we could build a more generalized Excel as a collection of interconnected blocks, where each block contains a spreadsheet (or other data structure) of its own. For each block, you could either enter data directly into it, as you would in Excel, or read from other blocks, just as formulas in Excel do. In the latter case, the formulas could be simple functions for performing common actions, or they could be generic Python. Each cell is, in effect, a tiny lambda, with easy-to-access inputs.


The rest of the interface should make it easy to control how data moves around the blocks, and to see the intermediate outputs that each block produces. Each bit of Python, then, could be focused on exactly the job it needed to do—parse some text, reformat a data structure, call an API. The goal, in other words, should be to make each block small enough that it could becopied from Stack Overflow.


By making each block run independently (i.e., they can read from other blocks but aren’t defined by other blocks, just aslogicin one Excel cell is independent of the logic in other cells), people can work piecemeal, without having to think about the entire system in their head. This interface would let people construct programs iteratively, with the UI guiding them to add more complexity just as Excel’s does.


Admittedly, I haven’t considered all of the details here. And it’s possible someone else has tried this, and it didn’t work.5But given the success of Excel, the power in simple programs, and the accessibility of languages like Python once you remove all of the preconditions that are typically required to use it, it’s hard to dismiss the possibilities of what a combination of Python and Excel could do.6


If I were living on another timeline, it’d be an idea that I’d want to explore. As someone who’s scattered dozens of Python scripts around my laptop and Dropbox account, I want a tool that would help make them easier to build and manage. And as someone who’s tried to deploy a number of AWS Lambdas internally at Mode, but has always been stymied by some API gateway permission, incomprehensible IAM configurations, or the unholy nightmare that is AWS CloudWatch, I’d love a tool that makes Lambdas serverlessandpainless.7


But more importantly, I think it’d be cool if a lot more people could do this too.


# “You can do anything”


Back in Mode’s early days, I was talking to a couple engineers about an idea for a new feature. At some point during the conversation, I asked them if it was possible to build it. In response, one engineer said, “It’s a computer. You can build anything.”


Initially, I thought it was a hyperbolic throwaway line, like a parent telling a kid that they can eat whatever they want at a mall food court. I’ve got a few choices, but I can’t actually buildanything…can I?


No, I was told; he meant it literally. Within the bounds of a few physical laws about the speed of light, we could build anything. Some things will be harder or take longer, but eventually, if we can think of it, we could make a computer do it.


It took me a while to truly internalize this idea, but there’s something magical about finally understanding what he meant. There’s something magical about seeing a problem and knowing—knowing—that, somehow, some way, it can be solved. There’s something magical about running a program and watching it slowly tick through its operations, each printout simultaneously affirming that you figured out the puzzle, and deepening your sense of amazement about how any of this actually works. And there’s something magical about hitting enter—always a little harder than normal—to run these scripts, and still feeling a shooting pride and reflexive smile as I watch them go.8


Sadly, most efforts to share this feeling with people focus on turning people into professional programmers. Programming, we’re implicitly told, is a career, not a skill. Or worse still, programmers are who you are, and some peoplejust aren’t math people.


Someone—something—should change that narrative. Programming is simply a tool, applicable to everything from planning a party to blogging, and to every career from recruiter to lawyer. With a bit of help to make it more accessible, anyone can do it—and with it, anyone can do anything.

[1](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-1-48607793)

I mean a literal calculator, with buttons and a screen and C and CE keys that allegedly do different things.

[2](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-2-48607793)

For sale, 300 ETH, OBO.

[3](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-3-48607793)

Prior tothis post, I was 16 for 18. After changing my strategy, 20 for 20, with only one game going six turns.

[4](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-4-48607793)

This was years ago; since then, people have built a number of products that do the same thing.

[5](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-5-48607793)

In which case, my stance isno one has truly tried it.

[6](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-6-48607793)

And yes, while you can kinda sortarun Python inside of actual Excel, that largely misses the point. The interface should be designed around using Python; Python can’t be tacked on to today’s spreadsheets.

[7](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-7-48607793)

Given how simple the substantive parts of the these Lambdas are, and how complex the cruft around them is, I’ve always felt that they represent a huge missed opportunity. Two things I’d immediately want to invest in: “Lambdas, but better,” and “Slack, but more like email.”

[8](https://benn.substack.com/p/the-next-billion-programmers#footnote-anchor-8-48607793)

I have a pet theory that this is one of the reasons dbt is popular. It introduced a lot of people to the command line—and, by extension, to the feeling that comes with executing a program on it. Moreover, most of the interface of the dbt’s command line product is a slow drip of green success indicators. To the cynical software engineer, this is just a day on the job. But to the rest of us, it’s a satisfying mix of power and wonder, like seeing under the hood a car for the first time.
