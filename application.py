from app.api.models.database import DataBase

db=DataBase()    #Creates an object of class Database called db

if __name__=='__main__':
    db.create_database()
    db.create_db_tables()
