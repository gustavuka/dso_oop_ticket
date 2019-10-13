from entidade.organizador import Organizador
from excecoes.comando_invalido import ComandoInvalido


class TelaOrganizador:

    def __init__(self):
        self.__info_cadastro = {
            'Nome': '',
            'Endereco': '',
            'Telefone': '',
            'Email': '',
            'cnpj': ''
        }

    def novo_organizador(self):
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")
        
        return self.__info_cadastro
    
    def alterar_dados(self):
        for item in self.__info_cadastro:
            self.__info_cadastro[item] = input(item + ": ")

        return (self.__info_cadastro)

    def print_lista(self, lista):
        print (lista)
        for item in lista:
            print (item.nome)

    def ler_titulo_evento(self):
        titulo = input("Digite o título do evento: ")
        return titulo

    def cadastrar_organizador(self):
        nome = input("Digite o nome do organizador: ")
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        cnpj = input("Digite o cnpj: ")
        organizador = Organizador(nome, endereco, telefone, email, cnpj)
        return organizador

    def pede_cnpj(self):
        cnpj = input('Qual o cnpj do organizador?\n')
        return cnpj  

    def criar_evento(self):
        titulo_evento = self.ler_titulo_evento()
        categoria_evento = input("Digite a categoria do evento: ")
        data_evento = input("Digite a data do evento: ")
        nome_local = input("Digite o nome do local: ")
        endereco_local = input("Digite o endereço do local: ")
        while False:
            capacidade_local = int(input("Digite a capacidade do local: "))
            classificacao_indicativa = int(input("Digite a classificação indicativa: "))
            valor_ingresso = float(input("Digite o valor do ingresso: "))
            if not isinstance(capacidade_local, int) or not isinstance(classificacao_indicativa, int) or not isinstance(
                    (valor_ingresso, float)):
                raise ComandoInvalido.numero_invalido()
            else:
                self.controlador.cadastra_evento(titulo_evento,
                                                 categoria_evento,
                                                 data_evento,
                                                 nome_local,
                                                 endereco_local,
                                                 capacidade_local,
                                                 classificacao_indicativa,
                                                 valor_ingresso)
                return True

    def listar_eventos_organizados(self):
        pass

    def mostrar_relatorio_compras(self):
        pass

    def mostrar_informacoes_evento(self, titulo_evento: str):
        pass
