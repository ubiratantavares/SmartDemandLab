"""Teste de exemplo (US-11): valida a estrutura de pacotes criada na US-10."""

import importlib

import pytest

LAYERS = ("ui", "app", "domain", "infrastructure")


@pytest.mark.parametrize("layer", LAYERS)
def test_layer_package_is_importable(layer: str) -> None:
    module = importlib.import_module(layer)
    assert module.__name__ == layer
