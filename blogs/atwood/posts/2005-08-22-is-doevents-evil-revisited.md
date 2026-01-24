---
title: "Is DoEvents Evil, Revisited"
date: 2005-08-22
url: https://blog.codinghorror.com/is-doevents-evil-revisited/
slug: is-doevents-evil-revisited
word_count: 339
---

A colleague of mine had some excellent comments on the surprising reentrancy issues you’ll run into when using **Application.DoEvents()**:

kg-card-begin: html

> *
> The Application.DoEvents method is often used to allow applications to repaint while some longer task is taking place. This is usually the result of polling instead of using events / delegates. That’s fine, but developers need to understand **DoEvents processes all of the messages in the message queue, not just paint messages**. This can lead to unexpected reentrancy issues. A simple example is shown below.*
> // some data we care about
> private int _count;
> // the click handler for a button
> private void buttonUserAction_Click(object sender, System.EventArgs e)
> {
> _count++;
> // _count won’t always be 1; it depends how many times
> // this method was reentered during the DoEvents calls
> Console.WriteLine(_count);
> // simulate longer tasks that we are polling the status on.
> // call DoEvents to allows the window to repaint
> for (int i=0; i < 100000; i++)
> Application.DoEvents();
> _count--;
> }
> *In this example, it doesn’t matter if the method is reentered. But it might in other methods or applications. Always remember that DoEvents can cause methods to be reentered. And understand which methods are affected: any method that is called directly or indirectly in response to processing messages in the message queue.
> *
> It would be useful if the Form object had a Busy property; the form would only process paint related messages and skip input related messages like menus, clicks, keyboard, etc.

kg-card-end: html

I put together a [VS.NET 2003 winforms solution](https://web.archive.org/web/20060714165154/http://www.codinghorror.com/blog/files/IsDoEventsEvil_Source.zip) (6kb) demonstrating the code sample above.


This may make you wonder: [Is DoEvents Evil?](https://blog.codinghorror.com/is-doevents-evil/)


I think it’s definitely the *lesser* of two evils: it’s either this simplified cooperative yielding or [full-bore multithreaded code](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/). DoEvents can be a big win with minimal effort in the right situations. For example, how about using it to [improve perceived form load performance?](https://blog.codinghorror.com/perceived-performance-and-formpaint/)

[events](https://blog.codinghorror.com/tag/events/)
[reentrancy issues](https://blog.codinghorror.com/tag/reentrancy-issues/)
[application.doevents](https://blog.codinghorror.com/tag/application-doevents/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
