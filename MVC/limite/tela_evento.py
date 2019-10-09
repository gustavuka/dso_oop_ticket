from controlador_evento import ControladorEvento


class TelaEvento:

    def __init__(self, controlador: ControladorEvento):
        self.__controlador = controlador
    
    @property
    def controlador(self):
        return self.__controlador
    
    def ler_codigo_evento(self):
        pass
    
    def cadastrar_evento(self):
        pass
    
    def alterar_local_evento(self, codigo_evento: str):
        pass
    
    def alterar_categoria_evento(self, codigo_evento: str):
        pass
    
    def alterar_titulo_evento(self, codigo_evento: str):
        pass
    
    def alterar_valor_evento(self, codigo_evento: str):
        pass
    
    def alterar_data_evento(self, codigo_evento: str):
        pass
