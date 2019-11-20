import PySimpleGUI as sg


class TelaCadastroComprador:
    def __init__(self):
        self.__window = None
        self.init_components([
            [sg.Text('Nome: ', size=(15, 1)), sg.InputText()],
            [sg.Text('Endereço: ', size=(15, 1)), sg.InputText()],
            [sg.Text('Telefone: ', size=(15, 1)), sg.InputText()],
            [sg.Text('Email: ', size=(15, 1)), sg.InputText()],
            [sg.Text('CPF: ', size=(15, 1)), sg.InputText()],
            [sg.Text('Idade: ', size=(15, 1)), sg.InputText()],
            [sg.Submit('Cadastrar usuário')]
        ])

    def init_components(self, layout):
        self.__window = sg.Window('Tela de cadastro').Layout(layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        return button, values

    def info_comprador(self):
        button, values = self.abrir_tela()
        while True:
            if button is None:
                return
            return values

    def fechar_tela(self):
        self.__window.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)