# Model Improvement

from scipy.stats import randint

parameters = {"max_depth": [3, None],
              "max_features": randint(1, 9),
              "min_samples_leaf": randint(1, 9),
              "criterion": ["gini", "entropy"]}

random_search = RandomizedSearchCV(estimator=regressor, param_distributions=parameters, cv = 5)
random_search.fit(X_train, Y_train)

best_accuracy = random_search.best_params_
best_parameters = random_search.best_score_

print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)