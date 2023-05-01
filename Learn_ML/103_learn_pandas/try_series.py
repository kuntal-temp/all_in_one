import pandas as pd
import numpy as np

# series
l1 = [10*i for i in range(1, 5)]
series_100 = pd.Series(data=l1, dtype='float', index=['A', 'B', 'C', 'D'], name="Learn Series")
print("series_100::\n", series_100, "type=", type(series_100), "shape=", series_100.shape,
      "size=", series_100.size, "ndim=", series_100.ndim, "dtype=", series_100.dtype, "name=", series_100.name)

# series to numpy
numpy_array = series_100.to_numpy()
print("numpy_array::\n", numpy_array)

to_list = series_100.to_list()
print("to_list::\n", numpy_array)

l1 = [
    [10, 20],
    [30, 40]
]
series_100 = pd.Series(data=l1, dtype='float')
print("series_100::\n", series_100, "type=", type(series_100), "shape=", series_100.shape, "size=", series_100.size)

d1 = {'a': 10, 'b': 20}
series_100 = pd.Series(data=d1, dtype='int')
print("series_100::\n", series_100, "type=", type(series_100), "shape=", series_100.shape, "size=", series_100.size)

d1 = {'a': [10, 20], 'b': [20, 10]}
series_100 = pd.Series(data=d1, dtype='int')
print("series_100::\n", series_100, "type=", type(series_100), "shape=", series_100.shape, "size=", series_100.size)

n1 = np.arange(10, 20, 2)
series_100 = pd.Series(data=n1)
print("series_100::\n", series_100)

n1 = np.ones((3,4))
l1 = n1.tolist()
series_100 = pd.Series(data=l1, index=['X', 'Y', 'Z'])
print("series_100::\n", series_100)

# diff pandas array type
'''
Categorical
PeriodArray
IntervalArray
IntegerArray
StringArray
BooleanArray
DatetimeArray
'''
cat_array = pd.Categorical(['a', 'b', 'a'])
print("cat_array::\n", cat_array)

# iteration
series_200 = pd.Series(['A', 'B', 'C'])
print("series keys", series_200.keys())
for index, value in series_200.items():
    print(index, value)

# index
output_100 = series_200.get(0)
print("output_100::GET\n", output_100)
output_100 = series_200.loc[: 1]
print("output_100::LOC\n", output_100)
series_100 = pd.Series([10, 20, 30, 40, 50])
series_pop = series_100.pop(2)
print("series_pop::\n", series_pop)

# operations
a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
series_add = a.add(b, fill_value=0)
print("series_add::\n", series_add)
series_subtract = a.subtract(b, fill_value=0)
print("series_subtract::\n", series_subtract)
series_mod = a.mod(b, fill_value=0)
print("series_mod::\n", series_mod)
series_lt = a.lt(b, fill_value=0)
series_le = a.le(b, fill_value=0)

array_0 = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])
def square(x):
    return x*x
output_100 =  array_0.apply(square)
print("apply function::\n", output_100)

# agg
array_0 = pd.Series([10, 20, 30, 40])
agg = array_0.agg('min')
agg_min_max = array_0.agg(['min', 'max'])
print("agg::\n", array_0)

# max, count, min, median, mean, mode
array_0 = pd.Series([20, 21, 12], index=['London', 'New York', 'Helsinki'])
max_val = array_0.max()
print("max_val::\n", max_val)
nlargest_val = array_0.nlargest(2)
print("nlargest_val::\n", nlargest_val)
nsmallest_val = array_0.nsmallest(2)
print("nsmallest_val::\n", nsmallest_val)
array_0 = pd.Series(data=np.arange(3), index=['A', 'B', 'C'])
drop_value = array_0.drop(labels=['B', 'C'])
print("drop_value::\n", drop_value)

# argmax, argmin
array_0 = pd.Series([10, 20, 30, 40])
arg_max_value = array_0.argmax()
print("arg_max_value::\n", arg_max_value)

# update
array_0 = pd.Series([10, 20, 30, 40])
array_0.update(pd.Series([4, 5, 6]))
array_0.update(pd.Series(['d', 'e'], index=[0, 2]))


# values and value_counts
series_100 = pd.Series([1, 2, 3, 2, 5, 1])
series_100_values = series_100.values
print("series_100_values::\n", series_100_values)
series_100_val_counts = series_100.value_counts()
print("series_100_val_counts::\n", series_100_val_counts)

# astype
series_100 = pd.Series([1, 2, 3, 2, 5, 1])
series_100 = series_100.astype('complex')
print("astype::\n", series_100)
series_100 = series_100.astype('category')
print("astype-category::\n", series_100)

# drop nan
array_0 = pd.Series([1., 2., np.nan])
output_dropna = array_0.dropna()
print("output_dropna::\n", output_dropna)

# where
array_0 = pd.Series(range(2, 8))
output_where = array_0.where(array_0 > 5)
print("output_where::\n", output_where)

# str operation
array_0 = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
output_str_lower = array_0.str.lower()
print("output_str_lower::\n", output_str_lower)

output_str_upper = array_0.str.upper()
print("output_str_upper::\n", output_str_upper)

# reindex
'''
s.reindex(["e", "b", "f", "d"])
'''