from controle.controlador_administrador import ControladorAdministrador
from controle.controlador_comprador import ControladorComprador
from controle.controlador_organizador import ControladorOrganizador
from limite.tela_comprador import TelaComprador
from limite.tela_organizador import TelaOrganizador


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
