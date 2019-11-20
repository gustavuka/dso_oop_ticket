import PySimpleGUI as gui

class TelaInicialOganizador:

    def __init__(self):
        gui.change_look_and_feel('DarkBlue')
        layout = [
            [gui.Text('Painel do Organizador', size=(30,2))],
            [gui.Button('Listar meus Eventos', size=(30,2))],
            [gui.Button('Mostrar Eventos', size=(30,2))],
            [gui.Button('Alterar', size=(30,2))],
            [gui.Button('Voltar', size=(30,2))],
            ]
        
        window = gui.Window('Organizador', layout)

        while True:
            event, value = window.read()
            print (event)
            if event in (None,):
                break
            elif event == "Listar meus Eventos":
                window.close()
                new = NovaTela()

        window.close()

class NovaTela:

    def __init__(self):
        gui.change_look_and_feel('DarkBlue')
        layout = [
            [gui.Text('Pxasxsar', size=(30,2))],
            [gui.Button('Lxasxs', size=(30,2))],
            [gui.Button('xasxsa Eventos', size=(30,2))],
            [gui.Button('Alteasdsarar', size=(30,2))],
            [gui.Button('xxxx', size=(30,2))],
            ]
        
        window = gui.Window('Organizador', layout)
        while True:
            event, value = window.read()
            print (event)
            if event in (None,):
                break
        window.close()         

app = TelaInicialOganizador()