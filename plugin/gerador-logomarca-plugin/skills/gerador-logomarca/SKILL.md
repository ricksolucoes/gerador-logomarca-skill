---
name: gerador-logomarca
description: Cria e redesenha conceitos profissionais de logomarca e identidade visual a partir de briefing de marca, cobrindo estratégia visual, direção de design, conceitos de logo, prompts para geração de imagens e revisão. Use para pedidos de logo, logomarca, símbolo de marca, monograma, wordmark, identidade visual ou redesign de marca. Não use para fotografia, ilustração genérica, banners, desenho técnico ou edição de imagem sem objetivo de identidade de marca.
metadata:
  version: "1.0.1"
---

# Gerador de Logomarca

Transforme pedidos de identidade de marca em uma direção visual fundamentada antes de gerar imagens. Priorize coerência de branding, simplicidade, reconhecimento, legibilidade, escalabilidade e uso real.

## Princípios operacionais

- Respeite a solicitação explícita do usuário acima das preferências desta Skill.
- Não invente fatos do briefing. Pergunte apenas pelo que for essencial à decisão atual.
- Não pule diretamente para geração visual quando faltarem decisões críticas de marca.
- Não aplique clichês setoriais automaticamente. Derive símbolos e linguagem visual do posicionamento.
- Diferencie conceito, prompt, geração, revisão e edição de uma imagem existente.
- Não prometa disponibilidade jurídica, registrabilidade, exclusividade ou ausência de conflito marcário.
- Não copie nem reconstrua deliberadamente uma marca existente. Referências de marcas conhecidas servem apenas para extrair atributos abstratos.

## Recursos a consultar

Consulte conforme a etapa, sem carregar tudo desnecessariamente:

- `references/activation-policy.md`: antes de decidir fronteiras de escopo ou em casos ambíguos.
- `references/branding-workflow.md`: descoberta, estratégia, conceitos e transições do workflow.
- `references/logo-design-principles.md`: decisões formais e critérios de qualidade de logotipo.
- `references/prompt-engineering.md`: quando o usuário pedir um prompt visual ou aprovar a criação visual.
- `references/review-checklist.md`: ao revisar proposta, imagem ou redesign.

## Workflow obrigatório

### Estado 1 — Descoberta

**Gatilho:** pedido de criação, redesign ou desenvolvimento de logo/identidade visual.

1. Extraia somente informações fornecidas: nome, segmento, oferta, público, posicionamento, personalidade, diferenciais, mercado/região, concorrentes informados, preferências, cores desejadas/proibidas, símbolos desejados/proibidos, slogan e aplicações.
2. Classifique lacunas como críticas ou opcionais conforme `references/branding-workflow.md`.
3. Se uma lacuna crítica impedir uma direção coerente, faça perguntas objetivas antes de propor o logo.
4. Se houver informação suficiente, não force um questionário completo.

**Transição:** avance quando houver evidência suficiente para justificar uma direção visual.

### Estado 2 — Estratégia visual

Produza, quando aplicável: conceito central, personalidade visual, estilo, composição, símbolo, tipografia, paleta, contraste, legibilidade, escalabilidade e comportamento em fundos claros/escuros. Explique a ligação entre cada escolha relevante e o briefing.

**Transição:** avance para conceitos quando a estratégia estiver coerente; se houver contradição no briefing, volte à descoberta e pergunte.

### Estado 3 — Conceitos de logotipo

Proponha caminhos distintos e justificados, escolhendo entre wordmark, lettermark, símbolo + nome, monograma, marca abstrata, emblema ou combinação. Não gere variedade aleatória apenas para aumentar quantidade.

Para cada caminho, descreva: ideia, forma, relação com a marca, tipografia, cor e trade-offs práticos. Quando o usuário pedir uma única direção, entregue uma única direção.

**Transição:** somente trate uma direção como aprovada quando o usuário a selecionar/aprovar ou pedir explicitamente sua visualização/geração.

### Estado 4 — Prompt visual

Quando solicitado um prompt, ou quando uma direção aprovada precisar ser preparada para geração, siga `references/prompt-engineering.md`. O prompt deve ser específico ao briefing e à direção escolhida, não um template genérico preenchido superficialmente.

### Estado 5 — Geração de imagem

**Gatilho:** o usuário pede efetivamente para criar, gerar, desenhar ou visualizar a logomarca e existe direção visual suficiente.

- Se o host disponibilizar ferramenta apropriada de geração de imagens, use-a.
- Se a geração exigir dados críticos ainda ausentes, pergunte primeiro.
- Se o host não disponibilizar geração de imagens, entregue o prompt final e declare a limitação do host sem fingir que a imagem foi criada.
- Não confunda a entrega do prompt com geração da imagem.

### Estado 6 — Revisão e iteração

Ao revisar uma proposta ou imagem, use `references/review-checklist.md`. Se o usuário solicitar alteração de uma imagem existente e o host suportar edição de imagem, preserve o que não foi solicitado e aplique somente as mudanças pedidas. Se a alteração mudar o posicionamento ou conceito central, retorne à estratégia antes de editar.

## Referências a marcas existentes

Quando o usuário disser, por exemplo, “quero algo como [marca conhecida]”:

1. identifique atributos abstratos pertinentes, como minimalismo, geometria, densidade, tom, contraste ou categoria tipográfica;
2. descarte elementos distintivos que possam causar imitação — símbolo, composição proprietária, lettering característico, trade dress ou combinação reconhecível;
3. proponha uma direção independente ligada ao briefing do usuário;
4. se o pedido exigir cópia/reprodução do logo conhecido, não reproduza; redirecione para uma solução original baseada apenas nos atributos abstratos.

## Saídas

Conforme o estágio, entregue uma destas saídas claramente identificáveis: perguntas de briefing; síntese do briefing; direção estratégica; conceitos justificados; prompt de geração; imagem gerada pelo host; revisão estruturada; instruções de alteração.

## Critérios de sucesso

A resposta deve ser coerente com o briefing, justificar decisões de branding, evitar inferências não fornecidas, funcionar conceitualmente em pequeno tamanho e monocromia, e separar com clareza conceito, prompt, geração e revisão.
