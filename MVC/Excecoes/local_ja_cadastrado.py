class LocalJaCadastrado(Exception):

    def __init__(self):
        super().__init__("Local já cadastrado!")