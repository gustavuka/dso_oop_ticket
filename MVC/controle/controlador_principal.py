from limite.tela_controlador_principal import TelaControladorPrincipal
from entidade.comprador import Comprador
from controle.controlador_comprador import ControladorComprador
# from controle.controlador_organizador import ControladorOrganizador

class ControladorPrincipal:
    def __init__(self):
        self.tela_principal = TelaControladorPrincipal()
        self.controlador = ControladorComprador()

    def inicia(self):
        while True:
            opcao_ini = self.tela_principal.menu_inicial()
            if opcao_ini == "1":                
                opcao_sec = self.tela_principal.menu_principal()
                self.abrir_tela_comprador(opcao_sec)
            elif opcao_ini == "2":
                opcao_sec = self.tela_principal.menu_principal()
                self.abrir_tela_organizador(opcao_sec)
            elif opcao_ini == "3":
                print ("Saindo...")
                exit()
            else:
                print ('-------------------------------------')
                print ("Por favor selecione uma opcao válida!")
                print ('-------------------------------------')


    def abrir_tela_comprador(self, opcao):
        if opcao == '2':
            self.controlador.adicionar_comprador()
        elif opcao == '3':
            self.controlador.alterar_dados()
        elif opcao == "4":
            self.controlador.print_lista()


    def abrir_tela_organizador(self, opcao):
        if opcao == 'n':
            ControladorOrganizador().adicionar_organizador()
        elif opcao == 'e':
            ControladorOrganizador().alterar_dados()