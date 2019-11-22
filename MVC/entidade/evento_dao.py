from entidade.evento import Evento
from entidade.DAO import DAO


class CompradorDAO(DAO):
    def __init__(self):
        super().__init__("compradores.pkl")

    def add(self, evento: Evento):
        if (
            isinstance(evento.titulo, str)
            and (evento is not None)
            and isinstance(evento, Evento)
        ):
            super().add(evento.titulo, evento)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)