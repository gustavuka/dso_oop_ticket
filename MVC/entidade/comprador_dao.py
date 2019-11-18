from MVC.entidade.comprador import Comprador
from MVC.entidade.dao import DAO


class CompradorDAO(DAO):

    def __init__(self):
        super().__init__('compradores.pkl')

    def add(self, comprador: Comprador):
        if isinstance(comprador.cpf, str) and (comprador is not None) and isinstance(comprador, Comprador):
            super().add(comprador.cpf, comprador)
