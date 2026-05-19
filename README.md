# Projetos em Python

![Status](https://img.shields.io/badge/status-arquivo%20de%20estudos-64748b)
![Python](https://img.shields.io/badge/Python-3.9%2B-2563eb)
![Selenium](https://img.shields.io/badge/Selenium-automa%C3%A7%C3%B5es-16a34a)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Web-22c55e)
![Instagram](https://img.shields.io/badge/Instagram-bots-e11d48)

Repositório com scripts, bots e automações em Python para estudo e uso pessoal, incluindo automações com Selenium, WhatsApp Web, Instagram, interface desktop com PyQt5 e utilitários simples.

> Use estes scripts com responsabilidade. Automações em plataformas como WhatsApp, Instagram e Google podem quebrar com mudanças de interface e devem respeitar termos de uso, limites de envio e privacidade dos usuários.

## Sumário

- [Status do Projeto](#status-do-projeto)
- [Stack](#stack)
- [Projetos](#projetos)
- [Estrutura](#estrutura)
- [Quick Start](#quick-start)
- [Instalação por Módulo](#instalação-por-módulo)
- [Execução](#execução)
- [Dependências](#dependências)
- [Observações Importantes](#observações-importantes)
- [Manutenção](#manutenção)
- [Autor](#autor)

## Status do Projeto

Este repositório funciona como uma coleção de automações antigas e utilitários em Python. Alguns scripts foram escritos para versões anteriores de Selenium e podem exigir ajustes nos seletores ou na inicialização do driver conforme a versão atual do navegador.

| Área                     | Status                                           |
| ------------------------ | ------------------------------------------------ |
| Busca automática Google  | Script disponível, depende de ajustes Selenium   |
| Instagram Bot            | Scripts disponíveis, dependem da interface atual |
| WhatsApp Bot             | Scripts disponíveis para WhatsApp Web            |
| WppMessage               | App desktop com PyQt5 para envio agendado        |
| Utilitário Base64        | Script simples funcional                         |

## Stack

**Linguagem**

- Python 3.9+

**Automação**

- Selenium
- WebDriver Manager
- Google Chrome / ChromeDriver
- Firefox / GeckoDriver

**WhatsApp**

- PyWhatKit
- Keyboard

**Dados**

- Pandas
- OpenPyXL
- XLRD

**Interface desktop**

- PyQt5
- PySimpleGUI

## Projetos

| Projeto | Descrição | Documentação |
| ------- | --------- | ------------ |
| `busca_automatica_google/` | Automação de buscas no Google com Selenium e navegação por resultados. | [`README`](busca_automatica_google/README.md) |
| `instagrambot/` | Bots para curtir, comentar, seguir e coletar dados do Instagram. | [`README`](instagrambot/README.md) |
| `whatsappbot/` | Scripts para envio automatizado de mensagens no WhatsApp Web. | [`README`](whatsappbot/README.md) |
| `wppmessage/` | Aplicação desktop para agendar/envio de mensagens no WhatsApp. | [`README`](wppmessage/README.md) |
| `decifra_base64.py` | Utilitário de terminal para decodificar strings Base64. | Script único |

## Estrutura

```text
python/
├── busca_automatica_google/
│   ├── README.md
│   ├── busca_google.py
│   └── screen.png
├── instagrambot/
│   ├── README.md
│   ├── instagram_curtir_fotos.py
│   ├── instagrambot.py
│   ├── instagrambot_baixa_seguidores.py
│   ├── instagrambot_segue_following.py
│   └── instagrambot_seguidores_lista_excel_mais_que_1_comentario.py
├── whatsappbot/
│   ├── README.md
│   ├── whatsappbot.py
│   ├── whatsappbot-listadecontatos.py
│   └── whasappbot-listadecontato-EXCEL.py
├── wppmessage/
│   ├── README.md
│   ├── imagens/
│   ├── versao1_0_single_number/
│   └── versao1_1_multiple_numbers/
├── decifra_base64.py
└── README.md
```

## Quick Start

### Requisitos

- Python 3.9+
- `pip`
- Google Chrome, para scripts que usam Chrome/WhatsApp Web/Google
- Firefox, para scripts do Instagram que usam GeckoDriver
- Conta logada no WhatsApp Web quando o script depender disso

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

### 3. Instalar dependências do módulo desejado

Este repositório não possui um `requirements.txt` global. Instale apenas o necessário para o módulo que vai executar.

## Instalação por Módulo

### Busca Automática Google

```bash
pip install selenium webdriver-manager requests
```

### Instagram Bot

```bash
pip install selenium webdriver-manager pysimplegui pandas openpyxl
```

### WhatsApp Bot

```bash
pip install selenium webdriver-manager pywhatkit keyboard pandas openpyxl
```

### WppMessage

```bash
pip install pywhatkit pandas openpyxl xlrd pyqt5 keyboard
```

### Base64

Não exige dependências externas.

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

### Decodificador Base64

```bash
python3 decifra_base64.py
```

## Dependências

Como os scripts têm propósitos diferentes, as dependências são separadas por módulo.

| Dependência | Uso principal |
| ----------- | ------------- |
| `selenium` | Automação de navegador |
| `webdriver-manager` | Gerenciar ChromeDriver/GeckoDriver automaticamente |
| `requests` | Requisições HTTP simples |
| `pywhatkit` | Envio via WhatsApp Web |
| `keyboard` | Atalhos e automação de teclado |
| `pandas` | Leitura e manipulação de planilhas |
| `openpyxl` | Leitura de arquivos `.xlsx` |
| `xlrd` | Leitura de planilhas legadas |
| `pyqt5` | Interface desktop do WppMessage |
| `pysimplegui` | Interface simples em alguns bots |

## Observações Importantes

- Scripts com Selenium dependem da estrutura atual da página. Mudanças no Google, Instagram ou WhatsApp Web podem exigir atualização de XPath, CSS selector ou fluxo.
- Evite deixar credenciais fixas nos scripts. Prefira variáveis de ambiente ou entrada manual.
- Em automações de mensagem, revise contatos e textos antes de executar.
- Durante envio automatizado no WhatsApp, evite usar mouse e teclado para reduzir falhas.
- Alguns scripts usam delays fixos com `time.sleep`; conexões lentas podem exigir aumento desses tempos.
- No macOS, automações com `keyboard` podem exigir permissões de acessibilidade.

## Manutenção

Sugestões para evoluir o repositório:

- Criar `requirements.txt` por pasta.
- Atualizar scripts antigos para Selenium 4 quando necessário.
- Substituir seletores frágeis por seletores mais estáveis.
- Remover credenciais hardcoded, se existirem, e usar `.env`.
- Criar exemplos de configuração por projeto.
- Padronizar nomes de arquivos e comandos de execução.

## Autor

Flávio Oliveira

- GitHub: [flaviooliveira-code](https://github.com/flaviooliveira-code)
