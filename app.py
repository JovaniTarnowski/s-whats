import pandas as pd
import pandas_datareader as web

dfDb = pd.read_csv(
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vRAAEPTLdtgK6tmAAOffsYt69zSBtNJpGSMWe6-Jaz6Zh-YJrGtZuEechkkT_6BIY4Ou6Hr0p2CTgi2/pub?output=csv")
dfDb = dfDb.drop(['CVM',
                  'Tributação',
                  'Aplicação Inicial',
                  'Liquidez_total_(CotizaçãoLiquidação)',
                  'Benchmark',
                  'CNPJ',
                  'Lamina_fundo',
                  ], axis=1)
# dfDb.head()

symbols = []

for dataDinicio in dfDb['Data de Início']:
    r = web.DataReader("^BVSP", "yahoo", dataDinicio)
    # r['Symbol'] = "^BVSP"
    print(r)
    symbols.append(r)

print(symbols)
# for f in dfDb:
#     print(f)
# start = dfDb['Data de Início']
