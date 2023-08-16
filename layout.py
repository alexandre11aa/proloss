print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from perda_por_atrito import atrito
from perda_por_acomodacao_de_ancoragem import acomodacao_de_ancoragem

root = Tk()

class funcoes():
            
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

            self.quadro_3_itens = atrito(self.variaveis_1[:4],
                                         dist,
                                         situ,
                                         altu,
                                         self.variaveis_1[4])[0]
            
            self.y_1, self.x_2, self.y_2  = [altu, self.x_1, self.quadro_3_itens]

        self.destruicao_1()

    def perda_por_acomodacao_de_ancoragem(self):

        self.resultados_de_ac_de_anc = acomodacao_de_ancoragem(self.quadro_4_itens,
                                                               self.variaveis_2[0],
                                                               self.variaveis_2[1],
                                                               self.variaveis_2[3],
                                                               self.variaveis_2[4],
                                                               self.variaveis_2[5],
                                                               self.variaveis_2[2],
                                                               self.variaveis_2[6],
                                                               self.variaveis_2[7])
                
        self.aplicar_1()

    def aplicar_1(self):

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

    # Destruições
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

    def exemplo_1_0(self):

        self.quadro_1_itens = [('A', 0.11), ('B', 0.07), ('C', 0.16), ('D', 0.18), ('E', 0.15), ('F', 0.04), ('G', 0.11)]
        self.quadro_2_itens = [(2.8, 'Curvo'), (3.5, 'Curvo'), (0.7, 'Curvo'), (0.9, 'Curvo'), (4.5, 'Curvo'), (3.6, 'Curvo')]

        self.variaveis_1 = [3, 1.4, 2100, 1890, 0.05]

        self.destruicao_1()

    def exemplo_1_1(self):
        
        self.quadro_1_itens = [('A', 1.245), ('B', 1.07), ('C', 0.175), ('D', 0.175), ('E', 1.07), ('F', 1.245)]
        self.quadro_2_itens = [(0.8, 'Reto'), (8.43, 'Curvo'), (2.04, 'Reto'), (8.43, 'Curvo'), (0.8, 'Reto')]

        self.variaveis_1 = [12, 1.014, 1900, 1710, 0.2]

        self.destruicao_1()

    def exemplo_2(self):
        self.quadro_4_itens = [3.5, 2]

        self.variaveis_2 = [5.5, 9.5, 200, 1177.68, 1093.37, 1084.66, 1.4, 6]

        self.destruicao_2()

    # Inserções
    def insercao_1(self):
        self.quadro_1_itens.append((self.ponto.get(), float(self.altura.get())))

        self.destruicao_1()

    def insercao_2(self):
        self.quadro_2_itens.append((float(self.trecho.get()), self.lista_de_tipo.get()))

        print(self.quadro_2_itens)

        self.destruicao_1()

    def insercao_3(self):
        if str(self.lista_de_links.get()) != "":
            lista_excel = np.asarray(pd.read_excel(str(self.lista_de_links.get()), index_col=None, header=None))

            for i in range(len(lista_excel)):
                self.quadro_1_itens.append((lista_excel[i][0], lista_excel[i][1]))

            for i in range(len(lista_excel) - 1):
                self.quadro_2_itens.append((lista_excel[i][2], lista_excel[i][3]))

        self.destruicao_1()

    def insercao_4(self):
        decisao = self.lista_variaveis_1.get()

        if decisao == 'μ':
            self.variaveis_1[4] = self.entrada_das_variaveis_1.get()
        
        elif decisao == 'fptk (MPa)':
            self.variaveis_1[2] = self.entrada_das_variaveis_1.get()

        elif decisao == 'fpyk (MPa)':
            self.variaveis_1[3] = self.entrada_das_variaveis_1.get()

        elif decisao == 'Ap⁽⁰⁾ (cm² / Cord.)':
            self.variaveis_1[1] = self.entrada_das_variaveis_1.get()

        elif decisao == 'Nº de Cordoalhas':
            self.variaveis_1[0] = self.entrada_das_variaveis_1.get()

        self.destruicao_1()

    def insercao_5(self):
        self.quadro_4_itens.append((float(self.valor_de_delta_w.get())))

        self.quadro_4_itens.sort(reverse=True)

        self.destruicao_2()

    def insercao_6(self):
        decisao = self.lista_de_variaveis_2.get()

        if decisao == 'a (m)':
            self.variaveis_2[0] = float(self.entrada_das_variaveis_2.get())
        
        elif decisao == 'l/2 (m)':
            self.variaveis_2[1] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Ep (GPa)':
            self.variaveis_2[2] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Pi (kN/Cabo)':
            self.variaveis_2[3] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'P₀(x = a) (kN)':
            self.variaveis_2[4] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'P₀(x = l/2) (kN)':
            self.variaveis_2[5] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Ap⁽⁰⁾ (cm²)':
            self.variaveis_2[6] = float(self.entrada_das_variaveis_2.get())

        elif decisao == 'Nº de Cord.':
            self.variaveis_2[7] = float(self.entrada_das_variaveis_2.get())

        self.destruicao_2()

    # Apagando
    def apagando_1(self):
        selecionador = self.quadro_1.selection()[0]

        self.quadro_1.delete(selecionador)

        del (self.quadro_1_itens[int(selecionador)])

        self.destruicao_1()

    def apagando_2(self):
        selecionador = self.quadro_2.selection()[0]

        self.quadro_2.delete(selecionador)

        del (self.quadro_2_itens[int(selecionador)])

        self.destruicao_1()

    def apagando_3(self):
        selecionador = self.quadro_4.selection()[0]

        self.quadro_4.delete(selecionador)

        del (self.quadro_4_itens[int(selecionador)])

        self.destruicao_2()

    # Procurar
    def procurar_1(self):
        arquivo = askopenfilename(filetypes=[('Arquivos do Excel', '*.xlsx')])

        self.links_1.append(arquivo)

        self.destruicao_1()

    # Menu de Opções
    def menus(self):
        barra_de_menu = Menu(self.root)
        root.config(menu=barra_de_menu)

        menu_de_arquivos = Menu(barra_de_menu)
        barra_de_menu.add_cascade(label='Arquivos', menu = menu_de_arquivos)
        menu_de_arquivos.add_command(label='Limpar', command=self.limpar)
        menu_de_arquivos.add_command(label='Reiniciar', command=self.reiniciar)
        menu_de_arquivos.add_command(label='Sair', command=self.sair)

        menu_de_exemplos = Menu(barra_de_menu)
        barra_de_menu.add_cascade(label='Exemplos', menu = menu_de_exemplos)
        menu_de_exemplos.add_command(label='Exemplo 1.0', command=self.exemplo_1_0)
        menu_de_exemplos.add_command(label='Exemplo 1.1', command=self.exemplo_1_1)
        menu_de_exemplos.add_command(label='Exemplo 2.0', command=self.exemplo_2)

    # Opção Limpar
    def limpar(self):
        self.quadro_1_itens = []
        self.quadro_2_itens = []
        self.quadro_3_itens = []

        self.x_1 = []
        self.y_1 = []

        self.x_2 = []
        self.y_2 = []

        self.links_1 = []

        self.variaveis = ['', '', '', '', '']

        self.destruicao_1()

    # Opção Reiniciar
    def reiniciar(self):
        self.__init__()

    # Opção Sair
    def sair(self):
        print("\nSaindo do programa...")
        quit()

