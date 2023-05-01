# XGBoost (eXtreme Gradient Boosting)
'''
The two main reasons to use XGBoost are:
    1) Execution speed
    2) Model performance.
'''


# way 1
regressor = XGBRegressor(objective ='reg:linear', n_estimators = 10, seed = 123)
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)


# way 2
regressor = XGBRFRegressor()
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)