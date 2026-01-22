---
title: "Three Ideas for defusing Weapons of Math Destruction"
date: 2016-06-03
url: https://mathbabe.org/2016/06/03/three-ideas-for-defusing-weapons-of-math-destruction/
word_count: 772
---


*This is a guest post by [Kareem Carr](http://scholar.harvard.edu/kareemcarr/home), a data scientist living in the Cambridge. He’s a fellow at Harvard’s Institute of Quantitative Social Science and an associate computational biologist at the Broad Institute of Harvard and MIT. Formerly, he has held positions at Harvard’s Molecular and Cellular Biology Department and the National Bureau of Economic Research.*


When your algorithms can potentially affect the way physicians treat their dying patients, it really brings home how critical it is to do data science right. I work at a biomedical research institute where I study cancer data and ways of using it to help make better decisions. It’s a tremendously rewarding experience. I get the chance to apply data science on a massive scale and in a socially relevant way. I am passionate about the ways in which we can use automated decision processes for social good and I spend the vast majority of my time thinking about data science.


A year ago, I started working on creating a framework for assessing performance of an algorithm used heavily in cancer research. The first part of the project involved gathering all the data that we could get our hands on. The datasets had been created by different processes and had various advantages and disadvantages. First, the most valued but labor-intensive category of datasets to create had been manually curated by multiple people. More plentiful were datasets that had not been manually curated, but had been assessed by so many different algorithms that they were considered extremely well-characterized. Finally, there were the artificial datasets that had been created by simulation and for which the truth was known, but which lacked the complexity and depth of real data. Each type of dataset required careful consideration of the type of evidence it provided for proper algorithm performance. I came to really understand that validation of an algorithm and characterization of the typical errors were an essential part of the data science. The project taught me a few lessons that I think might be generally applicable.


**Use open datasets**


In most cases, it is preferable that algorithms be open-source and available for all to examine. If algorithms must be closed-source and proprietary, then open, curated datasets are essential for comparisons among algorithms. These may include real data that has been cleared for general use, anonymized data or high-quality artificial data. Open datasets allow us to analyze algorithms even when they are too complex to understand or when the source code is hidden. We can observe where and when they make errors and discern patterns. We can determine in what circumstances other algorithms can be better. This insight can be extremely powerful when it comes to applying algorithms in the real world.


**Take manual curation seriously**


Domain-specific experts, such as doctors in medicine or coaches in sports, are generally a very powerful source of information. Panels of experts are even better. While humans are by no means perfect, when careful consideration of an algorithmic result by experts implies that the algorithm has failed, it’s important to take that message seriously. It’s important to investigate if and why the algorithm failed. Even if the problem is never fixed, it is important to understand the types of errors the algorithm makes and to measure its failure rate in various circumstances.


**Demand causal models**


While it has become very easy to build systems which generate high-performing black-box algorithms, we must push for explainable results wherever possible. Furthermore, we should demand truly causal models rather than the merely predictive. Predictive models perform well when there are no external modifications of the system. Causal models continue to be accurate despite exogenous shocks and policy interventions. Frequently, we create the former, yet try to deploy them as if they are the latter with disastrous consequences.


All three principles have one underlying idea. Bad data science obscures and ignores the real world performance of its algorithms. It relies on little to no validation. When it does perform validation, it relies on canned approaches to validation. It doesn’t critically examine instances of bad performance with an eye towards trying to understand how and why these failures occur. It doesn’t make the nature of these failures widely known so consumers of these algorithms can deploy them with discernment and sophistication.


Good data science does the opposite. It creates algorithms which are deeply and widely understood. It allows us to understand when algorithms fail and how to adapt to those failures. It allows us to intelligently interpret the results we receive. It leads to better decision making.


Let’s stop the proliferation of weapons of math destruction with better data science!
