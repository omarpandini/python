import pyautogui as py
import time as ti

print('começando')
py.hotkey('alt','tab')

def abrirMenuJanela(pathArquivo):
    py.click(x=1546, y=430) # Abrir menu da janela
    ti.sleep(2)
    py.click(x=1606, y=458) # Exportar arquivo
    py.write(pathArquivo)
    ti.sleep(1)

def salvaArquivo():
    py.click(x=1990, y=924) # Salva o arquivo
    ti.sleep(2)
    py.click(x=1482, y=553) # Clica no ok
    py.click(x=1579, y=433) # Fecha a janela de dados


def primeiroArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_8R.csv'
    py.click(x=307, y=220,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=414, y=721) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=697, y=745) # Clicar em Abrir dados do gráfico
    ti.sleep(1)
    abrirMenuJanela(pathArquivo)
    salvaArquivo()
    

def segundoArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_10R.csv'
    py.click(x=900, y=220,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=992, y=726) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=1276, y=741) # Clicar em Abrir dados do gráfico    
    ti.sleep(1)
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def terceiroArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_12R.csv'
    py.click(x=1445, y=220,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=1571, y=723) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=1879, y=745) # Clicar em Abrir dados do gráfico 
    ti.sleep(1)   
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def quartoArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_14R.csv'
    py.click(x=1975, y=220,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=2089, y=723) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=1858, y=748) # Clicar em Abrir dados do gráfico 
    ti.sleep(1)  
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def quintoArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_16R.csv'
    py.click(x=339, y=662,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=444, y=859) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=769, y=646) # Clicar em Abrir dados do gráfico 
    ti.sleep(1)   
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def sextoArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_18R.csv'
    py.click(x=874, y=662,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=984, y=855) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=1303, y=651) # Clicar em Abrir dados do gráfico 
    ti.sleep(1)   
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def setimoArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_20R.csv'
    py.click(x=1389, y=662,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=1470, y=855) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=1809, y=651) # Clicar em Abrir dados do gráfico 
    ti.sleep(1)   
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def oitavoArquivo():
    pathArquivo = 'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_22R.csv'
    py.click(x=1907, y=662,button='right') # Clicar com o botão direito na tela
    ti.sleep(1)
    py.click(x=2001, y=855) # Clicar em mais atalhos
    ti.sleep(1)
    py.click(x=2326, y=651) # Clicar em Abrir dados do gráfico 
    ti.sleep(1)   
    abrirMenuJanela(pathArquivo)    
    salvaArquivo()

def importaArquivoBaseDados():
    py.press('winleft')
    py.write('chrome')
    ti.sleep(1)
    py.press('enter')
    ti.sleep(1)
    py.write('http://localhost/bolsaEstatistica/importaCsv.php')
    py.press('enter')
    py.hotkey('ctrl','t')
    py.write('http://localhost/bolsaEstatistica/agressaoEstatistica.php')
    py.press('enter')


#primeiroArquivo()
#segundoArquivo()
#terceiroArquivo()
quartoArquivo()
quintoArquivo()
sextoArquivo()
setimoArquivo()
oitavoArquivo()
importaArquivoBaseDados()


ti.sleep(3)
print(py.position())
