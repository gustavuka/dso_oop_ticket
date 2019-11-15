from MVC.controle.controlador_administrador import ControladorAdministrador
from MVC.controle.controlador_comprador import ControladorComprador
from MVC.controle.controlador_organizador import ControladorOrganizador
from MVC.limite.tela_comprador import TelaComprador
from MVC.limite.tela_organizador import TelaOrganizador


class TelaAdministrador:

    def __init__(self, controlador_administrador: ControladorAdministrador):
        self.__controlador_administrador = controlador_administrador

    @property
    def controlador_administrador(self):
        return self.__controlador_administrador

    def mostrar_organizadores_cadastrados(self):
        self.controlador_administrador.mostra_organizadores_cadastrados()

    def mostrar_compradores_cadastrados(self):
        self.controlador_administrador.mostra_compradores_cadastrados()
