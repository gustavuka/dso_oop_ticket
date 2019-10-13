from entidade.organizador import Organizador
from limite.tela_organizador import TelaOrganizador

class ControladorOrganizador:
    def __init__(self):
        self.__tela_organizador = TelaOrganizador()
        self.__lista_organizadores = []        

    @property
    def lista_organizadores(self):
        return self.__lista_organizadores
    
    @property
    def tela_organizador(self):
        return self.__tela_organizador

    @lista_organizadores.setter
    def lista_organizadores(self, lista_organizadores):
        self.__lista_organizadores = lista_organizadores
    
    def confere_cnpj_existe(self, cnpj):
        for item in self.lista_organizadores:
            if item.cnpj == cnpj:
                return item
            else:
                return False  

    def adicionar_organizador(self):
        info_organizador = (self.tela_organizador.novo_organizador())

        novo_organizador = Organizador(
            info_organizador["Nome"],
            info_organizador["Endereco"],
            info_organizador["Telefone"],
            info_organizador["Email"],
            info_organizador["cnpj"],
        )
        self.lista_organizadores.append(novo_organizador)
        print ("Novo orgnizador cadastrado! Bem vindo " + novo_organizador.nome + "!")
        print (self.lista_organizadores)

    def alterar_dados(self):
        cnpj = self.tela_organizador.pede_cnpj() 
        usuario = self.tela_organizador.confere_cnpj_existe(cnpj)
        
        if usuario:
            nova_info_organizador = self.tela_organizador.alterar_dados()
            usuario.nome = nova_info_organizador["Nome"]
            usuario.endereco = nova_info_organizador["Endereco"]
            usuario.telefone = nova_info_organizador["Telefone"]
            usuario.email = nova_info_organizador["Email"]
            usuario.cnpj = nova_info_organizador["cnpj"]
            print ("Atualizacao de dados completa!")
            print (usuario.nome)
            print (self.lista_organizadores)
        else:
            print ("deu ruim")
    
    def mostrar_organizadores_cadastrados(self):
        self.tela_organizador.print_lista(self.lista_organizadores)

    def cria_evento(self):
        pass

    def lista_eventos_organizados(self, cnpj: str):
        pass

    def mostra_relatorio_compras(self):
        pass

    def mostra_informacoes_evento(self, titulo_evento: str):
        pass
