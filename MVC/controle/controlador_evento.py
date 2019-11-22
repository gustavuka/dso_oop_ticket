from entidade.evento import Evento
from entidade.local import Local
from limite.tela_evento import TelaEvento
from excecoes.evento_ja_cadastrado import EventoJaCadastrado
from entidade.evento_dao import EventoDAO

from excecoes.local_ja_cadastrado import LocalJaCadastrado


class ControladorEvento:
    def __init__(self):
        self.__eventos = []
        self.__locais = []
        self.__tela_evento = TelaEvento()
        self.__evento_dao = EventoDAO()

    @property
    def eventos(self):
        return self.__evento_dao.get_all()

    @property
    def tela_evento(self):
        return self.__tela_evento

    @property
    def locais(self):
        return self.__locais

    def busca_evento(self, titulo_evento: str):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                return True
        return False

    def cadastra_local(self, dados):
        novo_local = Local(dados[0], dados[1], dados[2])
        for local in self.locais:
            if novo_local.nome == local.nome.upper():
                raise LocalJaCadastrado
        self.locais.append(novo_local)
        print("Novo local cadastrado")
        return novo_local

    def criar_evento(self, cnpj: str, dados):
        # LOCAL PRECISA SER UM OBJ
        # local = self.tela_evento.selecionar_locais(self.locais)
        novo_evento = Evento(
            cnpj, dados[0], dados[1], dados[2], dados[3], dados[5], dados[4]
        )
        print (self.eventos)
        for evento in self.eventos:
            if evento.titulo.upper() == novo_evento.titulo:
                raise EventoJaCadastrado()
        self.__evento_dao.add(novo_evento)
        print("Evento criado com sucesso")
        return self.__evento_dao.get(novo_evento.titulo)

    def mostrar_todos_eventos(self):
        self.tela_evento.mostrar_eventos(self.eventos)
