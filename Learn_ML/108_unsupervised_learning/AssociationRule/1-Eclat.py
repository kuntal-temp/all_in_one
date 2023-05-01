"""
Eclat Model is based on Set Of Products, so min_confidence and min_lift is not considered
Note: min_support is only required
min_confidence: Optional(Not required for this)
min_lift: Optional(Not required for this)
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
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

# Print Outcome
print(resultsinDataFrame.nlargest(n = 10, columns = 'Support'))
