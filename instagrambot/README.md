
<h3 align="center">Bots para Instagram</h3>

## Sobre

Colecao de scripts para automacao no Instagram com Python e Selenium.

## Scripts

| Arquivo | Objetivo |
| --- | --- |
| `instagrambot.py` | Comenta em posts a partir de hashtag. |
| `instagram_curtir_fotos.py` | Curte fotos de uma hashtag. |
| `instagrambot_baixa_seguidores.py` | Coleta seguidores e comenta em sorteio. |
| `instagrambot_segue_following.py` | Segue perfis da lista de seguindo de uma conta. |
| `instagrambot_seguidores_lista_excel_mais_que_1_comentario.py` | Comenta marcando usuarios de uma planilha. |

## Pre-requisitos

- Python 3.9+
- Firefox instalado

## Instalacao

```bash
pip install selenium webdriver-manager pysimplegui pandas openpyxl
```

## Execucao

1. Entre na pasta: `cd instagrambot`
2. Execute o script desejado, por exemplo:

```bash
python3 instagrambot.py
```

## Observacoes

- Os scripts usam Selenium 4 com `webdriver-manager` para baixar e gerenciar o `geckodriver` automaticamente.
- A interface e os seletores do Instagram mudam com frequencia; pode ser necessario ajustar XPaths/CSS ao longo do tempo.
