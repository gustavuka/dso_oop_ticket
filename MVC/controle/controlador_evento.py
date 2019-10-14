from entidade.evento import Evento
from entidade.local import Local
from limite.tela_evento import TelaEvento
from datetime import datetime
from excecoes.evento_ja_cadastrado import EventoJaCadastrado
# from excecoes.evento_nao_encontrado import EventoNaoEncontrado
from excecoes.local_ja_cadastrado import LocalJaCadastrado
from inicia_for_tests import IniciaForTests


class ControladorEvento:

    def __init__(self):
        self.__eventos = []
        self.__locais = []
        self.__tela_evento = TelaEvento()
        #Cria alguns eventos de testes para executar as funcionalidades do programa
        IniciaForTests().eventos_teste(Evento, self.eventos)
        IniciaForTests().locais_teste(Local, self.locais)

    @property
    def eventos(self):
        return self.__eventos

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

    def cadastra_local(self):
        info_local = self.tela_evento.cadastrar_local()
        novo_local = Local(info_local['nome_local'], info_local['endereco_local'], info_local['capacidade_local'])
        for local in self.locais:
            if novo_local.nome == local.nome:
                raise LocalJaCadastrado
        self.locais.append(novo_local)

    def criar_evento(self, cnpj: str):
        dados_evento = self.tela_evento.cadastrar_evento(cnpj)
        local = self.tela_evento.selecionar_locais(self.locais)
        if local:
            novo_evento = Evento(
                dados_evento['cnpj_organizador'],
                dados_evento['titulo_evento'],
                dados_evento['categoria_evento'],
                dados_evento['data_evento'],
                local,
                dados_evento['classificacao_indicativa'],
                dados_evento['valor_ingresso'],
            )
            for evento in self.eventos:
                if evento.titulo == novo_evento.titulo:
                    raise EventoJaCadastrado()
            self.eventos.append(novo_evento)
            print ("Evento criado com sucesso")
            return novo_evento

    def mostrar_todos_eventos(self):
        self.tela_evento.print_eventos(self.eventos)

    #AINDA NAO ESTá SENDO USADO!
    # def altera_local_evento(self):
    #      evento_a_ser_alterado = self.tela_evento.ler_titulo_evento()
    #     for evento in self.eventos:
    #         if evento.titulo == evento_a_ser_alterado:
    #             evento.local = Local(novo_nome_local, novo_endereco_local, nova_capacidade_local)
    #         else:
    #             raise EventoNaoEncontrado()

    # def altera_categoria_evento(self, titulo_evento: str, nova_categoria: str):
    #     for evento in self.eventos:
    #         if evento.titulo == titulo_evento:
    #             evento.categoria = nova_categoria
    #         else:
    #             raise EventoNaoEncontrado()

    # def altera_titulo_evento(self, titulo_evento: str, novo_titulo: str):
    #     for evento in self.eventos:
    #         if evento.titulo == titulo_evento:
    #             evento.titulo = novo_titulo
    #         else:
    #             raise EventoNaoEncontrado()

    # def altera_valor_evento(self, titulo_evento: str, novo_valor: float):
    #     for evento in self.eventos:
    #         if evento.titulo == titulo_evento:
    #             evento.valor = novo_valor
    #         else:
    #             raise EventoNaoEncontrado

    # def altera_data_evento(self, titulo_evento: str, nova_data: str):
    #     for evento in self.eventos:
    #         if evento.titulo == titulo_evento:
    #             evento.data = nova_data
    #         else:
    #             raise EventoNaoEncontrado
