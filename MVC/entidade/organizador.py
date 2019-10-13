from entidade.cliente import Cliente

class Organizador(Cliente):

    def __init__(self, nome: str, endereco: str, telefone: str, email: str, cnpj: str):
        super().__init__(nome, endereco, telefone, email)
        self.__cnpj = cnpj
        self.__lista_eventos = []

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def lista_eventos(self):
        return self.__lista_eventos

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj

    @lista_eventos.setter
    def lista_eventos(self, novo_evento):
        self.__lista_eventos = lista_eventos
