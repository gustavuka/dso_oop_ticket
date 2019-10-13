
# from controle.controlador_comprador import ControladorComprador
from limite.tela_controlador_principal import TelaControladorPrincipal

class TelaComprador:
    def __init__(self):
        self.__info_cadastro = {
            'Nome': '',
            'Endereco': '',
            'Telefone': '',
            'Email': '',
            'cpf': '',
            'Idade': ''
        }


    def novo_comprador(self):
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")
        
        return self.__info_cadastro
    
    def alterar_dados(self):
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")

        return (self.__info_cadastro)

    def pede_cpf(self):
        cpf = input('Qual o cpf do comprador?\n')
        return cpf

    def mostrar_dados(self, cpf, lista_compradores):
        for item in lista_compradores:
            if item.cpf == cpf:
                for key, value in item.items():
                    print (key + ': ' + value)

    def print_lista(self, lista):
        print (lista)
        for item in lista:
            print (item.nome)
    
    def usuario_inexistente(self):
        print ("Usuario inexistente, por favor verfique o cpf.")

    def confirmacao_de_compra(self, evento):
        print ("Confirmar a compra para o evento: " + evento)
        print ("Confirmar - 1")
        print ("Cancelar - 2")
        confirmacao = TelaControladorPrincipal.le_numero_inteiro([1,2])
        if confirmacao == 1:
            return True
