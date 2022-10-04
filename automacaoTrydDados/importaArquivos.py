import pyautogui as py
import time as ti


def importaArquivoBaseDados():
    py.press('winleft')
    py.write('chrome')
    ti.sleep(2)
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

importaArquivoBaseDados()