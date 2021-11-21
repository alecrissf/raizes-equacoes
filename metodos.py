"""
Módulo contendo os métodos númericos:
- Bissecção
- Posição Falsa
- Newton-Raphson
"""
import math
from funcao import func, d_func


def bisseccao(param_a, int_a, int_b, prec, max_iter=100):
    """
    Resolve o problema das raizes usando o método da Bissecção
    recebe os parâmetros:
    - param_a: parâmetro de ajuste da função f
    - int_a: início do intervalo de isolamento (a, b)
    - int_b: fim do intervalo de isolamento (a, b)
    - prec: precisão do método
    - max_iter: número máximo de iterações do programa (padrão 100)

    Retorna o resultado de x ou -1 caso não possua raizes no intervalo
    TODO: retornar erro junto com o valor de x
    """
    # Caso f(a) * f(b) > 0, o intervalo (a,b) não possui raizes.
    if func(int_a, param_a) * func(int_b, param_a) > 0:
        return -1
    # Contador de iterações.
    cont = 0
    # Ponto médio.
    x_f = (int_a + int_b) / 2
    # Iterar até o valor de f(x) ser menor que a precisão.
    while math.fabs(func(x_f, param_a)) > prec:
        if func(int_a, param_a) * func(x_f, param_a) < 0:
            int_b = x_f
        else:
            int_a = x_f
        # Ponto médio.
        x_f = (int_a + int_b) / 2
        # Incrementar o contador.
        cont = cont + 1
        # Se atingir o número máximo de iterações interromper.
        if cont >= max_iter:
            break

    return x_f


def posicao_falsa(param_a, int_a, int_b, prec, max_iter=100):
    """
    Resolve o problema das raizes usando o método da Posição Falsa
    - param_a: parâmetro de ajuste da função f
    - int_a: início do intervalo de isolamento (a, b)
    - int_b: fim do intervalo de isolamento (a, b)
    - prec: precisão do método
    - max_iter: número máximo de iterações do programa (padrão 100)

    Retorna o resultado de x ou -1 caso não possua raizes no intervalo
    TODO: retornar erro junto com o valor de x
    """
    # Caso f(a) * f(b) > 0, o intervalo (a,b) não possui raizes.
    if func(int_a, param_a) * func(int_b, param_a) > 0:
        return -1
    # Contador de iterações.
    cont = 0
    # Ponto médio.
    x_f = (int_a * func(int_b, param_a) - int_b * func(int_a, param_a)) / (
        func(int_b, param_a) - func(int_a, param_a))
    # Iterar até o valor de f(x) ser menor que a precisão.
    while math.fabs(func(x_f, param_a)) > prec:
        if func(int_a, param_a) * func(x_f, param_a) < 0:
            int_b = x_f
        else:
            int_a = x_f

        # Ponto médio.
        x_f = (int_a * func(int_b, param_a) - int_b * func(int_a, param_a)) / (
            func(int_b, param_a) - func(int_a, param_a))
        # Incrementar o contador.
        cont = cont + 1
        # Se atingir o número máximo de iterações interromper.
        if cont >= max_iter:
            break

    return x_f


def newton_raphson(param_a, x_init, prec, max_iter=100):
    """
    Resolve o problema das raizes usando o método de Newton-Raphson
    - param_a: parâmetro de ajuste da função f
    - x_init: aproximação para o x inicial
    - prec: precisão do método
    - max_iter: número máximo de iterações do programa (padrão 100)

    Retorna o resultado de x ou -1 caso não possua raizes no intervalo
    TODO: retornar erro junto com o valor de x
    """
    # Contador de iterações.
    cont = 0
    # Valor de x
    x_f = x_init
    # Iterar até o valor de f(x) ser menor que a precisão.
    while math.fabs(func(x_f, param_a)) > prec:
        # Calcular o novo x.
        x_f = x_f - (func(x_f, param_a) / d_func(x_f, param_a))
        # Incrementar o contador.
        cont = cont + 1
        # Se atingir o número máximo de iterações interromper.
        if cont >= max_iter:
            break

    return x_f
