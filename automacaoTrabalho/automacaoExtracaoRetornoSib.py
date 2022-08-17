import pyautogui as py
import time as ti

textFind1 = '<conferencia>'
textFind2 = '</conferencia>'
nmArquivo = 'T:\\SIBXML\\retorno\\arquivo_3.CNS'

#================= ATENÇÃO =================
#================= DESATIVAR O NUMLOCK =================


#====== Funções ======
def pesquisa(textFind,ultLinha):
    py.hotkey('ctrl','f')                                  # Abre a janela de pesquisa
    py.click(x=180, y=214)                                 # Clica no input da janela
    py.press('home')                                       # Apaga o texto que estiver no input
    py.hotkey('ctrl','shiftright','shiftleft','end')       # Apaga o texto que estiver no input
    py.press('backspace')                                  # Apaga o texto que estiver no input
    py.write(textFind)                                     # Faz a pesquisa
    ti.sleep(1)                                            # Aguarda um segundo
    py.click(x=460, y=208)                                 # Clica em pesquisar
    py.click(x=485, y=177)                                 # Clica em fechar a janela do pesquisar
    
    if(ultLinha == 'N'):
      py.press('right')                                    # Seleciona o próximo texto após o texto da pesquisa
    else:
      py.press('left')                                     # Seleciona o próximo texto após o texto da pesquisa

    py.press('enter')                                      # Pressiona enter

def criarNovoArquivo():
    py.press('win')                                        #abre um novo bloco de notas
    ti.sleep(1)
    py.write('bloco de notas')                             #abre um novo bloco de notas
    ti.sleep(1)
    py.press('enter')                                      #abre um novo bloco de notas
    py.hotkey('win','up')                                  #Maximiza a tela
    py.hotkey('ctrl','v')                                  #cola a linha
    py.press('enter')                                      #pula a linha
    py.hotkey('alt','tab')                                 #volta para o arquivo anterior
    py.hotkey('ctrl','end')                                #vai para o final do arquivo
    py.hotkey('shift','home')                              #seleciona toda a linha
    py.hotkey('ctrl','c')                                  #copia a linha
    py.hotkey('alt','tab')                                 #volta para o arquivo anterior
    py.hotkey('ctrl','v')                                  #cola a linha

def salvarArquivo():
    py.hotkey('ctrl','s')                                  #Clica em salvar arquivo
    py.write(nmArquivo)                                    #Escreve o nome do arquivo
    ti.sleep(1)
    py.click(x=517, y=484)                                 #clica em salvar
    ti.sleep(1)
    py.hotkey('alt','tab')                                 #volta para o arquivo anterior
    py.hotkey('ctrl','s')                                  #Clica em salvar arquivo



#============  INÍCIO DO FLUXO =================

py.hotkey('alt','tab')                                 # Abre o notepad
py.hotkey('win','up')                                  # Maximiza a janela
py.hotkey('ctrl','home')                               # Posiciona o cursor na primeira linha

pesquisa(textFind1,'N')                                #Faz a pesquisa do texto no arquivo

py.hotkey('ctrl','end')                                # Vai para o final do arquivo
py.press('home')                                       # Vai para o início da linha

pesquisa(textFind2,'S')                                    #Faz a pesquisa do texto no arquivo

py.hotkey('ctrl','home')                               #Vai para o inicio do arquivo

py.hotkey('shift','end')                               #seleciona toda a linha

py.hotkey('ctrl','c')                                  #copia a linha

criarNovoArquivo()
salvarArquivo()

ti.sleep(3)
print(py.position())