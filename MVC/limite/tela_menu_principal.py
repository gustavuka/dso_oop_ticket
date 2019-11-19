import PySimpleGUI as sg


class MenuPrincipal:
    def __init__(self):
        self.__window = None
        self.init_components([
            [sg.InputCombo(('Entrar com um usuário existente', 'Cadastrar novo usuário', 'Editar usuário', 'Mostrar todos os eventos cadastrados', 'Mostrar informações do evento', 'Sair'), size=(100, 50))],
            [sg.Submit('Selecionar')]
        ])

    def init_components(self, layout, perfil):
        self.__window = sg.Window('Menu de {}! Escolha uma opção abaixo: '.format(perfil)).Layout(
            layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        return button, values

    def fechar_tela(self):
        self.__window.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
