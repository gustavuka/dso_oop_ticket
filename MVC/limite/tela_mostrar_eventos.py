import PySimpleGUI as sg

from MVC.controle.controlador_evento import ControladorEvento


class TelaMostrarEventos:
    def __init__(self, lista_eventos):
        self.__window = None
        self.__controlador_evento = ControladorEvento()

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    def abrir_tela(self):
        sg.Popup('Eventos cadastrados',
                 'The values are', values)