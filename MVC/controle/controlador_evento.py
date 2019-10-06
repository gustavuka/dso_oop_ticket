from local import Local

class ControladorEvento:

    def __init__(self):
        self.__eventos = []
        self.__locais = []

    def cadastrar_local(self, local: Local):
        if local not in self.locais:
            self.__locais.append(local)
