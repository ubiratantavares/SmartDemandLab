# Log de Execução: Criação do Ambiente Virtual (`uv sync`)

| Campo | Valor |
|-------|-------|
| Contexto | Pré-requisito para US-10 a US-12 (sprint01.md) |
| Objetivo | Criar o ambiente virtual do projeto com **uv**, instalando as dependências travadas em `uv.lock`. |
| Data | 2026-11-18 |
| Status | Concluída |

## 1. Comandos executados

| # | Horário | Comando | Resultado |
|---|---------|---------|-----------|
| 1 | 12:27 | `uv sync` | Criou `.venv` (CPython 3.14.4) e instalou 18 pacotes. |
| 2 | 12:27 | `ls -ld .venv` | `drwxrwxr-x 4 bira bira 4096 nov 18 12:27 .venv` |
| 3 | 12:27 | `uv run python -c "import sys, pandas, numpy; ..."` | `.venv/bin/python 3.14.4`, pandas 3.1.1, numpy 2.5.5 |
| 4 | 12:27 | `uv run pytest --version` | `pytest 9.2.0` |
| 5 | 12:27 | `uv run ruff --version` | `ruff 0.17.5` |
| 6 | 12:27 | `uv run mypy --version` | `mypy 2.4.1 (compiled: yes)` |

## 2. Saída de `uv sync`

```text
Using CPython 3.14.4
Creating virtual environment at: .venv
Resolved 21 packages in 3ms
Prepared 9 packages in 3.35s
Installed 18 packages in 89ms
 + ast-serialize==0.13.1
 + coverage==7.17.3
 + iniconfig==2.3.1
 + librt==0.16.0
 + mypy==2.4.1
 + mypy-extensions==1.2.0
 + numpy==2.5.5
 + packaging==26.3
 + pandas==3.1.1
 + pathspec==1.1.1
 + pluggy==1.7.0
 + pygments==2.21.0
 + pytest==9.2.0
 + pytest-cov==7.1.0
 + python-dateutil==4.0.0
 + ruff==0.17.5
 + typing-extensions==4.16.0
 + tzdata==2026.6
```

> 21 pacotes resolvidos, 18 instalados. A diferença: o próprio `smartdemandlab` (projeto virtual, sem build), a variante alternativa de `numpy` (2.4.6, para outras versões de Python) e `colorama` (somente Windows).

## 3. Uso

- Executar comandos no ambiente: `uv run <comando>` (ex.: `uv run pytest`).
- Ativação manual (opcional): `source .venv/bin/activate`.
- `.venv/` **não** deve ser versionado; adicionar ao `.gitignore`.

## 4. Observações
- O ambiente usa **CPython 3.14.4**. Em 2026-11-18 12:29, o SRS.md (Portabilidade) foi atualizado de Python 3.11 para Python 3.14.4, por decisão do usuário, alinhando especificação e ambiente.
