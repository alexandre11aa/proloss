'''
Cálculo de perda de protensão por encurtamento imediato do concreto explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 155-158.
'''

import math

def encurtamento_imediato_do_concreto(Ac, ycin, Ic, 
                                      Ep, Ap, n_fios, 
                                      fck28, Mg, n, 
                                      dias, forcas, altura):
    
    Ac = float(Ac)
    ycin = float(ycin)
    Ic = float(Ic)
    Ep = float(Ep)
    Ap = float(Ap)
    n_fios = float(n_fios)
    fck28 = float(fck28)
    Mg = float(Mg)
    n = float(n)

    # Ajustando Unidades

    ajuste_1 = 10**(-4)

    # Calculando

    # Módulos de elasticidade do concreto

    fcks, Ecis = [[],[]]

    for i in range(len(dias)):

        dias[i] = float(dias[i])
        forcas[i] = float(forcas[i])
        altura[i] = float(altura[i])

        # Calculando

        fcks.append(fck28 * math.e**(0.25 * (1 - (28 / dias[i])**(1/2))))
        Ecis.append(5600 * (fcks[i])**(1/2))

    Eci_med = sum(Ecis) / len(Ecis)

    alpha_p = Ep * 1000 / Eci_med

    # Tensões produzidas por todos os cabos

    y0, NP0i_epi = [0, 0]

    alturas_unicas = list(set(altura))

    for i in range(len(alturas_unicas)):
        n_1, n_2 = [0, 0]

        for j in range(len(altura)):
            if alturas_unicas[i] == altura[j]:
                n_1 += 1
                n_2 += forcas[j]
            
                y0 += alturas_unicas[i] / 100

        NP0i_epi += n_2 * (ycin - (alturas_unicas[i] / 100))

    y0 /= len(altura)

    ocp = (sum(forcas) / Ac) + ((NP0i_epi / Ic) * (ycin - y0))

    # Tensão mobilizada pela protenção no C.G. de Ap.

    ocg = Mg * (ycin - y0) / Ic

    # Perda média de protensão por encurtamento imediato do concreto

    delta_op = ((n - 1) / (n * 2)) * alpha_p * (ocp + ocg)

    # Perda da força de protenção para cabos

    perda_de_forca_todos_os_cabos = []

    for i in range(len(forcas)):
        perda_de_forca_todos_os_cabos.append(forcas[i] - n_fios * Ap * ajuste_1 * delta_op)

    return ('%.4f' % ocp, 
            '%.4f' % ocg, 
            '%.4f' % delta_op, 
            perda_de_forca_todos_os_cabos)
