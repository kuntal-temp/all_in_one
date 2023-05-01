# PLSRegression
'''
It is particularly useful when we need to predict a set of dependent variables from a (very) large set of independent variables.
'''

params = {
    'copy': True, 'max_iter': 500, 'n_components': 2, 'scale': True, 'tol': 1e-06
}
regressor = PLSRegression()
regressor.set_params(**params)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)


