---
title: "A Stopwatch Class for .NET 1.1"
date: 2005-12-06
url: https://blog.codinghorror.com/a-stopwatch-class-for-net-11/
slug: a-stopwatch-class-for-net-11
word_count: 485
---

The first rule of performance testing is to measure, then measure again, then measure one more time just to be sure. NET 2.0 adds a handy [Diagnostics.Stopwatch](http://msdn2.microsoft.com/en-us/library/system.diagnostics.stopwatch.aspx) which is perfect for this kind of ad-hoc precision timing.


A year ago I created a Stopwatch class which was eerily similar to the one that Microsoft ended up shipping in .NET 2.0. I went ahead and **made the minor modifications necessary to make my Stopwatch class identical to Microsoft's**. This way you can use the object in .NET 1.1 and port your code as-is to .NET 2.0 with only a namespace change.

kg-card-begin: html

```

using System;
/// <summary>
/// Provides a set of methods and properties that you can use to accurately
/// measure elapsed time.
/// </summary>
public class Stopwatch
{
[System.Runtime.InteropServices.DllImport("Kernel32")]
static extern bool QueryPerformanceCounter(out long @ref);
[System.Runtime.InteropServices.DllImport("Kernel32")]
static extern bool QueryPerformanceFrequency(out long @ref);
private long _Start = 0;
private long _Elapsed = 0;
private bool _IsRunning = false;
/// <summary>
/// the current performance-counter frequency, in counts per second
/// </summary>
readonly private long _CounterFrequency;
public Stopwatch()
{
/// prelinks all win32 api calls so there's less performance hit when called
System.Runtime.InteropServices.Marshal.PrelinkAll(typeof(Stopwatch));
if (QueryPerformanceFrequency(out _CounterFrequency) == false)
{
throw new Exception("High resolution timers are not available on this CPU");
}
}
/// <summary>
/// Starts, or resumes, measuring elapsed time for an interval.
/// </summary>
public void Start()
{
if (_IsRunning) this.Stop();
_Start = this.CurrentTime;
_IsRunning = true;
}
/// <summary>
/// Stops measuring elapsed time for an interval.
/// </summary>
public void Stop()
{
if (!_IsRunning) return;
_Elapsed += this.CurrentTime - _Start;
_Start = 0;
_IsRunning = false;
}
/// <summary>
/// Stops time interval measurement and resets elapsed time span to zero.
/// </summary>
public void Reset()
{
if (_IsRunning) this.Stop();
_Elapsed = 0;
}
/// <summary>
/// retrieves the current value of the high-resolution performance counter.
/// </summary>
private long CurrentTime
{
get
{
long l = 0;
QueryPerformanceCounter(out l);
return l;
}
}
/// <summary>
/// Indicates whether the Stopwatch timer is running.
/// </summary>
public bool IsRunning
{
get { return (_IsRunning); }
}
/// <summary>
/// Gets the total elapsed time measured by the current instance.
/// </summary>
public TimeSpan Elapsed
{
get { return new TimeSpan(this.ElapsedTicks); }
}
/// <summary>
/// Gets the total elapsed time measured by the current instance, in milliseconds
/// </summary>
public long ElapsedMilliseconds
{
get
{
if (_Elapsed == 0) return 0;
return (long)(((double)_Elapsed / _CounterFrequency) * 1000);
}
}
/// <summary>
/// Gets the total elapsed time measured by the current instance, in timer ticks
/// </summary>
public long ElapsedTicks
{
get
{
return (long)(this.ElapsedMilliseconds * TimeSpan.TicksPerMillisecond);
}
}
}

```

kg-card-end: html

Did you ever wonder **how the QueryPerformance* Win32 API functions work their magic** and provide accurate near-nanosecond timing results? There's some [interesting trivia about these functions](https://web.archive.org/web/20060420230123/http://www.mattwalsh.com/twiki/bin/view/Main/HighFrequencyCounterInC) on Matt Walsh's wiki.

[.net](https://blog.codinghorror.com/tag/net/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[stopwatch](https://blog.codinghorror.com/tag/stopwatch/)
[performance testing](https://blog.codinghorror.com/tag/performance-testing/)
