# KMeans Clustering

""" Elbow Method """
# Number of cluster choosing
wcss = []
for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 15), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# Now trained your model
clustering = KMeans()
params = {'algorithm': 'auto', 'copy_x': True, 'init': 'k-means++', 'max_iter': 300, 
          'n_clusters': 5, 'n_init': 10, 'random_state': 42, 'tol': 0.0001, 'verbose': 0}
clustering.set_params(**params)
clustering.fit(X)

# Make Predict
y_pred = clustering.predict(X)
print(y_pred)

# Visualising the KMeans clusters
plt.scatter(X[y_pred == 0, 0], X[y_pred == 0, 1], s = 100, c = 'red', label = 'Cluster 1', marker='1')
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], s = 100, c = 'blue', label = 'Cluster 2', marker='2')
plt.scatter(X[y_pred == 2, 0], X[y_pred == 2, 1], s = 100, c = 'green', label = 'Cluster 3', marker='3')
plt.scatter(X[y_pred == 3, 0], X[y_pred == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4', marker='+')
plt.scatter(X[y_pred == 4, 0], X[y_pred == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5', marker='.')
plt.scatter(X[y_pred == 5, 0], X[y_pred == 5, 1], s = 50, c = 'hotpink', label = 'Cluster 6', marker='h')
plt.scatter(X[y_pred == 6, 0], X[y_pred == 6, 1], s = 100, c = 'orange', label = 'Cluster 7', marker='*')
plt.scatter(X[y_pred == 7, 0], X[y_pred == 7, 1], s = 100, c = 'coral', label = 'Cluster 8', marker='.')
plt.scatter(clustering.cluster_centers_[:, 0], clustering.cluster_centers_[:, 1], s = 50, c = 'yellow', label = 'Centroids')
plt.title('KMeans Clusters')
plt.xlabel('your x level')
plt.ylabel('your y level')
plt.legend()
plt.show()