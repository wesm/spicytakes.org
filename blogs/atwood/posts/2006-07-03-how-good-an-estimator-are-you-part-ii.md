---
title: "How Good an Estimator Are You? Part II"
date: 2006-07-03
url: https://blog.codinghorror.com/how-good-an-estimator-are-you-part-ii/
slug: how-good-an-estimator-are-you-part-ii
word_count: 719
---

Here are the answers to the quiz presented in [How Good an Estimator Are You?](https://blog.codinghorror.com/how-good-an-estimator-are-you/)


If you’re concerned that a quiz like this has nothing to do with software development, consider:


> In software, you aren’t often asked to estimate the volume of the Great Lakes or the surface temperature of the sun. Is it reasonable to expect you to be able to estimate the amount of U.S. currency in circulation or the number of books published in the U.S., especially if you’re not in the U.S.?
> Software developers are often asked to estimate projects in unfamiliar business areas, projects that will be implemented in new technologies, the impacts of new programming tools on productivity, the productivity of unidentified personnel, and so on. Estimating in the face of uncertainty is business as usual for software estimators. The rest of [the book [Software Estimation](http://www.amazon.com/exec/obidos/ASIN/0735605351): Demystifying the Black Art] explains how to succeed in such circumstances.


If you haven’t read the entry with the quiz questions, please read it now before reading any further, so you’ll have an opportunity to try it before seeing the answers.

kg-card-begin: html


| **Question** | **Answer** |
| Surface temperature of the sun | 10,000F / 6,000C |
| Latitude of Shanghai | 31 degrees North |
| Area of the Asian continent | 17,139,000 square miles
44,390,000 square kilometers |
| The year of Alexander the Great's birth | 356 BC |
| Total value of U.S. currency in circulation in 2004 | $719.9 billion |
| Total volume of the Great Lakes | 5,500 cubic miles
23,000 cubic kilometers
2.4 x 10^22 cubic feet
6.8 x 10^20 cubic meters
1.8 x 10^23 U.S. gallons
6.8 x 10^23 liters |
| Worldwide box office receipts for the movie *Titanic* | $1.835 billion |
| Total length of the coastline of the Pacific Ocean | 84,300 miles
135,663 kilometers |
| Number of book titles published in the U.S. since 1776 | 22 million |
| Heaviest blue whale ever recorded | 380,000 pounds
190 English tons
170,000 kilograms
170 metric tons |


kg-card-end: html

The specific goal of the exercise was to **estimate at the 90 percent confidence level**. There are 10 questions in the quiz, so if you were truly estimating at a 90 percent confidence level, you would have gotten about 9 answers correct.


McConnell gives this quiz to every participant in his estimation course. The results are pictured in the chart below.


![](https://blog.codinghorror.com/content/images/2025/05/image-327.png)


He offers this analysis of the data:


> For the test takers whose results are shown in the figure, the average number of correct answers is 2.8. Only 2 percent of quiz takers score 8 or more correct answers. No one has ever gotten 10 correct. **I’ve concluded that most people’s intuitive sense of “90% confident” is really comparable to something closer to “30% confident.”** Other studies have confirmed this basic finding (Zultner 1999, Jrgensen 2002).


Additionally, the few people who manage to get close to the goal of ~9 correct answers typically feel they did something wrong:


> When I find the rare person who gets 7 or 8 answers correct, I ask “How did you get that many correct?” The typical response? “I made my ranges too wide.”
> My response is, “No, you didn’t! You didn’t make your ranges wide enough!” If you get only 7 or 8 correct, your ranges were still too narrow to include the correct answer as often as you should have.
> **We are conditioned to believe that estimates expressed as narrow ranges are more accurate than estimates expressed as wider ranges. We believe that wide ranges make us appear ignorant or incompetent.** The opposite is usually the case.


So, what have we learned from this exercise?

- When you ask someone for a range that provides 90% confidence, expect 30% confidence on average.
- People are naturally hesitant to provide wide ranges – even when the confidence level requires a wide range to be accurate – because they feel that narrow estimates are a sign of a better estimate.


Narrow estimates are self-defeating, but unfortunately they are human nature. Unless you have specific data that supports your narrow estimate, your estimate probably should be wider than you made it.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[estimation](https://blog.codinghorror.com/tag/estimation/)
[project management](https://blog.codinghorror.com/tag/project-management/)
[uncertainty](https://blog.codinghorror.com/tag/uncertainty/)
[software estimation](https://blog.codinghorror.com/tag/software-estimation/)
