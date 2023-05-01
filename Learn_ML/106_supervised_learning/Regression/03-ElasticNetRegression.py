# L1+L2
'''
A regression method that performs variable selection and regularization simultaneously. 

It first finds the ridge regression coefficients and then conducts the second step by using a lasso sort of shrinkage of the coefficients.

alpha: Choose an alpha value between 0 and 1 to optimize the elastic net. Effectively this will shrink some coefficients and set some to 0 for sparse selection.

Note: 
Why would you use ridge regression Lasso regression or elastic net?
> Lasso will eliminate many features, and reduce overfitting in your linear model. Ridge will reduce the impact of features that are not important in predicting your y values. Elastic Net combines feature elimination from Lasso and feature coefficient reduction from the Ridge model to improve your model's predictions.

selection: If set to ‘random’, a random coefficient is updated every iteration rather than looping over features sequentially by default. This (setting to ‘random’) often leads to significantly faster convergence especially when tol is higher than 1e-4.
'''

regressor = ElasticNet(alpha=1, l1_ratio=0.5, normalize=False)
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)