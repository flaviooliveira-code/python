<h3 align="center">WppMessage</h3>

## Sobre

Aplicacao desktop em Python para agendamento e envio de mensagens no WhatsApp, com interface grafica.

## Scripts

| Caminho | Objetivo |
| --- | --- |
| `versao1_0_single_number/wppmessage.py` | Envio agendado para um unico numero. |
| `versao1_1_multiple_numbers/wppmessage.py` | Envio agendado para multiplos numeros via planilha Excel. |

## Pre-requisitos

- Python 3.9+
- Google Chrome instalado
- Sessao ativa no WhatsApp Web

## Instalacao

```bash
pip install pywhatkit pandas openpyxl xlrd pyqt5 keyboard
```

## Execucao

1. Entre na pasta da versao desejada:
```bash
cd wppmessage/versao1_1_multiple_numbers
```
2. Execute o script principal:
```bash
python3 wppmessage.py
```

## Observacoes

- Em `versao1_1_multiple_numbers`, ajuste o caminho da planilha e o nome da coluna de numeros na interface.
- O envio abre abas do WhatsApp Web; evite interagir com mouse/teclado durante a automacao.
- Dependendo do sistema operacional, pode ser necessario ajustar atalho de fechamento de aba (`Ctrl+W` ou `Command+W`).
