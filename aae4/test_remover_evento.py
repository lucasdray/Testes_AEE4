import sys
import os
import pytest
from datetime import datetime
from agenda import Agenda
from evento import Evento

@pytest.fixture
def agenda():   
    return Agenda()

def test_remover_agenda(agenda):
    evento = Evento("Final dos 100m", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    agenda.adicionar_evento(evento)
    mensagem = agenda.remover_evento(evento.nome)

    assert mensagem == "Evento removido com sucesso."