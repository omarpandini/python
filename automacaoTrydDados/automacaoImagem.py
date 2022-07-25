from dataclasses import replace
import pyautogui as py
import time as ti

print('começando')

py.hotkey('alt','tab')

#============  PRIMEIRO ARQUIVO =================


#x=118, y=100
imagem = 'C:\\www\python\\automacaoTrydDados\\img1.png'
imagem2 = 'C:\\www\python\\automacaoTrydDados\\img2.png'

pos = py.locateOnScreen(imagem)

print(pos)

x,y = py.locateOnScreen(imagem2)

if pos:
    print('tem')
else:
    print('não tem')

#print(py.position())
print(x,y )
