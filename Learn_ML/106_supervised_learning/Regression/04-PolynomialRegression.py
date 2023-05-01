'''
Y= b0+a1x+a2x^2+a3x^3+…. anx^n

if the dependent variable is binary( 0 or 1), true or false, yes or no, logistics regression is used.

degree: int or tuple (min_degree, max_degree)
'''

""" Find best degree """
rmses = []
degrees = np.arange(1, 10)
min_rmse, min_deg = 1e10, 0   # 1e10 = 1*10^10
for deg in degrees:
    poly_features = PolynomialFeatures(degree=deg, include_bias=False)
    x_poly_train = poly_features.fit_transform(X_train)
    poly_reg = LinearRegression()
    poly_reg.fit(x_poly_train, Y_train)
    x_poly_test = poly_features.fit_transform(X_test)
    poly_predict = poly_reg.predict(x_poly_test)
    poly_rmse = mean_squared_error(Y_test, poly_predict, squared=False)
    rmses.append(poly_rmse)
    if min_rmse > poly_rmse:
        min_rmse = poly_rmse
        min_deg = deg

print('Best degree {} with RMSE {}'.format(min_deg, min_rmse))

""" Ploting MSE with degree """
plt.plot(degrees, rmses)
plt.xlabel('Degree')
plt.ylabel('RMSE')
rmses.sort()

# traing started
poly_features = PolynomialFeatures(degree=min_deg, include_bias=False)
X_train = poly_features.fit_transform(X_train)
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

X_test = poly_features.fit_transform(X_test)
Y_pred = regressor.predict(X_test)