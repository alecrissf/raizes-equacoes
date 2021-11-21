"""
Módulo contendo funções para construção dos quadros resposta e comparativo.
"""
from tkinter import Tk, NO, END
from tkinter import ttk
import metodos
from funcao import func


class Quadro:
    """
    Classe utilitária para a criação dos quadros resposta e comparativo.
    """
    def __init__(self, linhas: 'list[Linha]', tamanhos_colunas: 'list[int]'):
        """
        Recebe uma lista de linhas onde a primeira representa o cabeçalho do Quadro.
        """
        self.linhas = linhas
        self.tamanhos_colunas = tamanhos_colunas

    def mostrar(self):
        """
        Mostra o quadro.
        """
        print()
        self.linhas[0].mostrar(self.tamanhos_colunas, True)
        print()
        for linha in self.linhas[1:]:
            linha.mostrar(self.tamanhos_colunas)

    def mostrar_janela(self):
        """
        Mostra o quadro em uma janela usando tkinter.
        """
        janela = Tk()
        janela.title("Quadro Resposta")

        tree = ttk.Treeview(
            janela,
            selectmode="browse",
            column=[f"column{i+1}" for i in range(len(self.tamanhos_colunas))],
            show='headings')

        for i in range(len(self.tamanhos_colunas)):
            tree.column(f"column{i+1}",
                        width=self.tamanhos_colunas[i],
                        minwidth=50,
                        stretch=NO)
            tree.heading(f"#{i+1}", text=self.linhas[0].colunas[i])

        for i in range(1, len(self.linhas)):
            tree.insert("", END, values=self.linhas[i].colunas, tag='1')

        tree.grid(row=0, column=0)
        janela.mainloop()

        print("Quadro aberto em nova janela, feche-a para continuar...")

    class Linha:
        """
        Classe utilitária para a criação de linhas do quadro.
        """
        def __init__(self, colunas: list):
            self.colunas = colunas

        def mostrar(self, tamanhos_colunas: 'list[int]', eh_cabecalho=False):
            """
            Mostra a linha.
            """
            print("[ ", end="")
            for i in range(len(self.colunas)):
                col = str(self.colunas[i])[:tamanhos_colunas[i]]
                print(f"{col}".ljust(tamanhos_colunas[i]), end="")
                print(" | "
                      if i < len(self.colunas) - 1 and eh_cabecalho else "   ",
                      end="")
            print(" ]")


def menu_escolha_metodo():
    """
    Retorna a opção escolhida:
    1. Calculo pelo método da Bissecção
    2. Calculo pelo método da Posição Falsa
    3. Calculo pelo método de Newton-Raphson
    """
    escolha = {
        1: "- Calculo pelo método da Bissecção",
        2: "- Calculo pelo método da Posição Falsa",
        3: "- Calculo pelo método de Newton-Raphson",
    }
    for key, value in escolha.items():
        print(key, value)
    print()
    escolha = input("Qual método você deseja utilizar? ")
    print()
    return escolha


def pedir_intervalos():
    """
    Retorna o intervalo (a, b)
    Retorna: (int_a, int_b)
    """
    int_a = float(input("Informe o valor do início do intervalo (a): "))
    int_b = float(input("Informe o valor do fim do intervalo (b): "))
    return int_a, int_b


def pedir_dados_res():
    """
    Retorna os dados necessários para a execução dos métodos no contexto do quadro resposta.
    Retorna: (param_a, param_i, prec)
    """
    param_a = float(input("Informe o valor do parâmetro de ajuste inicial: "))
    param_i = float(input("Informe o incremento do parâmetro de ajuste: "))
    # int_a, int_b = pedir_intervalos()
    prec = float(input("Informe a precisão: "))
    return param_a, param_i, prec


def pedir_dados_comp():
    """
    Retorna os dados necessários para a execução dos métodos no contexto do quadro comparativo.
    Retorna: (param_a, int_a, int_b, prec)
    """
    param_a = float(input("Informe o valor do parâmetro de ajuste: "))
    int_a, int_b = pedir_intervalos()
    prec = float(input("Informe a precisão: "))
    return param_a, int_a, int_b, prec


def quadro_resposta():
    """
    Mostra o quadro resposta.
    """
    metodo = menu_escolha_metodo()
    num = int(input("Qual a quantidade de aviões a serem testados? "))
    print()
    param_a, param_i, prec = pedir_dados_res()

    linhas = [Quadro.Linha(["Parâmetro(a)", "valor de d", "Erro", "Método"])]

    for i in range(num):
        print(f"\nIntervalo para o avião {i}:")
        int_a, int_b = pedir_intervalos()

        try:
            func(int_a, param_a)
        except ValueError:
            print(f"A função f não estã definida para o valor {int_a}")

        # Calculo pelo método da Bissecção.
        if metodo == '1':
            x_f, erro = metodos.bisseccao(param_a, int_a, int_b, prec)
            cols = [param_a, x_f, erro, "Bissecção"]
            linhas.append(Quadro.Linha(cols))

        # Calculo pelo método da Posição Falsa.
        elif metodo == '2':
            x_f, erro = metodos.posicao_falsa(param_a, int_a, int_b, prec)
            cols = [param_a, x_f, erro, "Posição Falsa"]
            linhas.append(Quadro.Linha(cols))

        # Calculo pelo método de Newton-Raphson.
        elif metodo == '3':
            x_init = (int_a + int_b) / 2
            x_f, erro = metodos.newton_raphson(param_a, x_init, prec)
            cols = [param_a, x_f, erro, "Newton-Raphson"]
            linhas.append(Quadro.Linha(cols))

        param_a = param_a + param_i

    quadro = Quadro(linhas, [25, 25, 25, 25])
    quadro.mostrar()
    # quadro = Quadro(linhas, [100, 200, 200, 300])
    # quadro.mostrar_janela()
    print()


def quadro_comparativo():
    """
    Mostra o quadro comparativo.
    """
    escolha = {
        1: "- Calculo pelo método da Bissecção",
        2: "- Calculo pelo método da Posição Falsa",
        3: "- Calculo pelo método de Newton-Raphson",
    }

    linhas = [
        Quadro.Linha(
            ["Método", "Parâmetro(a)", "valor de d", "Erro", "Isolamento"])
    ]

    for i, metodo in escolha.items():
        print(i, metodo)
        param_a, int_a, int_b, prec = pedir_dados_comp()

        # Calculo pelo método da Bissecção.
        if i == 1:
            x_f, err = metodos.bisseccao(param_a, int_a, int_b, prec)
            cols = ["Bissecção", param_a, x_f, err, f"({int_a}, {int_b})"]
            linhas.append(Quadro.Linha(cols))

        # Calculo pelo método da Posição Falsa.
        elif i == 2:
            x_f, err = metodos.posicao_falsa(param_a, int_a, int_b, prec)
            cols = ["Posição Falsa", param_a, x_f, err, f"({int_a}, {int_b})"]
            linhas.append(Quadro.Linha(cols))

        # Calculo pelo método de Newton-Raphson.
        elif i == 3:
            x_init = (int_a + int_b) / 2
            x_f, err = metodos.newton_raphson(param_a, x_init, prec)
            cols = ["Newton-Raphson", param_a, x_f, err, f"({int_a}, {int_b})"]
            linhas.append(Quadro.Linha(cols))

    quadro = Quadro(linhas, [22, 22, 22, 22, 12])
    quadro.mostrar()
    # quadro = Quadro(linhas, [300, 100, 200, 200])
    # quadro.mostrar_janela()
    print()
