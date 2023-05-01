# score
score = classifier.score(X_test, Y_pred)
print("score = ", score)

# confusion matrix
con_matrix = confusion_matrix(Y_test, Y_pred)
print("confusion matrix = ", con_matrix)

# accuracy score
acc_score = accuracy_score(Y_test, Y_pred)
print("accuracy score = ", acc_score)


# zero one loss
"""
  If normalize is True, return the fraction of misclassifications (float), 
  else it returns the number of misclassifications (int). 
  The best performance is 0.
  
  normalize = True/False
"""
zero_one_loss(Y_test, Y_pred, normalize=True)



# Compare between Actual and Predicted
compare_predict_data = np.concatenate((Y_pred.reshape(len(Y_pred),1), Y_test.reshape(len(Y_test),1)),1)[0:5]
print(compare_predict_data)
