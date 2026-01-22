---
title: "Forecasting precipitation"
date: 2015-12-28
url: https://mathbabe.org/2015/12/28/forecasting-precipitation/
word_count: 1657
---


What does it means when you’re given a precipitation forecast? And how do you know if it’s accurate? What does it mean when you see that there’s a 37% chance of rain?


Well, there are two input variables you have to keep in mind: first, the geographic location – where you’re looking for a forecast, and second, the time window you’re looking at.


For simplicity let’s fix a specific spot – say 116th and Broadway – and let’s also fix a specific one hour time window, say 1am-2am.


Now we can ask again, how would we interpret a “37% chance of rain” for this location during this time? And when do we decide our forecast is good? It’s trickier than you might think.


***


Let’s first think about interpretation. Hopefully what that phrase means is something like, 37 out of 100 times, with these exact conditions, you’ll see a non-zero, measurable amount of rain or other precipitation during an hour. So far so good.


Of course, we only have exactly one of these exact hours. So we cannot directly test the forecast with that one hour. Instead, we should collect a lot of data on the forecast. Start by building 101 bins, labeled from 0 to 100, and throw each forecasted hour into the appropriate bin, along with a record of the actual precipitation outcome.


So if it actually rains between 1am and 2am at 116th and Columbia, I’d throw this record into the “37” bin, along with a note that said “YES IT RAINED.” I’d short hand this note by attaching a “1” to the record, which stands for “100% chance of rain because it actually rained.” I’d attach a “0” to each hour where it didn’t rain.


I’d do this for every single hour of every single day and at every single location as well, of course not into the “37” bin but into the bin with the *forecasted* number, along with the note of whether rain came. I’d do this for 100 years, or at least 1, and by the end of it I’d presumably have a lot of data in each bin.


So for the “0” bin I’d have many many hours where there wasn’t supposed to be rain. Was there sometimes rain? Yeah, probably. So my “0” bin would have a bunch of records with “0” labels and a few with “1” labels. Each time a “1” record made its way into the “0” bin, it would represent a failure of the model. I’d need to count such a failure against the model somehow.


But then again, what about the “37” bin? Well I’d want to know, for all the hours forecasted to have a 37% chance of rain, how often it actually happened. If I ended up with 100 examples, I’d hope that 37 our of the 100 examples ended up with rain. If it actually happened 50 times out of 100, I’d be disappointed – another failure of the model. I’d need to count this against the model.


Of course to be more careful I’d rather have 100,000 examples accumulated in bin “37” and see 50,000 of those hours actually had rain. With that data I’d be fairly certain this forecasting engine is inaccurate.


Or, if 37,003 of those examples actually saw rain, then I’d be extremely pleased. I’d be happy to trust this model when it says 37% chance of rain. But then again, it might still be kind of inaccurate when it comes to the bin labeled “72”.


We’ve worked so hard to interpret the forecast that we’re pretty close to determining if it’s accurate. Let’s go ahead and finish the job.


***


Let’s take a quick reality check first though. Since I’ve already decided to fix on a specific location, namely at 116th and Broadway, the ideal forecast would always just be 1 or 0: it’s either going to rain or it’s not.


In other words, we have the ideal forecast to measure all other forecasts against. Let’s call that God’s forecast, or if you’re an atheist like me, call it “mother nature’s forecast,” or MNF for short. If you tried to test MNF, you’d set up your 101 bins but you’d only ever use 2 of them. And they’d always be right.


***


OK, but this is the real world, and forecasting weather is hard, especially when it’s a day or two in advance, so let’s try instead to compare two forecasts head to head. Which one is better, Google or [Dark Sky](http://darkskyapp.com/)?


I’d want a way to assign scores to each of them and choose the better precipitation model. Here’s how I’d do it.


First, I’d do the bin thing for each of them, over the same time period. Let’s say I’m still obsessed with my spot, 116th and Broadway, and I’ve fixed a year or two of hourly forecasts to compare the two models.


Here’s my method. Instead of rewarding a model for accuracy, I’m going to penalize it for inaccuracy. Specifically, I’ll assign it a squared error term for each time it forecast wrong.


To see how that plays out, let’s look at the “37” bin for each model. As we mentioned above, any time the model forecasts 37% chance of rain, it’s wrong. It either rains, in which case it’s off by 1.00-0.37 = 0.63, or it doesn’t rain, in which case the error term is 0.37. I will assign it the square of those terms as penalty for its wrongness.


***


How did I come up with the square of the error term? Why is it a good choice? For one, it has the following magical property: it will be minimized when the label “37” is the most accurate.


In other words, if we fix for a moment the records that end up in the “37” bin, the sum of the squared error terms will be the smallest when the true proportion of “1”s to “0”s in that bin is 37%.


Said another way, if we have 100,000 records in the “37” bin, and actually 50,000 of them correspond to rainy hours, then the sum of all the squared error terms ends up much bigger than if only 37,000 of them turned into rain. So that’s a way of penalizing a model for inaccuracy.


To be more precise, if our true chances of rain is  but our bin is actually labeled  then the average penalty term, assuming we’ve collected enough data to ignore measurement error, will be  or


The crucial fact is that  is always positive, so the above penalty term will be minimized when  is zero, or in other words when the label of the bin perfectly corresponds to the actual chance of rain.


Moreover, other ways of penalizing a specific record in the “37” bin, say by summing up the absolute value of the error term, don’t have this property.


***


The above has nothing to do with “bin 37,” of course. I could have chosen any bin. To compare two forecasting models, then, we add up all the squared error terms of all the forecasts over a fixed time period.


Note that any model that ever spits out “37” is going to get some error no matter what. Or in other words, a model that wants to be closer to MNF would minimize the number of forecasts to put into the “37” bin and try hard to put forecasts into either the “0” bin or the “1” bin, assuming of course that they had confidence in the forecast.


Actually, the worst of all bins – the one the forecast accumulates the most penalty for – is the “50” bin. Putting an hourly forecast into the “50” bin is like giving up – you’re going to get a big penalty no matter what, because again, it’s either going to rain or it isn’t. Said another way, the above error term  is maximized at .


But the beauty of the square error penalty is that it also rewards certainty. Another way of saying this is that, if I am a forecast and I want to improve my score, I can either:

1. make sure the forecasts in each bin are as accurate as possible, or
2. try to get some of the forecasts in each bin out of their current bins and closer to either 0 or 1.


Either way their total sum of square error will go down.


I’m dwelling on this because there’s a forecast out there that we want to make sure is deeply shamed by any self-respecting scoring system. Namely, the forecast that says there’s a n% chance of rain for every hour of every day, where n is chosen to be the average hourly chance of rain. This is a super dumb forecast, and we want to make sure it doesn’t score as well as God or mother nature, and thankfully it doesn’t (even though it’s perfectly accurate within each bin, and it only uses one bin).


Then again, it would be good to make sure Google scores better than the super dumb forecast, which I’d be happy to do if I could actually get my hands on this data.


***


One last thing. This entire conversation assumed that the geographic location is fixed at 116th and Broadway. In general, forecasts are made over some larger land mass, and that fact affects the precipitation forecast. Specifically, if there’s an 80% chance that precipitation will occur over half the land mass and a 0% chance it will occur over the other half for a specific time window, the forecast will read 40%. This is something like the chance that an average person in that land mass will experience precipitation, assuming they don’t move and that people are equidistributed over the land mass.


Then again with the proliferation of apps that intend to give forecasts for pinpointed locations, this old-fashioned forecasting method will probably be gone soon.
