'''
Cálculos auxiliares explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 159-163.
'''

import math

def calculo_da_espessura_ficticia(Ac, u_ar, U):

    h_fic = []

    for i in range(len(U)):

        h_fic.append(100 * (1 + math.e**(-7.8 + 0.1 * U[i])) * (2 * Ac) / u_ar)

    return h_fic

def calculo_da_idade_ficticia(a, Ti, delta_t):
    
    constante = 0

    for i in range(len(Ti)):

        constante += ((Ti[i] + 10) / 30) * delta_t[i]

    t_fic = []

    for i in range(len(a)):

        t_fic.append('%.4f' % (a[i] * constante))

    return t_fic

'''
CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 162.

print('Aplicação numérica (Espessura fictícia): ' + str(calculo_da_espessura_ficticia(0.86, 8.2, [40, 60, 80])))

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 163.

print('Aplicação numérica (Idade fictícia): ' + str(calculo_da_idade_ficticia([2, 1, 3], [30, 26, 20], [7, 12, 9])))
'''