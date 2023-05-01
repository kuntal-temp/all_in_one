# Uniform Manifold Approximation and Projection [UMAP]
# [Used for Supervised & Unsupervised Learning]

"""
A dimensionality reduction technique that assumes the available data samples are evenly (uniformly) distributed across a topological space (manifold), which can be approximated from these finite data samples and mapped (projected) to a lower-dimensional space.

1. https://towardsdatascience.com/umap-dimensionality-reduction-an-incredibly-robust-machine-learning-algorithm-b5acb01de568


Most importantly, UMAP is fast, scaling well in terms of both dataset size and dimensionality. For example, UMAP can project the 784-dimensional, 70,000-point MNIST dataset in less than 3 minutes, compared to 45 minutes for scikit-learn's t-SNE implementation.
"""

umap = UMAP(n_neighbors=100, n_components=2, n_epochs=1000, min_dist=0.5, local_connectivity=2, random_state=42)

# for unsupervised
X_train = umap.fit_transform(X_train)
X_test = umap.fit_transform(X_test)

# for supervised
X_train = umap.fit_transform(X_train, y_train)
X_test = umap.transform(X_test)
