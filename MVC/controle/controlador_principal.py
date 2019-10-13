from limite.tela_controlador_principal import TelaControladorPrincipal
from entidade.comprador import Comprador
from controle.controlador_comprador import ControladorComprador
from controle.controlador_organizador import ControladorOrganizador

class ControladorPrincipal:
    def __init__(self):
        self.tela_principal = TelaControladorPrincipal()
        self.controlador_comprador = ControladorComprador()
        self.controlador_organizador = ControladorOrganizador()

    def inicia(self):
        while True:
            opcao_ini = self.tela_principal.menu_inicial()
            if opcao_ini == 1:                
                opcao_sec = self.tela_principal.menu_principal()
                self.abrir_tela_comprador(opcao_sec)
            elif opcao_ini == 2:
                opcao_sec = self.tela_principal.menu_principal()
                self.abrir_tela_organizador(opcao_sec)
            elif opcao_ini == 3:
                print ("Saindo...")
                exit()

    def abrir_tela_comprador(self, opcao):
        if opcao == 1:
            opcao_cadastrado = self.tela_principal.menu_comprador_cadastrado()
            if opcao_cadastrado == 1:
                self.controlador_comprador.comprar_ingressos()
            elif opcao_cadastrado == 2:
                self.controlador_comprador.mostrar_ingressos()
        elif opcao == 2:
            self.controlador_comprador.adicionar_comprador()
        elif opcao == 3:
            self.controlador_comprador.alterar_dados()
        elif opcao == 4:
            self.controlador_comprador.mostrar_compradores_cadastrados()


    def abrir_tela_organizador(self, opcao):
        if opcao == 1:
            opcao_cadastrado = self.tela_principal.menu_organizador_cadastrado()
            if opcao_cadastrado == 1:
                self.controlador_organizador.cadastrar_evento()
            elif opcao_cadastrado == 2:
                self.controlador_organizador.mostrar_eventos()
        elif opcao == 2:
            self.controlador_organizador.adicionar_organizador()
        elif opcao == 3:
            self.controlador_organizador.alterar_dados()
        elif opcao == 4:
            self.controlador_organizador.mostrar_organizadores_cadastrados()