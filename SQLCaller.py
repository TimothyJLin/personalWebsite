import mysql.connector
import os
def connect():
    mydb = mysql.connector.connect(
        host=os.environ["DATABASE_HOST"],
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        database=os.environ["DATABASE_NAME"],
        port=26362,
        #sensitive data here to be on a hidden file
  )
def attemptLogIn(username, password):
    pass
    

def storeCreatedAccount(username, password):
    pass