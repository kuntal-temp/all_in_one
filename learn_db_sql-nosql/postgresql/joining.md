# Joining Query

PostgreSQL supports Inner join, Left join, Right join, Full outer join, Cross join, 
Natural join, and a special kind of join called Self-join


# Inner Join
```
    select * from t1 inner join t2 on t1.key=t2.key;
```

# LEFT Join
```
    select * from t1 left join t2 on t1.key=t2.key;
```

# Right Join
```
   select * from t1 right join t2 on t1.key=t2.key; 
```

# LEFT Outer Join
```
    select * from t1 left join t2 on t1.key=t2.key where t2.key is null;
```

# Right Outer Join
```
   select * from t1 right join t2 on t1.key=t2.key where t1.key is null;
```

# Full Join
```
   select * from t1 full join t2 on t1.key=t2.key;
```

# Full Outer Join
```
   select * from t1 full join t2 on t1.key=t2.key where t1.key is null OR t2.key is null;
```

# Cross Join
```
   select * from t1 cross join t2;
```
