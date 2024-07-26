import sys
import os
import pytest
from datetime import datetime
from agenda import Agenda
from evento import Evento

@pytest.fixture
def agenda():   
    return Agenda()

def test_adicionar_evento(agenda):    
    evento1 = Evento("Jogo 1", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    mensagem = agenda.adicionar_evento(evento1)

    assert mensagem == "Evento Jogo 1 adicionado com sucesso"

def test_adicionar_evento2(agenda):
    evento2 = Evento("Jogo 2", datetime.fromisoformat("2024-07-24 11:30"), datetime.fromisoformat("2024-07-24 12:30"))
    mensagem = agenda.adicionar_evento(evento2)

    assert mensagem == "Evento Jogo 2 adicionado com sucesso"

def test_adicionar_evento3(agenda):
    novo_evento = Evento("Jogo 3",  datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    mensagem = agenda.adicionar_evento(novo_evento)
    
    assert mensagem == "Evento Jogo 3 adicionado com sucesso"