# DATA_SPECIFICATION.md

## Visão geral

Define o esquema e o processo de geração dos datasets sintéticos usados pelo SmartDemandLab.

## Esquema de dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `timestamp` | datetime (ISO‑8601, UTC) | Marca temporal a cada 15 min. |
| `load_mw` | float | Valor da carga em MW. |
| `temperature_c` | float | Temperatura ambiente em °C (feature exógena). |
| `holiday` | bool | Indica feriado nacional. |
| `day_of_week` | int (0‑6) | Índice do dia da semana (0 = domingo). |
| `is_peak_hour` | bool | Horário de pico (18‑22 h). |
| `scenario_id` | str | Identificador do cenário (S01‑S10). |

## Geração sintética

1. Intervalo: 2 anos, resolução 15 min (~35 040 pontos/ano).

2. Componentes sazonais: tendência anual, ciclo diário, efeitos de feriados.

3. Ruído gaussiano (σ = 0.05 × média).

4. Correlação temperatura‑carga (‑0.03 MW/°C).

5. Exportação: `datasets/synthetic_load.csv.gz` e `datasets/synthetic_load.parquet`.

## Metadados

- **source**: script `forecasting/scripts/generate_synthetic_data.py`.

- **author**: SmartDemandLab Team.

- **license**: MIT.

- **version**: v1.0.

- **notes**: inclui ruído controlado e variáveis exógenas.

## Validação

- Schema validation via **pandera**.

- Checks estatísticos (média, desvio‑padrão, autocorrelação).

- Semente aleatória configurável (`--seed`).

## Uso nos pipelines

1. `forecasting/data/data_loader.py` lê o Parquet.

2. Normalização e criação de *sliding windows*.

3. Divisão 70 % treino / 15 % validação / 15 % teste.

4. Cada `scenario_id` corresponde a um experimento em `EXPERIMENT_PLAN.md`.

*Documento mantido em `docs/DATA_SPECIFICATION.md` e atualizado conforme mudanças de esquema.*
