from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.lista_luoghi = None
        self.dizionario_luoghi = None
        self.grafo = nx.Graph()

    def get_luoghi(self):
        if self.lista_luoghi is None:
            self.lista_luoghi = DAO.read_all_luoghi()

        if self.dizionario_luoghi is None:
            for luogo in self.lista_luoghi:
                self.dizionario_luoghi[luogo.id] = luogo

        return self.lista_luoghi

    def crea_grafo(self):
        self.get_luoghi()
        nodi = self.lista_luoghi
        for n in nodi:
            self.grafo.add_node(n)
