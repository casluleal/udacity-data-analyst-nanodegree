# Loan Data Exploration
## by Lucas Leal da Silva


## Dataset

The dataset used was about 113,937 loans lent by the company Prosper, taken between 09/11/2005 and 10/03/2014. The original dataset included a total of 81 columns characterizing each loan, but I reduced it to 21 columns as a way to simplify the exploration of it, and focusing on the variables like date, borrower characterization, and other loan related variables like amount and status.


## Summary of Findings

Firstly, we identified that between the past due loans, there was a high concentration of until 15 days overdue loans, and this amount was reducing gradually when the amount of overdue days raised. But surprisingly, the period between 15 and 29 overdue days had the least amount of loans, that can be interpreted people tend to pay the overdue loans in this period.

Also, if we look at the amount of overdue loans in the years, we can see that it has a concentration of unpaid loans in the first years, that reduces, and begin to raise again in the last years, as we reduce the overdue period.

After, we discovered that the biggest category by far was the "debt consolidation", being more than three times higher than the second one, "not available". We also saw that the distribution of the amount borrowed had a right-skewed distribution, with a big tendency of people borrowing money next to multiples of $5,000. The only exception was the amount of $4,000, that was the highest count of loans.

Going to bivariate exploration, we saw that the average loan amount per category does not change so much like the number of loans, being a small decrease between the categories. We found out also that although the category "not available" is the second one in number of loans, it has almost the smallest amount of overdue loans, which is a surprising finding.

We found out also that the biggest concentration of loans are made by people with income range between $25,000 and $74,999. Yet about the income range, we saw that the Prosper score (historical analysis of borrower) has a tendency of being higher for the high income ranges.

At the end, we confirmed that people with higher salaries tend to borrow higher amounts of money, but most importantly, that the biggest influence of the amount of money here is the year that the loan was created, as almost all of the ranges and categories had similar increases and decreases between the consecutive years.


## Key Insights for Presentation

My main focus for the presentation will be related to the last finding, as it was for me the most significative one: how the average amount borrowed is significative influenced by the year.

I will start by showing the general visualization, focusing on the 2007/08 drop on the average, and then split the chart by the different categories (most significative ones) and borrower income range.