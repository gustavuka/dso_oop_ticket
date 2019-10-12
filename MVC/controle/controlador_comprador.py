from entidade.comprador import Comprador


class ControladorComprador:
    def __init__(self):
        self.__lista_compradores = []

    def adicionar_comprador(self, info_comprador):
        novo_comprador = Comprador(
            info_comprador["Nome"],
            info_comprador["Endereco"],
            info_comprador["Telefone"],
            info_comprador["Email"],
            info_comprador["cpf"],
            info_comprador["Idade"],
        )
        self.lista_compradores.append(novo_comprador)

    @property
    def lista_compradores(self):
        return self.__lista_compradores
    
    @lista_compradores.setter
    def lista_compradores(self, lista_compradores):
        self.__lista_compradores = lista_compradores
