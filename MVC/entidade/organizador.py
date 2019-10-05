from cliente import Cliente

class Organizador(Cliente):

    def __init__(self, nome: str, cnpj: str, idade: int, endereco: str, telefone: str, email: str):
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj
