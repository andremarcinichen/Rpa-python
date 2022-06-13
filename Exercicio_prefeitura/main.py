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
    except  Exception as e:
        print('Erro na Pagina inicial')
        print(e)

def pagina2():
    try:
        xpath='/html/body/table[5]/tbody/tr/td/div[1]/div[34]/a/table/tbody/tr/td[2]/span[1]'
        elemento=navegador.find_element(By.XPATH, xpath)
        navegador.execute_script("arguments[0].scrollIntoView();", elemento)
        navegador.execute_script("arguments[0].click();", elemento) 
        p.sleep(5)

    except  Exception as e:
        print('Erro na Pagina 2')
        print(e)

def pagina3():
    try:
        navegador.switch_to.window(navegador.window_handles[1])
        xpath= "/html/body/div[1]/section/div/div[1]/div/div/div[2]/div/div/a[1]"
        elemento=navegador.find_element(By.XPATH,xpath).click()
        navegador.execute_script("arguments[0].click();", elemento) 
        p.sleep(10)
    except Exception as e:
        print('Erro na Pagina 3')
        print(e)

def botaodownload():
    try:
        xpath= " /html/body/div[1]/section/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/a"
        elemento=navegador.find_element(By.XPATH,xpath).click()
        p.sleep(1)
    except Exception as e:
        print('Erro no download')
        print(e)



       

pag_inicial()
pagina2()
pagina3()
botaodownload()



navegador.quit()
