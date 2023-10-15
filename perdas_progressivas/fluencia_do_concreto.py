'''
Cálculo de perda de protensão por fluência do concreto explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 169-181.
'''

import math

def calculo_de_Bft(t_fic, h_fic):

    if h_fic / 100 <= 0.05:
        h_fic = 0.05

    elif h_fic / 100 >= 1.6:
        h_fic = 1.6

    else:
        h_fic /= 100

    A = 42 * h_fic**3 - 350 * h_fic**2 + 588 * h_fic + 113
    B = 768 * h_fic**3 - 3060 * h_fic**2 + 3234 * h_fic - 23
    C = -200 * h_fic**3 + 13 * h_fic**2 + 1090 * h_fic + 183
    D = 7579 * h_fic**3 - 31916 * h_fic**2 + 35343 * h_fic + 1931

    return (t_fic**2 + A * t_fic + B) / (t_fic**2 + C * t_fic + D)

def fluencia_do_concreto(U, h, CP, t0, t, abatimento):

    Q = []

    for i in range(len(U)):

        # Primeira Variável

        if CP[i] == 'I' or CP[i] == 'II':
            coeficiente = 0.25

        elif CP[i] == 'III' or CP[i] == 'IV':
            coeficiente = 0.38

        elif CP[i] == 'V':
            coeficiente = 0.20

        d0  = t0[i] / (3 * ((U[i] + 10) / 30))
        fc0 = math.e**(coeficiente * (1 - (28/d0)**(1/2)))

        d   = t[i]  / (3 * ((U[i] + 10) / 30))
        fc  = math.e**(coeficiente * (1 - (28/d )**(1/2)))

        Qa = 0.8 * (1 - (fc0 / fc))

        # Segunda Variável

        if abatimento[i] == '0 - 4' and U[i] <= 90:
            Q1c = (4.45 - 0.035 * U[i]) * 0.75

        elif abatimento[i] == '5 - 9' and U[i] <= 90:
            Q1c = (4.45 - 0.035 * U[i])

        elif abatimento[i] == '10 - 15' and U[i] <= 90:
            Q1c = (4.45 - 0.035 * U[i]) * 1.25

        Q2c = (42 * h[i]) / (20 + h[i])

        Qf = Q1c * Q2c

        # Coeficiente relativo à deformação lenta irreversível

        Bft0 = calculo_de_Bft(t0[i], h[i])

        if t0 == '∞':
            Bft = 1
            Bd = 1

        else:
            Bft = calculo_de_Bft(t[i], h[i])
            Bd = (t[i] - t0[i] + 20) / (t[i] - t0[i] + 70)

        # Valor final do coeficiente de deformação lenta reversível

        Qd = 0.4

        # Valor da Deformação por Fluência

        Q.append(Qa + Qf * (Bft - Bft0) * Qd * Bd)

    return Q
