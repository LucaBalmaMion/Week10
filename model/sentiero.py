from dataclasses import dataclass


@dataclass
class Sentiero:
    id : int
    id_luogo_1 : int
    id_luogo_2 : int
    nome : str
    lunghezza_km : float
    difficolta : str

    def __str__(self) -> str:
        return f'{self.id} {self.nome} {self.lunghezza_km} km'