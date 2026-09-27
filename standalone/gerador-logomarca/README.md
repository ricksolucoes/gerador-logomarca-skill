# Gerador de Logomarca

Agent Skill para transformar pedidos de logomarca e identidade visual em um processo profissional de **briefing → estratégia → conceitos → prompt/geração → revisão**.

## Para quem serve

Empresas, produtos, serviços e profissionais que precisam criar ou redesenhar uma identidade de marca com decisões justificadas, em vez de gerar imagens aleatórias imediatamente.

## O que resolve

- coleta apenas o briefing necessário e não inventa dados ausentes;
- converte posicionamento em direção visual;
- propõe wordmarks, lettermarks, monogramas, símbolos, marcas abstratas, emblemas e combinações com justificativa;
- cria prompts profissionais para geração de imagens;
- usa geração/edição de imagem quando o host oferece a ferramenta e o usuário efetivamente solicita a imagem;
- revisa legibilidade, equilíbrio, reconhecimento, escalabilidade, monocromia e coerência;
- evita cópia deliberada de marcas existentes e não promete registrabilidade.

## Arquitetura

```text
gerador-logomarca/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── activation-policy.md
│   ├── branding-workflow.md
│   ├── logo-design-principles.md
│   ├── prompt-engineering.md
│   └── review-checklist.md
├── scripts/
│   └── validate_skill_contract.py
└── tests/
    ├── README.md
    └── cases.json
```

`SKILL.md` mantém o workflow principal; detalhes são carregados progressivamente das referências. O único script existe para validação determinística do contrato e usa apenas a biblioteca padrão do Python.

## Instalação standalone

Coloque o diretório `gerador-logomarca/` em um local de Skills reconhecido pelo host. Em ambientes OpenAI Agents API, registre o diretório pai como capability directory conforme a documentação do host. Em outros hosts compatíveis com Agent Skills, siga o mecanismo de descoberta correspondente.

## Plugin portátil

O pacote de plugin entregue contém `plugin.json` na raiz e a Skill em `skills/gerador-logomarca/`. Não há MCP, hooks ou assets artificiais: a Skill usa as capacidades que o host já disponibilizar, inclusive geração de imagens quando presente.

## Exemplos de uso

- `Crie uma logomarca para minha empresa de manutenção industrial.`
- `Quero desenvolver a identidade visual da marca Nexo Norte.`
- `Tenho este briefing; proponha três caminhos conceituais de logo.`
- `Aprovado o conceito 2. Crie o prompt profissional para gerar a imagem.`
- `Agora gere e visualize essa logomarca.`
- `Revise este logo para favicon, uniforme e papel timbrado.`

## Comportamento esperado

A Skill não deve pular para a imagem quando decisões críticas estiverem ausentes. Ela pergunta somente o necessário, sintetiza o briefing, cria estratégia e conceitos fundamentados e só passa à geração quando houver pedido efetivo e capacidade disponível no host.

## Segurança e propriedade intelectual

Referências a marcas existentes podem orientar atributos abstratos — por exemplo minimalismo ou geometria — mas não autorizam reprodução de símbolo, lettering, composição ou trade dress reconhecível. A Skill não afirma que um logo é juridicamente exclusivo, registrável ou livre de conflito sem pesquisa apropriada.

## Testes e validação

Execute:

```bash
python3 scripts/validate_skill_contract.py
python3 -S scripts/validate_skill_contract.py
```

Os testes locais verificam contrato, estrutura e cobertura declarativa. A seleção semântica real da Skill deve ser avaliada em um host compatível com os prompts de `tests/cases.json`; o validador não tenta reproduzir o roteador proprietário.

## Estrutura de testes

O conjunto cobre ativação positiva e negativa, briefing incompleto/completo, iteração, referência a marca existente, prompt, geração de imagem, revisão, casos de fronteira e segurança.

## Contribuição

Ao alterar o workflow, atualize os casos de teste afetados e execute o validador com e sem `site-packages` (`python3 -S`). Evite duplicar regras entre `SKILL.md` e referências; mantenha cada arquivo com responsabilidade própria.

## Licença

Nenhuma licença de distribuição foi definida neste pacote. Defina uma licença antes de publicação pública se necessário.
