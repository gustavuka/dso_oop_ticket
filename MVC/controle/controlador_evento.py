from MVC.entidade.evento import Evento
from MVC.entidade.local import Local
from datetime import datetime
from MVC.excecoes.evento_ja_cadastrado import EventoJaCadastrado
from MVC.excecoes.evento_nao_encontrado import EventoNaoEncontrado
from MVC.excecoes.local_ja_cadastrado import LocalJaCadastrado


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
    
    def busca_evento(self, titulo_evento: str):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                return True
        return False
    
    def cadastra_local(self, nome_local: str, endereco_local: str, capacidade_local: int):
        novo_local = Local(nome_local, endereco_local, capacidade_local)
        for local in self.locais:
            if novo_local.nome == local.nome:
                raise LocalJaCadastrado
        self.locais.append(novo_local)

    def cadastra_evento(self, titulo_evento: str,
                                         categoria_evento: str,
                                         data_evento: str,
                                         nome_local: str,
                                         endereco_local: str,
                                         capacidade_local: int,
                                         classificacao_indicativa: int,
                                         valor_ingresso: float):
        novo_evento = Evento(titulo_evento,
                        categoria_evento,
                        data_evento,
                        Local(nome_local, endereco_local, capacidade_local),
                        classificacao_indicativa,
                        valor_ingresso)
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                raise EventoJaCadastrado()
        self.eventos.append(novo_evento)

    def altera_local_evento(self, titulo_evento: str,
                            novo_nome_local: str,
                            novo_endereco_local: str,
                            nova_capacidade_local: int):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                evento.local = Local(novo_nome_local, novo_endereco_local, nova_capacidade_local)
            else:
                raise EventoNaoEncontrado()

    def altera_categoria_evento(self, titulo_evento: str, nova_categoria: str):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                evento.categoria = nova_categoria
            else:
                raise EventoNaoEncontrado()

    def altera_titulo_evento(self, titulo_evento: str, novo_titulo: str):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                evento.titulo = novo_titulo
            else:
                raise EventoNaoEncontrado()

    def altera_valor_evento(self, titulo_evento: str, novo_valor: float):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                evento.valor = novo_valor
            else:
                raise EventoNaoEncontrado

    def altera_data_evento(self, titulo_evento: str, nova_data: str):
        for evento in self.eventos:
            if evento.titulo == titulo_evento:
                evento.data = nova_data
            else:
                raise EventoNaoEncontrado
