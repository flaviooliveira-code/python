"""
Flávio Oliveira - 2021
https://github.com/oliveiradeflavio
"""

"""
Antes de executar o código, seu whatsapp Web precisa estar conectado no celular
e logado no navegador Chrome, no meu teste usei o Chrome. Depois que estiver
executando a aplicação, não mexer no mouse.
"""

#importar as bibliotecas
import pywhatkit
import keyboard
import pandas as pd
from datetime import datetime, timedelta
from sys import platform

#importar contatos da planilha do excel, colocar o caminho onde se encontra o xlsx.
contatos = pd.read_excel(r"/Users/foliveira/Desenvolvimento Local/Python/celular.xlsx")

#definindo mensagem 
mensagem = "VAMO AUTOMATIZAR TUDO! Acesse o site https://www.flaviodeoliveira.com.br"

#definindo intervalo de envio. Lembrando que o nome da coluna do excel nesse exemplo é 
#celular. Se for outro nome, precisa ser alterado.
for i in contatos["celular"]:
    horario_envio = datetime.now() + timedelta(minutes=1)
    pywhatkit.sendwhatmsg("+55"+str(i), mensagem, horario_envio.hour, horario_envio.minute, 3)
    if platform == 'darwin':
        keyboard.press_and_release('command + w')
    else:
        keyboard.press_and_release('ctrl + w')
