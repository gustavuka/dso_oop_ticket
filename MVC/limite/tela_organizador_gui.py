import PySimpleGUI as sg

class AbstractTela:
    def __init__(self):
        sg.change_look_and_feel('DarkAmber')
        sg.set_options(font=(12), text_justification="center")


class TelaInicialOganizador(AbstractTela):

    def __init__(self):
        super().__init__()
        layout = [
            [sg.Text('Painel do Organizador', size=(30,2))],
            [sg.Button('Cadastrar Evento', size=(30,2))],
            [sg.Button('Histórico de Eventos', size=(30,2))],
            [sg.Button('Criar Local', size=(30,2))],
            [sg.Button('Voltar', size=(30,2))],
            ]
        
        window = sg.Window('Organizador', layout, size=(400, 400), element_justification='center')

        while True:
            event, value = window.read()
            print (event)
            if event in (None,):
                break
            elif event == "Histórico de Eventos":
                a=["Evento 1", "Evento 1", "Evento 1", "Evento 1"]
                window.close()
                new = TelaLista(a, TelaInicialOganizador)
            elif event == "Cadastrar Evento":
                window.close()
                TelaCadastroEvento()
            elif event == "Criar Local":
                window.close()
                TelaCadastroLocal()
        window.close()

class TelaLista:
    """Abre uma tela que lista itens, ao clicar ok volta para a tela selecionada"""
    def __init__(self, lista, voltar=""):
        self.lista = lista
        self.voltar = voltar
        sg.PopupScrolled(*self.lista, title="Lista")
        if voltar != "": 
            voltar()

class TelaCadastroOrganizador:
    def __init__(self):
        layout = [ 
            [sg.In(size=(30,3), key='nome')],
            [sg.In(size=(30,3), key='telefone')],
            [sg.In(size=(30,3), key='cnpj')],
            [sg.In(size=(30,3), key='email')],
            [sg.In(size=(30,3), key='endereco')],
            [sg.ReadButton('Cadastrar', bind_return_key=True), sg.Button('Sair', bind_return_key=True)]
            ]

        window = sg.Window('Organizador', layout, size=(400, 400), element_justification='center')

        while True:
            button, values = window.read()
            if button is not None:
                try:
                    name = values["nome"]
                    telefone = values["telefone"]
                    cnpj = values["cnpj"]
                    email = values["email"]
                    endereco = values["endereco"]
                    print (name, telefone, cnpj, email, endereco)
                except:
                    print ("ajsdnkj")             
            else:
                break
        window.close()

class TelaCadastroEvento:
    def __init__(self):
        layout = [ 
            [sg.InputText('Título', key='titulo', size=(35,150))],
            [sg.InputText("Categoria", key='categoria', size=(35,4))],
            [sg.InputText("Data", key='data', size=(35,4))],
            [sg.InputCombo(["Locais", "locaiscs"], default_value="Local", size=(29, 4), key='local'), sg.Button('+', bind_return_key=True)],
            [sg.InputText("Valor", key='valor', size=(35,4))],
            [sg.InputText("Classificação", key='classificacao', size=(35,4))],
            [sg.Submit('Cadastrar', bind_return_key=True), sg.Button('Voltar', bind_return_key=True)]
            ]

        window = sg.Window('Organizador', layout, size=(400, 400), element_justification='center')

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
                    print (titulo, categoria, data, local, valor, classificacao)
                except:
                    print ("ajsdnkj")
            elif button == "+":
                window.close()
                TelaCadastroLocal()
            elif button == "Voltar":
                window.Close()
                TelaInicialOganizador()
            else:
                break
        window.close()

class TelaCadastroLocal:
    def __init__(self):
        layout = [ 
            [sg.InputText('Nome do Local', key='nome', size=(35,150))],
            [sg.InputText("Endereço", key='endereco', size=(35,4))],
            [sg.InputText("Capacidade", key='capacidade', size=(35,4))],
            [sg.Submit('Cadastrar', bind_return_key=True), sg.Button('Voltar', bind_return_key=True)]
            ]

        window = sg.Window('Organizador', layout, size=(400, 400), element_justification='center')

        while True:
            button, values = window.read()
            if button == "Cadastrar":
                try:
                    nome = values["nome"]
                    endereco = values["endereco"]
                    capacidade = values["capacidade"]
                    print (nome, endereco, capacidade)
                except:
                    print ("ajsdnkj")
            elif button == "Voltar":
                window.Close()
                TelaInicialOganizador()
            else:
                break
        window.close()


TelaInicialOganizador()