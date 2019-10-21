class CompradorJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Comprador já cadastrado!")
