from excecoes.comando_invalido import ComandoInvalido


class TelaEvento:
    def __init__(self):
        pass

    def buscar_evento(self, titulo_evento: str):
        return self.controlador.busca_evento(titulo_evento)
    
    def ler_titulo_evento(self):
        titulo_evento = input("Digite o nome do evento: ")
        return titulo_evento
    
    def cadastrar_evento(self):
        info_evento = {}
        info_evento['titulo_evento'] = self.ler_titulo_evento()
        info_evento['categoria_evento'] = input("Digite a categoria do evento: ")
        info_evento['data_evento'] = input("Digite a data do evento: ")
        info_evento['classificacao_indicativa'] = (input("Digite a classificação indicativa: "))
        info_evento['valor_ingresso'] = (input("Digite o valor do ingresso: "))
        # if not isinstance(capacidade_local, int) or not isinstance(classificacao_indicativa, int) or not isinstance((valor_ingresso, float)):
        #     raise ComandoInvalido.numero_invalido()
        # else:
        return info_evento

    # Nao mexi aqui, tem que arrumar a funcao para alterar local
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
    
    def print_eventos(self, lista):
        for item in lista:
            print (item.titulo)

    def selecionar_locais(self, lista):
        if len(lista) > 1:
            count = 1
            print ('-------------------------------------')
            print ("Por favor selecione o local: ")
            for item in lista:
                print (item.nome + ": " + str(count))
                count += 1
            print ("Criar novo local: " + str(count))
            print ('-------------------------------------')
        else:
            #criar um raise
            print ("Nenhum local cadastrado, por favor realize o cadastro")
            return False
        #adicionar filtros aqui
        opcao = int(input())
        #tratar opcao para novo local
        opcao = lista[(opcao-1)]
        return opcao

    # def alterar_categoria_evento(self):
    #     titulo_evento = self.ler_titulo_evento()
    #     nova_categoria_evento = input("Digite a nova categoria do evento: ")
    #     self.controlador.altera_categoria_evento(titulo_evento, nova_categoria_evento)
    #     print("Categoria alterada com sucesso!")

    # def alterar_titulo_evento(self):
    #     titulo_evento = self.ler_titulo_evento()
    #     novo__evento = input("Digite o novo título do evento: ")
    #     self.controlador.altera_titulo_evento(titulo_evento, novo__evento)
    #     print("Titulo alterado com sucesso!")

    # def alterar_valor_evento(self):
    #     titulo_evento = self.ler_titulo_evento()
    #     novo_valor_evento = float(input("Digite o novo valor do evento: "))
    #     if isinstance(novo_valor_evento, float):
    #         self.controlador.altera_valor_evento(titulo_evento, novo_valor_evento)
    #         print("Valor alterado com sucesso!")
    #     else:
    #         raise ComandoInvalido.numero_invalido()

    # def alterar_data_evento(self):
    #     titulo_evento = self.ler_titulo_evento()
    #     nova_data_evento = input("Digite a nova data: ")
    #     self.controlador.altera_data_evento(titulo_evento, nova_data_evento)

    # def mostrar_eventos(self):
    #     for item in self.controlador.eventos:
    #         print (item.titulo)
