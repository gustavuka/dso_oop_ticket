from entidade.organizador import Organizador
from limite.tela_organizador import TelaOrganizador
from controle.controlador_evento import ControladorEvento
from inicia_for_tests import IniciaForTests


class ControladorOrganizador:
    def __init__(self, controlador_evento: ControladorEvento):
        self.__tela_organizador = TelaOrganizador()
        self.__controlador_evento = controlador_evento
        self.__lista_organizadores = []
        self.__lista_eventos_organizados = []
        # Cria alguns organizadores de testes para executar as funcionalidades do programa
        IniciaForTests().organizador_teste(Organizador, self.lista_organizadores)

    @property
    def lista_organizadores(self):
        return self.__lista_organizadores

    @property
    def tela_organizador(self):
        return self.__tela_organizador

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    @property
    def lista_eventos_organizados(self):
        return self.__lista_eventos_organizados

    @lista_organizadores.setter
    def lista_organizadores(self, lista_organizadores):
        self.__lista_organizadores = lista_organizadores

    def confere_cnpj_existe(self, cnpj):
        for organizador in self.lista_organizadores:
            if organizador.cnpj == cnpj:
                return organizador
        return False

    def adicionar_organizador(self, dados):

        # novo_organizador = Organizador(
        #     info_organizador["Nome"],
        #     info_organizador["Endereco"],
        #     info_organizador["Telefone"],
        #     info_organizador["Email"],
        #     info_organizador["cnpj"],
        # )

        novo_organizador = Organizador(dados[0], dados[4], dados[1], dados[3], dados[2])
        self.lista_organizadores.append(novo_organizador)
        self.tela_organizador.imprime_mensagem(
            ("Novo organizador cadastrado! Bem vindo " + novo_organizador.nome + "!")
        )
        return novo_organizador.cnpj

    def alterar_dados(self, cnpj, dados):
        usuario = self.confere_cnpj_existe(cnpj)

        if usuario:
            usuario.nome = dados[0]
            usuario.endereco = dados[4]
            usuario.telefone = dados[1]
            usuario.email = dados[3]
            usuario.cnpj = cnpj
            print("Atualizacao de dados completa!")
            print(usuario.nome)
        else:
            print("Error")
        return usuario

    def mostrar_organizadores_cadastrados(self):
        self.tela_organizador.lista_organizadores_cadastrados(self.lista_organizadores)

    # não consegui adicionar aos eventos gerais, só na lista do organizador
    def cadastrar_evento(self):
        cnpj = self.tela_organizador.pede_cnpj()
        usuario = self.confere_cnpj_existe(cnpj)
        if usuario:
            novo_evento = self.controlador_evento.criar_evento(cnpj)
            self.lista_eventos_organizados.append(novo_evento)
        else:
            print("cnpj nao cadastrado")
            self.cadastrar_evento()

    # está funcionando, se quiser testar mais vezes, mas está buscando o evento por cnpj
    def mostra_eventos_organizados(self, cnpj):
        organizador_existe = self.confere_cnpj_existe(cnpj)
        lista = ["Lista de eventos organizados: "]
        if organizador_existe:
            for evento in self.controlador_evento.eventos:
                if evento.cnpj_organizador == cnpj:
                    lista.append(["Evento: " + evento.titulo])
        self.tela_organizador.imprime_mensagem(lista)

        return lista

    def mostra_relatorio_compras(self):
        pass

    # tentei fazer tudo mas faltou a parte do local
    def mostra_informacoes_evento(self):
        cnpj = self.tela_organizador.pede_cnpj()
        organizador_existe = self.confere_cnpj_existe(cnpj)
        informacoes_evento = "Informações do evento: "
        if organizador_existe:
            titulo = self.tela_organizador.mostrar_informacoes_evento()
            for evento in self.controlador_evento.eventos:
                if evento.titulo == titulo:
                    informacoes_evento += (
                        "Titulo do evento: "
                        + evento.titulo
                        + "\nCategoria do evento: "
                        + evento.categoria
                        + "\nData do evento: "
                        + evento.data
                        + "\nLocal do evento: "
                        + evento.local
                        + "\nClassificacao indicativa: "
                        + evento.classificacao_indicativa
                        + "\nValor: R$"
                        + evento.valor
                    )
                if evento.titulo.upper() == titulo:
                    informacoes_evento += (
                        "Titulo do evento: {}\n"
                        "Categoria do evento: {}\n"
                        "Data do evento: {}\n"
                        "Local do evento: {}\n"
                        "Classificacao indicativa: {}\n"
                        "Valor: R${}".format(
                            evento.titulo,
                            evento.categoria,
                            evento.data,
                            evento.local,
                            evento.classificacao_indicativa,
                            evento.valor,
                        )
                    )
                    self.tela_organizador.imprime_mensagem(informacoes_evento)
                    return True
            self.tela_organizador.imprime_mensagem("Evento não encontrado!")
            self.mostra_informacoes_evento()
