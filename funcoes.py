# importa função matemática para calcular raiz quadrada
import math

# função que calcula equação do 1º grau
def calcular_1_grau(a, b):
    x = -b/a
    return x

# função que calcula delta
def calcular_delta(a, b, c):
    delta = b**2 - (4*a*c)
    return delta

# função que calcula x'
def calcular_x_linha(a, b, c):
    x = (-b + math.sqrt(calcular_delta(a, b, c)))/(2*a)
    return x

# função que calcula x"
def calcular_x_2_linha(a, b, c):
    x = (-b - math.sqrt(calcular_delta(a, b, c)))/(2*a)
    return x

# função que calcula equação do 2º grau
def calcular_2_grau(a, b, c):
    delta = calcular_delta(a, b, c)

    if delta > 0:
        return f'x linha = {calcular_x_linha(a, b, c)}. x 2 linha = {calcular_x_2_linha(a, b, c)}.'
    elif delta == 0:
        x = -b/(2*a)
        return x
    else:
        return 'A equação não possui uma solução real.'