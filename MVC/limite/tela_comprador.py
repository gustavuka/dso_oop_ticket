from comprador import Comprador

class TelaComprador:

    def novo_comprador(self):
        nome = input("Nome: ")
        endereco = input("Endereco: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cpf = input("cpf: ")
        idade = input("Idade: ")

        oo = Comprador(nome, endereco, telefone, email, cpf, idade)
        print (oo, oo.nome)
