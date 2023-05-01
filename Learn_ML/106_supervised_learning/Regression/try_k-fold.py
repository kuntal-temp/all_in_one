# K-fold Cross-Validation

# Way 1
accuracies = cross_val_score(estimator = regressor, X = X_train, y = Y_train, cv = 5)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


# Way 2
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
accuracies = cross_val_score(regressor, X, y, cv=cv, n_jobs=-1)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
