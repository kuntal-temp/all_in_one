"""
Note: min_support => 3*7/7501 [3 time a day for a week]
Note: min_confidence => Default is 0.8, but first start with 0.8 than come 0.7,0.6,0.5,0.4....0.2,0.1 like this
Note: min_lift => Choose a value 3 or more
Note: Buy 2 and get 3rd product free, Buy 10 and get 1 free
min_length => 3, 2
max_length => 3, 11
"""

rules = apriori(
      transactions = transactions, min_support = 0.003, min_confidence = 0.2, 
      min_lift = 3, min_length = 2, max_length = 2
    )

# printing the rules
results = list(rules)
for i in range(5):
    print(results[i])


def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))

resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

# Print Outcome
print(resultsinDataFrame.nlargest(n = 10, columns = 'Lift'))