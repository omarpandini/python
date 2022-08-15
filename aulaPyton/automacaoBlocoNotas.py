import pyautogui as py
import time as ti

nTabuada = int(input('Informe o número para tabuada: '))

nLoop = int(input('Multiplicar até quanto?: '))

py.press('win')
py.write('bloco de notas')
ti.sleep(1)
py.press('enter')
ti.sleep(1)
py.hotkey('win','up')
ti.sleep(1)
py.write('Tabuada de: '+ str(nTabuada) + '\n')

i=1


while i <= nLoop:
    resultado = i * nTabuada;
    texto = str(i).ljust(3,' ') + ' X ' + str(nTabuada) + ' = ' + str(resultado)
    py.write( texto+ '\n' )
    i+=1

py.write('\n')
py.write( ' Fim '.rjust(30,'#') + ''.ljust(30,'#')  )