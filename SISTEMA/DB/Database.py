
import mysql.connector

class Database():
    def __init__(self, banco="syspython"):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='10.28.2.114',database=self.banco,user='devweb',password='suporte@22')

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com sucesso: ",db_info)
        else:
            print("ERROR")

    def insert_client(self,args):
        self.connect()
        try:            
            self.cursor.execute('INSERT INTO cliente (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',args)
            self.conn.commit()
            print("Cliente cadastrado com sucesso!!!")

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def insert_product(self,tupla):
        self.connect()
        try:
            # tupla = ["Thiago Almeida","555","meulogin","333","222","CG"]
            
            self.cursor.execute('INSERT INTO produto (nome,cpf,login,senha,fone,cidade) VALUES (%s,%s,%s,%s,%s,%s)',tupla)
            self.conn.commit()
            # print("Cliente cadastrado com sucesso!!!")
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM cliente")
            clientes = self.cursor.fetchall()
            return clientes
            # for cli in clientes:
            #     print(cli)

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id = {id}")
            cli = self.cursor.fetchone()
            return cli

        except Exception as err:
            print(err)

    def update_client(self,lista):
        self.connect()
        try:
            self.cursor.execute(f"""
                        UPDATE cliente 
                        SET nome = '{lista[1]}',
                        cpf = '{lista[2]}',
                        login = '{lista[3]}', 
                        senha = '{lista[4]}', 
                        fone = '{lista[5]}',
                        cidade = '{lista[6]}' 
                        WHERE id = {lista[0]} 
                        """)
            self.conn.commit()
            # cli_atualizado = self.select_client_by_id(cliente[0])
            # print(cli_atualizado)
            return True
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()    

    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id = {id}")
            self.conn.commit()
            # print("CLiente deletado com sucesso!!!")
            return True

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!!")


if __name__ == '__main__':
    db = Database()
    #db.insert_client()
    db.update_client(6)
    #db.delete_client(8)
    # db.close_connection()
    # db.select_client()