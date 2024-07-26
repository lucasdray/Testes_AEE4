import sys
import os
import pytest
from datetime import datetime
from agenda import Agenda
from evento import Evento

@pytest.fixture
def agenda():   
    return Agenda()

def test_hora_invalida(agenda):
    evento = Evento("Jogo 1", "a", "b")
    mensagem = agenda.adicionar_evento_hora_invalido(evento)
    assert mensagem == "Data formatada de forma errada. O formato correto é 'YYYY-MM-DD HH:MM'"
