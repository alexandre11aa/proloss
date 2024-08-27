'''
Cálculo de perda de protensão por progressiva do concreto explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 193-202.
'''

import math

def perda_progressiva_processo_simplificado(Ac, Ap,
                                            ecs, e_p, Ep,
                                            fck, Ic, Mg,
                                            y, w1000,
                                            P0, t, t0,
                                            sinal):
    
    a_p = Ep / (5.6 * fck**(1/2))

    Ap *= 10**(-4)

    Ep *= 10**(6)
    
    oP0 = (P0 / Ap) + Mg * (e_p / Ic) * a_p

    pp = Ap / Ac

    if t == "∞":
        w = 2.5 * w1000
    else:
        w = w1000 * ((t - t0) / 41.67)**0.15

    X = - math.log(1 - w)

    Xc = 1 + 0.5 * y

    Xp = 1 + X

    n = 1 + e_p**2 * (Ac / Ic)

    ocpog = (Mg * e_p / Ic) - (P0 / Ac) - (P0 * e_p**2 / Ic)

    if sinal == 'Compressão':
        ocpog = abs(ocpog)
    elif sinal == 'Tração':
        ocpog = abs(ocpog) * -1

    delta_op = (ecs * Ep - a_p * ocpog * y - oP0 * X) / (Xp + Xc * a_p * n * pp)
    
    return '%.1f' % delta_op

def perda_progressiva_metodo_geral(delta_cs, delta_rrel):

    delta_cs = float(delta_cs)
    delta_rrel = float(delta_rrel)

    return '%.1f' % (delta_cs + delta_rrel)
