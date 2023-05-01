# boolean
```
    create table stock_availability (
    product_id int primary key,
    available boolean not null /# default false;
    );
```

BOOLEAN that can have three values: true, false and NULL.
TRUE,‘t’, ‘yes’, ‘y’, ‘1’
FALSE, ‘f’, ‘no’, ‘n’, ‘0’
SELECT *
FROM stock_availability
WHERE available = 'yes';
SELECT *
FROM stock_availability
WHERE available = 'no';
SELECT *
FROM stock_availability
WHERE NOT available;



# CHAR/ VARCHAR/ TEXT 
```
    create table character_tests (
        id serial primary key,
        x char (1),
        y varchar (10),
        z text );
```


#  NUMERIC
```
    create table products (
        id serial primary key,
        price numeric(5,2)
    );
```
numeric(precision) / numeric(precision, scale)
1234.567 has the precision 7 and scale 3
in addition to holding numeric values, the numeric type can also hold a special value called nan which stands for not-a-number



# INTEGER
```
    create table cities (
    city_id serial primary key,
    population int not null check (population >= 0)
    );
```

To store the whole numbers in PostgreSQL, you use one of the following 
integer types: 
* SMALLINT
* INTEGER
* BIGINT. 
PostgreSQL does not provide unsigned integer types



# DATE
```
    create table documents (
	user_id serial primary key,
	posting_date date not null default current_date,
    birth_date date not null
    );
```
default date format: yyyy-mm-dd format e.g., 2000-12-31

To get current date: SELECT CURRENT_DATE;
    or
SELECT NOW()::date;
    or
SELECT TO_CHAR(NOW()::DATE, 'dd/mm/yyyy');
    or
SELECT TO_CHAR(NOW()::DATE, 'Mon dd, yyyy');

SELECT 
    first_name, 
    last_name, 
    now() - hire_date as diff 
FROM 
    Table;

SELECT
    employee_id,
    first_name,
    last_name,
    AGE(birth_date)
FROM
     employees;

SELECT
	employee_id,
	first_name,
	last_name,
	age('2015-01-01',birth_date)
FROM
	employees;



#  TIMESTAMP
```
    create table timestamp_demo (
    ts timestamp, 
    tstz timestamptz
    );
```
Now need to set Time zone: SET timezone = 'America/Los_Angeles';



# UUID
```
    create table contacts (
    contact_id uuid default uuid_generate_v4 (),
    phone varchar,
    primary key (contact_id)
    ); 
```
To Install it:  create extension if not exists "uuid-ossp";

To Generate UUID:  
SELECT uuid_generate_v1();
    Or
SELECT uuid_generate_v4();



# SERIAL
```
    create table table_name(
    id serial
    );
```



# ARRAY
```
    create table contacts (
        id serial primary key,
        name varchar (100),
        phones text []
    );
```
Insert Data:

INSERT INTO contacts (name, phones) VALUES('John Doe',ARRAY ['(408)-589-5846','(408)-589-5555']);



# HSTORE
```
    create table books (
	id serial primary key,
	title varchar (255),
	attr hstore
    );
```
create extension if not exists hstore;

Insert Data:

INSERT INTO books (title, attr)
VALUES
(
    'PostgreSQL Cheat Sheet',
    '
    "paperback" => "5",
    "publisher" => "postgresqltutorial.com",
    "language"  => "English",
    "ISBN-13"   => "978-1449370001",
    "weight"    => "1 ounces"
    '
);

query: 

SELECT * from public.books WHERE  attr->'paperback'='5';
select p10->'k1' as as k1_key, p11 from public.table_4;



# JSON
```
    create table orders (
	id serial not null primary key,
	info json not null
    );
```
INSERT INTO orders (info) VALUES(
    '{ "customer": "John Doe", "items": {"product": "Beer","qty": 6}}'
);

select p9, p10, p11->'k1' from public.table_4;
