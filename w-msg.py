# =====================================================================================

# Handles "Guia de fundos" with pandas them format FUnd`s name to put on GUI.

# =====================================================================================

import PySimpleGUI as sg
import pandas as pd
from easygui import *
import pyshorteners
from pyshorteners import Shorteners


df = pd.read_csv(
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vRAAEPTLdtgK6tmAAOffsYt69zSBtNJpGSMWe6-Jaz6Zh-YJrGtZuEechkkT_6BIY4Ou6Hr0p2CTgi2/pub?output=csv")

df = df.set_index('FUNDO', drop=False)

choices = []

for fundo in df['FUNDO']:
    choices.append(fundo)

# =====================================================================================

# User Interface

# =====================================================================================

msg = "Selecione os fundos"
title = "Opcoes de investimento"

choice = multchoicebox(msg, title, choices)

for fundo in list(choice):

    df0 = df.CNPJ[fundo]
    df1 = df.FUNDO[fundo]
    df2 = df['Aplicação Inicial'][fundo]
    df3 = df.Desde_Início[fundo]
    df4 = df['Liquidez_total_(CotizaçãoLiquidação)'][fundo]
    df5 = df.Tributação[fundo]
    df6 = df.CVM[fundo]
    df7 = str(df.Lamina_fundo[fundo])

    s = pyshorteners.Shortener(Shorteners.TINYURL)

    if "https://institucional.xpi.com.br/downloads/xpgestao/Caracteristica" not in df7:

        if df5 == 'Renda Variável':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: IBOV + X (início)
*IR*: incidirá no momento do resgate, à alíquota de 15/% sobre o lucro obtido.
*Liquidez*: D+{1}
*Categoria*: {2}
*Aplicacao Minima*: {3}""".format(df1, df4, df6, df2), title='Verificar', yes_no=True)

        elif df5 == 'Debêntures Incentivadas':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: isento 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicacao Minima*: {4}""".format(df1, df3, df4, df6, df2), title='Verificar', yes_no=True)

        else:
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: respeita a tabela regressiva de renda fixa (antecipação via come-cotas) 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicacao Minima*: {4}""".format(df1, df3, df4, df6, df2), title='Verificar', yes_no=True)

    else:
        df7 = s.short(df7)


        if df5 == 'Renda Variável':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: IBOV + X (início)
*IR*: incidirá no momento do resgate, à alíquota de 15/% sobre o lucro obtido.
*Liquidez*: D+{1}
*Categoria*: {2}
*Aplicacao Minima*: {3}
*Mais informacoes do fundo*: {4} """.format(df1, df4, df6, df2, df7), title='Verificar', yes_no=True)

        elif df5 == 'Debêntures Incentivadas':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: isento
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicacao Minima*: {4}
*Mais informacoes do fundo*: {5} """.format(df1, df3, df4, df6, df2, df7), title='Verificar', yes_no=True)

        else:
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: respeita a tabela regressiva de renda fixa (antecipação via come-cotas) 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicacao Minima*: {4}
*Mais informacoes do fundo*: {5} """.format(df1, df3, df4, df6, df2, df7), title='Verificar', yes_no=True)


# =====================================================================================

# Bugs:
    #install: pip install --default-timeout=100 future

# =====================================================================================