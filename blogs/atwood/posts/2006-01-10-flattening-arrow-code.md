---
title: "Flattening Arrow Code"
date: 2006-01-10
url: https://blog.codinghorror.com/flattening-arrow-code/
slug: flattening-arrow-code
word_count: 478
---

I often encounter code like this:

kg-card-begin: html

```
if (rowCount > rowIdx)
{
  if (drc[rowIdx].Table.Columns.Contains("avalId")
  {
    do
    {
      if (Attributes[attrVal.AttributeClassId] == null)
      {
        // do stuff
      }
      else
      {
        if (!(Attributes[attrVal.AttributeClassId] is ArrayList))
        {
          // do stuff
        }
        else
        {
          if (!isChecking)
          {
            // do stuff
          }
          else
          {
            // do stuff
          }
        }
      }
      rowIdx++;
    }
    while (rowIdx < rowCount && GetIdAsInt32(drc[rowIdx]) == Id);
  }
  else
    rowIdx++;
}
return rowIdx;

```

kg-card-end: html

The excessive nesting of conditional clauses pushes the code out into an arrow formation:

kg-card-begin: html


| if
  if
    if
      if
        do something
      endif
    endif
  endif
endif |  |


kg-card-end: html

And you know you’re definitely in trouble when **the code you’re reading is regularly exceeding the right margin on a typical 1280x1024 display**. This is the [Arrow Anti-Pattern](http://c2.com/cgi/wiki?ArrowAntiPattern) in action.


One of my primary refactoring tasks is “flattening” arrow code like this. Those sharp, pointy barbs are dangerous! Arrow code has a high [cyclomatic complexity](http://www.sei.cmu.edu/str/descriptions/cyclomatic_body.html) value – a measure of how many distinct paths there are through code:


> **Studies show a correlation between a program’s cyclomatic complexity and its error frequency**. A low cyclomatic complexity contributes to a program’s understandability and indicates it is amenable to modification at lower risk than a more complex program. A module’s cyclomatic complexity is also a strong indicator of its testability.


Where appropriate, I flatten that arrow code by doing the following:

1. **Replace conditions with guard clauses.** This code...

kg-card-begin: html

```
if (SomeNecessaryCondition)
{
  // function body code
}

```

kg-card-end: html

... works better as a guard clause:

kg-card-begin: html

```
if (!SomeNecessaryCondition)
{
throw new RequiredConditionMissingException;
}
// function body code
```

kg-card-end: html
1. **Decompose conditional blocks into separate functions.** In the above example, we’re in a do... while loop which could be decomposed:

kg-card-begin: html

```
do
{
  ValidateRowAttribute(drc[rowIdx]);
  rowIdx++;
}
while(rowIdx < rowCount && GetIdAsInt32(drc[rowIdx]) == Id);
```

kg-card-end: html
1. **Convert negative checks into positive checks.** As a broad rule, I prefer to put the positive comparison first and let the negative comparison fall out naturally into the else clause. I think this reads a lot better and, more importantly, avoids the “I ain't not never doing that” syndrome:

kg-card-begin: html

```
if (Attributes[attrVal.AttributeClassId] is ArrayList)
{
  // do stuff
}
else
{
  // do stuff
}
```

kg-card-end: html
1. **Always opportunistically return as soon as possible from the function.** Once your work is done, get the heck out of there! This isn’t always possible – you might have resources you need to clean up. But whatever you do, you have to abandon the ill-conceived idea that there should only be one exit point at the bottom of the function.


The goal is to have code that scrolls vertically a lot… but not so much horizontally.

[code refactoring](https://blog.codinghorror.com/tag/code-refactoring/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[nested conditions](https://blog.codinghorror.com/tag/nested-conditions/)
[clean code](https://blog.codinghorror.com/tag/clean-code/)
[readability](https://blog.codinghorror.com/tag/readability/)
