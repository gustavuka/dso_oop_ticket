from MVC.controle.controlador_comprador import ControladorComprador
from MVC.controle.controlador_organizador import ControladorOrganizador

class ControladorAdministrador:

    def __init__(self, controlador_organizador: ControladorOrganizador, controlador_comprador: ControladorComprador):
        self.__controlador_organizador = controlador_organizador
        self.__controlador_comprador = controlador_comprador

    @property
    def controlador_organizador(self):
        return self.__controlador_organizador

    @property
    def controlador_comprador(self):
        return self.__controlador_comprador

    def mostra_compradores_cadastrados(self):
        self.controlador_comprador.mostrar_compradores_cadastrados()

    def mostra_organizadores_cadastrados(self):
        self.controlador_organizador.mostrar_organizadores_cadastrados()
