from limite.tela_controlador_principal import TelaControladorPrincipal


class TelaComprador:
    def le_numero_inteiro(self, inteiros_validos=None):
        while True:
            valor_lido = input()
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Por favor entre com um valor válido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)

    def tamanho_min_max(self, message):
        while True:
            valor_lido = input(message + ": ")
            try:
                if not len(valor_lido) >= 1 or not len(valor_lido) < 150:
                    raise ValueError
                return valor_lido
            except ValueError:
                print("Por favor entre com um valor válido")
                if valor_lido:
                    print("String com de 1 e 150 caracteres")

    def dados(self):
        info_cadastro = {
            "Nome": "",
            "Endereco": "",
            "Telefone": "",
            "Email": "",
            "cpf": "",
            "Idade": "",
        }
        for item in info_cadastro:
            info_cadastro[item] = self.tamanho_min_max(item)

        return info_cadastro

    def pede_cpf(self):
        cpf = input("Qual o cpf do comprador?\n")
        return cpf

    def mostrar_dados(self, cpf, lista_compradores):
        for item in lista_compradores:
            if item.cpf == cpf:
                for key, value in item.items():
                    print(key + ": " + value)

    def print_lista(self, lista_compradores):
        for comprador in lista_compradores:
            print("Nome: " + comprador.nome + "\n" + "Email: " + comprador.email + "\n")

    def usuario_inexistente(self):
        print("Usuario inexistente, por favor verfique o cpf.")

    def confirmacao_de_compra(self, evento):
        print("Confirmar a compra para o evento: " + str(evento.titulo))
        print("Confirmar - 1")
        print("Cancelar - 2")
        confirmacao = TelaControladorPrincipal.le_numero_inteiro([1, 2])
        if confirmacao == 1:
            print("Compra confirmada!")
            return True
        else:
            print("Compra cancelada!")
            return False

    def selecionar_eventos(self, lista):
        if len(lista) > 1:
            count = 1
            print("-------------------------------------")
            print("Por favor selecione o evento: ")
            for item in lista:
                print(item.titulo + ": " + str(count))
                count += 1
            print("-------------------------------------")
        else:
            raise NenhumLocalCadastrado()
        inteiros_validos = []
        for i in range(1, len(lista) + 1):
            inteiros_validos.append(i)
        opcao = self.le_numero_inteiro(inteiros_validos)
        opcao = lista[opcao - 1]
        return opcao
