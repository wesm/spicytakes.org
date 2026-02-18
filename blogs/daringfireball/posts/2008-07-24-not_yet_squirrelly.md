---
title: "Not Yet Squirrelly"
date: 2008-07-24
url: https://daringfireball.net/2008/07/not_yet_squirrelly
slug: not_yet_squirrelly
word_count: 554
---


Regarding my [piece earlier this week](http://daringfireball.net/2008/07/webkit_performance_iphone) regarding the striking improvement in JavaScript performance in the version of WebKit in the iPhone 2.0 update, one question I had was whether this was perhaps attributable to Apple having already switched to SquirrelFish, the all-new JavaScript interpreter that the WebKit team unveiled in early June. Announcing the project, [Geoffrey Garen wrote](http://webkit.org/blog/189/announcing-squirrelfish/):


> SquirrelFish is fast — much faster than WebKit’s previous
> interpreter. Check out the numbers. On the [SunSpider JavaScript
> benchmark](http://webkit.org/perf/sunspider-0.9/sunspider.html), SquirrelFish is 1.6 times faster than WebKit’s
> previous interpreter.


But it struck me as exceedingly unlikely that a project that new — having only been unveiled in June — would be included in the iPhone 2.0 OS. And, as the benchmark results from the SquirrelFish announcement show, version 3.1 of WebKit’s *old* JavaScript interpreter is itself 2.7 times faster than version 3.0. WebKit’s JavaScript performance had improved dramatically over the past year even before SquirrelFish.


But I decided to check anyway. When in doubt, look at the source, and the source code for JavaScriptCore is available from Apple’s Darwin sources both [for Mac OS X 10.5.4](http://www.opensource.apple.com/darwinsource/10.5.4/) (which we know isn’t yet using SquirrelFish) and [for iPhone OS 2.0](http://www.opensource.apple.com/darwinsource/iPhone2.0/). Running both source trees through BBEdit’s Find Differences command shows that they’re very similar — the JavaScript interpreter in iPhone OS 2.0 is nearly identical to the one in Safari 3.1.2.


If you look at the source directory for the version of JavaScriptCore [in the current WebKit trunk](http://trac.webkit.org/browser/trunk/JavaScriptCore), which *has* switched to SquirrelFish, you can see just by scanning the file names, let alone the source code, that much has changed.


One practical improvement in SquirrelFish over the previous WebKit interpreter is with regard to recursion depth. (Recursion is when a function is written in such a way that it calls itself, sort of like the programming equivalent of nested Russian dolls. [See Wikipedia for more](http://en.wikipedia.org/wiki/Recursion).) WebKit’s old JavaScript interpreter had a relatively shallow recursion limit of 499; recurse 500 times in your JavaScript code and you’d get an exception. SquirrelFish supports far deeper recursion.


[Here’s a very simple test page](http://daringfireball.net/misc/test/squirrelfish) to test how deep a JavaScript interpreter can recurse. The entire source:


```
<script type="text/javascript">
function recurse(n) {
    if (n > 0) {
        return recurse(n - 1);
    }
    return 0;
}

try {
    // recurse(43687);  // Highest that works for me in WebKit
                        // nightly builds as of 24 Jul 2008.
    // recurse(2999);   // Highest that works for me in Firefox 3.0.1
    // recurse(499);    // Highest that works for me in Safari 3.1.2
    recurse(3000);
    document.write("Could be SquirrelFish.");
} catch(e) {
    document.write("Not SquirrelFish.");
}
</script>

```


It calls a simple recursive function 3000 times. Pre-SquirrelFish versions of WebKit fail with any number higher than 499. Firefox 3.0.1 works up to 2,999 recursions. A recent WebKit nightly, with SquirrelFish, worked for me up to 43,687, which is pretty deep. MobileSafari in iPhone OS 2.0 has the same limit as Safari 3.1.2: 499.


Recursion depth, in and of itself, isn’t particularly important. It’s just a particularly simple way to distinguish pre- and post-SquirrelFish versions of WebKit. And so since we now know that the iPhone isn’t yet using SquirrelFish, it means further dramatic performance improvements are on the horizon.



| **Previous:** | [WebKit Performance on iPhone OS 2.0](https://daringfireball.net/2008/07/webkit_performance_iphone) |
| **Next:** | [iPhone Calendar Syncing](https://daringfireball.net/2008/08/iphone_calendar_syncing) |


PreviousNext