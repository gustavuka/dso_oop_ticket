from entidade.cliente import Cliente


class Comprador(Cliente):

    def __init__(self, nome: str, endereco: str, telefone: str, email: str, cpf: str, idade: int):
        super().__init__(nome, endereco, telefone, email)
        self.__cpf = cpf
        self.__idade = idade
        self.__lista_ingressos = []
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def lista_ingressos(self):
        return self.__lista_ingressos

    @property
    def idade(self):
        return self.__idade

    @property
    def email(self):
        return self.__email

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @lista_ingressos.setter
    def lista_ingressos(self, nova_lista_ingressos):
        self.__lista_ingressos = nova_lista_ingressos