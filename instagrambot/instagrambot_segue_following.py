"""
Esse bot clica no botao seguir dos perfis listados em seguidores ou seguindo de uma conta especifica.
Ele navega ate o perfil alvo, abre a lista configurada e clica no botao seguir dentro do modal.
"""


import argparse
import getpass
import importlib
import importlib.util
import platform
import re
import subprocess
import sys
import time


PACOTES_AUTOMACAO = [
    {"modulo": "selenium", "pacote": "selenium"},
    {"modulo": "webdriver_manager", "pacote": "webdriver-manager"},
]

MODO_EXECUCAO = "codigo" # opcoes: "codigo" ou "terminal"

#PREENCHA COM OS DADOS DA CONTA PARA LOGAR
DADOS_BOT_CODIGO = {
    "usuario": "",
    "senha": "",
    "usa_codigo_verificacao": False,
    "codigo_verificacao": "", # codigo de verificacao em 2 fatores, se a conta tiver habilitado
    "perfil_alvo": "", # perfil do Instagram onde vai seguir os perfis seguidos
    "tipo_lista": "seguidores", # opcoes: "seguidores" ou "seguindo"
    "limite_seguir": 50, # quantidade maxima de perfis para seguir por lote
    "intervalo_lote_segundos": 3600, # 1h de intervalo entre lotes de seguimento
}


def obter_pacotes_ausentes(pacotes_obrigatorios):
    pacotes_ausentes = []

    for dependencia in pacotes_obrigatorios:
        if importlib.util.find_spec(dependencia["modulo"]) is None:
            pacotes_ausentes.append(dependencia)

    return pacotes_ausentes


def obter_comando_pip():
    if platform.system().lower().startswith("win"):
        return "pip"

    return "pip3"


def tentar_instalar_pacotes(pacotes_ausentes, pacotes_obrigatorios):
    nomes_pacotes = [dependencia["pacote"] for dependencia in pacotes_ausentes]
    comandos_instalacao = [
        [obter_comando_pip(), "install", *nomes_pacotes],
        [sys.executable, "-m", "pip", "install", *nomes_pacotes],
    ]

    for comando in comandos_instalacao:
        print("Tentando instalar pacotes: " + " ".join(comando))

        try:
            resultado = subprocess.run(comando, check=False)
        except FileNotFoundError:
            print("Comando nao encontrado: " + comando[0])
            continue

        importlib.invalidate_caches()

        if resultado.returncode == 0 and not obter_pacotes_ausentes(pacotes_obrigatorios):
            return True

    return False


def mostrar_instrucoes_instalacao(pacotes_ausentes):
    nomes_pacotes = " ".join(dependencia["pacote"] for dependencia in pacotes_ausentes)

    print("\nNao foi possivel instalar todos os pacotes automaticamente.")
    print("Ative seu ambiente virtual e execute um destes comandos:")
    print(f"{obter_comando_pip()} install {nomes_pacotes}")
    print(f"{sys.executable} -m pip install {nomes_pacotes}")
    print("\nSe o pip nao estiver instalado, instale/atualize o pip antes de rodar o bot.")


def verificar_pacotes_instalados():
    pacotes_obrigatorios = PACOTES_AUTOMACAO.copy()
    pacotes_ausentes = obter_pacotes_ausentes(pacotes_obrigatorios)

    if not pacotes_ausentes:
        return True

    print("Pacotes ausentes:")
    for dependencia in pacotes_ausentes:
        print("- " + dependencia["pacote"])

    if tentar_instalar_pacotes(pacotes_ausentes, pacotes_obrigatorios):
        return True

    mostrar_instrucoes_instalacao(obter_pacotes_ausentes(pacotes_obrigatorios))
    return False


