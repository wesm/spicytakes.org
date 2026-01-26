---
title: "Class Instance Variable"
description: "When you learn about objects, you usually learn that they can   capture two kinds of data: instance and class. Instance variables are the   most common case, the data varies with each instance of the "
date: 2007-01-09T00:00:00
tags: ["language feature", "ruby"]
url: https://martinfowler.com/bliki/ClassInstanceVariable.html
slug: ClassInstanceVariable
word_count: 513
---


When you learn about objects, you usually learn that they can
  capture two kinds of data: instance and class. Instance variables are the
  most common case, the data varies with each instance of the object. Class
  variables, often referred to as static variables, are shared across all
  instances of a class. Every instance points to same value and any
  changes are seen by all. Class variables are much less common than
  instance variables, especially mutable class variables.


A particular wrinkle with class variables is how they interact
  with inheritance. Consider a class variable that's used to store
  instances of itself. (If the ruby is unfamiliar see my [reading guide](../articles/readingRuby.html).)


```

#ruby
class Employee
  @@instances = []
  def self.instances
    return @@instances
  end
  def store
    @@instances << self
  end
  def initialize name
    @name = name
  end
end

Employee.new('Martin').store
Employee.new('Roy').store
Employee.new('Erik').store

puts Employee.instances.size

```


No suprise here, there are three employees. But now try this.


```

#ruby
class Employee
  @@instances = []
  def self.instances
    @@instances
  end
  def store
    @@instances << self
  end
  def initialize name
    @name = name
  end
end

class Programmer < Employee; end
class Overhead < Employee; end

Overhead.new('Martin').store
Overhead.new('Roy').store
Programmer.new('Erik').store

puts Overhead.instances.size
puts Programmer.instances.size


```


The output here is 3 and 3, while we'd probably prefer 2 and 1. The
  reason is that a class variable is  shared across all
  instances of a class, which includes all subclasses. There are two
  classes but only one variable.


Sometimes this variable across a hierarchy is exactly what we
  want, but sometimes, as in this case,  we'd prefer a different
  variable for each class. I first came across this concept in some later
  versions of Smalltalk under the name of class instance variable. You
  could refer to a class instance variable the same way as with a
  class variable, but you got a different value per class.


Support for class instance variables isn't common in OO
  languages, but it's not too hard to it yourself. The obvious way is
  to use a dictionary keyed by class name.


```

#ruby
class Employee
  @@instances = {}
  def self.instances
    @@instances[self]
  end
  def store
    @@instances[self.class] ||= []
    @@instances[self.class] << self
  end
  def initialize name
    @name = name
  end
end

class Overhead < Employee; end
class Programmer < Employee; end

Overhead.new('Martin').store
Overhead.new('Roy').store
Programmer.new('Erik').store
puts Overhead.instances.size
puts Programmer.instances.size

```


You can use this technique in any OO language. Ruby, however,
  actually has class instance variables.


```
#ruby
class Employee
  class << self; attr_accessor :instances; end
  def store
    self.class.instances ||= []
    self.class.instances << self
  end
  def initialize name
    @name = name
  end
end

class Overhead < Employee; end
class Programmer < Employee; end

Overhead.new('Martin').store
Overhead.new('Roy').store
Programmer.new('Erik').store
puts Overhead.instances.size
puts Programmer.instances.size

```


The definition of the class instance variable is the fragment
`class << self; attr_accessor :instances; end`.
For reasons that I don't really want to go into, this defines an instance
variable (and getters and setters) on the class employee that's
inherited by its descendents. Unlike class variables these class
instance variables will take different values for each class object.


Class instance variables are pretty rare, but useful when you do
	need them.
