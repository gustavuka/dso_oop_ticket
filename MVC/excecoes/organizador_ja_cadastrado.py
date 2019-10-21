class OrganizadorJaCadastrado(Exception):
    def __init__(self):
        super().__init__("Organizador já cadastrado!")
