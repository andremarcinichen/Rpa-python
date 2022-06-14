from ast import If
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import pyautogui as p
import os
import zipfile
import pandas as pd

rodarNoBackground = False # antes tava funcionando por alguma razao foi bloqueado o uso

Caminho_meu_pc="C:/Users/andre/Downloads/Rpa python/"
Caminho_meu_pc_pref=r"C:\Users\andre\Downloads\Rpa python\Desafio-wind"

op = webdriver.ChromeOptions()
# config Diretorio download
prefs = {"download.default_directory" : Caminho_meu_pc_pref}
op.add_experimental_option("prefs",prefs)
op.add_experimental_option('excludeSwitches', ['enable-logging'])
# To evade the detection as a bot, pass the argument 
op.add_argument('--disable-blink-features=AutomationControlled') 
#Rodar Headless
if rodarNoBackground:
    op.add_argument("--headless")

#abrir navegador com as configrações
s = Service(Caminho_meu_pc+'chromedriver_win32/chromedriver.exe') 
navegador = webdriver.Chrome(service=s,options=op)

def RodarNoBackground(rodarNoBackground):
    if rodarNoBackground:
        navegador.quit()


def PaginaInicial():
    try:
        print('Pagina inicial')
        link='http://dados.tce.rs.gov.br/organization/tribunal-de-contas-do-estado-do-rio-grande-do-sul'
        navegador.get(link) 
        navegador.maximize_window()
        p.sleep(2)
        xpath='/html/body/div[2]/div/div[3]/div/article/div/ul/li[2]/div/h3/a'
        elemento=navegador.find_element(By.XPATH, xpath)
        navegador.execute_script("arguments[0].click();", elemento)
        p.sleep(2)
    except  Exception as e:
        print('Erro na Pagina inicial')
        print(e)

def Pagina2():
    try:
        print('Pagina 2')
        xpath='/html/body/div[2]/div/div[3]/div/article/div/section[1]/ul/li/div/button'
        elemento=navegador.find_element(By.XPATH, xpath)
        navegador.execute_script("arguments[0].click();", elemento) 
        p.sleep(2)
    except  Exception as e:
        print('Erro na Pagina 2')
        print(e)

def BotaoDownload():
    try:
        print('Download')
        xpath= "/html/body/div[2]/div/div[3]/div/article/div/section[1]/ul/li/div/ul/li[2]/a"
        elemento=navegador.find_element(By.XPATH,xpath)
        navegador.execute_script("arguments[0].click();", elemento) 
        p.sleep(80)
        navegador.quit()
    except Exception as e:
        print('Erro no download')
        print(e)

def RemoverZip():
    try:
        print('Dezipando e Removendo os arquivos')
        with zipfile.ZipFile(Caminho_meu_pc+r'Desafio-wind\2022.csv.zip', 'r') as zip_ref:
            zip_ref.extractall(Caminho_meu_pc+r'Desafio-wind')
        #apos extrair os arquivos remove os desnecessarios
        if os.path.exists(Caminho_meu_pc+r'Desafio-wind/comissao.csv'):
            os.remove(Caminho_meu_pc+r"Desafio-wind\comissao.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\documento_lic.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\documento_lic.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\dotacao_lic.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\dotacao_lic.csv")#
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\evento_lic.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\evento_lic.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\item_prop.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\item_prop.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\licitante.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\licitante.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\lote_prop.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\lote_prop.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\lote.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\lote.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\proposta.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\proposta.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\memcomissao.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\memcomissao.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\pessoas.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\pessoas.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\membrocons.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\membrocons.csv")
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind\2022.csv.zip"):
            os.remove(Caminho_meu_pc+r"Desafio-wind\2022.csv.zip")
        p.sleep(1)
    except Exception as e:
        print('Erro no deszipar')
        print(e)

