from limite.tela_controlador_principal import TelaControladorPrincipal
from limite.tela_comprador import TelaComprador
from entidade.comprador import Comprador
from controle.controlador_comprador import ControladorComprador

class ControladorPrincipal:

    def inicia(self):
        opcao = TelaControladorPrincipal().tela_inicial()
        if opcao == 'c':
            self.abrir_tela_comprador()
        elif opcao == 'o':
            self.abrir_tela_organizador()
        else:
            print ('Error')

    def abrir_tela_comprador(self):
        print ('Abrir tela compr.')
        info_comprador = (TelaComprador().novo_comprador())
        ControladorComprador().adicionar_comprador(info_comprador)


    def abrir_tela_organizador(self):
        print ('Abrir tela orgn.')