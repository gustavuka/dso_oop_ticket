

class ControladorComprador:

    def __init__(self):
        self.__lista_compradores = []
        self.__opcoes = {
            'n': 'Nome',
            'e': 'Endereco',
            't': 'Telefone',
            '@': 'Email',
            'c': 'cpf',
            'i': 'Idade'
        }

    def adicionar_comprador(self, novo_comprador):
        self.__lista_compradores.append(novo_comprador)

    @property
    def lista_compradores(self):
        return self.__lista_compradores

    @property
    def opcoes(self):
        return self.opcoes
