

import firebase_admin
from firebase_admin import credentials
from datetime import datetime


cred = credentials.Certificate("iotproject-b5a07-firebase-adminsdk-z44v7-6fbffc7dd6.json")
firebase_admin.initialize_app(cred)




# class Database:

    # subscribers = 'subscribers'
    # devices135 = "devices135"

    # def __init__(self,name="mydb.sqlite3"):
    #     self.con = sqlite3.connect(name)
    #     self.con.row_factory=sqlite3.Row
    #     # print('connected')
    # def close(self):
    #     self.con.close()

    # def run(self,querry):  #function to execute the querry
    #     try:
    #         self.con.execute(querry)
    #         self.con.commit() #saves the changes
            
    #         return True
    #     except Exception as e:
    #         print('error')
    #         print(e)
    #         return False
        

    # def create_table(self): # Capital letter in querry is to follow the convention and its not mandatory
    #     query = f""" 
    #         CREATE TABLE {self.subscribers} (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name VARCHAR(50),
    #         email VARCHAR(50),
    #         created VARCHAR(50)
    #         )
    #     """
    #     status = self.run(query)
    #     # execute as many as table queries
    #     query=f"""
    #     CREATE TABLE {self.devices135} (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         value DOUBLE,
    #         time TEXT
    #     )
    #     """
    #     status1 = self.run(query)
    #     return status,status1

    # def addsensor135_data(self,value):
    #     query=f"""INSERT INTO {self.devices135} VALUES(null, {value}, '{datetime.now()}')"""
    #     return self.run(query)
    


    # def addSubscriber(self,name,email,created):
    #     query = f"""
    #         INSERT INTO {self.subscribers} VALUES(
    #             null,'{name}', '{email}', '{created}'
    #         )
    #     """
    #     return self.run(query)

    # def deleteSubscriber(self,id):
    #     query = f""" 
    #         DELETE FROM {self.subscribers} WHERE id = {id}
    #     """
    #     return self.run(query)

    
    # def viewSubscriber(self):
    #     query = f"SELECT * FROM {self.subscribers}"
    #     try:
    #         result = self.con.execute(query)
    #         data = result.fetchall()
    #         print(data.__dir__())
    #         return data
    #     except Exception as e:
    #         print('error')
    #         print(e)

    # def viewDevice135Data(self):
    #     query = f"SELECT * FROM {self.devices135} ORDER BY time LIMIT 10"
    #     try:
    #         result = self.con.execute(query)
    #         data=[dict(row) for row in result.fetchall()]
    #         return data
    #     except Exception as e:
    #         print('error')
    #         print(e)

