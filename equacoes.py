# importa função matemática para calcular raiz quadrada
import math

# função que calcula equação do 1º grau
def calcular_1_grau(a, b):
    x = -b/a
    return x

# função que calcula equação do 2º grau
def calcular_2_grau(a, b, c):
    delta = b**2 - (4*a*c)

    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        yield f'x1 = {x1}'
        yield f'x2 = {x2}'
    elif delta == 0:
        x = -b/(2*a)
        return f'x = {x}'
    else:
        return 'A equação não possui uma solução real.'