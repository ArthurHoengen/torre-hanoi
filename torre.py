def print_towers(towers):
    for i, tower in enumerate(towers):
        print(f"Torre {chr(65 + i)}: {tower}")
    print("-" * 30)


def hanoi(n, origem_idx, destino_idx, auxiliar_idx, towers):
    if n == 1:
        disco = towers[origem_idx].pop()
        towers[destino_idx].append(disco)
        print(f"Movendo disco {disco} de {chr(65 + origem_idx)} para {chr(65 + destino_idx)}")
        print_towers(towers)
    else:
        hanoi(n - 1, origem_idx, auxiliar_idx, destino_idx, towers)
        hanoi(1, origem_idx, destino_idx, auxiliar_idx, towers)
        hanoi(n - 1, auxiliar_idx, destino_idx, origem_idx, towers)


def resolver_torre_hanoi(n, torre_origem, torre_destino):
    torre_origem = torre_origem.upper()
    torre_destino = torre_destino.upper()

    if torre_origem not in "ABC" or torre_destino not in "ABC" or torre_origem == torre_destino:
        print("Erro: Escolha torres diferentes entre A, B e C.")
        return

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2}
    origem_idx = letra_para_indice[torre_origem]
    destino_idx = letra_para_indice[torre_destino]
    auxiliar_idx = 3 - origem_idx - destino_idx

    torre_A = list(reversed(range(1, n + 1))) if origem_idx == 0 else []
    torre_B = list(reversed(range(1, n + 1))) if origem_idx == 1 else []
    torre_C = list(reversed(range(1, n + 1))) if origem_idx == 2 else []
    towers = [torre_A, torre_B, torre_C]

    print(f"Estado inicial (Origem: {torre_origem}, Destino: {torre_destino}):")
    print_towers(towers)

    hanoi(n, origem_idx, destino_idx, auxiliar_idx, towers)


resolver_torre_hanoi(5, 'B', 'C')