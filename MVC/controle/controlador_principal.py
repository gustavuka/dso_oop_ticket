from limite.tela_controlador_principal import TelaControladorPrincipal
from controle.controlador_comprador import ControladorComprador
from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_evento import ControladorEvento
from controle.controlador_administrador import ControladorAdministrador
from limite.tela_administrador import TelaAdministrador
from limite.tela_cadastro_comprador import TelaCadastroComprador
from limite.tela_comprador import TelaComprador
from limite.tela_comprador_cadastrado import TelaCompradorCadastrado
from limite.tela_menu_principal import MenuPrincipal
from limite.tela_pede_cpf import TelaPedeCPF

from limite.tela_organizador_gui import (
    TelaInicial,
    TelaInicialOganizador,
    TelaLogin,
    TelaCadastroOrganizador,
    TelaLista,
    TelaCadastroEvento,
    TelaCadastroLocal,
    TelaPopUp,
)
from limite.tela_administrador_gui import TelaAdministrador
from limite.tela_comprador_gui import TelaCadastroComprador, TelaInicialComprador


class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaControladorPrincipal()
        self.__tela_administrador = TelaAdministrador
        self.__controlador_evento = ControladorEvento()
        self.__controlador_comprador = ControladorComprador(self.controlador_evento)
        self.__controlador_organizador = ControladorOrganizador(self.controlador_evento)
        self.__controlador_administrador = ControladorAdministrador(
            self.controlador_organizador, self.controlador_comprador
        )
        self.__tela_menu_principal = MenuPrincipal()
        self.__tela_comprador = TelaComprador()
        self.__tela_comprador_cadastrado = TelaCompradorCadastrado()
        self.__tela_pede_cpf = TelaPedeCPF()
        self.__tela_cadastro_comprador = TelaCadastroComprador()

    @property
    def tela_principal(self):
        return self.__tela_principal

    @property
    def tela_administrador(self):
        return self.__tela_administrador

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    @property
    def controlador_comprador(self):
        return self.__controlador_comprador

    @property
    def controlador_organizador(self):
        return self.__controlador_organizador

    @property
    def controlador_administrador(self):
        return self.__controlador_administrador

    @property
    def tela_menu_principal(self):
        return self.__tela_menu_principal

    @property
    def tela_comprador(self):
        return self.__tela_comprador

    @property
    def tela_comprador_cadastrado(self):
        return self.__tela_comprador_cadastrado

    @property
    def tela_cadastro_comprador(self):
        return self.__tela_cadastro_comprador

    @property
    def tela_pede_cpf(self):
        return self.__tela_pede_cpf

    def inicia(self):
        opcao_ini = TelaInicial().screen()
        if opcao_ini == 1:
            while True:
                self.abrir_tela_comprador()
        elif opcao_ini == 2:
            while True:
                self.abrir_tela_organizador()
        elif opcao_ini == 3:
            while True:
                self.abrir_tela_administrador()
        elif opcao_ini == 4:
            print("Saindo...")
            exit()

    def abrir_tela_comprador(self):
        while True:
            cpf = TelaLogin().screen()
            if cpf == "cadastrar":
                dados = TelaCadastroComprador().screen()
                cpf = self.controlador_comprador.adicionar_comprador(dados)
                while True:
                    opcao = TelaInicialComprador().screen()
                    if opcao == "historico":
                        lista = self.controlador_comprador.mostrar_ingressos(cpf)
                        if len(lista) == 0:
                            TelaPopUp("Nao ha ingressos!")
                        else:
                            lista = [item.titulo for item in lista]
                            TelaLista(lista)
                    elif opcao == "comprar":
                        self.controlador_comprador.comprar_ingressos(cpf)
                    elif opcao == "editar":
                        dados = TelaCadastroComprador().screen()
                        usuario = self.controlador_comprador.alterar_dados(cpf, dados)
                        TelaPopUp(usuario.nome)
            elif cpf == "sair":
                exit(0)
            else:
                if self.controlador_comprador.confere_cpf_existe(cpf):
                    TelaInicialComprador().screen()
                else:
                    print("cnpj nao cadastrado")
                    TelaPopUp("Usuário inexistente")

    def abrir_tela_organizador(self):
        while True:
            cnpj = TelaLogin().screen()
            if cnpj == "cadastrar":
                dados = TelaCadastroOrganizador().screen()
                cnpj = self.controlador_organizador.adicionar_organizador(dados)
                while True:
                    opcao = TelaInicialOganizador().screen()
                    if opcao == "historico":
                        lista = self.controlador_organizador.mostra_eventos_organizados(
                            cnpj
                        )
                        if len(lista) == 0:
                            TelaPopUp("Não há eventos!")
                        else:
                            TelaLista(lista)
                    elif opcao == "cadastrar":
                        locais = self.controlador_evento.locais
                        # cadastrando só o nome do local e nao o obj
                        dados = TelaCadastroEvento(locais).screen()
                        if dados == "plus":
                            dados = TelaCadastroLocal().screen()
                            self.controlador_evento.cadastra_local(dados)
                        else:
                            self.controlador_evento.criar_evento(cnpj, dados)
                    elif opcao == "criar":
                        dados = TelaCadastroLocal().screen()
                        self.controlador_evento.cadastra_local(dados)
                    elif opcao == "editar":
                        dados = TelaCadastroOrganizador().screen()
                        usuario = self.controlador_organizador.alterar_dados(
                            cnpj, dados
                        )
                        TelaPopUp(usuario.nome + "\n Atualizacao de dados completa!")
            elif cnpj == "sair":
                exit(0)
            else:
                if self.controlador_organizador.confere_cnpj_existe(cnpj):
                    TelaInicialOganizador().screen()
                else:
                    print("cnpj nao cadastrado")
                    TelaPopUp()

    def abrir_tela_administrador(self):
        while True:
            opcao = TelaAdministrador().screen()
            if opcao == "compradores":
                lista = self.controlador_comprador.lista_compradores
                lista = [item.nome for item in lista]
                TelaLista(lista)
            elif opcao == "organizadores":
                lista = self.controlador_organizador.lista_organizadores
                lista = [item.nome for item in lista]
                TelaLista(lista)
            elif opcao == "eventos":
                lista = self.controlador_evento.eventos
                lista = [item.titulo for item in lista]
                TelaLista(lista)
            elif opcao == "locais":
                lista = self.controlador_evento.locais
                lista = [item.nome for item in lista]
                TelaLista(lista)
