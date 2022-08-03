import pyautogui as py
import time as ti


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

importaArquivoBaseDados()