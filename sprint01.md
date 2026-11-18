# Sprint 1 – Início do Projeto (SDD & Configuração Inicial)

**Objetivo da Sprint**: Consolidar a documentação técnica (SDD) e preparar o ambiente de desenvolvimento usando o gerenciador de pacotes **uv** e o framework de testes **pytest**.

## Metas da Sprint

1. Criar todos os artefatos de especificação (VISION, SRS, DOMAIN_MODEL, ARCHITECTURE, DATA_SPECIFICATION, EXPERIMENT_PLAN, QA_PLAN).

2. Inicializar o repositório Python com **uv** (gerar `pyproject.toml`, `uv.lock`).

3. Configurar o diretório de código (`src/`) e de testes (`tests/`).

4. Definir a configuração padrão do **pytest** (arquivo `pytest.ini`).

5. Garantir que o CI (GitHub Actions) instale dependências via `uv sync`.

## Itens do Sprint Backlog (prioridade alta)

| # | Tarefa | Descrição | Responsável | Estimativa (horas) |
|---|--------|-----------|-------------|-------------------|
| US-01 | `VISION.md` | Redigir visão, objetivos e limites do projeto. | 📌 | 4 |
| US-02 | `SRS.md` | Documentar requisitos funcionais e não‑funcionais, incluir RF‑PI‑* e RF‑REG‑*. | 📌 | 6 |
| US-03 | `DOMAIN_MODEL.md` | Definir entidades, value objects e diagramas de classe. | 📌 | 5 |
| US-04 | `ARCHITECTURE.md` | Descrever componentes, camadas, uso do **uv** e **pytest**. | 📌 | 4 |
| US-05 | `DATA_SPECIFICATION.md` | Especificar estrutura dos datasets sintéticos. | 📌 | 3 |
| US-06 | `EXPERIMENT_PLAN.md` | Listar hipóteses, cenários (S01‑S10) e métricas. | 📌 | 3 |
| US-07 | `QA_PLAN.md` | Estratégia de testes, cobertura, lint, tipagem. | 📌 | 3 |
| US-08 | `uv init` & `pyproject.toml` | Inicializar projeto com **uv**, declarar dependências básicas (`pandas`, `numpy`, `pytest`, `ruff`, `mypy`). | 📌 | 2 |
| US-09 | `uv lock` | Gerar `uv.lock` para versionamento de dependências. | 📌 | 1 |
| US-10 | Estrutura de diretórios | Criar `src/`, `tests/`, `docs/` e adicionar arquivos `__init__.py`. | 📌 | 2 |
| US-11 | `pytest.ini` | Configurar pytest (markers, log level, coverage). | 📌 | 1 |
| US-12 | GitHub Actions workflow | Arquivo `.github/workflows/ci.yml` usando `uv sync` e `pytest`. | 📌 | 3 |

## Definição de “Done”

- Todos os documentos Markdown listados acima estão presentes em `docs/` e seguem o padrão de formatação.

- `pyproject.toml` declara as dependências mínimas (`[project]`) e de desenvolvimento (`[dependency-groups]`); os testes são executados com `uv run pytest`.

- `uv.lock` está versionado no repositório.

- Diretório `src/` contém apenas pacotes vazios (`__init__.py`).

- Diretório `tests/` contém um teste de exemplo (`test_placeholder.py`) que passa.

- `pytest.ini` está configurado para gerar cobertura (`--cov=src`).

- Workflow CI executa `uv sync && uv run pytest` e falha caso cobertura < 80 %.

- Todas as tarefas marcadas como concluídas estão commitadas e pushadas.

## Cronograma da Sprint (2 semanas)

| Dia | Atividade |
|-----|-----------|
| 1   | Planejamento da sprint, criação do board e definição das tasks. |
| 2-4 | Redação de VISION, SRS, DOMAIN_MODEL. |
| 5-6 | Criação de ARCHITECTURE, DATA_SPECIFICATION, EXPERIMENT_PLAN. |
| 7   | Revisão dos documentos, feedback interno. |
| 8   | Inicializar projeto com **uv**, gerar `pyproject.toml` e `uv.lock`. |
| 9   | Estrutura de diretórios e arquivos iniciais (`src/`, `tests/`). |
| 10  | Configurar `pytest.ini` e escrever teste placeholder. |
| 11  | Implementar workflow GitHub Actions. |
| 12  | Revisão final, QA dos documentos e do setup, commit final. |

*Esta sprint estabelece a base documental e o ambiente de desenvolvimento necessário para avançar nas próximas fases do projeto.*
