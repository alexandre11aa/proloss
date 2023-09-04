'''
Cálculo de perda de protensão por atrito através do processo simplificado explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 128-144.
'''

import numpy as np

def calculo_da_forca(n_cordoalhas, area, fptk, fpyk):

    if (0.74 * float(fptk)) < (0.82 * float(fpyk)):
        forca_i = float(n_cordoalhas) * float(area) * 10**(-4) * (0.74 * float(fptk)) * 10**(3)

    else:
        forca_i = float(n_cordoalhas) * float(area) * 10**(-4) * (0.82 * float(fpyk)) * 10**(3)

    return forca_i

def atrito(variaveis_para_forca, distancias, situacao, alturas, constante_u):

    forca = calculo_da_forca(variaveis_para_forca[0],
                             variaveis_para_forca[1],
                             variaveis_para_forca[2],
                             variaveis_para_forca[3])

    iteracoes, distancia, perdas, constante_a = [len(distancias), distancias[0], [forca], 0]

    perda_media = 0

    for i in range(iteracoes):

        perda_media += perdas[i] * distancias[i]

        if (situacao[i] == 'Curvo'):
            constante_a += 2 * (abs(float(alturas[i]) - float(alturas[i + 1])) / float(distancias[i]))
        
        perdas.append(forca * np.exp(- (float(constante_u) * constante_a + 0.01 * float(constante_u) * distancia)))

        if (i != iteracoes - 1):
            distancia += float(distancias[i + 1])

        perda_percentual = ((forca - perdas[-1]) / forca) * 100

    perda_media /= (200 * variaveis_para_forca[0] * variaveis_para_forca[1] * 10**(-1))

    return (perdas, '%.2f' % perda_media, perda_percentual)
