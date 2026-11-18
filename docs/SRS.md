# SRS.md

## Visão geral

Especificação de requisitos de software para o SmartDemandLab, cobrindo funcionalidades, requisitos não funcionais, interfaces e critérios de aceitação.

## Requisitos funcionais

1. **Previsão de demanda** – gerar estimativa a cada 15 min com ponto e intervalo de confiança de 99 % (PI₉₉).

2. **Gestão de risco** – comparar `upper_bound` com `1.05 × DAC` e acionar controle preventivo.

3. **Simulação de dados** – produzir datasets sintéticos reproduzíveis por seed, incluindo sazonalidade, feriados e ruído.

4. **Configuração de cenários** – suportar cenários S01‑S10 com parâmetros customizados.

5. **Exportação de resultados** – salvar métricas (RMSE, MAE, cobertura PI, tempo de inferência) em CSV/Parquet.

## Requisitos não funcionais

- **Precisão** – cobertura empírica de PI₉₉ ≥ 99 % em validação.

- **Desempenho** – inferência < 50 ms por ponto.

- **Escalabilidade** – processar até 1 milhão de registros sem degradação significativa.

- **Segurança** – código livre de vulnerabilidades críticas (Bandit).

- **Portabilidade** – Linux, Python 3.14.4.

## Interfaces

- **CLI** – `smartdemandlab run <scenario>`.

- **API Python** – funções `predict()`, `evaluate_risk()`.

- **Entradas** – `synthetic_load.parquet` conforme `DATA_SPECIFICATION.md`.

## Critérios de aceitação

- Testes unitários com cobertura ≥ 80 % passam.

- Lint (ruff) e type checking (mypy) sem erros.

- Relatório de experimentos gera métricas para cada cenário conforme `EXPERIMENT_PLAN.md`.

*Documento mantido em `docs/SRS.md` e atualizado conforme mudanças de requisitos.*
