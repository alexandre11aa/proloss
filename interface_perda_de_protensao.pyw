print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

import tkinter as tk

import os
import sys
import base64

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from perdas_imediatas.atrito import atrito
from perdas_imediatas.acomodacao_da_ancoragem import acomodacao_da_ancoragem
from perdas_imediatas.encurtamento_imediato_do_concreto import encurtamento_imediato_do_concreto

from itens_auxiliares.tabelas_informativas import tabelas_informativas
from itens_auxiliares.calculos_auxiliares import calculo_da_espessura_ficticia
from itens_auxiliares.calculos_auxiliares import calculo_da_idade_ficticia
from itens_auxiliares.calculos_auxiliares import efeito_conjunto_retracao_e_fluencia

from perdas_progressivas.retracao_do_concreto import retracao_do_concreto
from perdas_progressivas.fluencia_do_concreto import fluencia_do_concreto
from perdas_progressivas.fluencia_do_concreto import superposicao_de_efeitos
from perdas_progressivas.relaxacao import relaxacao_pura
from perdas_progressivas.relaxacao import relaxacao_relativa
from perdas_progressivas.processos_de_calculo import perda_progressiva_processo_simplificado
from perdas_progressivas.processos_de_calculo import perda_progressiva_metodo_geral


root = Tk()

