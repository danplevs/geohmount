import os
import pandas as pd

cwd = os.getcwd() + '/focos-incendio/'
data_dir = cwd + 'Campanhas/'
columns_to_keep = ['X', 'Y', 'precipitacao', 'bioma', 'frp', 'satelite', 'riscofogo', 
                   'diasemchuva', 'estado', 'municipio', 'data/hora']
fire_outbreaks = pd.DataFrame()

for file in os.listdir(data_dir):
    campaign = pd.read_csv(f'{data_dir}{file}')
    campaign = campaign[columns_to_keep]
    campaign['data/hora'] = pd.to_datetime(campaign['data/hora'], dayfirst=True)
    campaign['campanha'] = str(file.split('.')[0])
    campaign.rename(columns={'X': 'longitude', 'Y': 'latitude'}, inplace=True)
    fire_outbreaks = pd.concat([fire_outbreaks, campaign], ignore_index=True)

fire_outbreaks.to_csv(cwd + 'fire_outbreaks.csv', sep=',', index=False)
