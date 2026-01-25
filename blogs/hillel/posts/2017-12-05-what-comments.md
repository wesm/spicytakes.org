---
title: "Maybe Comments SHOULD Explain 'What'"
date: 2017-12-05
url: https://www.hillelwayne.com/post/what-comments/
slug: what-comments
word_count: 772
---

People say “Comments should explain why, not what.” I feel like starting a flame war today so I’m going to argue that comments should explain ‘what’ too. Please don’t use this as justification to write bad code, okay? Okay.


First of all, why *shouldn’t* comments explain ‘what’? If you need comments to explain what’s going on, it suggests your code is unclear. If I write


```
//weight, radius, price
w = 10, r = 9, p = 1

```


That’s not as clear as saying


```
weight = 10, radius = 9, price = 3

```


“But it’s obvious that `w` is `weight`!” Sure, if you’re seeing those lines back-to-back. But presumably you’re initializing the variable to use it, which means that it’s going to appear later. When you see `w` later in the body, you need to go back and check what it is. That’s a frustrating context switch and you may skip it, possibly assuming that `w` is… width. Then bad things happen. So comments are not a substitute for clean code.


Okay,  so why *should* comments explain why? Some people argue that we should instead store the ‘why’ in [commit messages](http://mentalized.net/journal/2014/09/01/commit-messages-deserve-care-and-tenderness/) or [tests](https://twitter.com/sarahmei/status/937881294788108288). Most people feel icky about this, though. Given:


```
// Clear twice to deal with bug ABC in library XYZ, see [link]
XYZ.clear(); XYZ.clear();

```


Would you prefer that comment be removed and placed in the commit message? Then if you want to learn why `XYZ.clear()` is repeated twice, you have to dig up the commit. That can be a difficult and tedious job, especially if the line was reformatted, moved between files, anything that makes `git blame` not work. Searching all that is a context switch and you may skip it, possibly assuming that it’s a bug you can remove. Then bad things happen.


Both of these cases share the same problem: looking things up is hard. Best case it’s a context switch that takes time away from understanding the problem. Worst case you don’t look it up and make a potentially-dangerous assumption. It’s better to keep the information in the exact same place that you need it, whether that’s via descriptive code or comments over commits.


Now for the weird part. What if your descriptive code forces a context switch? Let’s take the code from Bob Martin’s [Extract Till You Drop](https://sites.google.com/site/unclebobconsultingllc/one-thing-extract-till-you-drop).1


```
    String replace() {
      Pattern symbolPattern = Pattern.compile("\\$([a-zA-Z]\\w*)");
      Matcher symbolMatcher = symbolPattern.matcher(stringToReplace);
      while (symbolMatcher.find()) {
        String symbolName = symbolMatcher.group(1);
        if (getSymbol(symbolName) != null && !alreadyReplaced.contains(symbolName)) {
          alreadyReplaced.add(symbolName);
          stringToReplace = stringToReplace.replace("$" + symbolName, translate(symbolName));
        }
      }
      return stringToReplace;

```


To make it more understandable, he replaces it with this:


```
  String replace() {
      replaceAllSymbols();
      return stringToReplace;
    }

    private void replaceAllSymbols() {
      for (String symbolName = nextSymbol(); symbolName != null; symbolName = nextSymbol())
        replaceAllInstances(symbolName);
    }

    private String nextSymbol() {
      return symbolMatcher.find() ? symbolMatcher.group(1) : null;
    }

    private void replaceAllInstances(String symbolName) {
      if (shouldReplaceSymbol(symbolName))
        replaceSymbol(symbolName);
    }

    private boolean shouldReplaceSymbol(String symbolName) {
      return getSymbol(symbolName) != null && !alreadyReplaced.contains(symbolName);
    }

    private void replaceSymbol(String symbolName) {
      alreadyReplaced.add(symbolName);
      stringToReplace = stringToReplace.replace(
        symbolExpression(symbolName),
        translate(symbolName));
    }

    private String symbolExpression(String symbolName) {
      return "$" + symbolName;
    }

```


So much better, right?! `replace` is now two lines instead of ten. But now there’s six other methods you have to read to understand how the class works. “But it’s easier to follow.” Not if I’m trying to track down a bug and I have to keep scrolling up and down, jumping from method to method to understand the whole. Is that really so much better than using comments?


```
    String replace() {
      Pattern symbolPattern = Pattern.compile("\\$([a-zA-Z]\\w*)"); //f.ex $F1a3
      Matcher symbolMatcher = symbolPattern.matcher(stringToReplace);

      // Replace all symbols
      while (symbolMatcher.find()) {
        String symbolName = symbolMatcher.group(1);
        // translate will replace all instances; only need to run it once
        if (getSymbol(symbolName) != null && !alreadyReplaced.contains(symbolName)) {
          alreadyReplaced.add(symbolName);
          stringToReplace = stringToReplace.replace("$" + symbolName, translate(symbolName));
        }
      }
      return stringToReplace;

```


I think that’s more understandable than either the original case or the clean code case, because you don’t have to context switch to a different method to understand what’s going on. Obviously this isn’t always the case, and often comments are superfluous. I’m just saying that there are at least a few cases where writing a ‘what’ comment is the right choice, so we shouldn’t reject them out-of-hand.


Welp that’s my argument so flame war awaaaaaaaaaay


---

1. I feel like I pick on Uncle Bob a lot, so here’s an essay I agree with: [The Lurn](http://blog.cleancoder.com/uncle-bob/2016/09/01/TheLurn.html). I disagree with his assumption that we’ve reached the limits of PLT, but I strongly agree that we tend to overfetishize learning programming languages at the cost of other useful programming knowledge.
 [return]
