# US-11 – Log de Execução: `pytest.ini`

| Campo | Valor |
|-------|-------|
| Tarefa | US-11 (sprint01.md) |
| Objetivo | Configurar o pytest (markers, log level, coverage). |
| Data | 2026-11-18 |
| Status | Concluída |

## 1. Referências de especificação

| Fonte | Requisito aplicado |
|-------|--------------------|
| sprint01.md – US-11 | `pytest.ini` com markers, log level e coverage. |
| sprint01.md – "Done" | `pytest.ini` gera cobertura (`--cov=src`); `tests/test_placeholder.py` passa. |
| QA_PLAN.md – Seção 1 | Tipos de teste: unitário, integração, performance, regressão. |
| QA_PLAN.md – Seção 2 | Cobertura mínima 80 % (`--cov=src --cov-fail-under=80`); relatório publicado como artefato do CI. |
| ARCHITECTURE.md – Estratégia de testes | Marcador `slow`; testes em `tests/`. |
| US-10_execution.md – Pendências | Configurar `pythonpath = ["src"]`. |

## 2. Ações executadas

| # | Horário | Ação | Resultado |
|---|---------|------|-----------|
| 1 | 12:34 | Criação de `pytest.ini` | 913 bytes |
| 2 | 12:34 | Criação de `tests/test_placeholder.py` | 346 bytes |
| 3 | 12:34 | Remoção de `[tool.pytest.ini_options]` de `pyproject.toml` | Fonte única de configuração (ver Seção 5) |
| 4 | 12:34–12:37 | Bateria de verificação | Ver Seção 4 |

## 3. Artefatos

### 3.1 `pytest.ini`

```ini
[pytest]
minversion = 9.0
testpaths = tests
pythonpath = src

addopts =
    -ra
    --strict-markers
    --strict-config
    --cov=src
    --cov-report=term-missing
    --cov-report=xml
    --cov-fail-under=80

markers =
    integration: fluxo completo ingestão -> previsão -> controle
    performance: tempo de treinamento e inferência dos modelos
    regression: comparação de métricas (RMSE, MAE, PI Coverage) entre versões
    slow: testes lentos (excluir com -m "not slow")

log_level = INFO
log_cli_level = WARNING
log_format = %(asctime)s %(levelname)s %(name)s: %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

| Opção | Justificativa |
|-------|---------------|
| `pythonpath = src` | Torna `ui`, `app`, `domain` e `infrastructure` importáveis (pendência da US-10). |
| `--strict-markers` | Marcador não declarado vira erro, evitando typos que desativariam filtros `-m`. |
| `--strict-config` | Chave inválida no `pytest.ini` vira erro. |
| `--cov-report=xml` | Gera `coverage.xml` para publicação no CI (QA_PLAN.md §2). |
| `--cov-fail-under=80` | Limite mínimo do QA_PLAN.md. |
| `log_level = INFO` | Logs capturados e exibidos em falhas. |
| `log_cli_level = WARNING` | Exibição ao vivo restrita a avisos e erros. |

### 3.2 `tests/test_placeholder.py`

```python
import importlib

import pytest

LAYERS = ("ui", "app", "domain", "infrastructure")


@pytest.mark.parametrize("layer", LAYERS)
def test_layer_package_is_importable(layer: str) -> None:
    module = importlib.import_module(layer)
    assert module.__name__ == layer
```

O teste valida a estrutura da US-10 e a opção `pythonpath`, em vez de um `assert True` sem valor.

## 4. Verificação

| # | Verificação | Comando | Resultado | Avaliação |
|---|-------------|---------|-----------|-----------|
| 1 | Execução padrão | `uv run pytest` | `configfile: pytest.ini`, `4 passed`, `Total coverage: 100.00%`, exit 0 | ✅ |
| 2 | Marcadores registrados | `uv run pytest --markers` | `integration`, `performance`, `regression`, `slow` listados | ✅ |
| 3 | Trava de cobertura (1ª tentativa) | `pytest --cov-fail-under=101` | Erro de uso: o pytest-cov rejeita valores > 100. **Teste inválido**, descartado. | ⚠️ |
| 4 | Trava de cobertura (refeita) | Módulo temporário `src/domain/_tmp_uncovered.py` com 4 linhas não cobertas | `FAIL Required test coverage of 80% not reached. Total coverage: 0.00%`; `4 passed`, **exit 1** | ✅ Falha mesmo com testes passando |
| 5 | Limpeza pós-teste | `rm` do módulo temporário + `uv run pytest` | exit 0 | ✅ |
| 6 | `--strict-markers` | Teste temporário com `@pytest.mark.naodeclarado` | `'naodeclarado' not found in markers configuration option` – erro de coleta | ✅ (arquivo temporário removido) |
| 7 | Lint / tipagem | `uv run ruff check src tests` / `uv run mypy src tests` | `All checks passed!` / `no issues found in 6 source files` | ✅ |
| 8 | Lock | `uv lock --check` | `Resolved 20 packages` – sem alteração | ✅ |

Saída da execução padrão:

```text
platform linux -- Python 3.14.4, pytest-9.2.0, pluggy-1.7.0
configfile: pytest.ini
testpaths: tests
plugins: cov-7.1.0
collected 4 items

tests/test_placeholder.py ....                                           [100%]

Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src/app/__init__.py                  0      0   100%
src/domain/__init__.py               0      0   100%
src/infrastructure/__init__.py       0      0   100%
src/ui/__init__.py                   0      0   100%
--------------------------------------------------------------
TOTAL                                0      0   100%
Coverage XML written to file coverage.xml
Required test coverage of 80% reached. Total coverage: 100.00%
============================== 4 passed in 0.07s ===============================
```

## 5. Decisões de projeto

- **Fonte única de configuração.** Com `pytest.ini` presente, o pytest ignora `[tool.pytest.ini_options]` do `pyproject.toml` sem aviso. A seção foi removida para evitar configuração morta e divergente.
- **100 % de cobertura sobre 0 instruções.** Os `__init__.py` estão vazios, logo a métrica atual não é informativa. A trava passa a ter efeito real a partir do primeiro código de domínio; o teste #4 comprova que ela funciona.
- **Marcador `performance` sem `pytest-benchmark`.** O QA_PLAN.md prevê `pytest-benchmark`, mas o plugin não foi adicionado nesta tarefa (fora do escopo da US-11). Adicionar via `uv add --dev pytest-benchmark` quando houver modelos.

## 6. Pendências

- **`.gitignore`.** O projeto ainda não tem um; `coverage.xml`, `.coverage` e `__pycache__/` são gerados a cada execução e não devem ser versionados.
- **US-12.** O workflow do CI deve publicar `coverage.xml` como artefato.

> **Atualização 2026-11-18 12:40:** `.gitignore` criado (P1). Ver `PENDENCIAS_execution.md`.
