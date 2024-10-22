import pandas as pd
from pandas import read_csv
from glob import glob 
import os


#Carregando e filtrando os dados da pnad 2019
file_2019 = glob(f'dados/dados_pnad_2019*.csv')
print(file_2019)

pnad_2019 = (
    pd.read_csv(file_2019[0], sep=',', encoding='latin1')
     .filter(items=['V2007', 'V2010', 'V2009', 'V3009A','UF'])
    .query('V3009A == 7 or V3009A == 8')
)
print(pnad_2019)

#Carregando e filtrando os dados da pnad 2023
file_2023 = glob(f'dados/dados_pnad_2023*.csv')
print(file_2023)

pnad_2023 = (
     pd.read_csv(file_2023[0], sep=',', encoding='latin1')
     .filter(items=['V2007', 'V2010', 'V2009', 'V3009A','UF'])
    .query('V3009A == 7 or V3009A == 8')
)
print(pnad_2023)

# 3. Salvar os dados filtrados
#2019
pnad_2019.to_csv("dados/pnad_2019_filtrado.csv", index=False, compression='gzip')
pnad_2019.to_csv("dados/pnad_2019_filtrado.csv", index=False)
#2023
pnad_2023.to_csv("dados/pnad_2023_filtrado.csv", index=False, compression='gzip')
pnad_2023.to_csv("dados/pnad_2023_filtrado.csv", index=False)