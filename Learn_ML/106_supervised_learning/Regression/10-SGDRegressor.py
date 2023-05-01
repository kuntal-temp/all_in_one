'''
#Stochastic Gradient Descent

Gradient descent is an iterative optimization algorithm used in machine learning to minimize a loss function.

Types of Gradient Descent:
    1) Batch Gradient Descent: Parameters are updated after computing the gradient of error with respect to the entire training set
    2) Stochastic Gradient Descent: Parameters are updated after computing the gradient of error with respect to a single training example
    3) Mini-Batch Gradient Descent: Parameters are updated after computing the gradient of error with respect to a subset of the training set
'''

# SGDRegressor with Lasso
reg = SGDRegressor(penalty="l1")
reg.fit(X_train, Y_train)

# SGDRegressor with Ridge
reg = SGDRegressor(penalty="l2")
reg.fit(X_train, Y_train)

# SGDRegressor with ElasticNet
reg = SGDRegressor(penalty="elasticnet", l1_ratio=0.5)
reg.fit(X_train, Y_train)

