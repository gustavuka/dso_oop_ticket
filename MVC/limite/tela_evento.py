from controle.controlador_evento import ControladorEvento
from excecoes.comando_invalido import ComandoInvalido


class TelaEvento:

    def __init__(self):
        self.__controlador = ControladorEvento()

    @property
    def controlador(self):
        return self.__controlador

    def buscar_evento(self, titulo_evento: str):
        return self.controlador.busca_evento(titulo_evento)
    
    def ler_titulo_evento(self):
        titulo_evento = input("Digite o título do evento: ")
        return titulo_evento
    
    def cadastrar_evento(self):
        titulo_evento = self.ler_titulo_evento()
        categoria_evento = input("Digite a categoria do evento: ")
        data_evento = input("Digite a data do evento: ")
        nome_local = input("Digite o nome do local: ")
        endereco_local = input("Digite o endereço do local: ")
        while False:
            capacidade_local = int(input("Digite a capacidade do local: "))
            classificacao_indicativa = int(input("Digite a classificação indicativa: "))
            valor_ingresso = float(input("Digite o valor do ingresso: "))
            if not isinstance(capacidade_local, int) or not isinstance(classificacao_indicativa, int) or not isinstance((valor_ingresso, float)):
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

    def alterar_local_evento(self):
        titulo_evento = self.ler_titulo_evento()
        novo_nome_local = input("Digite o novo nome do local do evento: ")
        novo_endereco_local = input("Digite o novo endereço do evento: ")
        while False:
            nova_capacidade_local = int(input("Digite a nova capacidade do local do evento: "))
            if not isinstance(nova_capacidade_local, int):
                raise ComandoInvalido.numero_invalido()
            else:
                self.controlador.altera_local_evento(titulo_evento,
                                                     novo_nome_local,
                                                     novo_endereco_local,
                                                     nova_capacidade_local)
                print("Local alterado com sucesso!")
                return True

    def alterar_categoria_evento(self):
        titulo_evento = self.ler_titulo_evento()
        nova_categoria_evento = input("Digite a nova categoria do evento: ")
        self.controlador.altera_categoria_evento(titulo_evento, nova_categoria_evento)
        print("Categoria alterada com sucesso!")

    def alterar_titulo_evento(self):
        titulo_evento = self.ler_titulo_evento()
        novo__evento = input("Digite o novo título do evento: ")
        self.controlador.altera_titulo_evento(titulo_evento, novo__evento)
        print("Titulo alterado com sucesso!")

    def alterar_valor_evento(self):
        titulo_evento = self.ler_titulo_evento()
        novo_valor_evento = float(input("Digite o novo valor do evento: "))
        if isinstance(novo_valor_evento, float):
            self.controlador.altera_valor_evento(titulo_evento, novo_valor_evento)
            print("Valor alterado com sucesso!")
        else:
            raise ComandoInvalido.numero_invalido()

    def alterar_data_evento(self):
        titulo_evento = self.ler_titulo_evento()
        nova_data_evento = input("Digite a nova data: ")
        self.controlador.altera_data_evento(titulo_evento, nova_data_evento)

    def mostrar_eventos(self):
        for item in self.controlador.eventos:
            print (item.titulo)
