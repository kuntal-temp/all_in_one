# Model Improvement

# Linear Regression
""" [default params]
params = {'copy_X': True, 'fit_intercept': True, 'n_jobs': None, 'normalize': 'deprecated', 'positive': False}
"""

""" [All scoring value for Regression]
scoring = [
  explained_variance, max_error, neg_mean_absolute_error, neg_mean_squared_error,
  neg_root_mean_squared_error, neg_mean_squared_log_error, neg_median_absolute_error, r2,
  neg_mean_poisson_deviance, neg_mean_gamma_deviance, neg_mean_absolute_percentage_error
  ]
"""

"""
For example, in the case of using cv=5-fold cross-validation, GridSearchCV divides the data into 5 folds and trains the model 5 times
"""

parameters = {
    'fit_intercept':[True,False], 
    'copy_X':[True, False],
    'positive': [True, False],
    'normalize': [False]
    }

grid_search = GridSearchCV(estimator=regressor, param_grid=parameters, scoring='explained_variance', cv=5)
grid_search.fit(X_train, Y_train)

best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)


# -------------------------------------------------------------------------------------

# Support Vector Regression
""" [default params]
  params = {'C': 1.0, 'cache_size': 200, 'coef0': 0.0, 'degree': 3, 'epsilon': 0.1, 'gamma': 'scale', 
          'kernel': 'rbf', 'max_iter': -1, 'shrinking': True, 'tol': 0.001, 'verbose': False}
"""

"""
All scoring value for Regression

scoring = [
  explained_variance, max_error, neg_mean_absolute_error, neg_mean_squared_error,
  neg_root_mean_squared_error, neg_mean_squared_log_error, neg_median_absolute_error, r2,
  neg_mean_poisson_deviance, neg_mean_gamma_deviance, neg_mean_absolute_percentage_error
  ]
"""

# parameters = {
#     'C':[1.0, 2.0, 3.0, 4.0, 5.0],
#     'cache_size':[i for i in range(100, 1000, 100)], 
#     'coef0' : [0.01,10,0.5],
#     'degree': [i for i in range(1, 10)],
#     'gamma' : ('auto','scale'),
#     'kernel' : ['linear', 'poly', 'rbf', 'sigmoid'],
#     'max_iter': [-1],
#     'shrinking': [True, False],
#     'verbose': [True, False]
#     }

parameters = [{'C': [0.25, 0.5, 0.75, 1], 'kernel': ['linear']},
              {'C': [0.25, 0.5, 0.75, 1], 'kernel': ['rbf'], 
               'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
              }]

grid_search = GridSearchCV(estimator = regressor, param_grid = parameters, cv = 5)
grid_search.fit(X_train, Y_train)

best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)



# ------------------------------------------------------------------------------

# XGBoost
parameters = {
        'n_estimators': [50,100,150,200,300,500],
        'max_depth': [None, 3, 5, 7, 9],
        'eta': [0.5, 1, 2, 3]
        }
grid_search = GridSearchCV(estimator = regressor, param_grid = parameters, cv = 5)
grid_search.fit(X_train, Y_train)

best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)
