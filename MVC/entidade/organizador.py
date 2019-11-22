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

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_endereco):
        self.__telefone = novo_endereco

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj
