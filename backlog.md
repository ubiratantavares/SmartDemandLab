# Backlog do Projeto SmartDemandLab

## Epics

- **EPIC-01: Definição e documentação do projeto**

  - Criar visão, requisitos, modelo de domínio e arquitetura.

- **EPIC-02: Simulação de dados sintéticos**

  - Gerador de perfis de carga, sazonalidade, ruído e falhas.

- **EPIC-03: Modelos preditivos**

  - Implementar modelos baseline, estatísticos, ML e DL.

  - Calibrar intervalos de previsão de 99% (Conformal Prediction).

- **EPIC-04: Motor de controle inteligente**

  - Implementar regras de decisão usando limites DAC e 1,05*DAC.

  - Histerese e tempos mínimos ligado/desligado.

- **EPIC-05: QA e testes automatizados**

  - Cobertura ≥80%, lint, tipagem estática.

- **EPIC-06: Deploy e monitoramento**

  - Containerização, CI/CD com uv, dashboard.

## User Stories / Tarefas (ordenadas por prioridade)

### EPIC-01 – Definição e documentação (SDD)

- **US-01**: Criar `VISION.md` – visão, objetivos e limites do projeto. (Estória: documentação inicial) 

- **US-02**: Criar `SRS.md` – requisitos funcionais e não funcionais, incluindo RF‑PI‑* e RF‑REG‑*. 

- **US-03**: Criar `DOMAIN_MODEL.md` – entidades, value objects e diagramas de classe. 

- **US-04**: Criar `ARCHITECTURE.md` – componentes, camadas e dependências (ex.: uv, pytest). 

- **US-05**: Criar `DATA_SPECIFICATION.md` – estrutura dos datasets sintéticos e metadados. 

- **US-06**: Criar `EXPERIMENT_PLAN.md` – hipóteses, cenários (S01‑S10) e métricas. 

- **US-07**: Criar `QA_PLAN.md` – estratégia de testes, cobertura, lint, tipagem. 

- **US-08**: Criar pasta `docs/` e versionar todos os arquivos acima.

### EPIC-02 – Simulação de dados sintéticos

- **US-09**: Implementar módulo `synthetic_data.py` usando NumPy/Pandas.

- **US-10**: Definir perfis de carga (Essencial, Prioritária, Não-prioritária) e funções de geração.

- **US-11**: Garantir reprodutibilidade via seed configurável (`--seed`).

- **US-12**: Persistir datasets em Parquet na pasta `data/`.

### EPIC-03 – Modelos preditivos

- **US-13**: Implementar baseline de persistência.

- **US-14**: Implementar SARIMA e ETS (statsmodels).

- **US-15**: Implementar XGBoost e Random Forest (scikit‑learn).

- **US-16**: Implementar LSTM e GRU (PyTorch).

- **US-17**: Implementar N‑BEATS (opcional, GPU).

- **US-18**: Implementar LSTM Autoencoder para detecção de anomalias.

- **US-19**: Implementar camada de **Conformal Prediction** (EnbPI/SCPI) para gerar PI₉₉.

- **US-20**: Unificar interface `DemandPredictor` que devolve `PredictionInterval`.

### EPIC-04 – Motor de controle inteligente

- **US-21**: Implementar `demand_controller.py` com regras baseada no limite superior do PI₉₉.

- **US-22**: Implementar histerese e tempos mínimos ligado/desligado.

- **US-23**: Implementar log de decisões e métricas de controle.

### EPIC-05 – QA e testes automatizados

- **US-24**: Configurar `pytest` e criar testes unitários para data loading, janela e calibrador.

- **US-25**: Criar testes de integração (pipeline completo).

- **US-26**: Configurar cobertura (`pytest-cov`) e garantir ≥80%.

- **US-27**: Configurar lint (`ruff`) e tipagem (`mypy`).

- **US-28**: Automatizar execução de testes via script `run_tests.py`.

### EPIC-06 – Deploy e monitoramento

- **US-29**: Criar Dockerfile para modelo e controlador.

- **US-30**: Configurar GitHub Actions CI/CD usando **uv** para instalar dependências (`uv sync`).

- **US-31**: Implementar dashboard Streamlit para visualização de previsões e alertas.

- **US-32**: Configurar notificação por e‑mail/SMS (ex.: smtplib ou Twilio).

## Notas adicionais

- Todas as dependências serão gerenciadas pelo instalador **uv** (`uv init`, `uv add`, `uv sync`).

- O ambiente de testes usará **pytest** como framework padrão.

- O repositório seguirá o padrão `src/` para código‑fonte e `tests/` para testes.
