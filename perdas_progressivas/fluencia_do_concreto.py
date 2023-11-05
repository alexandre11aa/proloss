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

def fluencia_do_concreto(U, Ti, t0, t, h, abatimento, CP):

    Q = []

    for i in range(len(U)):

        # Ajustando Formatos

        U[i] = float(U[i])
        Ti[i] = float(Ti[i])
        t0[i] = float(t0[i])
        h[i] = float(h[i])

        # Primeira Variável

        if CP[i] == 'I' or CP[i] == 'II':

            if t[i] == '∞':
                fc = 1.267

            coeficiente = 0.25

            alpha = 2

        elif CP[i] == 'III' or CP[i] == 'IV':

            if t[i] == '∞':
                fc = 1.433
        
            coeficiente = 0.38

            alpha = 1

        elif CP[i] == 'V':
            
            if t[i] == '∞':
                fc = 1.208

            coeficiente = 0.20

            alpha = 3

        fc0 = math.e**(coeficiente * (1 - (28/(t0[i] / (alpha * ((Ti[i] + 10) / 30))))**(1/2)))

        if t[i] != '∞':

            t[i] = float(t[i])

            fc = math.e**(coeficiente * (1 - (28/(t[i] / (alpha * ((Ti[i] + 10) / 30))))**(1/2)))
 
        Qa = 0.8 * (1 - (fc0 / fc))

        # Segunda Variável

        if abatimento[i] == '0 - 4' and U[i] <= 90:
            Q1c = (4.45 - 0.035 * U[i]) * 0.75

        elif abatimento[i] == '5 - 9' and U[i] <= 90:
            Q1c = (4.45 - 0.035 * U[i])

        elif abatimento[i] == '10 - 15' and U[i] <= 90:
            Q1c = (4.45 - 0.035 * U[i]) * 1.25

        Q2c = (42 + h[i]) / (20 + h[i])

        Qf = Q1c * Q2c

        # Coeficiente relativo à deformação lenta irreversível

        Bft0 = calculo_de_Bft(t0[i], h[i])

        if t[i] == '∞':
            Bft = 1
            Bd = 1

        elif t[i] != '∞':
            Bft = calculo_de_Bft(t[i], h[i])
            Bd = (t[i] - t0[i] + 20) / (t[i] - t0[i] + 70)

        # Valor final do coeficiente de deformação lenta reversível

        Qd = 0.4

        # Valor da Deformação por Fluência

        Q.append('%.4f' % (Qa + Qf * (Bft - Bft0) + Qd * Bd))

    return Q

def superposicao_de_efeitos(Q, o, fck):
    
    Q_o = []

    ecc = 0

    Eci_28 = 1 / (5600000 * fck**(1/2))

    for i in range(len(Q)):

        # Ajustando Formatos

        Q[i] = float(Q[i])
        o[i] = float(o[i])
        fck[i] = float(fck[i])

        # Calculando

        ecc += float(Q[i]) * float(o[i])

        Q_o.append('%.3f' % (float(Q[i]) * float(o[i])))

    ecc *= Eci_28

    return '%.2e' % ecc, Q_o
