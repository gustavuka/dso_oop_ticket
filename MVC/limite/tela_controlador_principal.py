class TelaControladorPrincipal:
    print ('Bem vindo ao dso ticket!')

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

        opcao = input()
        return opcao

    def menu_principal(self):
        menu_table = [
            '-------------------------------------',
            'Entrar com um usuário existente - 1',
            'Cadastrar novo usuário - 2',
            'Editar usuário - 3',
            'Listar usuários - 4',
            'Sair - 5',
            '-------------------------------------'
        ]
        for item in menu_table:
            print (item)

        opcao = input()
        return opcao
    
    def menu_usuario_cadastrado(self):
        menu_castrado = [
            '-------------------------------------',
            'Comprar ingresso - 1',
            'Mostrar histórico de ingressos - 2',
            '-------------------------------------'
        ]
        for item in menu_castrado:
            print (item)
        
        opcao = input()
        return opcao