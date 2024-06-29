# Importing the libraries
import mysql.connector
from . import mysql_credensials



class SQL():
    def __init__(self):
        # Connecting to the database
        self.mydb=mysql.connector.connect(username=mysql_credensials["username"],database=mysql_credensials["database"],host=mysql_credensials["host"])
        self.cursor=self.mydb.cursor()
    
    def create_table(self,columns:list):
        string=""
        for col in columns:
            string += f"{col} TEXT, "
        string=string.rstrip(", ")
        query=f"CREATE TABLE IF NOT EXISTS sensortopic ({string})" 
        self.cursor.execute(query)
    def add_record(self,data:list):
        self.cursor.execute(f"INSERT INTO sensortopic VALUES {tuple(data.values())}")
    def add_many(self,data:list):
        entries=str(data)[1:-1]
        self.cursor.execute(f"INSERT INTO sensortopic VALUES "+entries)
    def close(self):
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()





