import pandas as pd
from pandas import read_csv


# Analfabetos funcionais por região : 
# Nomeando as regiões:
regi = ['Norte','Nordeste','Centro-Oeste','Sudeste','Sul']
df_regi = pd.DataFrame(regi, columns=['Regiao'])

# os códigos UF são: 11-17 Norte, 21-29 Nordeste, 31-35 Sudeste, 41-43 Sul, 50-53 Centro-Oeste
uf_regi = {
    11: 'Norte', 12: 'Norte', 13: 'Norte', 14: 'Norte', 15: 'Norte', 16: 'Norte', 17: 'Norte',
    21: 'Nordeste', 22: 'Nordeste', 23: 'Nordeste', 24: 'Nordeste', 25: 'Nordeste', 26: 'Nordeste', 27: 'Nordeste', 28: 'Nordeste', 29: 'Nordeste',
    31: 'Sudeste', 32: 'Sudeste', 33: 'Sudeste', 34: 'Sudeste', 35: 'Sudeste',
    41: 'Sul', 42: 'Sul', 43: 'Sul',
    50: 'Centro-Oeste', 51: 'Centro-Oeste', 52: 'Centro-Oeste', 53: 'Centro-Oeste'
}
uf_regi