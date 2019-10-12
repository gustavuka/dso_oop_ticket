class ComandoInvalido(Exception):

    def __init__(self):
        super().__init__("Comando inválido!")
    
    def capacidade_excedida(self):
        super().__init__("Ingressos esgotados para este evento!")
    
    def numero_nao_inteiro(self):
        super().__init__("Digite um valor inteiro!")
    
    def numero_negativo(self):
        super().__init__("Não pode ser um valor negativo!")
