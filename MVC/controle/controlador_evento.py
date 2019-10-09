from MVC.entidade.local import Local
from MVC.entidade.evento import Evento
from datetime import datetime


class ControladorEvento:

    def __init__(self):
        self.__eventos = []
        self.__locais = []

    @property
    def eventos(self):
        return self.__eventos
    
    @property
    def locais(self):
        return self.__locais

    def cadastrar_local(self, local: Local):
        if local not in self.locais:
            self.__locais.append(local)

    def cadastrar_evento(self, evento: Evento):
        if evento not in self.eventos and isinstance(evento, Evento):
            self.eventos.append(evento)

    def alterar_local_evento(self, evento: Evento, novo_local: Local):
        if evento in self.eventos:
            evento.local = novo_local

    def altera_categoria_evento(self, evento: Evento, nova_categoria: str):
        if evento in self.eventos:
            evento.categoria = nova_categoria

    def altera_titulo_evento(self, evento: Evento, novo_titulo: str):
        if evento in self.eventos:
            evento.titulo = novo_titulo

    def altera_valor_evento(self, evento: Evento, novo_valor: float):
        if evento in self.eventos:
            evento.valor = novo_valor

    def altera_data_evento(self, evento: Evento, nova_data: datetime):
        if evento in self.eventos:
            evento.data = nova_data
