# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# %%
trajs = pd.read_csv('data/ps_resultado_manipulado.csv')
trajs.head()


# %%
trajs = trajs.drop('Unnamed: 0', 1)
trajs.head()


# %%
trajs['data'] = pd.to_datetime(trajs['data'], dayfirst=True, exact=False)
trajs['mes'] = trajs['data'].dt.strftime('%b')


# %%
meses_chuvosos = ('Jan', 'Feb', 'Mar', 'Apr', 'Oct', 'Nov', 'Dec')
meses_secos = ('May', 'Jun', 'Jul', 'Aug', 'Sep')


# %%
trajs['mes'] = trajs['data'].dt.strftime('%b')
trajs.head()


# %%
chuva_media = round(trajs['evt_soma_chuva'].unique().mean(), 1)
print(f'A precipitação média por evento é {chuva_media} mm')


# %%
periodo_umido = trajs.loc[trajs['mes'].isin(meses_chuvosos)]
periodo_umido.head()


# %%
prop_umido = periodo_umido.shape[0] / trajs.shape[0] * 100
print(f'O período úmido representa {prop_umido:.0f}% das retrotrajetórias')


# %%
periodo_seco = trajs.loc[trajs['mes'].isin(meses_secos)]
periodo_seco.head()


# %%
prop_seco = periodo_seco.shape[0] / trajs.shape[0] * 100
print(f'O período seco representa {prop_seco:.0f}% das retrotrajetórias')


