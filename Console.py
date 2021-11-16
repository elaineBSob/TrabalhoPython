from Calculadora import safe_number

def linha(tam):
    print("=-"*(tam-1) + "=")

def cabecalho(texto, fecha=False, tam=40):
    linha(tam)
    print(texto.center(tam*2))
    if fecha:
        linha(tam)

def opcoes(opcoes, seta="> "):
    for op in enumerate(opcoes,1):
        print(str(op[0]) + ") " + str(op[1]))
    linha(40)
    while True:
        op = safe_number(seta=seta)
        if op <= len(opcoes):
            return op
        else:
            print("Erro: Opção Inválida")

