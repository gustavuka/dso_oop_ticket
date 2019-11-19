import PySimpleGUI as sg


class TelaCompradorCadastrado:
    def __init__(self):
        self.__window = None
        self.init_components([
            [sg.InputCombo(('Comprar ingresso',
                            'Mostrar histórico de ingressos',
                            'Sair'),
                           size=(100, 50))],
            [sg.Submit('Selecionar')]
        ])

    def init_components(self, layout):
        self.__window = sg.Window('Menu de comprador! Escolha uma opção abaixo: ').Layout(
            layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        return button, values

    def menu_comprador_cadastrado(self):
        button, values = self.abrir_tela()
        while True:
            if button is None:
                return
            if values[0] == 'Comprar ingresso':
                return 1
            elif values[0] == 'Mostrar histórico de ingressos':
                return 2
            elif values[0] == 'Sair':
                return 3

    def fechar_tela(self):
        self.__window.Close()

    def mostrar_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)