from limite.tela_controlador_principal import TelaControladorPrincipal
from controle.controlador_comprador import ControladorComprador
from controle.controlador_organizador import ControladorOrganizador
from controle.controlador_evento import ControladorEvento
from MVC.controle.controlador_administrador import ControladorAdministrador
from MVC.limite.tela_administrador import TelaAdministrador
from MVC.limite.tela_comprador import TelaComprador
from MVC.limite.tela_comprador_cadastrado import TelaCompradorCadastrado
from MVC.limite.tela_menu_principal import MenuPrincipal
from MVC.limite.tela_pede_cpf import TelaPedeCPF


class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaControladorPrincipal()
        self.__tela_administrador = TelaAdministrador
        self.__controlador_evento = ControladorEvento()
        self.__controlador_comprador = ControladorComprador(self.controlador_evento)
        self.__controlador_organizador = ControladorOrganizador(self.controlador_evento)
        self.__controlador_administrador = ControladorAdministrador(self.controlador_organizador,
                                                                    self.controlador_comprador)
        self.__tela_menu_principal = MenuPrincipal()
        self.__tela_comprador = TelaComprador()
        self.__tela_comprador_cadastrado = TelaCompradorCadastrado()
        self.__tela_pede_cpf = TelaPedeCPF()

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
    def tela_pede_cpf(self):
        return self.__tela_pede_cpf

    def inicia(self):
        opcao_ini = self.tela_principal.menu_inicial()
        if opcao_ini == 1:
            while True:
                opcao_sec = self.tela_menu_principal.menu_cliente()
                if opcao_sec == 6:
                    self.inicia()
                self.abrir_tela_comprador(opcao_sec)
        elif opcao_ini == 2:
            while True:
                opcao_sec = self.tela_menu_principal.menu_cliente()
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
                opcao_cadastrado = self.tela_comprador_cadastrado.menu_comprador_cadastrado()
                if opcao_cadastrado == 1:
                    self.controlador_comprador.comprar_ingressos()
                elif opcao_cadastrado == 2:
                    self.controlador_comprador.mostrar_ingressos()
            else:
                self.tela_pede_cpf.mostrar_mensagem('Aviso!', 'CPF inexistente! Digite novamente.')
                self.abrir_tela_comprador(1)
        elif opcao == 2:
            self.controlador_comprador.adicionar_comprador()
        elif opcao == 3:
            self.controlador_comprador.alterar_dados()
        elif opcao == 4:
            self.controlador_evento.mostrar_todos_eventos()
        elif opcao == 5:
            exit()

    def abrir_tela_organizador(self, opcao):
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
