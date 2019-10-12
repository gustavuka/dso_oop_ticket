from limite.tela_controlador_principal import TelaControladorPrincipal
from entidade.comprador import Comprador
from controle.controlador_comprador import ControladorComprador
# from controle.controlador_organizador import ControladorOrganizador

class ControladorPrincipal:

    def inicia(self):
        opcao_ini, opcao_sec = TelaControladorPrincipal().menu_principal()
        if opcao_ini == "c":
            self.abrir_tela_comprador(opcao_sec)
        elif opcao_ini == "o":
            self.abrir_tela_organizador(opcao_sec)

    def abrir_tela_comprador(self, opcao):
        if opcao == 'n':
            ControladorComprador().adicionar_comprador()
        elif opcao == 'e':
            ControladorComprador().alterar_dados()


    def abrir_tela_organizador(self, opcao):
        if opcao == 'n':
            ControladorOrganizador().adicionar_organizador()
        elif opcao == 'e':
            ControladorOrganizador().alterar_dados()