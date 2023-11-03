import math

# Espessura Fictícia - CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 160, 162.

def calculo_da_espessura_ficticia(Ac, u_ar, U):

    h_fic = []

    for i in range(len(U)):

        h_fic.append(100 * (1 + math.e**(-7.8 + 0.1 * U[i])) * (2 * Ac) / u_ar)

    return h_fic

# Idade Fictícia - CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 161, 163.

def calculo_da_idade_ficticia(a, Ti, delta_t):
    
    constante = 0

    for i in range(len(Ti)):

        constante += ((Ti[i] + 10) / 30) * delta_t[i]

    t_fic = []

    for i in range(len(a)):

        t_fic.append('%.4f' % (a[i] * constante))

    return t_fic

# Efeito Conjunto de Retração e Fluência - CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 182-189.

def efeito_conjunto_retracao_e_fluencia(Ep, Ecs, Ecc, Eci28, ocP0, oP0, y):

    lista_de_resultados = []

    # Ajustando unidades de medidas

    ajuste_1 = 10**6

    ajuste_2 = 10**(-5)

    for i in range(len(Ep)):

        lista_de_resultados.append("%.2f" % ((Ep[i] * ajuste_1 * (Ecs[i] * ajuste_2 + Ecc[i] * ajuste_2)) / (1 - (Ep[i] * ajuste_1 * ocP0[i]  / (Eci28[i] * ajuste_1 * oP0[i])) * (1 + y[i] / 2))))

    return lista_de_resultados

# Método Geral para Perda de Tensão - CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 196-202.

def perda_de_tensao_pelo_metodo_geral_funcoes(delta_cs, delta_rrel):

    return '%.2f' % (delta_cs + delta_rrel)
