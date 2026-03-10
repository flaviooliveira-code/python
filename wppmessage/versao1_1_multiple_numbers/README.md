<h3 align="center">WppMessage - Versao 1.1 (Multiple Numbers)</h3>

## Sobre

Versao do WppMessage para agendar e enviar mensagens para multiplos numeros a partir de planilha Excel.

## Scripts

| Arquivo | Objetivo |
| --- | --- |
| `wppmessage.py` | Interface e fluxo de envio multiplo. |
| `wppmessage_rc.py` | Recursos visuais gerados pelo Qt. |
| `formatacao-planilha-de-numeros.xlsx` | Modelo de planilha para importacao dos numeros. |

## Pre-requisitos

- Python 3.9+
- Google Chrome instalado
- Sessao ativa no WhatsApp Web

## Instalacao

```bash
pip install pywhatkit pandas openpyxl xlrd pyqt5 keyboard
```

## Execucao

1. Entre na pasta da versao:
```bash
cd wppmessage/versao1_1_multiple_numbers
```
2. Execute a aplicacao:
```bash
python3 wppmessage.py
```

## Observacoes

- Use a planilha no formato esperado (`.xlsx`) com a coluna de numeros correta.
- Durante o envio multiplo, evite interagir com mouse/teclado.
- Dependendo do sistema operacional, ajuste o atalho de fechamento de aba (`Ctrl+W` ou `Command+W`).
