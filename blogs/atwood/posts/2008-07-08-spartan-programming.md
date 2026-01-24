---
title: "Spartan Programming"
date: 2008-07-08
url: https://blog.codinghorror.com/spartan-programming/
slug: spartan-programming
word_count: 461
---

As I grow older and wiser even older as a programmer, I’ve found that my personal coding style has trended heavily toward minimalism.


I was pleased, then, to find many of the coding conventions I’ve settled on over the last 20 years codified in [Spartan programming](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Spartan_programming).


![](https://blog.codinghorror.com/content/images/2025/04/image-174.png)


No, not that sort of [Spartan](http://en.wikipedia.org/wiki/Spartan_Army), although it is historically related. The particular meaning of **spartan** I’m referring to is this one:


> (adj.) ascetic, ascetical, austere, spartan (practicing great self-denial) “*Be systematically ascetic... do... something for no other reason than that you would rather not do it”* - William James; “*a desert nomad’s austere life”; “a spartan diet”; “a spartan existence”*


I’ve tried to [code smaller](https://blog.codinghorror.com/code-smaller/), even going so far as to write [no code at all](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/) when I can get away with it. Spartan programming aligns perfectly with these goals. You strive for **simultaneous minimization** of your code in many dimensions:

1. [Horizontal complexity](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Horizontal_complexity%2C_spartan_reduction_of). The depth of nesting of control structures.
2. [Vertical complexity](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Vertical_complexity%2C_spartan_reduction_of). The number of lines or length of code.
3. [Token count](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Token_count%2C_spartan_reduction_of).
4. [Character count](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Character_count%2C_spartan_reduction_of).
5. [Parameters](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Parameters%2C_spartan_reduction_of). The number of parameters to a routine or a generic structure.
6. [Variables](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Variables%2C_spartan_reduction_of).
7. Looping instructions. The number of iterative instructions and their nesting level.
8. Conditionals. The number of `if` and multiple branch `switch` statements.


The discipline of spartan programming means **frugal use of variables**:

1. Minimize *number* of variables. Inline variables which are used only once. Take advantage of `foreach` loops.
2. Minimize *visibility* of variables and other identifiers. Define variables at the smallest possible scope.
3. Minimize *accessibility* of variables. Prefer the greater encapsulation of `private` variables.
4. Minimize *variability* of variables. Strive to make variables `final` in Java and `const` in C++. Use annotations or restrictions whenever possible.
5. Minimize *lifetime* of variables. Prefer ephemeral variables to longer lived ones. Avoid persistent variables such as files.
6. Minimize *names* of variables. Short-lived, tightly scoped variables can [use concise, terse names](https://web.archive.org/web/20080712144603/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Terse_variable_naming).
7. Minimize *use of array* variables. Replace them with collections provided by your standard libraries.


It also means **frugal use of control structures**, with early `return` whenever possible. This is probably best illustrated with an actual example, starting with raw code and refactoring it using the spartan programming techniques:

- Applying Spartan programming techniques [to a C File](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/Spartan_programming_C_example)
- Applying Spartan programming techniques [to a Java function](https://web.archive.org/web/20081211181901/http://ssdl-wiki.cs.technion.ac.il/wiki/index.php/SendAnEmail_case_study)


I don’t agree with all the rules and guidelines presented here, but I was definitely nodding along with the majority of the page. **Minimalism isn’t always the right choice, but it’s rarely the *wrong* choice.** You could certainly do worse than to adopt the discipline of spartan programming on your next programming project.


(hat tip to Yuval Tobias for sending this link my way)

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[coding conventions](https://blog.codinghorror.com/tag/coding-conventions/)
