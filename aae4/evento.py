from datetime import datetime

class Evento:
    def __init__(self, nome, inicio, termino):
        self.nome = nome
        self.inicio = inicio 
        self.termino = termino 
        if self.inicio >= self.termino:
            raise ValueError("Hora de término deve ser após a hora de início.")