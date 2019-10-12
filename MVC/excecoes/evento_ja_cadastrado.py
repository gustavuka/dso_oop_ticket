class EventoJaCadastrado(Exception):
    
    def __init__(self):
        super().__init__("Evento já cadastrado!")