def carregar_dependencias_externas():
    global webdriver
    global NoSuchElementException
    global WebDriverException
    global TimeoutException
    global Keys
    global By
    global ChromeService
    global ChromeDriverManager
    global Options
    global WebDriverWait
    global EC

    from selenium import webdriver as selenium_webdriver
    from selenium.common.exceptions import NoSuchElementException as SeleniumNoSuchElementException
    from selenium.common.exceptions import WebDriverException as SeleniumWebDriverException
    from selenium.common.exceptions import TimeoutException as SeleniumTimeoutException
    from selenium.webdriver.common.keys import Keys as SeleniumKeys
    from selenium.webdriver.common.by import By as SeleniumBy
    from selenium.webdriver.chrome.options import Options as SeleniumChromeOptions
    from selenium.webdriver.chrome.service import Service as SeleniumChromeService
    from selenium.webdriver.support import expected_conditions as SeleniumEC
    from selenium.webdriver.support.wait import WebDriverWait as SeleniumWebDriverWait
    from webdriver_manager.chrome import ChromeDriverManager as SeleniumChromeDriverManager

    webdriver = selenium_webdriver
    NoSuchElementException = SeleniumNoSuchElementException
    WebDriverException = SeleniumWebDriverException
    TimeoutException = SeleniumTimeoutException
    Keys = SeleniumKeys
    By = SeleniumBy
    ChromeService = SeleniumChromeService
    ChromeDriverManager = SeleniumChromeDriverManager
    Options = SeleniumChromeOptions
    WebDriverWait = SeleniumWebDriverWait
    EC = SeleniumEC


XPATHS = {
    "campo_usuario": [
        "//input[@name='email']",
        "//input[@name='username']",
        "//input[contains(@autocomplete, 'username')]",
    ],
    "campo_senha": [
        "//input[@name='pass']",
        "//input[@name='password']",
        "//input[@type='password']",
    ],
    "botao_entrar": [
        "//*[@role='button' and @aria-label='Entrar']",
        "//button[@type='submit']",
        "//*[@role='button' and .//span[normalize-space()='Entrar']]",
    ],
    "campo_verificacao_codigo": [
        "//input[@name='verificationCode']",
        "//input[contains(@autocomplete, 'one-time-code')]",
    ],
    "tela_verificacao_manual": [
        "//*[contains(normalize-space(.), 'Verifique seu email')]",
        "//*[contains(normalize-space(.), 'Insira o código que enviamos')]",
        "//*[contains(normalize-space(.), 'Insira o codigo que enviamos')]",
        "//input[@name='email' and @autocomplete='off']",
    ],
    "link_seguidores": [
        "//header//a[contains(@href, '/followers')]",
        "//a[contains(@href, '/followers')]",
        "//a[contains(@href, 'followers')]",
        "//a[.//*[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'followers')]]",
        "//a[.//*[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'seguidores')]]",
    ],
    "link_seguindo": [
        "//header//a[contains(@href, '/following')]",
        "//a[contains(@href, '/following')]",
        "//a[contains(@href, 'following')]",
        "//a[.//*[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'following')]]",
        "//a[.//*[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'seguindo')]]",
    ],
    "modal_lista_perfis": [
        "//div[@role='dialog' and .//*[normalize-space()='Seguidores']]",
        "//div[@role='dialog' and .//*[normalize-space()='Seguindo']]",
        "//div[@role='dialog']",
    ],
    "botao_seguir_modal": [
        ".//button[.//div[normalize-space()='Seguir']]",
        ".//*[@role='button' and .//*[normalize-space()='Seguir']]",
        ".//button[normalize-space()='Seguir']",
    ],
}


def encontrar_elemento(driver, nome_elemento):
    for xpath in XPATHS[nome_elemento]:
        try:
            return driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            continue

    raise NoSuchElementException("Nao foi possivel encontrar o elemento: " + nome_elemento)


def elemento_existe(driver, nome_elemento):
    for xpath in XPATHS[nome_elemento]:
        if driver.find_elements(By.XPATH, xpath):
            return True

    return False


def esperar_elemento(driver, nome_elemento, timeout=20, clicavel=False):
    ultimo_erro = None

    for xpath in XPATHS[nome_elemento]:
        try:
            condicao = EC.element_to_be_clickable((By.XPATH, xpath)) if clicavel else EC.presence_of_element_located((By.XPATH, xpath))
            return WebDriverWait(driver, timeout).until(condicao)
        except TimeoutException as erro:
            ultimo_erro = erro

    raise NoSuchElementException("Nao foi possivel encontrar o elemento: " + nome_elemento) from ultimo_erro


def encontrar_elemento_dentro(elemento_base, nome_elemento):
    for xpath in XPATHS[nome_elemento]:
        elementos = elemento_base.find_elements(By.XPATH, xpath)
        if elementos:
            return elementos[0]

    raise NoSuchElementException("Nao foi possivel encontrar o elemento: " + nome_elemento)


