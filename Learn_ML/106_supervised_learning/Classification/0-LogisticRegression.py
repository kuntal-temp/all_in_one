'''
It is often used for classification and predictive analytics. Logistic regression estimates the probability of an event occurring.
Since the outcome is a probability, the dependent variable is bounded between 0 and 1.
For binary classification, a probability less than .5 will predict 0 while a probability greater than 0 will predict 1.

1) Binary logistic regression (It has only two possible outcomes)
2) Multinomial logistic regression (It has three or more possible outcomes)
3) Ordinal logistic regression (Response variable has three or more possible outcome)

It is also considered a discriminative model, which means that it attempts to distinguish between classes (or categories).

solver : {‘lbfgs’, ‘liblinear’, ‘newton-cg’, ‘newton-cholesky’, ‘sag’, ‘saga’} ‘multinomial’ option is supported only by the ‘lbfgs’, ‘sag’, ‘saga’ and ‘newton-cg’ solvers.

penalty : The ‘newton-cg’, ‘sag’, and ‘lbfgs’ solvers support only L2 regularization with primal formulation, or no regularization. The ‘liblinear’ solver supports both L1 and L2 regularization, with a dual formulation only for the L2 penalty. The Elastic-Net regularization is only supported by the ‘saga’ solver.

‘lbfgs’ - [‘l2’, None]
‘liblinear’ - [‘l1’, ‘l2’]
‘newton-cg’ - [‘l2’, None]
‘newton-cholesky’ - [‘l2’, None]
‘sag’ - [‘l2’, None]
‘saga’ - [‘elasticnet’, ‘l1’, ‘l2’, None]

multi_class : If the option chosen is ‘ovr’, then a binary problem is fit for each label. `Multinomial’ is unavailable when solver=’liblinear’. ‘auto’ selects ‘ovr’ if the data is binary, or if solver=’liblinear’, and otherwise selects ‘multinomial’.

class_weight : Weights associated with classes in the form {class_label: weight}. If not given, all classes are supposed to have weight one.
'''

classifier = LogisticRegression()
params = {'C': 1.0, 'class_weight': None, 'dual': False, 'fit_intercept': True, 'intercept_scaling': 1, 
          'l1_ratio': None, 'max_iter': 100, 'multi_class': 'auto', 'n_jobs': None, 'penalty': 'l2', 
          'random_state': 0, 'solver': 'lbfgs', 'tol': 0.0001, 'verbose': 0, 'warm_start': False}
classifier.set_params(**params)

classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

