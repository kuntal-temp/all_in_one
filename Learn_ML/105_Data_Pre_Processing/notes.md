# What can standard deviation tell you?

It tells you, on average, how far each score lies from the mean. In normal distributions, a high standard deviation means that values are generally far from the mean, while a low standard deviation indicates that values are clustered close to the mean.


# What can Mean tell you?

```
    Mean = (Sum of all the observations/Total number of observations)
```


# What is Standardization?

Standardization is a scaling technique where the values are centered around the mean with a unit standard deviation. This means that the mean of the attribute becomes zero and the resultant distribution has a unit standard deviation.


# why & when we need standardization on dataset?

Support Vector Machine tries to maximize the distance between the separating plane. If one feature has very large values, it will dominate over other features when calculating the distance. So Standardization gives all features the same influence on the distance metric.

Standardization comes into picture when features of the input data set have large differences between their ranges, or simply when they are measured in different measurement units (e.g., Pounds, Meters, Miles … etc).

To illustrate this with an example : say we have a 2-dimensional data set with two features, Height in Meters and Weight in Pounds, that range respectively from [1 to 2] Meters and [10 to 200] Pounds. No matter what distance based model you perform on this data set, the Weight feature will dominate over the Height feature and will have more contribution to the distance computation, just because it has bigger values compared to the Height. So, to prevent this problem, transforming features to comparable scales using standardization is the solution.
```
    z_score = (value - mean)/std
```


# which ML models and methods you have to standardize your data ?

1. pca: In Principal Component Analysis, features with high variances/wide ranges, get more weight than those with low variance, and consequently, they end up illegitimately dominating the First Principal Components.
2. clustering: Clustering models are distance based algorithms, in order to measure similarities between observations and form clusters they use a distance metric. So, features with high ranges will have a bigger influence on the clustering. 
3. knn: k-nearest neighbors is a distance based classifier that classifies new observations based on similarity measures (e.g., distance metrics) with labeled observations of the training set
4. svm: Support Vector Machine tries to maximize the distance between the separating plane and the support vectors. If one feature has very large values, it will dominate over other features when calculating the distance.
5. lasso & ridge: LASSO and Ridge regressions place a penalty on the magnitude of the coefficients associated with each variable. And the scale of variables will affect how much penalty will be applied on their coefficients. Because coefficients of variables with large variance are small and thus less penalized.


# when standardization is Not needed?

1. Logistic Regressio
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost

this are not sensitive to the magnitude of variables. So standardization is not needed before fitting these kinds of models.


# what is Normalization?

Normalization is a scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1. It is also known as Min-Max scaling.


# why is Normalization?

The goal of normalization is to change the values of numeric columns in the dataset to use a common scale, without distorting differences in the ranges of values or losing information.

For machine learning, every dataset does not require normalization. It is required only when features have different ranges.
For example, consider a data set containing two features, age(x1), and income(x2). Where age ranges from 0–100, while income ranges from 0–20,000 and higher. Income is about 1,000 times larger than age and ranges from 20,000–500,000. So, these two features are in very different ranges. When we do further analysis, like multivariate linear regression, for example, the attributed income will intrinsically influence the result more due to its larger value. But this doesn’t necessarily mean it is more important as a predictor.


# what is categorical features?

Often features are not given as continuous values but categorical. For example a person could have features ["male", "female"]


# what is OrdinalEncoder ?

This estimator transforms each categorical feature to one new feature of integers (0 to n_categories - 1)


# Types of Distributions

1. Bernoulli Distribution
2. Uniform Distribution
3. Binomial Distribution
4. Normal Distribution
5. Poisson Distribution
6. Exponential Distribution
https://www.analyticsvidhya.com/blog/2017/09/6-probability-distributions-data-science/



