---
title: "Analyzing the complexity of the Stacks Project graphs"
date: 2013-07-31
url: https://mathbabe.org/2013/07/31/analyzing-the-complexity-of-the-stacks-project-graphs/
word_count: 713
---


So [yesterday I told you about the cool new visualizations](https://mathbabe.org/2013/07/30/the-stacks-project-gets-ever-awesomer-with-new-viz/) now available on [Johan’s Stack Project](http://stacks.math.columbia.edu/).


But how do we use these visualizations to infer something about either mathematics or, at the very least, the way we *think* about mathematics? Here’s one way we thought of with [Pieter](http://pbelmans.wordpress.com/).


So, there’s a bunch of results, and each of them has its own subgraph of the entire graph which positions that result as the “base node” and shows all the other results which it logically depends on.


And each of those graphs has structure and attributes, the stupidest two of which are the just counts of the nodes and edges. So for each result, we have an ordered pair (#nodes, #edges). What can we infer about mathematics from these pairs?


Here’s a scatter plot of the nodes-vs-edges for each of the 10,445 results (email me if you want to play with this data yourself):


I also put a best-fit line in, just to illustrate that the scatter plot is super linear but not perfectly linear.


So there are a bunch of comments I can make about this, but I’ll limit myself to the following:

1. There are a *lot* of points at (1,0), corresponding to remarks, axioms, beginning lemmas, definitions, and tags for sections.
2. As a data person, let me just say that data is *never this clean*. There’s something going on, some internal structure to these graphs that we should try to understand.
3. By “clean” I’m not exactly referring to the fact that things look pretty linear, although that’s weird and we should think about that. What I really mean is that things are so close to the curve that is being approximated. They’re all within a very tight border of this imaginary line. It’s super amazing.
4. Let’s pretend it’s just plain straight. Does that make sense, that as graphs get more complex the edges don’t get more dense than some multiple (1.86) of of the number of nodes?
5. Kind of: remember, we don’t depict all logical dependency edges, just the ones that are directly referred to in the proof of a result. So right off the bat you are less surprised that the edges aren’t growing quadratically in the number of nodes, even though the number of possible edges is of course quadratic in the number of nodes.
6. Think about it this way: assume that every result that requires proof (so, that’s not a (1,0) result) refers to exactly 2 other results in its proof. Then those two child results each correspond to some subgraph of the entire graph, and say their subgraphs each have something like twice as many edges as nodes. Then, ignoring overlap, we’d see two graphs with a 2:1 ratio, then we’d see that parent node, plus two edges leading to each result, which is also a 2:1 ratio, and the disjoint union of all those graphs gives us a large graph with a 2:1 ratio.
7. Then if you imagine now allowing the overlap, the ratio goes down a bit on average. In this toy model, the discrepancy between 2.0 and the slope we actually see, 1.86, is a measurement of the collapse of the two child graphs, which can be taken as a proxy for how much the two supporting results overlap as notions.
8. Of course, not every result has exactly two children.
9. Plus it doesn’t really explain how ridiculously consistent the plot above is. What would?
10. If you think about it, the only real explanation of the consistency above is my husband brain.
11. In other words, he’s humming along, thinking about stacks, and at some point, when he thinks things have gotten complicated enough, he says to himself “It’s time to wrap this stuff up and call it a result!” and then he does so. That moment, when he’s decided things are getting complicated enough, is very consistent internally to his brain.
12. In other words, if someone else created the stacks project, I’d expect to see another kind of plot, possibly also very consistent, but possibly with a different slope.
13. Also it’d be interesting to compare this plot to another kind of citation network graph, like the papers in the arXiv. Has anyone made that?
