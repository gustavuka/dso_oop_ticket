class ControladorComprador:
    def __init__(self):
        self.__lista_organizadores = []

    @property
    def lista_organizadores(self):
        return self.__lista_organizadores

    @lista_organizadores.setter
    def lista_organizadores(self, lista_organizadores):
        self.__lista_organizadores = lista_organizadores    

    def adicionar_organizador(self):
        info_organizador = (TelaOrganizador().novo_organizador())

        # novo_organizador = Organizador(
        #     info_comprador["Nome"],
        #     info_comprador["Endereco"],
        #     info_comprador["Telefone"],
        #     info_comprador["Email"],
        #     info_comprador["cpf"],
        #     info_comprador["Idade"],
        # )
        self.lista_organizadores.append(novo_organizador)
        print ("Novo orgnizador cadastrado! Bem vindo " + novo_organizador.nome + "!")
        print (self.lista_organizadores)

    def alterar_dados(self):
        cnpj, nova_info_organizador = (TelaOrganizador().alterar_dados())
        
        for item in self.lista_organizadores:
            if item.cnpj == cnpj:
                # item.nome = nova_info_organizador["Nome"]
                # item.endereco = nova_info_organizador["Endereco"]
                # item.telefone = nova_info_organizador["Telefone"]
                # item.email = nova_info_organizador["Email"]
                # item.cnpj = nova_info_organizador["cnpj"]
                # print ("Atualizacao de dados completa!")
                print (item.nome)
                print (self.lista_organizadores)
        