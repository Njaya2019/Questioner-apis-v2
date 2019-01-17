import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2.extras as p_extras


class DataBase():


    def __init__(self):
        self.con_nection = psycopg2.connect(
                    dbname='postgres',
                    user='postgres',
                    host='localhost',
                    password=' '
                    )
        self.cursor = self.con_nection.cursor()

    def create_database(self):
        """
            This instance method creates a database called questioner db.
            It uses the cursor object to execute the select and create queries.
        """
        try:
            self.cursor.execute(
                """SELECT COUNT(*)=0 FROM pg_catalog.pg_database WHERE datname='questioner_db'
                """
                )
            not_exists_row = self.cursor.fetchone()
            not_exists = not_exists_row[0]
            if not_exists:
                self.con_nection.set_isolation_level(
                    ISOLATION_LEVEL_AUTOCOMMIT
                    )
                self.cursor.execute('CREATE DATABASE questioner_db')
                return 'database created'
            else:
                return 'database exists'
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.con_nection is not None:
                self.con_nection.close()

    def connect_questioner_db(self):
        """
            This instance method connects to new questioner database created.
            It creates a connection and cursor object.
        """
        con = psycopg2.connect(
                dbname='questioner_db',
                user='postgres',
                host='localhost',
                password=' '
                )
        cur = con.cursor(cursor_factory=p_extras.DictCursor)
        return cur, con

    def create_db_tables(self):
        """
            This instance method creates table users in questioner_db.
        """
        tables = (
            """CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                firstname VARCHAR(50) NOT NULL,
                lastname VARCHAR(50) NOT NULL,
                isAdmin BOOLEAN NOT NULL,
                email VARCHAR(50) NOT NULL,
                phonenumber VARCHAR(10) NOT NULL,
                username VARCHAR(50) NOT NULL,
                passwd TEXT NOT NULL)
            """,
                )
        try:
            con_values = self.connect_questioner_db()
            cur = con_values[0]
            con = con_values[1]
            """
                This creates tables one after the other and
                then commits the changes.
            """
            for table in tables:
                cur.execute(table)
                print('TABLE CREATED')
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
