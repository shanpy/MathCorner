Title: An Introduction to Think Stats - Chapter 1
Date: 2015-01-13
Modified: 2015-05-30
Category: Data Science
Tags: Statistics, Data Science
Slug: an-introduction-to-think-stats-chapter-1
Authors: Pengyin Shan
Summary: This post is one of the reading notes for **Think Stats, 2nd Edition**, written by **Allen B.Downey**, published by **O'Reilly**, on October 2014.

#Chapter 1: Exploratory Data Analysis

**Anecdotal Evidence** is the evidence based on the data that is unpublished and usually personal, rather than by a well-designed study.

Anecdotal Evidence usually fails because of four reasons:

- Small Number of Observations

- Selection Bias: people who discuss the question may be interested in one aspects of the answer

- Confirmation Bias: people who belive the claim might be more likely to contribute examples that confirm it

- Inaccuracy: Anecdotes are ofter personal, so there exists misremembered, misrepeated, etc.

To avoid Anecdotal Evidence, a few **tools of statistics** can be used:

- Data Collection: large and trustable data source

- Descriptive Statistics: statistics that summarize data concisely, maybe with data virtualization

- Exploratory Data Analysis: patterns, differnces and other features that address the question. Inconsistency and Identify limitations.

- Estimation: use data from sample to estimate characteristics

- Hypothesis Testing: if there is any apparent effects, such as a difference between two groups, evaluate if this effect happening by chance.

**Population**: a group we are interested in studying.

**Cross-Sectional Study**: captures a snapshot of a group at a point in time. It is **representative**, which means every number of the target population has an equal change of participating. **Oversampled** is opposite to representative. It means some groups of population has much higher rate in all sample groups. Oversampling is used to avoid errors due to small sample sizes.

**Longitudinal Study**: observes a group repeatedly over a period of time.

**Cycle**: a survey can be conducted several times. Each deployment is called a cycle.

**Sample**: data from a subset of population

**Record**: In a dataset, a collection of information about a single person or other subject.

**Respondents**: people who participate in the survey

**DataFrame**: the fundamental data structure provided by **pandas**. It contains a row of each record, and the variable names and their types. It also provides methods of accessing and modifying data.

**Raw Data**: values collected with little or no checking, calculation or interpretation.

**Recodes**: instead of being part of raw data, recodes are calculated by raw data. Recodes are often based on logic that checks the consistency and accuracy of the data.

**Data Cleaning**: operations such as check for errors, deal with sepecial values, convert data into different formats and perform calculations after you import data.

**Data Validation**: one way to validate data is to compute basic statistics and compare them with published results

**Data Interpretation**: To work with data effectively, you have to think on two levels at the same time: the level of **statistics** and the level of **context**. Some result is statistically acceptable but not natual in context.
