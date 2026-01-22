---
title: "Do Charter Schools Cherrypick Students?"
date: 2015-11-19
url: https://mathbabe.org/2015/11/19/do-charter-schools-cherrypick-students/
word_count: 591
---


Yesterday I looked into quantitatively measuring the rumor I’ve been hearing for years, namely that charter schools cherrypick students – get rid of troublesome ones, keep well-behaved ones, and so on.


Here are two pieces of anecdotal evidence. There was a [“Got To Go” list of students](http://www.nytimes.com/2015/10/30/nyregion/at-a-success-academy-charter-school-singling-out-pupils-who-have-got-to-go.html?_r=0) at one charter school in the Success Academy network. These were troublesome kids that the school was pushing out.


Also, I recently learned that [Success Academy doesn’t accept new kids after the fourth grade](http://ny.chalkbeat.org/2015/04/06/success-academy-a-guide-to-the-citys-largest-most-controversial-charter-school-network/#.Vk25Y9-rRE4). Their reasoning is that older kids wouldn’t be able to catch up with the rest of the kids, but on the other hand it also means that kids kicked out of one school will never land there. This is another form of selection.


Now that I’ve said my two examples I realize they both come from Success Academy. There really aren’t that many of them, as [you can see on this map](http://www.successacademies.org/schools/), but they are a politically potent force in the charter school movement.


Also, to be clear, I am not against charter schools as a concept. I love the idea of experimentation, and to the extent that charter schools perform experiments that can inform how public schools run, that’s interesting and worthwhile.


Anyhoo, let’s get to the analysis. I got my data from [this DOE website](http://schools.nyc.gov/Accountability/tools/report/default.htm), down at the bottom where I clicked “citywide results” and grabbed the following excel file:

- [2014-2015 School Quality Reports Results for elementary, middle, and K-8 schools](http://schools.nyc.gov/NR/rdonlyres/06F7DE89-AA46-4509-9A0C-600038728D14/0/2014_2015_EMS_SQR_Results_2015_11_17.xlsx)


With that data, I built an iPython Notebook which is on github [here](https://github.com/mathbabe/Charter/blob/master/Charter%20School%20EDA.ipynb) so you can take a look, reproduce my results with the above data (I removed the first line after turning it in to a csv file), or do more.


From talking to friends of mine who run NYC schools, I learned of two proxies for difficult students. One is ‘Percent Students with Disabilities’ and the other is ‘Percent English Language Learners’ (I also learned that charter schools’ DBN code starts with 84). Equipped with that information, I was able to build the following histograms:


![Percent Students with Disabilities non-charter](https://mathbabe.org/wp-content/uploads/2015/11/percent-students-with-disabilities-non-charter.png?w=595)


Percent Students with Disabilities, non-Charter


![Percent Students with Disabilities charter](https://mathbabe.org/wp-content/uploads/2015/11/percent-students-with-disabilities-charter.png?w=595)


Percent Students with Disabilities, Charter


![Percent English Language Learners non-charter](https://mathbabe.org/wp-content/uploads/2015/11/percent-english-language-learners-non-charter.png?w=595)


Percent English Language Learners, non-Charter


![Percent English Language Learners, Charter.png](https://mathbabe.org/wp-content/uploads/2015/11/percent-english-language-learners-charter.png?w=595)


Percent English Language Learners, Charter. Please note that the x-axis differs from above.


I also computed statistics which you can look at [on the iPython notebook](https://github.com/mathbabe/Charter/blob/master/Charter%20School%20EDA.ipynb). Finally, I put it all together with a single scatterplot:


The blue dots to the left and all the way down on the x-axis are mostly test schools and “screened” schools, which are actually constructed to cherrypick their students.


The main conclusion of this analysis is to say that, generally speaking, charter schools don’t have as many kids with disabilities or poor language skills, and so when we compare their performance to non-charter schools, we need to somehow take this into account.


A final caveat: we can see just by looking at the above scatter plot that there are plenty of charter schools that are well inside the middle of the blue cloud. So this is not a indictment on any specific charter school, but rather a statistical statement about wanting to compare apples to apples.


Update: I’ve now added [t-tests](https://en.wikipedia.org/wiki/Welch%27s_t_test) to test the hypothesis that this data comes from the same distribution. The answer is no.


![Screen Shot 2015-11-19 at 11.06.13 AM](https://mathbabe.org/wp-content/uploads/2015/11/screen-shot-2015-11-19-at-11-06-13-am.png?w=595)


Those very small numbers are the p-values which are much smaller than 0.05. Other t-tests give similar results (but go ahead and try them yourself)
