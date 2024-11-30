import mysql.connector

class conndb:
    def _init_(self):
        pass

    def queryResult(self,strsql):
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='praktikan')
        conn = cnx.cursor()
        conn.execute(strsql)
        result = conn.fetchall()
        return result
        pass

    def queryExecute(self, strsql):
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='praktikan') 
        conn = cnx.cursor()
        conn.execute(strsql)
        cnx.commit()
        pass