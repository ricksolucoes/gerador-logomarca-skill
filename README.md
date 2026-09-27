<div align="center">

# 🎨 Gerador de Logomarca

**Agent Skill para criação, estratégia, geração e revisão profissional de logomarcas e identidades visuais.**

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-OpenAI-000000.svg)](#)

</div>

---

## 📖 Visão geral

O **Gerador de Logomarca** é uma Agent Skill especializada em transformar solicitações de criação ou redesign de marcas em um processo estruturado de branding:

```text
Briefing
   ↓
Estratégia visual
   ↓
Conceitos de logotipo
   ↓
Prompt visual
   ↓
Geração
   ↓
Revisão e iteração
```

Em vez de partir diretamente para imagens ou produzir variações aleatórias, a Skill procura entender primeiro as informações necessárias sobre a marca e transformar esse contexto em decisões visuais justificadas.

O projeto contempla criação e redesign de **logomarcas, símbolos de marca, wordmarks, lettermarks, monogramas, marcas abstratas, emblemas e identidades visuais**, além de engenharia de prompts para geração de imagens e revisão estruturada de propostas.

---

## 🎯 Objetivo

A Skill foi projetada para ajudar empresas, produtos, serviços e profissionais que precisam desenvolver ou revisar uma identidade de marca com critérios claros de branding e design.

O processo prioriza:

- coerência com o posicionamento da marca;
- simplicidade com significado;
- reconhecimento;
- legibilidade;
- escalabilidade;
- aplicação em tamanhos reduzidos;
- reprodução monocromática;
- funcionamento em fundos claros e escuros;
- geometria e espaço negativo controlados;
- decisões justificadas pelo briefing.

A Skill evita transformar a criação de uma identidade visual em uma simples geração aleatória de imagens.

---

## ✨ Principais recursos

### 🔎 Descoberta de marca

A Skill identifica, quando necessário:

- nome da empresa ou marca;
- segmento e oferta;
- público-alvo;
- posicionamento;
- percepção desejada;
- personalidade;
- diferenciais;
- região ou mercado;
- concorrentes informados;
- preferências visuais;
- cores desejadas ou proibidas;
- símbolos desejados ou proibidos;
- slogan;
- aplicações prioritárias.

Informações ausentes não devem ser inventadas.

A Skill pergunta somente o que for necessário para a decisão atual, evitando transformar todo projeto em um questionário rígido.

### 🧠 Estratégia visual

O briefing é convertido em uma direção visual que pode considerar:

- conceito central;
- personalidade visual;
- estilo;
- geometria;
- composição;
- arquitetura símbolo/nome/slogan;
- tipografia;
- paleta;
- contraste;
- legibilidade;
- escalabilidade;
- aplicações;
- comportamento em fundos claros e escuros.

As decisões relevantes devem possuir relação explícita com o briefing.

### ✏️ Conceitos de logotipo

Dependendo do projeto, a Skill pode trabalhar com:

| Tipo | Aplicação |
|---|---|
| **Wordmark** | Marca baseada principalmente no nome |
| **Lettermark** | Construção baseada em letras ou iniciais |
| **Monograma** | Combinação estruturada de iniciais |
| **Símbolo + nome** | Elemento gráfico acompanhado do nome |
| **Marca abstrata** | Símbolo conceitual não literal |
| **Emblema** | Elementos integrados em uma composição |
| **Combinação** | Arquitetura composta conforme o briefing |

Os conceitos devem representar hipóteses de branding diferentes, e não apenas mudanças superficiais de cor ou ícone.

### 🖼️ Engenharia de prompt

Quando uma direção visual estiver suficientemente definida, a Skill pode produzir prompts específicos para geração de logomarcas.

Quando apropriado, são privilegiadas características como:

- `flat design`;
- `vector style`;
- `clean geometry`;
- `strong silhouette`;
- `balanced negative space`;
- `solid colors`;
- `professional typography`;
- `high legibility`;
- `scalable mark`;
- fundo branco ou neutro;
- apresentação adequada para revisão de identidade.

Por padrão, procura-se evitar elementos que prejudiquem a leitura ou reprodução da marca, como excesso de mockups, fotografia, 3D decorativo, efeitos metálicos, sombras pesadas, glow, texturas e detalhes excessivos.

### 🎨 Geração de imagem

Quando o usuário pede efetivamente para **criar, gerar, desenhar ou visualizar** a logomarca e existe uma direção visual suficiente, a Skill pode utilizar a ferramenta de geração de imagens disponibilizada pelo host.

O fluxo diferencia explicitamente:

```text
Conceito ≠ Prompt ≠ Imagem gerada ≠ Revisão
```

Se o ambiente não possuir uma ferramenta adequada de geração, a Skill pode entregar o prompt final sem afirmar que uma imagem foi criada.

### 🔍 Revisão de logotipo

Uma proposta, imagem ou redesign pode ser analisado considerando:

- coerência com o briefing;
- legibilidade;
- equilíbrio;
- composição;
- reconhecimento;
- adequação ao segmento;
- escalabilidade;
- favicon e avatar;
- monocromia;
- fundos claros e escuros;
- originalidade conceitual.

A revisão separa observações, riscos e recomendações de alteração.

---

## 🔄 Workflow

O comportamento principal está organizado em seis estados.

```text
1. Descoberta
      ↓
2. Estratégia visual
      ↓
3. Conceitos de logotipo
      ↓
4. Prompt visual
      ↓
5. Geração de imagem
      ↓
6. Revisão e iteração
```

A progressão ocorre conforme existam informações suficientes para justificar a próxima etapa.

Se houver uma contradição relevante no briefing, o fluxo pode retornar à descoberta.

Mudanças que alterem posicionamento, personalidade ou metáfora central retornam à estratégia antes de uma nova execução visual.

---

## 💬 Exemplos de uso

### Criar uma marca

```text
Crie uma logomarca para minha empresa de manutenção industrial.
```

### Desenvolver identidade visual

```text
Quero desenvolver a identidade visual da marca Nexo Norte.
```

### Trabalhar a partir de um briefing

```text
Tenho este briefing. Proponha três caminhos conceituais de logo.
```

### Criar um monograma

```text
Preciso de um monograma para a marca Aurora Capital.
```

### Gerar o prompt de uma direção aprovada

```text
Aprovado o conceito do monograma NN geométrico em azul escuro.
Crie o prompt final para gerar a imagem.
```

### Gerar a logomarca

```text
Gostei da direção 1. Agora gere e mostre a logomarca.
```

### Revisar uma marca existente

```text
Revise este logo para uso em favicon, bordado e papel timbrado.
```

---

## 🚦 Quando a Skill deve ser utilizada

A Skill foi projetada para solicitações cujo objetivo principal seja uma **identidade de marca** ou um **sistema de logo**.

Exemplos:

- criação de logomarca;
- redesign de logo;
- identidade visual;
- símbolo de marca;
- monograma;
- wordmark;
- lettermark;
- emblema;
- definição de direção visual;
- paleta associada à identidade;
- tipografia de marca;
- prompt para geração de logomarca;
- revisão de logo.

---

## ⛔ Quando não utilizar

A Skill não foi projetada para trabalhos visuais sem relação principal com identidade de marca, como:

- fotografia;
- ilustração genérica;
- banners publicitários isolados;
- desenho técnico;
- dúvidas genéricas de Photoshop ou Illustrator;
- ícones funcionais de interface;
- edição cosmética de fotografias;
- vetorização puramente técnica sem redesign;
- peças promocionais isoladas com identidade já definida.

Em casos ambíguos, o objetivo final do usuário determina se o workflow de branding é apropriado.

---

## 🛡️ Propriedade intelectual

Referências a marcas existentes podem ser utilizadas para identificar **atributos abstratos**, como minimalismo, geometria, densidade, contraste, tom e categoria tipográfica.

Essas referências não devem ser utilizadas para reproduzir deliberadamente símbolos, lettering característico, composições proprietárias, trade dress ou combinações visualmente reconhecíveis de outra marca.

A Skill também não afirma que uma proposta é juridicamente exclusiva, registrável, disponível para registro ou livre de conflito com marcas existentes.

Pesquisa de anterioridade e registrabilidade exige procedimento apropriado e fontes específicas.

---

## 🧱 Arquitetura do projeto

```text
gerador-logomarca-skill/
├── README.md
├── LICENSE
├── standalone/
│   └── gerador-logomarca/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       ├── references/
│       │   ├── activation-policy.md
│       │   ├── branding-workflow.md
│       │   ├── logo-design-principles.md
│       │   ├── prompt-engineering.md
│       │   └── review-checklist.md
│       ├── scripts/
│       │   └── validate_skill_contract.py
│       └── tests/
│           ├── README.md
│           └── cases.json
└── plugin/
    └── gerador-logomarca-plugin/
        ├── plugin.json
        └── skills/
            └── gerador-logomarca/
```

O `SKILL.md` concentra o workflow principal, enquanto `references/` aplica progressive disclosure aos detalhes especializados.

| Referência | Responsabilidade |
|---|---|
| `activation-policy.md` | Critérios de ativação, não ativação e fronteiras |
| `branding-workflow.md` | Descoberta, estratégia e desenvolvimento de conceitos |
| `logo-design-principles.md` | Princípios formais e critérios de qualidade |
| `prompt-engineering.md` | Construção de prompts para geração visual |
| `review-checklist.md` | Critérios estruturados de revisão |

---

## 📦 Instalação

### Skill standalone

O conteúdo utilizado como Skill independente está em:

```text
standalone/gerador-logomarca/
```

Instale o diretório `gerador-logomarca/` no local de Skills reconhecido pelo host utilizado.

O mecanismo exato de descoberta e instalação depende do ambiente compatível com Agent Skills.

### Plugin portátil

A distribuição de plugin está em:

```text
plugin/gerador-logomarca-plugin/
```

O pacote contém o manifesto `plugin.json` e a Skill em `skills/gerador-logomarca/`.

O manifesto identifica atualmente o plugin como versão **1.0.1**.

---

## ⚙️ Dependências

O projeto não depende de bibliotecas Python externas para sua validação local.

O script `validate_skill_contract.py` utiliza a biblioteca padrão do Python.

Recursos como geração ou edição de imagens dependem das capacidades disponibilizadas pelo host onde a Skill estiver sendo executada.

---

## 🧪 Testes

O projeto possui **18 casos declarativos** em:

```text
standalone/gerador-logomarca/tests/cases.json
```

A cobertura inclui ativação positiva e negativa, briefing incompleto e completo, alteração de conceito, referência a marca existente, criação de prompt, geração de imagem, revisão, fronteiras e regressão relacionada a afirmações jurídicas.

---

## ✅ Validação local

A partir do diretório da Skill standalone:

```bash
cd standalone/gerador-logomarca
python3 scripts/validate_skill_contract.py
python3 -S scripts/validate_skill_contract.py
```

Para validar também o plugin e sua paridade com a Skill standalone:

```bash
python3 scripts/validate_skill_contract.py \
  --plugin-root ../../plugin/gerador-logomarca-plugin

python3 -S scripts/validate_skill_contract.py \
  --plugin-root ../../plugin/gerador-logomarca-plugin
```

O validador verifica deterministicamente aspectos como front matter, identidade da Skill, referências obrigatórias, estrutura utilizada em `agents/openai.yaml`, casos de teste, artefatos temporários, manifesto do plugin, layout e equivalência entre standalone e plugin.

---

## ⚠️ Limites dos testes locais

Os casos presentes em `tests/cases.json` funcionam como **eval cases declarativos**.

O validador local não tenta reproduzir o roteador semântico do ChatGPT, Codex ou de outro host e não julga automaticamente a qualidade das respostas geradas.

```text
Validação estrutural local
          ≠
Avaliação semântica no host
```

Para avaliação funcional completa, os casos devem ser executados em um host compatível, verificando ativação, comportamento esperado, falsos positivos, falsos negativos, invenção de informações e regressões.

---

## 🤝 Contribuindo

Ao alterar comportamento, workflow ou política de ativação:

1. mantenha `SKILL.md` e referências coerentes;
2. atualize os casos afetados em `tests/cases.json`;
3. evite duplicação desnecessária de regras;
4. execute o validador;
5. execute também a validação com `python3 -S`;
6. valide a paridade entre standalone e plugin quando ambos forem alterados.

Contribuições devem preservar o princípio central do projeto: **decisões de identidade visual devem ser fundamentadas no briefing, e informações ausentes não devem ser inventadas**.

---

## 📄 Licença

Este projeto é distribuído sob a **MIT License**.

Consulte [LICENSE](LICENSE) para os termos completos.

Copyright © 2026 Rick Soluções.

---

<div align="center">

**Gerador de Logomarca · Agent Skill para branding e identidade visual**

</div>
