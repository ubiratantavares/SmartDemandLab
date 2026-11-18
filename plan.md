# Plano Estratégico de Desenvolvimento – SmartDemandLab (Versão Refinada)

## 1. Visão Geral do Objetivo

- **Objetivo operacional**: **evitar ultrapassar a demanda contratada**.

- **Tolerância regulatória**: 5 % (art. 301 da Resolução Normativa ANEEL nº 1.000/2021) – usada somente para avaliação de risco de cobrança, **não** como margem de operação.

- **Previsão com incerteza**: gerar, para cada intervalo de 15 min, um **intervalo de previsão de 99 %** (PI₉₉) e utilizar o **limite superior** para decisões preventivas.

## 2. Contexto das Fontes de Markdown
| Fonte | Contribuição principal |
|------|------------------------|
| `prompt01.md` | Definição de demanda, 5 % de tolerância, arquitetura de Autoencoder e métricas de avaliação. |
| `prompt05.md` | Estratégia de simulação digital (dados sintéticos, perfis de carga, arquitetura orientada a objetos, princípios SOLID, plano de QA e roadmap em 7 etapas). |
| `prompt06.md` | Requisito central: **PI₉₉** com cobertura nominal de 99 %, uso de Conformal Prediction ou métodos temporais (EnbPI, SPCI). |
| `prompt07.md` | Formalização de dois limites (demanda contratada *DAC* e limite regulatório 1,05 × DAC) e regras de decisão baseadas no limite superior do PI₉₉. |

## 3. Perguntas em Aberto (para validação)

> [!IMPORTANT]

> - Qual a **demanda contratada** (kW) da instalação alvo? 

100 kW

> - Existem **tarifas diferenciadas por posto** (ponta/fora‑ponta) que requerem limites por tarifa?

Não existem. Tarifa única para a demanda consumida em kW.

> - Qual o **tempo de antecedência** desejado para alertas (ex.: 30 min, 1 h)?

Antes da próxima janela de medição da grandeza física.

> - Qual a **seed** padrão para a geração sintética de dados?

42

## 4. Requisitos Técnicos Consolidado
| ID | Requisito |
|----|----------|
| RF‑PI‑001 | Modelo deve devolver ponto estimado + intervalo de previsão (PI₉₉). |
| RF‑PI‑002 | Cobertura nominal configurável (padrão 99 %). |
| RF‑PI‑003 | Calibração usando dados **independentes** do treinamento, respeitando ordem temporal. |
| RF‑PI‑004 | Monitoramento da cobertura empírica e da largura dos intervalos. |
| RF‑PI‑005 | Controlador usa **limite superior** do PI₉₉ contra dois limites: DAC e 1,05 × DAC. |
| RF‑REG‑001 | DAC é limite operacional de referência. |
| RF‑REG‑002 | Limite regulatório = 1,05 × DAC, parametrizável. |
| RF‑REG‑003 | Alertas preventivos disparados antes de atingir limite regulatório. |
| RF‑SOLID‑001 | Código deve obedecer aos princípios SOLID (SRP, OCP, LSP, ISP, DIP). |
| RF‑QA‑001 | Cobertura de testes ≥ 80 %; tipagem estática com *mypy*; lint *ruff*; testes *pytest*. |
| RF‑DATA‑001 | Dados sintéticos reproduzíveis via semente aleatória. |
| RF‑SIM‑001 | Simulador deve modelar carga (Essencial, Prioritária, Não‑prioritária) com tempos mínimo ligado/desligado e histerese. |

## 5. Modelos de Previsão – Catálogo Expandido
| Categoria | Modelo | Papel | Comentários |
|-----------|--------|-------|------------|
| Baseline | Persistência | Referência mínima | |
| Estatístico | SARIMA | Tendência & sazonalidade | |
| Statistical | ETS | Suavização exponencial | |
| ML | XGBoost / LightGBM | Não‑linearidade | |
| ML | Random Forest | Robustez | |
| DL | LSTM (univariado) | Dependências temporais | |
| DL | GRU | Variante compacta | |
| DL | TCN | Convolução temporal | |
| DL | N‑BEATS | Estado‑da‑arte | Requer GPU |
| Hybrid | LSTM Autoencoder (detecção de anomalias) | Reconstrução + extração latente | |
| Probabilístico | Conformal Prediction (EnbPI / SPCI) | Geração de PI₉₉ | Aplicado a qualquer modelo acima |

## 6. Arquitetura de Software (OOP + SOLID)
```
smartdemandlab/
├── domain/                # Entidades (Installation, Load, DemandInterval)
│   ├── entities/
│   │   ├── electrical_load.py
│   │   └── demand_interval.py
│   └── value_objects/     # Power, Energy, etc.
├── simulation/            # Gerador sintético, simulador elétrico, medidor
│   ├── synthetic_data.py
│   ├── electrical_plant.py
│   └── meter_simulator.py
├── prediction/            # Interfaces e implementações de modelos
│   ├── predictor.py       # Protocol com método predict_interval()
│   ├── baselines/
│   ├── machine_learning/
│   └── deep_learning/
├── control/               # Motor de decisão e regras de segurança
│   ├── demand_controller.py
│   ├── decision_engine.py
│   └── safety_rules.py
├── infrastructure/        # Persistência (Parquet, SQLite) e telemetria
└── application/           # Use‑cases, runner de experimentos
```

