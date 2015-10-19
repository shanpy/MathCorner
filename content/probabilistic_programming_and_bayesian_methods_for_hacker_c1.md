Title: Probabilistic Programming and Bayesian Methods for Hackers Reading Note - Chapter 1
Date: 2015-01-13
Modified: 2015-05-30
Category: Data Science
Tags: Statistics, Python, Data Science
Slug: probabilistic-programming-and-bayesian-methods-for-hacker-reading-note-chapter-1
Authors: Pengyin Shan
Summary: This is a reading notes for <a href=" https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers">Probabilistic Programming and Bayesian Methods for Hackers, Chapter 1, The Philosophy of Bayesian Inference</a>. 

This post is being transferred from <a href="shanpy.github.io/techblog">my old blog site</a>, about Python development for statistics.

##The Philosophy of Bayesian Inference

**Bayesian inference** is simply updating your **beliefs** after considering new evidence. We update our beliefs about an outcome; ralely can we be absolutely sure unless we rule out all other alternatives.

In Bayesian, the **probability** is consideres as **believablity** of an event. i.e. how **confident** we are.

**Frequentist**: assume probablity is the **long-run** frequency of events. 

**Bayesian**: asssume probablity is a measure of **belief**. Note that belief is assigneed **individually**, which means there can be **conflicting** of blieves.

**P(A)**: prior probability

**P(A|X)**: the probablity of A given the evidence `X`

For example: `P(A)`: The code likely has a bug with it. `P(A|X)`: The code passed all `X` tests, there still might be a bug, but its presence is less likely now

Every time after a new evidence `X` comes, we **re-weighted** the **prior probablity** to incorporated the new evidence. After this process, our guesses become **less wrong**. i.e. we try to be more **right** after each guess.

**Frequentist** will return a number, while Bayesians will return probablity. 

Forthe example above, if asking "My code passes all tests. Is my code bug-free?", Frequentist will return yes. 

If asking "*Often my code has bugs. (prior parameter)* My code passed all X tests. Is my code bug-free?", Bayesians will return "Yes, with probablity 0.8; No, with probablity 0.2".

Denote `N` as the number of **instances of evidence** we possess. As we gather an **infinite** amount of evidence, say as `N -> Infinity`, our Bayesian results (often) align with frequentist results.

So for large `N`, statistical inference is more or less **objective**

For small `N`, inference is much more **unstable**: Frequentist estimates have more variance and larger confidence intervals.

Hence Bayesians introduce a **prior** and returning **probablities**, it can **preserve** the **uncentainty** that reflects the instability (not stable) of statistical inference of a small `N` dataset.

###Bayes' Theorem

if our code passes `X` tests, we want to **update** our belief to incorporate this. We call this new belief the **posterior probability**. 

Bayes' Theorem is used for updating process.

Bayesian inference merely uses it to connect **prior probabilities** `P(A)` with an updated **posterior probabilities** `P(A|X)` .

###The Understanding of Variables for Coding Example

Assume `A` means the event that code has **no** bug and `X` means code passes `X` tests. Assume `P(A) = p`.

**P(A|X)**: the probability for no bugs, giving passing debug test `X`.

**P(X|A)**: the probability that code passes `X` test given there is no bugs. This always be 1.

	:::python
	#Since We can get P(X) by following way:

	P(X) = P(X and A) + P(X and ~A(not A))
	    = P(X|A)P(A) + P(X|~A)P(~A)
	    = P(X|A)p + P(X|~A)(1-p)
	    
	#Assume P(X|~A) = 0.5 here, and we know P(X|A) = 1  
	P(A|X) = 1*p/(1*p + 0.5*(1-p))
	#This is the posterior probability

##Probability Distributions	

Let `Z` be some random variable. Then associated with `Z` is a **probability distribution function** that assigns probablities to the different **outcomes** `Z` can take. A **probability distribution** is a curve where the probability of an outcome is *proportional* to the *height* of the curve.

`Z` can be discreate: only assume values on a speical list. Such as populations, movie ratings, etc.

`Z` can be continous: takes aribitrarily exact values. Such as temporature, speed, etc

`Z` can be mixed by two types above.

###If Z is discreate

If `Z` is discreate, its distribution is called **probability mass function**, which measures the probablity `Z` takes on the value `k`, denoted `P(Z=k)`.

We saw `Z` is **posisson-distributed** if: 

- `λ` is called a parameter of the distribution, or **intensity** of the **possison distribution** and it controls the distribution's **shape**. Here, `λ` can be any *positive* number.

- if `λ` increate, add probability to larger values. if `λ` decrease, add probability to smaller values.

- `k` must be a **non-negative** integer.

If a random variable `Z` has a **poisson mass distribution**, we can express as: `Z ~ Poi(λ)`

For a poisson distribution, its expected value is equal to its parameter, i.e. `E[Z | λ] = λ`

###If Z is continuous

If `Z` is continous, its distribution is called **probability density function**. 

>`z` can only take **non-negative** value, including non-integer

If `Z` has an exponential distribution, we say `Z` is **exponential** and we have: `Z ~ Exp(λ)` and `E[Z | λ] = 1/λ`

	:::python
	#PyMC

	import pymc as pm

	alpha = 1.0 / count_data.mean()

	lambda_1 = pm.Exponential("lambda_1", alpha)  #get lambda value
	lambda_2 = pm.Exponential("lambda_2", alpha)

	tau = pm.DistcreateUniform("tau", lower=0, upper=n_count_data)
