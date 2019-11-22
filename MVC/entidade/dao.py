from abc import ABC
import pickle


class DAO(ABC):
    def __init__(self, datasource=""):
        self.datasource = datasource
        self.object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.object_cache, open(self.datasource, "wb"))

    def __load(self):
        self.object_cache = pickle.load(open(self.datasource, "rb"))

    def add(self, key, obj):
        self.object_cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.object_cache[key]
        except KeyError:
            pass
    
    def get_all(self):
        return self.object_cache.values()

    def remove(self, key):
        try:
            self.object_cache.pop(key)
            self.__dump()
        except KeyError:
            pass


