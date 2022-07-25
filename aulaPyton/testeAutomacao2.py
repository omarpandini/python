import pyautogui as py
import time as ti
import pyperclip as pyp

py.alert('vai começar')

#

# py.press('winleft')
# py.write('chrome')
# py.press('enter')

py.hotkey('alt', 'tab')
py.hotkey('ctrlleft', 't')

# link da planilha https://docs.google.com/spreadsheets/d/1E18PPkWY7NBOGddmFY1mCOvcHidac-wG/edit?usp=sharing&ouid=109527398916871578494&rtpof=true&sd=true
link = 'https://drive.google.com/drive/folders/1SZg-iMX06berZWI6t69AZdkSelaSHKLi'

py.write(link)
py.press('enter')

ti.sleep(3)

imagem  = 'imgAula.png'
imagem2 = 'imgPlan.png'
imagem3 = 'imgDownLoad.png'

print('irá localizar a imagem')

res = py.locateOnScreen(imagem)

print(res)
py.click(res,clicks=2)

ti.sleep(3)

res2 = py.locateOnScreen(imagem2)
py.click(res2,button="right")

res3 = py.locateOnScreen(imagem3)
py.click(res3)