def FiltrarLicitacoes():
    try:
        print('Filtrando')
        df = pd.read_csv(Caminho_meu_pc+r'Desafio-wind/licitacao.csv', dtype=str)
        #filtro para data maior que 1 de maio
        Filtrado= df.loc[df["DT_ABERTURA"]>'2022-05-01']
        Filtrado.to_csv(Caminho_meu_pc+r'Desafio-wind/temporario.csv', mode='a', index=None, header=True)
        #apos a filtragem ele substitui o arquivo de licitaçãoe remove o temporario
        os.replace(Caminho_meu_pc+r'Desafio-wind/temporario.csv', Caminho_meu_pc+r'Desafio-wind/Licitacao.csv')
        if os.path.exists(Caminho_meu_pc+r"Desafio-wind/temporario.csv"):
            os.remove(Caminho_meu_pc+r"Desafio-wind/temporario.csv")
    except Exception as e:
        print('Erro no Filtrar')
        print(e)

def CriarDiretoriosELink():
    try:
        print('Criando os diretorios')
        licitacao_csv = pd.read_csv(Caminho_meu_pc+'Desafio-wind\licitacao.csv' , dtype=str)
        df = pd.DataFrame(licitacao_csv, columns=["CD_ORGAO","CD_TIPO_MODALIDADE", "NR_LICITACAO", "ANO_LICITACAO","LINK_LICITACON_CIDADAO"])
        contador=0
        for row in df.itertuples():
            #cria as 30 pastas no formato solicitado
            caminho =  Caminho_meu_pc + 'Desafio-wind/licitacao/' + str(row[1]) + ' - ' + str(row[2]) + ' - ' + str(row[3]) + ' - ' + str(row[4])
            os.makedirs(caminho)
            #cria o link.txt e coloca o link
            arquivo = open(caminho+"/link.txt", "a")
            arquivo.write(row[5])
            arquivo.close()
            contador= contador+1
            if contador==30:
                break
    except Exception as e:
        print('Erro no Filtrar')
        print(e)

def itemLicitacao():
    try:
        print('Criando item.csv')
        #abre as tabelas e seleciona as colunas de comparação
        licitacao_csv = pd.read_csv(Caminho_meu_pc+'Desafio-wind\licitacao.csv', dtype=str)
        item_completo = pd.read_csv(Caminho_meu_pc+'Desafio-wind\item.csv', dtype=str)
        licitacoes = pd.DataFrame(licitacao_csv, columns=["CD_ORGAO", "NR_LICITACAO", "ANO_LICITACAO","CD_TIPO_MODALIDADE"])
        items = pd.DataFrame(item_completo, columns=["CD_ORGAO", "NR_LICITACAO", "ANO_LICITACAO","CD_TIPO_MODALIDADE"])
        contador=0
        for row_licitacao in licitacoes.itertuples():
            array=[]
            for row_items in items.itertuples():
                #Validando a comparação
                row1=row_licitacao[1]==row_items[1]
                row2=str(int(float(row_licitacao[2])))==row_items[2]
                row3=row_licitacao[3]==row_items[3]
                row4=row_licitacao[4]==row_items[4]
                row5= True
                condition=row1&row2&row3&row4&row5
                array.append(condition)
            #filtra a tabela se for com as linhas validas
            Lista_filtrada = item_completo.loc[array]
            caminho =  Caminho_meu_pc+'Desafio-wind/licitacao/' + str(row_licitacao[1]) + ' - ' + str(row_licitacao[4]) + ' - ' + str(row_licitacao[2]) + ' - ' + str(row_licitacao[3])
            #Gera lista de itens dentro das licitacoes
            Lista_filtrada.to_csv(caminho+'/itens-licitacao.csv', mode='a', index=None, header=True)
            contador= contador+1
            if contador==30:
                break
    except Exception as e:
        print('Erro no item licitacao')
        print(e)


#comandos para rodar por partes o programa
RodarNoBackground(rodarNoBackground)
PaginaInicial()
Pagina2()
BotaoDownload()
RemoverZip()
FiltrarLicitacoes()
CriarDiretoriosELink()
itemLicitacao()