- **SRP**: Cada pacote tem responsabilidade única (ex.: gerador de dados não treina modelos).

- **OCP**: Novos modelos são adicionados implementando `DemandPredictor` sem tocar no controlador.

- **LSP**: Todas as classes que implementam `DemandPredictor` devem obedecer ao mesmo contrato de retorno `PredictionInterval`.

- **ISP**: Interfaces específicas (`Meter`, `Actuator`, `Predictor`).

- **DIP**: `DemandController` depende de abstrações (`DemandPredictor`, `IntervalCalibrator`).

## 7. Fases Estratégicas de Desenvolvimento (Refinadas)

### Fase 1 – Especificação (SDD) & Documentação

- Produzir: `VISION.md`, `SRS.md`, `DOMAIN_MODEL.md`, `ARCHITECTURE.md`, `DATA_SPECIFICATION.md`, `EXPERIMENT_PLAN.md`, `QA_PLAN.md`.

- Definir formalmente os requisitos RF‑PI‑* e RF‑REG‑* acima.

### Fase 2 – Infraestrutura de Simulação

1. Implementar **gerador de dados sintéticos** (perfis de carga, sazonalidade, ruído, falhas) usando `numpy`/`pandas`.

2. Criar **simulador elétrico** com parâmetros de carga (potência nominal, prioridade, tempos mínimo ligado/desligado, histerese).

3. Persistir datasets em **Parquet** para reproducibilidade.

### Fase 3 – Implementação dos Modelos

- Codificar todos os modelos listados na Seção 5, seguindo a interface `DemandPredictor`.

- Integrar **Conformal Prediction** (EnbPI) como camada de calibração para gerar PI₉₉.

- Cada modelo gera `PredictionInterval` (point, lower, upper, coverage, horizon).

### Fase 4 – Motor de Controle Inteligente

- **Regra de decisão** (usando limite superior):

  - `upper ≤ DAC` → Operação normal.

  - `DAC < upper ≤ 1,05*DAC` → Alerta de risco, possível carga prioritária.

  - `upper > 1,05*DAC` → Intervenção preventiva (desligamento de cargas não‑essenciais).

- Implementar **histerese** e **tempo mínimo ligado/desligado** para evitar churn.

### Fase 5 – Experimentos & QA

- Definir **cenários** S01‑S10 (como em `prompt05.md`).

- Executar pipeline **end‑to‑end** para cada modelo + política de controle (3 políticas definidas em `prompt07.md`).

- Medir métricas: MAE, RMSE, PICP, PINAW, taxa de ultrapassagens evitadas, número de desligamentos, antecedência média dos alertas.

- Suite de testes automatizados (unit, integration, functional, performance, robustness) com cobertura ≥ 80 %.

### Fase 6 – Deploy & Monitoramento

- Containerizar o **melhor modelo** (ex.: N‑BEATS + Conformal) e o **controlador** como micro‑serviços.

- CI/CD (GitHub Actions) para retraining mensal e atualização de calibradores.

- Dashboard (Streamlit) exibindo previsões, PI₉₉, limites DAC/Regulatórios e alertas.

- Notificações via e‑mail/SMS quando política 3 for acionada.

### Fase 7 – Avaliação para Embarcamento

- Medir footprint (RAM, CPU, latência) em **ESP32/STM32** usando quantização (TensorFlow Lite, ONNX).

- Decidir viabilidade de implantação em campo.

## 8. Plano de Verificação

### Testes Automatizados

- **Unitários**: conversão de CSV → `kW`, geração de janelas, cálculo de PI₉₉.

- **Integração**: fluxo completo (dados → modelo → intervalo → decisão).

- **Funcional**: execução de cada cenário S01‑S10, comparação de políticas.

- **Desempenho**: tempo de inferência < 50 ms, uso de memória < 200 MB.

- **Robustez**: ruído, missings, atrasos de comunicação.

### Verificação Manual

- Visualização de séries temporais e PI₉₉ em plots.

- Revisão de logs de decisão (qual carga foi desligada, por quê).

- Avaliação de cobertura empírica (PICP) contra objetivo 99 %.

## 9. Riscos & Mitigações

- **Escassez de dados reais** → usar **dados sintéticos** de longo prazo (≥ 1 ano) e, posteriormente, validar com dados de campo.

- **Deriva de calibrador** → monitorar cobertura; recalibrar automaticamente se PICP < 95 %.

- **Complexidade de OOP** → iniciar com MVP (poucas classes), evoluir conforme necessidade.

- **Regulamentação** → deixar percentagem de tolerância configurável; atualizar ADRs se a ANEEL mudar regras.

## 10. Próximos Passos Imediatos

1. **Consolidar requisitos** em `SRS.md` (incluir RF‑PI‑* e RF‑REG‑*).

2. **Criar repositório de dados sintéticos** (`data/synthetic/`) com seed padrão.

3. **Implementar interface `DemandPredictor`** e esqueleto de um modelo baseline (Persistência).

4. **Desenvolver calibrador Conformal** (EnbPI) e integrar ao baseline.

5. **Escrever testes unitários** para geração de janelas e cálculo de PI₉₉.

*Este plano refinado incorpora os detalhes técnicos de `prompt05.md`, `prompt06.md` e `prompt07.md`. Aguardo sua revisão e aprovação para avançarmos com a implementação.*
