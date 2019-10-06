from entidade.comprador import Comprador
from controle.controlador_comprador import ControladorComprador

class TelaComprador:

    controlador = ControladorComprador()

    def novo_comprador(self):
        nome = input("Nome: ")
        endereco = input("Endereco: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cpf = input("cpf: ")
        idade = input("Idade: ")

        novo_comprador = Comprador(nome, endereco, telefone, email, cpf, idade)
        controlador.adicionar_comprador(novo_comprador)

    def alterar_dados(self, cpf):
        #precisa ser feito >
        #acessar lista de compradores e selecionar comprador pelo cpf

        opcao = input('Qual item você gostaria de editar? Nome(n), Endereco(e), \
        Telefone(t), Email(@), cpf(c), Idade(i).')
        selecionado = controlador.opcoes[opcao]

        novo_valor = input('Qual o novo valor?')

        comprador.selecionado = novo_valor
