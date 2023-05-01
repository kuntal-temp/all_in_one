# xg_boost

# Way1
classifier = XGBClassifier()
classifier.fit(X_train, y_train)
Y_pred = classifier.predict(X_test)

# Way2
classifier = XGBRFClassifier()
classifier.fit(X_train, y_train)
Y_pred = classifier.predict(X_test)