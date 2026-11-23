import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        self._model.crea_grafo()
        print(self._model.grafo)

    def handle_visita_ampiezza(self, e):
        pass

    def handle_visita_profondita(self, e):
        pass
