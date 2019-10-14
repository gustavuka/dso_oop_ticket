class NenhumLocalCadastrado(Exception):

    def __init__(self):
        super().__init__("Nenhum local cadastrado. Por favor, cadastre um novo local!")