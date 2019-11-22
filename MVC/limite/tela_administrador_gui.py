import PySimpleGUI as sg

class AbstractTela:
    def __init__(self):
        sg.change_look_and_feel("DarkBlue")
        sg.set_options(font=(12), text_justification="center")

class TelaAdministrador(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.Button("Listar Compradores", size=(30, 2))],
            [sg.Button("Listar Organizadores", size=(30, 2))],
            [sg.Button("Listar Eventos", size=(30, 2))],
            [sg.Button("Listar Locais", size=(30, 2))],
            [sg.Button("Sair", size=(30, 2))],
        ]

    def screen(self):
        window = sg.Window(
            "Login", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            button, values = window.read()
            if button == "Listar Compradores":
                window.close()
                return "compradores"
            elif button == "Listar Organizadores":
                window.close()
                return "organizadores"
            elif button == "Listar Eventos":
                window.close()
                return "eventos"
            elif button == "Listar Locais":
                window.close()
                return "locais"
            else:
                break
        window.close()
        exit(0)