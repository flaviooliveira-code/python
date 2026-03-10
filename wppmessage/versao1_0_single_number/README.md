<h3 align="center">WppMessage - Versao 1.0 (Single Number)</h3>

## Sobre

Versao do WppMessage para agendar e enviar mensagem para um unico numero no WhatsApp.

## Scripts

| Arquivo | Objetivo |
| --- | --- |
| `wppmessage.py` | Interface e fluxo de envio para um numero. |
| `wppmessage_rc.py` | Recursos visuais gerados pelo Qt. |

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
cd wppmessage/versao1_0_single_number
```
2. Execute a aplicacao:
```bash
python3 wppmessage.py
```

## Observacoes

- Verifique horario e numero antes de enviar para evitar disparos indevidos.
- Durante a automacao, evite interagir com mouse/teclado.
