class TelaControladorPrincipal:
    print ('Bem vindo ao dso ticket!')

    def le_numero_inteiro(self, inteiros_validos = None):
        while True:
            valor_lido = input()
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print ("Por favor entre com um valor válido")
                if inteiros_validos:
                    print ("Valores validos: ", inteiros_validos)

    def menu_inicial(self):
        print ("Como gostaria de utilizar o sistema?")
        menu_inicial = [
            '-------------------------------------',
            'Comprador - 1',
            'Organizador - 2',
            'Sair - 3',
            '-------------------------------------']
        for item in menu_inicial:
            print (item)       

        opcao = self.le_numero_inteiro([1,2,3])
        return opcao

    def menu_principal(self):
        menu_table = [
            '-------------------------------------',
            'Entrar com um usuário existente - 1',
            'Cadastrar novo usuário - 2',
            'Editar usuário - 3',
            'Listar usuários - 4',
            'Mostrar todos os eventos cadastrados - 5',
            'Sair - 6',
            '-------------------------------------'
        ]
        for item in menu_table:
            print (item)

        opcao = self.le_numero_inteiro([1,2,3,4,5,6])
        return opcao
    
    def menu_comprador_cadastrado(self):
        menu_castrado = [
            '-------------------------------------',
            'Comprar ingresso - 1',
            'Mostrar histórico de ingressos - 2',
            '-------------------------------------'
        ]
        for item in menu_castrado:
            print (item)
        
        opcao = self.le_numero_inteiro([1,2])
        return opcao

    def menu_organizador_cadastrado(self):
        menu_castrado = [
            '-------------------------------------',
            'Cadastrar novo evento - 1',
            'Mostrar o seu histórico de eventos - 2',
            'Criar novo local para eventos - 3',
            '-------------------------------------'
        ]
        for item in menu_castrado:
            print (item)
        
        opcao = self.le_numero_inteiro([1,2,3])
        return opcao
