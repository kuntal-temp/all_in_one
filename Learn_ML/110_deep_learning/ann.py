# Artificial Neural Network [ANN]

ann = tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
ann.fit(X_train, Y_train, batch_size = 32, epochs = 100)

y_pred = ann.predict(X_test)
# y_pred = (y_pred > 0.5)  # [compare from set threshold]

cm = confusion_matrix(Y_test, y_pred)
print("confusion matrix = ", cm)
acc = accuracy_score(Y_test, y_pred)
print("accuracy score = ", acc)
print(ann.evaluate(X_test, Y_test))


# Compare between actual and predicted
print(np.concatenate((y_pred.reshape(len(y_pred),1), Y_test.reshape(len(Y_test),1)),1)[0:10])


# Try to predict
print(ann.predict(sc.transform([[619, 1, 1, 42, 2, 0.0, 1, 0, 0, 101348.88]])) > 0.5)
