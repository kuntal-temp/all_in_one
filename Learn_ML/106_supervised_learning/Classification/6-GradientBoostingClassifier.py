"""
## Gradient Boosted Decision Trees

Gradient Boosting algorithms tackle one of the biggest problems in Machine Learning: bias.

In Gradient Boosted algorithms the technique used to control bias is called Boosting

The intuition behind Boosting is that you train the same weak learner, a model with simple rules, 
several times. Then combine its weak predictions into a single, more accurate result. 
The model is always of the same type same but, each time, it is trained with different 
weights for the observations it misclassified
"""

classifier = GradientBoostingClassifier()
params = {'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 1.0, 'loss': 'deviance', 'max_depth': 1, 
          'max_features': None, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 
          'min_weight_fraction_leaf': 0.0, 'n_estimators': 100, 'n_iter_no_change': None, 'random_state': 0, 'subsample': 1.0, 
          'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False}
classifier.set_params(**params)

classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)