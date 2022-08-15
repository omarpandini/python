import pyautogui as py
import time as ti


path = 'C:\Program Files\PLSQL Developer 12\plsqldev.exe'
usuario = 'SIPPROD'
senha = 'sipmanager'
db = 'CHU'
sql1 = 'S:\\pwr\\cliente\\power\\fontes\\alterando\\Omar\\Uteis\\lista_envio_emails_fila.sql'
sql2 = 'S:\\pwr\\cliente\\power\\fontes\\alterando\\Omar\\Uteis\\locks.sql'


def abrirPlsql():
    py.press('win')
    ti.sleep(1)
    py.write(path)
    ti.sleep(1)
    py.press('enter')
    #ti.sleep(5)    

def fazerLogin():
    i = 1
    locationInput = ''
    while not locationInput: #Enquanto não achar o input não sairá do loop
        locationInput = py.locateOnScreen('automacaoTrabalho/username.png')
        print('não achou '+str(i))
        i+=1

    x = locationInput.left + 150
    y = locationInput.top + 5
    py.click(x,y)
    py.hotkey('ctrl','a')    
    py.write(usuario)
    py.press('tab')
    py.write(senha)
    py.press('tab')
    py.write(db)
    
    locationBtnOk = py.locateCenterOnScreen('automacaoTrabalho/btnOk.png')
    print('locationBtnOk = ' + str(locationBtnOk))
    x = locationBtnOk.x
    y = locationBtnOk.y
    py.click(x,y)


def fechaJanelasAbertas():
    for i in range(15):
        py.hotkey('ctrl','f4')


def abrirArquivos(sql,fecharJanela):
    locationBtnAbrir = ''
    i = 1

    while not locationBtnAbrir:
        locationBtnAbrir = py.locateCenterOnScreen('automacaoTrabalho/btnAbrir.png')
        print('não achou '+str(i))        
        i+=1

    if fecharJanela == 'S':
        fechaJanelasAbertas()

    x = locationBtnAbrir.x
    y = locationBtnAbrir.y
    py.click(x,y)  

    locationBtnSql = ''
    i = 1

    while not locationBtnSql:
        locationBtnSql = py.locateCenterOnScreen('automacaoTrabalho/btnSql.png')
        print('não achou '+str(i))        
        i+=1  
        
    x = locationBtnSql.x
    y = locationBtnSql.y
    py.click(x,y) 
    py.write(sql)
    py.press('tab')
    py.press('tab')
    py.press('enter')

#=====================================================================================================#

abrirPlsql()
fazerLogin()
abrirArquivos(sql1,'S')
abrirArquivos(sql2,'N')

#ti.sleep(4)
#print(py.position())
