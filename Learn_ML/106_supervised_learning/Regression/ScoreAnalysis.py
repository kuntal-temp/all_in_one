# Score
training_score = regressor.score(X_train, Y_train)
test_score = regressor.score(X_test, Y_test)
print("training_score = ", training_score)
print("test_score = ", test_score)

# R2 Score
r_2_score = r2_score(Y_test, Y_pred)
print("r_2_score = ", r_2_score)

# Mean Squared Error
mse = mean_squared_error(Y_test, Y_pred, squared=False)
print("mse = ", mse)
rmse = mean_squared_error(Y_test, Y_pred, squared=True)
print("rmse = ", rmse)

# Compare between Actual and Predicted
compare_predict_data = np.concatenate((Y_pred.reshape(len(Y_pred),1), Y_test.reshape(len(Y_test),1)),1)[0:5]
print(compare_predict_data)
