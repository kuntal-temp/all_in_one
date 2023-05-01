# Multidimensional Scaling
# [Used for Unsupervised Learning]

"""
MDS is a non-linear technique for embedding data in a lower-dimensional space.

Multidimensional Scaling is a good technique to use when you wish to preserve both global and local structures of your high-dimensional data. This is achieved by keeping distances between points in lower dimensions as similar as possible to distances in the original high-dimensional space.

Euclidean distance is preserved in Metric MDS
"""

# Find n_components from graph
stress, max_range = [], 10

for i in range(1, max_range):
    params = {'dissimilarity': 'euclidean', 'eps': 0.001, 'max_iter': 300, 'metric': True, 
          'n_components': i, 'n_init': 4, 'n_jobs': None, 'random_state': 0, 'verbose': 0}
    mds = MDS()
    mds.set_params(**params)
    X_train = mds.fit_transform(X_train)
    stress.append(mds.stress_)

plt.plot(range(1, max_range), stress)
plt.xticks(range(1, max_range, 2))
plt.xlabel('n_components [dissimilarity = euclidean]')
plt.ylabel('stress')
plt.show()


# Train Model
mds = MDS()
params = {'dissimilarity': 'euclidean', 'eps': 0.001, 'max_iter': 300, 'metric': True, 
          'n_components': 2, 'n_init': 4, 'n_jobs': None, 'random_state': 0, 'verbose': 0}
mds.set_params(**params)

X_train = mds.fit_transform(X_train)
X_test = mds.fit_transform(X_test)




# ---------------------------------------------------

# Plotting n_components graph
stress1, stress2, max_range = [], [], 11
dist_euclidean = euclidean_distances(X_train)
dist_manhattan = manhattan_distances(X_train)

for i in range(1, max_range):
    params = {'dissimilarity': 'precomputed', 'eps': 0.001, 'max_iter': 300, 'metric': True, 
          'n_components': i, 'n_init': 4, 'n_jobs': None, 'random_state': 0, 'verbose': 0}
    mds1 = MDS()
    mds2 = MDS()
    mds1.set_params(**params)
    mds2.set_params(**params)
    pts1 = mds1.fit_transform(dist_euclidean)
    pts2 = mds2.fit_transform(dist_manhattan)
    stress1.append(mds1.stress_)
    stress2.append(mds2.stress_)

plt.plot(range(1, max_range), stress1)
plt.xticks(range(1, max_range, 2))
plt.xlabel('n_components')
plt.ylabel('stress euclidean')
plt.show()

plt.plot(range(1, max_range), stress2)
plt.xticks(range(1, max_range, 2))
plt.xlabel('n_components')
plt.ylabel('stress manhattan')
plt.show()


mds = MDS()
params = {'dissimilarity': 'precomputed', 'eps': 0.001, 'max_iter': 300, 'metric': True, 
          'n_components': 2, 'n_init': 4, 'n_jobs': None, 'random_state': 0, 'verbose': 0}
mds.set_params(**params)

X_train = mds.fit_transform(X_train)
X_test = mds.fit_transform(X_test)