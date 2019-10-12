
# from controle.controlador_comprador import ControladorComprador

class TelaComprador:

    # self.controlador = ControladorComprador()

    def novo_comprador(self):
        info_cadastro = {
            'Nome': 'Nome',
            'Endereco': 'Endereco',
            'Telefone': 'Telefone',
            'Email': 'Email',
            'cpf': 'cpf',
            'Idade': 'Idade'
        }
        for item in info_cadastro:
            info_cadastro[item] = input(item + ": ")
        
        return info_cadastro

    def alterar_dados(self, cpf):
        #precisa ser feito >
        #acessar lista de compradores e selecionar comprador pelo cpf

        opcao = input('Qual item você gostaria de editar? Nome(n), Endereco(e), \
        Telefone(t), Email(@), cpf(c), Idade(i).')
        selecionado = controlador.opcoes[opcao]

        novo_valor = input('Qual o novo valor?')

        comprador.selecionado = novo_valor
