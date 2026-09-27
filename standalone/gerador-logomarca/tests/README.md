# Testes e evals

`cases.json` contém **18 casos declarativos** para avaliação de ativação e comportamento: positivos, negativos, briefing incompleto/completo, mudança de conceito, referência a marca existente, criação de prompt, pedido efetivo de imagem, revisão, fronteiras e regressão de segurança.

## O que o validador local comprova

O script `scripts/validate_skill_contract.py` valida deterministicamente:

- front matter e identidade da Skill;
- referências obrigatórias e links locais citados no `SKILL.md`;
- estrutura do subconjunto utilizado em `agents/openai.yaml`;
- sintaxe e cobertura estrutural de `tests/cases.json`;
- ausência de artefatos temporários;
- quando `--plugin-root` é informado: `plugin.json`, layout `skills/gerador-logomarca/` e equivalência byte a byte entre standalone e Skill empacotada.

Execute da raiz da Skill standalone:

```bash
python3 scripts/validate_skill_contract.py
python3 -S scripts/validate_skill_contract.py
```

Para validar também o plugin e a paridade, informe a raiz do plugin:

```bash
python3 scripts/validate_skill_contract.py --plugin-root /caminho/para/gerador-logomarca-plugin
python3 -S scripts/validate_skill_contract.py --plugin-root /caminho/para/gerador-logomarca-plugin
```

## O que exige host/modelo real

Os campos `prompt`, `expected_activation` e `expect` são **eval cases**, não asserts executados pelo script local. O validador não tenta reproduzir o roteador semântico do ChatGPT/Codex nem julgar respostas geradas.

Para validar funcionalmente, instale a Skill/plugin em um host compatível e execute cada caso em uma conversa limpa. Para cada caso, registre separadamente:

1. se a Skill foi considerada/ativada conforme `expected_activation`;
2. se a resposta satisfez todos os itens de `expect`;
3. qualquer falso positivo, falso negativo, invenção de briefing ou regressão;
4. host/modelo e versão/data usados na avaliação.

Casos com `expected_activation: "ambiguous"` devem ser avaliados pela decisão contextual descrita em `expect`, não como aprovação automática de ativação.

**Limitação explícita:** sem um evaluation harness/roteador real do host disponível neste repositório, ativação semântica e qualidade comportamental não podem ser comprovadas por testes locais.
