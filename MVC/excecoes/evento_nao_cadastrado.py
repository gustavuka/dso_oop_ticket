class EventoNaoCadastrado(Exception):
    def __init__(self):
        super().__init__("Evento não cadastrado!")
