# Learn Machine Learning

### Mean
```
    Mean = (12 + 34 + 45 + 50 + 24)/5
```

### Mode
```
    Observation with maximum frequency
    2 samples, 3 features
    X = [[ 1, 2, 3], [11, 12, 13]]
```

### Median
```
    For example, consider the data: 4, 4, 6, 3, 2. Let's arrange this data in ascending order: 2, 3, 4, 4, 6. There are 5 observations. Thus, median = middle value i.e. 4. We can see here: 2, 3, 4, 4 , 6 (Thus, 4 is the median)
```

- Mean Squared Error?
> There are various ways in which we can evaluate how good is our model. The most common way is Mean Squared Error

- What is a Variance error
> It refers to the amount that the predicted value would change if different training data were used.

- What is a Bias error?
> It is the error due to the model assumptions that are made to simplify the model.

- What is overfitting?
> When your model learns all complex and noise from training data and performs well in training data but while coming to validation data it does not work well then our data is overfitting.

- What is underfitting?
> When our data is underfitting then our model does learn the underlying trend data. It occurs when we have fewer data to build the model or when we try to build the linear model with non-linear data.

- What is Cross-Validation?
> Cross-Validation is essentially a technique used to assess how well a model performs on a new independent dataset. The simplest example of cross-validation is when you split your data into three groups: training data, validation data, and testing data, where you see the training data to build the model, the validation data to tune the hyperparameters, and the testing data to evaluate your final model.

- Regularization
> It reduces the overfitting nature of the model. Even if the model works well, this is done in order to prevent the problem from occurring in the future. This is done by introducing more errors and making the model learn more. This will help the model to learn more. And as a result, even if more data is added in the later stage, the model will be able to process those without any issues. Now the model performance will increase and will be better than the unregularized model.

### Types of regularization
- Ridge regularization
- Lasso regularization
- ElascticNet Regression


> **Ridge regularization:**
It adds the “Squared magnitude” of coefficient as a penalty term to the loss function. It is called an L2 penalty
sse = np.sum ((y-b1x1-b2x2-…-bo) **2) + (alpha * (b1**2+b2**2+b3**2+…+bo**2))

> **Lasso regularization**
The (least absolute shrinkage and selection operator) adds the “Absolute value of magnitude” of coefficient as a penalty term to the loss function. It is called an L1 penalty.
sse = np.sum ((y-b1x1-b2x2-…-bo) **2) + (alpha * (|b1|+|b2|+|b3|+…+|bo|))

> **ElascticNet Regression**
It is the combination of both Ridge and Lasso regularization.
sse = np.sum ((y-b1x1-b2x2-…-bo) **2) + (alpha_ridge * (b1**2+b2**2+b3**2+…+bo**2)) +(alpha_lasso * (|b1|+|b2|+|b3|+…+|bo|))


- Gradient Descent ?
> We can find the best alpha value and best regularization using this method. Gradient descent is an iterative optimization algorithm used in machine learning to minimize a loss function. The loss function describes how well the model will perform given the current set of parameters (weights and biases), and gradient descent is used to find the best set of parameters.
It is an optimization algorithm used to train machine learning models by minimizing errors between predicted and actual results.

## Types of Gradient Descent
1. Batch Gradient Descent: Parameters are updated after computing the gradient of error with respect to the entire training set
2. Stochastic Gradient Descent: Parameters are updated after computing the gradient of error with respect to a single training example
3. Mini-Batch Gradient Descent: Parameters are updated after computing the gradient of error with respect to a subset of the training set

The only difference comes while iterating. In Gradient Descent, we consider all the points in calculating loss and derivative, while in Stochastic gradient descent, we use single point in loss function and its derivative randomly

**Understanding**

> Say we have 10,000 data points and 10 features. The sum of squared residuals consists of as many terms as there are data points, so 10000 terms in our case. We need to compute the derivative of this function with respect to each of the features, so in effect we will be doing 10000 * 10 = 100,000 computations per iteration. It is common to take 1000 iterations, in effect we have 100,000 * 1000 = 100000000 computations to complete the algorithm. That is pretty much an overhead and hence gradient descent is slow on huge data.