class programa(funcoes):

    # Inicialização e Variáveis
    def __init__(self):

        # Variáveis de Perda por Atrito

        self.quadro_1_itens = []
        self.quadro_2_itens = []

        self.quadro_3_itens = []

        self.x_1 = []
        self.y_1 = []

        self.x_2 = []
        self.y_2 = []

        self.links_1 = []

        self.variaveis_1 = ['','','','','']

        # Variáveis de Perda por Acomodação de Ancoragem

        self.quadro_4_itens = []

        self.variaveis_2 = ['','','','','','','','']

        self.resultados_1 = ['','','','','','','']

        # Funções

        self.root = root
        self.tela()
        self.frame_tela()
        self.menus()
        self.apps_da_pagina_1()
        root.mainloop()

    # Configurações da Tela
    def tela(self):
        self.root.title("Cálculo de Perdas de Protensão")
        self.root.configure(background='#F0F0F0')
        self.root.geometry('750x500')
        self.root.resizable(False, False)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=750, height=500)
        self.root.protocol("WM_DELETE_WINDOW", self.sair)

    # Configurações do Frame da Tela
    def frame_tela(self):
        self.frame = Frame(self.root, bd=0.1, bg='#FFFFFF',
                           highlightbackground='#F0F0F0', highlightthickness=2)
        self.frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.98)

    # Aplicativos da Página 1
    def apps_da_pagina_1(self):

        # Configurações de Abas

        self.abas = ttk.Notebook(self.frame)

        self.aba_1 = Frame(self.abas)
        self.aba_1.configure(background='#F0F0F0')
        self.abas.add(self.aba_1, text=" Atrito ")

        self.aba_2 = Frame(self.abas)
        self.aba_2.configure(background='#F0F0F0')
        self.abas.add(self.aba_2, text=" Ancoragem ")

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.aba_1_funcoes()
        self.aba_1_funcoes_destrutivas()

        self.aba_2_funcoes()
        self.aba_2_funcoes_destrutivas()

    # Widgets Estáticos da Aba 1 da Página 1
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

        self.botao_apagar_1 = tk.Button(self.aba_1, text='Apagar', bg='#F0F0F0', fg='#000000', command=self.apagando_1)
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

        self.botao_apagar_2 = tk.Button(self.aba_1, text='Apagar', bg='#F0F0F0', fg='#000000', command=self.apagando_2)
        self.botao_apagar_2.place(relx=0.34, rely=0.89, relwidth=0.08, relheight=0.05)

        # 3.0 Quadrante:

        self.fundo_do_quadro_3 = Label(self.aba_1, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_3.place(relx=0.455, rely=0.01, relwidth=0.137, relheight=0.98)

        self.fundo_de_resultados_1 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_1.place(relx=0.465, rely=0.04, relwidth=0.115, relheight=0.58)

        self.resultados = Label(self.aba_1, text='Força P0 :', bg='#F0F0F0', fg='#000000')
        self.resultados.place(relx=0.475, rely=0.02, relwidth=0.07, relheight=0.035)

        self.fundo_de_resultados_2 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_resultados_2.place(relx=0.465, rely=0.645, relwidth=0.115, relheight=0.325)

        self.botao_inserir_3 = tk.Button(self.aba_1, text='Procurar', bg='#F0F0F0', fg='#000000',
                                         command=self.procurar_1)
        self.botao_inserir_3.place(relx=0.4825, rely=0.7425, relwidth=0.08, relheight=0.05)

        self.botao_inserir_3 = tk.Button(self.aba_1, text='Inserir', bg='#F0F0F0', fg='#000000',
                                         command=self.insercao_3)
        self.botao_inserir_3.place(relx=0.4825, rely=0.8175, relwidth=0.08, relheight=0.05)

        self.botao_calcular_1 = tk.Button(self.aba_1, text='Calcular', bg='#F0F0F0', fg='#000000', 
                                          command=self.perda_por_atrito)
        self.botao_calcular_1.place(relx=0.4825, rely=0.89, relwidth=0.08, relheight=0.05)

        # 4.0 Quadrante:

        self.fundo_do_quadro_4 = Label(self.aba_1, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_4.place(relx=0.605, rely=0.01, relwidth=0.388, relheight=0.98)

        self.fundo_de_variaveis_1 = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_1.place(relx=0.615, rely=0.04, relwidth=0.368, relheight=0.23)

        self.fptk_texto = Label(self.aba_1, text='fptk :', bg='#F0F0F0', fg='#000000')
        self.fptk_texto.place(relx=0.7925, rely=0.15, relwidth=0.038, relheight=0.05)

        self.fpyk_texto = Label(self.aba_1, text='fpyk :', bg='#F0F0F0', fg='#000000')
        self.fpyk_texto.place(relx=0.89, rely=0.15, relwidth=0.038, relheight=0.05)

        self.ncd_texto = Label(self.aba_1, text='Nº Cd. :', bg='#F0F0F0', fg='#000000')
        self.ncd_texto.place(relx=0.63, rely=0.156, relwidth=0.058, relheight=0.05)

        self.area_texto = Label(self.aba_1, text='Ap⁽⁰⁾ :', bg='#F0F0F0', fg='#000000')
        self.area_texto.place(relx=0.63, rely=0.203, relwidth=0.048, relheight=0.05)

        self.u_texto = Label(self.aba_1, text='μ :', bg='#F0F0F0', fg='#000000')
        self.u_texto.place(relx=0.63, rely=0.108, relwidth=0.02, relheight=0.05)

        self.entrada_das_variaveis_1 = Entry(self.aba_1, text="")
        self.entrada_das_variaveis_1.place(relx=0.7925, rely=0.058, relwidth=0.076, relheight=0.046)

        self.botao_inserir_4 = tk.Button(self.aba_1, text='Inserir', bg='#F0F0F0', fg='#000000', command=self.insercao_4)
        self.botao_inserir_4.place(relx=0.8875, rely=0.056, relwidth=0.08, relheight=0.05)

        self.lista_variaveis_1 = ttk.Combobox(self.aba_1, values=['', 
                                                                  'μ', 
                                                                  'fptk (MPa)', 
                                                                  'fpyk (MPa)', 
                                                                  'Ap⁽⁰⁾ (cm² / Cord.)', 
                                                                  'Nº de Cordoalhas'])
        self.lista_variaveis_1.place(relx=0.63, rely=0.056, relwidth=0.145, relheight=0.05)
        self.lista_variaveis_1.current(0)

        # 5.0 Quadrante:

        self.fundo_de_duracoes = Label(self.aba_1, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_duracoes.place(relx=0.615, rely=0.3, relwidth=0.368, relheight=0.67)
        
    # Widgets Dinâmicos da Aba 1 da Página 1
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

        self.quadro_3.place(relx=0.475, rely=0.0665, relwidth=0.075, relheight=0.535)

        self.y_scroll_3 = ttk.Scrollbar(self.aba_1, orient=tk.VERTICAL, command=self.quadro_3.yview)

        self.quadro_3['yscroll'] = self.y_scroll_3.set

        self.y_scroll_3.place(relx=0.55, rely=0.0665, relwidth=0.025, relheight=0.535)

        for i in range(len(self.quadro_3_itens)):
            self.quadro_3.insert(parent='', index=i, iid=i, text='', values=(str(self.quadro_3_itens[i])))

        self.lista_de_links = ttk.Combobox(self.aba_1, values=self.links_1)
        self.lista_de_links.place(relx=0.48, rely=0.675, relwidth=0.085, relheight=0.045)

        # 4.0 Quadrante:

        self.constante_u = Label(self.aba_1, text=str(self.variaveis_1[4]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.constante_u.place(relx=0.695, rely=0.115, relwidth=0.08, relheight=0.04)

        self.ncd = Label(self.aba_1, text=str(self.variaveis_1[0]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.ncd.place(relx=0.695, rely=0.163, relwidth=0.08, relheight=0.04)

        self.area = Label(self.aba_1, text=str(self.variaveis_1[1]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.area.place(relx=0.695, rely=0.21, relwidth=0.08, relheight=0.04)   

        self.fptk = Label(self.aba_1, text=str(self.variaveis_1[2]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.fptk.place(relx=0.7925, rely=0.21, relwidth=0.08, relheight=0.04)

        self.fpyk = Label(self.aba_1, text=str(self.variaveis_1[3]), relief="sunken", bg='#FFFFFF', fg='#000000')
        self.fpyk.place(relx=0.89, rely=0.21, relwidth=0.08, relheight=0.04)

        # 5.0 Quadrante:

        fig, ax = plt.subplots(2, 1, figsize=(2.66, 3.035))

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

        self.canvas.get_tk_widget().pack(side=RIGHT, anchor=SW, padx=15.25, pady=17)

    # Widgets Estáticos da Aba 1 da Página 1
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
                                         command=self.apagando_3)
        self.botao_apagar_3.place(relx=0.0325, rely=0.8175, relwidth=0.08, relheight=0.05)

        self.botao_calcular_2 = tk.Button(self.aba_2, text='Calcular', bg='#F0F0F0', fg='#000000', 
                                          command=self.perda_por_acomodacao_de_ancoragem)
        self.botao_calcular_2.place(relx=0.0325, rely=0.89, relwidth=0.08, relheight=0.05)

        # 2.0 Quadrante:

        self.fundo_do_quadro_5 = Label(self.aba_2, text='', relief="raised", bg='#F0F0F0', fg='#800000')
        self.fundo_do_quadro_5.place(relx=0.155, rely=0.01, relwidth=0.454, relheight=0.98)

        self.fundo_de_variaveis_2 = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_2.place(relx=0.165, rely=0.04, relwidth=0.432, relheight=0.78)

        self.fundo_de_variaveis_3 = Label(self.aba_2, text='', relief="groove", bg='#F0F0F0', fg='#800000')
        self.fundo_de_variaveis_3.place(relx=0.165, rely=0.845, relwidth=0.432, relheight=0.125)

        self.comprimento_a_nome = Label(self.aba_2, text='a :', bg='#F0F0F0', fg='#000000')
        self.comprimento_a_nome.place(relx=0.23, rely=0.1, relwidth=0.02, relheight=0.035)

        self.comprimento_meio_l_nome = Label(self.aba_2, text='l/2 :', bg='#F0F0F0', fg='#000000')
        self.comprimento_meio_l_nome.place(relx=0.41, rely=0.1, relwidth=0.03, relheight=0.035)

        self.variavel_constante_E_nome = Label(self.aba_2, text='Ep :', bg='#F0F0F0', fg='#000000')
        self.variavel_constante_E_nome.place(relx=0.23, rely=0.27, relwidth=0.03, relheight=0.035)

        self.variavel_p_i_nome = Label(self.aba_2, text='Pi :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_i_nome.place(relx=0.41, rely=0.27, relwidth=0.028, relheight=0.035)

        self.variavel_p_a_nome = Label(self.aba_2, text='P₀(x = a) :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_a_nome.place(relx=0.23, rely=0.44, relwidth=0.075, relheight=0.035)

        self.variavel_p_meio_l_nome = Label(self.aba_2, text='P₀(x = l/2) :', bg='#F0F0F0', fg='#000000')
        self.variavel_p_meio_l_nome.place(relx=0.41, rely=0.44, relwidth=0.085, relheight=0.035)

        self.area_p_nome = Label(self.aba_2, text='Ap⁽⁰⁾ :', bg='#F0F0F0', fg='#000000')
        self.area_p_nome.place(relx=0.23, rely=0.61, relwidth=0.048, relheight=0.035)

        self.ncd_texto_2 = Label(self.aba_2, text='Nº de Cord. :', bg='#F0F0F0', fg='#000000')
        self.ncd_texto_2.place(relx=0.41, rely=0.61, relwidth=0.1, relheight=0.035)
        
        self.lista_de_variaveis_2 = ttk.Combobox(self.aba_2, values=['',
                                                                     'a (m)', 
                                                                     'l/2 (m)', 
                                                                     'Ep (GPa)', 
                                                                     'Pi (kN/Cabo)', 
                                                                     'P₀(x = a) (kN)', 
                                                                     'P₀(x = l/2) (kN)', 
                                                                     'Ap⁽⁰⁾ (cm²)',
                                                                     'Nº de Cord.'])
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

    # Widgets Dinâmicos da Aba 1 da Página 1
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

        self.lista_de_delta_w_para_exibir = ttk.Combobox(self.aba_2, values=[('Δw = ' + str(i)) for i in self.quadro_4_itens])
        self.lista_de_delta_w_para_exibir.place(relx=0.67, rely=0.075, relwidth=0.14, relheight=0.05)

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

programa()
