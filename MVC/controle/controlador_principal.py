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
)


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

        self.tela_inicial = TelaInicial()
        self.tela_organizador = TelaInicialOganizador()
        self.tela_login = TelaLogin()
        self.cadastro_organizador = TelaCadastroOrganizador()

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
        opcao_ini = self.tela_inicial.screen()
        if opcao_ini == 1:
            while True:
                cpf = self.tela_login.screen()
                opcao_sec = self.tela_menu_principal.menu_cliente()
                if opcao_sec == 6:
                    self.inicia()
                self.abrir_tela_comprador(opcao_sec)
        elif opcao_ini == 2:
            while True:
                self.abrir_tela_organizador()            
                if opcao_sec == 6:
                    self.inicia()
                self.abrir_tela_organizador(opcao_sec)
        elif opcao_ini == 3:
            while True:
                opcao_sec = self.tela_principal.menu_administrador()
                if opcao_sec == 3:
                    self.inicia()
                self.abrir_tela_administrador(opcao_sec)
        elif opcao_ini == 4:
            print("Saindo...")
            exit()

    def abrir_tela_comprador(self, opcao):
        if opcao == 1:
            cpf = self.tela_pede_cpf.pede_cpf()
            cpf_existe = self.controlador_comprador.confere_cpf_existe(cpf)
            if cpf_existe:
                opcao_cadastrado = (
                    self.tela_comprador_cadastrado.menu_comprador_cadastrado()
                )
                if opcao_cadastrado == 1:
                    self.controlador_comprador.comprar_ingressos()
                elif opcao_cadastrado == 2:
                    self.controlador_comprador.mostrar_ingressos()
            else:
                self.tela_pede_cpf.mostrar_mensagem(
                    "Aviso!", "CPF inexistente! Digite novamente."
                )
                self.abrir_tela_comprador(1)
        elif opcao == 2:
            comprador = self.tela_cadastro_comprador.info_comprador()
            cpf_existe = self.controlador_comprador.confere_cpf_existe(comprador[4])
            if not cpf_existe:
                self.controlador_comprador.adicionar_comprador(comprador)
                self.tela_cadastro_comprador.mostrar_mensagem(
                    "Sucesso!",
                    "Bem vindo {}!".format(
                        self.tela_cadastro_comprador.info_comprador()[0]
                    ),
                )
            else:
                self.tela_cadastro_comprador.mostrar_mensagem(
                    "Erro!", "Comprador já cadastrado! Tente com outro CPF"
                )
                self.abrir_tela_comprador(2)
        elif opcao == 3:
            cpf = self.tela_pede_cpf.pede_cpf()
            comprador_existe = self.controlador_comprador.confere_cpf_existe(cpf)
            if comprador_existe:
                self.controlador_comprador.alterar_dados(comprador_existe)
                self.tela_cadastro_comprador.mostrar_mensagem(
                    "Sucesso!", "Alterado com sucesso\n{}".format(comprador_existe)
                )
            else:
                self.tela_pede_cpf.mostrar_mensagem(
                    "Aviso!", "CPF inexistente! Digite novamente."
                )
                self.abrir_tela_comprador(3)
        elif opcao == 4:
            self.controlador_evento.mostrar_todos_eventos()
        elif opcao == 5:
            exit()

    def abrir_tela_organizador(self):        
        cnpj = self.tela_login.screen()
        if cnpj == "cadastrar":
            dados = self.cadastro_organizador.screen()            
            organizador = self.controlador_organizador.adicionar_organizador(dados)
            self.tela_organizador.screen()
        elif cnpj == "sair":
            exit()
        else:
            if self.controlador_organizador.confere_cnpj_existe(cnpj):
                





        if opcao == 1:
            opcao_cadastrado = self.tela_principal.menu_organizador_cadastrado()
            if opcao_cadastrado == 1:
                self.controlador_organizador.cadastrar_evento()
            elif opcao_cadastrado == 2:
                self.controlador_organizador.mostra_eventos_organizados()
            elif opcao_cadastrado == 3:
                self.controlador_evento.cadastra_local()
            elif opcao == 4:
                exit()
        elif opcao == 2:
            self.controlador_organizador.adicionar_organizador()
        elif opcao == 3:
            self.controlador_organizador.alterar_dados()
        elif opcao == 4:
            self.controlador_organizador.mostra_eventos_organizados()
        elif opcao == 5:
            self.controlador_organizador.mostra_informacoes_evento()
        elif opcao == 6:
            exit()

    def abrir_tela_administrador(self, opcao):
        if opcao == 1:
            self.controlador_administrador.mostra_organizadores_cadastrados()
        elif opcao == 2:
            self.controlador_administrador.mostra_compradores_cadastrados()
