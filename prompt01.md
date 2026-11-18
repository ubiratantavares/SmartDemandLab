# PROMPT

A **memória de massa** **é o registro detalhado das medições de energia elétrica (como consumo, demanda e grandezas elétricas em intervalos de minutos) armazenado no medidor eletrônico da unidade consumidora.&#x20;**

# Relatório de Memória de Massa: Como Interpretar os Dados do Medidor da Concessionária Landis+Gyr

A leitura correta do relatório de memória de massa é uma habilidade essencial para qualquer engenheiro eletricista que deseja atuar com consultoria energética profissional. Em muitas regiões do Brasil, especialmente para consumidores do Grupo A (média tensão), concessionárias como a Energisa utilizam medidores eletrônicos da fabricante Landis+Gyr para registrar o perfil de carga de clientes. Mas apesar do acesso a esses relatórios ser um direito do consumidor, entender o que cada campo significa ainda é um desafio para a maioria.



Se você já teve acesso a um relatório com colunas como “C1”, “varIND”, “DCR” e “UFER”, mas não soube o que fazer com isso, este artigo vai te dar clareza. Vamos destrinchar cada campo do relatório, explicar seu impacto e mostrar como você pode usar esses dados em diagnósticos energéticos, prevenção de multas e consultorias de alto valor.

---

## O Que é o Relatório de Memória de Massa?

### Finalidade do Relatório

O relatório de memória de massa é um registro detalhado das medições horárias (ou a cada 15 minutos) feitas pelo medidor eletrônico. Ele registra, ao longo do mês, a potência ativa, reativa, o fator de potência, a demanda medida, o status tarifário e outros dados relevantes.

### Quando o Cliente Recebe Esse Relatório?

Em geral, o relatório é fornecido mediante solicitação formal, contestação de fatura ou para auditorias energéticas. Consultores também usam esses dados para propor soluções de eficiência energética, gestão de modalidades tarifárias e correção do fator de potência.

---

## Entendendo os Medidores Landis+Gyr

### Características Técnicas Gerais

Os modelos da Landis+Gyr utilizados por concessionárias são medidores eletrônicos trifásicos com canais configuráveis, medição bidirecional (importação e exportação de energia) e compatíveis com softwares como o PAD Win.

### Como Algumas Distribuidoras Configura os Canais de Medida

A distribuidora define canais padrões como:

- C1: energia ativa
- C2: energia reativa indutiva
- C3: energia reativa capacitiva

Essas definições podem variar de acordo com o contrato e perfil tarifário.

---

## Significado de Cada Campo do Relatório de Memória de Massa

## [image](https://worldeletrica.com.br/wp-content/webp-express/webp-images/uploads/2025/05/memoria_de_massa_energisa_medidor_landisGyr-1.jpg.webp)

**Importante:** muitos valores aparecem em unidades básicas como **W, Wh, VAR, VARh**. Para interpretar corretamente, divida por **1000** para converter para kW, kWh, kVAR, kVARh.



**Atenção:** é fundamental observar na sua fatura de energia a **Constante do Medidor (Constante k)**, que é um fator de multiplicação aplicado sobre os valores registrados pelo equipamento. Por exemplo, se a constante for 500, um valor de 10 Wh no canal C1 deve ser interpretado como 5000 Wh (ou 5 kWh).

### Canais de Energia e Potência

- **W** – Potência ativa média do intervalo (em W). Divide-se por 1000 para obter kW.
- **C1** – Energia ativa medida no intervalo (Wh). Divide-se por 1000 para kWh.
- **varIND / C2** – Potência reativa indutiva média (W) e energia acumulada (VARh). Dividir por 1000 para obter valores em kvar e kvarh.
- **varCAP / C3** – Potência reativa capacitiva média (W) e energia acumulada (VARh). Mesmo critério de conversão.

### Indicadores Operacionais

- **SH** – Status Horário: identifica se o intervalo ocorreu em ponta (P) ou fora de ponta (F).
- **SR** – Status Reativo: mostra se o intervalo teve excesso de reativo indutivo (L) ou capacitivo (C).
- **FPot.** – Fator de potência instantâneo (ex: 0,94 ou 94%). Valores abaixo de 0,92 podem gerar cobrança de excedente.
- **DCR** – Demanda Corrigida Registrada: potência ativa corrigida pelo fator de potência. Utilizada para verificar ultrapassagens contratuais.
- **UFER** – Unidade de Faturamento de Energia Reativa Excedente: quantifica o excedente reativo para aplicação de penalidades.

