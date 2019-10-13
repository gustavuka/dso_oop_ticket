from entidade.local import Local
from datetime import datetime

class Evento:

    def __init__(self, titulo: str,
                 categoria: str,
                 data: str,
                 nome_local: str,
                 endereco_local: str,
                 capacidade_local: str,
                 classificacao_indicativa: int,
                 valor_ingresso: float):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__data = data
        self.__local = Local(nome_local, endereco_local, capacidade_local)
        self.__classificacao_indicativa = classificacao_indicativa
        self.__valor_ingresso = valor_ingresso
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nova_categoria: str):
        self.__categoria = nova_categoria
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data):
        self.__data = nova_data
    
    @property
    def local(self):
        return self.__local
    
    @local.setter
    def local(self, novo_local: Local):
        self.__local = novo_local
    
    @property
    def classificacao_indicativa(self):
        return self.__classificacao_indicativa

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor: float):
        self.__valor = novo_valor
