# ARCHITECTURE.md

## Visão geral

Arquitetura em camadas alinhada aos princípios SOLID, separando responsabilidades entre UI, aplicação, domínio e infraestrutura.

### Camadas

| Camada | Responsabilidade | Pacotes principais |
|--------|------------------|--------------------|
| **Apresentação** | Interface (CLI ou Streamlit) para visualização e configuração. | `src/ui/` |
| **Aplicação** | Orquestra fluxos de simulação, previsão e controle. | `src/app/` |
| **Domínio** | Modela entidades e regras de negócio. | `src/domain/` |
| **Infraestrutura** | Persistência, acesso a dados e integração com bibliotecas de ML. | `src/infrastructure/` |
| **Testes** | Verificação automática de qualidade. | `tests/` |

### Diagrama de componentes

```mermaid
graph TD
    UI[UI] --> Service[Application Service]
    Service --> Domain[Domain Layer]
    Service --> Infra[Infrastructure Layer]
    Domain --> Entities[Entidades & VO]
    Infra --> DB[Repositório (SQLite/Postgres)]
    Infra --> ML[Modelos ML]
    Service --> Tests[Suite de testes]
```

### Gerenciamento de dependências (uv)

1. `uv init` → gera `pyproject.toml` com dependências básicas (`pandas`, `numpy`, `scikit-learn`, `torch`, `prophet`, `ruff`, `mypy`).

2. `uv lock` → cria `uv.lock` determinístico.

3. Execução via `uv run <script>`; CI usa `uv sync && uv run pytest`.

### Estratégia de testes (pytest)

- Estrutura de testes em `tests/` por módulo.

- Cobertura mínima 80 % (`--cov=src --cov-fail-under=80`).

- Lint (`ruff`) e tipagem (`mypy`) integrados ao CI.

### Integração contínua (GitHub Actions)
```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Sync dependencies
        run: uv sync
      - name: Lint
        run: uv run ruff check src/
      - name: Type check
        run: uv run mypy src/
      - name: Test
        run: uv run pytest --cov=src --cov-fail-under=80
```

*Documento mantido em `docs/ARCHITECTURE.md`.*
