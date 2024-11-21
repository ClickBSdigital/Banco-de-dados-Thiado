import mysql.connector

class Database():
    def __init__(self, banco="syspython"):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco,user='root',password='')

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com suceso!")
        else:
            print("Erro!!")