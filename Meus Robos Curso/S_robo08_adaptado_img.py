from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time as t

RodarnoBackground = True


options = webdriver.ChromeOptions()
if RodarnoBackground:
    options.add_argument("--headless")
navegador = webdriver.Chrome(r'C:\Users\andre\Downloads\Rpa python\chromedriver_win32\chromedriver.exe',chrome_options=options)

link='https://condado.acervodejogos.com.br/'

navegador.get(link) 
navegador.maximize_window()
t.sleep(2)
xpath='/html/body/div[2]/div[1]/div/h1/img'
#navegador.find_element_by_xpath()
#botao_avancar=navegador.find_element_by_id('fhweurfhuer').click()
# navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('condado luderia')
# navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.RETURN)
img=navegador.find_element_by_xpath(xpath)
src = img.get_attribute('src')
urllib.request.urlretrieve(src, "teste_foto.png")

navegador.quit()
