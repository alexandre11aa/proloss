import math

# Espessura Fictícia

def calculo_da_espessura_ficticia(Ac, u_ar, U):

    h_fic = []

    for i in range(len(U)):

        h_fic.append(100 * (1 + math.e**(-7.8 + 0.1 * U[i])) * (2 * Ac) / u_ar)

    return h_fic

'''
CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 160, 162.

print('Aplicação numérica (Espessura fictícia): ' + str(calculo_da_espessura_ficticia(0.86, 8.2, [40, 60, 80])))
'''

# Idade Fictícia

def calculo_da_idade_ficticia(a, Ti, delta_t):
    
    constante = 0

    for i in range(len(Ti)):

        constante += ((Ti[i] + 10) / 30) * delta_t[i]

    t_fic = []

    for i in range(len(a)):

        t_fic.append('%.4f' % (a[i] * constante))

    return t_fic

'''
CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 161, 163.

print('Aplicação numérica (Idade fictícia): ' + str(calculo_da_idade_ficticia([2, 1, 3], [30, 26, 20], [7, 12, 9])))
'''

# Efeito Conjunto de Retração e Fluência

def efeito_conjunto_retracao_e_fluencia(Ep, Ecs, Ecc, Eci28, ocP0, oP0, y):

    return (Ep * (Ecs + Ecc)) / (1 - (Ep * ocP0  / (Eci28 * oP0)) * (1 + y / 2))

'''
CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 182-189.

print(efeito_conjunto_retracao_e_fluencia(200 * 10**6, -18 * 10**(-5), -0.0011763725, 32 * 10**6, -29143.6, 1242603.5, 1.95))
'''
