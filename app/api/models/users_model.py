from models.database import DataBase
import psycopg2

d_b = DataBase()
cur_con = d_b.connect_to_store_db()


class usersmodel():

    cur = cur_con[0]
    con = cur_con[1]

    def __init__(self, first_name, last_name, email, username, 
                 isAdmin, phonenumber, password, confirm_pwd):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.isAdmin = isAdmin
        self.phonenumber = phonenumber
        self.password = password
        self.confirm_pwd = confirm_pwd

    def register_user(self):
   
        insert_user_sql = """ INSERT INTO
                users(firstname,lastname,isAdmin,email,phonenumber,username,passwd)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
                RETURNING
                firstname,lastname,isAdmin,email,phonenumber,username
            """
        user_data = (
            self.first_name, self.last_name, 
            self.email, self.username, 
            self.isAdmin, self.phonenumber, 
            self.password, self.confirm_pwd)
        self.cur.execute(insert_user_sql, user_data)
        user = self.cur.fetchone()
        self.con.commit()
        return user
