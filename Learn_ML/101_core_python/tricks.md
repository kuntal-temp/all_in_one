```
    print(True + False + False) # -> 1
```

```
    print("https://www.{url}.com".format(url="google"))

    data = dict(v1="Python", v2="Programming")
    print("I love {v1} {v2}".format(**data))
```

```
# l[start:end:step]

l = [10,20,30,40,50]
> l[1:3:2]
> l[::2]
> l[::-1]
```

```
xx = 'Abc Xyz'
print(xx[1:-2])  # [positive: negative]
print(xx[-3:-1]) # [negative: negative]

print(xx[-1:2])  # no output for [negative: positive]
```

- Difference between == & is?
> The Equality operator (==) is a comparison operator in Python that compare values of both the operands and checks for value equality. Whereas the ‘is’ operator is the  identity operator that checks whether both the operands refer to the same object or not (present in the same memory location).
```
> x=40
> y=x
> id(x) # -> 9802496
> id(y) # -> 9802496
```
