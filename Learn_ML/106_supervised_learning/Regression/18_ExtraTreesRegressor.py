# ExtraTreesRegressor
'''
This class implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
'''

params = {
    'bootstrap': False, 'ccp_alpha': 0.0, 'criterion': 'squared_error', 'max_depth': None, 
    'max_features': 'auto', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0,
    'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 100,
    'n_jobs': None, 'oob_score': False, 'random_state': None, 'verbose': 0, 'warm_start': False
}
regressor = ExtraTreesRegressor()
regressor.set_params(**params)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

