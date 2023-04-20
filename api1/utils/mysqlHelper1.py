import mysql.connector

class mysqlHelper1:
    query = None

    def __init__(self, query):
        self.query = query
    
    def exec(self):
        # print("Will exec sql query")
        cnx = mysql.connector.connect(
            host="box1",
            user='dbroot1', 
            password="P@ssw0rd@",
            database='fbdb_dev')
        cursor = cnx.cursor()
        cursor.execute(self.query)
        resultList = cursor.fetchall()

        cursor.close()
        cnx.close()

        return resultList




           

        

