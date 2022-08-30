from operator import le
import time # importa todo o módulo
import time as tm
from time import sleep # importa do módulo a função sleep
from time import sleep, time
'''
importa todas as funcionalidades do módulo
não recomendo, pois pode haver conflitos
entre módulos com mesmo nome de funções
'''
from time import * 
import os.path # importa o módulo os, importa módulo path

CURRENT_PATH_FILE = os.path.abspath(__file__) # Pega o caminho atual e arquivo
# print(CURRENT_PATH_FILE)
CURRENT_PATH_FILE_LIST = CURRENT_PATH_FILE.split("\\") # CURRENT_PATH_FILE_LIST.pop()
# Vai retornar uma lista com cada palavra da pasta. OBS: é necessário usar 2x o \,
# pois ele é um caracter especial usado para printar caracteres especiais
CURRENT_PATH_FILE_LIST_LENGTH = len(CURRENT_PATH_FILE_LIST)
# pega o tamanho da lista
CURRENT_PATH_FILE_LIST = CURRENT_PATH_FILE_LIST[0:CURRENT_PATH_FILE_LIST_LENGTH - 1]
# Vai pegar do inicio do array até a penutlima rota
CURRENT_PATH = '\\'.join(CURRENT_PATH_FILE_LIST)
'''
Vai juntar todos dados dos arrays com \ ( montar a rota )
mostrando que é possivel utilizar mesmo assim a módulo os
'''
print(CURRENT_PATH)
os.system(f"start notepad {CURRENT_PATH}\\notas.txt")


'''
Instalando pacotes
Package Install Python -> PIP
'''

# pip install requests

import requests

url = f'https://www.fruityvice.com/api/fruit/all' 

# print(requests.get(url).json())