class TelaControladorPrincipal:
    def __init__(self):
        self.__menu_table = [
            'Entrar com um usuário existente: (x)',
            'Cadastrar novo usuário: (n)',
            'Editar usuário: (e)',
        ]
    
    @property
    def menu_table(self):
        return self.__menu_table

    def menu_principal(self):
        print ('Bem vindo ao dso ticket!')
        opcao_ini = input('Gostaria de utilizar o sistema como comprador(c) ou organizador(o)?')
        for item in self.menu_table:
            print (item)

        opcao_sec = input()
        return (opcao_ini, opcao_sec)
