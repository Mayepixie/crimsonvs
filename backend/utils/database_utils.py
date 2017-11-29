import sqlite3 as lite
from sqlite3 import Error as LiteError


def create_connection(db_path):
    """ create a database connection to a SQLite database """
    db = None

    try:
        db = lite.connect(db_path)
        print(lite.version)
    except LiteError as e:
        print(e)
    finally:
        db.close()


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except LiteError as e:
        print(e)
