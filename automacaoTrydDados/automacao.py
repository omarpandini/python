from dataclasses import replace
import pyautogui as py
import time as ti

print('começando')

py.hotkey('alt','tab')

#============  PRIMEIRO ARQUIVO =================

py.click(x=360, y=280,button='right') # Clicar com o botão direito na tela

py.click(x=480, y=791) # Clicar em mais atalhos

py.click(x=772, y=784) # Clicar em Abrir dados do gráfico

py.click(x=1048, y=432) # Abrir menu da janela

py.click(x=1091, y=455) # Exportar arquivo

pathArquivo = 'C:\\www\python\\automacaoTrydDados\\teste.csv'

py.write(pathArquivo)

ti.sleep(1)

py.click(x=1621, y=919) # Salva o arquivo

ti.sleep(1)

py.click(x=1160, y=562) # Clica no ok

py.click(x=1079, y=434) # Fecha a janela de dados

#============  SEGUNDO ARQUIVO =================

pathArquivo2 = 'C:\\www\python\\automacaoTrydDados\\teste2.csv'

py.click(x=770, y=280,button='right') # Clicar com o botão direito na tela

py.click(x=890, y=791) # Clicar em mais atalhos

py.click(x=1182, y=784) # Clicar em Abrir dados do gráfico

py.click(x=1048, y=432) # Abrir menu da janela

py.click(x=1091, y=455) # Exportar arquivo

py.write(pathArquivo2)

ti.sleep(1)

py.click(x=1621, y=919) # Salva o arquivo

ti.sleep(1)

py.click(x=1160, y=562) # Clica no ok

py.click(x=1079, y=434) # Fecha a janela de dados

ti.sleep(4)
print(py.position())