def encontrar_elementos_dentro(elemento_base, nome_elemento):
    elementos_encontrados = []
    ids_encontrados = set()

    for xpath in XPATHS[nome_elemento]:
        for elemento in elemento_base.find_elements(By.XPATH, xpath):
            if elemento.id in ids_encontrados:
                continue

            ids_encontrados.add(elemento.id)
            elementos_encontrados.append(elemento)

    return elementos_encontrados


def esperar_elemento_dentro(elemento_base, nome_elemento, timeout=20):
    fim = time.time() + timeout

    while time.time() < fim:
        try:
            return encontrar_elemento_dentro(elemento_base, nome_elemento)
        except NoSuchElementException:
            time.sleep(0.5)

    raise NoSuchElementException("Nao foi possivel encontrar o elemento dentro do modal: " + nome_elemento)


def salvar_diagnostico(driver, contexto):
    caminho_screenshot = f"/tmp/instagrambot_{contexto}.png"

    print("\nDiagnostico da pagina:")
    print("URL atual: " + driver.current_url)
    print("Titulo: " + driver.title)

    try:
        driver.save_screenshot(caminho_screenshot)
        print("Screenshot salvo em: " + caminho_screenshot)
    except WebDriverException:
        print("Nao foi possivel salvar screenshot de diagnostico.")


def extrair_total_perfis_lista(texto_total):
    texto_normalizado = texto_total.lower().replace("seguindo", "").replace("following", "").strip()
    match = re.search(r"[\d.,]+", texto_normalizado)

    if not match:
        raise ValueError("Nao foi possivel identificar o total de perfis no texto: " + texto_total)

    return int(match.group(0).replace(".", "").replace(",", ""))


def esta_logado(driver):
    return driver.get_cookie("sessionid") is not None


def esta_em_tela_login(driver):
    url_atual = driver.current_url.lower()

    if "/accounts/login" in url_atual:
        return True

    return elemento_existe(driver, "campo_usuario") and elemento_existe(driver, "campo_senha")


def esta_em_verificacao_manual(driver):
    url_atual = driver.current_url.lower()
    return (
        elemento_existe(driver, "tela_verificacao_manual") or
        "/auth_platform/" in url_atual
    )


def esta_em_fluxo_de_verificacao(driver):
    url_atual = driver.current_url.lower()
    return (
        "/challenge/" in url_atual or
        "/checkpoint/" in url_atual or
        "/two_factor" in url_atual or
        "/accounts/login/two_factor" in url_atual
    )


def esperar_login_concluido(driver, timeout=90):
    tempo_esperar_cookie = 12

    try:
        WebDriverWait(driver, timeout).until(
            lambda navegador: (
                esta_logado(navegador) or
                esta_em_verificacao_manual(navegador) or
                esta_em_fluxo_de_verificacao(navegador) or
                not esta_em_tela_login(navegador)
            )
        )
    except TimeoutException as erro:
        salvar_diagnostico(driver, "login_nao_concluido")
        raise TimeoutException("Login nao concluiu dentro do tempo esperado. Verifique usuario, senha ou bloqueios do Instagram.") from erro

    if esta_logado(driver):
        print("Login concluido.")
        return

    if esta_em_verificacao_manual(driver):
        print("\nO Instagram pediu verificacao manual por codigo.")
        print("Digite o codigo no navegador e clique em Continuar.")
        print("O bot vai aguardar o login concluir antes de continuar.")

        try:
            WebDriverWait(driver, 300).until(lambda navegador: esta_logado(navegador))
        except TimeoutException as erro:
            salvar_diagnostico(driver, "verificacao_manual_nao_concluida")
            raise TimeoutException("A verificacao manual nao foi concluida em ate 5 minutos.") from erro

        print("Login concluido apos verificacao manual.")
        return

    if not esta_em_tela_login(driver):
        print("Tela de login encerrada. Confirmando autenticacao...")
        deadline = time.time() + tempo_esperar_cookie

        while time.time() < deadline:
            if esta_logado(driver):
                print("Login concluido.")
                return
            time.sleep(1)

        print("Login parece ter saindo da tela de login sem o cookie de sessao detectavel.")
        return

    salvar_diagnostico(driver, "login_exige_verificacao")
    raise RuntimeError("O Instagram abriu uma etapa de verificacao/checkpoint. Conclua essa etapa ou habilite o codigo 2FA no script antes de continuar.")


def criar_opcoes_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chrome_options