class funcoes():

    # Ícone
    def conversao_de_icone(self, janela):
        
        icone = base64.b64decode(tabelas_informativas('icone'))

        with open("icone_temporario.ico", "wb") as ico:
            ico.write(icone)

        janela.iconbitmap('icone_temporario.ico')

        os.remove("icone_temporario.ico")
            
    # Resultados
    def perda_por_atrito(self):

        self.x_1 = []
        self.y_1 = []

        self.x_2 = []
        self.y_2 = []

        if len(self.quadro_1_itens) == (len(self.quadro_2_itens) + 1):

            dist, situ, altu = [[], [], []]
        
            for i in range(len(self.quadro_1_itens)):
                altu.append(self.quadro_1_itens[i][1])

            soma = 0

            self.x_1.append(soma)

            for i in range(len(self.quadro_2_itens)):
                soma += self.quadro_2_itens[i][0]

                self.x_1.append(soma)

                dist.append(self.quadro_2_itens[i][0])
                situ.append(self.quadro_2_itens[i][1])

            resultados = atrito(self.variaveis_1[:4],
                                dist,
                                situ,
                                altu,
                                self.variaveis_1[4],
                                self.variaveis_1[5])
            
            self.quadro_3_itens = resultados[0]
            
            self.resultado_delta_l = resultados[1]
            
            self.y_1, self.x_2, self.y_2  = [altu, self.x_1, self.quadro_3_itens]

        self.destruicao_1()

    def perda_por_acomodacao_de_ancoragem(self):

        self.resultados_de_ac_de_anc = acomodacao_da_ancoragem(self.quadro_4_itens,
                                                               self.variaveis_2[0],
                                                               self.variaveis_2[1],
                                                               self.variaveis_2[3],
                                                               self.variaveis_2[4],
                                                               self.variaveis_2[5],
                                                               self.variaveis_2[2],
                                                               self.variaveis_2[6],
                                                               self.variaveis_2[7])
                
        self.aplicar_1()

    def perda_por_cura_do_concreto(self):
        
        self.resultados_2 = encurtamento_imediato_do_concreto(self.variaveis_3[1],
                                                              self.variaveis_3[6],
                                                              self.variaveis_3[4],
                                                              self.variaveis_3[3],
                                                              self.variaveis_3[2],
                                                              self.variaveis_3[8],
                                                              self.variaveis_3[7],
                                                              self.variaveis_3[5],
                                                              self.variaveis_3[0],
                                                              self.quadro_5_itens[1],
                                                              self.quadro_5_itens[2],
                                                              self.quadro_5_itens[3])
        
        self.destruicao_3()   

    def perda_por_retracao_do_concreto(self):

        self.quadro_7_itens = retracao_do_concreto(self.quadro_6_itens[0], 
                                                   self.quadro_6_itens[1], 
                                                   self.quadro_6_itens[2], 
                                                   self.quadro_6_itens[3], 
                                                   self.quadro_6_itens[4])
            
        self.destruicao_4()

    def perda_por_fluencia_do_concreto(self, calculo):

        if calculo == 0:

            self.quadro_9_itens = fluencia_do_concreto(self.quadro_8_itens[0],
                                                       self.quadro_8_itens[1], 
                                                       self.quadro_8_itens[2], 
                                                       self.quadro_8_itens[3], 
                                                       self.quadro_8_itens[4],
                                                       self.quadro_8_itens[5],
                                                       self.quadro_8_itens[6])

        elif calculo == 1:
            
            self.resultado_ecc, self.quadro_11_itens = superposicao_de_efeitos(self.quadro_9_itens,
                                                                               self.quadro_10_itens,
                                                                               self.fck_ecc)

        self.destruicao_5()

    def perda_por_relaxacao(self, calculo):

        if calculo == 0:
        
            (self.valores_variaveis_ppra[12], 
             self.valores_variaveis_ppra[13], 
             self.valores_variaveis_ppra[16]) = relaxacao_pura(self.valores_variaveis_ppra[0],
                                                               self.valores_variaveis_ppra[1],
                                                               self.valores_variaveis_ppra[2],
                                                               self.valores_variaveis_ppra[3],
                                                               self.valores_variaveis_ppra[4],
                                                               self.valores_variaveis_ppra[5],
                                                               self.valores_variaveis_ppra[6],
                                                               self.valores_variaveis_ppra[7],
                                                               self.valores_variaveis_ppra[8],
                                                               self.valores_variaveis_ppra[9],
                                                               self.valores_variaveis_ppra[10],
                                                               self.valores_variaveis_ppra[11])
            
        elif calculo == 1:

            self.valores_variaveis_ppra[15] = relaxacao_relativa(self.valores_variaveis_ppra[13],
                                                                 self.valores_variaveis_ppra[14],
                                                                 self.valores_variaveis_ppra[16])
            
        self.destruicao_6()

    def perda_processo_simplificado(self):
        
        self.valores_de_ps[14] = perda_progressiva_processo_simplificado(self.valores_de_ps[0] , self.valores_de_ps[1] , self.valores_de_ps[2],
                                                                         self.valores_de_ps[3] , self.valores_de_ps[4] , self.valores_de_ps[5],
                                                                         self.valores_de_ps[6] , self.valores_de_ps[7] , self.valores_de_ps[8],
                                                                         self.valores_de_ps[9] , self.valores_de_ps[10], self.valores_de_ps[11],
                                                                         self.valores_de_ps[12], self.valores_de_ps[13])
        
        self.destruicao_7()

    def perda_metodo_geral(self):
        
        self.valores_de_mg[0] = perda_progressiva_metodo_geral(self.valores_de_mg[1],
                                                               self.valores_de_mg[2])
        
        self.destruicao_7()

    # Aplicações
    def aplicar_1(self):

        self.indice_da_lista_de_delta_w_para_exibir = self.lista_de_delta_w_para_exibir.current()

        if self.lista_de_delta_w_para_exibir.get() != '':

            if self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][0] == 'HIPOTESE 1':

                self.resultados_1[0] = self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][0]
                self.resultados_1[1] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][1]
                self.resultados_1[2] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][3]
                self.resultados_1[3] = '-'
                self.resultados_1[4] = '-'
                self.resultados_1[5] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][2]
                self.resultados_1[6] = '-'

            elif self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][0] == 'HIPOTESE 2':
            
                self.resultados_1[0] = self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][0]
                self.resultados_1[1] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][1]
                self.resultados_1[2] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][4]
                self.resultados_1[3] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][2]
                self.resultados_1[4] = '-'
                self.resultados_1[5] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][3]
                self.resultados_1[6] = '-'

            elif self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][0] == 'HIPOTESE 3':
            
                self.resultados_1[0] = self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][0]
                self.resultados_1[1] = '-'
                self.resultados_1[2] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][4]
                self.resultados_1[3] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][3]
                self.resultados_1[4] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][2]
                self.resultados_1[5] = '-'
                self.resultados_1[6] = '%.4f' % self.resultados_de_ac_de_anc[self.lista_de_delta_w_para_exibir.current()][1]
        
        self.destruicao_2()

    def aplicar_2(self):

        self.indice_da_lista_de_p_individual_para_exibir = self.lista_de_resultados.current()
        
        if self.lista_de_resultados.current() != 0 and len(self.resultados_2[3]) != 0:
            self.p_individual = '%.4f' % self.resultados_2[3][(self.lista_de_resultados.current() - 1)]

        self.destruicao_3()

    # Destruições
    def destruicao_1(self):

        self.quadro_1.destroy()
        self.y_scroll_1.destroy()
        self.quadro_2.destroy()
        self.y_scroll_2.destroy()
        self.quadro_3.destroy()
        self.y_scroll_3.destroy()
        self.fptk.destroy()
        self.fpyk.destroy()
        self.ncd.destroy()
        self.area.destroy()
        self.constante_u.destroy()
        self.canvas.get_tk_widget().destroy()

        self.aba_1_funcoes_destrutivas()

    def destruicao_2(self):

        self.quadro_4.destroy()
        self.y_scroll_4.destroy()
        self.comprimento_a.destroy()
        self.comprimento_meio_l.destroy()
        self.variavel_constante_E.destroy()
        self.variavel_p_i.destroy()
        self.variavel_p_a.destroy()
        self.variavel_p_meio_l.destroy()
        self.area_p.destroy()
        self.tipo_de_hipotese.destroy()
        self.variavel_p_w.destroy()
        self.p_linha_0.destroy()
        self.p_linha_a.destroy()
        self.p_linha_l_2.destroy()
        self.delta_0.destroy()
        self.delta_l_2.destroy()

        self.aba_2_funcoes_destrutivas()

    def destruicao_3(self):
        
        self.quadro_5.destroy()
        self.y_scroll_5.destroy()
        self.lista_de_links_2.destroy()
        self.variavel_ppec_n.destroy()
        self.variavel_ppec_ac.destroy()
        self.variavel_ppec_ap.destroy()
        self.variavel_ppec_ep.destroy()
        self.variavel_ppec_ic.destroy()
        self.variavel_ppec_mg.destroy()
        self.variavel_ppec_ycin.destroy()
        self.variavel_ppec_fck.destroy()
        self.variavel_ppec_ncord.destroy()
        self.variavel_ppec_ocp.destroy()
        self.variavel_ppec_ocg.destroy()
        self.variavel_ppec_dop.destroy()
        self.variavel_ppec_p_individuais.destroy()
        self.lista_de_resultados.destroy()

        self.aba_3_funcoes_destrutivas()

    def destruicao_4(self):

        self.quadro_6.destroy()
        self.y_scroll_6.destroy()
        self.lista_de_links_3.destroy()
        self.quadro_7.destroy()
        self.y_scroll_7.destroy()

        self.aba_4_funcoes_destrutivas()

    def destruicao_5(self):

        self.quadro_8.destroy()
        self.y_scroll_8.destroy()
        self.lista_de_links_4.destroy()
        self.quadro_9.destroy()
        self.y_scroll_9.destroy()
        self.quadro_10.destroy()
        self.y_scroll_10.destroy()
        self.quadro_11.destroy()
        self.y_scroll_11.destroy()

        self.aba_5_funcoes_destrutivas()

    def destruicao_6(self):
        
        self.variavel_n_ppra.destroy()
        self.variavel_ap_ppra.destroy()
        self.variavel_p0_ppra.destroy()
        self.variavel_Mg_ppra.destroy()
        self.variavel_ep_ppra.destroy()
        self.variavel_Ep_ppra.destroy()
        self.variavel_Ic_ppra.destroy()
        self.variavel_Eci28_ppra.destroy()
        self.variavel_fptk_ppra.destroy()
        self.variavel_t0_ppra.destroy()
        self.variavel_t_ppra.destroy()
        self.variavel_relaxacao_ppra.destroy()
        self.variavel_w_ppra.destroy()
        self.variavel_delta_o_pr_ppra.destroy()
        self.variavel_delta_o_p_cs_ppra.destroy()
        self.variavel_delta_o_pr_rel_ppra.destroy()

        self.aba_6_funcoes_destrutivas()

    def destruicao_7(self):
        
        self.variavel_delta_csr.destroy()
        self.delta_cs.destroy()
        self.delta_rrel.destroy()
        self.variavel_Ac_ps.destroy()
        self.variavel_Ap_ps.destroy()
        self.variavel_ecs_ps.destroy()
        self.variavel_ep_ps.destroy()
        self.variavel_Ep_ps.destroy()
        self.variavel_fck_ps.destroy()
        self.variavel_Ic_ps.destroy()
        self.variavel_Mg_ps.destroy()
        self.variavel_y_ps.destroy()
        self.variavel_w1000_ps.destroy()
        self.variavel_P0_ps.destroy()
        self.variavel_t_ps.destroy()
        self.variavel_t0_ps.destroy()
        self.variavel_delta_op_ps.destroy()
        self.variavel_ocpog_ps.destroy()

        self.aba_7_funcoes_destrutivas()

    # Exemplos
    def exemplos(self, ex):

        if ex == '1.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 138-142.
            
            self.quadro_1_itens = [('A', 1.245), ('B', 1.07), ('C', 0.175), ('D', 0.175), ('E', 1.07), ('F', 1.245)]
            self.quadro_2_itens = [(0.8, 'Reto'), (8.43, 'Curvo'), (2.04, 'Reto'), (8.43, 'Curvo'), (0.8, 'Reto')]

            self.variaveis_1 = [12, 1.014, 1900, 1710, 0.2, 200]

            self.destruicao_1()

        elif ex == '1.1':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 142-144.

            self.quadro_1_itens = [('A', 0.11), ('B', 0.07), ('C', 0.16), ('D', 0.18), ('E', 0.15), ('F', 0.04), ('G', 0.11)]
            self.quadro_2_itens = [(2.8, 'Curvo'), (3.5, 'Curvo'), (0.7, 'Curvo'), (0.9, 'Curvo'), (4.5, 'Curvo'), (3.6, 'Curvo')]

            self.variaveis_1 = [3, 1.4, 2100, 1890, 0.05, 200]

            self.destruicao_1()

        elif ex == '2.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 151-154.

            self.quadro_4_itens = [3.5, 2]

            self.variaveis_2 = [5.5, 9.5, 200, 1177.68, 1093.37, 1084.66, 1.4, 6]

            self.destruicao_2()

        elif ex == '3.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 156-158.

            self.quadro_5_itens = [['C1.1', 'C2.1', 'C3.1', 'C4.1', 'C5.1', 'C1.2', 'C2.2', 'C3.2', 'C4.2', 'C5.2'],
                                [ 14, 28, 14, 28, 14, 14, 28, 14, 28, 14],
                                [-924, -945, -934, -892, -913, -924, -945, -934, -892, -913],
                                [8, 8, 8, 20, 20, 8, 8, 8, 20, 20]]
            
            self.variaveis_3 = [5, 2.678, 1.014, 200, 2, 5000, 1.454, 30, 7]

            self.destruicao_3()

        elif ex == '4.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 166-168.

            self.quadro_6_itens = [[80, 70], [18, 18], ['∞', '∞'], [51.9, 33.9], ['5 - 9', '10 - 15']]

            self.destruicao_4()

        elif ex == '5.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 175-177.

            self.quadro_8_itens = [[75, 75], [30, 30], [38, 160], ['∞', '∞'], [17.9, 17.9], ['10 - 15', '10 - 15'], ['II', 'II']]

            self.quadro_10_itens = [-19.134 + 7.281, 986]

            self.fck_ecc = 30

            self.destruicao_5()

        elif ex == '5.1':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 178-181.

            self.quadro_8_itens = [[70, 70, 70], [28, 28, 28], [18, 35, 76], ['∞', '∞', '∞'], [40, 40, 40], ['5 - 9', '5 - 9', '5 - 9'], ['III', 'III', 'III']]

            self.quadro_10_itens = [-22240.04 + 3794.65, -2471.11, 7083.08]

            self.fck_ecc = 40

            self.destruicao_5()

        elif ex == '6.0':
            
            self.valores_variaveis_ppra = [22, 1.014, 130, 0, 0, 0, 1, 1, 1900, 0, '∞', 'Cord. RB', '', '', -217063, '', '']

            self.destruicao_6()

        elif ex == '7.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 162.

            self.valores_de_U = [40, 60, 80]

            self.valor_de_Ac = 0.86

            self.valor_de_u_ar = 8.2

        elif ex == '8.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 163.

            self.valores_de_Ti = [30, 26, 20]

            self.valores_de_delta_t = [7, 12, 9]

            self.valores_de_alpha = [2, 1, 3]

        elif ex == '9.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 184-189.

            self.valores_de_ecrf = [3, [200, 200, 200], [-18, -18, -18], [-117.637, -122.657, -112.312], [32, 32, 32], [-29143.6, -30698.2, -27492.8], [1242603.5, 1282051, 1203156], [1.95, 1.95, 1.95], []]

        elif ex == '0.0':

            # CHOLFE, L.; BONILHA, L. Concreto Protendido: teoria e prática. São Paulo: Pini, 2013. Páginas 197-202.

            self.valores_de_mg = ['', -118946.8, -89032.2]

            self.valores_de_ps = [0.726, (3 * 12) * 1.4, -0.00017, (0.855 - 0.12), 200, 30, 0.176, 5000, 2.25, 0.03, (3 * 12) * 180, '∞', 16, 'Compressão', '']

            self.destruicao_7()

    # Inserções
    def insercao_1(self):
        self.quadro_1_itens.append((self.ponto.get(), float(self.altura.get())))

        self.destruicao_1()

    def insercao_2(self):
        self.quadro_2_itens.append((float(self.trecho.get()), self.lista_de_tipo.get()))

        self.destruicao_1()

    def insercao_3(self):
        if str(self.lista_de_links.get()) != "":
            lista_excel = np.asarray(pd.read_excel(self.lista_de_links.get(), index_col=None, header=None))

            for i in range(len(lista_excel)):
                self.quadro_1_itens.append((lista_excel[i][0], float(lista_excel[i][1])))

            for i in range(len(lista_excel) - 1):
                self.quadro_2_itens.append((float(lista_excel[i][2]), lista_excel[i][3]))

        self.destruicao_1()

    def insercao_4(self):
        decisao = self.lista_variaveis_1.get()

        if decisao == 'Eₚ':
            self.variaveis_1[5] = float(self.entrada_das_variaveis_1.get())

        elif decisao == 'μ':
            self.variaveis_1[4] = float(self.entrada_das_variaveis_1.get())
        
        elif decisao == 'fptk':
            self.variaveis_1[2] = float(self.entrada_das_variaveis_1.get())

        elif decisao == 'fpyk':
            self.variaveis_1[3] = float(self.entrada_das_variaveis_1.get())

        elif decisao == 'Aₚ⁽⁰⁾':
            self.variaveis_1[1] = float(self.entrada_das_variaveis_1.get())

        elif decisao == 'Nº de Cordoalhas':
            self.variaveis_1[0] = float(self.entrada_das_variaveis_1.get())

        elif decisao == 'Planilha em Excel':
            self.insercao_3()

        self.destruicao_1()

    def insercao_5(self):
        self.quadro_4_itens.append((float(self.valor_de_delta_w.get())))

        self.quadro_4_itens.sort(reverse=True)

        self.destruicao_2()

    def insercao_6(self):
        decisao = self.lista_de_variaveis_2.get()

        if decisao == 'a':
            self.variaveis_2[0] = float(self.entrada_das_variaveis_2.get())
        
        elif decisao == 'l/2':
            self.variaveis_2[1] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Eₚ':
            self.variaveis_2[2] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Pᵢ':
            self.variaveis_2[3] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'P₀(x = a)':
            self.variaveis_2[4] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'P₀(x = l/2)':
            self.variaveis_2[5] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Aₚ⁽⁰⁾':
            self.variaveis_2[6] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Nº de Cordoalhas':
            self.variaveis_2[7] = float(self.entrada_das_variaveis_2.get())

        self.destruicao_2()

    def insercao_7(self):

        if (self.cabos_ppec.get() != '') and (self.dias_ppec.get() != '') and (self.forca_ppec.get() != '') and (self.altura_ppec.get() != ''):

            inserir_1 = float(self.dias_ppec.get())
            inserir_2 = float(self.forca_ppec.get())
            inserir_3 = float(self.altura_ppec.get())

            self.quadro_5_itens[0].append(self.cabos_ppec.get())
            self.quadro_5_itens[1].append(inserir_1)
            self.quadro_5_itens[2].append(inserir_2)
            self.quadro_5_itens[3].append(inserir_3)

        if str(self.lista_de_links_2.get()) != "":
            lista_excel = np.asarray(pd.read_excel(str(self.lista_de_links_2.get()), index_col=None, header=None))

            for i in range(len(lista_excel)):

                inserir_1_e = float(lista_excel[i][1])
                inserir_2_e = float(lista_excel[i][2])
                inserir_3_e = float(lista_excel[i][3])

                self.quadro_5_itens[0].append(lista_excel[i][0])
                self.quadro_5_itens[1].append(inserir_1_e)
                self.quadro_5_itens[2].append(inserir_2_e)
                self.quadro_5_itens[3].append(inserir_3_e)

        self.destruicao_3()

    def insercao_8(self):

        if self.lista_de_variaveis_4.get() == 'n':
            self.variaveis_3[0] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'Ac':
            self.variaveis_3[1] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'Aₚ⁽⁰⁾':
            self.variaveis_3[2] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'Eₚ':
            self.variaveis_3[3] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'Ic':
            self.variaveis_3[4] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'Mg':
            self.variaveis_3[5] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'ycin':
            self.variaveis_3[6] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'fck₂₈':
            self.variaveis_3[7] = float(self.entrada_das_variaveis_5.get())

        elif self.lista_de_variaveis_4.get() == 'Nº de Cordoalhas':
            self.variaveis_3[8] = float(self.entrada_das_variaveis_5.get())

        self.destruicao_3()

    def insercao_9(self):

        if (self.variavel_U_tabela.get()  != '' and 
            self.variavel_t0_tabela.get() != '' and 
            self.variavel_h_tabela.get()  != ''):

            inserir_0 = float(self.variavel_U_tabela.get())
            inserir_1 = float(self.variavel_t0_tabela.get())
            inserir_3 = float(self.variavel_h_tabela.get())

            if self.variavel_t_tabela_lista.get() == '= ∞':

                self.quadro_6_itens[0].append(inserir_0)
                self.quadro_6_itens[1].append(inserir_1)
                self.quadro_6_itens[2].append('∞')
                self.quadro_6_itens[3].append(inserir_3)
                self.quadro_6_itens[4].append(self.variavel_abatimento_tabela_lista.get())

            elif self.variavel_t_tabela_lista.get() == '≠ ∞' and self.variavel_t_tabela.get() != '':

                inserir_2 = float(self.variavel_t_tabela.get())

                self.quadro_6_itens[0].append(inserir_0)
                self.quadro_6_itens[1].append(inserir_1)
                self.quadro_6_itens[2].append(inserir_2)
                self.quadro_6_itens[3].append(inserir_3)
                self.quadro_6_itens[4].append(self.variavel_abatimento_tabela_lista.get())

        if self.lista_de_links_3.get() != '':

            lista_excel = np.asarray(pd.read_excel(self.lista_de_links_3.get(), index_col=None, header=None))

            for i in range(len(lista_excel)):

                inserir_0_e = float(lista_excel[i][0])
                inserir_1_e = float(lista_excel[i][1])

                if lista_excel[i][2] != '∞':
                    inserir_2_e = float(lista_excel[i][2])
                
                else:
                    inserir_2_e = '∞'

                inserir_3_e = float(lista_excel[i][3])

                self.quadro_6_itens[0].append(inserir_0_e)
                self.quadro_6_itens[1].append(inserir_1_e)
                self.quadro_6_itens[2].append(inserir_2_e)
                self.quadro_6_itens[3].append(inserir_3_e)
                self.quadro_6_itens[4].append(lista_excel[i][4])

        self.destruicao_4()

    def insercao_10(self):
        

        if (self.variavel_U_tabela_2.get()  != '' and 
            self.variavel_t0_tabela_2.get() != '' and 
            self.variavel_h_tabela_2.get()  != ''):

            inserir_0 = float(self.variavel_U_tabela_2.get())
            inserir_1 = float(self.variavel_Ti_tabela_2.get())
            inserir_2 = float(self.variavel_t0_tabela_2.get())
            inserir_4 = float(self.variavel_h_tabela_2.get())

            if self.variavel_t_tabela_lista_2.get() == '= ∞':

                self.quadro_8_itens[0].append(inserir_0)
                self.quadro_8_itens[1].append(inserir_1)
                self.quadro_8_itens[2].append(inserir_2)
                self.quadro_8_itens[3].append('∞')
                self.quadro_8_itens[4].append(inserir_4)
                self.quadro_8_itens[5].append(self.variavel_abatimento_tabela_lista_2.get())
                self.quadro_8_itens[6].append(self.variavel_CP_tabela_lista_2.get())

            elif self.variavel_t_tabela_lista_2.get() == '≠ ∞' and self.variavel_t_tabela_2.get() != '':

                inserir_3 = float(self.variavel_t_tabela_2.get())

                self.quadro_8_itens[0].append(inserir_0)
                self.quadro_8_itens[1].append(inserir_1)
                self.quadro_8_itens[2].append(inserir_2)
                self.quadro_8_itens[3].append(inserir_3)
                self.quadro_8_itens[4].append(inserir_4)
                self.quadro_8_itens[5].append(self.variavel_abatimento_tabela_lista_2.get())
                self.quadro_8_itens[6].append(self.variavel_CP_tabela_lista_2.get())

        if self.lista_de_links_4.get() != '':

            lista_excel = np.asarray(pd.read_excel(self.lista_de_links_4.get(), index_col=None, header=None))

            for i in range(len(lista_excel)):

                inserir_0_e = float(lista_excel[i][0])
                inserir_1_e = float(lista_excel[i][1])
                inserir_2_e = float(lista_excel[i][2])

                if lista_excel[i][3] != '∞':
                    inserir_3_e = float(lista_excel[i][3])
                
                else:
                    inserir_3_e = '∞'

                inserir_4_e = float(lista_excel[i][4])

                self.quadro_8_itens[0].append(inserir_0_e)
                self.quadro_8_itens[1].append(inserir_1_e)
                self.quadro_8_itens[2].append(inserir_2_e)
                self.quadro_8_itens[3].append(inserir_3_e)
                self.quadro_8_itens[4].append(inserir_4_e)
                self.quadro_8_itens[5].append(lista_excel[i][5])
                self.quadro_8_itens[6].append(lista_excel[i][6])

        self.destruicao_5()

    def insercao_11(self, tipo):

        if self.variavel_Bst0_tabela.get() != '' and tipo == 0:

            self.quadro_10_itens.append(float(self.variavel_Bst0_tabela.get()))

        if self.inserir_fck_ppfc.get() != '' and tipo == 1:
            
            self.fck_ecc = float(self.inserir_fck_ppfc.get())

        self.destruicao_5()

    def insercao_12(self, tipo):

        if tipo == 0 and self.lista_ppra_1.get() != '':

            if self.lista_ppra_1.get() == 'Cordoalhas RN':
                self.valores_variaveis_ppra[11] = 'Cord. RN'
            
            elif self.lista_ppra_1.get() == 'Cordoalhas RB':
                self.valores_variaveis_ppra[11] = 'Cord. RB'
            
            elif self.lista_ppra_1.get() == 'Fios RN':
                self.valores_variaveis_ppra[11] = 'Fios RN'
            
            elif self.lista_ppra_1.get() == 'Fios RB':
                self.valores_variaveis_ppra[11] = 'Fios RB'
            
            elif self.lista_ppra_1.get() == 'Barras':
                self.valores_variaveis_ppra[11] = 'Barras'

        elif tipo == 1 and self.lista_ppra_2.get() != '':

            if self.lista_ppra_2.get() == 'Nº de Cordoalhas':
                self.valores_variaveis_ppra[0] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'Aₚ⁽⁰⁾':
                self.valores_variaveis_ppra[1] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'P₀':
                self.valores_variaveis_ppra[2] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'Mg':
                self.valores_variaveis_ppra[3] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'eₚ':
                self.valores_variaveis_ppra[4] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'Eₚ':
                self.valores_variaveis_ppra[5] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'Ic':
                self.valores_variaveis_ppra[6] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'Eci₂₈':
                self.valores_variaveis_ppra[7] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 'fptk':
                self.valores_variaveis_ppra[8] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 't₀':
                self.valores_variaveis_ppra[9] = float(self.variaveis_ppra.get())

            elif self.lista_ppra_2.get() == 't = ∞':
                self.valores_variaveis_ppra[10] = '∞'

            elif self.lista_ppra_2.get() == 't ≠ ∞':
                self.valores_variaveis_ppra[10] = float(self.variaveis_ppra.get())

        elif tipo == 2 and self.variavel_delta_o_p_cs_ppra_entrada.get() != '':
            self.valores_variaveis_ppra[14] = float(self.variavel_delta_o_p_cs_ppra_entrada.get())

        self.destruicao_6()

    def insercao_13(self, tipo):

        if tipo == 0 and self.lista_variaveis_mg.get() != '':

            if self.lista_variaveis_mg.get() == 'Δσₚ,c+s':
                self.valores_de_mg[1] = float(self.variavel_mg.get())
            
            elif self.lista_variaveis_mg.get() == 'Δσₚᵣ,rel':
                self.valores_de_mg[2] = float(self.variavel_mg.get())
            
        elif tipo == 1 and self.lista_variaveis_ps.get() != '':

            if self.lista_variaveis_ps.get() == 'Ac':
                self.valores_de_ps[0] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'Aₚ':
                self.valores_de_ps[1] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'εcs':
                self.valores_de_ps[2] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'eₚ':
                self.valores_de_ps[3] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'fck':
                self.valores_de_ps[4] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'Ic':
                self.valores_de_ps[5] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'Mg':
                self.valores_de_ps[6] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'φ':
                self.valores_de_ps[7] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'Ψ₁₀₀₀':
                self.valores_de_ps[8] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'P₀':
                self.valores_de_ps[9] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 't ≠ ∞':
                self.valores_de_ps[10] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 't = ∞':
                self.valores_de_ps[11] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 't₀':
                self.valores_de_ps[12] = float(self.variavel_ps.get())
            elif self.lista_variaveis_ps.get() == 'σc,pog = +':
                self.valores_de_ps[13] = 'Compressão'
            elif self.lista_variaveis_ps.get() == 'σc,pog = -':
                self.valores_de_ps[13] = 'Tração'

        self.destruicao_7()

    # Apagando
    def apagando(self, quadro, quadro_itens, destruir, modelo):
        selecionador = quadro.selection()[0]

        quadro.delete(selecionador)

        if modelo == 1:
            del (quadro_itens[int(selecionador)])

        elif modelo == 2:
            for i in range(len(quadro_itens)):
                del (quadro_itens[i][int(selecionador)])

        destruir()

    # Procurar
    def procurar(self, links, destruir):
        arquivo = askopenfilename(filetypes=[('Arquivos do Excel', '*.xlsx')])

        links.append(arquivo)

        destruir()

    # Menu de Opções
    def menus(self):
        barra_de_menu = Menu(self.root)
        root.config(menu=barra_de_menu)

        menu_de_arquivos = Menu(barra_de_menu)
        barra_de_menu.add_cascade(label='Arquivos', menu = menu_de_arquivos)
        menu_de_arquivos.add_command(label='Limpar', command=self.limpar)
        menu_de_arquivos.add_command(label='Reiniciar', command=self.reiniciar)
        menu_de_arquivos.add_command(label='Sobre', command=lambda: self.tabelas_auxiliares('sobre', '750x505'))
        menu_de_arquivos.add_command(label='Sair', command=self.sair)

        menu_de_exemplos = Menu(barra_de_menu)
        barra_de_menu.add_cascade(label='Exemplos', menu = menu_de_exemplos)
        menu_de_exemplos.add_command(label='E.1.0. PIAT', command=lambda: self.exemplos('1.0'))
        menu_de_exemplos.add_command(label='E.1.1. PIAT', command=lambda: self.exemplos('1.1'))
        menu_de_exemplos.add_command(label='E.2.0. PIAC', command=lambda: self.exemplos('2.0'))
        menu_de_exemplos.add_command(label='E.3.0. PIEC', command=lambda: self.exemplos('3.0'))
        menu_de_exemplos.add_command(label='E.4.0. PPRC', command=lambda: self.exemplos('4.0'))
        menu_de_exemplos.add_command(label='E.5.0. PPFC', command=lambda: self.exemplos('5.0'))
        menu_de_exemplos.add_command(label='E.5.1. PPFC', command=lambda: self.exemplos('5.1'))
        menu_de_exemplos.add_command(label='E.6.0. PPRA', command=lambda: self.exemplos('6.0'))
        menu_de_exemplos.add_command(label='E.C.1. ESFI', command=lambda: self.exemplos('7.0'))
        menu_de_exemplos.add_command(label='E.C.2. IDFI', command=lambda: self.exemplos('8.0'))
        menu_de_exemplos.add_command(label='E.C.3. ECRF', command=lambda: self.exemplos('9.0'))
        menu_de_exemplos.add_command(label='E.0.0. PPPC', command=lambda: self.exemplos('0.0'))

        menu_de_tabelas = Menu(barra_de_menu)
        barra_de_menu.add_cascade(label='Tabelas', menu = menu_de_tabelas)
        menu_de_tabelas.add_command(label='T.1.0. Siglas', command=lambda: self.tabelas_auxiliares('siglas', '430x510'))
        menu_de_tabelas.add_command(label='T.2.0. Variáveis', command=lambda: self.tabelas_auxiliares('variaveis', '535x505'))
        menu_de_tabelas.add_command(label='T.3.0. Fluência e Retração', command=lambda: self.tabelas_auxiliares('numeros_usuais_para_determinacao_da_fluencia_e_retracao', '650x500'))
        menu_de_tabelas.add_command(label='T.4.0. Endurecimento do Cimento', command=lambda: self.tabelas_auxiliares('fluencia_e_retracao_em_funcao_da_vel_de_endurecimento_do_cim', '650x500'))

        menu_de_calculos = Menu(barra_de_menu)
        barra_de_menu.add_cascade(label='Cálculos', menu = menu_de_calculos)
        menu_de_calculos.add_command(label='C.1.0. ESFI', command=self.calculo_espessura_ficticia)
        menu_de_calculos.add_command(label='C.2.0. IDFI', command=self.calculo_idade_ficticia)
        menu_de_calculos.add_command(label='C.3.0. ECRF', command=self.calculo_efeito_conjunto_r_f)

    # Tabelas Informativas
    def tabelas_auxiliares(self, img, geometria):

        # Configurações da Página

        self.janela_de_ajuda = tk.Toplevel()

        self.janela_de_ajuda.geometry(geometria)

        self.janela_de_ajuda.resizable(False, False)

        self.janela_de_ajuda.grab_set()
        
        self.main_frame = Frame(self.janela_de_ajuda)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.conversao_de_icone(self.janela_de_ajuda)

        # Criando um Canvas

        self.my_canvas = Canvas(self.main_frame)

        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if int(list(geometria.split('x'))[1]) > 500:

            # Adicionando ScrollBar ao Canvas

            self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
            self.my_scrollbar.pack(side=RIGHT, fill=Y)

            # Configurando o Canvas

            self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
            self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        # Adicionando Imagem à Janela na Tela

        self.informacoes = tk.PhotoImage(data=tabelas_informativas(img))

        self.my_canvas.create_image(1, 1, image=self.informacoes, anchor=tk.NW)

    # Cálculos Auxiliares
    def calculo_espessura_ficticia(self):

        # Configurações da Página

        self.janela = tk.Toplevel()

        self.janela.geometry("303x350")

        self.janela.resizable(False, False)

        self.janela.grab_set()

        self.conversao_de_icone(self.janela)
       
        self.fundo_ef_0 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ef_0.place(relx=0.0225, rely=0.04, relwidth=0.955, relheight=0.94)

        self.fundo_ef_1 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ef_1.place(relx=0.0545, rely=0.0825, relwidth=0.285, relheight=0.865)

        self.fundo_ef_2 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ef_2.place(relx=0.3595, rely=0.0825, relwidth=0.285, relheight=0.3)

        self.fundo_ef_3 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ef_3.place(relx=0.3595, rely=0.415, relwidth=0.285, relheight=0.5325)
        
        self.fundo_ef_4 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ef_4.place(relx=0.6625, rely=0.0825, relwidth=0.285, relheight=0.865)

        self.texto_ef = Label(self.janela, text='Espessura Fictícia', bg='#F0F0F0', fg='#000000')
        self.texto_ef.place(relx=0.125, rely=0.01, relwidth=0.32, relheight=0.05)

        # Variáveis

        self.quadro_ef_1 = ttk.Treeview(self.janela, columns=('U'))

        self.quadro_ef_1.column('#0', width=0, stretch=NO)
        self.quadro_ef_1.column('U', anchor=CENTER, width=20)

        self.quadro_ef_1.heading('U', text='U', anchor=CENTER)

        self.quadro_ef_1.place(relx=0.075, rely=0.118, relwidth=0.19, relheight=0.808)

        self.y_scroll_ef_1 = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.quadro_ef_1.yview)

        self.quadro_ef_1['yscroll'] = self.y_scroll_ef_1.set

        self.y_scroll_ef_1.place(relx=0.268, rely=0.118, relwidth=0.05, relheight=0.808)

        for i in range(len(self.valores_de_U)):
            self.quadro_ef_1.insert(parent='', index=i, iid=i, text='',
                                    values=('%.4f' % float(self.valores_de_U[i])))
            
        self.variavel_1 = Entry(self.janela, text="")
        self.variavel_1.place(relx=0.41, rely=0.12, relwidth=0.19, relheight=0.064)

        self.botao_inserir_ef_1 = tk.Button(self.janela, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.calculo_espessura_ficticia_funcoes('inserir_1'))
        self.botao_inserir_ef_1.place(relx=0.41, rely=0.2075, relwidth=0.19, relheight=0.065)

        self.botao_apagar_ef = tk.Button(self.janela, text='Apagar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.calculo_espessura_ficticia_funcoes('apagar'))
        self.botao_apagar_ef.place(relx=0.41, rely=0.295, relwidth=0.19, relheight=0.065)

        self.texto_ef = Label(self.janela, text='Ac', bg='#F0F0F0', fg='#000000')
        self.texto_ef.place(relx=0.41, rely=0.42, relwidth=0.05, relheight=0.05)

        self.r1 = Label(self.janela, text=str(self.valor_de_Ac), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.r1.place(relx=0.41, rely=0.48, relwidth=0.19, relheight=0.064)

        self.texto_ef = Label(self.janela, text='μₐᵣ', bg='#F0F0F0', fg='#000000')
        self.texto_ef.place(relx=0.41, rely=0.54, relwidth=0.08, relheight=0.05)

        self.r2 = Label(self.janela, text=str(self.valor_de_u_ar), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.r2.place(relx=0.41, rely=0.6, relwidth=0.19, relheight=0.064)

        self.variavel_2 = Entry(self.janela, text="")
        self.variavel_2.place(relx=0.41, rely=0.6875, relwidth=0.19, relheight=0.064)

        self.lista_variaveis_ef = ttk.Combobox(self.janela, values=['', 
                                                                    'Ac', 
                                                                    'μₐᵣ'])
        self.lista_variaveis_ef.place(relx=0.41, rely=0.775, relwidth=0.19, relheight=0.065)
        self.lista_variaveis_ef.current(0)

        self.botao_inserir_ef_2 = tk.Button(self.janela, text='Inserir', bg='#F0F0F0', fg='#000000',
                                            command=lambda: self.calculo_espessura_ficticia_funcoes('inserir_2'))
        self.botao_inserir_ef_2.place(relx=0.41, rely=0.8625, relwidth=0.19, relheight=0.065)       

        # Resultados
        
        self.botao_calcular_ef = tk.Button(self.janela, text='Calcular', bg='#F0F0F0', fg='#000000',
                                           command=lambda: self.calculo_espessura_ficticia_funcoes('calcular'))
        self.botao_calcular_ef.place(relx=0.71, rely=0.8625, relwidth=0.19, relheight=0.065)

        self.quadro_ef_2 = ttk.Treeview(self.janela, columns=('h_fic'))

        self.quadro_ef_2.column('#0', width=0, stretch=NO)
        self.quadro_ef_2.column('h_fic', anchor=CENTER, width=20)

        self.quadro_ef_2.heading('h_fic', text='h', anchor=CENTER)

        self.quadro_ef_2.place(relx=0.685, rely=0.118, relwidth=0.19, relheight=0.715)

        self.y_scroll_ef_2 = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.quadro_ef_2.yview)

        self.quadro_ef_2['yscroll'] = self.y_scroll_ef_2.set

        self.y_scroll_ef_2.place(relx=0.878, rely=0.118, relwidth=0.05, relheight=0.715)

        for i in range(len(self.valores_de_h_fic)):
            self.quadro_ef_2.insert(parent='', index=i, iid=i, text='',
                                    values=('%.4f' % float(self.valores_de_h_fic[i])))

    def calculo_espessura_ficticia_funcoes(self, funcao):
        
        if funcao == 'inserir_1':
            self.valores_de_U.append(float(self.variavel_1.get()))

        elif funcao == 'apagar':
            selecionador = self.quadro_ef_1.selection()[0]

            self.quadro_ef_1.delete(selecionador)

            del (self.valores_de_U[int(selecionador)])

        elif funcao == 'inserir_2':
            if self.lista_variaveis_ef.get() == 'Ac':
                self.valor_de_Ac = float(self.variavel_2.get())

            elif self.lista_variaveis_ef.get() == 'μₐᵣ':
                self.valor_de_u_ar = float(self.variavel_2.get())

        elif funcao == 'calcular':
            self.valores_de_h_fic = calculo_da_espessura_ficticia(self.valor_de_Ac, 
                                                                  self.valor_de_u_ar, 
                                                                  self.valores_de_U)

        self.janela.destroy()
        self.calculo_espessura_ficticia()

    def calculo_idade_ficticia(self):

        # Configurações da Página

        self.janela = tk.Toplevel()

        self.janela.geometry("375x350")

        self.janela.resizable(False, False)

        self.janela.grab_set()

        self.conversao_de_icone(self.janela)
        
        self.fundo_tf_0 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tf_0.place(relx=0.02, rely=0.04, relwidth=0.955, relheight=0.94)

        self.fundo_tf_1 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tf_1.place(relx=0.0425, rely=0.08, relwidth=0.5175, relheight=0.865)

        self.fundo_tf_2 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tf_2.place(relx=0.575, rely=0.08, relwidth=0.375, relheight=0.35)

        self.fundo_tf_3 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tf_3.place(relx=0.575, rely=0.45, relwidth=0.375, relheight=0.495)

        self.texto_tf = Label(self.janela, text='Idade Fictícia', bg='#F0F0F0', fg='#000000')
        self.texto_tf.place(relx=0.125, rely=0.01, relwidth=0.2, relheight=0.05)

        # Variáveis

        self.quadro_tf = ttk.Treeview(self.janela, columns=('Ti', 'Δt'))

        self.quadro_tf.column('#0', width=0, stretch=NO)
        self.quadro_tf.column('Ti', anchor=CENTER, width=20)
        self.quadro_tf.column('Δt', anchor=CENTER, width=20)

        self.quadro_tf.heading('Ti', text='Ti', anchor=CENTER)
        self.quadro_tf.heading('Δt', text='Δt', anchor=CENTER)

        self.quadro_tf.place(relx=0.062, rely=0.118, relwidth=0.436, relheight=0.808)

        self.y_scroll_tf = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.quadro_tf.yview)

        self.quadro_tf['yscroll'] = self.y_scroll_tf.set

        self.y_scroll_tf.place(relx=0.5, rely=0.118, relwidth=0.05, relheight=0.808)

        if len(self.valores_de_Ti) > len(self.valores_de_delta_t):
            indice_da_tabela_1 = len(self.valores_de_Ti)

            for i in range(len(self.valores_de_Ti) - len(self.valores_de_delta_t)):
                self.valores_de_delta_t.append('')

        elif len(self.valores_de_Ti) < len(self.valores_de_delta_t):
            indice_da_tabela_1 = len(self.valores_de_delta_t)

            for i in range(len(self.valores_de_delta_t) - len(self.valores_de_Ti)):
                self.valores_de_Ti.append('')

        else:
            indice_da_tabela_1 = len(self.valores_de_delta_t)

        for i in range(indice_da_tabela_1):
            self.quadro_tf.insert(parent='', index=i, iid=i, text='',
                                  values=(self.valores_de_Ti[i], self.valores_de_delta_t[i]))

        self.lista_variaveis_if = ttk.Combobox(self.janela, values=['', 
                                                                    'α', 
                                                                    'Ti', 
                                                                    'Δt'])
        self.lista_variaveis_if.place(relx=0.595, rely=0.125, relwidth=0.335, relheight=0.065)
        self.lista_variaveis_if.current(0)

        self.variavel = Entry(self.janela, text="")
        self.variavel.place(relx=0.77, rely=0.225, relwidth=0.157, relheight=0.064)

        self.botao_inserir_if = tk.Button(self.janela, text='Inserir', bg='#F0F0F0', fg='#000000',
                                          command=lambda: self.calculo_idade_ficticia_funcoes('inserir'))
        self.botao_inserir_if.place(relx=0.595, rely=0.325, relwidth=0.157, relheight=0.065)

        self.botao_apagar_if = tk.Button(self.janela, text='Apagar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.calculo_idade_ficticia_funcoes('apagar'))
        self.botao_apagar_if.place(relx=0.77, rely=0.325, relwidth=0.157, relheight=0.065)

        # Resultados

        self.botao_calcular_if = tk.Button(self.janela, text='Calcular', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.calculo_idade_ficticia_funcoes('calcular'))
        self.botao_calcular_if.place(relx=0.595, rely=0.225, relwidth=0.157, relheight=0.065)

        self.quadro_tf_res = ttk.Treeview(self.janela, columns=('α', 't_fic'))

        self.quadro_tf_res.column('#0', width=0, stretch=NO)
        self.quadro_tf_res.column('α', anchor=CENTER, width=10)
        self.quadro_tf_res.column('t_fic', anchor=CENTER, width=30)

        self.quadro_tf_res.heading('α', text='α', anchor=CENTER)
        self.quadro_tf_res.heading('t_fic', text='t_fic', anchor=CENTER)

        self.quadro_tf_res.place(relx=0.595, rely=0.5025, relwidth=0.295, relheight=0.424)

        self.y_scroll_tf_res = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.quadro_tf_res.yview)

        self.quadro_tf_res['yscroll'] = self.y_scroll_tf_res.set

        self.y_scroll_tf_res.place(relx=0.89, rely=0.5025, relwidth=0.05, relheight=0.424)

        if len(self.valores_de_alpha) > len(self.valores_de_i_fic):
            indice_da_tabela_2 = len(self.valores_de_alpha)

            for i in range(len(self.valores_de_alpha) - len(self.valores_de_i_fic)):
                self.valores_de_i_fic.append('')

        elif len(self.valores_de_alpha) < len(self.valores_de_i_fic):
            indice_da_tabela_2 = len(self.valores_de_i_fic)

            for i in range(len(self.valores_de_i_fic) - len(self.valores_de_alpha)):
                self.valores_de_delta_t.append('')

        else:
            indice_da_tabela_2 = len(self.valores_de_alpha)

        for i in range(indice_da_tabela_2):
            self.quadro_tf_res.insert(parent='', index=i, iid=i, text='',
                                      values=(self.valores_de_alpha[i], self.valores_de_i_fic[i]))

    def calculo_idade_ficticia_funcoes(self, funcao):
        
        if funcao == 'inserir':
            if self.lista_variaveis_if.get() == 'α':
                self.valores_de_alpha = list(filter(lambda item: item != '', self.valores_de_alpha))

                self.valores_de_alpha.append(float(self.variavel.get()))
            
            elif self.lista_variaveis_if.get() == 'Ti':
                self.valores_de_Ti = list(filter(lambda item: item != '', self.valores_de_Ti))

                self.valores_de_Ti.append(float(self.variavel.get()))
            
            elif self.lista_variaveis_if.get() == 'Δt':
                self.valores_de_delta_t = list(filter(lambda item: item != '', self.valores_de_delta_t))

                self.valores_de_delta_t.append(float(self.variavel.get()))

        elif funcao == 'apagar':

            # Tabela 1

            if self.quadro_tf.selection() != ():

                del (self.valores_de_Ti[int(self.quadro_tf.selection()[0])])

                del (self.valores_de_delta_t[int(self.quadro_tf.selection()[0])])
                
                self.quadro_tf.delete(self.quadro_tf.selection()[0])

            # Tabela 2

            if self.quadro_tf_res.selection() != ():

                del (self.valores_de_alpha[int(self.quadro_tf_res.selection()[0])])

                del (self.valores_de_i_fic[int(self.quadro_tf_res.selection()[0])])

                self.quadro_tf_res.delete(self.quadro_tf_res.selection()[0])

        elif funcao == 'calcular':

            if (len(self.valores_de_Ti) == len(self.valores_de_delta_t)) and (len(self.valores_de_alpha) != 0):

                self.valores_de_i_fic = calculo_da_idade_ficticia(self.valores_de_alpha, 
                                                                  self.valores_de_Ti, 
                                                                  self.valores_de_delta_t)

        self.janela.destroy()
        self.calculo_idade_ficticia()

    def calculo_efeito_conjunto_r_f(self):

        # Configurações da Página

        self.janela = tk.Toplevel()

        self.janela.geometry("650x350")

        self.janela.resizable(False, False)

        self.janela.grab_set()

        self.conversao_de_icone(self.janela)

        self.fundo_ecrf_0 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ecrf_0.place(relx=0.02, rely=0.04, relwidth=0.955, relheight=0.94)

        self.fundo_ecrf_1 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ecrf_1.place(relx=0.044, rely=0.0825, relwidth=0.71, relheight=0.7)

        self.fundo_ecrf_2 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ecrf_2.place(relx=0.7715, rely=0.0825, relwidth=0.18, relheight=0.7)

        self.fundo_ecrf_3 = Label(self.janela, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ecrf_3.place(relx=0.044, rely=0.7975, relwidth=0.9075, relheight=0.16)

        self.texto_ecrf = Label(self.janela, text='Efeito Conjunto de Retração e Fluência', bg='#F0F0F0', fg='#000000')
        self.texto_ecrf.place(relx=0.125, rely=0.01, relwidth=0.33, relheight=0.05)

        self.texto_ecrf = Label(self.janela, text='Δσₚ,c+s', bg='#F0F0F0', fg='#000000')
        self.texto_ecrf.place(relx=0.825, rely=0.0525, relwidth=0.07, relheight=0.05)

        # Variáveis

        self.quadro_ecrf = ttk.Treeview(self.janela, columns=('Eₚ', 'εcs', 'εcc', 'Eci₂₈', 'αcP₀', 'αP₀', 'φ'))

        self.quadro_ecrf.column('#0', width=0, stretch=NO)
        self.quadro_ecrf.column('Eₚ', anchor=CENTER, width=20)
        self.quadro_ecrf.column('εcs', anchor=CENTER, width=20)
        self.quadro_ecrf.column('εcc', anchor=CENTER, width=20)
        self.quadro_ecrf.column('Eci₂₈', anchor=CENTER, width=20)
        self.quadro_ecrf.column('αcP₀', anchor=CENTER, width=20)
        self.quadro_ecrf.column('αP₀', anchor=CENTER, width=20)
        self.quadro_ecrf.column('φ', anchor=CENTER, width=20)

        self.quadro_ecrf.heading('Eₚ', text='Eₚ', anchor=CENTER)
        self.quadro_ecrf.heading('εcs', text='εcs', anchor=CENTER)
        self.quadro_ecrf.heading('εcc', text='εcc', anchor=CENTER)
        self.quadro_ecrf.heading('Eci₂₈', text='Eci₂₈', anchor=CENTER)
        self.quadro_ecrf.heading('αcP₀', text='αcP₀', anchor=CENTER)
        self.quadro_ecrf.heading('αP₀', text='αP₀', anchor=CENTER)
        self.quadro_ecrf.heading('φ', text='φ', anchor=CENTER)

        self.quadro_ecrf.place(relx=0.063, rely=0.12, relwidth=0.6375, relheight=0.6215)

        self.y_scroll_ecrf = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.quadro_ecrf.yview)

        self.quadro_ecrf['yscroll'] = self.y_scroll_ecrf.set

        self.y_scroll_ecrf.place(relx=0.7, rely=0.12, relwidth=0.03, relheight=0.6215)

        for i in range(1, 8):
            if self.valores_de_ecrf[0] < len(self.valores_de_ecrf[i]):
                self.valores_de_ecrf[0] = len(self.valores_de_ecrf[i])

        for i in range(1, 8):
            if len(self.valores_de_ecrf[i]) < self.valores_de_ecrf[0]:
                for j in range(self.valores_de_ecrf[0] - len(self.valores_de_ecrf[i])):
                    self.valores_de_ecrf[i].append('')

        for i in range(self.valores_de_ecrf[0]):
            self.quadro_ecrf.insert(parent='', index=i, iid=i, text='',
                                    values=(self.valores_de_ecrf[1][i], self.valores_de_ecrf[2][i],
                                            self.valores_de_ecrf[3][i], self.valores_de_ecrf[4][i],
                                            self.valores_de_ecrf[5][i], self.valores_de_ecrf[6][i],
                                            self.valores_de_ecrf[7][i]))

        self.lista_variaveis_ecrf = ttk.Combobox(self.janela, values=['', 'Eₚ', 'εcs', 'εcc', 'Eci₂₈', 'αcP₀', 'αP₀', 'φ'])
        self.lista_variaveis_ecrf.place(relx=0.063, rely=0.84, relwidth=0.165, relheight=0.065)
        self.lista_variaveis_ecrf.current(0)

        self.variavel = Entry(self.janela, text="")
        self.variavel.place(relx=0.25, rely=0.84, relwidth=0.157, relheight=0.064)

        self.botao_inserir_ecrf = tk.Button(self.janela, text='Inserir', bg='#F0F0F0', fg='#000000',
                                          command=lambda: self.calculo_efeito_conjunto_r_f_funcoes('inserir'))
        self.botao_inserir_ecrf.place(relx=0.427, rely=0.84, relwidth=0.157, relheight=0.065)

        self.botao_apagar_ecrf = tk.Button(self.janela, text='Apagar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.calculo_efeito_conjunto_r_f_funcoes('apagar'))
        self.botao_apagar_ecrf.place(relx=0.6, rely=0.84, relwidth=0.157, relheight=0.065)

        # Resultados

        self.botao_calcular_ecrf = tk.Button(self.janela, text='Calcular', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.calculo_efeito_conjunto_r_f_funcoes('calcular'))
        self.botao_calcular_ecrf.place(relx=0.775, rely=0.84, relwidth=0.157, relheight=0.065)

        self.quadro_ecrf_res = ttk.Treeview(self.janela, columns=('Δσₚ,c+s'))

        self.quadro_ecrf_res.column('#0', width=0, stretch=NO)
        self.quadro_ecrf_res.column('Δσₚ,c+s', anchor=CENTER, width=10)

        self.quadro_ecrf_res.heading('Δσₚ,c+s', text='Δσ', anchor=CENTER)

        self.quadro_ecrf_res.place(relx=0.79, rely=0.12, relwidth=0.11, relheight=0.6215)

        self.y_scroll_ecrf_res = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.quadro_ecrf_res.yview)

        self.quadro_ecrf_res['yscroll'] = self.y_scroll_ecrf_res.set

        self.y_scroll_ecrf_res.place(relx=0.9, rely=0.12, relwidth=0.03, relheight=0.6215)

        for i in range(len(self.valores_de_ecrf[8])):
            self.quadro_ecrf_res.insert(parent='', index=i, iid=i, text='',
                                        values=(self.valores_de_ecrf[8][i]))

    def calculo_efeito_conjunto_r_f_funcoes(self, funcao):
        
        if funcao == 'inserir':
            
            matriz = [[valor for valor in sublista if valor != ''] for sublista in self.valores_de_ecrf[1:]]

            self.valores_de_ecrf = [self.valores_de_ecrf[0]]

            for i in range(len(matriz)):
                self.valores_de_ecrf.append(matriz[i])
            
            if self.lista_variaveis_ecrf.get() == 'Eₚ':
                self.valores_de_ecrf[1].append(float(self.variavel.get()))

            elif self.lista_variaveis_ecrf.get() == 'εcs':
                self.valores_de_ecrf[2].append(float(self.variavel.get()))

            elif self.lista_variaveis_ecrf.get() == 'εcc':
                self.valores_de_ecrf[3].append(float(self.variavel.get()))

            elif self.lista_variaveis_ecrf.get() == 'Eci₂₈':
                self.valores_de_ecrf[4].append(float(self.variavel.get()))

            elif self.lista_variaveis_ecrf.get() == 'αcP₀':
                self.valores_de_ecrf[5].append(float(self.variavel.get()))

            elif self.lista_variaveis_ecrf.get() == 'αP₀':
                self.valores_de_ecrf[6].append(float(self.variavel.get()))

            elif self.lista_variaveis_ecrf.get() == 'φ':
                self.valores_de_ecrf[7].append(float(self.variavel.get()))

        elif funcao == 'apagar':

            for i in range(1,8):
            
                del (self.valores_de_ecrf[i][int(self.quadro_ecrf.selection()[0])])

            self.quadro_ecrf.delete(self.quadro_ecrf.selection()[0])

            self.valores_de_ecrf[0] -= 1

        elif funcao == 'calcular':
            
            self.valores_de_ecrf[8] = efeito_conjunto_retracao_e_fluencia(self.valores_de_ecrf[1], self.valores_de_ecrf[2],
                                                                          self.valores_de_ecrf[3], self.valores_de_ecrf[4],
                                                                          self.valores_de_ecrf[5], self.valores_de_ecrf[6],
                                                                          self.valores_de_ecrf[7])

        self.janela.destroy()
        self.calculo_efeito_conjunto_r_f()

    # Opção Limpar
    def limpar(self):
        self.variaveis_iniciais()

        self.destruicao_1()
        self.destruicao_2()
        self.destruicao_3()
        self.destruicao_4()
        self.destruicao_5()
        self.destruicao_6()

    # Opção Reiniciar
    def reiniciar(self):
        self.__init__()

    # Opção Sair
    def sair(self):
        print("\nEm verdade que não convém gloriar-me; mas passarei às visões e revelações do Senhor. 2 Coríntios 12:1\n")
        
        self.root.destroy()
        sys.exit()

    # Variáveis Iniciais
    def variaveis_iniciais(self):

        # Variáveis de Perda por Atrito

        self.quadro_1_itens = []
        self.quadro_2_itens = []

        self.quadro_3_itens = []

        self.resultado_delta_l = ''

        self.x_1 = []
        self.y_1 = []

        self.x_2 = []
        self.y_2 = []

        self.links_1 = []

        self.variaveis_1 = ['','','','','','']

        # Variáveis de Perda por Acomodação de Ancoragem

        self.quadro_4_itens = []

        self.variaveis_2 = ['','','','','','','','']

        self.resultados_1 = ['','','','','','','']

        self.indice_da_lista_de_delta_w_para_exibir = 0

        # Variáveis de Perda por Cura do Concreto

        self.quadro_5_itens = [[], [], [], []]

        self.links_2 = []
        
        self.variaveis_3 = ['','','','','','','','','']

        self.resultados_2 = ['','','',[]]

        self.p_individual = ''

        self.indice_da_lista_de_p_individual_para_exibir = 0

        # Variáveis de Cálculo da Espessura Fictícia

        self.valores_de_U = []

        self.valor_de_Ac = ''

        self.valor_de_u_ar = ''

        self.valores_de_h_fic = []

        # Variáveis de Cálculo da Idade Fictícia

        self.valores_de_Ti = []

        self.valores_de_delta_t = []

        self.valores_de_alpha = []

        self.valores_de_i_fic = []

        # Variáveis de Perda por Retração do Concreto

        self.quadro_6_itens = [[], [], [], [], []]

        self.quadro_7_itens = []

        self.links_3 = []

        # Variáveis de Perda por Fluência do Concreto

        self.quadro_8_itens = [[], [], [], [], [], [], []]

        self.quadro_9_itens = []

        self.quadro_10_itens = []

        self.quadro_11_itens = []

        self.links_4 = []

        self.resultado_ecc = ''

        self.fck_ecc = ''

        # Variáveis de Relaxação Pura e Relativa

        self.valores_variaveis_ppra = ['', '', '', '', 
                                       '', '', '', '', 
                                       '', '', '', '', 
                                       '', '', '', '', '']
        
        # Efeito Conjunto de Retração e Fluência

        self.valores_de_ecrf = [ 0, [], [], 
                                [], [], [], 
                                [], [], []]
        
        # Perda de Tensão pelo Método Geral

        self.valores_de_mg = ['', '', '']

        # Perda de Tensão pelo Processo Simplificado

        self.valores_de_ps = ['', '', '', '', '',
                              '', '', '', '', '',
                              '', '', '', '', '', '']

class programa(funcoes):

    # Inicialização e Variáveis
    def __init__(self):
        self.root = root
        self.variaveis_iniciais()
        self.tela()
        self.frame_tela()
        self.menus()
        self.apps_da_pagina_1()
        root.mainloop()

    # Configurações da Tela
    def tela(self):
        self.root.title("ProLoss")
        self.root.configure(background='#F0F0F0')
        self.root.geometry('750x500')
        self.root.resizable(False, False)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=750, height=500)
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

        self.conversao_de_icone(self.root)

    # Configurações do Frame da Tela
    def frame_tela(self):
        self.frame = Frame(self.root, bd=0.1, bg='#FFFFFF',
                           highlightbackground='#F0F0F0', highlightthickness=2)
        self.frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.98)

    # Aplicativos da Página 1
    def apps_da_pagina_1(self):

        # Configurações de Abas

        self.abas = ttk.Notebook(self.frame)

        # Perda de Protensão Imediato por Atrito
        
        self.aba_1 = Frame(self.abas)
        self.aba_1.configure(background='#F0F0F0')
        self.abas.add(self.aba_1, text=" PIAT ")

        # Perda de Protensão Imediata por Acomodação e Ancoragem

        self.aba_2 = Frame(self.abas)
        self.aba_2.configure(background='#F0F0F0')
        self.abas.add(self.aba_2, text=" PIAC ")

        # Perda de Protensão Imediata por Encurtamento do Concreto

        self.aba_3 = Frame(self.abas)
        self.aba_3.configure(background='#F0F0F0')
        self.abas.add(self.aba_3, text=" PIEC ")

        # Perda de Protensão Progressiva por Retração do Concreto

        self.aba_4 = Frame(self.abas)
        self.aba_4.configure(background='#F0F0F0')
        self.abas.add(self.aba_4, text=" PPRC ")

        # Perda de Protensão Progressiva por Fluência do Concreto

        self.aba_5 = Frame(self.abas)
        self.aba_5.configure(background='#F0F0F0')
        self.abas.add(self.aba_5, text=" PPFC ")

        # Perda de Protensão Progressiva por Relaxação do Aço de Protensão

        self.aba_6 = Frame(self.abas)
        self.aba_6.configure(background='#F0F0F0')
        self.abas.add(self.aba_6, text=" PPRA ")

        # Perda de Protensão Progressiva - Processos de Cálculo

        self.aba_7 = Frame(self.abas)
        self.aba_7.configure(background='#F0F0F0')
        self.abas.add(self.aba_7, text=" PPPC ")

        # Abrindo Abas

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.aba_1_funcoes()
        self.aba_1_funcoes_destrutivas()

        self.aba_2_funcoes()
        self.aba_2_funcoes_destrutivas()

        self.aba_3_funcoes()
        self.aba_3_funcoes_destrutivas()

        self.aba_4_funcoes()
        self.aba_4_funcoes_destrutivas()

        self.aba_5_funcoes()
        self.aba_5_funcoes_destrutivas()

        self.aba_6_funcoes()
        self.aba_6_funcoes_destrutivas()

        self.aba_7_funcoes()
        self.aba_7_funcoes_destrutivas()

    # Widgets Estáticos da Aba 1
    def aba_1_funcoes(self):

        # 1.0 Quadrante:

        self.fundo_do_quadro_1 = Label(self.aba_1, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_1.place(relx=0.005, rely=0.01, relwidth=0.2135, relheight=0.98)

        self.fundo_de_local = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_local.place(relx=0.015, rely=0.04, relwidth=0.1925, relheight=0.58)

        self.local = Label(self.aba_1, text='Perfil do Cabo :', bg='#F0F0F0', fg='#000000')
        self.local.place(relx=0.025, rely=0.02, relwidth=0.11, relheight=0.035)

        self.fundo_de_inserir = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_inserir.place(relx=0.015, rely=0.645, relwidth=0.1925, relheight=0.325)

        self.insercao_de_informacoes = Label(self.aba_1, text='Inserção em Tabela :', bg='#F0F0F0',
                                             fg='#000000')
        self.insercao_de_informacoes.place(relx=0.025, rely=0.63, relwidth=0.165, relheight=0.0335)

        self.titulo_ponto = Label(self.aba_1, text='Ponto :', bg='#F0F0F0', fg='#000000')
        self.titulo_ponto.place(relx=0.03, rely=0.675, relwidth=0.05, relheight=0.0335)

        self.ponto = Entry(self.aba_1, text="")
        self.ponto.place(relx=0.03, rely=0.72, relwidth=0.16, relheight=0.04)

        self.titulo_altura = Label(self.aba_1, text='Altura :', bg='#F0F0F0', fg='#000000')
        self.titulo_altura.place(relx=0.03, rely=0.77, relwidth=0.052, relheight=0.0335)

        self.altura = Entry(self.aba_1, text="")
        self.altura.place(relx=0.03, rely=0.815, relwidth=0.16, relheight=0.04)

        self.botao_inserir_1 = tk.Button(self.aba_1, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=self.insercao_1)
        self.botao_inserir_1.place(relx=0.025, rely=0.89, relwidth=0.08, relheight=0.05)

        self.botao_apagar_1 = tk.Button(self.aba_1, text='Apagar', bg='#F0F0F0', fg='#000000', 
                                        command=lambda: self.apagando(self.quadro_1, self.quadro_1_itens, self.destruicao_1, 1))
        self.botao_apagar_1.place(relx=0.115, rely=0.89, relwidth=0.08, relheight=0.05)

        # 2.0 Quadrante:

        self.fundo_do_quadro_2 = Label(self.aba_1, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_2.place(relx=0.23, rely=0.01, relwidth=0.2135, relheight=0.98)

        self.fundo_de_distancias = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_distancias.place(relx=0.24, rely=0.04, relwidth=0.1925, relheight=0.58)

        self.distancias = Label(self.aba_1, text='Trechos :', bg='#F0F0F0', fg='#000000')
        self.distancias.place(relx=0.25, rely=0.02, relwidth=0.065, relheight=0.035)

        self.fundo_de_inserir = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_inserir.place(relx=0.24, rely=0.645, relwidth=0.1925, relheight=0.325)

        self.insercao_de_informacoes = Label(self.aba_1, text='Inserção em Tabela :', bg='#F0F0F0', fg='#000000')
        self.insercao_de_informacoes.place(relx=0.2525, rely=0.63, relwidth=0.165, relheight=0.0335)

        self.titulo_trecho = Label(self.aba_1, text='Trecho :', bg='#F0F0F0', fg='#000000')
        self.titulo_trecho.place(relx=0.255, rely=0.675, relwidth=0.058, relheight=0.0335)

        self.trecho = Entry(self.aba_1, text="")
        self.trecho.place(relx=0.255, rely=0.72, relwidth=0.16, relheight=0.04)

        self.titulo_tipo = Label(self.aba_1, text='Tipo :', bg='#F0F0F0', fg='#000000')
        self.titulo_tipo.place(relx=0.255, rely=0.77, relwidth=0.04, relheight=0.0335)

        self.lista_de_tipo = ttk.Combobox(self.aba_1, values=['Curvo', 'Reto'])
        self.lista_de_tipo.place(relx=0.255, rely=0.815, relwidth=0.16, relheight=0.045)
        self.lista_de_tipo.current(0)

        self.botao_inserir_2 = tk.Button(self.aba_1, text='Inserir', bg='#F0F0F0', fg='#000000',
                                        command=self.insercao_2)
        self.botao_inserir_2.place(relx=0.25, rely=0.89, relwidth=0.08, relheight=0.05)

        self.botao_apagar_2 = tk.Button(self.aba_1, text='Apagar', bg='#F0F0F0', fg='#000000', 
                                        command=lambda: self.apagando(self.quadro_2, self.quadro_2_itens, self.destruicao_1, 1))
        self.botao_apagar_2.place(relx=0.34, rely=0.89, relwidth=0.08, relheight=0.05)

        # 3.0 Quadrante:

        self.fundo_do_quadro_3 = Label(self.aba_1, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_3.place(relx=0.455, rely=0.01, relwidth=0.137, relheight=0.98)

        self.fundo_de_resultados_1 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_1.place(relx=0.465, rely=0.04, relwidth=0.115, relheight=0.535)

        self.resultados = Label(self.aba_1, text='Força P₀ :', bg='#F0F0F0', fg='#000000')
        self.resultados.place(relx=0.475, rely=0.02, relwidth=0.07, relheight=0.035)

        self.fundo_de_resultados_1_1 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_1_1.place(relx=0.465, rely=0.6025, relwidth=0.115, relheight=0.09)

        self.fundo_de_resultados_2 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_2.place(relx=0.465, rely=0.72, relwidth=0.115, relheight=0.25)

        self.botao_procurar_1 = tk.Button(self.aba_1, text='Procurar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.procurar(self.links_1, self.destruicao_1))
        self.botao_procurar_1.place(relx=0.4825, rely=0.8175, relwidth=0.08, relheight=0.05)

        self.botao_calcular_1 = tk.Button(self.aba_1, text='Calcular', bg='#F0F0F0', fg='#000000', 
                                          command=self.perda_por_atrito)
        self.botao_calcular_1.place(relx=0.4825, rely=0.89, relwidth=0.08, relheight=0.05)
        
        self.delta_l_texto = Label(self.aba_1, text='Δl :', bg='#F0F0F0', fg='#000000')
        self.delta_l_texto.place(relx=0.4725, rely=0.5875, relwidth=0.028, relheight=0.025)

        # 4.0 Quadrante:

        self.fundo_do_quadro_4 = Label(self.aba_1, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_4.place(relx=0.605, rely=0.01, relwidth=0.388, relheight=0.98)

        self.fundo_de_variaveis_1 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_1.place(relx=0.615, rely=0.04, relwidth=0.368, relheight=0.23)

        self.E_mod_elast_texto = Label(self.aba_1, text='Eₚ :', bg='#F0F0F0', fg='#000000')
        self.E_mod_elast_texto.place(relx=0.8225, rely=0.108, relwidth=0.025, relheight=0.05)

        self.fptk_texto = Label(self.aba_1, text='fptk :', bg='#F0F0F0', fg='#000000')
        self.fptk_texto.place(relx=0.8225, rely=0.15, relwidth=0.038, relheight=0.05)

        self.fpyk_texto = Label(self.aba_1, text='fpyk :', bg='#F0F0F0', fg='#000000')
        self.fpyk_texto.place(relx=0.8225, rely=0.203, relwidth=0.038, relheight=0.05)

        self.ncd_texto = Label(self.aba_1, text='Nº Cd. :', bg='#F0F0F0', fg='#000000')
        self.ncd_texto.place(relx=0.63, rely=0.156, relwidth=0.058, relheight=0.05)

        self.area_texto = Label(self.aba_1, text='Aₚ⁽⁰⁾ :', bg='#F0F0F0', fg='#000000')
        self.area_texto.place(relx=0.63, rely=0.203, relwidth=0.048, relheight=0.05)

        self.u_texto = Label(self.aba_1, text='μ :', bg='#F0F0F0', fg='#000000')
        self.u_texto.place(relx=0.63, rely=0.108, relwidth=0.02, relheight=0.05)

        self.entrada_das_variaveis_1 = Entry(self.aba_1, text="")
        self.entrada_das_variaveis_1.place(relx=0.7925, rely=0.058, relwidth=0.076, relheight=0.046)

        self.botao_inserir_4 = tk.Button(self.aba_1, text='Inserir', bg='#F0F0F0', fg='#000000', command=self.insercao_4)
        self.botao_inserir_4.place(relx=0.8875, rely=0.056, relwidth=0.08, relheight=0.05)

        self.lista_variaveis_1 = ttk.Combobox(self.aba_1, values=['', 
                                                                  'μ',
                                                                  'Eₚ',
                                                                  'fptk', 
                                                                  'fpyk', 
                                                                  'Aₚ⁽⁰⁾',
                                                                  'Nº de Cordoalhas',
                                                                  'Planilha em Excel'])
        self.lista_variaveis_1.place(relx=0.63, rely=0.056, relwidth=0.145, relheight=0.05)
        self.lista_variaveis_1.current(0)

        # 5.0 Quadrante:

        self.fundo_de_duracoes = Label(self.aba_1, text='', relief="groove", bg='#FFFFFF', fg='#800000')
        self.fundo_de_duracoes.place(relx=0.615, rely=0.3, relwidth=0.368, relheight=0.67)
        
    # Widgets Dinâmicos da Aba 1
    def aba_1_funcoes_destrutivas(self):

        # 1.0 Quadrante:

        self.quadro_1 = ttk.Treeview(self.aba_1, columns=('Ponto', 'Altura'))

        self.quadro_1.column('#0', width=0, stretch=NO)
        self.quadro_1.column('Ponto', anchor=CENTER, width=20)
        self.quadro_1.column('Altura', anchor=CENTER, width=20)

        self.quadro_1.heading('Ponto', text='Ponto', anchor=CENTER)
        self.quadro_1.heading('Altura', text='Altura', anchor=CENTER)

        self.quadro_1.place(relx=0.025, rely=0.0665, relwidth=0.15, relheight=0.535)

        self.y_scroll_1 = ttk.Scrollbar(self.aba_1, orient=tk.VERTICAL, command=self.quadro_1.yview)

        self.quadro_1['yscroll'] = self.y_scroll_1.set

        self.y_scroll_1.place(relx=0.175, rely=0.0665, relwidth=0.025, relheight=0.535)

        for i in range(len(self.quadro_1_itens)):
            self.quadro_1.insert(parent='', index=i, iid=i, text='',
                                 values=(self.quadro_1_itens[i][0], '%.4f' % float(self.quadro_1_itens[i][1])))

        # 2.0 Quadrante:

        self.quadro_2 = ttk.Treeview(self.aba_1, columns=('Trecho', 'Tipo'))

        self.quadro_2.column('#0', width=0, stretch=NO)
        self.quadro_2.column('Trecho', anchor=CENTER, width=20)
        self.quadro_2.column('Tipo', anchor=CENTER, width=20)

        self.quadro_2.heading('Trecho', text='Trecho', anchor=CENTER)
        self.quadro_2.heading('Tipo', text='Tipo', anchor=CENTER)

        self.quadro_2.place(relx=0.25, rely=0.0665, relwidth=0.15, relheight=0.535)

        self.y_scroll_2 = ttk.Scrollbar(self.aba_1, orient=tk.VERTICAL, command=self.quadro_2.yview)

        self.quadro_2['yscroll'] = self.y_scroll_2.set

        self.y_scroll_2.place(relx=0.40, rely=0.0665, relwidth=0.025, relheight=0.535)

        for i in range(len(self.quadro_2_itens)):
            self.quadro_2.insert(parent='', index=i, iid=i, text='', values=('%.4f' % float(self.quadro_2_itens[i][0]), self.quadro_2_itens[i][1]))

        # 3.0 Quadrante:

        self.quadro_3 = ttk.Treeview(self.aba_1, columns=('Perda'))

        self.quadro_3.column('#0', width=0, stretch=NO)
        self.quadro_3.column('Perda', anchor=CENTER, width=20)

        self.quadro_3.heading('Perda', text='Perda', anchor=CENTER)

        self.quadro_3.place(relx=0.475, rely=0.0665, relwidth=0.075, relheight=0.4925)

        self.y_scroll_3 = ttk.Scrollbar(self.aba_1, orient=tk.VERTICAL, command=self.quadro_3.yview)

        self.quadro_3['yscroll'] = self.y_scroll_3.set

        self.y_scroll_3.place(relx=0.55, rely=0.0665, relwidth=0.025, relheight=0.4925)

        for i in range(len(self.quadro_3_itens)):
            self.quadro_3.insert(parent='', index=i, iid=i, text='', values=(str(self.quadro_3_itens[i])))

        self.delta_l = Label(self.aba_1, text=self.resultado_delta_l, relief="sunken", bg='#FFFFFF', fg='#000000')
        self.delta_l.place(relx=0.4825, rely=0.625, relwidth=0.08, relheight=0.0475) 

        self.lista_de_links = ttk.Combobox(self.aba_1, values=self.links_1)
        self.lista_de_links.place(relx=0.4825, rely=0.7475, relwidth=0.08, relheight=0.045)

        # 4.0 Quadrante:

        self.constante_u = Label(self.aba_1, text=str(self.variaveis_1[4]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.constante_u.place(relx=0.695, rely=0.115, relwidth=0.08, relheight=0.04)

        self.ncd = Label(self.aba_1, text=str(self.variaveis_1[0]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.ncd.place(relx=0.695, rely=0.163, relwidth=0.08, relheight=0.04)

        self.area = Label(self.aba_1, text=str(self.variaveis_1[1]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.area.place(relx=0.695, rely=0.21, relwidth=0.08, relheight=0.04)   

        self.fptk = Label(self.aba_1, text=str(self.variaveis_1[2]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.fptk.place(relx=0.8875, rely=0.163, relwidth=0.08, relheight=0.04)

        self.fpyk = Label(self.aba_1, text=str(self.variaveis_1[3]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.fpyk.place(relx=0.8875, rely=0.21, relwidth=0.08, relheight=0.04)

        self.E_mod_elast = Label(self.aba_1, text=str(self.variaveis_1[5]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.E_mod_elast.place(relx=0.8875, rely=0.115, relwidth=0.08, relheight=0.04)

        # 5.0 Quadrante:

        fig, ax = plt.subplots(2, 1, figsize=(2.66, 2.9))

        fig.subplots_adjust(hspace=0.6)

        ax[0].plot(self.x_1, self.y_1, color='black', marker='o', markersize=3) 
        ax[0].set_title('Traçado Reto do Cabo Parabólico', fontsize=8)
        ax[0].set_xlabel('Trecho (m)', fontsize=7)
        ax[0].set_ylabel('Altura (cm)', fontsize=7, labelpad=-180)
        ax[0].grid(True)  
        ax[0].tick_params(axis='both', labelsize=5)

        ax[1].plot(self.x_2, self.y_2, color='black', marker='o', markersize=3)
        ax[1].set_title('Diagrama de Forças', fontsize=8)
        ax[1].set_xlabel('Trecho (m)', fontsize=7)
        ax[1].set_ylabel('Força (KN)', fontsize=7, labelpad=-180)
        ax[1].grid(True)
        ax[1].tick_params(axis='both', labelsize=5) 

        self.canvas = FigureCanvasTkAgg(fig, master=self.aba_1)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=RIGHT, anchor=SW, padx=15.25, pady=16)

    # Widgets Estáticos da Aba 2
    def aba_2_funcoes(self):

        # 1.0 Quadrante:

        self.fundo_do_quadro_4 = Label(self.aba_2, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_4.place(relx=0.005, rely=0.01, relwidth=0.137, relheight=0.98)

        self.fundo_de_constante_w = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_constante_w.place(relx=0.015, rely=0.04, relwidth=0.115, relheight=0.58)

        self.fundo_de_constante_w = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_constante_w.place(relx=0.015, rely=0.645, relwidth=0.115, relheight=0.325)

        self.constante_w = Label(self.aba_2, text='A. de Anc. :', bg='#F0F0F0', fg='#000000')
        self.constante_w.place(relx=0.025, rely=0.02, relwidth=0.082, relheight=0.035)

        self.valor_de_delta_w = Entry(self.aba_2, text="")
        self.valor_de_delta_w.place(relx=0.03, rely=0.675, relwidth=0.085, relheight=0.045)

        self.botao_inserir_5 = tk.Button(self.aba_2, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=self.insercao_5)
        self.botao_inserir_5.place(relx=0.0325, rely=0.7425, relwidth=0.08, relheight=0.05)

        self.botao_apagar_3 = tk.Button(self.aba_2, text='Apagar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.apagando(self.quadro_4, self.quadro_4_itens, self.destruicao_2, 1))
        self.botao_apagar_3.place(relx=0.0325, rely=0.8175, relwidth=0.08, relheight=0.05)

        self.botao_calcular_2 = tk.Button(self.aba_2, text='Calcular', bg='#F0F0F0', fg='#000000', 
                                          command=self.perda_por_acomodacao_de_ancoragem)
        self.botao_calcular_2.place(relx=0.0325, rely=0.89, relwidth=0.08, relheight=0.05)

        # 2.0 Quadrante:

        self.fundo_do_quadro_5 = Label(self.aba_2, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_5.place(relx=0.155, rely=0.01, relwidth=0.454, relheight=0.98)

        self.fundo_de_variaveis_2 = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_2.place(relx=0.165, rely=0.04, relwidth=0.432, relheight=0.78)

        self.fundo_de_variaveis_2 = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_2.place(relx=0.165, rely=0.845, relwidth=0.432, relheight=0.125)

        self.comprimento_a_nome = Label(self.aba_2, text='a :', bg='#F0F0F0', fg='#000000')
        self.comprimento_a_nome.place(relx=0.23, rely=0.1, relwidth=0.02, relheight=0.035)

        self.comprimento_meio_l_nome = Label(self.aba_2, text='l/2 :', bg='#F0F0F0', fg='#000000')
        self.comprimento_meio_l_nome.place(relx=0.41, rely=0.1, relwidth=0.03, relheight=0.035)

        self.variavel_constante_E_nome = Label(self.aba_2, text='Eₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_constante_E_nome.place(relx=0.23, rely=0.27, relwidth=0.03, relheight=0.035)

        self.variavel_p_i_nome = Label(self.aba_2, text='Pᵢ :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_i_nome.place(relx=0.41, rely=0.27, relwidth=0.028, relheight=0.035)

        self.variavel_p_a_nome = Label(self.aba_2, text='P₀(x = a) :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_a_nome.place(relx=0.23, rely=0.44, relwidth=0.075, relheight=0.035)

        self.variavel_p_meio_l_nome = Label(self.aba_2, text='P₀(x = l/2) :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_meio_l_nome.place(relx=0.41, rely=0.44, relwidth=0.085, relheight=0.035)

        self.area_p_nome = Label(self.aba_2, text='Aₚ⁽⁰⁾ :', bg='#F0F0F0', fg='#000000')
        self.area_p_nome.place(relx=0.23, rely=0.61, relwidth=0.048, relheight=0.035)

        self.ncd_texto_2 = Label(self.aba_2, text='Nº Cd. :', bg='#F0F0F0', fg='#000000')
        self.ncd_texto_2.place(relx=0.41, rely=0.61, relwidth=0.06, relheight=0.035)
        
        self.lista_de_variaveis_2 = ttk.Combobox(self.aba_2, values=['',
                                                                     'a', 
                                                                     'l/2', 
                                                                     'Eₚ', 
                                                                     'Pᵢ', 
                                                                     'P₀(x = a)', 
                                                                     'P₀(x = l/2)', 
                                                                     'Aₚ⁽⁰⁾',
                                                                     'Nº de Cordoalhas'])
        self.lista_de_variaveis_2.place(relx=0.19, rely=0.88, relwidth=0.165, relheight=0.05)
        self.lista_de_variaveis_2.current(0)

        self.entrada_das_variaveis_2 = Entry(self.aba_2, text="")
        self.entrada_das_variaveis_2.place(relx=0.3725, rely=0.88, relwidth=0.09, relheight=0.05)

        self.botao_inserir_6 = tk.Button(self.aba_2, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=self.insercao_6)
        self.botao_inserir_6.place(relx=0.48, rely=0.88, relwidth=0.09, relheight=0.05)

        # 3.0 Quadrante

        self.fundo_do_quadro_5 = Label(self.aba_2, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_5.place(relx=0.6225, rely=0.01, relwidth=0.37, relheight=0.98)

        self.fundo_de_resultados_3 = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_3.place(relx=0.6325, rely=0.04, relwidth=0.347, relheight=0.125)

        self.fundo_de_resultados_4 = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_4.place(relx=0.6325, rely=0.19, relwidth=0.347, relheight=0.78)

        self.botao_aplicar_1 = tk.Button(self.aba_2, text='Aplicar', bg='#F0F0F0', fg='#000000',
                                         command=self.aplicar_1)
        self.botao_aplicar_1.place(relx=0.85, rely=0.075, relwidth=0.09, relheight=0.05)

        self.tipo_de_hipotese_nome = Label(self.aba_2, text='Hipótese :', bg='#F0F0F0', fg='#000000')
        self.tipo_de_hipotese_nome.place(relx=0.68, rely=0.25, relwidth=0.07, relheight=0.05)

        self.variavel_p_w_nome = Label(self.aba_2, text='P₀(x = w) :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_w_nome.place(relx=0.68, rely=0.35, relwidth=0.071, relheight=0.05)

        self.p_linha_0_nome = Label(self.aba_2, text="P'₀(x = 0) :", bg='#F0F0F0', fg='#000000')
        self.p_linha_0_nome.place(relx=0.68, rely=0.45, relwidth=0.074, relheight=0.05)

        self.p_linha_a_nome = Label(self.aba_2, text="P'₀(x = a) :", bg='#F0F0F0', fg='#000000')
        self.p_linha_a_nome.place(relx=0.68, rely=0.55, relwidth=0.074, relheight=0.05)

        self.p_linha_l_2_nome = Label(self.aba_2, text="P'₀(x = l/2) :", bg='#F0F0F0', fg='#000000')
        self.p_linha_l_2_nome.place(relx=0.68, rely=0.65, relwidth=0.0835, relheight=0.05)

        self.delta_0_nome = Label(self.aba_2, text="ΔP₀(x = 0) :", bg='#F0F0F0', fg='#000000')
        self.delta_0_nome.place(relx=0.68, rely=0.75, relwidth=0.08, relheight=0.05)

        self.delta_l_2_nome = Label(self.aba_2, text="ΔP₀(x = l/2) :", bg='#F0F0F0', fg='#000000')
        self.delta_l_2_nome.place(relx=0.68, rely=0.85, relwidth=0.09, relheight=0.05)

    # Widgets Dinâmicos da Aba 2
    def aba_2_funcoes_destrutivas(self):

        # 1.0 Quadrante:

        self.quadro_4 = ttk.Treeview(self.aba_2, columns=('Δw'))

        self.quadro_4.column('#0', width=0, stretch=NO)
        self.quadro_4.column('Δw', anchor=CENTER, width=20)

        self.quadro_4.heading('Δw', text='Δw', anchor=CENTER)

        self.quadro_4.place(relx=0.025, rely=0.0665, relwidth=0.075, relheight=0.535)

        self.y_scroll_4 = ttk.Scrollbar(self.aba_2, orient=tk.VERTICAL, command=self.quadro_3.yview)

        self.quadro_4['yscroll'] = self.y_scroll_4.set

        self.y_scroll_4.place(relx=0.1, rely=0.0665, relwidth=0.025, relheight=0.535)

        for i in range(len(self.quadro_4_itens)):
            self.quadro_4.insert(parent='', index=i, iid=i, text='', values=(str(self.quadro_4_itens[i])))

        # 2.0 Quadrante:

        self.comprimento_a = Label(self.aba_2, text=str(self.variaveis_2[0]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.comprimento_a.place(relx=0.23, rely=0.15, relwidth=0.12, relheight=0.05)
      
        self.comprimento_meio_l = Label(self.aba_2, text=str(self.variaveis_2[1]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.comprimento_meio_l.place(relx=0.41, rely=0.15, relwidth=0.12, relheight=0.05)
        
        self.variavel_constante_E = Label(self.aba_2, text=str(self.variaveis_2[2]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_constante_E.place(relx=0.23, rely=0.32, relwidth=0.12, relheight=0.05)

        self.variavel_p_i = Label(self.aba_2, text=str(self.variaveis_2[3]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_p_i.place(relx=0.41, rely=0.32, relwidth=0.12, relheight=0.05)

        self.variavel_p_a = Label(self.aba_2, text=str(self.variaveis_2[4]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_p_a.place(relx=0.23, rely=0.49, relwidth=0.12, relheight=0.05)

        self.variavel_p_meio_l = Label(self.aba_2, text=str(self.variaveis_2[5]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_p_meio_l.place(relx=0.41, rely=0.49, relwidth=0.12, relheight=0.05)

        self.area_p = Label(self.aba_2, text=str(self.variaveis_2[6]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.area_p.place(relx=0.23, rely=0.66, relwidth=0.12, relheight=0.05)

        self.variavel_n_de_cord_2 = Label(self.aba_2, text=str(self.variaveis_2[7]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_n_de_cord_2.place(relx=0.41, rely=0.66, relwidth=0.12, relheight=0.05)

        # 3.0 Quadrante:

        lista_de_delta_w_para_exibir = [('Δw = ' + str(i)) for i in self.quadro_4_itens]
        lista_de_delta_w_para_exibir.append('')
        self.lista_de_delta_w_para_exibir = ttk.Combobox(self.aba_2, values=lista_de_delta_w_para_exibir)
        self.lista_de_delta_w_para_exibir.place(relx=0.67, rely=0.075, relwidth=0.14, relheight=0.05)
        self.lista_de_delta_w_para_exibir.current(self.indice_da_lista_de_delta_w_para_exibir)

        self.tipo_de_hipotese = Label(self.aba_2, text=self.resultados_1[0], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.tipo_de_hipotese.place(relx=0.81, rely=0.25, relwidth=0.12, relheight=0.05)

        self.variavel_p_w = Label(self.aba_2, text=self.resultados_1[1], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_p_w.place(relx=0.81, rely=0.35, relwidth=0.12, relheight=0.05)

        self.p_linha_0 = Label(self.aba_2, text=self.resultados_1[2], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.p_linha_0.place(relx=0.81, rely=0.45, relwidth=0.12, relheight=0.05)

        self.p_linha_a = Label(self.aba_2, text=self.resultados_1[3], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.p_linha_a.place(relx=0.81, rely=0.55, relwidth=0.12, relheight=0.05)

        self.p_linha_l_2 = Label(self.aba_2, text=self.resultados_1[4], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.p_linha_l_2.place(relx=0.81, rely=0.65, relwidth=0.12, relheight=0.05)

        self.delta_0 = Label(self.aba_2, text=self.resultados_1[5], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.delta_0.place(relx=0.81, rely=0.75, relwidth=0.12, relheight=0.05)

        self.delta_l_2 = Label(self.aba_2, text=self.resultados_1[6], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.delta_l_2.place(relx=0.81, rely=0.85, relwidth=0.12, relheight=0.05)

    # Widgets Estáticos da Aba 3
    def aba_3_funcoes(self):

        # 1.0 Quadrante:

        self.fundo_do_quadro_6 = Label(self.aba_3, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_6.place(relx=0.005, rely=0.01, relwidth=0.3645, relheight=0.98)

        self.fundo_cabos_dias_forcas_alturas = Label(self.aba_3, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_cabos_dias_forcas_alturas.place(relx=0.015, rely=0.04, relwidth=0.3425, relheight=0.58)

        self.fundo_cabos_dias_forcas_alturas = Label(self.aba_3, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_cabos_dias_forcas_alturas.place(relx=0.015, rely=0.645, relwidth=0.3425, relheight=0.325)

        self.cabos_ppec_texto = Label(self.aba_3, text='Cabo :', bg='#F0F0F0', fg='#000000')
        self.cabos_ppec_texto.place(relx=0.04, rely=0.685, relwidth=0.043, relheight=0.035)

        self.cabos_ppec = Entry(self.aba_3, text="")
        self.cabos_ppec.place(relx=0.1075, rely=0.685, relwidth=0.07, relheight=0.04)

        self.dias_ppec_texto = Label(self.aba_3, text='Dia :', bg='#F0F0F0', fg='#000000')
        self.dias_ppec_texto.place(relx=0.195, rely=0.685, relwidth=0.034, relheight=0.035)

        self.dias_ppec = Entry(self.aba_3, text="")
        self.dias_ppec.place(relx=0.2625, rely=0.685, relwidth=0.07, relheight=0.04)

        self.forca_ppec_texto = Label(self.aba_3, text='Força :', bg='#F0F0F0', fg='#000000')
        self.forca_ppec_texto.place(relx=0.04, rely=0.75, relwidth=0.045, relheight=0.035)

        self.forca_ppec = Entry(self.aba_3, text="")
        self.forca_ppec.place(relx=0.1075, rely=0.75, relwidth=0.07, relheight=0.04)

        self.altura_ppec_texto = Label(self.aba_3, text='Altura :', bg='#F0F0F0', fg='#000000')
        self.altura_ppec_texto.place(relx=0.195, rely=0.75, relwidth=0.051, relheight=0.035)

        self.altura_ppec = Entry(self.aba_3, text="")
        self.altura_ppec.place(relx=0.2625, rely=0.75, relwidth=0.07, relheight=0.04)

        self.botao_procurar_2 = tk.Button(self.aba_3, text='Procurar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.procurar(self.links_2, self.destruicao_3))
        self.botao_procurar_2.place(relx=0.2525, rely=0.81, relwidth=0.08, relheight=0.05)

        self.botao_calcular_3 = tk.Button(self.aba_3, text='Calcular', bg='#F0F0F0', fg='#000000',
                                         command=self.perda_por_cura_do_concreto)
        self.botao_calcular_3.place(relx=0.04, rely=0.88, relwidth=0.08, relheight=0.05)

        self.botao_inserir_7 = tk.Button(self.aba_3, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=self.insercao_7)
        self.botao_inserir_7.place(relx=0.1475, rely=0.88, relwidth=0.08, relheight=0.05)

        self.botao_apagar_4 = tk.Button(self.aba_3, text='Apagar', bg='#F0F0F0', fg='#000000',
                                         command=lambda: self.apagando(self.quadro_5, self.quadro_5_itens, self.destruicao_3, 2))
        self.botao_apagar_4.place(relx=0.2525, rely=0.88, relwidth=0.08, relheight=0.05)

        # 2.0 Quadrante:

        self.fundo_do_quadro_7 = Label(self.aba_3, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_7.place(relx=0.385, rely=0.01, relwidth=0.402, relheight=0.98)

        self.fundo_de_variaveis_3 = Label(self.aba_3, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_3.place(relx=0.395, rely=0.04, relwidth=0.38, relheight=0.78)

        self.fundo_de_variaveis_3 = Label(self.aba_3, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_3.place(relx=0.395, rely=0.845, relwidth=0.38, relheight=0.125)

        self.lista_de_variaveis_4 = ttk.Combobox(self.aba_3, values=['',
                                                                     'n',
                                                                     'Ac',
                                                                     'Aₚ⁽⁰⁾',
                                                                     'Eₚ',
                                                                     'Ic',
                                                                     'Mg',
                                                                     'ycin',
                                                                     'fck₂₈',
                                                                     'Nº de Cordoalhas'])
        self.lista_de_variaveis_4.place(relx=0.42, rely=0.88, relwidth=0.135, relheight=0.05)
        self.lista_de_variaveis_4.current(0)

        self.variavel_n_ppec_texto = Label(self.aba_3, text='n :', bg='#F0F0F0', fg='#000000')
        self.variavel_n_ppec_texto.place(relx=0.42, rely=0.13, relwidth=0.02, relheight=0.035)

        self.variavel_ppec_ac_texto = Label(self.aba_3, text='Ac :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_ac_texto.place(relx=0.42, rely=0.37, relwidth=0.034, relheight=0.035)

        self.variavel_ppec_ap_texto = Label(self.aba_3, text='Aₚ⁽⁰⁾ :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_ap_texto.place(relx=0.42, rely=0.6, relwidth=0.04, relheight=0.035)

        self.variavel_ep_ppec_texto = Label(self.aba_3, text='Eₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_ep_ppec_texto.place(relx=0.535, rely=0.13, relwidth=0.030, relheight=0.035)

        self.variavel_ppec_ic_texto = Label(self.aba_3, text='Ic :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_ic_texto.place(relx=0.535, rely=0.37, relwidth=0.03, relheight=0.035)

        self.variavel_ppec_mg_texto = Label(self.aba_3, text='Mg :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_mg_texto.place(relx=0.535, rely=0.6, relwidth=0.034, relheight=0.035)

        self.variavel_ycin_ppec_texto = Label(self.aba_3, text='ycin :', bg='#F0F0F0', fg='#000000')
        self.variavel_ycin_ppec_texto.place(relx=0.65, rely=0.13, relwidth=0.038, relheight=0.035)

        self.variavel_ppec_fck_texto = Label(self.aba_3, text='fck₂₈ :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_fck_texto.place(relx=0.65, rely=0.37, relwidth=0.045, relheight=0.035)

        self.variavel_ppec_ncord_texto = Label(self.aba_3, text='Nº Cd. :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_ncord_texto.place(relx=0.65, rely=0.6, relwidth=0.058, relheight=0.035)

        self.entrada_das_variaveis_5 = Entry(self.aba_3, text="")
        self.entrada_das_variaveis_5.place(relx=0.5725, rely=0.88, relwidth=0.08, relheight=0.05)

        self.botao_inserir_9 = tk.Button(self.aba_3, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=self.insercao_8)
        self.botao_inserir_9.place(relx=0.67, rely=0.88, relwidth=0.08, relheight=0.05)

        # 3.0 Quadrante:

        self.fundo_do_quadro_8 = Label(self.aba_3, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_8.place(relx=0.805, rely=0.01, relwidth=0.185, relheight=0.98)

        self.fundo_de_resultados_5 = Label(self.aba_3, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_5.place(relx=0.815, rely=0.04, relwidth=0.163, relheight=0.61)

        self.fundo_de_resultados_6 = Label(self.aba_3, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_6.place(relx=0.815, rely=0.675, relwidth=0.163, relheight=0.295)

        self.variavel_ocp_ppec_texto = Label(self.aba_3, text='σcp :', bg='#F0F0F0', fg='#000000')
        self.variavel_ocp_ppec_texto.place(relx=0.8475, rely=0.1, relwidth=0.034, relheight=0.04)

        self.variavel_ppec_ocg_texto = Label(self.aba_3, text='σcg :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_ocg_texto.place(relx=0.8475, rely=0.28, relwidth=0.034, relheight=0.04)

        self.variavel_ppec_dop_texto = Label(self.aba_3, text='Δσp :', bg='#F0F0F0', fg='#000000')
        self.variavel_ppec_dop_texto.place(relx=0.8475, rely=0.46, relwidth=0.045, relheight=0.04)

        self.botao_aplicar_2 = tk.Button(self.aba_3, text='Aplicar', bg='#F0F0F0', fg='#000000',
                                         command=self.aplicar_2)
        self.botao_aplicar_2.place(relx=0.8475, rely=0.88, relwidth=0.1, relheight=0.05)

    # Widgets Dinâmicos da Aba 3
    def aba_3_funcoes_destrutivas(self):

        # 1.0 Quadrante:

        self.quadro_5 = ttk.Treeview(self.aba_3, columns=('Cabos', 'Dias', 'Forças', 'Alturas'))

        self.quadro_5.column('#0', width=0, stretch=NO)
        self.quadro_5.column('Cabos', anchor=CENTER, width=20)
        self.quadro_5.column('Dias', anchor=CENTER, width=20)
        self.quadro_5.column('Forças', anchor=CENTER, width=20)
        self.quadro_5.column('Alturas', anchor=CENTER, width=20)

        self.quadro_5.heading('Cabos', text='Cabos', anchor=CENTER)
        self.quadro_5.heading('Dias', text='Dias', anchor=CENTER)
        self.quadro_5.heading('Forças', text='Forças', anchor=CENTER)
        self.quadro_5.heading('Alturas', text='Alturas', anchor=CENTER)

        self.quadro_5.place(relx=0.025, rely=0.0665, relwidth=0.3, relheight=0.535)

        self.y_scroll_5 = ttk.Scrollbar(self.aba_3, orient=tk.VERTICAL, command=self.quadro_5.yview)

        self.quadro_5['yscroll'] = self.y_scroll_5.set

        self.y_scroll_5.place(relx=0.325, rely=0.0665, relwidth=0.025, relheight=0.535)

        for i in range(len(self.quadro_5_itens[0])):
            self.quadro_5.insert(parent='', index=i, iid=i, text='', values=((self.quadro_5_itens[0][i]), 
                                                                             '%.0f' % float(self.quadro_5_itens[1][i]), 
                                                                             '%.2f' % float(self.quadro_5_itens[2][i]), 
                                                                             '%.2f' % float(self.quadro_5_itens[3][i])))

        self.lista_de_links_2 = ttk.Combobox(self.aba_3, values=self.links_2)
        self.lista_de_links_2.place(relx=0.04, rely=0.81, relwidth=0.19, relheight=0.05)

        # 2.0 Quadrante:

        self.variavel_ppec_n = Label(self.aba_3, text=self.variaveis_3[0], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_n.place(relx=0.42, rely=0.2, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ac = Label(self.aba_3, text=self.variaveis_3[1], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ac.place(relx=0.42, rely=0.44, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ap = Label(self.aba_3, text=self.variaveis_3[2], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ap.place(relx=0.42, rely=0.67, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ep = Label(self.aba_3, text=self.variaveis_3[3], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ep.place(relx=0.535, rely=0.2, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ic = Label(self.aba_3, text=self.variaveis_3[4], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ic.place(relx=0.535, rely=0.44, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_mg = Label(self.aba_3, text=self.variaveis_3[5], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_mg.place(relx=0.535, rely=0.67, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ycin = Label(self.aba_3, text=self.variaveis_3[6], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ycin.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_fck = Label(self.aba_3, text=self.variaveis_3[7], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_fck.place(relx=0.65, rely=0.44, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ncord = Label(self.aba_3, text=self.variaveis_3[8], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ncord.place(relx=0.65, rely=0.67, relwidth=0.1, relheight=0.05)

        # 3.0 Quadrante:

        self.variavel_ppec_ocp = Label(self.aba_3, text=self.resultados_2[0], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ocp.place(relx=0.8475, rely=0.17, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_ocg = Label(self.aba_3, text=self.resultados_2[1], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_ocg.place(relx=0.8475, rely=0.35, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_dop = Label(self.aba_3, text=self.resultados_2[2], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_dop.place(relx=0.8475, rely=0.53, relwidth=0.1, relheight=0.05)

        self.variavel_ppec_p_individuais = Label(self.aba_3, text=self.p_individual, relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ppec_p_individuais.place(relx=0.8475, rely=0.72, relwidth=0.1, relheight=0.05)

        perdas_individuais_de_força = ['']

        for i in range(len(self.quadro_5_itens[0])):
            perdas_individuais_de_força.append(f'P_{self.quadro_5_itens[0][i]}')

        self.lista_de_resultados = ttk.Combobox(self.aba_3, values=perdas_individuais_de_força)
        self.lista_de_resultados.place(relx=0.8475, rely=0.8, relwidth=0.1, relheight=0.05)
        self.lista_de_resultados.current(self.indice_da_lista_de_p_individual_para_exibir)

    # Widgets Estáticos da Aba 4
    def aba_4_funcoes(self):

        # 1.0 Quadrante:

        self.fundo_do_quadro_9 = Label(self.aba_4, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_9.place(relx=0.005, rely=0.01, relwidth=0.466, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_pprc = Label(self.aba_4, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_pprc.place(relx=0.015, rely=0.04, relwidth=0.4455, relheight=0.93)

        # 2.0 Quadrante:

        self.fundo_do_quadro_10 = Label(self.aba_4, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_10.place(relx=0.481, rely=0.01, relwidth=0.3685, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_pprc_2 = Label(self.aba_4, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_pprc_2.place(relx=0.492, rely=0.04, relwidth=0.3475, relheight=0.6)

        self.fundo_tabelas_calculo_automatico_pprc_2_variaveis = Label(self.aba_4, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_pprc_2_variaveis.place(relx=0.492, rely=0.665, relwidth=0.3475, relheight=0.305)

        self.variavel_t0_texto = Label(self.aba_4, text='t₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_t0_texto.place(relx=0.52, rely=0.09, relwidth=0.02, relheight=0.035)

        self.variavel_t0_tabela = Entry(self.aba_4, text="")
        self.variavel_t0_tabela.place(relx=0.52, rely=0.16, relwidth=0.12, relheight=0.05)

        self.variavel_U_texto = Label(self.aba_4, text='U :', bg='#F0F0F0', fg='#000000')
        self.variavel_U_texto.place(relx=0.690, rely=0.09, relwidth=0.02, relheight=0.035)

        self.variavel_U_tabela = Entry(self.aba_4, text="")
        self.variavel_U_tabela.place(relx=0.690, rely=0.16, relwidth=0.12, relheight=0.05)

        self.variavel_t_texto = Label(self.aba_4, text='t :', bg='#F0F0F0', fg='#000000')
        self.variavel_t_texto.place(relx=0.52, rely=0.27, relwidth=0.02, relheight=0.035)

        self.variavel_t_tabela = Entry(self.aba_4, text="")
        self.variavel_t_tabela.place(relx=0.52, rely=0.35, relwidth=0.12, relheight=0.05)

        self.variavel_t_tabela_lista = ttk.Combobox(self.aba_4, values=['≠ ∞', '= ∞'])
        self.variavel_t_tabela_lista.place(relx=0.690, rely=0.35, relwidth=0.12, relheight=0.05)
        self.variavel_t_tabela_lista.current(1)

        self.variavel_h_texto = Label(self.aba_4, text='h :', bg='#F0F0F0', fg='#000000')
        self.variavel_h_texto.place(relx=0.52, rely=0.46, relwidth=0.02, relheight=0.035)

        self.variavel_h_tabela = Entry(self.aba_4, text="")
        self.variavel_h_tabela.place(relx=0.52, rely=0.53, relwidth=0.12, relheight=0.05)

        self.variavel_abatimento_texto = Label(self.aba_4, text='Abatimento :', bg='#F0F0F0', fg='#000000')
        self.variavel_abatimento_texto.place(relx=0.690, rely=0.46, relwidth=0.1, relheight=0.035)

        self.variavel_abatimento_tabela_lista = ttk.Combobox(self.aba_4, values=['0 - 4', '5 - 9', '10 - 15'])
        self.variavel_abatimento_tabela_lista.place(relx=0.690, rely=0.53, relwidth=0.12, relheight=0.05)
        self.variavel_abatimento_tabela_lista.current(0)

        self.botao_inserir_10 = tk.Button(self.aba_4, text='Inserir', bg='#F0F0F0', fg='#000000', command=self.insercao_9)
        self.botao_inserir_10.place(relx=0.52, rely=0.85, relwidth=0.08, relheight=0.05)

        self.botao_apagar_5 = tk.Button(self.aba_4, text='Apagar', bg='#F0F0F0', fg='#000000', 
                                        command=lambda: self.apagando(self.quadro_6, self.quadro_6_itens, self.destruicao_4, 2))
        self.botao_apagar_5.place(relx=0.625, rely=0.85, relwidth=0.08, relheight=0.05)

        self.botao_calcular_4 = tk.Button(self.aba_4, text='Calcular', bg='#F0F0F0', fg='#000000', command=lambda: self.perda_por_retracao_do_concreto())
        self.botao_calcular_4.place(relx=0.73, rely=0.85, relwidth=0.08, relheight=0.05)

        self.botao_procurar_3 = tk.Button(self.aba_4, text='Procurar', bg='#F0F0F0', fg='#000000', 
                                          command=lambda: self.procurar(self.links_3, self.destruicao_4))
        self.botao_procurar_3.place(relx=0.52, rely=0.73, relwidth=0.08, relheight=0.05)

        # 3.0 Quadrante:

        self.fundo_do_quadro_11 = Label(self.aba_4, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_11.place(relx=0.86, rely=0.01, relwidth=0.14, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_pprc_3 = Label(self.aba_4, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_pprc_3.place(relx=0.871, rely=0.04, relwidth=0.1175, relheight=0.93)

    # Widgets Dinâmicos da Aba 4
    def aba_4_funcoes_destrutivas(self):

        # 1º Quadrante
        
        self.quadro_6 = ttk.Treeview(self.aba_4, columns=('U', 't₀', 't', 'h', 'Abatimento'))

        self.quadro_6.column('#0', width=0, stretch=NO)
        self.quadro_6.column('U', anchor=CENTER, width=20)
        self.quadro_6.column('t₀', anchor=CENTER, width=20)
        self.quadro_6.column('t', anchor=CENTER, width=20)
        self.quadro_6.column('h', anchor=CENTER, width=20)
        self.quadro_6.column('Abatimento', anchor=CENTER, width=20)

        self.quadro_6.heading('U', text='U', anchor=CENTER)
        self.quadro_6.heading('t₀', text='t₀', anchor=CENTER)
        self.quadro_6.heading('t', text='t', anchor=CENTER)
        self.quadro_6.heading('h', text='h', anchor=CENTER)
        self.quadro_6.heading('Abatimento', text='Abto.', anchor=CENTER)

        self.quadro_6.place(relx=0.025, rely=0.0665, relwidth=0.4025, relheight=0.885)

        self.y_scroll_6 = ttk.Scrollbar(self.aba_4, orient=tk.VERTICAL, command=self.quadro_6.yview)

        self.quadro_6['yscroll'] = self.y_scroll_6.set

        self.y_scroll_6.place(relx=0.4275, rely=0.0665, relwidth=0.025, relheight=0.885)

        for i in range(len(self.quadro_6_itens[0])):
            self.quadro_6.insert(parent='', index=i, iid=i, text='', values=((self.quadro_6_itens[0][i], 
                                                                              self.quadro_6_itens[1][i], 
                                                                              self.quadro_6_itens[2][i], 
                                                                              self.quadro_6_itens[3][i],
                                                                              self.quadro_6_itens[4][i])))
            
        # 2º Quadrante

        self.lista_de_links_3 = ttk.Combobox(self.aba_4, values=self.links_3)
        self.lista_de_links_3.place(relx=0.625, rely=0.73, relwidth=0.185, relheight=0.05)
        
        # 3º Quadrante

        self.quadro_7 = ttk.Treeview(self.aba_4, columns=('εcs'))

        self.quadro_7.column('#0', width=0, stretch=NO)
        self.quadro_7.column('εcs', anchor=CENTER, width=20)

        self.quadro_7.heading('εcs', text='εcs', anchor=CENTER)

        self.quadro_7.place(relx=0.8815, rely=0.0665, relwidth=0.075, relheight=0.885)

        self.y_scroll_7 = ttk.Scrollbar(self.aba_4, orient=tk.VERTICAL, command=self.quadro_7.yview)

        self.quadro_7['yscroll'] = self.y_scroll_7.set

        self.y_scroll_7.place(relx=0.9572, rely=0.0665, relwidth=0.025, relheight=0.885)

        for i in range(len(self.quadro_7_itens)):
            self.quadro_7.insert(parent='', index=i, iid=i, text='', values=((self.quadro_7_itens[i])))

    # Widgets Estáticos da Aba 5
    def aba_5_funcoes(self):

        # 1.0 Quadrante:

        self.fundo_do_quadro_9 = Label(self.aba_5, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_9.place(relx=0.005, rely=0.01, relwidth=0.545, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_ppfc = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_ppfc.place(relx=0.015, rely=0.04, relwidth=0.5225, relheight=0.58)

        self.fundo_variaveis_calculo_automatico_ppfc = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_variaveis_calculo_automatico_ppfc.place(relx=0.015, rely=0.645, relwidth=0.5225, relheight=0.325)

        self.variavel_t0_texto_2 = Label(self.aba_5, text='t₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_t0_texto_2.place(relx=0.028, rely=0.6915, relwidth=0.02, relheight=0.035)

        self.variavel_t0_tabela_2 = Entry(self.aba_5, text="")
        self.variavel_t0_tabela_2.place(relx=0.058, rely=0.6915, relwidth=0.08, relheight=0.0425)

        self.variavel_Ti_texto_2 = Label(self.aba_5, text='Ti :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ti_texto_2.place(relx=0.155, rely=0.6915, relwidth=0.02, relheight=0.035)

        self.variavel_Ti_tabela_2 = Entry(self.aba_5, text="")
        self.variavel_Ti_tabela_2.place(relx=0.185, rely=0.6915, relwidth=0.08, relheight=0.0425)

        self.variavel_U_texto_2 = Label(self.aba_5, text='U :', bg='#F0F0F0', fg='#000000')
        self.variavel_U_texto_2.place(relx=0.285, rely=0.6915, relwidth=0.02, relheight=0.035)

        self.variavel_U_tabela_2 = Entry(self.aba_5, text="")
        self.variavel_U_tabela_2.place(relx=0.315, rely=0.6915, relwidth=0.08, relheight=0.0425)

        self.variavel_h_texto_2 = Label(self.aba_5, text='h :', bg='#F0F0F0', fg='#000000')
        self.variavel_h_texto_2.place(relx=0.4125, rely=0.6915, relwidth=0.02, relheight=0.035)

        self.variavel_h_tabela_2 = Entry(self.aba_5, text="")
        self.variavel_h_tabela_2.place(relx=0.4425, rely=0.6915, relwidth=0.08, relheight=0.0425)

        self.variavel_t_texto_2 = Label(self.aba_5, text='t :', bg='#F0F0F0', fg='#000000')
        self.variavel_t_texto_2.place(relx=0.028, rely=0.79, relwidth=0.02, relheight=0.035)

        self.variavel_t_tabela_2 = Entry(self.aba_5, text="")
        self.variavel_t_tabela_2.place(relx=0.058, rely=0.79, relwidth=0.05, relheight=0.0425)

        self.variavel_t_tabela_lista_2 = ttk.Combobox(self.aba_5, values=['≠ ∞', '= ∞'])
        self.variavel_t_tabela_lista_2.place(relx=0.12, rely=0.7875, relwidth=0.06, relheight=0.0425)
        self.variavel_t_tabela_lista_2.current(1)

        self.variavel_abatimento_texto_2 = Label(self.aba_5, text='Abto. :', bg='#F0F0F0', fg='#000000')
        self.variavel_abatimento_texto_2.place(relx=0.2, rely=0.79, relwidth=0.06, relheight=0.035)

        self.variavel_abatimento_tabela_lista_2 = ttk.Combobox(self.aba_5, values=['0 - 4', '5 - 9', '10 - 15'])
        self.variavel_abatimento_tabela_lista_2.place(relx=0.26, rely=0.79, relwidth=0.09, relheight=0.0425)
        self.variavel_abatimento_tabela_lista_2.current(0)

        self.variavel_CP_texto_2 = Label(self.aba_5, text='CP :', bg='#F0F0F0', fg='#000000')
        self.variavel_CP_texto_2.place(relx=0.37, rely=0.79, relwidth=0.04, relheight=0.035)

        self.variavel_CP_tabela_lista_2 = ttk.Combobox(self.aba_5, values=['I', 'II', 'III', 'IV', 'V'])
        self.variavel_CP_tabela_lista_2.place(relx=0.41, rely=0.79, relwidth=0.11, relheight=0.0425)
        self.variavel_CP_tabela_lista_2.current(0)

        self.botao_inserir_10 = tk.Button(self.aba_5, text='Inserir', bg='#F0F0F0', fg='#000000', command=self.insercao_10)
        self.botao_inserir_10.place(relx=0.028, rely=0.88, relwidth=0.08, relheight=0.05)

        self.botao_apagar_5 = tk.Button(self.aba_5, text='Apagar', bg='#F0F0F0', fg='#000000', 
                                        command=lambda: self.apagando(self.quadro_8, self.quadro_8_itens, self.destruicao_5, 2))
        self.botao_apagar_5.place(relx=0.132, rely=0.88, relwidth=0.08, relheight=0.05)

        self.botao_procurar_3 = tk.Button(self.aba_5, text='Procurar', bg='#F0F0F0', fg='#000000', 
                                          command=lambda: self.procurar(self.links_4, self.destruicao_5))
        self.botao_procurar_3.place(relx=0.44, rely=0.88, relwidth=0.08, relheight=0.05)

        # 2.0 Quadrante:

        self.fundo_do_quadro_10 = Label(self.aba_5, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_10.place(relx=0.56, rely=0.01, relwidth=0.14, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_ppfc_2 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_ppfc_2.place(relx=0.571, rely=0.04, relwidth=0.1175, relheight=0.78)

        self.fundo_variaveis_calculo_automatico_ppfc_2 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_variaveis_calculo_automatico_ppfc_2.place(relx=0.571, rely=0.8505, relwidth=0.1175, relheight=0.12)

        self.botao_calcular_4 = tk.Button(self.aba_5, text='Calcular', bg='#F0F0F0', fg='#000000', command=lambda: self.perda_por_fluencia_do_concreto(0))
        self.botao_calcular_4.place(relx=0.59, rely=0.88, relwidth=0.08, relheight=0.05)

        # 3.0 Quadrante:

        self.fundo_do_quadro_11 = Label(self.aba_5, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_11.place(relx=0.71, rely=0.01, relwidth=0.14, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_ppfc_3 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_ppfc_3.place(relx=0.721, rely=0.04, relwidth=0.1175, relheight=0.34)

        self.fundo_variaveis_calculo_automatico_ppfc_3_1 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_variaveis_calculo_automatico_ppfc_3_1.place(relx=0.721, rely=0.41, relwidth=0.1175, relheight=0.265)

        self.fundo_variaveis_calculo_automatico_ppfc_3_2 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_variaveis_calculo_automatico_ppfc_3_2.place(relx=0.721, rely=0.705, relwidth=0.1175, relheight=0.265)

        self.variavel_Bst0_tabela = Entry(self.aba_5, text="")
        self.variavel_Bst0_tabela.place(relx=0.74, rely=0.445, relwidth=0.08, relheight=0.05)

        self.botao_inserir_11 = tk.Button(self.aba_5, text='Inserir', bg='#F0F0F0', fg='#000000', command=lambda: self.insercao_11(0))
        self.botao_inserir_11.place(relx=0.74, rely=0.515, relwidth=0.08, relheight=0.05)

        self.botao_apagar_6 = tk.Button(self.aba_5, text='Apagar', bg='#F0F0F0', fg='#000000', 
                                        command=lambda: self.apagando(self.quadro_10, self.quadro_10_itens, self.destruicao_5, 1))
        self.botao_apagar_6.place(relx=0.74, rely=0.585, relwidth=0.08, relheight=0.05)       

        self.inserir_fck_ppfc = Entry(self.aba_5, text="")
        self.inserir_fck_ppfc.place(relx=0.74, rely=0.81, relwidth=0.08, relheight=0.05)

        self.texto_fck_ppfc = Label(self.aba_5, text='fck :', bg='#F0F0F0', fg='#000000')
        self.texto_fck_ppfc.place(relx=0.73, rely=0.6875, relwidth=0.035, relheight=0.03)

        self.botao_inserir_12 = tk.Button(self.aba_5, text='Inserir', bg='#F0F0F0', fg='#000000', 
                                        command=lambda: self.insercao_11(1))
        self.botao_inserir_12.place(relx=0.74, rely=0.88, relwidth=0.08, relheight=0.05)

        # 4.0 Quadrante:

        self.fundo_do_quadro_12 = Label(self.aba_5, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_12.place(relx=0.86, rely=0.01, relwidth=0.14, relheight=0.98)

        self.fundo_tabelas_calculo_automatico_pprc_4 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_tabelas_calculo_automatico_pprc_4.place(relx=0.871, rely=0.04, relwidth=0.1175, relheight=0.66)

        self.fundo_variaveis_calculo_automatico_pprc_4 = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_variaveis_calculo_automatico_pprc_4.place(relx=0.871, rely=0.8505, relwidth=0.1175, relheight=0.12)

        self.fundo_de_ecc = Label(self.aba_5, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_ecc.place(relx=0.871, rely=0.73, relwidth=0.1175, relheight=0.09)

        self.ecc_texto = Label(self.aba_5, text='εcc :', bg='#F0F0F0', fg='#000000')
        self.ecc_texto.place(relx=0.8785, rely=0.718, relwidth=0.04, relheight=0.02)

        self.botao_calcular_5 = tk.Button(self.aba_5, text='Calcular', bg='#F0F0F0', fg='#000000', command=lambda: self.perda_por_fluencia_do_concreto(1))
        self.botao_calcular_5.place(relx=0.89, rely=0.88, relwidth=0.08, relheight=0.05)

    # Widgets Dinâmicos da Aba 5
    def aba_5_funcoes_destrutivas(self):

        # 1º Quadrante
        
        self.quadro_8 = ttk.Treeview(self.aba_5, columns=('U', 'Ti', 't₀', 't', 'h', 'Abatimento', 'CP'))

        self.quadro_8.column('#0', width=0, stretch=NO)
        self.quadro_8.column('U', anchor=CENTER, width=20)
        self.quadro_8.column('Ti', anchor=CENTER, width=20)
        self.quadro_8.column('t₀', anchor=CENTER, width=20)
        self.quadro_8.column('t', anchor=CENTER, width=20)
        self.quadro_8.column('h', anchor=CENTER, width=20)
        self.quadro_8.column('Abatimento', anchor=CENTER, width=20)
        self.quadro_8.column('CP', anchor=CENTER, width=20)

        self.quadro_8.heading('U', text='U', anchor=CENTER)
        self.quadro_8.heading('Ti', text='Ti', anchor=CENTER)
        self.quadro_8.heading('t₀', text='t₀', anchor=CENTER)
        self.quadro_8.heading('t', text='t', anchor=CENTER)
        self.quadro_8.heading('h', text='h', anchor=CENTER)
        self.quadro_8.heading('Abatimento', text='Abto.', anchor=CENTER)
        self.quadro_8.heading('CP', text='CP', anchor=CENTER)

        self.quadro_8.place(relx=0.025, rely=0.0665, relwidth=0.48, relheight=0.535)

        self.y_scroll_8 = ttk.Scrollbar(self.aba_5, orient=tk.VERTICAL, command=self.quadro_8.yview)

        self.quadro_8['yscroll'] = self.y_scroll_8.set

        self.y_scroll_8.place(relx=0.505, rely=0.0665, relwidth=0.025, relheight=0.535)

        for i in range(len(self.quadro_8_itens[0])):
            self.quadro_8.insert(parent='', index=i, iid=i, text='', values=((self.quadro_8_itens[0][i], 
                                                                              self.quadro_8_itens[1][i], 
                                                                              self.quadro_8_itens[2][i], 
                                                                              self.quadro_8_itens[3][i],
                                                                              self.quadro_8_itens[4][i],
                                                                              self.quadro_8_itens[5][i],
                                                                              self.quadro_8_itens[6][i])))
            
        self.lista_de_links_4 = ttk.Combobox(self.aba_5, values=self.links_4)
        self.lista_de_links_4.place(relx=0.236, rely=0.88, relwidth=0.185, relheight=0.05)

        # 2º Quadrante

        self.quadro_9 = ttk.Treeview(self.aba_5, columns=('φ'))

        self.quadro_9.column('#0', width=0, stretch=NO)
        self.quadro_9.column('φ', anchor=CENTER, width=20)

        self.quadro_9.heading('φ', text='φ', anchor=CENTER)

        self.quadro_9.place(relx=0.581, rely=0.0665, relwidth=0.075, relheight=0.735)

        self.y_scroll_9 = ttk.Scrollbar(self.aba_5, orient=tk.VERTICAL, command=self.quadro_9.yview)

        self.quadro_9['yscroll'] = self.y_scroll_9.set

        self.y_scroll_9.place(relx=0.6567, rely=0.0665, relwidth=0.025, relheight=0.735)

        for i in range(len(self.quadro_9_itens)):
            self.quadro_9.insert(parent='', index=i, iid=i, text='', values=((self.quadro_9_itens[i])))

        # 3º Quadrante

        self.quadro_10 = ttk.Treeview(self.aba_5, columns=('σ'))

        self.quadro_10.column('#0', width=0, stretch=NO)
        self.quadro_10.column('σ', anchor=CENTER, width=20)

        self.quadro_10.heading('σ', text='σ', anchor=CENTER)

        self.quadro_10.place(relx=0.731, rely=0.0665, relwidth=0.075, relheight=0.295)

        self.y_scroll_10 = ttk.Scrollbar(self.aba_5, orient=tk.VERTICAL, command=self.quadro_10.yview)

        self.quadro_10['yscroll'] = self.y_scroll_10.set

        self.y_scroll_10.place(relx=0.8067, rely=0.0665, relwidth=0.025, relheight=0.295)

        for i in range(len(self.quadro_10_itens)):
            self.quadro_10.insert(parent='', index=i, iid=i, text='', values=((self.quadro_10_itens[i])))

        self.variavel_fck_ppfc = Label(self.aba_5, text=self.fck_ecc, relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_fck_ppfc.place(relx=0.74, rely=0.74, relwidth=0.08, relheight=0.05)

        # 4º Quadrante

        self.quadro_11 = ttk.Treeview(self.aba_5, columns=('εcc'))

        self.quadro_11.column('#0', width=0, stretch=NO)
        self.quadro_11.column('εcc', anchor=CENTER, width=20)

        self.quadro_11.heading('εcc', text='σ . φ', anchor=CENTER)

        self.quadro_11.place(relx=0.881, rely=0.0665, relwidth=0.075, relheight=0.616)

        self.y_scroll_11 = ttk.Scrollbar(self.aba_5, orient=tk.VERTICAL, command=self.quadro_11.yview)

        self.quadro_11['yscroll'] = self.y_scroll_11.set

        self.y_scroll_11.place(relx=0.9567, rely=0.0665, relwidth=0.025, relheight=0.616)

        for i in range(len(self.quadro_11_itens)):
            self.quadro_11.insert(parent='', index=i, iid=i, text='', values=((self.quadro_11_itens[i])))

        self.ecc = Label(self.aba_5, text=self.resultado_ecc, relief="sunken", bg='#FFFFFF', fg='#000000')
        self.ecc.place(relx=0.89, rely=0.7525, relwidth=0.08, relheight=0.0475) 

    # Widgets Estáticos da Aba 6
    def aba_6_funcoes(self):

        # 1.0 Quadrante

        self.fundo_do_quadro_13 = Label(self.aba_6, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_13.place(relx=0.005, rely=0.011, relwidth=0.7835, relheight=0.98)

        self.fundo_de_variaveis_4 = Label(self.aba_6, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_4.place(relx=0.018, rely=0.041, relwidth=0.759, relheight=0.78)

        self.fundo_insercao_de_variaveis = Label(self.aba_6, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_insercao_de_variaveis.place(relx=0.018, rely=0.8485, relwidth=0.759, relheight=0.12)

        self.variavel_n_ppra_texto = Label(self.aba_6, text='Nº Cd.:', bg='#F0F0F0', fg='#000000')
        self.variavel_n_ppra_texto.place(relx=0.078, rely=0.125, relwidth=0.05, relheight=0.035)

        self.variavel_ap_ppra_texto = Label(self.aba_6, text='Aₚ⁽⁰⁾ :', bg='#F0F0F0', fg='#000000')
        self.variavel_ap_ppra_texto.place(relx=0.254, rely=0.125, relwidth=0.04, relheight=0.05)

        self.variavel_p0_ppra_texto = Label(self.aba_6, text='P₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_p0_ppra_texto.place(relx=0.4415, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_Mg_ppra_texto = Label(self.aba_6, text='Mg :', bg='#F0F0F0', fg='#000000')
        self.variavel_Mg_ppra_texto.place(relx=0.6175, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_ep_ppra_texto = Label(self.aba_6, text='eₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_ep_ppra_texto.place(relx=0.078, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_Ep_ppra_texto = Label(self.aba_6, text='Eₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ep_ppra_texto.place(relx=0.254, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_Ic_ppra_texto = Label(self.aba_6, text='Ic :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ic_ppra_texto.place(relx=0.4415, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_Eci28_ppra_texto = Label(self.aba_6, text='Eci₂₈ :', bg='#F0F0F0', fg='#000000')
        self.variavel_Eci28_ppra_texto.place(relx=0.6175, rely=0.3625, relwidth=0.04, relheight=0.05)

        self.variavel_fptk_ppra_texto = Label(self.aba_6, text='fptk :', bg='#F0F0F0', fg='#000000')
        self.variavel_fptk_ppra_texto.place(relx=0.078, rely=0.6, relwidth=0.035, relheight=0.05)

        self.variavel_t0_ppra_texto = Label(self.aba_6, text='t₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_t0_ppra_texto.place(relx=0.254, rely=0.6, relwidth=0.03, relheight=0.05)

        self.variavel_t_ppra_texto = Label(self.aba_6, text='t :', bg='#F0F0F0', fg='#000000')
        self.variavel_t_ppra_texto.place(relx=0.4415, rely=0.6, relwidth=0.02, relheight=0.05)

        self.variavel_relaxacao_ppra_texto = Label(self.aba_6, text='Relaxação :', bg='#F0F0F0', fg='#000000')
        self.variavel_relaxacao_ppra_texto.place(relx=0.6175, rely=0.6, relwidth=0.088, relheight=0.05)

        self.lista_ppra_1 = ttk.Combobox(self.aba_6, values=['', 'Cordoalhas RN', 'Cordoalhas RB', 'Fios RN', 'Fios RB', 'Barras'])
        self.lista_ppra_1.place(relx=0.041, rely=0.8825, relwidth=0.135, relheight=0.05)
        self.lista_ppra_1.current(0)

        self.botao_inserir_13 = tk.Button(self.aba_6, text='Inserir', bg='#F0F0F0', fg='#000000', command=lambda: self.insercao_12(0))
        self.botao_inserir_13.place(relx=0.195, rely=0.8825, relwidth=0.08, relheight=0.05)

        self.lista_ppra_2 = ttk.Combobox(self.aba_6, values=['', 
                                                             'Nº de Cordoalhas', 
                                                             'Aₚ⁽⁰⁾', 
                                                             'P₀', 
                                                             'Mg', 
                                                             'eₚ', 
                                                             'Eₚ', 
                                                             'Ic', 
                                                             'Eci₂₈', 
                                                             'fptk', 
                                                             't₀', 
                                                             't = ∞', 
                                                             't ≠ ∞'])
        self.lista_ppra_2.place(relx=0.2922, rely=0.8825, relwidth=0.206, relheight=0.05)
        self.lista_ppra_2.current(0)

        self.variaveis_ppra = Entry(self.aba_6, text="")
        self.variaveis_ppra.place(relx=0.5170, rely=0.8825, relwidth=0.135, relheight=0.05)

        self.botao_inserir_14 = tk.Button(self.aba_6, text='Inserir', bg='#F0F0F0', fg='#000000', command=lambda: self.insercao_12(1))
        self.botao_inserir_14.place(relx=0.6725, rely=0.8825, relwidth=0.08, relheight=0.05)

        # 2.0 Quadrante

        self.fundo_do_quadro_14 = Label(self.aba_6, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_14.place(relx=0.805, rely=0.011, relwidth=0.1865, relheight=0.98)

        self.fundo_de_respostas_1 = Label(self.aba_6, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_respostas_1.place(relx=0.816, rely=0.041, relwidth=0.163, relheight=0.365)

        self.fundo_de_respostas_2 = Label(self.aba_6, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_respostas_2.place(relx=0.816, rely=0.44, relwidth=0.163, relheight=0.290)

        self.fundo_de_respostas_3 = Label(self.aba_6, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_respostas_3.place(relx=0.816, rely=0.764, relwidth=0.163, relheight=0.2075)

        self.variavel_w_ppra_texto = Label(self.aba_6, text='Ψ₁₀₀₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_w_ppra_texto.place(relx=0.85, rely=0.0675, relwidth=0.04, relheight=0.035)

        self.variavel_delta_o_pr_ppra_texto = Label(self.aba_6, text='Δσₚᵣ :', bg='#F0F0F0', fg='#000000')
        self.variavel_delta_o_pr_ppra_texto.place(relx=0.85, rely=0.18, relwidth=0.04, relheight=0.035)

        self.botao_calcular_6 = tk.Button(self.aba_6, text='Calcular', bg='#F0F0F0', fg='#000000', command=lambda: self.perda_por_relaxacao(0))
        self.botao_calcular_6.place(relx=0.85, rely=0.318, relwidth=0.0985, relheight=0.05)

        self.variavel_delta_o_p_cs_ppra_texto = Label(self.aba_6, text='Δσₚ,c+s :', bg='#F0F0F0', fg='#000000')
        self.variavel_delta_o_p_cs_ppra_texto.place(relx=0.825, rely=0.42, relwidth=0.0675, relheight=0.035)

        self.variavel_delta_o_p_cs_ppra_entrada = Entry(self.aba_6, text="")
        self.variavel_delta_o_p_cs_ppra_entrada.place(relx=0.85, rely=0.565, relwidth=0.0985, relheight=0.05)

        self.botao_inserir_15 = tk.Button(self.aba_6, text='Inserir', bg='#F0F0F0', fg='#000000', command=lambda: self.insercao_12(2))
        self.botao_inserir_15.place(relx=0.85, rely=0.65, relwidth=0.0985, relheight=0.05)

        self.variavel_delta_o_pr_rel_ppra_texto = Label(self.aba_6, text='Δσₚᵣ,rel :', bg='#F0F0F0', fg='#000000')
        self.variavel_delta_o_pr_rel_ppra_texto.place(relx=0.825, rely=0.745, relwidth=0.0675, relheight=0.035)

        self.botao_calcular_7 = tk.Button(self.aba_6, text='Calcular', bg='#F0F0F0', fg='#000000', command=lambda: self.perda_por_relaxacao(1))
        self.botao_calcular_7.place(relx=0.85, rely=0.89, relwidth=0.0985, relheight=0.05)

    # Widgets Dinâmicos da Aba 6
    def aba_6_funcoes_destrutivas(self):

        # 1.0 Quadrante

        self.variavel_n_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[0], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_n_ppra.place(relx=0.078, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_ap_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[1], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ap_ppra.place(relx=0.254, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_p0_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[2], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_p0_ppra.place(relx=0.4415, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_Mg_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[3], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Mg_ppra.place(relx=0.6175, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_ep_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[4], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ep_ppra.place(relx=0.078, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_Ep_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[5], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Ep_ppra.place(relx=0.254, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_Ic_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[6], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Ic_ppra.place(relx=0.4415, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_Eci28_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[7], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Eci28_ppra.place(relx=0.6175, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_fptk_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[8], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_fptk_ppra.place(relx=0.078, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_t0_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[9], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_t0_ppra.place(relx=0.254, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_t_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[10], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_t_ppra.place(relx=0.4415, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_relaxacao_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[11], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_relaxacao_ppra.place(relx=0.6175, rely=0.6775, relwidth=0.0985, relheight=0.05)

        # 2.0 Quadrante

        self.variavel_w_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[12], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_w_ppra.place(relx=0.85, rely=0.12, relwidth=0.0985, relheight=0.05)

        self.variavel_delta_o_pr_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[13], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_delta_o_pr_ppra.place(relx=0.85, rely=0.2375, relwidth=0.0985, relheight=0.05)

        self.variavel_delta_o_p_cs_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[14], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_delta_o_p_cs_ppra.place(relx=0.85, rely=0.48, relwidth=0.0985, relheight=0.05)

        self.variavel_delta_o_pr_rel_ppra = Label(self.aba_6, text=self.valores_variaveis_ppra[15], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_delta_o_pr_rel_ppra.place(relx=0.85, rely=0.805, relwidth=0.0985, relheight=0.05)

    def aba_7_funcoes(self):

        # 1.0 Quadrante

        self.fundo_mg_0 = Label(self.aba_7, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_mg_0.place(relx=0.005, rely=0.011, relwidth=0.1865, relheight=0.98)

        self.fundo_mg_1 = Label(self.aba_7, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_mg_1.place(relx=0.018, rely=0.041, relwidth=0.163, relheight=0.3)
        
        self.fundo_mg_2 = Label(self.aba_7, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_mg_2.place(relx=0.018, rely=0.365, relwidth=0.163, relheight=0.6)

        self.texto_mg = Label(self.aba_7, text='PTMG', bg='#F0F0F0', fg='#000000')
        self.texto_mg.place(relx=0.03, rely=0.023, relwidth=0.05, relheight=0.04)
            
        self.texto_csr = Label(self.aba_7, text='Δσₚ,c+s+r', bg='#F0F0F0', fg='#000000')
        self.texto_csr.place(relx=0.058, rely=0.08, relwidth=0.08, relheight=0.04)
        
        self.botao_calcular_mg = tk.Button(self.aba_7, text='Calcular', bg='#F0F0F0', fg='#000000',
                                           command=self.perda_metodo_geral)
        self.botao_calcular_mg.place(relx=0.04, rely=0.25, relwidth=0.12, relheight=0.05)       

        self.texto_delta_cs = Label(self.aba_7, text='Δσₚ,c+s', bg='#F0F0F0', fg='#000000')
        self.texto_delta_cs.place(relx=0.058, rely=0.4, relwidth=0.08, relheight=0.04)

        self.texto_delta_rrel = Label(self.aba_7, text='Δσₚᵣ,rel', bg='#F0F0F0', fg='#000000')
        self.texto_delta_rrel.place(relx=0.058, rely=0.52, relwidth=0.08, relheight=0.04)

        self.variavel_mg = Entry(self.aba_7, text="")
        self.variavel_mg.place(relx=0.04, rely=0.68, relwidth=0.12, relheight=0.05)

        self.lista_variaveis_mg = ttk.Combobox(self.aba_7, values=['', 
                                                                   'Δσₚ,c+s', 
                                                                   'Δσₚᵣ,rel'])
        self.lista_variaveis_mg.place(relx=0.04, rely=0.78, relwidth=0.12, relheight=0.05)
        self.lista_variaveis_mg.current(0)

        self.botao_inserir_mg = tk.Button(self.aba_7, text='Inserir', bg='#F0F0F0', fg='#000000',
                                          command=lambda: self.insercao_13(0))
        self.botao_inserir_mg.place(relx=0.04, rely=0.88, relwidth=0.12, relheight=0.05)

        # 2.0 Quadrante

        self.fundo_ps_0 = Label(self.aba_7, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_ps_0.place(relx=0.208, rely=0.011, relwidth=0.7835, relheight=0.98)

        self.fundo_ps_1 = Label(self.aba_7, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ps_1.place(relx=0.219, rely=0.041, relwidth=0.759, relheight=0.78)

        self.fundo_ps_2 = Label(self.aba_7, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ps_2.place(relx=0.219, rely=0.8485, relwidth=0.3, relheight=0.12)

        self.fundo_ps_3 = Label(self.aba_7, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_ps_3.place(relx=0.54, rely=0.8485, relwidth=0.44, relheight=0.12)

        self.texto_ps = Label(self.aba_7, text='PTPS', bg='#F0F0F0', fg='#000000')
        self.texto_ps.place(relx=0.232, rely=0.023, relwidth=0.042, relheight=0.04)

        self.variavel_Ac_ps_texto = Label(self.aba_7, text='Ac :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ac_ps_texto.place(relx=0.25, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_Ap_ps_texto = Label(self.aba_7, text='Aₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ap_ps_texto.place(relx=0.40, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_ecs_ps_texto = Label(self.aba_7, text='εcs :', bg='#F0F0F0', fg='#000000')
        self.variavel_ecs_ps_texto.place(relx=0.55, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_ep_ps_texto = Label(self.aba_7, text='eₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_ep_ps_texto.place(relx=0.70, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_Ep_ps_texto = Label(self.aba_7, text='Eₚ :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ep_ps_texto.place(relx=0.85, rely=0.125, relwidth=0.03, relheight=0.05)

        self.variavel_fck_ps_texto = Label(self.aba_7, text='fck :', bg='#F0F0F0', fg='#000000')
        self.variavel_fck_ps_texto.place(relx=0.325, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_Ic_ps_texto = Label(self.aba_7, text='Ic :', bg='#F0F0F0', fg='#000000')
        self.variavel_Ic_ps_texto.place(relx=0.475, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_Mg_ps_texto = Label(self.aba_7, text='Mg :', bg='#F0F0F0', fg='#000000')
        self.variavel_Mg_ps_texto.place(relx=0.625, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_y_ps_texto = Label(self.aba_7, text='φ :', bg='#F0F0F0', fg='#000000')
        self.variavel_y_ps_texto.place(relx=0.775, rely=0.3625, relwidth=0.03, relheight=0.05)

        self.variavel_w1000_ps_texto = Label(self.aba_7, text='Ψ₁₀₀₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_w1000_ps_texto.place(relx=0.25, rely=0.6, relwidth=0.04, relheight=0.05)

        self.variavel_P0_ps_texto = Label(self.aba_7, text='P₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_P0_ps_texto.place(relx=0.40, rely=0.6, relwidth=0.03, relheight=0.05)

        self.variavel_t_ps_texto = Label(self.aba_7, text='t :', bg='#F0F0F0', fg='#000000')
        self.variavel_t_ps_texto.place(relx=0.55, rely=0.6, relwidth=0.03, relheight=0.05)

        self.variavel_t0_ps_texto = Label(self.aba_7, text='t₀ :', bg='#F0F0F0', fg='#000000')
        self.variavel_t0_ps_texto.place(relx=0.70, rely=0.6, relwidth=0.03, relheight=0.05)

        self.variavel_ocpog_ps_texto = Label(self.aba_7, text='σc,pog :', bg='#F0F0F0', fg='#000000')
        self.variavel_ocpog_ps_texto.place(relx=0.85, rely=0.6, relwidth=0.06, relheight=0.05)

        self.texto_delta_op_ps = Label(self.aba_7, text='Δσₚ(t,t₀)', bg='#F0F0F0', fg='#000000')
        self.texto_delta_op_ps.place(relx=0.24, rely=0.88, relwidth=0.058, relheight=0.04)

        self.botao_calcular_ps = tk.Button(self.aba_7, text='Calcular', bg='#F0F0F0', fg='#000000',
                                            command=self.perda_processo_simplificado)
        self.botao_calcular_ps.place(relx=0.42, rely=0.88, relwidth=0.08, relheight=0.05)

        self.lista_variaveis_ps = ttk.Combobox(self.aba_7, values=['', 'Ac', 'Aₚ', 'εcs',
                                                                   'eₚ', 'fck', 'Ic', 'Mg',
                                                                   'φ', 'Ψ₁₀₀₀', 'P₀', 
                                                                   't ≠ ∞', 't = ∞', 't₀',
                                                                   'σc,pog = +', 'σc,pog = -'])
        self.lista_variaveis_ps.place(relx=0.56, rely=0.88, relwidth=0.16, relheight=0.05)
        self.lista_variaveis_ps.current(0)

        self.variavel_ps = Entry(self.aba_7, text="")
        self.variavel_ps.place(relx=0.73, rely=0.88, relwidth=0.135, relheight=0.05)

        self.botao_inserir_ps = tk.Button(self.aba_7, text='Inserir', bg='#F0F0F0', fg='#000000',
                                          command=lambda: self.insercao_13(1))
        self.botao_inserir_ps.place(relx=0.878, rely=0.88, relwidth=0.08, relheight=0.05)

    def aba_7_funcoes_destrutivas(self):

        # 1.0 Quadrante

        self.variavel_delta_csr = Label(self.aba_7, text=self.valores_de_mg[0], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_delta_csr.place(relx=0.04, rely=0.16, relwidth=0.12, relheight=0.05)

        self.delta_cs = Label(self.aba_7, text=self.valores_de_mg[1], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.delta_cs.place(relx=0.04, rely=0.46, relwidth=0.12, relheight=0.05)

        self.delta_rrel = Label(self.aba_7, text=self.valores_de_mg[2], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.delta_rrel.place(relx=0.04, rely=0.58, relwidth=0.12, relheight=0.05)

        # 2.0 Quadrante

        self.variavel_Ac_ps = Label(self.aba_7, text=self.valores_de_ps[0], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Ac_ps.place(relx=0.25, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_Ap_ps = Label(self.aba_7, text=self.valores_de_ps[1], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Ap_ps.place(relx=0.40, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_ecs_ps = Label(self.aba_7, text=self.valores_de_ps[2], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ecs_ps.place(relx=0.55, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_ep_ps = Label(self.aba_7, text=self.valores_de_ps[3], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ep_ps.place(relx=0.70, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_Ep_ps = Label(self.aba_7, text=self.valores_de_ps[4], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Ep_ps.place(relx=0.85, rely=0.2025, relwidth=0.0985, relheight=0.05)

        self.variavel_fck_ps = Label(self.aba_7, text=self.valores_de_ps[5], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_fck_ps.place(relx=0.325, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_Ic_ps = Label(self.aba_7, text=self.valores_de_ps[6], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Ic_ps.place(relx=0.475, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_Mg_ps = Label(self.aba_7, text=self.valores_de_ps[7], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_Mg_ps.place(relx=0.625, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_y_ps = Label(self.aba_7, text=self.valores_de_ps[8], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_y_ps.place(relx=0.775, rely=0.44, relwidth=0.0985, relheight=0.05)

        self.variavel_w1000_ps = Label(self.aba_7, text=self.valores_de_ps[9], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_w1000_ps.place(relx=0.25, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_P0_ps = Label(self.aba_7, text=self.valores_de_ps[10], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_P0_ps.place(relx=0.40, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_t_ps = Label(self.aba_7, text=self.valores_de_ps[11], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_t_ps.place(relx=0.55, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_t0_ps = Label(self.aba_7, text=self.valores_de_ps[12], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_t0_ps.place(relx=0.70, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_ocpog_ps = Label(self.aba_7, text=self.valores_de_ps[13], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_ocpog_ps.place(relx=0.85, rely=0.6775, relwidth=0.0985, relheight=0.05)

        self.variavel_delta_op_ps = Label(self.aba_7, text=self.valores_de_ps[14], relief="sunken", bg='#FFFFFF', fg='#000000')
        self.variavel_delta_op_ps.place(relx=0.31, rely=0.88, relwidth=0.1, relheight=0.05)

programa()
