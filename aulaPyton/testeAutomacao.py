import pyautogui as py
import time as ti
import pyperclip as pyp

py.alert('vai começar')

py.PAUSE = 1
#py.press('winleft')
#py.write('chrome')
#py.press('enter')

py.hotkey('alt','tab')
ti.sleep(1)
py.hotkey('ctrlleft','t')

#link da planilha https://docs.google.com/spreadsheets/d/1E18PPkWY7NBOGddmFY1mCOvcHidac-wG/edit?usp=sharing&ouid=109527398916871578494&rtpof=true&sd=true
link = 'https://drive.google.com/drive/folders/1SZg-iMX06berZWI6t69AZdkSelaSHKLi'

py.write(link)
py.press('enter')
ti.sleep(10)
print(py.position())
py.click(x=329,y=258,clicks=2)
ti.sleep(2)
print(py.position())
py.click(x=337, y=400,button="right")
ti.sleep(3)
print(py.position())
py.click(x=441, y=850)

#print(py.KEYBOARD_KEYS)

