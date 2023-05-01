# Known as L1
'''
If the variables are highly correlated groups, lasso tends to choose one variable from such groups and ignore the rest entirely.
This means that the model does some automatic feature selection to decide which features should and should not be included on its own.

L1 is therefore useful for feature selection, as we can drop any variables associated with coefficients that go to zero. By applying Lasso Regression you can shrink the coefficients of some of the unwanted features to 0 thus eliminating multicollinearity

Lasso Regression tends to pick non-zero as predictors and sometimes it affects accuracy when relevant predictors are considered as non zero.

"Absolute value of magnitude" of the coefficient as a penalty term to the loss function.

alpha: Constant that multiplies the L1 term, controlling regularization strength. alpha must be a non-negative float i.e. in [0, inf) When alpha = 0, the objective is equivalent to ordinary least squares.

positive: When set to True, forces the coefficients to be positive.
'''

regressor = Lasso(alpha=0.3)
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
