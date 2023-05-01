# Kernel Principal Component Analysis [K-PCA]
# [Used for Unsupervised Learning]

'''
There are various kernel methods like linear, polynomial, and gaussian.


'''

kpca = KernelPCA(n_components = 2, kernel = 'rbf')
X_train = kpca.fit_transform(X_train)
X_test = kpca.fit_transform(X_test)