import rpa as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request
import time as t
import pyautogui as p


RodarNoBackground = False
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
if RodarNoBackground:
    op.add_argument("--headless")
s = Service(r'C:\Users\andre\Downloads\Rpa python\chromedriver_win32\chromedriver.exe') 
navegador = webdriver.Chrome(service=s,options=op)
# navegador = webdriver.Chrome(r'C:\Users\andre\Downloads\Rpa python\chromedriver_win32\chromedriver.exe',chrome_options=options)

def pag_inicial():
    try:
        link='https://www.lages.sc.gov.br/'
        navegador.get(link) 
        navegador.maximize_window()
        p.sleep(1)
        sair= p.locateOnScreen(r'Exercicio_prefeitura\assets\sair.PNG', confidence=0.8)
        coord = p.center(sair)
        coordx , coordy = coord
        p.moveTo(coordx,coordy)
        p.click(coordx,coordy)
        p.moveTo(0,0)
        p.sleep(1)
        xpath='/html/body/table[2]/tbody/tr/td/div[1]/table/tbody/tr/td/table[3]/tbody/tr/td/a/span/span'
        navegador.find_element(By.XPATH, xpath).click()
        p.sleep(2)
    except:
        print('Ruim na Pag inicial')

def pagina2():
    try:
        # '//*[@onclick="contador_acesso(19)"]'
        #/html/body/table[5]/tbody/tr/td/div[1]/div[34]/a
        # xpath='/html/body/table[5]/tbody/tr/td/div[1]/div[34]/a'
        xpath='/html/body/table[5]/tbody/tr/td/div[1]/div[34]/a/table/tbody/tr/td[2]/span[1]'
        elemento=navegador.find_element(By.XPATH, xpath)
        p.sleep(3)
        elemento.click()
        print(elemento)
        p.sleep(3)

    except  Exception as e:
        print('Ruim na Pagina 2')
        print(e)

# def pagina3():
#     try:
#         xpath= "//option[text()='Licitações']"
#         p.sleep(5)
#         navegador.find_element(By.XPATH,xpath).click()
#         p.sleep(5)
#     except:
#         print('Ruim na Pagina 3')

pag_inicial()
pagina2()
# pagina3()



navegador.quit()
