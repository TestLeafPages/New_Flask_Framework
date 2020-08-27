import sqlite3


class DataBaseFile:

    def __init__(self, filename):
        self.filename = filename

    def get_connection(self):
        con = sqlite3.connect(self.filename)
        print("DataBase Opened")
        return con


    def create_table(self, con, table_name):
        con.execute('''CREATE TABLE IF NOT EXISTS ''' +table_name+'''(FNAME, LNAME, EMAIL, PWD)''')
        print('Table Created')

    def insert_record(self, con, obj, table_name):
        data = "INSERT INTO "+table_name+"(FNAME, LNAME, EMAIL, PWD) VALUES (?, ?, ?, ?)"
        con.execute(data, (obj.fname, obj.lname, obj.email, obj.pwd))
        con.commit()
        print("Record inserted")

    def close_connection(self, con):
        con.close()
