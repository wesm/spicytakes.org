---
title: "BISG Methodology"
date: 2016-08-29
url: https://mathbabe.org/2016/08/29/bisg-methodology/
word_count: 936
---


I’ve been tooling around with the slightly infamous [BISG methodology](http://files.consumerfinance.gov/f/201409_cfpb_report_proxy-methodology.pdf) lately. It’s a simple concept which takes the last name of a person, as well as the zip code of their residence, and imputes the probabilities of that person being of various races and ethnicities using the [Bayes updating rule](https://en.wikipedia.org/wiki/Bayes%27_rule).


The methodology is implemented with the most recent U.S. census data and critically relies on the fact that segregation is widespread in this country, especially among whites and blacks, and that Asian and Hispanic last names are relatively well-defined. It’s not a perfect methodology, of course, and it breaks down in the cases that people marry people of other races, or there are names in common between races, and especially when they live in diverse neighborhoods.


The BISG methodology came up recently in [this article](http://www.latimes.com/business/la-fi-rand-elliott-20160824-snap-story.html) (hat tip Don Goldberg) about the man who invented it and the politics surrounding it. Specifically, it was recently used by the CFPB to infer disparate impact in auto lending, and the Republicans who side with auto lending lobbyists called it “junk science.” I blogged about this [here](https://mathbabe.org/2015/11/11/republicans-would-let-car-dealers-continue-racist-practices-undeterred/) and, even earlier, [here](https://mathbabe.org/2015/10/02/the-tricky-thing-about-disparate-impact/).


Their complaints, I believe, center around the fact that the methodology, being based on the entire U.S. population, isn’t entirely accurate when it comes to auto lending, or for that matter when it comes to mortgages, which was the CFPB’s “ground truth” testing arena.


And that’s because minorities basically have less wealth, due to a bunch of historical racist reasons, but the upshot is that this methodology assumes a random sampling of the U.S. population but what we actually see in auto financing isn’t random.


Which begs the question, why don’t we update the probabilities with the known distribution of auto lending? That’s the thing about Bayes Law, we can absolutely do that. And once we did that, the Republican’s complaint would disappear. Please, someone tell me what I’m misunderstanding.


Between you and me, I think the real gripe is something along the lines of the so-called voter fraud problem, which is not really a problem statistically but since examples can be found of mistakes, we might imagine they’re widespread. In this case, the “mistake” is a white person being offered restitution for racist auto lending practices, which happens, and is a strange problem to have, but needs to be compared to *not* offering restitution to a lot of people who actually deserve it.


Anyhoo, I’m planning to add the below code to github, but I recently purchased a new laptop and I haven’t added a public key yet, so I’ll get to it soon. To be clear, the below code isn’t perfect, and it only uses zip code whereas a more precise implementation would use addresses. I’m supplying this because I didn’t find it online in python, only in STATA or something crazy expensive like that. Even so, I stole their munged census data, which you can too, from [this github page](https://github.com/cfpb/proxy-methodology/tree/master/input_files).


Also, I can’t seem to get the python spacing to work in WordPress, so this is really pretty terrible, but python users will be able to figure it out until I can get it on github.


%matplotlib inline


import numpy

import matplotlib

from pandas import *

import pylab

pylab.rcParams[‘figure.figsize’] = 16, 12


#Clean your last names and zip codes.


def get_last_name(fullname):

parts_list = fullname.split(‘ ‘)

while parts_list[-1] in [”, ‘ ‘,’ ‘,’Jr’, ‘III’, ‘II’, ‘Sr’]:

parts_list = parts_list[:-1]

if len(parts_list)==0:

return “”

else:

return parts_list[-1].upper().replace(“‘”, “”)


def clean_zip(fullzip):

if len(str(fullzip))<5:

return 0

else:

try:

return int(str(fullzip)[:5])

except:

return 0


Test = read_csv(“file.csv”)

Test[‘Name’] = Test[‘name’].map(lambda x: get_last_name(x))

Test[‘Zip’] = Test[‘zip’].map(lambda x: clean_zip(x))


#Add zip code probabilities. Note these are probability of living in a specific zip code given that you have a given race. They are extremely small numbers.


F = read_stata(“zip_over18_race_dec10.dta”)

print “read in zip data”


names =[‘NH_White_alone’,’NH_Black_alone’, ‘NH_API_alone’, ‘NH_AIAN_alone’,       ‘NH_Mult_Total’, \

‘Hispanic_Total’,’NH_Other_alone’]


trans = dict(zip(names, [‘White’, ‘Black’, ‘API’, ‘AIAN’, ‘Mult’, ‘Hisp’, ‘Other’]))

totals_by_race = [float(F[r].sum()) for r in names]

sum_dict = dict(zip(names, totals_by_race))


#I’ll use the generic_vector down below when I don’t have better name information


generic_vector = numpy.array(totals_by_race)/numpy.array(totals_by_race).sum()


for r in names:

F[‘pct of total %s’ %(trans[r])] = F[r]/sum_dict[r]


print “ready to add zip probabilities”


def get_zip_probs(zip):

G = F[F[‘ZCTA5’]==str(zip)][[‘pct of total White’,’pct of total Black’, ‘pct of total API’, \

‘pct of total AIAN’, ‘pct of total Mult’, ‘pct of total Hisp’, \

‘pct of total Other’]]

if len(G.values)>0:

return numpy.array(G.values[0])

else:

print “no data for zip = “, zip

return numpy.array([1.0]*7)


Test[‘Prob of zip given race’] = Test[‘Zip’].map(lambda x: get_zip_probs(x))


#Next, compute the probability of each race given a specific name.


Names = read_csv(“app_c.csv”)


print “read in name data”


def clean_probs(p):

try:

return float(p)

except:

return 0.0


for cat in [‘pctwhite’, ‘pctblack’, ‘pctapi’, ‘pctaian’, ‘pct2prace’, ‘pcthispanic’]:

Names[cat] = Names[cat].map(lambda x: clean_probs(x)/100.0)


Names[‘pctother’] = Names.apply(lambda row: max (0, 1 – float(row[‘pctwhite’]) – \

float(row[‘pctblack’]) – float(row[‘pctapi’]) – \

float(row[‘pctaian’]) – float(row[‘pct2prace’]) – \

float(row[‘pcthispanic’])), axis = 1)


print “ready to add name probabilities”


def get_name_probs(name):

G = Names[Names[‘name’]==name][[‘pctwhite’, ‘pctblack’, ‘pctapi’, ‘pctaian’,  ‘pct2prace’, ‘pcthispanic’, ‘pctother’]]

if len(G.values)>0:

return numpy.array(G.values[0])

else:

return generic_vector


Test[‘Prob of race given name’] = Test[‘Name’].map(lambda x: get_name_probs(x))


#Finally, use the Bayesian updating formula to compute overall probabilities of each race.


Test[‘Prod’] = Test[‘Prob of zip given race’]*Test[‘Prob of race given name’]

Test[‘Dot’] = Test[‘Prod’].map(lambda x: x.sum())

Test[‘Final Probs’] = Test[‘Prod’]/Test[‘Dot’]


Test[‘White Prob’] = Test[‘Final Probs’].map(lambda x: x[0])

Test[‘Black Prob’] = Test[‘Final Probs’].map(lambda x: x[1])

Test[‘API Prob’] = Test[‘Final Probs’].map(lambda x: x[2])

Test[‘AIAN Prob’] = Test[‘Final Probs’].map(lambda x: x[3])

Test[‘Mult Prob’] = Test[‘Final Probs’].map(lambda x: x[4])

Test[‘Hisp Prob’] = Test[‘Final Probs’].map(lambda x: x[5])

Test[‘Other Prob’] = Test[‘Final Probs’].map(lambda x: x[6])
