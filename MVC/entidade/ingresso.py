


class Ingresso:

    def __init__(self, evento: evento, tipo: str, data_compra: Date):
        self.__evento = evento
        self.__tipo = tipo
        self.__data_compra = data_compra
    
    @property
    def evento(self):
        return self.__evento
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def data_compra(self):
        return self.__data_compra
