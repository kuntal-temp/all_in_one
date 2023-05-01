# Locally Linear Embedding [LLE]
# [Used for Unsupervised Learning]

"""
if you are specifically looking for a non-linear approach, then Locally Linear Embedding (LLE) and Isometric Mapping (Isomap) 
would be good ones to explore.


"""

lle = LocallyLinearEmbedding()
params = {'eigen_solver': 'auto', 'hessian_tol': 0.0001, 'max_iter': 100, 'method': 'standard', 
          'modified_tol': 1e-12, 'n_components': 2, 'n_jobs': None, 'n_neighbors': 5, 'neighbors_algorithm': 'auto', 
          'random_state': None, 'reg': 0.001, 'tol': 1e-06}
lle.set_params(**params)

X_train = lle.fit_transform(X_train)
X_test = lle.fit_transform(X_test)