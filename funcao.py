"""
Módulo contendo a função do problema.
"""

import math


def func(x_f, a_f):
    """
    Função f, recebe um valor 'x' e o parametro 'a'
    """
    return a_f * x_f - x_f * math.log(x_f, math.e)


def d_func(x_f, a_f):
    """
    Derivada da função f, recebe um valor 'x' e o parametro 'a'
    """
    return a_f - math.log(x_f, math.e) - 1
