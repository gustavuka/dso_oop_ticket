from entidade.comprador import Comprador
from limite.tela_comprador import TelaComprador
from inicia_for_tests import IniciaForTests
from entidade.comprador_dao import CompradorDAO
from entidade.dao import DAO
from limite.tela_cadastro_comprador import TelaCadastroComprador
from limite.tela_mostrar_eventos import TelaMostrarEventos


class ControladorComprador:
    def __init__(self, controlador_evento):
        self.__tela_comprador = TelaComprador()
        self.__lista_compradores = []
        self.__controlador_evento = controlador_evento
        self.__comprador_dao = CompradorDAO()
        self.__tela_cadastro_comprador = TelaCadastroComprador()
        #self.__tela_mostrar_eventos = TelaMostrarEventos()
        # Cria alguns usuários de testes para executar as funcionalidades do programa
        IniciaForTests().comprador_teste(Comprador, self.__lista_compradores)

    @property
    def tela_comprador(self):
        return self.__tela_comprador

    @property
    def tela_cadastro_comprador(self):
        return self.__tela_cadastro_comprador

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    @property
    def lista_compradores(self):
        return self.__lista_compradores

    #@property
    #def tela_mostrar_eventos(self):
     #   return self.__tela_mostrar_eventos

    #@property
    #def comprador_dao(self):
    #    return self.__comprador_dao.get_all()

    #@property
    #def comprador_dao(self):
    #    return self.__comprador_dao

    def confere_cpf_existe(self, cpf):
        for item in self.lista_compradores:
            if item.cpf == cpf:
                return item
        return False

    def adicionar_comprador(self, info_comprador):
        novo_comprador = Comprador(
            info_comprador[0],
            info_comprador[1],
            info_comprador[2],
            info_comprador[3],
            info_comprador[4],
            info_comprador[5],
        )
        print (novo_comprador)
        #self.__comprador_dao.add(novo_comprador)
        #self.comprador_dao.add(novo_comprador.cpf, novo_comprador)
        self.lista_compradores.append(novo_comprador)

    def alterar_dados(self, comprador):
        nova_info_comprador = self.tela_cadastro_comprador.info_comprador()
        comprador.nome = nova_info_comprador[0]
        comprador.endereco = nova_info_comprador[1]
        comprador.telefone = nova_info_comprador[2]
        comprador.email = nova_info_comprador[3]
        comprador.cpf = nova_info_comprador[4]
        comprador.idade = nova_info_comprador[5]


    def mostrar_compradores_cadastrados(self):
        self.tela_comprador.print_lista(self.lista_compradores)

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
