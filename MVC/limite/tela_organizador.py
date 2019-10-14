from entidade.organizador import Organizador
from excecoes.comando_invalido import ComandoInvalido


class TelaOrganizador:
    
    def tamanho_min_max(self, message):
        while True:
            valor_lido = input(message+": ")
            try:
                if not len(valor_lido) > 1 or not len(valor_lido) < 100:
                    raise ValueError
                return valor_lido
            except ValueError:
                print ("Por favor entre com um valor válido")
                if valor_lido:
                    print ("String com de 1 e 150 caracteres")

    def dados(self):
        info_cadastro = {
            'Nome': '',
            'Endereco': '',
            'Telefone': '',
            'Email': '',
            'cnpj': ''
        }

        for item in info_cadastro:
            info_cadastro[item] = self.tamanho_min_max(item)
        
        return info_cadastro

    def lista_organizadores_cadastrados(self, lista):
        print (lista)
        for item in lista:
            print (item.nome)

    def ler_nome_evento(self):
        titulo = input("Digite o nome do evento: ")
        return titulo

    def pede_cnpj(self):
        cnpj = input('Qual o cnpj do organizador?\n')
        return cnpj

    # def criar_evento(self):
    #     info_evento = {
    #         'Categoria do Evento': '',
    #         'Data do Evento': '',
    #         'Nome do Local': '',
    #     }
        
    #     titulo_evento = self.ler_nome_evento()
    #     categoria_evento = input("Digite a categoria do evento: ")
    #     data_evento = input("Digite a data do evento: ")
    #     nome_local = input("Digite o nome do local: ")
    #     endereco_local = input("Digite o endereço do local: ")
    #     while False:
    #         capacidade_local = int(input("Digite a capacidade do local: "))
    #         classificacao_indicativa = int(input("Digite a classificação indicativa: "))
    #         valor_ingresso = float(input("Digite o valor do ingresso: "))
    #         if not isinstance(capacidade_local, int) or not isinstance(classificacao_indicativa, int) or not isinstance(
    #                 (valor_ingresso, float)):
    #             raise ComandoInvalido.numero_invalido()
    #         else:
    #             self.controlador.cadastra_evento(titulo_evento,
    #                                              categoria_evento,
    #                                              data_evento,
    #                                              nome_local,
    #                                              endereco_local,
    #                                              capacidade_local,
    #                                              classificacao_indicativa,
    #                                              valor_ingresso)
    #             return True

    def mostrar_relatorio_compras(self):
        pass

    def mostrar_informacoes_evento(self, titulo_evento: str):
        pass
