# Log de Execução: Resolução de Pendências (Sprint 1)

| Campo | Valor |
|-------|-------|
| Solicitante | Usuário, 2026-11-18 12:38 ("Execute as pendências") |
| Status | Concluída |

## 1. Pendências tratadas

| # | Pendência | Origem | Ação |
|---|-----------|--------|------|
| P1 | `.gitignore` ausente | US-11_execution.md §6 | Criado |
| P2 | Documentos SDD fora de `docs/` | US-10_execution.md §6; sprint01.md "Done" | 7 documentos movidos para `docs/` |
| P3 | Critério "Done" com `[tool.uv]` / `test = "pytest"` (recurso inexistente no uv) | US-08_execution.md §4 | sprint01.md corrigido |
| P4 | QA_PLAN.md não refinado na rodada de refinamento | Resposta de 2026-11-18 12:26 | Refinado |

## 2. Comandos e ações executados (12:39–12:40)

| # | Ação | Resultado |
|---|------|-----------|
| 1 | `git rev-parse --is-inside-work-tree` | `fatal: not a git repository`: o diretório não é um repositório Git |
| 2 | Criação de `.gitignore` | Ver §3.1 |
| 3 | `mv -n VISION.md SRS.md DOMAIN_MODEL.md ARCHITECTURE.md DATA_SPECIFICATION.md EXPERIMENT_PLAN.md QA_PLAN.md docs/` | 7 arquivos em `docs/`; nenhum sobrescrito (`-n`) |
| 4 | `rm docs/.gitkeep` | Removido; `docs/` não está mais vazio |
| 5 | `sed -i 's\|^readme = "VISION.md"$\|readme = "docs/VISION.md"\|' pyproject.toml` | Linha 5: `readme = "docs/VISION.md"` |
| 6 | Reescrita de `docs/QA_PLAN.md` | Ver §3.2 |
| 7 | Edição de `sprint01.md` linha 38 | Ver §3.3 |

## 3. Detalhamento

### 3.1 `.gitignore` (P1)
Ignora: `.venv/`, `__pycache__/`, `*.py[cod]`, `.coverage*`, `coverage.xml`, `htmlcov/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `build/`, `dist/`, `*.egg-info/`, `datasets/`, `.vscode/`, `.idea/`, `.DS_Store`.

Mantidos versionados (sprint01.md "Done"): `uv.lock`, `.python-version`.

`datasets/` é ignorado porque os dados sintéticos são reproduzíveis por seed (DATA_SPECIFICATION.md).

### 3.2 QA_PLAN.md refinado (P4)

| Problema na versão anterior | Correção |
|-----------------------------|----------|
| Citava `ruff.toml` e `mypy.ini`, que não existem | Configuração padrão das ferramentas; customização futura em `pyproject.toml`, marcada **(planejado)** |
| Afirmava `mypy strict = true` já configurado | Marcado **(planejado)** |
| bandit no CI, mas não instalado | Marcado **(planejado)**, com comando de instalação |
| `ruff-report.json` e `mypy-report.txt` como artefatos | Removidos (não são gerados) |
| Badge com URL incompleta (`url=…`) | Removido |
| Comando do CI duplicava flags de cobertura já presentes em `pytest.ini` | `uv run pytest` (configuração centralizada) |
| `uv sync` sem garantia de lock | `uv sync --locked` |
| Marcadores ausentes | Tabela relaciona cada tipo de teste ao marcador do `pytest.ini` |

### 3.3 sprint01.md (P3)

```diff
-- `pyproject.toml` contém a seção `[tool.uv]` com dependências mínimas e scripts (`test = "pytest"`).
+- `pyproject.toml` declara as dependências mínimas (`[project]`) e de desenvolvimento (`[dependency-groups]`); os testes são executados com `uv run pytest`.
```

## 4. Verificação

| # | Verificação | Resultado | Avaliação |
|---|-------------|-----------|-----------|
| 1 | `uv lock --check` (após mudar `readme`) | `Resolved 20 packages` | ✅ |
| 2 | `uv sync --locked` | `Checked 18 packages`, exit 0 | ✅ |
| 3 | `uv run pytest -q` | `4 passed`, `Total coverage: 100.00%` | ✅ |
| 4 | `uv run ruff check src tests` / `uv run mypy src tests` | `All checks passed!` / `no issues found in 6 source files` | ✅ |
| 5 | `.gitignore`: cópia do projeto em diretório temporário + `git init` + `git add -A --dry-run` | 0 artefatos gerados seriam versionados; `uv.lock`, `.python-version`, `.gitignore`, `pytest.ini` e os 7 `docs/*.md` incluídos; 37 arquivos no total | ✅ (diretório temporário removido) |
| 6 | Referências | `pyproject.toml` aponta para `docs/VISION.md`; os documentos referenciam-se pelo nome, no mesmo diretório | ✅ |

## 5. Estrutura resultante

```text
docs/
├── ARCHITECTURE.md
├── DATA_SPECIFICATION.md
├── DOMAIN_MODEL.md
├── EXPERIMENT_PLAN.md
├── QA_PLAN.md
├── SRS.md
└── VISION.md
```

Os logs de execução (`*_execution.md`) permanecem na raiz.

## 6. Pendência remanescente

- **Repositório Git inexistente.** O critério "Todas as tarefas … commitadas e pushadas" (sprint01.md) e a US-12 (GitHub Actions) dependem de `git init` e de um remoto no GitHub. Aguarda decisão do usuário.
