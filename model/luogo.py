from dataclasses import dataclass

@dataclass
class Luogo:
    id : int
    nome : str
    tipo : str
    quota_m : int

    def __hash__(self):
        return hash(self.id)

    def __str__(self) -> str:
        return f'{self.id} | {self.nome} | {self.tipo} | {self.quota_m}'
