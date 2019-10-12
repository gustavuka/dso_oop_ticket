from entidade.cliente import Cliente

class Organizador(Cliente):

    def __init__(self, nome: str, endereco: str, telefone: str, email: str, cnpj: str):
        super().__init__(nome, endereco, telefone, email)
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj
