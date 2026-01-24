---
title: "Perceived Performance and Form.Paint"
date: 2005-01-07
url: https://blog.codinghorror.com/perceived-performance-and-formpaint/
slug: perceived-performance-and-formpaint
word_count: 266
---

As a follow-up to my [caution about exceptions in Form.Paint()](https://blog.codinghorror.com/if-an-exception-happens-in-formpaint-does-anyone-catch-it/), I wanted to illustrate why this technique is so effective. Let’s say you had a form with this code:

kg-card-begin: html

```
Private IsFirstPaint As Boolean = True
Private Sub DoWork()
Cursor = Cursors.WaitCursor
StatusBar1.Text = "Loading..."
System.Threading.Thread.Sleep(2000)
For i As Integer = 0 To 99
ComboBox1.Items.Add("ComboBoxItem " & i)
System.Threading.Thread.Sleep(5)
Next
ComboBox1.SelectedIndex = 4
System.Threading.Thread.Sleep(2000)
For i As Integer = 0 To 99
ListBox1.Items.Add("ListBoxItem " & i)
System.Threading.Thread.Sleep(5)
Next
ListBox1.SelectedIndex = 4
StatusBar1.Text = "Ready."
Cursor = Cursors.Default
End Sub
Private Sub Form1_Load(ByVal sender As System.Object, _
ByVal e As System.EventArgs) Handles MyBase.Load
DoWork()
End Sub
Private Sub Form1_Paint(ByVal sender As Object, _
ByVal e As System.Windows.Forms.PaintEventArgs) _
Handles MyBase.Paint
If IsFirstPaint Then
IsFirstPaint = False
Application.DoEvents()
DoWork()
End If
End Sub
```

kg-card-end: html

So either we’re doing 5 seconds of work in Paint, or we’re doing 5 seconds of work in form Load. Here’s what it looks like when the work is done in **Form.Load**:


![movie of Form Load doing work](https://blog.codinghorror.com/content/images/uploads/2005/01/6a0120a85dcdae970b0128776fbbb8970c-pi.gif)


And here’s what it looks like when the work is done in **Form.Paint**:


![movie of Form Paint doing work](https://blog.codinghorror.com/content/images/uploads/2005/01/6a0120a85dcdae970b0128776fbbe7970c-pi.gif)


The amount of time is the same in both cases, but **guess which one users will tell you is “faster?”** Perceived performance is more important than actual performance.


Sure, you can do a lot better job with threading, but I guarantee that’ll take a lot more work than three lines of code! That’s why I love the [IsFirstPaint and DoEvents combo](https://blog.codinghorror.com/is-doevents-evil/): maximum benefit for minimum effort.

[multithreading](https://blog.codinghorror.com/tag/multithreading/)
[visual basic](https://blog.codinghorror.com/tag/visual-basic/)
[ui performance](https://blog.codinghorror.com/tag/ui-performance/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
