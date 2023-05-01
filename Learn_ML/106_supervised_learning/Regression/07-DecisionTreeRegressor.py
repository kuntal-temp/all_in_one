'''
ccp_alpha: Greater values of ccp_alpha increase the number of nodes pruned.
'''

regressor = DecisionTreeRegressor()
params = {'ccp_alpha': 0.0, 'criterion': 'squared_error', 'max_depth': None, 'max_features': None, 
          'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 
          'min_weight_fraction_leaf': 0.0, 'random_state': 0, 'splitter': 'best'}
regressor.set_params(**params)
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)


# view tree
from sklearn import tree
tree.plot_tree(regressor)
