from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = Options()
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['Contato']
mensagem = 'mensagem'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    time.sleep(5)

for contato in contatos:
    buscar_contato(contato)
    for a in range(150):
        enviar_mensagem(mensagem)