# Q&A

Tables, keys, and relationships are the three core components of a relational database.

A major purpose of a database is to provide the user with only as much information as is required of them. This means that the system does not disclose all the details of the data, rather it hides some details of how the data is stored and maintained.


The different levels of the database are implemented through three layers:
1. Internal Level(Physical Level): The lowest level of abstraction, the internal level, is closest to physical storage. It describes how the data is stored concretely on the storage medium.

2. Conceptual Level: This level of abstraction describes what data is concretely stored in the database. It also describes the relationships that exist between the data. At this level, databases are described logically in terms of simple data structures. Users at this level are not concerned with how these logical data structures will be implemented at the physical level.

3. External Level(View Level): It is the level closest to users and is related to the way the data is viewed by individual users.



To store and manage data efficiently in the database let us understand some key terms:

1. Database Schema: It is a design of the database. Or we can say that it is a skeleton of the database that is used to represent the structure, types of data will be stored in the rows and columns, constraints, relationships between the tables.

2. Data Constraints:  In a database, sometimes we put some restrictions on the table that what type of data can be stored in one or more columns of the table, it can be done by using constraints.

3. Data dictionary or Metadata: Metadata is known as the data about the data. Or we can say that the database schema along with different types of constraints on the data is stored by DBMS in the dictionary is known as metadata.

4. Data Engine: It is an underlying component that is used to create and manage various database queries.



Types of DBMS Architecture:

1. 1- Tier Architecture: database is directly available to the user.

2. 2- Tier Architecture: client-server model. The application at the client end directly communicates with the database at the server-side. APIs like ODBC, JDBC are used for this interaction.

3. 3- Tier Architecture: The client does not directly communicate with the server. Instead, it interacts with an application server which further communicates with the database system.








