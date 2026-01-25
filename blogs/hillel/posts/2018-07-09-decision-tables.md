---
title: "Decision Tables"
date: 2018-07-09
url: https://www.hillelwayne.com/post/decision-tables/
slug: decision-tables
word_count: 1266
---

I really like decision tables but they’ve fallen out of common knowledge. Let’s fix that.


A **decision table** is a means of concisely representing branching and conditional computations. In the most basic form, you have some columns that represent the “inputs” as booleans and some columns that represent outputs and effects. It looks like this:



| A | B | C | f(A, B, C) |
| T | T | T | **1** |
| T | T | F | **3** |
| T | F | T | **7** |
| T | F | F | **“cucumber”** |
| F | - | - | **`NullError`** |



`-` means that it doesn’t matter what the value is. If you’re feeling saucy you can add enumeration inputs, too, as long as the enumerations cover all the possible values for that input. For a decision table to be “consistent”, all possible inputs must map to *exactly one* row. There can’t be any inputs that aren’t covered, and a two rows can’t overlap in what inputs they cover. Two rows may, however, map to the same output.


As an example, here’s fizzbuzz:



| `n % 3` | `n % 5` | f(n) |
| T | T | **“FizzBuzz”** |
| T | F | **“Fizz”** |
| F | T | **“Buzz”** |
| F | F | **`n`** |



That’s all there is to decision tables. That’s what I like about them: you can explain the whole idea in under two minutes. So how does it work in practice?


# Use Case


At a previous job we had to migrate a legacy audio system without downtime. We had an app with quiz questions and answers, and for some people (English language learners, preschoolers, special needs) there was a “speak aloud” button. The legacy system for this had some serious data integrity problems.


Questions and answers had a `text` field. If you clicked the button, we’d play the sound clip for that text. We didn’t have nearly enough people to record clips for all of our text, so we shelled out to a third-party automated “text to speech” (TTS) service. We’d send the text and get back a sound file. To save money and keep things performant we’d store the file as an asset and create an `Audio` database record. Since we had a lot of questions with duplicate texts (“what is the theme of this story?”) we decided to look up the audio records on their *text*. That way all questions with the same text would retrieve the same file.


With me so far? Let’s make it worse. The `text` data for a question/answer was the text to be *displayed*, markup and all. The text might be “which is `<em>incorrect</em>`”, which the TTS would pronounce “which is left angle bracket em right angle bracket incorrect left angle bracket slash em right angle bracket”. To address this we added an `override` field. If null, then we’d look up on `text` as normal. If it had content, we’d look up the audio using the text in `override` instead.


Now you might be thinking “the TTS can’t be *that* good” and you’d be right. We had a manual upload feature where for a given question, we could just upload a sound file that would be read for that question. But we’d have to create a corresponding `Audio` record, and we could only look up `Audio` on its corresponding *text*, meaning we had to save the record with the text/override of the question we uploaded the file under and *not* the question id.


So if you uploaded a manual audio file, it would play for all text snippets that shared the same text or override.


Now consider what happens when we have a question like “which letter matches its sound?” where three of the answers need to be the *wrong* sound.


New version: text and overrides remain global. Manual audio doesn’t have a text field and is tied to a specific question/answer. We had to implement this system without disrupting the existing records. If somebody requested the audio file we had to make it work no matter what, and if it was on the old system, migrate that file to the new system in the process. In some cases, we needed to log what happened, and in some cases, the text never had a corresponding audio file as nobody had yet clicked the “read aloud” button. So we’d still have to make calls to the TTS service as normal.


A lot of different variables and conditionals in play here and no “pattern” to the actions involved. When designing the solution, we used decision tables to make sure we covered every possible case and that every outcome matched our requirements. Here’s (very roughly) what it looked like.



| `has_id` | `override` | `in_db` | `auto` | TTS | clone | log |
| T | - | - | - | **F** | **F** | **F** |
| F | T | T | T | **F** | **F** | **F** |
| F | T | T | F | **F** | **T** | **T** |
| F | T | F | - | **T** | **T** | **F** |
| F | F | T | T | **F** | **F** | **F** |
| F | F | T | F | **T** | **T** | **T** |
| F | F | F | - | **T** | **F** | **F** |



This made reasoning about the problem a lot easier. We could quickly answer questions about the imagined case. Take the question “what should happen if we have an legacy override but it points at a manual upload”. Figuring out what should happen from the informal description is really hard. With a decision table, that question just maps to row 3: “clone the audio and point the new row at the question, then update the question to directly call that row. Log that this happened and do not call the TTS service.”


Like all formal specifications, we can use the table to discover properties about our program. One common property is irrelevance: determining that some value does *not* affect the outcome. In an earlier decision table1 we also had a “type of TTS” input, but that proved irrelevant and we nixed it. Another property is decomposition: can you break a table into two smaller independent tables? In this case no, but in other decision tables that can simplify things considerably.


# Discussion


Decision tables are an extremely lightweight formal specification. There’s only one consistency rule and the contained information is obvious: “if X, do Y”. Pretty much anyone can learn to write one. More importantly, anybody can learn to read one, so it provides a simple means of sharing information between people. That’s why it’s a shame they’re so obscure: a lot of people would find them useful and there’s zero learning curve to start using them.


While basic decision tables are already great, there’s some advanced tricks you can do with them. We wrote a few rspec macros that expanded our decision table into a test suite. That let us check the consistency of the code with respect to the table. You also can also try to generalize them, giving you the general class of specifications informally called **Parnas Tables**. Here’s some more on the [history](https://pdfs.semanticscholar.org/750f/ecf4349faeeab9a827a929de37be30f3df26.pdf) of tabular specifications.


*Thanks to [Jay Parlar](https://twitter.com/parlar) for feedback.*


---

1. “Earlier” meaning “two minutes earlier”. You can sketch out decision tables pretty quickly. 
 [return]
