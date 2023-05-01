# Hierarchical clustering

# Number of cluster choosing
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()


# Now trained your model
clustering = AgglomerativeClustering()
params = {'affinity': 'euclidean', 'compute_distances': False, 'compute_full_tree': 'auto', 'connectivity': None, 
          'distance_threshold': None, 'linkage': 'ward', 'memory': None, 'n_clusters': 5}
clustering.set_params(**params)

# Make predict
y_pred = clustering.fit_predict(X)
print(y_pred)

# Visualising the Hierarchical clusters
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
