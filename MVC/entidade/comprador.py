from cliente import Cliente


def Comprador(Cliente):

    def __init__(self, nome: str, cpf: str, idade: int, endereco: str, telefone: str, email: str):
        super().__init__(nome, cpf, idade, endereco, telefone, email)
        self.__cpf = cpf
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

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
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
