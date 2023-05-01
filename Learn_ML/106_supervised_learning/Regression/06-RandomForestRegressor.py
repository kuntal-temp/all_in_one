'''
Random Forest Regression is a supervised learning algorithm that uses ensemble learning[Bagging] method for regression.
'''
regressor = RandomForestRegressor()
params = {'bootstrap': True, 'ccp_alpha': 0.0, 'criterion': 'squared_error', 'max_depth': None, 
          'max_features': 'auto', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 
          'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 10, 
          'n_jobs': None, 'oob_score': False, 'random_state': 0, 'verbose': 0, 'warm_start': False}
regressor.set_params(**params)
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)