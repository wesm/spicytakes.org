---
title: "The Opposite of Fitts’ Law"
date: 2010-03-24
url: https://blog.codinghorror.com/the-opposite-of-fitts-law/
slug: the-opposite-of-fitts-law
word_count: 759
---

If you’ve ever wrangled a user interface, you’ve probably heard of [Fitts’ Law](https://blog.codinghorror.com/fitts-law-and-infinite-width/). It’s pretty simple – **the larger an item is, and the closer it is to your cursor, the easier it is to click on**. Kevin Hale put together a great [visual summary of Fitts’ Law](https://web.archive.org/web/20100409114907/http://particletree.com/features/visualizing-fittss-law/), so rather than over-explain it, I’ll refer you there.


The short version of Fitts’ law, to save you all that tedious *reading*, is this:

- Put commonly accessed UI elements on the edges of the screen. Because the cursor automatically stops at the edges, they will be easier to click on.
- Make clickable areas as large as you can. Larger targets are easier to click on.


I know, it’s very simple, almost too simple, but humor me by following along with some thought exercises. Imagine yourself trying to click on...

- a 1 x 1 target at a random location
- a 5 x 5 target at a random location
- a 50 x 50 target at a random location
- a 5 x 5 target in the corner of your screen
- a 1 x 100 target at the bottom of your screen


Fitts’ Law is mostly common sense, and enjoys enough currency with UI designers that they’re likely to know about it even if they don’t follow it as religiously [as they should](https://web.archive.org/web/20100325172235/http://yokozar.org/blog/archives/194). Unfortunately, I’ve found that designers are much less likely to consider the *opposite* of Fitts’ Law, which is arguably just as important.


If we should make UI elements we *want* users to click on large, and ideally place them at corners or edges for maximum clickability – **what should we do with UI elements we *don’t* want users to click on?** Like, say, the “delete all my work” button?


Alan Cooper, in [About Face 3](https://blog.codinghorror.com/the-three-faces-of-about-face/), calls this the ejector seat lever.

kg-card-begin: html

> In the cockpit of every jet fighter is a brightly painted lever that, when pulled, fires a small rocket engine underneath the pilot’s seat, blowing the pilot, still in his seat, out of the aircraft to parachute safely to earth. Ejector seat levers can only be used once, and their consequences are significant and irreversible.
>   Applications must have ejector seat levers so that users can “occasionally” movepersistent objects in the interface, or dramatically (sometimes irreversibly) alter the function or behavior of the application. The one thing that must never happen is accidental deployment of the ejector seat.
> The interface design must assure that a user can never inadvertently fire the ejector seat when all he wants to do is make some minor adjustment to the program.

kg-card-end: html

I can think of a half-dozen applications I regularly use where **the ejector seat button is inexplicably placed right next to the cabin lights button**. Let’s take a look at our old friend Gmail, for example:


![](https://blog.codinghorror.com/content/images/2025/04/image-465.png)


I can tell what you’re thinking. Did he click **Send** or **Save Now**? Well, to tell you the truth, in all the excitement of composing that angry email, I kind of lost track myself. Good thing we can easily undo a sent mail! Oh wait, we *totally can’t*. Consider my seat, or at least that particular rash email, ejected.


It’s even worse when I’m archiving emails.


![](https://blog.codinghorror.com/content/images/2025/04/image-464.png)


While there were at least 10 pixels between the buttons in the previous example, here there are all of... *three*. Every few days I accidentally click **Report Spam **when I really meant to click **Archive**. Now, to Google’s credit, they do offer a simple, obvious undo path for these accidental clicks. But I can’t help wondering why it is, exactly, that these two buttons with such radically different functionality just *have* to be right next to each other.


Undo is powerful stuff, but wouldn’t it be better still if I wasn’t pulling the darn ejector seat lever all the time? Wouldn’t it make more sense to put that risky ejector seat lever in a different location, and make it smaller? Consider the WordPress post editor.


![](https://blog.codinghorror.com/content/images/2025/04/image-463.png)


Here, the common **Update** operation is large and obviously a button – it’s easy to see and easy to click on. The less common **Move to Trash** operation is smaller, presented as a vanilla hyperlink, and placed well away from Update.


The next time you’re constructing a user interface, you should absolutely follow Fitts’ law. It just makes sense. But don’t forget to follow the opposite of Fitts’ law, too – uncommon or dangerous UI items should be *difficult* to click on!

[usability](https://blog.codinghorror.com/tag/usability/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[human-computer interaction](https://blog.codinghorror.com/tag/human-computer-interaction/)
[ui design](https://blog.codinghorror.com/tag/ui-design/)
[fitts' law](https://blog.codinghorror.com/tag/fitts-law/)
