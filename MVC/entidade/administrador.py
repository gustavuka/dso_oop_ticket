from entidade.cliente import Cliente


class Administrador(Cliente):
    def __init__(self, nome: str, endereco: str, telefone: str, email: str):
        super().__init__(nome, endereco, telefone, email)
        self.__codigo_administrador = codigo

    @property
    def codigo_administrador(self):
        return self.__codigo_administrador
