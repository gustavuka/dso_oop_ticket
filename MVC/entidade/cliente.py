from abc import ABC, abstractmethod

class Cliente(ABC):

    @abstractmethod
    def __init__(self, nome: str, endereco: str, telefone: str, email: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email

    @abstractmethod
    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    @property
    def endereco(self):
        return self.__endereco
    
    @abstractmethod
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
    
    @abstractmethod
    @property
    def telefone(self):
        return self.__telefone
    
    @abstractmethod
    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
    @abstractmethod
    @property
    def endereco(self):
        return self.__endereco
    
    @abstractmethod
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
