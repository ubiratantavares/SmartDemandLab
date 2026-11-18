# Log de Execução: Migração de `forecasting/requirements.txt` para `pyproject.toml`

| Campo | Valor |
|-------|-------|
| Solicitante | Usuário, 2026-11-18 17:29 |
| Motivação | Diretriz "todo o gerenciamento do projeto se dará pelo uv"; `requirements.txt` é legado do pip (GIT_INIT_execution.md §3) |
| Status | **Bloqueada: aguarda decisão do usuário sobre o TensorFlow** |

## 1. Conteúdo original de `forecasting/requirements.txt`

```text
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.0
statsmodels==0.14.2
xgboost==2.0.3
torch==2.3.0
tensorflow==2.16.1
matplotlib==3.9.0
seaborn==0.13.2
```

As versões fixadas são anteriores ao Python 3.14 (ex.: numpy 1.26.4 e torch 2.3.0 não têm wheels `cp314`). Migrar os pins literalmente é inviável; a estratégia adotada foi migrar os **nomes** e deixar o uv resolver versões compatíveis.

## 2. Comandos executados

| # | Horário | Comando | Resultado |
|---|---------|---------|-----------|
| 1 | 17:29 | Backup de `pyproject.toml` e `uv.lock` | Cópias temporárias criadas |
| 2 | 17:29 | `uv add --no-sync scikit-learn statsmodels xgboost torch tensorflow matplotlib seaborn` | `Resolved 94 packages` |
| 3 | 17:30 | Inspeção das versões resolvidas no `uv.lock` | **tensorflow 2.22.0rc1** (release candidate); o `uv add` gravou `tensorflow>=2.22.0rc1` |
| 4 | 17:30 | `uv lock --dry-run --prerelease disallow` | Falha: `only tensorflow<2.22.0rc1 is available` |
| 5 | 17:31 | `uv pip compile` (tensorflow, Python 3.14, Linux x86_64, sem pré-releases) | `all versions of tensorflow have no wheels with a matching Python ABI tag (cp314)` |
| 6 | 17:32 | `uv pip compile` (tensorflow, Python 3.13) | `tensorflow==2.21.0` (última estável suporta até 3.13) |
| 7 | 17:32 | Restauração do backup | `git status` limpo; `uv lock --check`: `Resolved 20 packages` |

### Versões resolvidas na tentativa (descartada)

| Pacote | requirements.txt | Resolvido (Python 3.14) |
|--------|------------------|-------------------------|
| pandas | 2.2.2 | 3.1.1 |
| numpy | 1.26.4 | 2.5.5 |
| scikit-learn | 1.5.0 | 1.9.1 |
| statsmodels | 0.14.2 | 0.15.0 |
| xgboost | 2.0.3 | 3.4.1 |
| torch | 2.3.0 | 2.15.0 |
| **tensorflow** | 2.16.1 | **2.22.0rc1 (pré-release)** |
| matplotlib | 3.9.0 | 3.11.2 |
| seaborn | 0.13.2 | 0.13.2 |

## 3. Análise

- Não há TensorFlow estável para Python 3.14 (decisão registrada em PYTHON_PIN_execution.md).
- Uso do TensorFlow nas especificações:
  - `docs/ARCHITECTURE.md` define **torch** para os modelos de deep learning (autoencoders/LSTM).
  - TensorFlow aparece apenas em `plan.md` (linha 163), como opção futura de quantização para ESP32/STM32 (TensorFlow Lite), ao lado de ONNX.
- Torch e TensorFlow cobrem o mesmo papel; manter ambos duplica cerca de 1 GB de dependências.

## 4. Opções para decisão

| Opção | Descrição | Impacto |
|-------|-----------|---------|
| **A (recomendada)** | Migrar todos os pacotes **exceto** tensorflow | Coerente com ARCHITECTURE.md (torch); quantização futura via ONNX, exportável do torch |
| B | Incluir `tensorflow>=2.22.0rc1` (pré-release) | Funciona hoje, mas fixa uma versão não estável |
| C | Rebaixar o projeto para Python 3.13 | Reverte a decisão de PYTHON_PIN_execution.md e exige alterar SRS.md |
