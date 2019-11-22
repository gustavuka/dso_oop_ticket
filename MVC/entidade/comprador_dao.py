from entidade.comprador import Comprador
from entidade.dao import DAO


class CompradorDAO(DAO):
    def __init__(self):
        super().__init__("compradores.pkl")

    def add(self, comprador: Comprador):
        if (
            isinstance(comprador.cpf, str)
            and (comprador is not None)
            and isinstance(comprador, Comprador)
        ):
            super().add(comprador.cpf, comprador)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
