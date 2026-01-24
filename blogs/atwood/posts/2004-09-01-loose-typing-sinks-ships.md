---
title: "Loose Typing Sinks Ships"
date: 2004-09-01
url: https://blog.codinghorror.com/loose-typing-sinks-ships/
slug: loose-typing-sinks-ships
word_count: 532
---

The recent release of [IronPython](http://ironpython.com/) .NET, and Microsoft’s subsequent hiring of its creator, got me thinking about typing. There’s a really interesting, albeit old, post on the [dubious benefit of strong typing](https://web.archive.org/web/20041009162135/http://mindview.net/WebLog/log-0025) at Bruce Eckel’s blog. Which reminds me **how much I hate constantly casting objects via CType() and DirectCast()**. It’s a waste of my time – a productivity tax. You can disregard my opinion, sure, but Eckel is the author of [Thinking in Java](http://www.amazon.com/exec/obidos/tg/detail/-/0131002872/qid=1094069203/sr=8-1/ref=pd_ka_1/104-5563168-1958300?v=glance&s=books&n=507846). And he’s not the only one that feels this way:


> *I also realized that the flexibility of dynamically typed languages makes writing code significantly easier. Modules are easier to write, and easier to change. There are no build time issues at all. Life in a dynamically typed world is fundamentally simpler. Now I am back programming in Java because the projects I’m working on call for it. But I can’t deny that I feel the tug of the dynamically typed languages. I wish I was programming in Ruby or Python, or even Smalltalk.*


That’s from [Robert Martin](http://www.artima.com/weblogs/viewpost.jsp?thread=4639), author of [Designing Object Oriented C++ Applications Using The Booch Method](http://www.amazon.com/exec/obidos/ASIN/0132038374/qid=1094069343/sr=ka-3/ref=pd_ka_3/104-5563168-1958300), among other books.


So why do we do it? Why define a class like this, with all the overhead of inheritance:

kg-card-begin: html

```
// Speaking pets in Java:
interface Pet {
void speak();
}
class Cat implements Pet {
public void speak() { System.out.println("meow!"); }
}
class Dog implements Pet {
public void speak() { System.out.println("woof!"); }
}
public class PetSpeak {
static void command(Pet p) { p.speak(); }
public static void main(String[] args) {
Pet[] pets = { new Cat(), new Dog() };
for(int i = 0; i < pets.length; i++)
command(pets[i]);
}
}
```

kg-card-end: html

Now compare that to the Python version:


> *Python and similar “weak” or “latently” typed languages are very lazy about type checking. Instead of putting the strongest possible constraints upon the type of objects, as early as possible (as C++ and Java do), languages like Ruby, Smalltalk and Python put the loosest possible constraints on types, and evaluate types only if they have to. **That is, you can send any message to any object, and the language only cares that the object can accept the message – it doesn’t require that the object be a particular type, as Java and C++ do.***

kg-card-begin: html

```
# Speaking pets in Python, but without base classes:
class Cat:
def speak(self):
print "meow!"
class Dog:
def speak(self):
print "woof!"
class Bob:
def bow(self):
print "thank you, thank you!"
def speak(self):
print "hello, welcome to the neighborhood!"
def drive(self):
print "beep, beep!"
def command(pet):
pet.speak()
pets = [ Cat(), Dog(), Bob() ]
for pet in pets:
command(pet)
```

kg-card-end: html

In other words, you call methods on objects without the unnecessary complexity of inheritance, and most of all without the mind-numbing cast-a-thon that strong typing requires. So the question is, **do you want to be correct and pure, or do you want to be productive?** However good you are, three Indian programmers can churn out mechanical code blocks a lot faster than you can – and for the same price. Choose carefully.

[dynamic typing](https://blog.codinghorror.com/tag/dynamic-typing/)
[strong typing](https://blog.codinghorror.com/tag/strong-typing/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[typing constraints](https://blog.codinghorror.com/tag/typing-constraints/)
