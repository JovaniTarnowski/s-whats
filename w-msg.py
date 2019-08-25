# =====================================================================================

# Handles "Guia de fundos" with pandas them format FUnd`s name to put on GUI.

import PySimpleGUI as sg
import pandas as pd
# =====================================================================================
from easygui import *

# from io import BytesIO
# import requests

# asdalsd


df = pd.read_csv(
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vRAAEPTLdtgK6tmAAOffsYt69zSBtNJpGSMWe6-Jaz6Zh-YJrGtZuEechkkT_6BIY4Ou6Hr0p2CTgi2/pub?output=csv")

df = df.set_index('FUNDO', drop=False)
# df = df[df.Tributação != 'Renda Variável']

choices = []
for fundo in df['FUNDO']:
    choices.append(fundo)

# =====================================================================================

# UI Select fund`s name

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

    if df5 == 'Renda Variável':
        sg.PopupScrolled(
"""Fundo: *{0}*
*Rentabilidade*: {1} IBOV (início)
*IR*: incidirá no momento do resgate, à alíquota de 15/% sobre o lucro obtido.
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicacao Minima*: {4}""".format(df1, df3, df4, df6, df2),
            title='Verificar', yes_no=True)

    else:
        sg.PopupScrolled(
"""Fundo: *{0}*
*Rentabilidade*: {1} CDI (início)
*IR*: respeita a tabela regressiva de renda fixa (antecipação via come-cotas) 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicacao Minima*: {4}""".format(df1, df3, df4, df6, df2),
            title='Verificar', yes_no=True)

# =====================================================================================

# Mais de um Fundo

# =====================================================================================


# for fundo in list(choice):
#     # fundo_info = []
#     df0 = df.CNPJ[fundo]
#     df1 = df.FUNDO[fundo]
#     df2 = df['Aplicação Inicial'][fundo]
#     df3 = df.Desde_Início[fundo]
#     df4 = df['Liquidez_total_(CotizaçãoLiquidação)'][fundo]
#     df5 = df.Tributação[fundo]
#     df6 = df.CVM[fundo]

# sg.PopupScrolled(
# """Fundo: *{0}*
# *Rentabilidade*: {1} CDI (início)
# *IR*: respeita a tabela regressiva de renda fixa (antecipação via come-cotas)
# *Liquidez*: D+{2}
# *Categoria*: {3}
# *Aplicacao Minima*: {4}""".format(df1, df3, df4, df6, df2),
# title='Verificar', yes_no=True)

