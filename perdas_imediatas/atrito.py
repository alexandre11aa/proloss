'''
Cálculo de perda de protensão por atrito através do processo simplificado explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 128-144.
'''

import numpy as np

def calculo_da_forca(n_cordoalhas, area, fptk, fpyk):

    # Ajustando Unidades

    ajuste_1 = 10**(3)
    ajuste_2 = 10**(-4)

    # Calculando

    if (0.74 * fptk) < (0.82 * fpyk):
        forca_i = n_cordoalhas * area * ajuste_2 * (0.74 * fptk) * ajuste_1

    else:
        forca_i = n_cordoalhas * area * ajuste_2 * (0.82 * fpyk) * ajuste_1

    return forca_i

def atrito(variaveis_para_forca, distancias, situacao, alturas, constante_u):

    # Ajustando Formatos

    variaveis_para_forca[0] = float(variaveis_para_forca[0])
    variaveis_para_forca[1] = float(variaveis_para_forca[1])
    variaveis_para_forca[2] = float(variaveis_para_forca[2])
    variaveis_para_forca[3] = float(variaveis_para_forca[3])

    constante_u = float(constante_u)

    # Calculando

    forca = calculo_da_forca(variaveis_para_forca[0],
                             variaveis_para_forca[1],
                             variaveis_para_forca[2],
                             variaveis_para_forca[3])

    iteracoes, distancia, perdas, constante_a = [len(distancias), distancias[0], [forca], 0]

    perda_media = 0

    for i in range(iteracoes):

        # Ajustando Formatos

        alturas[i] = float(alturas[i])
        alturas[i + 1] = float(alturas[i + 1])
        distancias[i] = float(distancias[i])
        perdas[i] = float(perdas[i])

        # Ajustando Unidades

        ajuste_1 = 10**(-1)

        # Calculando

        perda_media += perdas[i] * distancias[i]

        if (situacao[i] == 'Curvo'):
            constante_a += 2 * (abs(alturas[i] - alturas[i + 1]) / distancias[i])
        
        perdas.append(forca * np.exp(- (constante_u * constante_a + ajuste_1 * constante_u * distancia)))

        if (i != iteracoes - 1):

            distancias[i + 1] = float(distancias[i + 1])
            
            distancia += distancias[i + 1]

        perda_percentual = ((forca - perdas[-1]) / forca) * 100

    perda_media /= (200 * variaveis_para_forca[0] * variaveis_para_forca[1] * ajuste_1)

    return (perdas, '%.2f' % perda_media, perda_percentual)
