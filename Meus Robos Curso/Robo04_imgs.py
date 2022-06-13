import rpa as r
import pyautogui as p
import pandas as pd

tempo=0.3
tempo2=2

r.init()
p.press('esc')
p.sleep(tempo)
p.getActiveWindow().maximize()
r.url('https://www.udemy.com')
p.sleep(tempo2*2)
# SEGUNDO VALOR É PRECISAO 0.8
localpesq= p.locateOnScreen('busca_udemy.PNG', confidence=0.8)
coord = p.center(localpesq)
coordx , coordy = coord
p.moveTo(coordx,coordy)
p.click(coordx,coordy)
p.sleep(tempo)
p.write('charles lima')
p.press('enter')
p.sleep(tempo2)
p.screenshot('cursos.png')
p.sleep(tempo2)
r.close()