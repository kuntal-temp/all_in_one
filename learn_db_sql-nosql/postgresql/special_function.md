# Special Function


# String Function

1. CONCAT

```
    update public.table_5 as mytab set url=concat(mytab.url, 'www.ibm.com')  where id=1;

    select concat_ws('.', 'www', 'google', 'com');
```

2. SUBSTRING / LEFT / RIGHT
```
    select substring('SQL Tutorial', 1, 3) as sub_string;

    select left('SQL Tutorial', 3) as sub_string;

    select right('SQL Tutorial', 3) as sub_string;
```

3. LENGTH
```
    select length('SQL Tutorial');
```

4. LOWER / UPPER
```
    select lower('SQL Tutorial is FUN!');

    select upper('sql tutorial is fun!');
```

5. TRIM / LTRIM / RTRIM
```
    select trim('     sql tutorial    ') as lefttrimmedstring;
```

6. REPLACE
```
    select replace('sql tutorial', 't', 'm');
```

7. REVERSE
```
    select reverse('sql tutorial');
```


# Numeric Functions

1. ABS
```
    SELECT Abs(-243.5) AS AbsNum;
```

2. AVG
```
    select AVG(price) from public.table_6
```

3. COUNT
```
    select count(id) from public.table_6;
```

4. MAX / MIN
```
    select MAX(id) from public.table_6;

    select MIN(id) from public.table_6;
```

5. SUM
```
    select SUM(id) from public.table_6;
```

6. POWER
```
    SELECT POWER(4, 2);
```

7. ROUND
```
    SELECT ROUND(235.415, 2) AS RoundValue;
```

8. SQRT
```
    SELECT SQRT(64);
```


# Date Functions

1. TO_CHAR
```
    select TO_CHAR(join_date, 'dd/mm/yyyy')  from public.table_50;
```

2. EXTRACT
```
    extract (year from birth_date) as year,
    extract (month from birth_date) as month,
    extract (day from birth_date) as day
```
