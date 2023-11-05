'''
Cálculo de perda de protensão por acomodação de ancoragem explicado por Cholfe e Bonilha (2013).

CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 145-154.
'''

def eq_2_grau(a, b, c):

    delta = b**2 - 4 * a * c

    x_1 = (- b + delta**(1/2)) / (2 * a)

    x_2 = (- b - delta**(1/2)) / (2 * a)

    return [x_1, x_2]

def acomodacao_da_ancoragem(delta_w,
                            comprimento_a,
                            comprimento_meio_l,
                            p_i,
                            p_a,
                            p_meio_l,
                            constante_E,
                            area_p,
                            ncd):
    
    comprimento_a = float(comprimento_a)
    comprimento_meio_l = float(comprimento_meio_l)
    p_i = float(p_i)
    p_a = float(p_a)
    p_meio_l = float(p_meio_l)
    constante_E = float(constante_E)
    area_p = float(area_p)
    ncd = float(ncd)
   
    hipoteses = []
  
    for i in range(len(delta_w)):

        delta_w[i] = float(delta_w[i])

        for j in range(3):
            delta_p_1 = (p_i - p_a) / comprimento_a
            delta_p_2 = (p_a - p_meio_l) / (comprimento_meio_l - comprimento_a)

            if   (j + 1) == 1:
                comprimento_w = ((delta_w[i] * constante_E * ncd * area_p * 10**(-1)) / delta_p_1) ** (1/2)

                if comprimento_w < comprimento_a:

                    hipotese = ['HIPOTESE 1',
                                (p_i - delta_p_1 * comprimento_w),
                                (2 * delta_p_1 * comprimento_w),
                                (p_i - 2 * delta_p_1 * comprimento_w)]

                    hipoteses.append(hipotese)

                    break

            elif (j + 1) == 2:

                raizes = eq_2_grau(delta_p_2, 
                                   2 * delta_p_2 * comprimento_a, 
                                   delta_p_1 * comprimento_a**2 - delta_w[i] * constante_E * ncd * area_p * 10**(-1))
                
                if raizes[0] > raizes[1]:
                    comprimento_w_linha = raizes[0]

                else:
                    comprimento_w_linha = raizes[1]

                if comprimento_w_linha < (comprimento_meio_l - comprimento_a):

                    hipotese = ['HIPOTESE 2',
                                (p_a - delta_p_2 * comprimento_w_linha),
                                (p_a - 2 * delta_p_2 * comprimento_w_linha),
                                (2 * (delta_p_2 * comprimento_w_linha + delta_p_1 * comprimento_a)),
                                (p_i - 2 * (delta_p_2 * comprimento_w_linha + delta_p_1 * comprimento_a))]

                    hipoteses.append(hipotese)

                    break

            elif (j + 1) == 3:

                hipotese = ['HIPOTESE 3',
                            ((1 / comprimento_meio_l) * (delta_w[i] * constante_E * ncd * area_p * 10**(-1) - (delta_p_1 * comprimento_a**2 + 2 * comprimento_a * delta_p_2 * (comprimento_meio_l - comprimento_a) + delta_p_2 * (comprimento_meio_l - comprimento_a)**2))),
                            (p_meio_l - ((1 / comprimento_meio_l) * (delta_w[i] * constante_E * ncd * area_p * 10**(-1) - (delta_p_1 * comprimento_a**2 + 2 * comprimento_a * delta_p_2 * (comprimento_meio_l - comprimento_a) + delta_p_2 * (comprimento_meio_l - comprimento_a)**2)))),
                            (p_a - (((1 / comprimento_meio_l) * (delta_w[i] * constante_E * ncd * area_p * 10**(-1) - (delta_p_1 * comprimento_a**2 + 2 * comprimento_a * delta_p_2 * (comprimento_meio_l - comprimento_a) + delta_p_2 * (comprimento_meio_l - comprimento_a)**2))) + 2 * delta_p_2 * (comprimento_meio_l - comprimento_a))),
                            (p_i - (((1 / comprimento_meio_l) * (delta_w[i] * constante_E * ncd * area_p * 10**(-1) - (delta_p_1 * comprimento_a**2 + 2 * comprimento_a * delta_p_2 * (comprimento_meio_l - comprimento_a) + delta_p_2 * (comprimento_meio_l - comprimento_a)**2))) + 2 * delta_p_1 * comprimento_a + 2 * delta_p_2 * (comprimento_meio_l - comprimento_a)))]

                hipoteses.append(hipotese)

    return hipoteses
