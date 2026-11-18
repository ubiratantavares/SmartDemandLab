# VISION.md

## Propósito

Desenvolver uma plataforma de simulação e controle de demanda elétrica que preveja carga a cada 15 min, forneça intervalos de confiança de 99 % e permita ações preventivas para não ultrapassar 
a demanda contratada (DAC).

## Objetivos

1. Previsão precisa – modelos de série temporal com ponto estimado e intervalo de 99 % (PI₉₉).

2. Gestão de risco – usar o limite superior do PI para acionar controle, respeitando tolerância regulatória de 5 % (1,05 × DAC).

3. Reprodutibilidade – gerador de dados sintéticos configurável por seed.

4. Qualidade de software – arquitetura orientada a objetos (SOLID), tipagem estática (mypy) e cobertura de testes ≥ 80 % (pytest).

5. Gerenciamento de dependências – utilizar o gerenciador **uv**.

## Escopo

- Domínio: instalações de média/alta tensão.

- Entradas: série temporal de potência ativa (kW) a cada 15 min.

- Saídas: `point_estimate_kw`, `lower_bound_kw`, `upper_bound_kw`, `coverage_percent`.

- Limites operacionais: DAC e 1,05 × DAC (tolerância regulatória).

## Benefícios

- Redução de multas por ultrapassagem.

- Melhor aproveitamento da capacidade instalada.

- Base de pesquisa para modelos preditivos e estratégias de controle.

## Stakeholders

Engenheiros de eficiência energética, gestores de operação de distribuição, equipe de desenvolvimento, reguladores (ANEEL).

## Restrições

- Implementação em Python em ambiente Linux.

- Sem integração hardware nesta fase.

- Tolerância de 5 % configurável, padrão conforme ANEEL Resolução 1000/2021.

## Métricas de sucesso

- Cobertura empírica de PI₉₉ ≥ 99 %.

- Redução de ultrapassagens ≥ 30 %.

- Cobertura de testes automatizados ≥ 80 %.

- Inferência de modelo < 50 ms.
