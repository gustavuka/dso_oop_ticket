from entidade.comprador import Comprador
from limite.tela_comprador import TelaComprador
from inicia_for_tests import IniciaForTests
from MVC.entidade.comprador_dao import CompradorDAO
from MVC.entidade.dao import DAO


class ControladorComprador:
    def __init__(self, controlador_evento):
        self.__tela_comprador = TelaComprador()
        self.__lista_compradores = []
        self.__controlador_evento = controlador_evento
        self.__comprador_dao = CompradorDAO()
        # Cria alguns usuários de testes para executar as funcionalidades do programa
        IniciaForTests().comprador_teste(Comprador, self.__lista_compradores)

    @property
    def tela_comprador(self):
        return self.__tela_comprador

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    #@property
    #def comprador_dao(self):
    #    return self.__comprador_dao.get_all()

    #@property
    #def comprador_dao(self):
    #    return self.__comprador_dao

    def confere_cpf_existe(self, cpf):
        for item in self.comprador_dao:
            if item.cpf == cpf:
                return item
        return False

    def adicionar_comprador(self):
        info_comprador = self.tela_comprador.dados()
        novo_comprador = Comprador(
            info_comprador["Nome"],
            info_comprador["Endereco"],
            info_comprador["Telefone"],
            info_comprador["Email"],
            info_comprador["cpf"],
            info_comprador["Idade"],
        )
        self.__comprador_dao.add(novo_comprador)
        #self.comprador_dao.add(novo_comprador.cpf, novo_comprador)
        print("Novo comprador cadastrado! Bem vindo " + novo_comprador.nome + "!")

    def alterar_dados(self):
        cpf = self.tela_comprador.pede_cpf()
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            nova_info_comprador = self.tela_comprador.dados()
            usuario.nome = nova_info_comprador["Nome"]
            usuario.endereco = nova_info_comprador["Endereco"]
            usuario.telefone = nova_info_comprador["Telefone"]
            usuario.email = nova_info_comprador["Email"]
            usuario.cpf = nova_info_comprador["cpf"]
            usuario.idade = nova_info_comprador["Idade"]
            print("Atualizacao de dados completa!")
            print(usuario.nome, usuario.idade)
            print(self.__comprador_dao)
        else:
            print("Falha na atualização")

    def mostrar_compradores_cadastrados(self):
        self.tela_comprador.print_lista(self.comprador_dao)

    def comprar_ingressos(self):
        cpf = self.tela_comprador.pede_cpf()
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            eventos = self.controlador_evento.eventos
            opcao = self.tela_comprador.selecionar_eventos(eventos)
            if opcao:
                evento_selecionado = opcao
                confirmacao = self.tela_comprador.confirmacao_de_compra(
                    evento_selecionado
                )
                if confirmacao:
                    usuario.lista_ingressos.append(evento_selecionado)
            else:
                print("Algum erro ocorreu")
        else:
            self.tela_comprador.usuario_inexistente()

    def mostrar_ingressos(self):
        cpf = self.tela_comprador.pede_cpf()
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            for item in usuario.lista_ingressos:
                print(item)
