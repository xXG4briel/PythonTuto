import os

assuntos = [
    'variavéis e tipo de dados',
    'saida/entrada de dados',
    'operadores aritméticos',
    'operadores condicionais',
    'bibliotecas',
    'condicionais',
    'condicionais aninhadas',
    'funções',
    'laços de repetição',
    'listas',
    'tuplas',
    'dicionários',
    'classes',
    'modulações'
]

for index, assunto in enumerate(assuntos):
    nomePasta = f'{index} - {assunto}'
    command = f'mkdir "{nomePasta}" ' # Cria a pasta
    command +=f'&& cd {nomePasta} ' # Troca para a pasta criada
    command += '&& type nul > main.py ' # cria um arquivo .py
    command += '&& type nul > notas.txt ' # cria um arquivo .txt
    command += '&& cd ..' # volta parar a raiz
    os.system(command)

