from database.DAO import DAO
import networkx as nx

from model.sentiero import Sentiero


class Model:
    def __init__(self):
        self.lista_luoghi = None
        self.dizionario_luoghi = None
        self.grafo = nx.Graph()

    def get_luoghi(self):
        if self.lista_luoghi is None:
            self.lista_luoghi = DAO.read_all_luoghi()

        if self.dizionario_luoghi is None:
            self.dizionario_luoghi = {}
            for luogo in self.lista_luoghi:
                self.dizionario_luoghi[luogo.id] = luogo

        return self.lista_luoghi

    def crea_grafo(self):
        self.get_luoghi()
        nodi = self.lista_luoghi
        for n in nodi:
            self.grafo.add_node(n)

        sentieri = DAO.read_all_sentieri()
        for sentiero in sentieri:
            self.grafo.add_edge(self.dizionario_luoghi[sentiero.id_luogo_1], self.dizionario_luoghi[sentiero.id_luogo_2])

        print(self.grafo)