def criar_driver_chrome():
    chrome_options = criar_opcoes_chrome()

    try:
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)
    except WebDriverException as erro_webdriver_manager:
        print("Falha ao iniciar Chrome com chromedriver do webdriver-manager.")
        print("Tentando fallback com Selenium Manager...")

        try:
            return webdriver.Chrome(options=chrome_options)
        except WebDriverException as erro_selenium_manager:
            print("\nNao foi possivel iniciar o Chrome automaticamente.")
            print("Tente remover o cache do chromedriver e rodar novamente:")
            print("rm -rf ~/.wdm/drivers/chromedriver")
            print("\nErro webdriver-manager:")
            print(erro_webdriver_manager)
            print("\nErro Selenium Manager:")
            print(erro_selenium_manager)
            raise


class InstagramBot:
    def __init__(
        self,
        usuario,
        senha,
        usa_codigo_verificacao,
        codigo_verificacao,
        perfil_alvo,
        tipo_lista,
        limite_seguir,
        intervalo_lote_segundos,
    ):
        self.usuario = usuario
        self.senha = senha
        self.usa_codigo_verificacao = usa_codigo_verificacao
        self.codigo_verificacao = codigo_verificacao
        self.lista_seguidores = []
        self.perfil = perfil_alvo.strip().lstrip('@') # perfil do Instagram onde vai seguir os perfis seguidos
        self.tipo_lista = tipo_lista
        self.limite_seguir = limite_seguir
        self.intervalo_lote_segundos = intervalo_lote_segundos
        self.driver = criar_driver_chrome()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        #input[@name=email] = login inspecionado na pagina instagram
        #input[@name=pass] = senha inspecionado na pagina instagram
        #input[@name=verificationCode] = verificaçao de codigo em autenticaçao de dois fatores
        campo_usuario = esperar_elemento(driver, "campo_usuario", timeout=30)
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.usuario)
        campo_senha = esperar_elemento(driver, "campo_senha", timeout=20)
        campo_senha.clear()
        campo_senha.send_keys(self.senha)
        botao_entrar = esperar_elemento(driver, "botao_entrar", timeout=20, clicavel=True)
        botao_entrar.click()

        if self.usa_codigo_verificacao:
            campo_verificacao_codigo = esperar_elemento(driver, "campo_verificacao_codigo", timeout=30)
            campo_verificacao_codigo.click()
            campo_verificacao_codigo.clear()
            campo_verificacao_codigo.send_keys(self.codigo_verificacao)
            campo_verificacao_codigo.send_keys(Keys.RETURN)

        esperar_login_concluido(driver)
        self.seguir_perfis_da_lista(self.perfil)
  
    def seguir_perfis_da_lista(self, perfil_instagram):
        driver = self.driver
        driver.get("https://www.instagram.com/" + perfil_instagram + "/")
        nome_link_lista = "link_seguidores" if self.tipo_lista == "seguidores" else "link_seguindo"

        try:
            link_lista = esperar_elemento(driver, nome_link_lista, timeout=30, clicavel=True)
        except NoSuchElementException:
            salvar_diagnostico(driver, f"link_{self.tipo_lista}_nao_encontrado")
            raise

        total_perfis_lista = link_lista.text
        print(total_perfis_lista)
        total_perfis_lista = extrair_total_perfis_lista(total_perfis_lista)
        link_lista.click()

        self.seguir_perfis_no_modal(total_perfis_lista)

    def seguir_perfis_no_modal(self, total_perfis_lista):
        driver = self.driver
        modal = esperar_elemento(driver, "modal_lista_perfis", timeout=30)
        esperar_elemento_dentro(modal, "botao_seguir_modal", timeout=30)

        total_seguidos = 0
        total_lote = 0
        tentativas_sem_novos_botoes = 0

        print(f"Iniciando cliques em Seguir na lista de {self.tipo_lista}.")
        print(f"Limite por lote: {self.limite_seguir}. Intervalo entre lotes: {self.intervalo_lote_segundos} segundos.")

        while total_seguidos < total_perfis_lista and tentativas_sem_novos_botoes < 8:
            botoes_seguir = [
                botao for botao in encontrar_elementos_dentro(modal, "botao_seguir_modal")
                if botao.is_displayed() and botao.is_enabled()
            ]

            if not botoes_seguir:
                tentativas_sem_novos_botoes += 1
                self.rolar_modal_seguindo(modal)
                time.sleep(2)
                continue

            tentativas_sem_novos_botoes = 0

            for botao_seguir in botoes_seguir:
                if total_seguidos >= total_perfis_lista:
                    break

                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_seguir)
                    time.sleep(0.5)
                    botao_seguir.click()
                    total_seguidos += 1
                    total_lote += 1
                    print(f"Seguindo perfil {total_seguidos}/{total_perfis_lista} (lote {total_lote}/{self.limite_seguir})")
                    time.sleep(2)
                except WebDriverException:
                    continue

                if total_lote >= self.limite_seguir and total_seguidos < total_perfis_lista:
                    print(f"Limite do lote atingido. Aguardando {self.intervalo_lote_segundos} segundos para continuar de onde parou.")
                    time.sleep(self.intervalo_lote_segundos)
                    total_lote = 0
                    print("Retomando cliques no modal.")
                    self.rolar_modal_seguindo(modal)
                    time.sleep(2)
                    break

            self.rolar_modal_seguindo(modal)
            time.sleep(2)

        print(f"Finalizado. Total seguido nesta execucao: {total_seguidos}")

    def rolar_modal_seguindo(self, modal):
        self.driver.execute_script(
            """
            const modal = arguments[0];
            const scrollables = Array.from(modal.querySelectorAll('div')).filter((element) => {
                const style = window.getComputedStyle(element);
                return element.scrollHeight > element.clientHeight && ['auto', 'scroll'].includes(style.overflowY);
            });
            const target = scrollables[scrollables.length - 1] || modal;
            target.scrollTop = target.scrollHeight;
            """,
            modal,
        )

