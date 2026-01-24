---
title: "Teaching Users to Read"
date: 2004-10-25
url: https://blog.codinghorror.com/teaching-users-to-read/
slug: teaching-users-to-read
word_count: 549
---

I’ve talked about [irresponsible use of dialog boxes](https://blog.codinghorror.com/death-to-the-dialog-box/) before, but a few pages I’ve read recently highlighted an interesting aspect of this topic that I hadn’t considered. First, [Joel Spolsky](http://www.joelonsoftware.com/uibook/fog0000000249.html):


> *This may sound a little harsh, but you’ll see, when you do usability tests, that **there are quite a few users who simply do not read words that you put on the screen. If you pop up an error box of any sort, they simply will not read it.** This may be disconcerting to you as a programmer, because you imagine yourself as conducting a dialog with the user. Hey, user! You can’t open that file, we don’t support that file format! Still, experience shows that the more words you put on that dialog box, the fewer people will actually read it.*


And [Mike Pope](http://mikepope.com/blog/DisplayBlog.aspx?permalink=480) dug up a fascinating [Eric Lippert comment](http://blogs.msdn.com/ericlippert/) on the same topic:

kg-card-begin: html

> It’s not that users are morons or that they “forget” to think. It’s that users are trained to not think. Users very quickly learn from experience that:
> Dialog boxes are modal. But users do not think of them as “modal,” they think of them as **“preventing me from getting any work done until I get rid of them.”**
> Dialog boxes almost always go away when you click the leftmost or rightmost button.
> Dialog boxes usually say **“If you want to tech the tech, you need to tech the tech with the teching tech tech. Tech the tech? Yes / No.”**
> If you press one of those buttons, something happens. If you press the other one, nothing happens. Very few users want nothing to happen – in the majority of cases, whatever happens is what the user wanted to happen. Only in rare cases does something bad happen.
> In short, from a user perspective, dialog boxes are impediments to productivity which provide no information. It’s like giving shocks or food pellets to monkeys when they press buttons – primates very quickly learn what gives them the good stuff and avoids the bad.

kg-card-end: html

Well, I couldn’t help thinking of this classic Gary Larson strip:


![](https://blog.codinghorror.com/content/images/2025/06/image-16.png)


My intent is not to make fun of users, but to illustrate that there are far more effective ways to communicate with your dog. Essentially, **any time you’re asking the user to make a choice they don’t care about, you have failed the user. **Well designed software takes care of “teching the tech tech” all by itself, and leaves the user free to worry about things relevant to the work they are doing. Dialog boxes are almost always detrimental. The goal should be to write **an entire application free of dialog boxes**.


Well designed software avoids asking the user questions by...

- Anticipating user needs (wizards, templates, autocomplete, IUI)
- Remembering past preferences and using that to better anticipate future needs
- Silently and automatically protecting the user from the consequences of any negative actions (versioning, undo)


It’s amazing how few software packages even *try* to meet these goals, even with simple, common things. For example, why does the file save dialog *always* default to My Documents even though I saved to Desktop the last time I used the application?

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[usability](https://blog.codinghorror.com/tag/usability/)
[user behavior](https://blog.codinghorror.com/tag/user-behavior/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[technical communication](https://blog.codinghorror.com/tag/technical-communication/)
