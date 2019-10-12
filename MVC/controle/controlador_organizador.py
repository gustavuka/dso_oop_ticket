from MVC.entidade.cliente import Cliente


class ControladorOrganizador:

    def __init__(self, nome: str, endereco: str, telefone: str, email: str, cnpj: str):
        super().__init__(nome, endereco, telefone, email)
        self.__cnpj = cnpj
        self.__organizadores = []
        self.__eventos_organizados = []


    def cadastra_organizador(self, nome: str, endereco: str, telefone: str, email: str, cnpj: str):
        pass

    def lista_eventos_organizados(self, cnpj: str):
        pass

    def cria_evento(self):
        pass

    def lista_eventos_organizados(self):
        pass

    def mostra_relatorio_compras(self):
        pass

    def mostra_informacoes_evento(self, titulo_evento: str):
        pass