def campo_vazio(valor):
    return not str(valor).strip()


def validar_formulario(valores_formulario):
    campos_pendentes = []

    if campo_vazio(valores_formulario['usuario']):
        campos_pendentes.append('Usuario')

    if campo_vazio(valores_formulario['senha']):
        campos_pendentes.append('Senha')

    if campo_vazio(valores_formulario['perfil_alvo']):
        campos_pendentes.append('Perfil alvo')

    if valores_formulario['tipo_lista'] not in ("seguidores", "seguindo"):
        campos_pendentes.append('Tipo lista deve ser "seguidores" ou "seguindo"')

    if valores_formulario['usa_codigo_verificacao'] and campo_vazio(valores_formulario['codigo_verificacao']):
        campos_pendentes.append('Codigo 2FA')

    if int(valores_formulario['limite_seguir']) <= 0:
        campos_pendentes.append('Limite seguir maior que zero')

    if int(valores_formulario['intervalo_lote_segundos']) < 0:
        campos_pendentes.append('Intervalo do lote maior ou igual a zero')

    return campos_pendentes


def criar_parser_argumentos():
    parser = argparse.ArgumentParser(description='Bot para seguir perfis da lista de seguidores ou seguindo de uma conta do Instagram.')
    parser.add_argument('--terminal', action='store_true', help='Roda sem janela, solicitando dados pelo terminal.')
    parser.add_argument('--usuario', help='Usuario, email ou telefone da conta do Instagram.')
    parser.add_argument('--senha', help='Senha da conta do Instagram.')
    parser.add_argument('--perfil-alvo', dest='perfil_alvo', help='Perfil de onde o bot vai abrir a lista configurada.')
    parser.add_argument('--tipo-lista', dest='tipo_lista', choices=['seguidores', 'seguindo'], default='seguindo', help='Lista que sera aberta no perfil alvo.')
    parser.add_argument('--usa-codigo-verificacao', action='store_true', help='Indica que a conta usa codigo 2FA.')
    parser.add_argument('--codigo-verificacao', help='Codigo de verificacao em 2 fatores.')
    parser.add_argument('--limite-seguir', dest='limite_seguir', type=int, default=50, help='Quantidade maxima de perfis para seguir por lote.')
    parser.add_argument('--intervalo-lote-segundos', dest='intervalo_lote_segundos', type=int, default=3600, help='Pausa entre lotes de cliques em Seguir.')
    return parser


def obter_modo_execucao(argumentos):
    if argumentos.terminal:
        return "terminal"

    return MODO_EXECUCAO


def validar_modo_execucao(modo_execucao):
    modos_validos = ("codigo", "terminal")

    if modo_execucao not in modos_validos:
        print("MODO_EXECUCAO invalido: " + modo_execucao)
        print('Use "codigo" ou "terminal".')
        sys.exit(1)


