import PySimpleGUI as sg


class TelaPedeCPF:
    def __init__(self):
        self.__window = None
        self.init_components(
            [
                [sg.Text("Por favor, digite o seu CPF: ")],
                [sg.Text("CPF: ", size=(15, 1)), sg.InputText()],
                [sg.Submit("Entrar")],
            ]
        )

    def init_components(self, layout):
        self.__window = sg.Window("Tela de acesso ao menu de comprador").Layout(layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        return button, values

    def pede_cpf(self):
        button, values = self.abrir_tela()
        while True:
            if button is None:
                return
            return values[0]

    def fechar_tela(self):
        self.__window.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
