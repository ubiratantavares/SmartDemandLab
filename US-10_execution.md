# US-10 – Log de Execução: Estrutura de Diretórios

| Campo | Valor |
|-------|-------|
| Tarefa | US-10 (sprint01.md) |
| Objetivo | Criar `src/`, `tests/` e `docs/` e adicionar arquivos `__init__.py`. |
| Data | 2026-11-18 |
| Status | Concluída |

## 1. Referências de especificação

| Fonte | Requisito aplicado |
|-------|--------------------|
| sprint01.md – US-10 | Criar `src/`, `tests/`, `docs/` com `__init__.py`. |
| sprint01.md – "Done" | `src/` contém apenas pacotes vazios (`__init__.py`). |
| ARCHITECTURE.md – Camadas | Pacotes `src/ui/`, `src/app/`, `src/domain/`, `src/infrastructure/`; testes em `tests/`. |
| QA_PLAN.md – Seção 1 | Testes unitários por módulo (`src/domain/`, `src/infrastructure/`, `src/app/`). |

## 2. Comandos executados

| # | Horário | Comando | Resultado |
|---|---------|---------|-----------|
| 1 | 12:33 | `ls -d src tests docs` | Os três diretórios não existiam (estado inicial limpo). |
| 2 | 12:33 | `mkdir -p src/ui src/app src/domain src/infrastructure tests docs` | Diretórios criados. |
| 3 | 12:33 | `touch src/{ui,app,domain,infrastructure}/__init__.py tests/__init__.py docs/.gitkeep` | Arquivos criados. |
| 4 | 12:33 | `find src tests docs -print \| sort` | Árvore conforme Seção 3. |
| 5 | 12:33 | `find src tests -name '__init__.py' -size +0c \| wc -l` | `0`: todos os `__init__.py` vazios. |

## 3. Estrutura resultante

```text
docs/
└── .gitkeep
src/
├── app/__init__.py
├── domain/__init__.py
├── infrastructure/__init__.py
└── ui/__init__.py
tests/
└── __init__.py
```

## 4. Verificação

| # | Comando | Resultado | Avaliação |
|---|---------|-----------|-----------|
| 1 | `uv run python -c "...; import ui, app, domain, infrastructure"` (com `src` no `sys.path`) | `imports OK: ['ui', 'app', 'domain', 'infrastructure']` | ✅ Pacotes importáveis |
| 2 | `uv run ruff check src tests` | `All checks passed!` | ✅ |
| 3 | `uv run mypy src` | `Success: no issues found in 4 source files` | ✅ |
| 4 | `uv run pytest -q` | `no tests ran` (exit 5) | ✅ Esperado: o teste de exemplo é escopo da US-11 |

## 5. Decisões de projeto

- **Layout por camada, conforme ARCHITECTURE.md.** Os pacotes ficam diretamente em `src/` (`src/domain/`, …), sem pacote raiz `smartdemandlab/`.
- **Sem `src/__init__.py`.** `src/` é a raiz de importação, não um pacote; os módulos são importados como `domain`, `app`, etc. O `sys.path` será configurado na US-11 com `pythonpath = ["src"]` em `[tool.pytest.ini_options]`.
- **`docs/.gitkeep`.** O Git não versiona diretórios vazios; o arquivo garante que `docs/` seja rastreado.
- **`tests/__init__.py`.** Evita colisão de nomes entre módulos de teste homônimos em subpastas futuras.

## 6. Pendências

- **Documentos SDD fora de `docs/`.** O critério de "Done" exige os 7 documentos em `docs/`, mas eles continuam na raiz e não foram movidos. Mover exige ajustar `readme = "VISION.md"` em `pyproject.toml` e os links cruzados. Aguarda decisão do usuário.
- **`pythonpath = ["src"]`** a configurar na US-11.

> **Atualização 2026-11-18 12:40:** documentos SDD movidos para `docs/` (P2); `pythonpath = src` configurado na US-11. Ver `PENDENCIAS_execution.md`.
