'''
Hist Gradient Boosting Regressor is a much faster variant of this algorithm for intermediate datasets (n_samples >= 10_000)
'''

reg = HistGradientBoostingRegressor()
reg.fit(X_train, y_train)
