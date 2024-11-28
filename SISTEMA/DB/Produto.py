import mysql.connector

class Database():
    def __init__(self, banco="thiaguerastor"):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(
        host='10.28.2.114',
        database=self.banco,
        user='devweb',
        password='suporte@22'
        )

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com suceso!")
        else:
            print("Erro!!")

    def insert_produto(self):
        self.connect()
        try:
            # nome = "Eliandro"
            # cpf = "90909090"
            # login = "eliandro@senha"
            # senha = "senhaElia"
            # fone = "67992997470"
            # cidade = "Campo Grande"

            args = ("Tabua de marmore","766","me12logghsdin","55","2024-26-11","Feito em madeira")

            # self.cursor.execute(f'INSERT INTO cliente (nome,cpf,login,senha,fone,cidade) VALUES ("{nome}","{cpf}","{login}","{senha}","{fone}","{cidade}");')
            self.cursor.execute('INSERT INTO produto (nome,codigo,marca,quantidade,data_entrada,descricao) VALUES (%s,%s,%s,%s,%s,%s)',args)
            self.conn.commit()
            print("Produto cadastrado com sucesso!!!")

        except Exception as err:
            print(err)

    def select_produto(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            produtos = self.cursor.fetchall()
            for cli in produtos:
                print(produtos)

        except Exception as err:
            print(err)

    def select_produto_by_id(self,id):
        self.connect()
        # id = 1
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id = {id}")
            cli = self.cursor.fetchone()
            # for cli in clientes:
            # print(cli[0],cli[1],cli[2],cli[2])
            return cli

        except Exception as err:
            print(err)

    def update_produto(self,id):
        self.connect()
        try:
            produto = list(self.select_produto_by_id(id))
            print(produto)
            # print(cliente)
            # nome = cliente[1]
            # cpf = cliente[2]
            # login = cliente[3]
            # senha = cliente[4]
            # fone = cliente[5]
            # cidade = cliente[6]

            # nome2 = input("Digite o NOME: ")
            # cpf2 = input("Digite o CPF: ")
            # login2 = input("Digite o LOGIN: ")
            # senha2 = input("Digite o SENHA: ")
            # fone2 = input("Digite o FONE: ")
            # cidade2 = input("Digite o CIDADE: ")
            # print(cpf)
          
            produto[1] = input("Digite o novo NOME DO PRODUTO: ")
            produto[2] = input("Digite o novo CÓDIGO DO PRODUTO: ")
            produto[3] = input("Digite a nova MARCA DO PRODUTO: ")
            produto[4] = input("Digite a nova QUNATIDADE DO PRODUTO: ")
            produto[5] = input("Digite a nova DATA DE ENTRADA DO PRODUTO: ")
            produto[6] = input("Digite a nova DESCRIÇÃO DO PRODUTO: ")

            self.cursor.execute(f"""
                                UPDATE produto 
                                SET nome = '{produto[1]}',
                                codigo = '{produto[2]}',
                                marca = '{produto[3]}',
                                quantidade = '{produto[4]}',
                                data_entrada = '{produto[5]}',
                                descricao = '{produto[6]}' 
                                WHERE id = {produto[0]}
                                """)
            self.conn.commit()
            cli_atualizado = self.select_produto_by_id(produto[0])
            print("Produto Atualizado com sucesso!!! ")
            print(cli_atualizado)


        except Exception as erro:
            print(erro)

    
    def delete_produto(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id = {id}")
            self.conn.commit()
            print("Produto deletado com sucesso!!!!")

        except Exception as erro:
            print(erro)

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexõs encerrada com sucesso!!!")

d1 = Database()
d1.connect()

if __name__ == '__main__':
    db = Database()
    # db.connect()
    # db.insert_produto()
    # db.select_produto()
    db.select_produto_by_id(1)
    db.close_connection()
    # db.delete_produto(2)
    db.update_produto(13)
    db.close_connection()