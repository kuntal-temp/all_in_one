# Multivariate Adaptive Regression Splines in Python [MARS]

from pyearth import Earth

regressor = Earth()
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)