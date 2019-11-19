import PySimpleGUI as sg


class MenuPrincipal:
    def __init__(self):
        self.__window = None
        self.init_components([
            [sg.InputCombo(('Entrar com um usuário existente',
                            'Cadastrar novo usuário',
                            'Editar usuário',
                            'Mostrar todos os eventos cadastrados',
                            'Mostrar informações do evento',
                            'Sair'),
                           size=(100, 50))],
            [sg.Submit('Selecionar')]
        ])

    def init_components(self, layout):
        self.__window = sg.Window('Menu de cliente! Escolha uma opção abaixo: ').Layout(
            layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        return button, values

    def menu_cliente(self):
        button, values = self.abrir_tela()
        while True:
            if button is None:
                return
            if values[0] == 'Entrar com um usuário existente':
                return 1
            elif values[0] == 'Cadastrar novo usuário':
                return 2
            elif values[0] == 'Editar usuário':
                return 3
            if values[0] == 'Mostrar todos os eventos cadastrados':
                return 4
            elif values[0] == 'Mostrar informações do evento':
                return 5
            elif values[0] == 'Sair':
                return 6

    def fechar_tela(self):
        self.__window.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
