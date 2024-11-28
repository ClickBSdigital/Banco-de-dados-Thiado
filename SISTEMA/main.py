# # from DB.Database import Database certoooooo
# # from Entity.cliente import Cliente

# # from matplotlib.pyplot import plot_date

# # # from pandas import 

# # import pandas as pd # apilido do pandas

# # import matplotlib.pyplot as plt # apelido

# # dados = plt.show

# banco = Database()

# dados = banco.select_client()

# # print(type(dados))

# # print(dados)
# print("Clientes Cadastrados: ")
# for item in dados:
#     print(item)

# print("\n SELECIONE UM CLIENTE PARA EDITAR! ")
# id_selecao = int(input("DIGITE O ID: "))

# cli_selecionado = list(banco.select_client_by_id(id_selecao))
# # print(type(cli_selecionado))

# # cli_selecionado = list(self.select_client_by_id(id))
# # print(cli_selecionado)
# cli_selecionado[1] = input("Digite o novo NOME: ")
# cli_selecionado[2] = input("Digite o novo CPF: ")
# cli_selecionado[3] = input("Digite o novo LOGIN: ")
# cli_selecionado[4] = input("Digite o novo SENHA: ")
# cli_selecionado[5] = input("Digite o novo FONE: ")
# cli_selecionado[6] = input("Digite o novo CIDADE: ")

# atualiza = banco.update_client(cli_selecionado)
# if atualiza:
#     print("\n CLIENTE ATUALIZADO COM SUCESSO!!!!")



#     +++++++++++++++++++++++++++++++++++++++++++

# from Entity.cliente import Cliente

# cli1 = Cliente()

# clientes = cli1.selecionar()
# for cliente in clientes:
#     print(cliente)


# print("\n DESEJA DELETAR ALGUEM???")
# id_deletar = int(input("\n DIGITE O ID DO CABOCLO:  "))
# cli_deletado = cli1.deletar(id_deletar)

# # print("\n CADASTRAR UM CLIENTE?")
# # cli1.nome = input("Digite o novo NOME: ")
# # cli1.cpf = input("Digite o novo CPF: ")
# # cli1.login = input("Digite o novo LOGIN: ")
# # cli1.senha = input("Digite o novo SENHA: ")
# # cli1.fone = input("Digite o novo FONE: ")
# # cli1.cidade = input("Digite o novo CIDADE: ")

# # cadastro = cli1.cadastrar()
# if cli_deletado == True:
#     print("\n NO FRONT, CLIENTE Deletado COM SUCESSO!!!")
#     clientes = cli1.selecionar()
#     for cliente in clientes:
#         print(cliente)
# else:
#     print("ERRRO AO DELETAR!!!")




#     =======================================================


from Entity.cliente import Cliente

cli1 = Cliente()

clientes = cli1.selecionar()
for cliente in clientes:
    print(cliente)


print("\n SELECIONE UM CLIENTE PARA ALTERAR ???")
id_selecao = int(input("\n DIGITE O ID DO CABOCLO:  "))

cli_selecionado = list(cli1.selecionar_por_id(id_selecao))

# print(cli_selecionado)

# # cli_selecionado = list(self.select_client_by_id(id))
# # print(cli_selecionado)
cli_selecionado[1] = input("Digite o novo NOME: ")
cli_selecionado[2] = input("Digite o novo CPF: ")
cli_selecionado[3] = input("Digite o novo LOGIN: ")
cli_selecionado[4] = input("Digite o novo SENHA: ")
cli_selecionado[5] = input("Digite o novo FONE: ")
cli_selecionado[6] = input("Digite o novo CIDADE: ")

atualiza = cli1.atualizar(cli_selecionado)
if atualiza:
    print("CLIENTE ATUALIZADO COM SECESSO!!!!!")

# cadastro = cli1.cadastrar()
# if cli_deletado == True:
#     print("\n NO FRONT, CLIENTE Deletado COM SUCESSO!!!")
#     clientes = cli1.selecionar()
#     for cliente in clientes:
#         print(cliente)
# else:
#     print("ERRRO AO DELETAR!!!")