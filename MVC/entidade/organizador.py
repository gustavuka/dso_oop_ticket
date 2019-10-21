from entidade.cliente import Cliente


class Organizador(Cliente):
    def __init__(self, nome: str, endereco: str, telefone: str, email: str, cnpj: str):
        super().__init__(nome, endereco, telefone, email)
        self.__cnpj = cnpj
        self.__email = email
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @property
    def cnpj(self):
        return self.__cnpj
