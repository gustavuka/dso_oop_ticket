class IniciaForTests:   
    def comprador_teste(self, Comprador, lista_compradores):
        novo_comprador = Comprador(
            "Zé Alguém",
            "Rua Camargo 253",
            "(48) 92020-0566",
            "ze@email.com",
            "123.456.789-00",
            "30"
        )
        lista_compradores.append(novo_comprador)
        novo_comprador2 = Comprador(
            "João Ninguém",
            "Av. Acácia 22",
            "(51) 95458-9632",
            "joao@email.com",
            "789.456.123-00",
            "21"
        )
        lista_compradores.append(novo_comprador2)

    def organizador_teste(self, Organizador, lista_organizadores):
        novo_organizador = Organizador(
            "Evento Mania",
            "Rua Eventin 456",
            "(51) 95458-9632",
            "evento@email.com",
            "12.345.678/0001"
        )
        lista_organizadores.append(novo_organizador)
        novo_organizador2 = Organizador(
            "Shows S/A",
            "Av. Show 111",
            "(48) 92020-0566",
            "shows@gmail.com",
            "98.765.432/0002"
        )
        lista_organizadores.append(novo_organizador2)

    def eventos_teste(self, Evento, eventos):
        eventoteste = Evento(
            '98.765.432/0002',
            'Super Show Pirotécnico',
            'Gratuito',
            '01/01/2020',
            'Av.Beira Mar, Florianópolis',
            '14',
            '0'
        )
        eventos.append(eventoteste)
        eventoteste2 = Evento(
            '12.345.678/0001',
            'Ratos de Porão',
            'Show',
            '06/11/2019',
            'Parador 55',
            '18',
            '120'
        )
        eventos.append(eventoteste2)

    def locais_teste(self, Local, locais):
        localteste = Local(
            'Casa 48',
            'Av. Lagoa 123',
            '560'
        )
        locais.append(localteste)
        localteste2 = Local(
            'Parador 66',
            'Rua. Poligot 66',
            '1000'
        )
        locais.append(localteste2)
