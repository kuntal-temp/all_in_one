classifier = KNeighborsClassifier()
params = {'algorithm': 'auto', 'leaf_size': 30, 'metric': 'minkowski', 'metric_params': None, 'n_jobs': None, 
          'n_neighbors': 5, 'p': 2, 'weights': 'uniform'}
classifier.set_params(**params)

classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)