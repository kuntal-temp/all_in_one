classifier = GaussianNB()
params = {'priors': None, 'var_smoothing': 1e-09}
classifier.set_params(**params)

classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)