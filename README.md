# Projetos em Python

![Status](https://img.shields.io/badge/status-arquivo%20de%20estudos-64748b)
![Python](https://img.shields.io/badge/Python-3.9%2B-2563eb)
![Selenium](https://img.shields.io/badge/Selenium-automa%C3%A7%C3%B5es-16a34a)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Web-22c55e)
![Instagram](https://img.shields.io/badge/Instagram-bots-e11d48)

Repositório com pequenos sistemas em Python para estudo e uso pessoal. Cada pasta raiz representa um sistema independente, com seu próprio README, scripts e dependências.

> Use estes scripts com responsabilidade. Automações em plataformas como WhatsApp, Instagram e Google podem quebrar com mudanças de interface e devem respeitar termos de uso, limites de envio e privacidade dos usuários.

## Como o repositório está organizado

Este projeto está mais próximo de um monorepo de automações do que de um pacote Python único. Por isso, a organização recomendada é manter cada sistema isolado em sua própria pasta:

- `busca_automatica_google/`: automação de buscas no Google com Selenium.
- `instagrambot/`: scripts de automação para Instagram.
- `whatsappbot/`: scripts simples de envio pelo WhatsApp Web.
- `wppmessage/`: aplicação desktop PyQt5 para envio/agendamento de mensagens.

O utilitário `decifra_base64.py` foi movido para a branch `legacy` e não faz parte da branch principal.

## Projetos

| Sistema | Descrição | Como instalar | Documentação |
| ------- | --------- | ------------- | ------------ |
| `busca_automatica_google/` | Automação de busca e navegação no Google. | `pip install -r busca_automatica_google/requirements.txt` | [`README`](busca_automatica_google/README.md) |
| `instagrambot/` | Bots para curtir, comentar, seguir e coletar dados do Instagram. | `pip install -r instagrambot/requirements.txt` | [`README`](instagrambot/README.md) |
| `whatsappbot/` | Scripts para envio automatizado de mensagens no WhatsApp Web. | `pip install -r whatsappbot/requirements.txt` | [`README`](whatsappbot/README.md) |
| `wppmessage/` | Aplicação desktop para envio/agendamento de mensagens no WhatsApp. | `pip install -r wppmessage/requirements.txt` | [`README`](wppmessage/README.md) |

## Estrutura

```text
python/
├── busca_automatica_google/
│   ├── README.md
│   ├── busca_google.py
│   ├── requirements.txt
│   └── screen.png
├── instagrambot/
│   ├── README.md
│   ├── requirements.txt
│   └── *.py
├── whatsappbot/
│   ├── README.md
│   ├── requirements.txt
│   └── *.py
├── wppmessage/
│   ├── README.md
│   ├── requirements.txt
│   ├── imagens/
│   ├── versao1_0_single_number/
│   └── versao1_1_multiple_numbers/
├── .gitignore
└── README.md
```

## Quick Start

### Requisitos

- Python 3.9+
- `pip`
- Google Chrome, para scripts que usam Chrome/WhatsApp Web/Google
- Firefox, para scripts do Instagram
- Conta logada no WhatsApp Web quando o sistema depender disso

### 1. Clonar o repositório

```bash
git clone git@github.com:flaviooliveira-code/python.git
cd python
```

### 2. Criar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar somente o sistema desejado

Exemplo:

```bash
pip install -r whatsappbot/requirements.txt
```

Evite instalar dependências globais para todos os sistemas ao mesmo tempo. Os scripts têm finalidades diferentes e algumas bibliotecas exigem permissões específicas do sistema operacional.

## Execução

### Busca Automática Google

```bash
cd busca_automatica_google
python3 busca_google.py
```

Antes de executar, revise no script:

- palavras-chave;
- link alvo;
- quantidade de páginas;
- comportamento de proxy/navegação.

### Instagram Bot

```bash
cd instagrambot
python3 instagrambot.py
```

Outros scripts disponíveis:

```bash
python3 instagram_curtir_fotos.py
python3 instagrambot_baixa_seguidores.py
python3 instagrambot_segue_following.py
python3 instagrambot_seguidores_lista_excel_mais_que_1_comentario.py
```

### WhatsApp Bot

```bash
cd whatsappbot
python3 whatsappbot.py
```

Outros scripts disponíveis:

```bash
python3 whatsappbot-listadecontatos.py
python3 whasappbot-listadecontato-EXCEL.py
```

### WppMessage

Envio para um número:

```bash
cd wppmessage/versao1_0_single_number
python3 wppmessage.py
```

Envio para múltiplos números:

```bash
cd wppmessage/versao1_1_multiple_numbers
python3 wppmessage.py
```

## Boas práticas para manter este repositório

- Mantenha cada sistema com seu próprio `requirements.txt`.
- Evite credenciais, tokens e caminhos pessoais fixos nos scripts.
- Antes de rodar automações de mensagem, revise contatos, textos e horários.
- Scripts com Selenium dependem da estrutura atual da página; mudanças no Google, Instagram ou WhatsApp Web podem exigir atualização de seletores.
- No macOS, automações com `keyboard` podem exigir permissões de acessibilidade.
- Se um sistema crescer, crie subpastas internas como `src/`, `data/`, `assets/` e `docs/` apenas dentro daquele sistema.

## Autor

Flávio Oliveira

- GitHub: [flaviooliveira-code](https://github.com/flaviooliveira-code)
