---
title: "If an Exception happens in Form.Paint, does anyone catch it?"
date: 2005-01-05
url: https://blog.codinghorror.com/if-an-exception-happens-in-formpaint-does-anyone-catch-it/
slug: if-an-exception-happens-in-formpaint-does-anyone-catch-it
word_count: 547
---

In a previous post, I mentioned the old [VB6 trick](https://blog.codinghorror.com/is-doevents-evil/) of deferring form work until the Form.Paint event in order to provide a (seemingly) responsive interface to the user. Well, in the .NET world there’s **one strange side effect when you do this**. Let’s say you had this code, in a solution where the startup object is **Sub Main**:

kg-card-begin: html

```
Public Class Form1
Inherits System.Windows.Forms.Form
Private Sub Form1_Load(ByVal sender As System.Object, _
ByVal e As System.EventArgs) Handles MyBase.Load
Throw New Exception("This is a Form_Load exception")
End Sub
Private Sub Form1_Paint(ByVal sender As Object, _
ByVal e As System.Windows.Forms.PaintEventArgs) _
Handles MyBase.Paint
Throw New Exception("This is a Form_Paint exception")
End Sub
End Class
Public Class Class1
Public Shared Sub Main()
Application.Run(New Form1)
End Sub
End Class
```

kg-card-end: html

The Form.Load exception happens as expected. The Form.Paint exception, on the other hand... looks like this:


![](https://blog.codinghorror.com/content/images/2025/05/image-37.png)


**The breakpoint the debugger puts us on is nowhere near the offending line of code.** As I’m sure you can imagine, this makes debugging... interesting. Oddly enough, if you look at the debug output for this exception, the actual line of the exception *is* present there:

kg-card-begin: html

```
Unhandled Exception: System.Exception: This is a Form_Paint exception
at WindowsApplication1.Form1.Form1_Paint(Object sender, PaintEventArgs e) in WindowsApplication1Form1.vb:line 50
at System.Windows.Forms.Control.OnPaint(PaintEventArgs e)
at System.Windows.Forms.Form.OnPaint(PaintEventArgs e)
at System.Windows.Forms.Control.PaintWithErrorHandling(PaintEventArgs e, Int16 layer, Boolean disposeEventArgs)
at System.Windows.Forms.Control.WmPaint(Message& m)
at System.Windows.Forms.Control.WndProc(Message& m)
at System.Windows.Forms.ScrollableControl.WndProc(Message& m)
at System.Windows.Forms.ContainerControl.WndProc(Message& m)
at System.Windows.Forms.Form.WndProc(Message& m)
at System.Windows.Forms.ControlNativeWindow.OnMessage(Message& m)
at System.Windows.Forms.ControlNativeWindow.WndProc(Message& m)
at System.Windows.Forms.NativeWindow.DebuggableCallback(IntPtr hWnd, Int32 msg, IntPtr wparThe program '[2856] WindowsApplication1.exe' has exited with code 0 (0x0).
am, IntPtr lparam)
at System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
at System.Windows.Forms.ComponentManager.System.Windows.Forms.UnsafeNativeMethods+IMsoComponentManager.FPushMessageLoop(Int32 dwComponentID, Int32 reason, Int32 pvLoopData)
at System.Windows.Forms.ThreadContext.RunMessageLoopInner(Int32 reason, ApplicationContext context)
at System.Windows.Forms.ThreadContext.RunMessageLoop(Int32 reason, ApplicationContext context)
at System.Windows.Forms.Application.Run(Form mainForm)
at WindowsApplication1.Class1.Main() in WindowsApplication1Class1.vb:line 4
```

kg-card-end: html

And it gets even weirder! You can make the debugger break on the actual line in Form.Paint() by messing around with the Debug, Exceptions dialog in VS.NET. Turn on **“When the exception is thrown, break into the debugger” for all CLR Exceptions**. Now you’ll break on *every* exception – even the handled ones, and even exceptions inside third party binaries – which can be annoying. But at least it gets you to the actual line of code where the exception was raised:


![](https://blog.codinghorror.com/content/images/2025/05/image-38.png)


I don’t pretend to understand the arcane win32 api rules that cause exceptions to be somehow absorbed in Form.Paint() and passed back to the main application thread. All I know is, it’s incredibly annoying. When I originally researched this problem last year, I dug up this [rather unsatisfying answer](http://www.mail-archive.com/advanced-dotnet@discuss.develop.com/msg01781.html):


> *The exception is caught in **PaintWithErrorHandling** and then re-thrown again, all the way back to the program entry point because nowhere else along the callstack to your paint function is there an exception handler.
> My two suggestions are: 1) put an exception handler in your paint function. 2) Have the debugger break on exceptions that aren’t known to be owned by you when they are thrown.*


Anyway, **be careful when debugging forms that do work in the paint event**. I have yet to see any reasonable explanation for this behavior. If any [Windows Forms Coding Heroes](http://www.sellsbrothers.com/) want to step up and justify this in the comments, be my guest.

[windows forms](https://blog.codinghorror.com/tag/windows-forms/)
[.net](https://blog.codinghorror.com/tag/net/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[form events](https://blog.codinghorror.com/tag/form-events/)
[vb6](https://blog.codinghorror.com/tag/vb6/)
