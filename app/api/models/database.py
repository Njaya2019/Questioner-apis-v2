import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2.extras as p_extras

class DataBase():
    """
        This class will create and connect to questioner_db
    """
    
    def __init__(self):
        """
            Connects to default postgress database.
             it creates a connection and a cursor object
         """
        self.con_nection=psycopg2.connect(
                    dbname='postgres',
                     user='postgres',
                      host='localhost',
                       password='a1990n'
                       )
        self.cursor=self.con_nection.cursor()

 
    def create_database(self):
        """
            This instance method creates a database called questioner db.
            It uses the cursor object to execute the select and create 
            queries.
        """
        try:

            self.cursor.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'questioner_db'")
            not_exists_row = self.cursor.fetchone()
            not_exists = not_exists_row[0]
            if not_exists:
                self.con_nection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                self.cursor.execute('CREATE DATABASE questioner_db')
                return 'database created'
            else:
                return 'database exists'
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.con_nection is not None:
                self.con_nection.close()

    def connect_to_store_db(self):
        """
            This instance method connects to new questioner database created.
            It creates a connection and cursor object.
        """
        con=psycopg2.connect(
                dbname='questioner_db',
                user='postgres',
                host='localhost',
                password='a1990n'
                )
        cur=con.cursor(cursor_factory=p_extras.DictCursor)
        return cur, con
    