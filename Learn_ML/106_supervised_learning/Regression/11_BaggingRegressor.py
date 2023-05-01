'''
Bagging Regressor

It is used to deal with bias-variance(over fitting) trade-offs and reduces the variance of a prediction model. Bagging avoids overfitting of data and is used for both regression and classification models.
'''

regressor = BaggingRegressor(
    estimator=SVR(), n_estimators=10, random_state=0
)

regressor.fit(X, y)
regressor.predict(X)