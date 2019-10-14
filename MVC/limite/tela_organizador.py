from entidade.organizador import Organizador
from excecoes.comando_invalido import ComandoInvalido


class TelaOrganizador:
    
    def tamanho_min_max(self, message):
        while True:
            valor_lido = input(message+": ")
            try:
                if not len(valor_lido) >= 1 or not len(valor_lido) < 150:
                    raise ValueError
                return valor_lido
            except ValueError:
                print ("Por favor entre com um valor válido")
                if valor_lido:
                    print ("String com de 1 e 150 caracteres")

    def le_dados(self):
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

    def lista_organizadores_cadastrados(self, lista_organizadores):
        for organizador in lista_organizadores:
            print("Nome do organizador: "+organizador.nome+"\nEmail: "+organizador.email+"\nTelefone: "+organizador.telefone+"\n")

    def ler_nome_evento(self):
        titulo = input("Digite o nome do evento: ")
        return titulo

    def pede_cnpj(self):
        cnpj = input('Qual o cnpj do organizador?\n')
        return cnpj

    def imprime_mensagem(self, mensagem):
        print(mensagem)

    def criar_evento(self):
         info_evento = {
             'Nome do Evento: ',
             'Categoria do Evento ',
             'Data do evento: ',
             'Nome do local: ',
             'Endereço do local ',
             'Capacidade do local: ',
         }
         while False:
             capacidade_local = int(input("Digite a capacidade do local: "))
             classificacao_indicativa = int(input("Digite a classificação indicativa: "))
             valor_ingresso = float(input("Digite o valor do ingresso: "))
             if not isinstance(capacidade_local, int) or not isinstance(classificacao_indicativa, int) or not isinstance(
                    (valor_ingresso, float)):
                 raise ComandoInvalido.numero_invalido()
             else:
                 return True


    def mostrar_relatorio_compras(self):
        pass

    def mostrar_informacoes_evento(self):
        titulo = input("Digite o título do evento que deseja visualizar as informações: ")
        return titulo
