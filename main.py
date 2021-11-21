"""
Módulo Principal
"""
import metodos
import quadro


def menu_escolha_principal():
    """
    Retorna a opção escolhida:
    1. Calculo pelo método da Bissecção
    2. Calculo pelo método da Posição Falsa
    3. Calculo pelo método de Newton-Raphson
    4. Fornecer quadro resposta
    5. Fornecer quadro comparativo
    6. Sair
    """
    escolha = {
        1: "- Calculo pelo método da Bissecção",
        2: "- Calculo pelo método da Posição Falsa",
        3: "- Calculo pelo método de Newton-Raphson",
        4: "- Fornecer quadro resposta",
        5: "- Fornecer quadro comparativo",
        6: "- Sair"
    }
    for key, value in escolha.items():
        print(key, value)
    print()
    escolha = input("Qual função você deseja realizar? ")
    print()
    return escolha


def pedir_dados():
    """
    Retorna os dados necessários para a execução dos métodos.
    Retorna: (param_a, int_a, int_b, prec)
    """
    param_a = float(input("Informe o valor do parâmetro de ajuste: "))
    int_a = float(input("Informe o valor do início do intervalo (a): "))
    int_b = float(input("Informe o valor do fim do intervalo (b): "))
    prec = float(input("Informe a precisão: "))
    return param_a, int_a, int_b, prec


def main():
    """
    Função principal.
    """
    while True:
        escolha = menu_escolha_principal()

        # Calculo pelo método da Bissecção.
        if escolha == '1':
            param_a, int_a, int_b, prec = pedir_dados()
            x_f, erro = metodos.bisseccao(param_a, int_a, int_b, prec)
            print(f"\nO valor da raiz é: {x_f}\nCom erro de: {erro}\n")

        # Calculo pelo método da Posição Falsa.
        elif escolha == '2':
            param_a, int_a, int_b, prec = pedir_dados()
            x_f, erro = metodos.posicao_falsa(param_a, int_a, int_b, prec)
            print(f"\nO valor da raiz é: {x_f}\nCom erro de: {erro}\n")

        # Calculo pelo método de Newton-Raphson.
        elif escolha == '3':
            param_a, int_a, int_b, prec = pedir_dados()
            x_init = (int_a + int_b) / 2
            x_f, erro = metodos.newton_raphson(param_a, x_init, prec)
            print(f"\nO valor da raiz é: {x_f}\nCom erro de: {erro}\n")

        # Fornecer quadro resposta.
        elif escolha == '4':
            quadro.quadro_resposta()

        # Fornecer quadro comparativo.
        elif escolha == '5':
            quadro.quadro_comparativo()

        # Sair.
        elif escolha == '6':
            break

        input("Pressione Enter para continuar...")
        print()


if __name__ == "__main__":
    main()
