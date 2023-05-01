clustering = SpectralClustering()
params = {'affinity': 'rbf', 'assign_labels': 'discretize', 'coef0': 1, 'degree': 3, 'eigen_solver': None, 
          'eigen_tol': 0.0, 'gamma': 1.0, 'kernel_params': None, 'n_clusters': 5, 'n_components': None, 
          'n_init': 10, 'n_jobs': None, 'n_neighbors': 10, 'random_state': 0, 'verbose': False}
clustering.set_params(**params)
clustering.fit(X)

# Make predict
y_pred = clustering.fit_predict(X)
print(y_pred)

# Visualising the OPTICS clusters
plt.scatter(X[y_pred == 0, 0], X[y_pred == 0, 1], s = 100, c = 'red', label = 'Cluster 1', marker='1')
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], s = 100, c = 'blue', label = 'Cluster 2', marker='2')
plt.scatter(X[y_pred == 2, 0], X[y_pred == 2, 1], s = 100, c = 'green', label = 'Cluster 3', marker='3')
plt.scatter(X[y_pred == 3, 0], X[y_pred == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4', marker='+')
plt.scatter(X[y_pred == 4, 0], X[y_pred == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5', marker='.')
plt.scatter(X[y_pred == 5, 0], X[y_pred == 5, 1], s = 50, c = 'hotpink', label = 'Cluster 6', marker='h')
plt.scatter(X[y_pred == 6, 0], X[y_pred == 6, 1], s = 100, c = 'orange', label = 'Cluster 7', marker='*')
plt.scatter(X[y_pred == 7, 0], X[y_pred == 7, 1], s = 100, c = 'coral', label = 'Cluster 8', marker='.')
plt.title('Hierarchical Clusters')
plt.xlabel('your x level')
plt.ylabel('your y level')
plt.legend()
plt.show()