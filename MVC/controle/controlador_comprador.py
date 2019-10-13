from entidade.comprador import Comprador
from limite.tela_comprador import TelaComprador


class ControladorComprador:
    def __init__(self):
        self.__tela_comprador = TelaComprador()
        self.__lista_compradores = []

    @property
    def tela_comprador(self):
        return self.__tela_comprador
    
    @property
    def lista_compradores(self):
        return self.__lista_compradores

    @lista_compradores.setter
    def lista_compradores(self, lista_compradores):
        self.__lista_compradores = lista_compradores

    def confere_cpf_existe(self, cpf):
        for item in self.lista_compradores:
            if item.cpf == cpf:
                return item
            else:
                return False        

    def adicionar_comprador(self):
        info_comprador = (TelaComprador().novo_comprador())

        novo_comprador = Comprador(
            info_comprador["Nome"],
            info_comprador["Endereco"],
            info_comprador["Telefone"],
            info_comprador["Email"],
            info_comprador["cpf"],
            info_comprador["Idade"],
        )
        self.lista_compradores.append(novo_comprador)
        print ("Novo comprador cadastrado! Bem vindo " + novo_comprador.nome + "!")
        print (self.lista_compradores)

    def alterar_dados(self):
        cpf = self.tela_comprador.pede_cpf()        
        usuario = self.confere_cpf_existe(cpf)

        if usuario:
            nova_info_comprador = self.tela_comprador.alterar_dados()
            usuario.nome = nova_info_comprador["Nome"]
            usuario.endereco = nova_info_comprador["Endereco"]
            usuario.telefone = nova_info_comprador["Telefone"]
            usuario.email = nova_info_comprador["Email"]
            usuario.cpf = nova_info_comprador["cpf"]
            usuario.idade = nova_info_comprador["Idade"]
            print ("Atualizacao de dados completa!")
            print (usuario.nome, usuario.idade)
            print (self.lista_compradores)
        else:
            print ("deu ruim")

    def mostrar_usuarios_cadastrados(self):
        self.tela_comprador.print_lista(self.lista_compradores)

    def comprar_ingressos(self):
        cpf = self.tela_comprador.pede_cpf()
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            # evento_selecionado = tela_comprador.mostrar_eventos()
            evento_selecionado = "showzao maneiro"
            confirmacao = self.tela_comprador.confirmacao_de_compra(evento_selecionado)
            if confirmacao:
                usuario.lista_ingressos.append(evento_selecionado)
        else:
            self.tela_comprador.usuario_inexistente()

    def mostrar_ingressos(self):
        cpf = self.tela_comprador.pede_cpf()
        usuario = self.confere_cpf_existe(cpf)
        if usuario:
            for item in usuario.lista_ingressos:
                print (item)
