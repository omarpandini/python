import pyautogui as py
import time as ti

posicaoX1 = 355
posicaoY1 = 200

arquivos = ['C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_24P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_12P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_15P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_20P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_14P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_16P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_18P.csv'
           ,'C:\\wamp64\\www\\bolsaEstatistica\\WINFUT_22P.csv'
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

ti.sleep(3)
print(py.position())