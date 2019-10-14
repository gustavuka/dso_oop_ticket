
class Local:

    def __init__(self, nome: str, endereco: str, capacidade: int):
        self.__nome = nome
        self.__endereco = endereco
        self.__capacidade = capacidade
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def capacidade(self):
        return self.__capacidade
