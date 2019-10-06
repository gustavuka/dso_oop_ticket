from Local import *


class Evento:

    def __init__(self, titulo: str, categoria: str, data: Date, local: Local, classificacao_indicativa: int, valor_ingresso: float):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__data = data
        self.__local = local
        self.__classificacao_indicativa = classificacao_indicativa
        self.__valor_ingresso = valor_ingresso
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def categoria(self):
        self.__categoria = categoria
    
    @property
    def data(self):
        self.__data = data
    
    @data.setter
    def data(self, nova_data):
        self.__data = nova_data
    
    @property
    def local(self):
        return self.__local
    
    @local.setter
    def local(self, novo_local):
        self.__local = novo_local
    
    @property
    def classificacao_indicativa(self):
        return self.__classificacao_indicativa

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor
