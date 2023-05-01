# Linear Discriminant Analysis [LDA]
# [Used for Supervised Learning]

'''
LDA is mainly used in classification problems.

1) Assumes the data to be distributed normally or Gaussian distribution of data points i.e. each feature must make a bell-shaped curve when plotted. 
2) Each of the classes has identical covariance matrices.

Linear discriminant analysis is not just a dimension reduction tool, but also a robust classification method.
'''

lda = LDA(n_components = 2)
print(lda.explained_variance_ratio_)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)
