'''
Voting Regressor

A voting regressor is an ensemble meta-estimator that fits several base regressors, each on the whole dataset. Then it averages the individual predictions to form a final prediction.
'''

r1 = LinearRegression()
r2 = RandomForestRegressor(n_estimators=10, random_state=1)
r3 = KNeighborsRegressor()

estimators = [
    ('r1', r1),
    ('r2', r2),
    ('r3', r3)
]

reg = VotingRegressor(estimators=estimators)

reg.fit(X, y)
reg.predict(X)