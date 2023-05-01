# Adaptive Boosting

classifier = AdaBoostClassifier()
params = {'algorithm': 'SAMME.R', 'base_estimator': None, 'learning_rate': 1.0, 'n_estimators': 50, 'random_state': None}
classifier.set_params(**params)

classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)