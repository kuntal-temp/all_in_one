# Key & Constraints


# CHECK / NOT NULL / UNIQUE
```
    create table test_table (
        id serial primary key,
        ...
        email char(20) unique,
        y integer not null,
        z integer check(z>=0),
        birth_date date check (birth_date > '1900-01-01'),
        ...
        );
```


# Primary Key
```
    create table test_table (
        id serial,
        ...
        x char(10) unique,
        y integer not null,
        z integer check(z>=0),
        ...

        primary key (id, y)
        );
```

```
    Column     |          Type          | Collation | Nullable |                     Default                     
---------------+------------------------+-----------+----------+-------------------------------------------------
 id   | integer                |           | not null | nextval('test_table_id_seq'::regclass)
 y    | character varying(255) |           |          | 
Indexes:
    "test_table_pkey" PRIMARY KEY, btree (id, y)
```


1. Add Primary Key in Existing Table
```
    alter table table_name add primary key (column_1, column_2);
```

2. Remove primary key
```
    alter table table_name drop constraint primary_key_constraint;
                    OR
    alter table table_4 drop constraint table_4_pkey;
```


# Foreign Key
```
create table customers(
    customer_id serial,
    customer_name varchar(255),

    primary key(customer_id)
);

create table contacts(
    contact_id serial,
    customer_id int,
    phone varchar(15),

    primary key(contact_id),
    foreign key(customer_id) references customers(customer_id) ON DELETE CASCADE
);
```

```
    Column     |          Type          | Collation | Nullable |                    Default                     
---------------+------------------------+-----------+----------+------------------------------------------------
 customer_id   | integer                |           | not null | nextval('customers_customer_id_seq'::regclass)
 customer_name | character varying(255) |           |          | 
Indexes:
    "customers_pkey" PRIMARY KEY, btree (customer_id)
Referenced by:
    TABLE "contacts" CONSTRAINT "contacts_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE


   Column    |         Type          | Collation | Nullable |                   Default                    
-------------+-----------------------+-----------+----------+----------------------------------------------
 contact_id  | integer               |           | not null | nextval('contacts_contact_id_seq'::regclass)
 customer_id | integer               |           |          | 
 phone       | character varying(15) |           |          | 
Indexes:
    "contacts_pkey" PRIMARY KEY, btree (contact_id)
Foreign-key constraints:
    "contacts_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
```


insert into customers(customer_name) values
('bluebird inc'), 
('dolphin llc');

insert into contacts(customer_id, contact_name, phone, email) values
(1,'john doe','(408)-111-1234','john.doe@bluebird.dev'),
(1,'jane doe','(408)-111-1235','jane.doe@bluebird.dev'),
(2,'david wright','(408)-222-1234','david.wright@dolphin.dev');


Action Listing:
    1) SET NULL
    2) SET DEFAULT
    3) RESTRICT
    4) NO ACTION
    5) CASCADE

