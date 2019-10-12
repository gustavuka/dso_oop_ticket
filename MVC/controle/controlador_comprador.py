from entidade.comprador import Comprador
from limite.tela_comprador import TelaComprador


class ControladorComprador:
    def __init__(self):
        self.__lista_compradores = []

    @property
    def lista_compradores(self):
        return self.__lista_compradores

    @lista_compradores.setter
    def lista_compradores(self, lista_compradores):
        self.__lista_compradores = lista_compradores    

    def adicionar_comprador(self):
        info_comprador = (TelaComprador().novo_comprador())

        novo_comprador = Comprador(
            info_comprador["Nome"],
            info_comprador["Endereco"],
            info_comprador["Telefone"],
            info_comprador["Email"],
            info_comprador["cpf"],
            info_comprador["Idade"],
        )
        self.lista_compradores.append(novo_comprador)
        print ("Novo comprador cadastrado! Bem vindo " + novo_comprador.nome + "!")
        print (self.lista_compradores)

    def alterar_dados(self):
        cpf, nova_info_comprador = (TelaComprador().alterar_dados())
        
        for item in self.lista_compradores:
            if item.cpf == cpf:
                item.nome = nova_info_comprador["Nome"]
                item.endereco = nova_info_comprador["Endereco"]
                item.telefone = nova_info_comprador["Telefone"]
                item.email = nova_info_comprador["Email"]
                item.cpf = nova_info_comprador["cpf"]
                item.idade = nova_info_comprador["Idade"]
                print ("Atualizacao de dados completa!")
                print (item.nome, item.idade)
                print (self.lista_compradores)
        