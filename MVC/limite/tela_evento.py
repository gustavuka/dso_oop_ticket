from date import datetime

class TelaEvento:

    def __init__(self, controlador: ControladorEvento):
        self.__controlador = controlador
    
    @property
    def controlador(self):
        return self.__controlador
    
    def buscar_evento(self):
        while True:
            codigo_evento = input("Digite o código do evento: ")
            evento = self.controlador.busca_evento(codigo_evento)
            if isinstance(evento, Evento):
                return evento
        return False
    
    def cadastrar_evento(self):
        pass
    
    def alterar_local_evento(self):
        evento = 
    
    def alterar_categoria_evento(self):
        pass
    
    def alterar_titulo_evento(self):
        pass
    
    def alterar_valor_evento(self):
        pass
    
    def alterar_data_evento(self):
        pass
