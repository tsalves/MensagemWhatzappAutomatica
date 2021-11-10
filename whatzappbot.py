# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# navegar ate o whatzapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

# aguarda ate cel logar no whatsaapp
time.sleep(30)

# definir contatos e grupos e msg a ser enviada
contatos = ['Grupo', 'Numero do contato1', 'Numero do contato2']
# contatos = ['Anotação']
mensagem = 'Olá Boa tarde!! Segue abaixo link com as ultimas atualizações do BI CCOA\n *TELA 1 - Agendamento de Recebimento* \n https://bit.ly/3mInycY \n by *CCOA-Desenvolvimento* ;)'

midia = '\\\\192.168.100.9\\testerede\\cultodeensino.jpg'
# midia = '\\\\192.168.100.9\\testerede\\Pasta1.xlsx'
# midia = '\\\\192.168.100.9\\testerede\\Pasta2.csv'

# copyable-text selectable-text
# buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_msg[1].click()
    time.sleep(3)
    campo_msg[1].send_keys(mensagem)
    campo_msg[1].send_keys(Keys.ENTER)

def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element_by_xpath("//div[contains(@class, '_33pCO')]")
    send.click()

# enviar msg para os contatos/grupo
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    # enviar_midia(midia)
    time.sleep(1)
