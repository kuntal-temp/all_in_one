# Gaussian Mixture Model

model = GaussianMixture(n_components=2)
model.fit(X)
yhat = model.predict(X)
print(yhat)