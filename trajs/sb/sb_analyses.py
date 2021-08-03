# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# %%
trajs = pd.read_csv('data/sb_resultado_manipulado.csv')
trajs.head()


# %%
trajs = trajs.drop('Unnamed: 0', 1)
trajs.head()


# %%
trajs['data'] = pd.to_datetime(trajs['data'])
trajs['mes'] = trajs['data'].dt.strftime('%b')


# %%
trajs_659 = trajs.query('altitude == 659')


# %%
meses_chuvosos = ('Jan', 'Feb', 'Mar', 'Apr', 'Oct', 'Nov', 'Dec')
meses_secos = ('May', 'Jun', 'Jul', 'Aug', 'Sep')


# %%
trajs_659['mes'] = trajs_659['data'].dt.strftime('%b')
trajs_659.head()


# %%
round(trajs_659['evt_soma_chuva'].unique().mean(), 1)


# %%
periodo_umido = trajs_659.loc[trajs_659['mes'].isin(meses_chuvosos)]
periodo_umido.head()


# %%
f'O período úmido representa {periodo_umido.shape[0] / trajs_659.shape[0] * 100:.2f}% das retrotrajetórias'


# %%
periodo_seco = trajs_659.loc[trajs_659['mes'].isin(meses_secos)]
periodo_seco.head()


# %%
f'O período seco representa {periodo_seco.shape[0] / trajs_659.shape[0] * 100:.2f}% das retrotrajetórias'


# %%
prop_direcoes_seco = periodo_seco['direcao_cat'].value_counts(normalize=True) * 100

fig = plt.figure(figsize=(14, 8))
sns.set_context('talk')
sns.barplot(x=prop_direcoes_seco.index, y=prop_direcoes_seco, palette='flare_r')
plt.ylabel('%')
plt.title('Direções (período seco)')
plt.show()
# atualiza a figura
# fig.savefig('plots/analises/proporcao_direcoes_seco.svg')


# %%
round(prop_direcoes_seco, 2)


# %%
prop_direcoes_umido = periodo_umido['direcao_cat'].value_counts(normalize=True) * 100

fig = plt.figure(figsize=(14, 8))
sns.set_context('talk')
sns.barplot(x=prop_direcoes_umido.index, y=prop_direcoes_umido, palette='flare_r')
plt.ylabel('%')
plt.title('Direções (período úmido)')
plt.show()
# atualiza a figura
# fig.savefig('plots/analises/proporcao_direcoes_umido.svg')


# %%
round(prop_direcoes_umido, 2)


# %%
prop_direcoes = trajs_659['direcao_cat'].value_counts(normalize=True) * 100

fig = plt.figure(figsize=(14, 8))
sns.set_context('talk')
sns.barplot(x=prop_direcoes.index, y=prop_direcoes, palette='flare_r')
plt.ylabel('%')
plt.title('Direções')
plt.show()
# atualiza a figura
# fig.savefig('plots/analises/proporcao_direcoes.svg')  


# %%
velocidades = ['0-5 km/h', '5-10 km/h', '10-15 km/h', '15-20 km/h', '20-25 km/h', '25-30 km/h', '30-35 km/h', '35-40 km/h','40-45 km/h']

prop_velocidades = trajs_659['velocidade_cat'].value_counts(normalize=True)* 100
prop_velocidades = prop_velocidades.reindex(index=velocidades)


# %%
fig = plt.figure(figsize=(20, 8))
sns.set_context('talk')
sns.barplot(x=prop_velocidades.index, y=prop_velocidades, palette='magma_r')
plt.ylabel('%')
plt.title('Velocidades')
# atualiza a figura
# fig.savefig('plots/analises/proporcao_velocidades.svg')


# %%
chuvas = ['5-20 mm', '20-35 mm', '35-50 mm', '50-65 mm', '65-80 mm', '80-95 mm', '95-110 mm', '110-125 mm', '125-130 mm']

prop_chuvas = trajs_659['evt_soma_chuva_cat'].value_counts(normalize=True).sort_index() * 100
prop_chuvas = prop_chuvas.reindex(index=chuvas)


# %%
fig = plt.figure(figsize=(18, 8))
sns.barplot(x=prop_chuvas.index, y=prop_chuvas, palette='Blues')
plt.ylabel('%')
plt.title('Precipitação')
# atualiza a figura
# fig.savefig('plots/analises/proporcao_chuva.svg')


# %%
fig = plt.figure(figsize=(16, 8))
sns.boxplot(data=trajs_659, x='direcao_cat', y='evt_soma_chuva')
plt.ylabel('Soma de precipitação do evento (mm)'), plt.xlabel('Direção')
# atualiza a figura
# fig.savefig('plots/analises/dist_chuva_direcoes.svg')


# %%
principais_direcoes = trajs_659.query('direcao_cat == ["SSW", "S", "E", "ESE"]')
fig = plt.figure(figsize=(12, 8))
sns.boxplot(data=principais_direcoes, x='direcao_cat', y='evt_soma_chuva')
plt.ylabel('Soma de precipitação do evento (mm)'), plt.xlabel('Direção')
# atualiza a figura
# fig.savefig('plots/analises/dist_chuva_principais_direcoes.svg')
