import PySimpleGUI as sg


class AbstractTela:
    def __init__(self):
        sg.change_look_and_feel("DarkBlue")
        sg.set_options(font=(12), text_justification="center")


class TelaCadastroComprador(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.InputText("Nome", size=(30, 3), key="nome")],
            [sg.InputText("Telefone", size=(30, 3), key="telefone")],
            [sg.InputText("CPF", size=(30, 3), key="cpf")],
            [sg.InputText("Email", size=(30, 3), key="email")],
            [sg.InputText("Idade", size=(30, 3), key="idade")],
            [sg.InputText("Endereco", size=(30, 3), key="endereco")],
            [
                sg.ReadButton("Cadastrar", bind_return_key=True),
                sg.Button("Sair", bind_return_key=True),
            ],
        ]

    def screen(self):
        window = sg.Window(
            "Organizador", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            button, values = window.read()
            if button == "Cadastrar":
                try:
                    name = values["nome"]
                    telefone = values["telefone"]
                    cpf = values["cpf"]
                    email = values["email"]
                    idade = values["idade"]
                    endereco = values["endereco"]
                    window.close()
                    return [name, telefone, cpf, email, idade, endereco]
                except:
                    print("Error")
            else:
                break
        window.close()
        exit(0)


class TelaInicialComprador(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.Text("Painel do Comprador", size=(30, 2))],
            [sg.Button("Comprar Ingressos", size=(30, 2))],
            [sg.Button("Histórico de Ingressos", size=(30, 2))],
            [sg.Button("Editar Dados", size=(30, 2))],
            [sg.Button("Sair", size=(30, 2))],
        ]

    def screen(self):
        window = sg.Window(
            "Organizador", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            event, value = window.read()
            if event in (None,):
                window.close()
                exit(0)
                break
            elif event == "Histórico de Ingressos":
                window.close()
                return "historico"
            elif event == "Comprar Ingressos":
                window.close()
                return "comprar"
            elif event == "Sair":
                window.close()
                exit(0)
            elif event == "Editar Dados":
                window.close()
                return "editar"
                break
        window.close()


class TelaCompraEventos:
    def __init__(self, lista):
        self.lista = lista
        self.lista = [item.titulo for item in self.lista]
        self.layout = [
            [sg.InputCombo(self.lista, size=(100, 50))],
            [sg.Submit("Selecionar")],
        ]

    def screen(self):
        window = sg.Window(
            "Organizador", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            event, value = window.read()
            if event in (None,):
                window.close()
                exit(0)
                break
            elif event == "Selecionar":
                window.close()
                return value[0]
        window.close()


class TelaConfirmacao:
    def __init__(self, evento):
        self.evento = evento
        self.layout = [
            [sg.Text("Confirmação de Compra!", size=(30, 2))],
            [sg.Text(self.evento.titulo, size=(30, 2))],
            [sg.Button("Confirmar", size=(30, 2))],
            [sg.Button("Cancelar", size=(30, 2))],
        ]

    def screen(self):
        window = sg.Window(
            "Organizador", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            event, value = window.read()
            if event in (None,):
                window.close()
                exit(0)
                break
            elif event == "Confirmar":
                window.close()
                return True
            elif event == "Cancelar":
                window.close()
                return False
        window.close()
