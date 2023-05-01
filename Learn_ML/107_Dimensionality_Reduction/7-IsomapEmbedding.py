# Isomap Embedding
# [Used for Unsupervised Learning]
"""
Isomap should be used when there is a non-linear mapping between your higher-dimensional data and your lower-dimensional manifold.

An Awesome Approach to Non-linear Dimensionality Reduction.

The isomap algorithm uses euclidean metrics to prepare the neighborhood graph.

geodesic distance is preserved in ISOMAP.
"""

isomap = Isomap()
params = {'eigen_solver': 'auto', 'max_iter': None, 'metric': 'minkowski', 'metric_params': None, 'n_components': 2, 
          'n_jobs': -1, 'n_neighbors': 5, 'neighbors_algorithm': 'auto', 'p': 2, 'path_method': 'auto', 'tol': 0}
isomap.set_params(**params)

X_train = isomap.fit_transform(X_train)
X_test = isomap.fit_transform(X_test)