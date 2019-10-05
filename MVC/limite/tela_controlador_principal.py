class TelaControladorPrincipal:
    print ('hesad')

    def tela_inicial(self):
        option = input("Comprador ou organizador? (c/o)")
        if option == 'c':
            self.abrir_tela_comprador()
        elif option == 'o':
            self.abrir_tela_organizador()
        else:
            print ('Error')

    def abrir_tela_comprador(self):
        print ('Abrir tela compr.')

    def abrir_tela_organizador(self):
        print ('Abrir tela orgn.')
