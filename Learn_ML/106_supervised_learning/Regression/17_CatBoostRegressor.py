# catboost
'''
It allows to use GPU-training.

CatBoost is based on gradient boosted decision trees. During training, a set of decision trees is built consecutively. Each successive tree is built with reduced loss compared to the previous trees.

In CatBoost, symmetric trees, or balanced trees, refer to the splitting condition being consistent across all nodes at the same depth of the tree.
'''

params = {
    'nan_mode': 'Min', 'eval_metric': 'RMSE', 'iterations': 1000, 'sampling_frequency': 'PerTree',
    'leaf_estimation_method': 'Newton', 'grow_policy': 'SymmetricTree', 'penalties_coefficient': 1,
    'boosting_type': 'Plain', 'model_shrink_mode': 'Constant', 'feature_border_type': 'GreedyLogSum', 
    'bayesian_matrix_reg': 0.10000000149011612, 'eval_fraction': 0, 'force_unit_auto_pair_weights': False,
    'l2_leaf_reg': 3, 'random_strength': 1, 'rsm': 1, 'boost_from_average': True, 'model_size_reg': 0.5,
    'pool_metainfo_options': {'tags': {}}, 'subsample': 0.800000011920929, 'use_best_model': False,
    'random_seed': 0, 'depth': 6, 'posterior_sampling': False, 'border_count': 254, 'classes_count': 0,
    'auto_class_weights': 'None', 'sparse_features_conflict_fraction': 0, 
    'leaf_estimation_backtracking': 'AnyImprovement', 'best_model_min_trees': 1, 'model_shrink_rate': 0,
    'min_data_in_leaf': 1, 'loss_function': 'RMSE', 'learning_rate': 0.028970999643206596,
    'score_function': 'Cosine', 'task_type': 'CPU', 'leaf_estimation_iterations': 1, 'bootstrap_type': 'MVS',
    'max_leaves': 64
}
regressor = CatBoostRegressor()
# regressor.set_params(**params)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

