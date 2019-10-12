
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
        for item in self.info_cadastro:
            self.info_cadastro[item] = input(item + ": ")
        
        return self.__info_cadastro

    def alterar_dados(self):
        cpf = input('Qual o cpf do comprador a ser editado?')
        for item in self.info_cadastro:
            self.info_cadastro[item] = input(item + ": ")

        return (cpf, self.info_cadastro)

    def mostrar_dados(self, cpf, lista_compradores):
        for item in lista_compradores:
            if item.cpf == cpf:
                for key, value in item.items():
                    print (key + ': ' + value) 
            