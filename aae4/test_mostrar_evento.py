import sys
import os
import pytest
from datetime import datetime
from agenda import Agenda
from evento import Evento

@pytest.fixture
def agenda():   
    return Agenda()

def test_mostrar_agenda(agenda):
    evento1 = Evento("Final dos 100m", datetime.fromisoformat("2024-07-24T10:00:00"), 
    datetime.fromisoformat("2024-07-24T11:00:00"))
    evento2 = Evento("Final dos 200m", datetime.fromisoformat("2024-07-24T11:30:00"), 
    datetime.fromisoformat("2024-07-24T12:30:00"))
    agenda.adicionar_evento(evento1)
    agenda.adicionar_evento(evento2)
    result = agenda.mostrar_agenda()
    expected_result = [
        "Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00",
        "Final dos 200m: 2024-07-24 11:30 a 2024-07-24 12:30"
    ]
    assert result == expected_result