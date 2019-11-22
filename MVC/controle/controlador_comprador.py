from entidade.comprador import Comprador
from limite.tela_comprador import TelaComprador
from inicia_for_tests import IniciaForTests
from entidade.comprador_dao import CompradorDAO
from limite.tela_cadastro_comprador import TelaCadastroComprador
from limite.tela_mostrar_eventos import TelaMostrarEventos
from limite.tela_comprador_gui import TelaCompraEventos, TelaConfirmacao
from limite.tela_organizador_gui import TelaPopUp


class ControladorComprador:
    def __init__(self, controlador_evento):
        self.__tela_comprador = TelaComprador()
        self.__lista_compradores = []
        self.__controlador_evento = controlador_evento
        self.__comprador_dao = CompradorDAO()
        self.__tela_cadastro_comprador = TelaCadastroComprador()
        # self.__tela_mostrar_eventos = TelaMostrarEventos()
        # Cria alguns usuários de testes para executar as funcionalidades do programa
        # IniciaForTests().comprador_teste(Comprador, self.__lista_compradores)

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
        return self.__comprador_dao.get_all()

    def confere_cpf_existe(self, cpf):
        for comprador in self.lista_compradores:
            if comprador.cpf == cpf:
                return comprador
        return False

    def adicionar_comprador(self, dados):
        novo_comprador = Comprador(
            dados[0], dados[5], dados[1], dados[3], dados[2], dados[4]
        )
        self.__comprador_dao.add(novo_comprador)
        return self.__comprador_dao.get(novo_comprador.cpf).cpf

    #FAZER
    def alterar_dados(self, cpf, dados):
        comprador = self.confere_cpf_existe(cpf)

        if comprador:
            comprador.nome = (dados[0],)
            comprador.endereco = dados[5]
            comprador.telefone = dados[1]
            comprador.email = dados[3]
            comprador.cpf = cpf
            comprador.idade = dados[4]
            print("Atualizacao de dados completa!")
            print(comprador.nome)
        else:
            print("Error")
        print(comprador)
        return comprador

    def comprar_ingressos(self, cpf):
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            eventos = self.controlador_evento.eventos
            opcao = TelaCompraEventos(eventos).screen()
            print(eventos)
            for item in eventos:
                if item.titulo == opcao:
                    evento_selecionado = item
            confirmacao = TelaConfirmacao(evento_selecionado).screen()
            if confirmacao:
                usuario.lista_ingressos.append(evento_selecionado)
                TelaPopUp("Compra efetuada, parabéns.")
            else:
                print("Algum erro ocorreu")
        else:
            self.tela_comprador.usuario_inexistente()

    def mostrar_ingressos(self, cpf):
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            return usuario.lista_ingressos
