#Importação de Bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Importação de Variavel
from secret import password
from ips import *

#Negação de Certificado
table = pd.DataFrame()
df2 = pd.DataFrame()

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)

_current = 0
for ip,_keyword in lista:
    if ip != _current:
        print(ip,_current)
        _current = ip
        ip_1 = (f"https://{ip}/tmui/login.jsp")
        ip_2 = (f"https://{ip}/tmui/Control/jspmap/tmui/locallb/virtual_server/stats.jsp")
        driver.get(ip_1)
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/form/input[1]").send_keys("USUARIO")
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/form/input[2]").send_keys(password)
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/form/button").click()

        time.sleep(5)
        #Acessar o Local Traffic/VirtualServer Statistics VS1
        driver.get(ip_2)
        time.sleep(6)

        #Procura os dados
        actions = ActionChains(driver)
        for _ in range(5):
            actions.send_keys(Keys.TAB) 
        actions.send_keys(_keyword)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        #Pega a tabela
        driver.switch_to.frame(driver.find_element(by=By.NAME, value="contentframe"))
        pagesource1 = driver.page_source
        driver.switch_to.default_content()
        BeautifulSoup1 = BeautifulSoup(pagesource1,'lxml')
        all_tables1 = BeautifulSoup1.find_all('table', attrs={'id': 'list_table'})
        tables1 = pd.read_html(str(all_tables1[0]))
        df1 = tables1[0]

        #Edição de Tabela
        del df1['Unnamed: 0_level_0']
        del df1['Unnamed: 1_level_0']
        del df1['Unnamed: 3_level_0']
        del df1['Unnamed: 4_level_0']
        del df1['Bits']
        del df1['Packets']
        del df1['Requests']
        del df1['CPU Utilization Avg.']
        df1['IP']=ip
        df1['Current']=df1['Connections']['Current']
        df1["Virtual Server"]=df1['Unnamed: 2_level_0']['Virtual Server']
        del df1['Connections']
        del df1['Unnamed: 2_level_0']

        #Concatenação
        frames = [df1, df2]
        df2 = pd.concat(frames)
    else:
        time.sleep(4)
        actions = ActionChains(driver)
        for _ in range(5):
            actions.send_keys(Keys.TAB) 
        actions.send_keys(_keyword)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        #Pega a tabela
        driver.switch_to.frame(driver.find_element(by=By.NAME, value="contentframe"))
        pagesource1 = driver.page_source
        driver.switch_to.default_content()
        BeautifulSoup1 = BeautifulSoup(pagesource1,'lxml')
        all_tables1 = BeautifulSoup1.find_all('table', attrs={'id': 'list_table'})
        tables1 = pd.read_html(str(all_tables1[0]))
        df1 = tables1[0]

        #Edição de Tabela
        del df1['Unnamed: 0_level_0']
        del df1['Unnamed: 1_level_0']
        del df1['Unnamed: 3_level_0']
        del df1['Unnamed: 4_level_0']
        del df1['Bits']
        del df1['Packets']
        del df1['Requests']
        del df1['CPU Utilization Avg.']
        df1['IP']=ip
        df1['Current']=df1['Connections']['Current']
        df1["Virtual Server"]=df1['Unnamed: 2_level_0']['Virtual Server']
        del df1['Connections']
        del df1['Unnamed: 2_level_0']
        
        #Concatenação
        frames = [df1, df2]
        df2 = pd.concat(frames)

#Criação do Arquivo Excel
df2 = df2.reset_index()
df3 = df2.reindex(index=df2.index[::-1])
del df3['index']
try:
    df3.to_excel(r"CurrentConnections.xlsx")
except:
    df3.to_excel(r"CurrentConnections(voce deixou aberto).xlsx")