import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 7 # tempo de esperar entre ações poderia ser substituido por time.sleep()

# Abrir navegador e entrar no site
pg.press("win")
pg.write("chrome")
pg.press("enter")
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")

# Colocar email e senha no site
pg.click(x=625, y=364) # Localização do login   


pg.write("email@gmail.com")
pg.press("tab")
pg.write("senhaUsuario")
pg.press("tab")
pg.press("enter")

# Abastecer váriavel com dados do arquivo csv

tabela_produtos = pd.read_csv("produtos.csv")

for linha in tabela_produtos.index: # Povoando os dados
    pg.click(x=539, y=255)
    pg.write(str(tabela_produtos.loc[linha, "codigo"]))
    pg.press("tab")

    pg.write(str(tabela_produtos.loc[linha, "marca"]))
    pg.press("tab")

    pg.write(str(tabela_produtos.loc[linha, "tipo"]))
    pg.press("tab")
    
    pg.write(str(tabela_produtos.loc[linha, "categoria"]))
    pg.press("tab")

    pg.write(str(tabela_produtos.loc[linha, "preco_unitario"]))
    pg.press("tab")

    pg.write(str(tabela_produtos.loc[linha, "custo"]))
    pg.press("tab")

    obs = tabela_produtos.loc[linha, "obs"]
    if not pd.isna(obs):
        pg.write(str(tabela_produtos.loc[linha, "obs"]))
    pg.press("tab")
        
    pg.press("enter")
    pg.scroll(50000)