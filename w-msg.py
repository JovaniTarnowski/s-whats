# =====================================================================================
# Handles "Guia de fundos" with pandas them format FUnd`s name to put on GUI.
# Ver0.1.2  - Moved the short link to DB,
#           -
# Bugs:
    #install: pip install --default-timeout=100 future
# =====================================================================================

import PySimpleGUI as sg
import pandas as pd
from easygui import *

""" Read DB from Drive"""
df = pd.read_csv(
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vRAAEPTLdtgK6tmAAOffsYt69zSBtNJpGSMWe6-Jaz6Zh-YJrGtZuEechkkT_6BIY4Ou6Hr0p2CTgi2/pub?output=csv")

df = df.set_index('FUNDO', drop=False)
date = "08/09/2019"
# =====================================================================================
# User Interface
# =====================================================================================

msg = """-- Selecione os fundos e CLIQUE OK 

-- COPIE e COLE o Texto antes de fechar a Janela

-- Rentabilidade fundos Atualizados dia {0}""".format(date)

title = "Opções de investimento"

choices = []

for fundo in df['FUNDO']:
    choices.append(fundo)

choice = multchoicebox(msg, title, choices)

for fundo in list(choice):

    df0 = df.CNPJ[fundo]
    df1 = df.FUNDO[fundo]
    df2 = df['Aplicação Inicial'][fundo]
    df3 = df.Desde_Início[fundo]
    df4 = int(df['Liquidez_total_(CotizaçãoLiquidação)'][fundo])
    df5 = df.Tributação[fundo]
    df6 = df.CVM[fundo]
    df7 = str(df.Lamina_fundo[fundo])
    df8 = df.Acima_IBOV[fundo]

    if df7 == "nan":

        if df5 == 'Renda Variável':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: IBOV + {4}% (início)
*IR*: incidirá no momento do resgate, à alíquota de 15/% sobre o lucro obtido.
*Liquidez*: D+{1}
*Categoria*: {2}
*Aplicação Miníma*: {3}""".format(df1, df4, df6, df2, df8), title='Verificar', yes_no=True, size=(80, 10))

        elif df5 == 'Debêntures Incentivadas':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: isento 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicação Miníma*: {4}""".format(df1, df3, df4, df6, df2), title='Verificar', yes_no=True, size=(80, 10))

        else:
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: respeita a tabela regressiva de renda fixa (antecipação via come-cotas) 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicação Miníma*: {4}""".format(df1, df3, df4, df6, df2), title='Verificar', yes_no=True, size=(80, 10))

    elif df1 == 'Opportunity Total FIC de FIM':
        sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: incidirá no momento do resgate, à alíquota de 15/% sobre o lucro obtido. 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicação Miníma*: {4}
*Mais informações do fundo*: {5} """.format(df1, df3, df4, df6, df2, df7), title='Verificar', yes_no=True, size=(80, 10))

    else:
        if df5 == 'Renda Variável':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: IBOV + {5}% (início)
*IR*: incidirá no momento do resgate, à alíquota de 15/% sobre o lucro obtido.
*Liquidez*: D+{1}
*Categoria*: {2}
*Aplicação Miníma*: {3}
*Mais informações do fundo*: {4} """.format(df1, df4, df6, df2, df7, df8), title='Verificar', yes_no=True, size=(80, 10))

        elif df5 == 'Debêntures Incentivadas':
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: isento
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicação Miníma*: {4}
*Mais informações do fundo*: {5} """.format(df1, df3, df4, df6, df2, df7), title='Verificar', yes_no=True, size=(80, 10))

        else:
            sg.PopupScrolled(
"""Fundo: *{0}* 
*Rentabilidade*: {1} CDI (início)
*IR*: respeita a tabela regressiva de renda fixa (antecipação via come-cotas) 
*Liquidez*: D+{2}
*Categoria*: {3}
*Aplicação Miníma*: {4}
*Mais informações do fundo*: {5} """.format(df1, df3, df4, df6, df2, df7), title='Verificar', yes_no=True, size=(80, 10))