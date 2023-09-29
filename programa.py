# passo 1: entrar no site
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)



# passo 2: se cadastrar

pyautogui.click(x=840, y=353)
pyautogui.write("bodao@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha148")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)






# passo 3: colocar as informações da tabela
# passo 4: repetir o processo 

tabela = pd.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=801, y=240)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
 

