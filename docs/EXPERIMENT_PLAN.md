# EXPERIMENT_PLAN.md

## Visão geral

Define os experimentos para comparar modelos de previsão de carga elétrica, avaliar cobertura de intervalos (PI99) e validar a regra regulatória de 5%.

## Hipóteses

| # | Hipótese |
|---|----------|
| H1 | Modelos tradicionais (ARIMA, Prophet, Exponential Smoothing) têm desempenho similar a modelos deep‑learning (LSTM, Autoencoder) em RMSE/MAE. |
| H2 | Incluir `temperature_c` melhora a acurácia (p < 0.05). |
| H3 | Conformal Prediction fornece cobertura ≈ 99 % dos intervalos. |
| H4 | Aplicar a regra de tolerância (1.05 × DAC) reduz falsos positivos de violação comparado ao uso do ponto estimado. |
| H5 | Desempenho diminui em períodos de pico (18‑22 h). |

## Cenários (S01‑S10)

| Cenário | Descrição |
|---------|-----------|
| S01 | Dados sintéticos padrões, sem feriados. |
| S02 | Inclui feriados nacionais (carga reduzida). |
| S03 | Temperaturas extremas (> 35 °C). |
| S04 | DAC reduzida 10 % (sensibilidade). |
| S05 | Falhas de sensores (5 % missing). |
| S06 | Carga base aumentada 15 % ( crescimento). |
| S07 | Pico deslocado (16‑20 h). |
| S08 | Feridos + clima extremo. |
| S09 | Alta penetração renovável (carga -20 %). |
| S10 | Stress test (1 milhão de registros). |

## Métricas

- **RMSE**, **MAE** – erro pontual.

- **PI Coverage** – % de observações dentro do intervalo 99 %.

- **Regulatory Risk** – % de vezes que `pi_upper_mw` > `DAC × 1.05`.

- **Tempo de execução** – treinamento + inferência (s).

- **Peak Error** – RMSE nos períodos de pico.

## Protocolo

1. **Pré‑processamento** – carregar `synthetic_load.parquet`, gerar *sliding windows* (24 h).

2. **Divisão** – 70 % treino, 15 % validação, 15 % teste.

3. **Treinamento** – para cada modelo e cenário, ajuste de hiper‑parâmetros simples.

4. **Conformal Prediction** – gerar intervalos 99 %.

5. **Avaliação** – calcular métricas listadas.

6. **Registro** – salvar resultados em `experiments/results_<scenario>.csv` e gráficos resumidos.

## Ferramentas

- Python 3.14 (`pandas`, `numpy`, `scikit-learn`, `statsmodels`, `torch`, `prophet`, `mapie`).

- Gerenciamento de dependências: **uv**.

- Testes: `pytest`.

- CI: GitHub Actions (executa experimentos em pull‑requests).

## Cronograma

| Etapa | Data prevista |
|-------|---------------|
| Setup | 2026‑11‑20 |
| Execução inicial (S01‑S03) | 2026‑11‑22 |
| Deep Learning (todos cenários) | 2026‑11‑24 |
| Análise Conformal | 2026‑11‑26 |
| Relatório final | 2026‑11‑28 |

*Documento mantido em `docs/EXPERIMENT_PLAN.md`.*
