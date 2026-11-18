# QA_PLAN.md

## Visão geral
Estratégia de garantia de qualidade do SmartDemandLab: testes automatizados, cobertura, análise estática, CI e revisão. Itens marcados como **(planejado)** ainda não estão implementados.

## 1. Tipos de teste
| Tipo | Ferramenta | Escopo | Marcador | Frequência |
|------|------------|--------|----------|------------|
| Unitário | pytest | Cada pacote (`domain`, `app`, `infrastructure`, `ui`) | – | Todo commit (CI) |
| Integração | pytest + fixtures | Fluxo ingestão → previsão → controle | `integration` | Todo commit (CI) |
| Performance | pytest-benchmark **(planejado)** | Tempo de treinamento e inferência (meta < 50 ms, SRS.md) | `performance` | PRs que alteram modelos |
| Regressão | pytest + snapshot de métricas | RMSE, MAE, PI Coverage entre versões | `regression` | Cada release |

- Testes lentos recebem também o marcador `slow` (excluir com `-m "not slow"`).
- Marcadores não declarados são rejeitados (`--strict-markers`).

## 2. Cobertura
- Mínimo: **80 %** sobre `src/`. Abaixo disso, a execução falha.
- Relatórios: terminal (`term-missing`) e `coverage.xml` (artefato do CI).
- Configuração: `pytest.ini` (fonte única).

## 3. Análise estática
| Ferramenta | Finalidade | Comando | Configuração |
|------------|------------|---------|--------------|
| ruff | Lint (PEP 8, imports, código morto) | `uv run ruff check src tests` | Padrão do ruff; regras customizadas em `[tool.ruff]` do `pyproject.toml` **(planejado)** |
| mypy | Tipagem estática | `uv run mypy src tests` | Padrão do mypy; `strict = true` em `[tool.mypy]` do `pyproject.toml` **(planejado)** |
| bandit | Segurança (SRS.md) | `uv run bandit -r src` | Requer `uv add --dev bandit` **(planejado)** |

## 4. Integração contínua
Workflow `.github/workflows/ci.yml` (US-12) executa, em ordem:
1. `uv sync --locked`: instala exatamente o `uv.lock`.
2. `uv run ruff check src tests`
3. `uv run mypy src tests`
4. `uv run pytest`: cobertura e limite de 80 % aplicados via `pytest.ini`.
5. Publicação de `coverage.xml` como artefato.

Qualquer etapa com falha reprova o build.

## 5. Política de pull request
1. Pelo menos uma aprovação de revisor.
2. Todas as etapas do CI aprovadas.
3. Mudança de comportamento exige atualização do documento correspondente em `docs/`.

## 6. Melhoria contínua
| Ciclo | Atividade |
|-------|-----------|
| Sprint | Revisão de falhas de teste e de cobertura |
| Mensal | Revisão de regras de lint e tipagem |
| Trimestral | Auditoria de segurança de dependências |

## Referências
- pytest: https://docs.pytest.org/
- pytest-cov: https://pytest-cov.readthedocs.io/
- ruff: https://docs.astral.sh/ruff/
- mypy: https://mypy.readthedocs.io/
- uv: https://docs.astral.sh/uv/
- PEP 8 (estilo) e PEP 484 (type hints): https://peps.python.org/

*Documento mantido em `docs/QA_PLAN.md`.*
