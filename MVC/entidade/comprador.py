from cliente import Cliente


def Comprador(Cliente):

    def __init__(self, nome: str, cpf: str, idade: int, endereco: str, telefone: str, email: str):
        super().__init__(nome, endereco, telefone, email)
        self.__cpf = cpf
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade
