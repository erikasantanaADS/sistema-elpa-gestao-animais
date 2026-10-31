import pytest
from app import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


def test_pagina_inicial(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200


def test_pagina_sobre(cliente):
    resposta = cliente.get("/sobre")
    assert resposta.status_code == 200


def test_pagina_cadastro(cliente):
    resposta = cliente.get("/cadastrar-animal")
    assert resposta.status_code == 200


def test_pagina_consulta(cliente):
    resposta = cliente.get("/consultar-animais")
    assert resposta.status_code == 200


def test_pagina_atendimento(cliente):
    resposta = cliente.get("/atendimento-veterinario")
    assert resposta.status_code == 200