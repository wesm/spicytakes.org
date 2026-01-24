---
title: "Just Say No to Finalization!"
date: 2004-07-26
url: https://blog.codinghorror.com/just-say-no-to-finalization/
slug: just-say-no-to-finalization
word_count: 304
---

I am working with some classes that wrap unmanaged APIs, so I have to be concerned with releasing the resources associated with these APIs – e.g., the IDisposable interface. I was a little confused about the distinction between Dispose() and Finalize(), and in my research I found [this article](https://web.archive.org/web/20041215155111/http://www.developer.com/net/csharp/article.php/2233111) by Brent Rector of Wintellect:


> *In a worst-case scenario, your object’s Finalize method won’t run until your process terminates gracefully. (Actually, the real worst case is that it never runs at all because the process terminates abnormally.) Shortly thereafter, non-memory resources will be released anyway, so **the Finalize method served no real purpose other than to keep the application from running as fast as it otherwise could.**
> Just say No to Finalize methods!*


It’s a good point. In a true worst case scenario – unhandled exception time – you won’t get any benefit from Finalize. So, given the (evidently) large performance penalty of Finalize, why bother? I tend to agree. However, the best practice according to Microsoft is, if you implement IDispose, you should also implement a Finalizer:

kg-card-begin: html

```
<Private _IsDisposed as Boolean = False 
''' <summary> 
''' public Dispose method intended for client use 
''' </summary> 
Public Overloads Sub Dispose() Implements IDisposable.Dispose 
Dispose(False) 
GC.SuppressFinalize(Me) 
End Sub 
''' <summary> 
''' common Dispose method; can be called by client or the runtime 
''' </summary> 
Protected Overridable Overloads Sub Dispose(ByVal IsFinalizer As Boolean)
If Not _IsDisposed Then
If IsFinalizer Then 
'-- dispose unmanaged resources
End If 
'-- disposed managed resources 
End If 
_IsDisposed = True 
End Sub 
''' <summary> 
''' called by the runtime only, at garbage collection time 
''' this protects us if the client "forgets" to call myObject.Dispose() 
''' </summary> 
Protected Overrides Sub Finalize() 
Dispose(True) 
End Sub>
```

kg-card-end: html

It’s all rather contradictory.

[idisposable](https://blog.codinghorror.com/tag/idisposable/)
[finalize](https://blog.codinghorror.com/tag/finalize/)
[resource management](https://blog.codinghorror.com/tag/resource-management/)
[unmanaged apis](https://blog.codinghorror.com/tag/unmanaged-apis/)
[performance](https://blog.codinghorror.com/tag/performance/)
