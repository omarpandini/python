from sys import displayhook
import pandas as pd

df = pd.read_excel('Vendas - Dez.xlsx')

print(df)

quantidade = df['Quantidade'].sum()

print('Quantidade total: '+str(quantidade))
