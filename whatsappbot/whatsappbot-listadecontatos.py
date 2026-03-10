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
from datetime import datetime, timedelta
from sys import platform

#definir para quais contatos ou de uma lista de excel
contatos = ["+5519999999999", "+5519999999999", "+5519999999999", "+5519999999999"]

#definindo intervalo de envio
while len(contatos) >= 1:
    horario_envio = datetime.now() + timedelta(minutes=1)
    #envia mensagem
    pywhatkit.sendwhatmsg(contatos[0], 'Olá, eu sou uma mensagem automática', horario_envio.hour, horario_envio.minute)
    del contatos[0]
    if platform == 'darwin':
        keyboard.press_and_release('command + w')
    else:
        keyboard.press_and_release('ctrl + w')
