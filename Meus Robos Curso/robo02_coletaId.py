import rpa
import pyautogui


rpa.init(visual_automation = True, chrome_browser = True)
#olhando github nao tem mto suporte para outros navegadores =(
rpa.url('https://pt.wowhead.com/')
janela = pyautogui.getActiveWindow().maximize()
rpa.wait(2.0)
# link no xpath, algo_a_ser_digitado[tecla]
#rpa.type('/html/body/div[4]/div/div[3]/div[1]/form/input','FOOD[enter]') 
#outra forma //*[@name="q"]
rpa.type('//*[@name="q"]','FOOD[enter]') 
# OBS. id normalmente é unico entao imagino que seja mais garantido de fazer
rpa.wait(2.0)
#print
rpa.snap('page','imagemlegal.png')
rpa.wait(2.0)
rpa.close()