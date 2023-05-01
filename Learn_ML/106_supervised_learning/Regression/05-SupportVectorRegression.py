'''
This algorithm acknowledges the presence of non-linearity in the data and provides a proficient prediction model.

In Support Vector Regression, the straight line that is required to fit the data is referred to as hyperplane. The objective of a support vector machine algorithm is to find a hyperplane in an n-dimensional space that distinctly classifies the data points. The data points on either side of the hyperplane that are closest to the hyperplane are called Support Vectors.

The most widely used kernels include Linear, Non-Linear, Polynomial, Radial Basis Function (RBF) and Sigmoid.

Support Vector Regression is a supervised learning algorithm that is used to predict discrete values.

The fit time complexity of SVR is more than quadratic with the number of samples which makes it hard to scale to datasets with more than a couple of 10000 samples. For large datasets, LinearSVR or SGDRegressor is used. Linear SVR provides a faster implementation than SVR but only considers the linear kernel.

The model produced by Support Vector Regression depends only on a subset of the training data, because the cost function ignores samples whose prediction is close to their target.

In cases where the number of features for each data point exceeds the number of training data samples, the SVM will underperform.

The Decision model does not perform very well when the data set has more noise i.e. target classes are overlapping.

C: This parameter tells the SVM optimization how much you want to avoid misclassifying each training example. For large values of C, the optimization will choose a smaller-margin hyperplane if that hyperplane does a better job of getting all the training points classified correctly.

Gamma: Low values of gamma indicates a large similarity radius which results in more points being grouped together.
'''

params = {'C': 1.0, 'cache_size': 200, 'coef0': 0.0, 'degree': 0, 'epsilon': 0.1, 'gamma': 'scale', 
          'kernel': 'rbf', 'max_iter': -1, 'shrinking': True, 'tol': 0.001, 'verbose': False}

# kernel = rbf
regressor = SVR()

# kernel = poly
regressor = SVR(kernel="poly", degree=2, C=100, epsilon=0.1)

regressor.set_params(**params)
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)
