﻿import pyautogui as py
import time as ti

posicaoX1 = 355
posicaoY1 = 200

arquivos = ['C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_24R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_26R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_28R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_14R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_16R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_18R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_20R.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_22R.csv'
           ]

def abreTryd():
    print('começando')
    py.hotkey('alt','tab')

def cliqueBotaoDireito(x,y):
    py.rightClick(x,y)

def exportaArquivo(nmArquivo,x,y):

    #Clica com o botão direito na tela
    cliqueBotaoDireito(x,y)   

    locationBtn = ''
    i = 1

    # Acha a posição do mais atalhos
    while not locationBtn:
        locationBtn = py.locateCenterOnScreen('automacaoTrydDados/imgMaisAtalhos.png')
        print('não achou '+str(i))        
        i+=1  

    py.click(locationBtn);

    locationBtn = ''
    i = 1
    # Acha a posição do abrir dados gráfico
    while not locationBtn:
        locationBtn = py.locateCenterOnScreen('automacaoTrydDados/imgAbrirDadosGrafico.png')
        print('não achou '+str(i))        
        i+=1  

    py.click(locationBtn);

    #Clica no botão do menu exportar
    ti.sleep(2)
    py.click(x=1545, y=429)


    #Clica no botão do exportar
    locationBtn = ''
    i = 1
    # Acha a posição do abrir dados gráfico
    while not locationBtn:
        locationBtn = py.locateCenterOnScreen('automacaoTrydDados/imgExportarCsv3.png')
        print('não achou '+str(i))        
        i+=1  

    py.click(locationBtn)

    #Passa o nome do arquivo
    ti.sleep(1)
    py.write(nmArquivo)

    #salva o arquivo
    locationBtn = ''
    i = 1
    while not locationBtn:
        locationBtn = py.locateCenterOnScreen('automacaoTrydDados/imgBtnSalvar2.png')
        print('não achou '+str(i))        
        i+=1  

    py.click(locationBtn)

    
    #clica em ok
    locationBtn = ''
    i = 1
    while not locationBtn:
        locationBtn = py.locateCenterOnScreen('automacaoTrydDados/imgBtnOk.png')
        print('não achou '+str(i))        
        i+=1  

    py.click(locationBtn)

    #Fecha a janela de dados
    py.sleep(2)
    py.click(x=1580, y=433)


def importaArquivoBaseDados():
    py.press('winleft')
    py.write('chrome')
    ti.sleep(1)
    py.press('enter')
    ti.sleep(1)
    py.write('http://localhost/bolsaEstatistica/importaCsvV2.php')
    py.press('enter')
    py.hotkey('ctrl','t')
    py.write('http://localhost/bolsaEstatistica/agressaoEstatistica.php')
    py.press('enter')
    py.press('enter')
    py.hotkey('ctrl','t')
    py.write('http://localhost/bolsaEstatistica/agressaoEstatisticaExcel.php')
    py.press('enter')
    py.hotkey('ctrl','t')
    py.write('http://localhost/bolsaEstatistica/agressaoEstatisticaV2.php')
    py.press('enter')

#===============================  Inicia executação do Robo ===============================

abreTryd()


i=1
for arquivo in arquivos:
    print(arquivo + str(i))    

    if i <= 4:
        exportaArquivo(arquivo,posicaoX1,posicaoY1)
        posicaoX1 += 550
    else :
        if i == 5 :
            posicaoX1 = 355
            posicaoY1 = 671

        exportaArquivo(arquivo,posicaoX1,posicaoY1)
        posicaoX1 += 550

    i+=1 

#importaArquivoBaseDados()

ti.sleep(3)
print(py.position())