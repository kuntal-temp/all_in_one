'''
Stacking Regressor
'''

estimators = [
    ('lr', RidgeCV()),
    ('svr', LinearSVR(random_state=42))
]

reg = StackingRegressor(
    estimators=estimators, final_estimator=RandomForestRegressor(n_estimators=10, random_state=42)
)

reg.fit(X_train, y_train)