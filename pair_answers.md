You are a data scientist at Etsy, a peer-to-peer e-commerce platform. The marketing department has been organizing meetups among its sellers in various markets, and your task is to determine if attending these meetups causes sellers to generate more revenue.

a)  Your boss suggests comparing the past sales from meetup attendees to the sales from sellers who did not attend a meetup. Will this allow us to conclude attending meetups cause sellers to generate more revenue? If so, why, otherwise, why not?

This will not conclude that attending meetups will cause sellers to generate more revenue because it is not comparing results before and after attending the meetup.  Instead it is only comparing the results of two different groups (ones who went to meetups and ones who didnt).

b)  Outline the steps to design an experiment that would allow us to determine if local meetups cause a seller to sell more?

To determine this we would need to compare a sellers revenue before and after a meetup for both groups who attended and groups who didnt attend meetups.  Then we would compare the results from these two groups to determine if there was a difference.

c)  What is the purpose of running an experiment (A/B testing) as opposed to applying various statistical techniques to your existing data?

Running an experiment gives us a chance to identify the causation of the outcome.

2)  Suppose you have built a book recommendation system at Company X using the latest discoveries in research (recommendation techniques are covered later). You are interested in finding out if the book recommender makes good recommendations. The quality of the book recommendations is determined by the click through rate (CTR) of the recommendations.

Design an experiment that allows us to conclude if latest discoveries in recommenders are worthy of being implemented and put into production. State what the control group should be and justify your choice.

Randomly assign the old or the new generator when users perform a search.  Group A will be exposed to the new reccomender system.  Group B will be exposed to the older system.  Record the click through rate of both systems and do analysis on the results of the two groups.  If the group with the new recommender system has a higher click through rate then it would appear that this new recommender system is better.


Part 2: A / B Testing
Include your answers in pair_answers.py.

Download the starter code and data here.

Designers at Etsy have created a new landing page in an attempt to improve sign-up rate for local meetups.

The historic sign-up rate for the old landing page is 10%. An improvement to only 10.1% would provide a lift of 1%. A 1% lift would translate to an absolute difference of 0.1% difference in conversion. If statistically significant, the new landing page would be considered a success. The product manager will not consider implementing the new page if the lift is not greater than or equal to 1%.

Your task is to determine if the new landing page can provide a 1% or more lift to the sign-up rate. You are also given the understanding that there is a very different user base on weekends and a significant amount of the revenue comes from those weekend users.



1)   Design an experiment in order to decide if the new page has a 1% lift in sign-up rate as compared to the old page? Describe in detail the data collection scheme you would use for the experiment. Justify why the data will be collected that way.

Randomly show both old and new landing page and track who shown new and old site and sign-ups.  This data collection should take place equally over different days of the week.  For example run this data collection over a 2 week period so that weekends and weekdays both have their data represented.  We can then run a statistical Z score test on it to s




Why is it useful to report the change in conversion in terms of lift instead of absolute difference in conversion?

Reporting the change in conversion allows us to see the difference in the new landing page vs the old landing page as a comparison in terms of percentage.  Just checking the absolute difference only shows an improvement or not.


State your null hypothesis and alternative hypothesis? Is your alternative hypothesis set up for a one-tailed or two-tailed test? Explain your choice.

Null:  There is less than 1 percent increase in CTR of the new landing page compared to the old landing page.

Alternative hypothesis:  There is greater than or equal to a 1% increase in the new landing page CTR compared to the old landing page

It will be set up as a one tailed test because we are only interest in an increase in CTR.

You ran a pilot experiment according to Question 1 for ~1 day (Tuesday). The collected data is in data/experiment.csv. Import the data into a pandas dataframe. Check the data for duplicates and clean the data as appropriate.

Calculate a p-value for a 1% lift from using the new page compare to the old page.

Use from z_test import z_test
What assumptions are you making when you use a z-test.

Interpret the p-value and explain your decision whether to adopt the new page or not.

The results mean that we can not reject our null hypothesis.
z-score: -0.689944276707, p-value: 0.754885384821, reject null: False

6)   Assume your test was insignificant. Given the setting of the experiment and the context of the problem, why might you be hesitant to make the conclusion to not use the new landing page. What would you do instead?

The data we have is from a weekday, when most Etsy traffic is from a weekend, so maybe the results would be different if we have data from a weekend day instead.  Continue to take data for a week and then rerun the analysis and make a conclusion from there.

Why might it be a problem if you keep evaluating the p-value as more data comes in and stop when the p-value is significant? See this article.

If you stop when the p-value is significant then you may be cutting the experiment off short.  Maybe the p-value becomes insignificant when more data comes in, but if you cut off early, then you wont reach this point, and you will draw an incorrect conclusion on the experiment.

One perennial problem for A/B testing is when to stop your test. We will cover a more in-depth treatment of calculating statistical power of your experiment. One semi-quantitative way to access if your conclusion is going to change if you have had run the experiment longer is to plot the progression of the p-value as a time series. If the p-value is consistent upon the collection of more data over an extended period of time, then you are more confident that your conclusion would stay the same even if the experiment had run on longer.

See Airbnb's talk on this technique here and here.
Plot the time series of the p-values using hourly intervals, such that the p-value at the second hour would be evaluating data up to second hour and at the third hour would be evaluating the data up to the third hour. Describe the insights you gain from the plot.

There is an additional file data/country.csv providing country information about the clicks. Does the country data offer any additional insights?
