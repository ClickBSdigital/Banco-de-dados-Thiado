nome = "Eliandro"
cpf = "90909090"
login = "eliandro@senha"
senha = "senhaElia"
fone = "67992997470"
cidade = "Campo Grande"

self.cursor.execute(
    f'INSERT INTO cliente (nome,cpf,login,senha,fone,cidade)
    VALUES ("{nome}","{cpf}","{login}","{senha}","{fone}","{cidade}",)'
    )