# Model Improvement

# Logistic Regression
""" [default params]
params = {'C': 1.0, 'class_weight': None, 'dual': False, 'fit_intercept': True, 'intercept_scaling': 1, 
          'l1_ratio': None, 'max_iter': 100, 'multi_class': 'auto', 'n_jobs': None, 'penalty': 'l2', 
          'random_state': 0, 'solver': 'lbfgs', 'tol': 0.0001, 'verbose': 0, 'warm_start': False}
"""

""" [All scoring value for Regression]

scoring = [
  accuracy, balanced_accuracy, top_k_accuracy, average_precision, neg_brier_score, f1. f1_micro, f1_macro,
  f1_weighted, f1_samples, neg_log_loss, roc_auc_ovo_weighted, roc_auc_ovo, roc_auc_ovr,  roc_auc, jaccard, recall, precision
  ]

penalty : ['l2', 'l1', 'elasticnet']
solver : ['lbfgs', 'newton-cg', 'liblinear', 'sag', 'saga']
"""

parameters = [
  {
    'C': [0.25, 0.5, 0.75, 1],
    'fit_intercept': [True, False],
    'intercept_scaling': [1, 2, 3, 4, 5],
    'max_iter': [100],
    'penalty': ['l2'],
    'warm_start': [True, False],
    'solver': ['lbfgs']
  },
  {
    'C': [0.25, 0.5, 0.75, 1],
    'fit_intercept': [True, False],
    'intercept_scaling': [1, 2, 3, 4, 5],
    'max_iter': [100],
    'penalty': ['l2', 'l1'],
    'warm_start': [True, False],
    'solver': ['liblinear']
  },
  {
    'C': [0.25, 0.5, 0.75, 1],
    'fit_intercept': [True, False],
    'intercept_scaling': [1, 2, 3, 4, 5],
    'max_iter': [100],
    'penalty': ['l2', 'l1', 'elasticnet'],
    'warm_start': [True, False],
    'solver': ['saga']
  }  
]

grid_search = GridSearchCV(estimator = classifier, param_grid = parameters, scoring = 'accuracy', cv = 5)
grid_search.fit(X_train, Y_train)

best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)





# ---------------------------------------------------------------------------------

# XGBoost
parameters = {
        'n_estimators': [50,100,150,200,300,500],
        'max_depth': [None, 3, 5, 7, 9],
        'eta': [0.5, 1, 2, 3]
        }
grid_search = GridSearchCV(estimator = classifier, param_grid = parameters, scoring = 'accuracy', cv = 5)
grid_search.fit(X_train, Y_train)

best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)
