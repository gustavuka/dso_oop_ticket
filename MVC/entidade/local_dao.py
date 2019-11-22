from entidade.evento import Evento
from entidade.dao import DAO


class LocalDAO(DAO):
    def __init__(self):
        super().__init__("local.pkl")

    def add(self, local: Local):
        if (
            isinstance(local.titulo, str)
            and (evento is not None)
            and isinstance(local, Local)
        ):
            super().add(local.titulo, local)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)