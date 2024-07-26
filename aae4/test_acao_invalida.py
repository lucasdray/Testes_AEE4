from main import main
from time import sleep
import pytest

def test_acao_invalida(monkeypatch, capsys):
    nonsense = "blabla"
    sair = "sair"
    
    entradas = iter([nonsense, sair])

    monkeypatch.setattr('builtins.input', lambda nonsense: next(entradas))

    main()
    
    output = capsys.readouterr().out
    
    assert "Ação inválida. Por favor, tente novamente." in output
    