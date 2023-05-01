> docker-compose up --build

Note:
ERROR: Named volume "postgres_data:/var/lib/postgresql/data:rw" is used in service "psql-db" but no declaration was found in the volumes section.


Note:
Creating network "example-3_default" with the default driver
Creating volume "example-3_postgres_data" with default driver
Pulling psql-db (postgres:12.0-alpine)...


Note:
remember, docker-compose can create network automatically but not volume
