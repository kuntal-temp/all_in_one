# AdaBoost or Adaptive Boosting
'''
AdaBoost algorithms can be used for both classification and regression problem.

base_estimator/estimator: The base estimator from which the boosted ensemble is built. If None, then the base estimator is DecisionTreeRegressor initialized with max_depth=3. 
'''

from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

#Choosing Decision Tree with 1 level as the weak learner
DTR=DecisionTreeRegressor(max_depth=1)
regr = AdaBoostRegressor(n_estimators=50, base_estimator=DTR ,learning_rate=1)
regr.fit(X, y)
