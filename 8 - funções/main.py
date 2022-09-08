# O asterico serve para indicar
# que não se sabe o número de argumentos ( arguments )
# os tipos também não são esperados, ou seja, qualquer um

def args(*args):
    mensagem = ""

    argsLength = len(args) - 1

    if argsLength >= 0:
        mensagem += "-"*30
        mensagem += f"\n{args[0]}"
    if argsLength >= 1:
        mensagem += f"\n{args[1]}"
    
    if mensagem != "":
        mensagem += "\n"
        mensagem += "-"*30

    # multipleArgs(["teste", "asda", True], 0)
    print(mensagem)

# Os astericos serve para indicar
# que não se sabe o número de argumentos de arguments ( keyword arguments )
# os tipos também não são esperados, ou seja, qualquer um
def kwargs(**kwargs):
    nome = kwargs['nome']
    idade = kwargs.get('idade')
    # se não tiver a chave então a variável ficara
    # vazia ( None ) e o python entendera como False
    if idade:  # se declarar a chave e for maior que 0
        from datetime import datetime
        
        current_date = datetime.now()
        current_year = current_date.year
        
        # kwargs(nome="Gabriel", idade=19)
        print(f"Olá {nome}, você nasceu em {current_year - idade} ?")
    else:
        # kwargs(nome="Gabriel")
        print(f"Olá {nome} !")

