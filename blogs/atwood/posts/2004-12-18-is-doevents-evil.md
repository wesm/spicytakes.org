---
title: "Is DoEvents Evil?"
date: 2004-12-18
url: https://blog.codinghorror.com/is-doevents-evil/
slug: is-doevents-evil
word_count: 990
---

It’s an old VB developer trick, but it also works quite well in .NET: **to present responsive WinForms interfaces, do most of your heavy lifting in the first Paint event, rather than in the Load event.** I’ve seen many naive WinForm developers perform database queries and other heavyweight operations in the Form Load event, which absolutely kills perceived performance – the form doesn’t even display until all the work is done! It’s much better to render part of the form first so the user gets immediate visual feedback, beyond an hourglass cursor, that stuff is happening.


The easiest way to deliver a semi-responsive interface is to attach an IsFirstPaint boolean to the paint event, and move the intensive part of the work you’re doing on Load into Paint. However, for this to work, you still need to yield a bit to give the form time to paint some of its elements – that means putting a little bit of **DoEvents spackle** in there, prior to going off and doing a bunch of work.


Now, I like the effort/results ratio that DoEvents and IsFirstPaint delivers, but **I’ve never really been comfortable with DoEvents in the brave new world of .NET.** It seems like.. old-school Win3x cooperative multitasking. I’m not the only developer to question the meaning of DoEvents in .NET, as [this MSDN threading chat](https://web.archive.org/web/20051028105338/http://msdn.microsoft.com/chats/transcripts/vstudio/vstudio_112503.aspx) illustrates:


> *Q: What is the reason for maintaining DoEvents in the .NET framework? Why was it not limited to an assembly in the Microsoft.VisualBasic namespace? What is the need for DoEvents when there is proper support for multi-threaded applications?
> A: Jason (Microsoft) DoEvenets is a holdover from VB 5.x, but it is still useful in the .NET Framework world. If you have a loop that runs for a long time, it is often easier to call DoEvents than to refactor your loop to use true .NET threading.
> Q: Why is DoEvents in the BCL namespace?
> A: Glenn (Microsoft) Threading is difficult, and should be avoided if there’s an easier way. If all you need to do is yield on your UI thread, DoEvents is perfect.
> **Q: DoEvents is evil?**
> A: Glenn (Microsoft) Yielding on the UI thread is a legitimate Windows programming practice. It always has been. DoEvents makes it easy, because the situations in which you need to use it are simple.*


Or, [as Dan Tohatan puts it](https://web.archive.org/web/20040627214809/http://dacris.com/blog/archive/2004/05/29/155.aspx):


> ***Application.DoEvents() - The call of the devil.**
> DoEvents messes up the normal flow of your application. If I recall correctly, DoEvents is asynchronous which means it terminates before the application has actually processed any outstanding events, so if you’re using it in a procedure with many sequential statements, calling DoEvents causes a huge disturbance whenever it’s called. Basically, if you find yourself needing to call DoEvents anywhere, think about starting another thread instead, or using asynchronous delegates.
> Imagine this if you will: You have a button on your form that, when clicked, does some complex processing. During the complex processing it also intermittently calls DoEvents to keep the application’s user interface “responsive” – not the best method, I would have used async delegates, but we’re talking about a mediocre programmer here. Anyhow, the user sees the application still responding and no indication that there’s some processing going on. So the user clicks that button again WHILE the processing is going on! **The button responds to the event and starts another processing thread but it isn’t actually a thread here**, I hope you get what I’m saying. So, like I said earlier, DoEvents screws up the flow of the application too easily.*


Of course, DoEvents and IsFirstPaint are only partial solutions to make the forms *look* like they load faster. Never underestimate the power of **perceived performance**, but the actual interface is still unresponsive. If you want a fully responsive interface with background processing, the [correct way to do it](https://web.archive.org/web/20080510104858/http://blogs.msdn.com/dphill/archive/2004/07/14/183503.aspx) is with threading and Control.Invoke. A lot of armchair developers like to conveniently forget this, but **threading is hard**. Dangerous, even. It’s not a coding burden you take on lightly. When things start happening in asynchronous, indeterminate order instead of the deterministic 1-2-3 order you’d expect... things get absurdly difficult really quickly, as noted in [this Roy Osherove blog post](https://web.archive.org/web/20061114084028/http://weblogs.asp.net/rosherove/archive/2003/05/06/6554.aspx):


> *Beware - I’ve spent quite a lot of time on this problem. We are building a client application fetching information from a server (using SOAP) in the background, and displaying the information in the windows UI when it arrives. Unfortunately it arrives in another thread. On top of this we have implemented a cache the UI components should be reading from. **The problem is that it is insufficient to call Control.Invoke() when changing information in, for example, a listbox. We also need to make sure the underlying data to be displayed does not change while the UI thread reads it.** And simple synchronization is not enough as this will only give atomic access to a single element, when we need to block the entire array while updating the control.
> The best solution I’ve found until now is to model an UI thread and background threads as two separate processes (implemented as .NET threads) that only communicates through messages and has NO shared memory. The messages are modeled through a homebuild “mailbox” interface. The modeled is inspired by the language Erlang.*


You’ve never truly debugged an app until you’ve struggled with an obscure threading issue. Threading is a manly approach for tough guys, and it will put hair on your chest – but you may not have any left on your head when you’re done.


I agree that DoEvents is not exactly great programming practice, but **even Microsoft recommends using it in lieu of hard-core threading for simple problems**. So it’s something of a tradeoff. Easier WinForms threading is coming in .NET 2.0, but in the meantime, I’d look into the [backgroundworker code samples](https://web.archive.org/web/20051103133714/http://weblogs.asp.net/rosherove/articles/BackgroundWorker.aspx).

[vb](https://blog.codinghorror.com/tag/vb/)
[.net](https://blog.codinghorror.com/tag/net/)
[winforms](https://blog.codinghorror.com/tag/winforms/)
[doevents](https://blog.codinghorror.com/tag/doevents/)
