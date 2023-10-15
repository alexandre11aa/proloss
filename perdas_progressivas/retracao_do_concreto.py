'''
Cálculo de perda de protensão por retração do concreto explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 164-169.
'''

def calculo_de_Bst(t_fic, h_fic):

    if h_fic / 100 <= 0.05:
        h_fic = 0.05

    elif h_fic / 100 >= 1.6:
        h_fic = 1.6

    else:
        h_fic /= 100

    A = 40
    B = 116 * h_fic**3 - 282 * h_fic**2 + 220 * h_fic - 4.8
    C = 2.5 * h_fic**3 - 8.8 * h_fic + 40.7
    D = -75 * h_fic**3 + 585 * h_fic**2 + 496 * h_fic - 6.8
    E = -169 * h_fic**4 + 88 * h_fic**3 + 584 * h_fic**2 - 39 * h_fic + 0.8

    t_1 = (t_fic / 100)**3
    t_2 = (t_fic / 100)**2
    t_3 = (t_fic / 100)

    return (t_1 + A * t_2 + B * t_3) / (t_1 + C * t_2 + D * t_3 + E)

def retracao_do_concreto(U, t0, t, h, abatimento):

    ecs = []

    for i in range(len(U)):

        # Primeira Variável

        if abatimento[i] == '0 - 4':
            ajuste = 0.75

        elif abatimento[i] == '5 - 9':
            ajuste = 1
        
        elif abatimento[i] == '10 - 15':
            ajuste = 1.25
        
        e1s = ((- 6.16 - (U[i] / 484) + (U[i]**2 / 1590)) * ajuste) / 10**4

        # Segunda Variável

        e2s = (33 + 2 * h[i]) / (20.8 + 3 * h[i])

        # Terceira Variável

        Bs_t0 = calculo_de_Bst(t0[i], h[i])

        if t[i] == '∞':
            Bs_t = 1
        
        else:
            Bs_t = calculo_de_Bst(t[i], h[i])

        # Resultado

        ecs.append(e1s * e2s * (Bs_t - Bs_t0))

    return ecs