---

## Como Usar Esses Dados em Consultorias Elétricas

### Verificação de Ultrapassagem de Demanda

Comparar o valor de **W** com a demanda contratada e observar **DCR** em intervalos de pico.

### Análise de Fator de Potência e Penalidades

Com base em **FPot.**, identificar horas em que o fator está abaixo de 0,92 e cruzar com **SR** e **UFER**.

### Identificação de Excedente Reativo

Campos **C2**, **C3** e **UFER** mostram quando há consumo reativo não compensado. Serve de base para propor correção do fator de potência através de banco de capacitores.

---

## Como Se Capacitar para Atuar com Diagnóstico Energético Profissional

[**image**](https://worldeletrica.com.br/wp-content/webp-express/webp-images/uploads/2025/05/consultor_energia_memoria_de_massa-300x300.png.webp)



Interpretar relatórios como esse é o primeiro passo para atuar com consultorias em eficiência energética. Muitos engenheiros e técnicos perdem oportunidades por não dominarem essa análise. O mercado exige profissionais que saibam transformar dados em recomendações.

---

## Conclusão

Dominar a leitura do relatório de memória de massa dos medidores eletrônicos utilizados pelas concessionárias é uma vantagem estratégica para quem quer atuar com consultoria elétrica. Cada campo do relatório fornece pistas valiosas sobre o comportamento energético da instalação.



Aprender a interpretar grandezas como W, C1, varIND e UFER permite:

- Identificar ultrapassagens de demanda
- Apontar ineficiências no uso de energia reativa
- Elaborar planos de ação técnico-comerciais para seus clientes

E é exatamente isso que o mercado espera de um consultor de alto valor.  Considerando a informação da demanda ativa (W) presente na memória de massa como uma série temporal medida em 15 em 15 minutos, avalie a possibilidade de utilização do modelo Autoencoder do aprendizado profundo para detectar a ultrapassagem de demanda (A **ultrapassagem de demanda** ocorre quando a demanda de potência ativa medida no ciclo de faturamento (em intervalos de 15 minutos) supera o valor de demanda contratada junto à distribuidora além da margem de tolerância prevista pela ANEEL, A tolerância permitida pela ANEEL para ultrapassagem de demanda de consumo é de **5%** sobre a demanda contratada, conforme o artigo 301 da Resolução Normativa nº 1.000/2021. A **demanda contratada** **é a potência elétrica ativa (medida em kW) que um consumidor do Grupo A (média ou alta tensão) reserva junto à distribuidora para ficar disponível de forma contínua**. Ela funciona como uma reserva de capacidade na rede para atender aos picos de uso simultâneo dos equipamentos. A previsão futura da próxima medição da potência ativa, isto é, a previsão do valor da potência ativa para a próxima medição da série temporal, pode ser detectada a partir de somente os valores desta série.

## RESPOSTA

# **Aplicação de Autoencoders para detecção e previsão de ultrapassagem de demanda elétrica**



Viabilidade técnica: alta

Aprendizado profundo



A utilização de modelos de aprendizado profundo para detectar e antecipar ultrapassagens de demanda elétrica é uma proposta tecnicamente viável e apresenta potencial para o desenvolvimento de uma solução de diagnóstico energético inteligente.

Minha avaliação é que **podemos utilizar um Autoencoder, mas precisamos distinguir duas tarefas diferentes: detecção de anomalias e previsão de demanda**.

Essa distinção é importante porque o Autoencoder tradicional não é, por natureza, um modelo de previsão de séries temporais. Entretanto, existem arquiteturas que permitem combinar suas características com mecanismos de previsão.

Vou estruturar a análise considerando que temos apenas uma variável de entrada: a série temporal da potência ativa, medida a cada 15 minutos.

## **1. Formulação do problema**

Considere uma unidade consumidora do Grupo A que possui uma demanda contratada de 500 kW.

Adotando a tolerância de 5% mencionada na sua definição, temos:

\\[ D\_{\text{limite}}=D\_{\text{contratada}}\times 1,05 \\]

\\[ D\_{\text{limite}}=500\times1,05=525\ kW \\]

**Exemplo de limites operacionais**

Demanda contratada

# **500 kW**

Limite com tolerância

# **525 kW**

Interpretação operacional

- Até 500 kW: dentro da demanda contratada.
- Acima de 500 até 525 kW: acima da contratada, mas dentro da margem considerada.
- Acima de 525 kW: ultrapassagem do limite de referência.

Nosso objetivo será desenvolver um sistema capaz de:

1. Aprender o comportamento histórico da demanda elétrica.
2. Identificar comportamentos anormais na série temporal.
3. Prever a potência ativa do próximo intervalo de 15 minutos.
4. Estimar a possibilidade de ultrapassagem do limite de demanda.
5. Emitir alertas preventivos para permitir ações de gerenciamento de carga.

É importante separar a previsão do resultado de faturamento: a ultrapassagem efetivamente faturável depende das regras regulatórias e contratuais aplicáveis, não apenas de uma previsão acima do limite.

## **2. É possível utilizar somente a série temporal?**

**Sim. É possível desenvolver um modelo univariado**, ou seja, um modelo que recebe exclusivamente os valores históricos da potência ativa.

Imagine que a memória de massa forneça os seguintes registros:

**Exemplo de série temporal**

Potência ativa medida a cada 15 minutos

| Horário | Potência ativa |
| ------- | -------------- |
| 08:00   | 380 kW         |
| 08:15   | 395 kW         |
| 08:30   | 410 kW         |
| 08:45   | 425 kW         |
| 09:00   | 440 kW         |
| 09:15   | 465 kW         |
| 09:30   | 490 kW         |
| 09:45   | 510 kW         |
| 10:00   | 520 kW         |
| 10:15   | ?              |

Objetivo

Prever a potência ativa das 10:15 utilizando os valores anteriores.

O modelo não precisa conhecer inicialmente:

- Demanda contratada.
- Fator de potência.
- Energia reativa.
- Temperatura ambiente.
- Quantidade de equipamentos ligados.
- Horário de funcionamento da instalação.

Essas informações podem melhorar o desempenho, mas não são obrigatórias para uma primeira implementação.

A série temporal, entretanto, precisa preservar a ordem cronológica dos registros. Recomendo também manter os timestamps, mesmo que eles não sejam utilizados inicialmente como variáveis de entrada.

### **2.1. Como preparar os dados**

Considerando medições a cada 15 minutos:

\\[ N=4\times24=96 \\]

Portanto, teremos 96 observações por dia e aproximadamente 2.880 observações em um mês de 30 dias.

Uma representação simplificada:

\\[ X=[P_1,P_2,P_3,\ldots,P_t] \\]

Onde:

- \\(P_t\\): potência ativa medida no instante \\(t\\).
- \\(t\\): índice da observação.
- Intervalo entre observações: 15 minutos.

Para alimentar uma rede neural, podemos utilizar uma janela deslizante (*sliding window*).

Por exemplo, utilizando as últimas 16 medições:

\\[ X_t=[P\_{t-15},\ldots,P\_{t-1},P_t] \\]

Essa janela representa quatro horas de histórico.

O objetivo será prever:

\\[ \hat{P}\_{t+1}=f(X_t) \\]

Ou seja, estimar a próxima medição, correspondente aos 15 minutos seguintes.

A escolha de 16 observações é apenas uma hipótese inicial. Posteriormente, podemos experimentar janelas de 32, 48, 96 ou mais observações.

## **3. Onde entra o Autoencoder?**

Um Autoencoder é uma rede neural que aprende a representar os dados de entrada em uma dimensão reduzida e depois tenta reconstruir os dados originais.

Sua arquitetura básica possui três componentes:

[What is an Autoencoder? A Complete Guide for Beginners](https://images.openai.com/static-rsc-4/cy8OTJVvqYsKnvLxVoIUoVM89emDhfbavHQprYbuxNIy1uYRqFbV-9McnZY_wHneQBStJ1-5YsBRIk1bBHr9ZBAqqumSQflrWO9SSyIJ1byoZsGgeABiLhHcxhNcDv3T1ydGlnHMntHqb2vm4ksu4Px33xatPPsm_zvmc9lRVoU?purpose=inline)

[upgrad.com](https://www.upgrad.com/blog/what-is-an-autoencoder/?utm_source=chatgpt.com)

1. **Encoder:** recebe a série temporal e comprime suas informações.
2. **Latent Space:** representa as características mais importantes que a rede aprendeu.
3. **Decoder:** utiliza essa representação para reconstruir a entrada.

### **3.1. Autoencoder para detecção de anomalias**

Aqui temos uma aplicação bastante interessante.

Podemos treinar o Autoencoder com períodos que representem o comportamento operacional normal da instalação.

Depois do treinamento, apresentamos novas janelas de medições.

O modelo tentará reconstruir essas janelas.

Quando o comportamento observado for muito diferente dos padrões aprendidos, poderá ocorrer um erro elevado de reconstrução.

Esse erro pode ser calculado pelo MSE (*Mean Squared Error*):

\\[ MSE=\frac{1}{n}\sum\_{i=1}^{n}(P_i-\hat{P}\_i)^2 \\]

Onde:

- \\(P_i\\): valor efetivamente medido.
- \\(\hat{P}\_i\\): valor reconstruído pelo Autoencoder.
- \\(n\\): quantidade de observações.

**Exemplo conceitual de detecção**

Erro de reconstrução

Normal

# **0,012**

Erro de reconstrução

Anomalia

# **0,185**

Valores ilustrativos, não são resultados de treinamento real. A decisão depende de um limiar calibrado com dados históricos.

O Autoencoder pode identificar, por exemplo:

- Picos de potência incomuns.
- Mudanças abruptas no perfil de carga.
- Comportamentos de consumo diferentes do histórico.
- Padrões operacionais atípicos.

**Uma ressalva importante:** uma ultrapassagem de demanda não é necessariamente uma anomalia estatística. Uma instalação pode apresentar consumo elevado todos os dias e ultrapassar sua demanda contratada de maneira recorrente. Por isso, precisamos de uma segunda camada de análise baseada no limite contratual.

### **3.2. Autoencoder para previsão da próxima medição**

Aqui precisamos fazer uma distinção arquitetural.

O Autoencoder tradicional reconstrói a própria entrada:

\\[ X_t\rightarrow\hat{X}\_t \\]

Mas nossa necessidade é prever uma observação futura:

\\[ X_t\rightarrow\hat{P}\_{t+1} \\]

Podemos desenvolver uma arquitetura de Autoencoder preditivo, na qual o Encoder aprende as características da janela histórica e uma camada de saída produz a previsão da próxima medição.

Uma possibilidade é:

**Entrada**

16 medições históricas de potência ativa

**Encoder**

Extração de características temporais

**Espaço latente**

Representação comprimida do comportamento da carga

**Camada de previsão**

Regressão para o próximo intervalo

# **P̂(t+1)**

**Potência ativa prevista (kW)**

Essa arquitetura pode ser treinada minimizando o erro entre a previsão e a medição real:

\\[ L=\frac{1}{N}\sum\_{i=1}^{N}(P\_{t+1}^{(i)}-\hat{P}\_{t+1}^{(i)})^2 \\]

Assim, o modelo aprende a prever a próxima medição a partir do comportamento anterior.

Uma alternativa bastante interessante é utilizar um LSTM Encoder para capturar dependências temporais, seguido de uma camada densa de regressão.

## **4. Comparação entre arquiteturas possíveis**

Eu avaliaria quatro alternativas para o projeto.

| Arquitetura             | Detecção de anomalias           | Previsão futura |
| ----------------------- | ------------------------------- | --------------- |
| Autoencoder tradicional | Excelente aplicação             | Não diretamente |
| LSTM Autoencoder        | Sim, com dependências temporais | Com adaptação   |
| LSTM Encoder + Dense    | Não é sua finalidade principal  | Sim             |
| Autoencoder preditivo   | Sim, dependendo da arquitetura  | Sim             |

Minha recomendação é experimentar inicialmente três modelos:

**Modelo A — LSTM Autoencoder**

Para aprender o comportamento histórico e detectar anomalias por erro de reconstrução.

**Modelo B — LSTM Encoder + Dense**

Para prever a potência ativa do próximo intervalo de 15 minutos.

**Modelo C — Autoencoder preditivo**

Para investigar a possibilidade de reunir aprendizado de representação e previsão em uma única arquitetura.

Isso permitirá avaliar se a utilização de uma arquitetura mais sofisticada realmente oferece vantagens em relação a modelos mais simples.

## **5. Como detectar a possibilidade de ultrapassagem?**

Esta é a parte que considero mais interessante para transformar o estudo em uma aplicação prática.

Não precisamos depender exclusivamente da capacidade de detecção de anomalias da rede neural.

Podemos combinar a previsão com uma regra determinística baseada na demanda contratada.

Considere:

\\[ D_c=500\ kW \\]

\\[ D\_{\max}=525\ kW \\]

Após receber a previsão da próxima medição, o sistema compara o resultado com esses limites.

**Simulador de previsão de demanda**

**Demanda contratada**

## **500 kW**

**Potência prevista**

## **515 kW**

Demanda contratada + 5%

# **525.0 kW**

Margem até o limite

# **10.0 kW**



Atenção: acima da demanda contratada

A previsão permanece dentro da tolerância de referência.



Simulação ilustrativa. A classificação considera somente a previsão e não representa uma apuração de faturamento.

O fluxo operacional seria:

1. Receber a nova medição de potência ativa.
2. Atualizar a janela histórica.
3. Executar o modelo de previsão.
4. Comparar a previsão com a demanda contratada.
5. Classificar o risco.
6. Gerar um alerta preventivo.

Uma evolução interessante seria trabalhar com três níveis:

- Normal: previsão abaixo da demanda contratada.
- Atenção: previsão acima da demanda contratada, mas dentro da tolerância.
- Crítico: previsão acima do limite de referência.

O sistema também pode utilizar uma margem preventiva inferior a 5%, para alertar antes que a instalação se aproxime do limite regulatório.

## **6. Cuidados técnicos e regulatórios**

Há alguns pontos que precisamos observar antes de implementar a solução.

**6.1. A medição precisa representar corretamente a demanda**

É necessário confirmar que o campo W do relatório representa a potência ativa média do intervalo de integração de 15 minutos e verificar a aplicação da constante do medidor e dos fatores dos transformadores de instrumento, quando aplicáveis.

Não devemos confundir potência instantânea com demanda média integrada.

**6.2. A regra dos 5%**

A referência de 5% para demanda contratada de consumo está prevista no artigo 301 da REN ANEEL nº 1.000/2021. A redação consolidada recebeu alterações posteriores, inclusive em 2026, mas mantém esse percentual para a demanda contratada de consumo. A avaliação também considera os postos tarifários aplicáveis.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www2.aneel.gov.br\&sz=32)

Aneel+1



Portanto, é importante que o algoritmo considere a modalidade tarifária e as demandas contratadas correspondentes.

**6.3. Poucos dados podem prejudicar o treinamento**

Embora um mês forneça aproximadamente 2.880 registros, isso pode ser insuficiente para aprender padrões operacionais complexos.

Eu procuraria obter pelo menos vários meses de dados, preferencialmente um ano ou mais, para capturar variações semanais, mensais e sazonais.

**6.4. A avaliação precisa respeitar a ordem temporal**

Não devemos dividir aleatoriamente as observações em treinamento e teste.

O correto é utilizar uma divisão cronológica, por exemplo:

- Treinamento: primeiros 70% do histórico.
- Validação: 15% seguintes.
- Teste: 15% finais.

Isso evita que o modelo aprenda com informações do futuro.

## **7. Métricas para avaliar o modelo**

Para a previsão de potência ativa, sugiro:

| Métrica | Finalidade                                                              |
| ------- | ----------------------------------------------------------------------- |
| MAE     | Erro absoluto médio em kW                                               |
| RMSE    | Penaliza erros maiores                                                  |
| MAPE    | Erro percentual médio, com ressalvas quando há valores próximos de zero |
| R²      | Avalia a capacidade explicativa                                         |

Para a detecção de anomalias e os alertas de ultrapassagem:

- Precisão (*Precision*).
- Revocação (*Recall*).
- F1-score.
- Taxa de falsos alarmes.
- Antecedência média dos alertas.

Uma métrica especialmente importante para nossa aplicação será o tempo de antecedência entre o alerta e a possível ultrapassagem.

Não basta prever corretamente: precisamos prever com antecedência suficiente para permitir alguma ação de gerenciamento de carga.

## **8. Arquitetura inicial recomendada**

Considerando a finalidade de desenvolver uma solução de diagnóstico energético inteligente, eu começaria com uma arquitetura híbrida.

**Memória de massa do medidor**

Série temporal de potência ativa (kW)

Amostragem a cada 15 minutos

**Pré-processamento**

Limpeza, normalização e janelamento temporal

**Modelo 1**

Autoencoder

Detecção de anomalias

**Erro de reconstrução**

**Modelo 2**

LSTM

Previsão da próxima medição

**Potência prevista**

**Motor de decisão**

Comparação com demanda contratada e limite de tolerância

## **Sistema de diagnóstico energético**

**Alertas e recomendações de gerenciamento de carga**

Essa arquitetura apresenta uma vantagem: os dois modelos possuem responsabilidades distintas e podem ser avaliados independentemente.

## **9. Possibilidade de pesquisa científica**

Vejo potencial para transformar essa proposta em um trabalho de pesquisa aplicada.

Uma questão de pesquisa possível seria:

> Em que medida arquiteturas de Autoencoder e redes LSTM, utilizando exclusivamente séries temporais univariadas de demanda ativa, podem antecipar ultrapassagens de demanda contratada em unidades consumidoras do Grupo A?

Podemos formular três hipóteses:

- **H1:** Autoencoders conseguem identificar padrões anormais de demanda a partir exclusivamente do histórico de potência ativa.
- **H2:** Redes LSTM conseguem prever a próxima medição de potência ativa com precisão suficiente para apoiar decisões preventivas.
- **H3:** A combinação de detecção de anomalias e previsão temporal proporciona melhores resultados para o gerenciamento preventivo de demanda do que a utilização isolada de cada abordagem.

Sugiro também comparar os modelos com uma referência simples, como a persistência (prever que a próxima medição será igual à última), para demonstrar se o aprendizado profundo realmente agrega valor.

### **Minha recomendação final**

Estratégia recomendada

Eu não começaria tentando construir um Autoencoder que faça tudo.

Desenvolveria inicialmente dois modelos independentes:

1. **LSTM Autoencoder:** aprender o comportamento da instalação e detectar anomalias.
2. **LSTM Encoder + Dense:** prever a potência ativa dos próximos 15 minutos.

Depois, integraria os resultados em um sistema de alerta preventivo.

Há ainda uma oportunidade interessante: investigar se a representação latente aprendida pelo Autoencoder melhora a qualidade da previsão quando utilizada como entrada de outro modelo.

Isso poderia constituir uma contribuição experimental relevante.

**Uma última observação:** como o objetivo é prever a demanda utilizando somente seus valores históricos, estamos diante de um problema de previsão univariada de séries temporais. Não precisamos começar com dados de dezenas de variáveis ou sistemas complexos de IoT. A própria memória de massa já oferece uma base experimental bastante interessante.

## **10. Próxima etapa sugerida**

Eu proporia desenvolver um projeto experimental em Python, seguindo uma abordagem orientada à especificação (SDD), com:

- Dataset sintético de demanda elétrica com intervalos de 15 minutos.
- Simulação de diferentes perfis de carga.
- Autoencoder para detecção de anomalias.
- LSTM para previsão da próxima medição.
- Comparação dos resultados.
- Simulador de demanda contratada e tolerância.
- Avaliação da antecedência e confiabilidade dos alertas.

Esse experimento permitirá verificar a viabilidade da solução antes de trabalhar com relatórios reais de memória de massa.

A principal questão científica que eu investigaria é: **um modelo que aprende o comportamento normal de consumo consegue antecipar uma ultrapassagem de demanda com antecedência suficiente para permitir uma intervenção operacional?**

