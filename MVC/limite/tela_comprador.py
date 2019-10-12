
# from controle.controlador_comprador import ControladorComprador

class TelaComprador:
    # self.controlador = ControladorComprador()
    def __init__(self):
        self.__info_cadastro = {
            'Nome': 'n',
            'Endereco': 'e',
            'Telefone': 't',
            'Email': '@',
            'cpf': 'c',
            'Idade': 'i'
        }

    def novo_comprador(self):
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")
        
        return self.__info_cadastro

    def alterar_dados(self):
        cpf = input('Qual o cpf do comprador a ser editado?')
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")

        return (cpf, self.__info_cadastro)
