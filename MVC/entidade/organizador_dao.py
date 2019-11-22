from entidade.organizador import Organizador
from entidade.dao import DAO


class OrganizadorDAO(DAO):
    def __init__(self):
        super().__init__("organizadores.pkl")

    def add(self, organizador: Organizador):
        if (
                isinstance(organizador.cnpj, str)
                and (organizador is not None)
                and isinstance(organizador, Organizador)
        ):
            super().add(organizador.cnpj, organizador)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
