# Eclat with Other Python Package [For small dataset]
transactions = [
    ['beer', 'wine', 'cheese'],
    ['beer', 'potato chips'],
    ['eggs', 'flower', 'butter', 'cheese'],
    ['eggs', 'flower', 'butter', 'beer', 'potato chips'],
    ['wine', 'cheese'],
    ['potato chips'],
    ['eggs', 'flower', 'butter', 'wine', 'cheese'],
    ['eggs', 'flower', 'butter', 'beer', 'potato chips'],
    ['wine', 'beer'],
    ['beer', 'potato chips'],
    ['butter', 'eggs'],
    ['beer', 'potato chips'],
    ['flower', 'eggs'],
    ['beer', 'potato chips'],
    ['eggs', 'flower', 'butter', 'wine', 'cheese'],
    ['beer', 'wine', 'potato chips', 'cheese'],
    ['wine', 'cheese'],
    ['beer', 'potato chips'],
    ['wine', 'cheese'],
    ['beer', 'potato chips']
]
dataset = pd.DataFrame(transactions)


from pyECLAT import ECLAT

min_support = 5/len(transactions)
min_n_products = 2
max_length = max([len(x) for x in transactions])

my_eclat = ECLAT(data=dataset, verbose=True)
rule_indices, rule_supports = my_eclat.fit(min_support=min_support, min_combination=min_n_products, max_combination=max_length)
print("\n\nrule_supports : \n", rule_supports)