def pedir_texto_terminal(rotulo, valor_atual=None, oculto=False):
    if valor_atual:
        return valor_atual.strip()

    while True:
        if oculto:
            valor = getpass.getpass(rotulo + ': ')
        else:
            valor = input(rotulo + ': ')

        valor = valor.strip()

        if valor:
            return valor

        print(rotulo + ' e obrigatorio.')


def pedir_confirmacao_terminal(rotulo):
    while True:
        resposta = input(rotulo + ' [s/N]: ').strip().lower()

        if resposta == '':
            return False

        if resposta in ('s', 'sim', 'y', 'yes'):
            return True

        if resposta in ('n', 'nao', 'não', 'no'):
            return False

        print('Responda com s ou n.')


def coletar_dados_terminal(argumentos):
    usuario = pedir_texto_terminal('Usuario', argumentos.usuario)
    senha = pedir_texto_terminal('Senha', argumentos.senha, oculto=argumentos.senha is None)
    perfil_alvo = pedir_texto_terminal('Perfil alvo', argumentos.perfil_alvo)

    usa_codigo_verificacao = argumentos.usa_codigo_verificacao

    if not usa_codigo_verificacao and argumentos.codigo_verificacao:
        usa_codigo_verificacao = True

    if not usa_codigo_verificacao:
        usa_codigo_verificacao = pedir_confirmacao_terminal('Conta tem verificacao em 2 fatores?')

    codigo_verificacao = ''

    if usa_codigo_verificacao:
        codigo_verificacao = pedir_texto_terminal('Codigo 2FA', argumentos.codigo_verificacao)

    return {
        'usuario': usuario,
        'senha': senha,
        'usa_codigo_verificacao': usa_codigo_verificacao,
        'codigo_verificacao': codigo_verificacao,
        'perfil_alvo': perfil_alvo,
        'tipo_lista': argumentos.tipo_lista,
        'limite_seguir': argumentos.limite_seguir,
        'intervalo_lote_segundos': argumentos.intervalo_lote_segundos,
    }


def coletar_dados_codigo():
    dados_bot = {
        'usuario': DADOS_BOT_CODIGO['usuario'].strip(),
        'senha': DADOS_BOT_CODIGO['senha'].strip(),
        'usa_codigo_verificacao': DADOS_BOT_CODIGO['usa_codigo_verificacao'],
        'codigo_verificacao': DADOS_BOT_CODIGO['codigo_verificacao'].strip(),
        'perfil_alvo': DADOS_BOT_CODIGO['perfil_alvo'].strip(),
        'tipo_lista': DADOS_BOT_CODIGO['tipo_lista'].strip().lower(),
        'limite_seguir': int(DADOS_BOT_CODIGO['limite_seguir']),
        'intervalo_lote_segundos': int(DADOS_BOT_CODIGO['intervalo_lote_segundos']),
    }
    campos_pendentes = validar_formulario(dados_bot)

    if campos_pendentes:
        print("Preencha os campos em DADOS_BOT_CODIGO antes de rodar:")
        for campo in campos_pendentes:
            print("- " + campo)
        sys.exit(1)

    return dados_bot


def iniciar_bot(dados_bot):
    bot_instagram = InstagramBot(
        dados_bot['usuario'],
        dados_bot['senha'],
        dados_bot['usa_codigo_verificacao'],
        dados_bot['codigo_verificacao'],
        dados_bot['perfil_alvo'],
        dados_bot['tipo_lista'],
        dados_bot['limite_seguir'],
        dados_bot['intervalo_lote_segundos'],
    )
    bot_instagram.login()


def executar_modo_terminal(argumentos):
    dados_bot = coletar_dados_terminal(argumentos)
    print('Iniciando automacao...')
    iniciar_bot(dados_bot)


def executar_modo_codigo():
    dados_bot = coletar_dados_codigo()
    print('Iniciando automacao com dados definidos no codigo...')
    iniciar_bot(dados_bot)


def main():
    argumentos = criar_parser_argumentos().parse_args()
    modo_execucao = obter_modo_execucao(argumentos)
    validar_modo_execucao(modo_execucao)

    if not verificar_pacotes_instalados():
        sys.exit(1)

    carregar_dependencias_externas()

    if modo_execucao == "codigo":
        executar_modo_codigo()
    else:
        executar_modo_terminal(argumentos)


if __name__ == '__main__':
    main()
