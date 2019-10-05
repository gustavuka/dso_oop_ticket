from abc import ABC, abstractmethod

class Cliente(ABC):

    @abstractmethod
    def __init__(self, nome: str, endereco: str, telefone: str, email: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email

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

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @endereco.setter
    def email(self, novo_email):
        self.__email = novo_email
