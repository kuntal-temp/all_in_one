'''
y = c + b*x; where y is the dependent variable (outcome), x is the independent variable (predictor)
b is the slope of the line; also known as regression coefficient and c is the intercept

Ordinary least squares Linear Regression

fit_intercept: Whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (i.e. data is expected to be centered)
positive: When set to True, forces the coefficients to be positive. This option is only supported for dense arrays.
'''

regressor = LinearRegression()
params = {
    'copy_X': True, 'fit_intercept': True, 'n_jobs': None, 'normalize': 'deprecated', 
    'positive': False
    }
regressor.set_params(**params)

regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)

print(regressor.coef_)
print(regressor.intercept_)