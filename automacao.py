# Passo 1 - Entrar no site da empresa
#     Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Pegar/Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.2

# Abrir o Chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrar no site
time.sleep(0.5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')   

# Logar no site
time.sleep(0.5)
pyautogui.press('tab')
pyautogui.write('igor@gmail.com')
pyautogui.press('tab')
pyautogui.write('1346798250')
pyautogui.press('enter')     

# Importar a Base de Dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

pyautogui.press('tab')

# Cadastrar os produtos
for linha in tabela.index:
    # codigo
    codigo = str(tabela.loc[linha,'codigo']) #Pega o código da tabela e escreve no campo
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # marca
    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    # tipo
    tipo = str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # categoria
    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')


    # preco_unitario
    preco_unitario = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    # custo
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    # obs
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha,'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('pgup')
    pyautogui.click(x=1191, y=263)







