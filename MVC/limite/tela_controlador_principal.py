import PySimpleGUI as sg


class TelaControladorPrincipal:
    #print("Bem vindo ao dso ticket!")
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.InputCombo(('Comprador', 'Organizador', 'Administrador', 'Sair'), size=(100, 50))],
            [sg.Submit()]
        ]
        self.__window = sg.Window('Bem vindo ao DSO Ticket! Escolha o perfil com o qual deseja acessar: ').Layout(layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        return button, values

    def fechar_tela(self):
        self.__window.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def le_numero_inteiro(self, inteiros_validos=None):
        while True:
            valor_lido = input()
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Por favor entre com um valor válido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)

    def menu_inicial(self):
        button, values = self.abrir_tela()
        print(button)
        print(values)
        while True:
            if button is None:
                return
            if values[0] == 'Comprador':
                return 1
            elif values[0] == 'Organizador':
                return 2
            elif values[0] == 'Administrador':
                return 3
        #print("Como gostaria de utilizar o sistema?")
        #menu_inicial = [
        #    "-------------------------------------",
        #    "Comprador - 1",
        #    "Organizador - 2",
        #    "Administrador - 3",
        #    "Sair - 4",
        #    "-------------------------------------",
        #]
        #for item in menu_inicial:
        #    print(item)
        #opcao = self.le_numero_inteiro([1, 2, 3, 4])

    def menu_principal(self):
        menu_table = [
            "-------------------------------------",
            "Entrar com um usuário existente - 1",
            "Cadastrar novo usuário - 2",
            "Editar usuário - 3",
            "Mostrar todos os eventos cadastrados - 4",
            "Mostrar informações do evento - 5",
            "Sair - 6",
            "-------------------------------------",
        ]
        for opcao_menu in menu_table:
            print(opcao_menu)
        opcao = self.le_numero_inteiro([1, 2, 3, 4, 5, 6])
        return opcao

    def menu_comprador_cadastrado(self):
        menu_castrado = [
            "-------------------------------------",
            "Comprar ingresso - 1",
            "Mostrar histórico de ingressos - 2",
            "Sair - 3",
            "-------------------------------------",
        ]
        for opcao_menu in menu_castrado:
            print(opcao_menu)

        opcao = self.le_numero_inteiro([1, 2, 3])
        return opcao

    def menu_organizador_cadastrado(self):
        menu_organizador_cadastrado = [
            "-------------------------------------",
            "Cadastrar novo evento - 1",
            "Mostrar o seu histórico de eventos - 2",
            "Criar novo local para eventos - 3",
            "Sair - 4",
            "-------------------------------------",
        ]
        for item in menu_organizador_cadastrado:
            print(item)
        opcao = self.le_numero_inteiro([1, 2, 3, 4])
        return opcao

    def menu_administrador(self):
        menu_administrador = [
            "-------------------------------------",
            "Listar organizadores cadastrados - 1",
            "Listar compradores cadastrados - 2",
            "Sair - 3",
            "-------------------------------------",
        ]
        for item in menu_administrador:
            print(item)
        opcao = self.le_numero_inteiro([1, 2, 3])
        return opcao
