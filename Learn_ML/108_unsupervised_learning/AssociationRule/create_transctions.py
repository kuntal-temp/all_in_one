# Creating Transactions

transactions = []
for i in range(0, len(dataset)):
  transactions.append([str(dataset.values[i,j]) for j in range(0, len(dataset.columns))])