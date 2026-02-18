---
title: "Day 31: Binary trees with core.logic!"
date: 2013-11-20
url: https://jvns.ca/blog/2013/11/20/day-31-logic-programming-pretty-music/
slug: day-31-logic-programming-pretty-music
word_count: 324
---


TODAY WAS FUN.


In the morning I paired with [Will Byrd](http://webyrd.net/) on some
logic programming. We worked on implementing binary search trees with
`core.logic` in Clojure. We got somewhere! My favorite thing about
logic programming is that all the functions end with ‘o’.


Here is what our code looked like:


```
(ns core-logic-search-tree.core
  (:refer-clojure :exclude [==])
  (:require
   [clojure.core.logic.fd :as fd]
   [clojure.core.logic :refer [== fresh conde run]]))

(def my-tree
  [:value 6
   :left [:value 4
          :left [:value 3 :left nil :right nil]
          :right [:value 5 :left nil :right nil]]
   :right nil])

(defn containso [tree x]
   (fresh [v l r]
           (fd/in v (fd/interval 0 2000))
           (== tree [:value v :left l :right r])
           (conde
            [(fd/== v x)]
            [(fd/> v x) (containso l x)]
            [(fd/< v x) (containso r x)])))

```


Then we could run


```
(run 1 [q] (containso my-tree 3))

```


and it would say that the tree contains 3. Which is okay! But the
really fun part is that you can run it “backwards” and ask


```
(run 10 [q] (containso q 3))

```


and get 10 trees that contain 3:


```
(
[:value 3 :left _0 :right _1]
[:value 4 :left [:value 3 :left _0 :right _1] :right _2]
[:value 0 :left _0 :right [:value 3 :left _1 :right _2]]
[:value 5 :left [:value 3 :left _0 :right _1] :right _2]
[:value 6 :left [:value 3 :left _0 :right _1] :right _2]
[:value 1 :left _0 :right [:value 3 :left _1 :right _2]]
[:value 7 :left [:value 3 :left _0 :right _1] :right _2]
[:value 8 :left [:value 3 :left _0 :right _1] :right _2]
[:value 2 :left _0 :right [:value 3 :left _1 :right _2]]
[:value 9 :left [:value 3 :left _0 :right _1] :right _2])

```


If you inspect carefully, you will see that those are all binary trees
and they all contain 3! =)


I am also doing magical music magic with Lyndsey, but that will have
to wait until tomorrow
