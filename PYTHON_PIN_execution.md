# Log de Execução: Alinhamento da versão do Python (3.14)

| Campo | Valor |
|-------|-------|
| Contexto | Alinhar `pyproject.toml`, interpretador e `uv.lock` ao SRS.md (Portabilidade: Python 3.14.4). |
| Solicitante | Usuário, 2026-11-18 12:30 |
| Status | Concluída |

## 1. Comandos executados (12:30)

| # | Comando | Resultado |
|---|---------|-----------|
| 1 | `sed -i 's/^requires-python = ">=3.11"$/requires-python = ">=3.14"/' pyproject.toml` | Linha 6: `requires-python = ">=3.14"` |
| 2 | `uv python pin 3.14` | `Pinned .python-version to 3.14` |
| 3 | `uv lock` | `Resolved 20 packages in 337ms` / `Updated numpy v2.4.6, v2.5.5 -> v2.5.5` |
| 4 | `uv sync` | `Checked 18 packages` (ambiente já consistente; nenhuma reinstalação) |
| 5 | `uv lock --check` | `Resolved 20 packages in 2ms` (lock consistente) |
| 6 | `uv run python --version` | `Python 3.14.4` |

## 2. Efeito no `uv.lock`

| Item | Antes | Depois |
|------|-------|--------|
| `requires-python` | `>=3.11` | `>=3.14` |
| Pacotes resolvidos | 21 | 20 |
| numpy | 2.4.6 e 2.5.5 (por versão de Python) | 2.5.5 (único) |
| Tamanho | 188 093 bytes | 111 656 bytes |

A redução se deve à eliminação da variante de numpy (e seus wheels) destinada a Python < 3.14.

## 3. Artefatos

```text
-rw-r--r-- 1 bira bira    388 nov 18 12:30 pyproject.toml
-rw-rw-r-- 1 bira bira      5 nov 18 12:30 .python-version   (conteúdo: 3.14)
-rw-rw-r-- 1 bira bira 111656 nov 18 12:30 uv.lock
```

`.python-version` e `uv.lock` devem ser versionados no Git.
