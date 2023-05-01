# Known as L2
'''
If the size of data is less. i.e. less features, we can go with Ridge Regression.

It is most suitable when a data set contains a higher number of predictor variables than the number of observations. The second-best scenario is when multicollinearity is experienced in a set.

It is used highly for the treatment of multicollinearity in regression. So in Ridge regression, we make bias and variance proportional to each other, or it basically decreases the difference between actual and predictive values.

Ridge regression does not promise to remove all irrelevant coefficient.

"squared magnitude" of the coefficient as the penalty term to the loss function.
'''

regressor = Ridge(alpha=0.01)
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)