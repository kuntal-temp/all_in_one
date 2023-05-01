import numpy as np
import pandas as pd

# dataframe = collection of series
df_0 = pd.DataFrame(
    {
        "Name": ["AA", "BB", "CC"],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print("df_0::\n", df_0)

df_describe = df_0.describe().T
print("df_describe::\n", df_describe)
'''
titanic[["Age", "Fare"]].describe()
'''

print("df_0.info()::\n")
df_0.info()

'''
df = pd.DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]}, dtype=bool)
df = pd.DataFrame(
    [
        ("bird", "Falconiformes", 389.0),
        ("bird", "Psittaciformes", 24.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),
)
'''

# Dataframe data type convert for col
'''
dft1 = dft1.astype({"a": np.bool_, "c": np.float64})
'''

# df to numpy
df_to_numpy = df_0.to_numpy()
print("df_to_numpy::\n", df_to_numpy)

# operation
series_age = df_0['Age']
print("series_age::\n", series_age)
series_age_max = df_0['Age'].max()
print("series_age_max::\n", series_age_max)

# value_counts
'''
similar value group by
'''
age_value_count = df_0['Age'].value_counts()
print("age_value_count::\n", age_value_count)

# count
'''
count of all the values for every col
'''
print("df count::\n", df_0.count())

# Example
housing = pd.read_csv("housing.csv")
print("housing::\n", housing)
print("head::\n", housing.head(2))
print("tail::\n", housing.tail(2))
print("all columns =\n", housing.columns)
print("all index =\n", housing.index)
print("data types of dataframe::\n", housing.dtypes)

# select a subset
housing_total_rooms_population = housing[['total_rooms', 'population']]
print("housing_total_rooms_population::\n", housing_total_rooms_population.head(2))

# filter
housing_filter = housing[housing['total_rooms'] > 32099]
print("housing_filter::\n", housing_filter)
'''
- df[df["A"] > 0]
- titanic[titanic["Pclass"].isin([2, 3])]
- titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
- df1.loc['col_1':, 'col_A':'col_C']
- titanic[titanic["Age"].notna()]
- titanic.loc[titanic["Age"] > 35, "Name"]
- titanic.iloc[9:25, 2:5]
- air_quality["new_col"] = air_quality["existing"] * 10
- air_quality["existing"] = air_quality["existing_1"] / air_quality["existing_2"]
- air_quality[air_quality["parameter"] == "no2"]
'''

'''
# columns/index change in DF
df_renamed = df.rename(
    columns={
        "col1": "new_col_B",
        "col2": "new_col_A",
    }
)

df.rename(
    columns={"one": "foo", "two": "bar"},
    index={"a": "apple", "b": "banana", "d": "durian"},
)
'''

'''
# aggregating
df.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

df.agg(np.sum)
df["A"].agg("sum")
df["A].agg(["sum", "mean"])
'''

# sort_values
sort_values = housing.sort_values(by='population').head(2)
print("sort_values::\n", sort_values)
'''
titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
'''

# sort index
'''
df.sort_index()
df.sort_index(ascending=False)
'''

# Indexing
'''
[loc]
- df.loc["20130102":"20130104", ["A", "B"]]
- df.loc[:, ["A", "B"]]
[iloc]
- df.iloc[3]
- df.iloc[3:5, 0:2]
- df.iloc[[1, 2, 4], [0, 2]]
'''

# Nan handling
'''
- df.dropna(how="any")
- df.fillna(value=5)
- pd.isna(df)
'''

# apply function
'''
- df.apply(lambda x: x.max() - x.min())
'''

df_1 = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

# group by
output_0 = df_1.groupby('A').sum()
print(output_0)
output_0 = df_1.groupby(['A', 'B']).sum()
print(output_0)

# Iterating through groups
'''
grouped = df.groupby('A')
for name, group in grouped:
    print(name)
    print(group)

for name, group in df.groupby(['A', 'B']):
    print(name)
    print(group)

grouped[["C", "D"]].aggregate(np.sum)
'''


# deleted col
'''
df.drop(["col_name"], axis=1)
del df["col_name"]
df.pop("col_name")
'''

# delete row
'''
df.drop(["row_index_0", "row_index_1"], axis=0)
'''


# assign [always returns a copy of the data, leaving the original DataFrame untouched]
'''
- iris.assign(sepal_ratio=iris["SepalWidth"] / iris["SepalLength"])

dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])
'''

# arithmetic operation
'''
add(), sub(), mul(), div(), eq, ne, lt, gt, le, ge,  any(), all()
nan+5 = nan
df + df2
>df_0.add(df_1, fill_value=0)

df.gt(df2)

df + df == df * 2
>(df + df).equals(df * 2)

df.mean(0)
df.mean(1)

df.sum(axis=0, skipna=True)
df.sum(axis=1, skipna=True)

df.idxmin(axis=0)
df.idxmax(axis=1)

(df > 0).all()
(df > 0).any()
'''

# Comparing
'''
pd.Series(["foo", "bar", "baz"]) == "foo"
'''

# combine
'''
df1.combine_first(df2)
'''

# transform
'''
df.transform(np.abs)
df.transform("abs")
df["col"].transform(np.abs)

# selective transforming per column
df.transform({"col_A": np.abs, "col_B": lambda x: x + 1})
'''

# map & applymap
'''
 applymap() on DataFrame and analogously map() on Series accept any Python function taking a single value and returning a single value
'''

# reindex
'''
df.reindex(index=["c", "f", "b"], columns=["three", "two", "one"])
'''

# DF iteration [only view]
df = pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})
for index, row in df.iterrows():
    print("index=", index, " :: ", row["a"], "----", row["b"])

# nlargest/nsmallest
'''
df.nlargest(5, ["a", "c"])
df.nsmallest(3, "a")
'''

# Replace a Row
x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
x.iloc[1] = {'x': 9, 'y': 99}
print(x)

# Selecting random samples
df = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
random_sample = df.sample(2)

# query
'''
df[(df['a'] < df['b']) & (df['b'] < df['c'])]
==
df.query('(a < b) & (b < c)')

df[df['a'].isin(df['b'])]
==
df.query('a not in b')
'''

# Multiple Index
'''
you can pass a list of arrays directly into Series or DataFrame to construct a MultiIndex
'''
arrays = [
    np.array(["bar", "bar", "baz", "baz"]),
    np.array(["one", "two", "one", "two"]),
]
df = pd.DataFrame(np.random.randn(4, 5), index=arrays)
print(df)
print("print row = ", df.loc[("bar", "two")])
print("print data from 1st index = ", df.loc["bar"])
print(df.loc["baz":"foo"])

arrays = [
    np.array(["bar_0", "bar_1", "baz_0", "baz_1"]),
    np.array(["one", "two", "one", "two"]),
]
df = pd.DataFrame(np.random.randn(4, 5), index=arrays)
print(df)






