"""
Ponto de integração com a Shopee.

Não coloque senha, cookie ou código de autenticação aqui.

A função abaixo usa dados de demonstração enquanto não configurarmos
uma API/integração oficialmente autorizada para sua conta de afiliado.
"""


import json
from pathlib import Path


DEMO_FILE = Path("data/products_demo.json")


def get_eligible_products():
    """
    Retorna produtos elegíveis para o motor aleatório.

    Substituir futuramente pela integração oficial disponível para a
    conta do afiliado.
    """
    return json.loads(DEMO_FILE.read_text(encoding="utf-8"))
