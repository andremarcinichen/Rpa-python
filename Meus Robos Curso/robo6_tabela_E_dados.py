import rpa as r
import pyautogui as p
import pandas as pd
import os as o

# from robo02 import funcaoX

# https://rpachallengeocr.azurewebsites.net/
# Bibliotecas para manipular arquivos xls e xlsx:
# pip install openpyxl
# pip install xlrd

# modo back ground true
r.init(headless_mode = True)
p.sleep(0.3)
# p.press('esc')
p.getActiveWindow().maximize()
r.url('https://rpachallengeocr.azurewebsites.net/')

p.sleep(2)
xpath = '//*[@id="tableSandbox"]'

countpage=1

while countpage<4:
    r.table(xpath,'temp.csv')
    dados=pd.read_csv('temp.csv')
    if countpage==1:
        dados.to_csv(r'webtable.csv', mode='a',index=None,header=True)
    else:
        dados.to_csv(r'webtable.csv', mode='a',index=None,header=False)
    r.click('//*[@id="tableSandbox_next"]')
    countpage= countpage+1

o.remove('temp.csv')
r.close()
# excel=pd.read_csv(r'webtable.csv')
# excel.to_excel('teste.xlsx')

