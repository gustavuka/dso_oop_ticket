import PySimpleGUI as sg


class AbstractTela:
    def __init__(self):
        sg.change_look_and_feel("DarkBlue")
        sg.set_options(font=(12), text_justification="center")


class TelaInicial(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.Button("Comprador", size=(30, 2))],
            [sg.Button("Organizador", size=(30, 2))],
            [sg.Button("Administrador", size=(30, 2))],
            [sg.Button("Sair", size=(30, 2))],
        ]

    def screen(self):
        window = sg.Window(
            "Login", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            button, values = window.read()
            if button == "Comprador":
                window.close()
                return 1
            elif button == "Organizador":
                window.close()
                return 2
            elif button == "Administrador":
                window.close()
                return 3
            else:
                break
        window.close()
        exit(0)


class TelaLogin(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.InputText("cpf/cnpj", size=(30, 3), key="identidade")],
            [sg.Button("Login", size=(30, 2))],
            [sg.Button("Cadastrar", size=(30, 2))],
            [sg.Button("Sair", size=(30, 2))],
        ]

    def screen(self):
        window = sg.Window(
            "Login", self.layout, size=(400, 400), element_justification="center"
        )

        while True:
            button, values = window.read()
            if button == "Login":
                id = values["identidade"]
                window.close()
                return id
            elif button == "Cadastrar":
                window.close()
                return "cadastrar"
            else:
                return "sair"
                break
        window.close()
        exit(0)


class TelaCadastroOrganizador(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.InputText("Nome", size=(30, 3), key="nome")],
            [sg.InputText("Telefone", size=(30, 3), key="telefone")],
            [sg.InputText("CNPJ", size=(30, 3), key="cnpj")],
            [sg.InputText("Email", size=(30, 3), key="email")],
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
                    cnpj = values["cnpj"]
                    email = values["email"]
                    endereco = values["endereco"]
                    window.close()
                    return [name, telefone, cnpj, email, endereco]
                except:
                    print("Error")
            else:
                break
        window.close()
        exit(0)


class TelaInicialOganizador(AbstractTela):
    def __init__(self):
        super().__init__()
        self.layout = [
            [sg.Text("Painel do Organizador", size=(30, 2))],
            [sg.Button("Cadastrar Evento", size=(30, 2))],
            [sg.Button("Histórico de Eventos", size=(30, 2))],
            [sg.Button("Criar Local", size=(30, 2))],
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
            elif event == "Histórico de Eventos":
                window.close()
                return "historico"
                new = TelaLista(a, TelaInicialOganizador)
            elif event == "Cadastrar Evento":
                window.close()
                return "cadastrar"
            elif event == "Criar Local":
                window.close()
                return "criar"
            elif event == "Editar Dados":
                window.close()
                return "editar"
            elif event == "Sair":
                window.close()
                break
        window.close()


class TelaLista:
    """Abre uma tela que lista itens, ao clicar ok volta para a tela selecionada"""

    def __init__(self, lista=[]):
        self.lista = lista
        sg.PopupScrolled(*self.lista, title="Lista")


class TelaCadastroEvento:
    def __init__(self, locais):
        self.locais = [local.nome for local in locais]
        self.layout = [
            [sg.InputText("Título", key="titulo", size=(35, 150))],
            [sg.InputText("Categoria", key="categoria", size=(35, 4))],
            [sg.InputText("Data", key="data", size=(35, 4))],
            [
                sg.InputCombo(
                    self.locais, default_value="Local", size=(29, 4), key="local"
                ),
                sg.Button("+", bind_return_key=True),
            ],
            [sg.InputText("Valor", key="valor", size=(35, 4))],
            [sg.InputText("Classificação", key="classificacao", size=(35, 4))],
            [
                sg.Submit("Cadastrar", bind_return_key=True),
                sg.Button("Voltar", bind_return_key=True),
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
                    titulo = values["titulo"]
                    categoria = values["categoria"]
                    data = values["data"]
                    local = values["local"]
                    valor = values["valor"]
                    classificacao = values["classificacao"]
                    window.close()
                    return [titulo, categoria, data, local, valor, classificacao]
                except:
                    print("Erro")
            elif button == "+":
                window.close()
                return "plus"
            elif button == "Voltar":
                window.close()
                break
            elif button == None:
                break
        window.close()
        exit(0)


class TelaCadastroLocal:
    def __init__(self):
        self.layout = [
            [sg.InputText("Nome do Local", key="nome", size=(35, 150))],
            [sg.InputText("Endereço", key="endereco", size=(35, 4))],
            [sg.InputText("Capacidade", key="capacidade", size=(35, 4))],
            [
                sg.Submit("Cadastrar", bind_return_key=True),
                sg.Button("Voltar", bind_return_key=True),
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
                    nome = values["nome"]
                    endereco = values["endereco"]
                    capacidade = values["capacidade"]
                    return [nome, endereco, capacidade]
                    window.close()
                except:
                    print("Error")
            elif button == "Voltar":
                window.Close()
                break
            else:
                break
        window.close()
        exit(0)


class TelaPopUp:
    def __init__(self, message):
        sg.Popup(message)
