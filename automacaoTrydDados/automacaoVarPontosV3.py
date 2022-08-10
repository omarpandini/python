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

def salvaArquivo1(x,y,nomeArquivo):    
    py.rightClick(x,y)
    py.click(x=550, y=710)
    py.click(x=709, y=721)
    py.click(x=1547, y=431)
    py.click(x=1606, y=457)
    py.write(nomeArquivo)
    py.click(x=2144, y=1002) #salva
    py.click(x=1502, y=560) #clica ok


def salvaArquivo2(x,y,nomeArquivo):
    py.click(x,y)


#===============================  Inicia executação do Robo ===============================

abreTryd()


i=1
for arquivo in arquivos:
    print(arquivo + str(i)) 
    if(i == 1):
        salvaArquivo1(posicaoX1,posicaoY1,arquivo)
    else:
        posicaoX1 += 300
        salvaArquivo2(posicaoX1,posicaoY1,arquivo)


    i+=1

ti.sleep(3)
print(py.position())