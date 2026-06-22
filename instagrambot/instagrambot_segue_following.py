"""
Esse bot irá clicar no botão seguir dos seguindos da conta especifica. 
Irá navegar até o perfil da conta, clicar nos seguindos e nesse modal que abrir, irá clicar no botão seguir de cada username.
"""


#importação de lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from PySimpleGUI import PySimpleGUI as sg


class InstagramBot:
    def __init__(self, usuario, senha, usa_codigo_verificacao, codigo_verificacao, perfil_alvo):
        self.usuario = usuario
        self.senha = senha
        self.usa_codigo_verificacao = usa_codigo_verificacao
        self.codigo_verificacao = codigo_verificacao
        self.lista_seguidores = []
        self.perfil = perfil_alvo.strip().lstrip('@') # perfil do Instagram onde vai seguir os perfis seguidos
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        #input[@name=username] = login inspecionado na pagina instagram
        #input[@name=password] = senha inspecionado na pagina instagram
        #input[@name=verificationCode] = verificaçao de codigo em autenticaçao de dois fatores
        time.sleep(3)
        campo_usuario = driver.find_element(By.XPATH, "//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.usuario)
        campo_senha = driver.find_element(By.XPATH, "//input[@name='password']")
        campo_senha.clear()
        campo_senha.send_keys(self.senha)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(3)

        if self.usa_codigo_verificacao:
            campo_verificacao_codigo = driver.find_element(By.XPATH, "//input[@name='verificationCode']")
            campo_verificacao_codigo.click()
            campo_verificacao_codigo.clear()
            campo_verificacao_codigo.send_keys(self.codigo_verificacao)
            campo_verificacao_codigo.send_keys(Keys.RETURN)
            time.sleep(3)

        self.seguir_perfis_seguidos(self.perfil)
  
    def seguir_perfis_seguidos(self, perfil_instagram):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ perfil_instagram)
        time.sleep(3)
        #seguidores = driver.find_elements(By.XPATH, '//li[contains(@class,"Y8-fY")]')
        #seguidores[1].click()
        
        aba_seguindo = 'following' # para seguidores followers || para seguindo following
        driver.find_element(By.XPATH, '//a[contains(@href, "%s")]' % aba_seguindo).click()
        link_total_seguindo = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        total_perfis_seguidos = link_total_seguindo.text
        print(total_perfis_seguidos)
        total_perfis_seguidos = total_perfis_seguidos.replace("seguindo", "")
    

        for indice_perfil in range(1, int(total_perfis_seguidos)):
            time.sleep(3)
            indice_modal = indice_perfil + 3 # a cada usuário o scroll do modal vai abaixando
            item_perfil_seguido = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]/ul/div/li[%s]' % indice_modal) # captura o nome do seguidor
            driver.execute_script("arguments[0].scrollIntoView();", item_perfil_seguido)
            driver.switch_to.active_element
            botoes_seguir = driver.find_elements(By.XPATH, '//*[contains(text(), "Seguir")]')
            botoes_seguir[1].click() # clica no botão para seguir #### TESTEI ATÉ O VALOR 48, QUE SERIA 48 SEGUIDORES ####
            print(indice_perfil)
            time.sleep(1)
 
#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(30, 4))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(30, 4))],
    [sg.Checkbox('Conta tem verificacao em 2 fatores', key='usa_codigo_verificacao')],
    [sg.Text('Verificacao 2 Fatores'), sg.Input(key='codigo_verificacao', size=(30, 4))],
    [sg.Text('Perfil alvo'), sg.Input(key='perfil_alvo', size=(30, 4))],
    [sg.Button('Logar')]
]

#Janela
janela = sg.Window('BOT INSTAGRAM SEGUE SEGUIDORES', layout)

#ler os eventos
while True:
    evento, valores_formulario = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Logar':
        tem_campos_obrigatorios_vazios = (
            valores_formulario['usuario'] == '' or
            valores_formulario['senha'] == '' or
            valores_formulario['perfil_alvo'] == ''
        )
        tem_codigo_verificacao_vazio = (
            valores_formulario['usa_codigo_verificacao'] and
            valores_formulario['codigo_verificacao'] == ''
        )

        if tem_campos_obrigatorios_vazios or tem_codigo_verificacao_vazio:
            sg.Popup('Há campos vazios a serem preenchidos', title='Atenção')
        else:
            bot_instagram = InstagramBot(
                valores_formulario['usuario'],
                valores_formulario['senha'],
                valores_formulario['usa_codigo_verificacao'],
                valores_formulario['codigo_verificacao'],
                valores_formulario['perfil_alvo']
            )
            bot_instagram.login()
