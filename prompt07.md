# PROMPT

Lembrando que nos cálculos deve ser levanto em consideração a tolerância de 5% acima de demanda contratada.

# RESPOSTA

Perfeito. Vamos incorporar essa tolerância de 5% como uma regra regulatória do sistema de controle, mas há uma distinção importante para evitar um erro de projeto: **os 5% representam o limite regulatório para a incidência da cobrança por ultrapassagem, não uma margem de operação que devemos consumir deliberadamente.**

O art. 301 da Resolução Normativa ANEEL nº 1.000/2021 estabelece que, para consumidores com demanda contratada de consumo, a cobrança por ultrapassagem é aplicável quando a demanda medida excede a contratada em mais de 5%.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www2.aneel.gov.br\&sz=32)

Aneel+1



## **1. Dois limites diferentes no controlador**

Vamos trabalhar com dois limites:

- **Demanda contratada (DAC):** limite operacional de referência.
- **Limite de tolerância regulatória:** 105% da demanda contratada.

\\[ D\_{\text{tolerância}}=D\_{\text{contratada}}\times1,05 \\]

Exemplo com demanda contratada de 500 kW:

## **Limites de demanda**

Demanda contratada

# **500 kW**

Limite de 105%

# **525 kW**

Faixa contratada

Até 500 kW

Faixa de tolerância

500 a 525 kW

Faixa acima da tolerância

Acima de 525 kW

Representação ilustrativa. A incidência regulatória depende da demanda medida e das condições de faturamento aplicáveis.

## **2. Como incorporar o intervalo de previsão de 99%**

O modelo preditivo continuará retornando:

\\[ PI\_{99\\%}=[D\_{\text{inf}},D\_{\text{sup}}] \\]

O controlador avaliará o limite superior em relação aos dois limites de demanda.

| Condição                              | Interpretação                                                        | Ação sugerida                      |
| ------------------------------------- | -------------------------------------------------------------------- | ---------------------------------- |
| \\(D\_{\text{sup}}\leq DAC\\)         | Previsão dentro da demanda contratada                                | Operação normal                    |
| \\(DAC\<D\_{\text{sup}}\leq1,05DAC\\) | Risco de ultrapassar a contratada, mas dentro da faixa de tolerância | Alerta e avaliação preventiva      |
| \\(D\_{\text{sup}}>1,05DAC\\)         | Risco de ultrapassar o limite regulatório                            | Intervenção preventiva prioritária |

**Importante:** não devemos esperar que a previsão ultrapasse 105% para desligar cargas. O sistema deve tentar preservar a operação dentro da demanda contratada.

## **3. Alteração dos requisitos do SmartDemandLab**

Acrescentaria estes requisitos ao SRS:

| ID         | Requisito                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| RF-REG-001 | O sistema deverá considerar a demanda contratada como limite operacional de referência.                                           |
| RF-REG-002 | O sistema deverá calcular automaticamente o limite regulatório de 105% da demanda contratada.                                     |
| RF-REG-003 | O sistema deverá avaliar o limite superior do intervalo de previsão de 99% contra ambos os limites.                               |
| RF-REG-004 | O sistema deverá emitir alertas preventivos antes de atingir o limite regulatório.                                                |
| RF-REG-005 | O sistema deverá registrar as decisões de controle e as ultrapassagens simuladas.                                                 |
| RF-REG-006 | O percentual de tolerância deverá ser parametrizável, mantendo 5% como configuração inicial para o cenário regulatório aplicável. |

Também precisamos considerar que o faturamento pode ter particularidades por posto tarifário, como ponta e fora de ponta. Portanto, a demanda contratada e os respectivos limites devem ser configuráveis por posto tarifário quando aplicável.

## **4. Hipótese experimental atualizada**

Nossa hipótese passa a ser:

**H1:** A utilização de modelos preditivos com intervalos de previsão de 99%, associados a uma política de controle que considere a demanda contratada e a tolerância regulatória de 5%, permite reduzir a incidência de ultrapassagens de demanda, minimizando desligamentos desnecessários de cargas.

Vamos comparar três políticas:

1. Controle baseado somente na previsão pontual.
2. Controle baseado no limite superior do intervalo de 99%, considerando a demanda contratada.
3. Controle baseado no limite superior do intervalo de 99%, considerando a demanda contratada e o limite regulatório de 105%.

Isso permitirá avaliar se a informação estatística adicional realmente melhora a operação.

