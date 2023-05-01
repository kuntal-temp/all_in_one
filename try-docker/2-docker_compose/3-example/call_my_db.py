import psycopg2
import random
from structlog import get_logger
log = get_logger()


db, user, password = 'postgres', 'postgres', '', 
host = 'my-postgres-db'  # main logic


def connect_db():
    try:
        connection = psycopg2.connect(
            database=db, user = user,
            password = password, host = host,
            port = "5432"
        )
        log.info("Database Connected")
        return connection
    except Exception as e:
        log.debug(f"Unable to connect DB Exception : {e}")


def create_table():
    connection = connect_db()
    cursor_object = connection.cursor()
    query = '''CREATE TABLE MyTable 
        (id SERIAL PRIMARY KEY,firstname Text,lastname Text,phone CHAR(10));'''
    try:
        cursor_object.execute(query)
        connection.commit()
        connection.close()
        log.info("Table created successfully")
    except Exception as e:
        log.debug("create_table exception : {e}")


def insert_data_into_table():
    try:
        create_table()
    except:
        pass
    connection = connect_db()
    cursor_object = connection.cursor()
    query = '''INSERT INTO MyTable (id, firstname, lastname, phone) 
        VALUES ('''+str(random.randint(1, 100000))+''', 'Kuntal', 'Samanta', 9876543210);'''
    try:
        cursor_object.execute(query)
        connection.commit()
        connection.close()
        log.info("Record created successfully")
    except Exception as e:
        log.debug("insert_data_into_table exception : {e}")
