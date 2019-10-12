
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

    def pede_cpf(self):
        cpf = input('Qual o cpf do comprador a ser editado?')
        return cpf

    def alterar_dados(self):
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")

        return (self.__info_cadastro)

    def mostrar_dados(self, cpf, lista_compradores):
        for item in lista_compradores:
            if item.cpf == cpf:
                for key, value in item.items():
                    print (key + ': ' + value)

    def print_lista(self, lista):
        print (lista)
        for item in lista:
            print (item.nome)
