# Protocolo da RSL — Mitigação de viés sem retreino em modelos que aprendem em contexto
Data de definição: 2026-10-21. Diretrizes: Kitchenham & Charters (2007); relato conforme PRISMA 2020.

## Questão principal (QP)
Quais métodos de mitigação de viés social que não atualizam os pesos do modelo (aplicados em tempo de inferência) foram propostos para modelos de fundação que aprendem em contexto (LLMs e TFMs), e como eles são avaliados?

PICO: P = LLMs/TFMs usados via prompt/aprendizado em contexto; I = mitigação sem atualização de pesos; C = (opcional) baselines como ajuste fino / sem intervenção; O = métricas de justiça e de desempenho.

## Questões secundárias
- QS1 Em que ponto do pipeline intervêm (contexto/prompt; representações internas; saída/decodificação)?
- QS2 Que informação sobre atributos sensíveis exigem, e em que momento (inferência, calibração, nenhum)?
- QS3 Como são avaliados (métricas de justiça, benchmarks, custo em desempenho)?
- QS4 Em que tipo de tarefa e família de modelo são aplicados (geração vs. classificação/decisão; LLM vs. TFM)?

## Critérios de inclusão (CI)
- CI1 Propõe ou avalia empiricamente um método de mitigação de viés social (grupos demográficos).
- CI2 O método não atualiza os pesos do modelo-base (componentes auxiliares leves permitidos, desde que o modelo-base fique congelado).
- CI3 Modelo-alvo é LLM (prompting/ICL) ou TFM tabular baseado em ICL.
- CI4 Publicado entre 2020 e 2026, em inglês ou português.
- CI5 Texto completo acessível (artigo revisado por pares ou preprint no arXiv).

## Critérios de exclusão (CE)
- CE1 Requer atualização de pesos (ajuste fino, LoRA, RLHF/DPO, pré-treinamento).
- CE2 Apenas mede/audita viés, sem propor ou avaliar mitigação.
- CE3 "Viés" não social (ex.: viés de rótulo/maioria em ICL, viés posicional) sem avaliação de justiça entre grupos.
- CE4 Modelos fora do escopo (só visão, word embeddings estáticos, encoders tipo BERT sem uso via prompt).
- CE5 Survey, position paper, tutorial ou resumo estendido (usados apenas como contexto/snowballing).
- CE6 Duplicata ou versão anterior de estudo já incluído.
- CE7 Fora do tema (não trata de viés/justiça), incluindo páginas não acadêmicas (agregadores, blogs).
- (CI4 não atendido = fora do período.)

## Fontes
Mecanismo de busca web (WebSearch) com filtros de domínio: arxiv.org; aclanthology.org; openreview.net; proceedings.neurips.cc / proceedings.mlr.press; dl.acm.org. Mais busca sem filtro e snowballing (backward/forward) a partir dos incluídos e de surveys.

## String genérica
("large language model*" OR LLM OR "in-context learning" OR "tabular foundation model*" OR TabPFN OR TabICL)
AND (bias OR fairness OR stereotyp*)
AND ("inference-time" OR "test-time" OR "training-free" OR "without fine-tuning" OR "post-hoc" OR prompting OR "activation steering" OR "attention steering" OR decoding)
AND (mitigat* OR debias*)
Adaptação: o mecanismo web não aceita booleanos completos; a string foi decomposta em consultas por combinação de blocos (ver log).

## Qualidade (0 / 0,5 / 1 cada; total 0–5)
Q1 Objetivo e método claramente descritos; Q2 Baselines adequados (sem intervenção + ao menos 1 método de mitigação); Q3 Mais de um modelo/benchmark; Q4 Reporta custo em desempenho/utilidade; Q5 Código disponível.
Alto ≥ 4; médio 2,5–3,5; baixo ≤ 2.

## Extração
ID, referência, ano, venue/tipo, objetivo, método, ponto de intervenção, acesso a atributo sensível, família de modelo, tipo de tarefa, modelos testados, benchmarks, métricas de justiça, métricas de utilidade, principais resultados, limitações declaradas, código, escore de qualidade.
