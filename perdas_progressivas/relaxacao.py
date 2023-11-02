'''
Cálculo de perda de protensão por relaxação pura e relativa explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 189-193.
'''

def interpolacao_linear(op0, tabela):

    op0_tab = [0.500, 0.600, 0.700, 0.800]

    for i in range(4):

        if op0_tab[i] > op0:
            indice = i - 1
            break

    w = tabela[indice] + ((op0 - op0_tab[indice]) / (op0_tab[indice + 1] - op0_tab[indice])) * (tabela[indice + 1] - tabela[indice])

    return w

def relaxacao_pura(n, Ap, P0, Mg, ep, Ep, Ic, Eci28, fptk, t0, t, relaxacao):

    # Ajustando Unidades de Medida

    Ap *= 10**(-4)

    fptk *= 1000

    # Calculando

    opi = ((n * P0) / (n * Ap)) + ((Mg * ep * Ep) / (Ic * Eci28))

    op0 = opi / fptk

    if op0 >= 0.5 and op0 <= 0.8:

        if relaxacao == 'Cord. RN':
            tabela = [0.000, 3.500, 7.000, 12.00]

        elif relaxacao == 'Cord. RB':
            tabela = [0.000, 1.300, 2.500, 3.500]

        elif relaxacao == 'Fios RN':
            tabela = [0.000, 2.500, 5.000, 8.500]

        elif relaxacao == 'Fios RB':
            tabela = [0.000, 1.000, 2.000, 3.000]

        elif relaxacao == 'Barras':
            tabela = [0.000, 1.500, 4.000, 7.000]

        w1000 = interpolacao_linear(op0, tabela)

    elif op0 < 0.5:

        w1000 = 0

    if t == '∞':

        w = 2.5 * w1000

    elif t != '∞':

        w = w1000 * ((t - t0) / 41.67)**0.15

    delta_o_pr = w * opi / (100 * 1000)

    return ('%.2f' % w1000), ('%.2f' % delta_o_pr), ('%.2f' % opi)

def relaxacao_relativa(delta_o_pr, delta_p_cs, opi):

    delta_o_pr_rel = float(delta_o_pr) * (1 - 2 * abs(float(delta_p_cs)) / float(opi))

    return ('%.2f' % delta_o_pr_rel)
