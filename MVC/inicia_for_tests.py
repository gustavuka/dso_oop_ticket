class IniciaForTests:   
    def comprador_teste(self, Comprador, lista_compradores):
        novo_comprador = Comprador(
            "Nome",
            "Endereco",
            "Telefone",
            "Email",
            "cpf",
            "Idade"
        )
        lista_compradores.append(novo_comprador)
        novo_comprador2 = Comprador(
            "Nome",
            "Endereco",
            "Telefone",
            "Email",
            "cpf",
            "Idade"
        )
        lista_compradores.append(novo_comprador2)

    def organizador_teste(self):
        novo_organizador = Comprador(
            "Nome",
            "Endereco",
            "Telefone",
            "Email",
            "cpf",
            "Idade"
        )
        self.__lista_compradores.append(novo_organizador)
        novo_comprador2 = Comprador(
            "Nome",
            "Endereco",
            "Telefone",
            "Email",
            "cpf",
            "Idade"
        )
        self.__lista_compradores.append(novo_organizador2)

    def eventos_teste(self):
        eventoteste = Evento(
            'eventoteste',
            'categoria_evento',
            'data_evento',
            'nome_local',
            'classificacao_indicativa',
            'valor_ingresso'
        )
        self.__eventos.append(eventoteste)
        eventoteste2 = Evento(
            'eventoteste2',
            'categoria_evento',
            'data_evento',
            'nome_local',
            'classificacao_indicativa',
            'valor_ingresso'
        )
        self.__eventos.append(eventoteste2)
