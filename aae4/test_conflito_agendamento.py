import sys
import os
import pytest
from datetime import datetime
from agenda import Agenda
from evento import Evento

@pytest.fixture
def agenda():   
    return Agenda()

def test_conflito_agendamento_ao_adicionar(agenda):    
    evento1 = Evento("Jogo 1", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    evento2 = Evento("Jogo 2", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    agenda.adicionar_evento(evento1)
    mensagem = agenda.adicionar_evento(evento2)

    assert mensagem == "Evento tem conflito de horário com um ou mais eventos cadastrados"

def test_conflito_agendamento_ao_adicionar2(agenda):    
    evento1 = Evento("Jogo 1", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    evento2 = Evento("Jogo 2", datetime.fromisoformat("2024-07-24 10:30"), datetime.fromisoformat("2024-07-24 11:00"))
    agenda.adicionar_evento(evento1)
    mensagem = agenda.adicionar_evento(evento2)

    assert mensagem == "Evento tem conflito de horário com um ou mais eventos cadastrados"

def test_conflito_agendamento_ao_adicionar3(agenda):    
    evento1 = Evento("Jogo 1", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    evento2 = Evento("Jogo 1", datetime.fromisoformat("2024-07-24 11:00"), datetime.fromisoformat("2024-07-24 12:00"))
    agenda.adicionar_evento(evento1)
    mensagem = agenda.adicionar_evento(evento2)

    assert mensagem == "Evento tem o mesmo nome de outro evento cadastrado"
