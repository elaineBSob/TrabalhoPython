def safe_number(seta="> "):
    while True:
        try:
            num = int(input(seta))
        except ValueError:
            print("Erro: Número inválido")
        except KeyboardInterrupt:
            print("Erro: teclado interrompido")
            exit()
        except Exception as e:
            print("Erro: ",e)
        else:
            return num

def safe_float(seta="> "):
    while True:
        try:
            num = float(input(seta))
        except ValueError:
            print("Erro: Número inválido")
        except KeyboardInterrupt:
            print("Erro: teclado interrompido")
            exit()
        except Exception as e:
            print("Erro: ",e)
        else:
            return num

def get_media(notas):
    av1 = notas[0]
    av2 = notas[1]
    av3 = notas[2]
    avd = notas[3]
    avds = notas[4]

    digital = avd
    av = (av1,av2)

    if av3 > av1 or av3 > av2:
        if av2 > av1:
            av = (av3,av2)
        else:
            av = (av3,av1)

    if avds > avd:
        digital = avds
    
    return (av[0] + av[1] + digital) / 3