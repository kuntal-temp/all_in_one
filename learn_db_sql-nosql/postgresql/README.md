# Basic CMD

PostgreSQL 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, 64-bit

```
>> sudo su - postgres
>> psql
```

- Version Check: 
``` \g   or  select version(); ```

- Quit CMD: 
``` \q ```

- List Users and their Roles: 
``` \du or \du+ ```

- List of Schema: 
``` \dn or \dn+ ```

- List of Function: 
``` \df ```

- List of View: 
``` \dv ```

- List of Databases: 
``` \l or \l+ ```

- Switch to new Databases: 
``` \c  new_database_name ```

- List of Tables: 
``` \dt or \dt+   \dt schema_name.  # by default schema is public ```

- Describe a Table: 
``` \d  table_name  or \d schema.table_name ```





# Create Table - with all Data Type in Postgres
```
    create table if not exists public.table_4(
        id uuid default uuid_generate_v4(),
        p0 serial,
        p1 boolean default false, 
        p2 char(10), p3 varchar(10), 
        p4 text, 
        p5 numeric(8, 2) check(p5>=0),
        p6 integer not null, 
        p7 date default CURRENT_DATE, 
        p8 timestamp, 
        p9 int [], 
        p10 hstore, 
        p11 json,

        primary key(id)
        );
```

```
 Column |            Type             | Collation | Nullable |               Default               
--------+-----------------------------+-----------+----------+-------------------------------------
 id     | uuid                        |           | not null | uuid_generate_v4()
 p0     | integer                     |           | not null | nextval('table_4_p0_seq'::regclass)
 p1     | boolean                     |           |          | false
 p2     | character(10)               |           |          | 
 p3     | character varying(10)       |           |          | 
 p4     | text                        |           |          | 
 p5     | numeric(8,2)                |           |          | 
 p6     | integer                     |           | not null | 
 p7     | date                        |           |          | CURRENT_DATE
 p8     | timestamp without time zone |           |          | 
 p9     | integer[]                   |           |          | 
 p10    | hstore                      |           |          | 
 p11    | json                        |           |          | 
Indexes:
    "table_4_pkey" PRIMARY KEY, btree (id)
Check constraints:
    "table_4_p5_check" CHECK (p5 >= 0::numeric)
```


# DROP TABLE
```
    drop table public.table_4;
```

```
    drop table if exists table_name;
```


# TRUNCATE TABLE [clear all data from table]
```
    truncate table table_name;
```


# Rename Table
```
    alter table public.table_40 rename to public.table_50;
```


# COLUMN Add / Drop
```
    alter table public.table_40 add column new_column_name varchar(20); 

    alter table public.table_40 drop column new_column_name; 
```



# INSERT Data
```
insert into public.table_4 (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11) values 
(
    true, 'p2-0', 'p3-0', 'p4-0', 199999.99, 11, 
    '2022-07-25', '2016-06-22 19:10:25-07',
    ARRAY[123, 321], 
    '"k1"=>"v1", "k2"=>"v2"',
    '{"k1":"v1", "k2":"v2"}'
);
```


# INSERT ON CONFLICT
Note: this can only fit where unique constrain present
```
    insert into
        customers (name, email)
    values
        ('IBM', 'contact@ibm.com'),
        ('Microsoft', 'contact@microsoft.com'),
        ('Intel', 'contact@intel.com');
```

Now ON CONFLICT No Action
```
    insert into 
        customers (name, email)
    values
        ('Microsoft','hotline@microsoft.com')
    on conflict 
        (name)
    do 
        nothing;
```

Now ON CONFLICT with Action
```
    insert into 
        customers (name, email)
    values
        ('Microsoft','hotline@microsoft.com')
    on conflict 
        (name)
    do 
        update set email = excluded.email || ';' || customers.email;
```



# Select Query
```
    select * from public.table_4;
```

```
    select
        p2 || ' ' || p3 as merge_col, p9
    from
        public.table_4;;
```

```
    select TO_CHAR(p7, 'dd/mm/yyyy')  from public.table_4;  [date]
```

```
    select p9, p10, p11 from public.table_4 where p9[1]=123;   [array]
```

```
    select p9, p10, p11->'k1' from public.table_4;  [json]
```

```
    SELECT * from public.books WHERE  attr->'paperback'='5';  [hstore]
```




###################### SAMPLE TABLE FOR QUERY ######################

```
    create table public.table_5 (id uuid default uuid_generate_v4(), url text);
```

```
 Column | Type | Collation | Nullable |      Default       
--------+------+-----------+----------+--------------------
 id     | uuid |           |          | uuid_generate_v4()
 url    | text |           |          | 

```

```
    insert into public.table_5 (url) values ('www.gggg.com');
```

```
    insert into public.table_5 (url) values ('www.bing.com');
```


# UPDATE

update table_name
    set column1 = value1,
    column2 = value2,
    ...
where condition;


```
    update public.table_5 set url='www.google.com' where id='89';
```

```
    update public.table_5 as mytab set url=concat(mytab.url, 'www.ibm.com')  where id=1;
```



# DELETE

delete from 
    table_name 
where 
    condition;

```
    delete from public.table_5 where id='89';
```

[delete & return the deleted data]
```
delete from public.table_5 where id='79f' returning *;
```


# ORDER BY

default = ASC

```
    select
        first_name,
        last_name
    from
        customer
    order by
        first_name ASC, last_name DESC ;
```

```
    select
        first_name,
        last_name
    from
        customer
    order by
        first_name DESC;
```


# GROUP BY
```
    select
        customer_id
    FROM
        payment
    GROUP BY
        customer_id;
```


# HAVING
```
    select
        customer_id
    FROM
        payment
    GROUP BY
        customer_id;
```


# DISTINCT
```
    SELECT
        customer_id, SUM (amount)
    FROM
        payment
    GROUP BY
        customer_id
    HAVING
        SUM (amount) > 200;
```


# WHERE
```
    SELECT
        last_name,
        first_name
    FROM
        customer
    WHERE
        first_name = 'Jamie';
```

# <> <=> not equal 
```
    SELECT
        last_name,
        first_name
    FROM
        customer
    WHERE
        first_name <> 'Jamie';
```

# AND
```
    SELECT
        last_name,
        first_name
    FROM
        customer
    WHERE
        first_name = 'Jamie' AND last_name = 'Rice';
```

# OR
```
    SELECT
        last_name,
        first_name
    FROM
        customer
    WHERE
        first_name = 'Jamie' OR last_name = 'Rice';
```

# IN
```
    SELECT
        last_name,
        first_name
    FROM
        customer
    WHERE
        first_name IN ('Ann','Anne','Annie');
```

# Like
'foo' LIKE 'foo', -- true
'foo' LIKE 'f%', -- true
'foo' LIKE '_o_', -- true
'bar' LIKE 'b_'; -- false

```
    SELECT
        last_name,
        first_name
    FROM
        customer
    WHERE
        LIKE 'Ann%';
```

#  LIMIT & OFFSET
```
    SELECT
        film_id, title, release_year
    FROM
        film
    ORDER BY
        film_id
    LIMIT 4 OFFSET 3;
```

# BETWEEN
```
    SELECT
        customer_id, payment_id, amount
    FROM
        payment
    WHERE
        amount BETWEEN 8 AND 9;
```


# Temporary Table
Exampl-1:
```
    create temp table new_temp_table_7 as select * from public.table_6;
```


# SUBQUERY
```
    SELECT
        film_id, title, rental_rate
    FROM
        Film
    WHERE
        rental_rate > ( SELECT AVG (rental_rate) FROM film );
```
