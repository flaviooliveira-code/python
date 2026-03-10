
<h3 align="center">Bots para WhatsApp</h3>

## Sobre

Scripts para envio automatizado de mensagens no WhatsApp Web.

## Scripts

| Arquivo | Objetivo |
| --- | --- |
| `whatsappbot.py` | Envio por nome de contato/grupo usando Selenium. |
| `whatsappbot-listadecontatos.py` | Envio para lista fixa de numeros com PyWhatKit. |
| `whasappbot-listadecontato-EXCEL.py` | Envio para numeros lidos de planilha Excel. |

## Pre-requisitos

- Python 3.9+
- Google Chrome instalado
- Sessao ativa no WhatsApp Web

## Instalacao

```bash
pip install selenium webdriver-manager pywhatkit keyboard pandas openpyxl
```

## Execucao

1. Entre na pasta: `cd whatsappbot`
2. Ajuste os contatos/mensagem no script desejado.
3. Execute o script, por exemplo:

```bash
python3 whatsappbot.py
```

## Observacoes

- Para `whatsappbot.py`, o Selenium 4 usa `webdriver-manager` para baixar e gerenciar o `chromedriver` automaticamente.
- Durante o envio automatizado, evite interagir com mouse/teclado para reduzir falhas.
