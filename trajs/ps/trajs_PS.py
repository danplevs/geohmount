# %%
import pandas as pd
import plotly.express as px
from geohmount.trajs import stringify_direction, stringify_speed, stringify_speed_ps, stringify_rain, wind_rose

# %%
trajs = pd.read_csv('data/ps_resultado.csv', sep=";")
trajs.head()

# %%
trajs = trajs.rename(columns={'velocidade_km/h': 'velocidade', 'rain': 'chuva_gdas', 'evt_sum_rain': 'evt_soma_chuva', 
                              'evt_avg_rain': 'evt_media_chuva', 'evt_max_rain': 'evt_max_chuva', 'direcao_graus': 'direcao'})

# %%
trajs = trajs.dropna()
trajs.head()

# %%
trajs['data'] = pd.to_datetime(trajs['data'], dayfirst=True, exact=False)

# %%
trajs['direcao_cat'] = trajs['direcao'].apply(stringify_direction)
trajs.head(10)

# %%
trajs['velocidade_cat'] = trajs['velocidade'].apply(stringify_speed_ps)
trajs.head(10)

# %%
trajs['evt_soma_chuva_cat'] = trajs['evt_soma_chuva'].apply(stringify_rain)
trajs.head(10)

# %%
gp_vel = trajs.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
gp_vel.head(5)

# %%
gp_vel['frequencia'] = gp_vel['frequencia'] / gp_vel['frequencia'].sum() * 100
gp_vel.head(5)

# %%
fig = wind_rose(gp_vel, location='ps', title='<b>Pedra do Sino</b>',
                bg=False, tickvals=[5, 8, 11, 14, 17], color_sequence=px.colors.sequential.Inferno_r)
fig.show()
# fig.write_html('plots/geral/html/trajsPS_vel.html')
# fig.write_image('plots/geral/png/trajsPS_vel.png')
# fig.write_image('plots/geral/svg/trajsPS_vel.svg')

# %%
gp_chuva = trajs.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva.head(5)

# %%
gp_chuva['frequencia'] = gp_chuva['frequencia'] / gp_chuva['frequencia'].sum() * 100
gp_chuva.head(5)

# %%
fig = wind_rose(gp_chuva, bg=False, kind='chuva', tickvals=[5, 8, 11, 14, 17], title='<b>Pedra do Sino</b>')
fig.show()
# fig.write_html('plots/geral/html/trajsPS_chuva.html')
# fig.write_image('plots/geral/png/trajsPS_chuva.png')
# fig.write_image('plots/geral/svg/trajsPS_chuva.svg')

# %%
fig = wind_rose(gp_vel, location='ps', tickvals=[4, 8, 12, 18], font_color='black', title='<b>PS</b>', legend_title='<b>Wind Speed</b>', color_sequence=px.colors.sequential.Inferno_r)
fig.show()
# tickvals=[5, 8, 11, 14, 17]
fig.write_html('plots/artigo-yasmin/trajsPS_vel.html')
fig.write_image('plots/artigo-yasmin/trajsPS_vel.png')
fig.write_image('plots/artigo-yasmin/trajsPS_vel.svg')

# %%
meses_chuvosos = ('Jan', 'Feb', 'Mar', 'Apr', 'Oct', 'Nov', 'Dec')
meses_secos = ('May', 'Jun', 'Jul', 'Aug', 'Sep')

# %%
trajs['mes'] = trajs['data'].dt.strftime('%b')
trajs.head()

# %%
periodo_umido = trajs.loc[trajs['mes'].isin(meses_chuvosos)]
periodo_umido.head()

# %%
periodo_seco = trajs.loc[trajs['mes'].isin(meses_secos)]
periodo_seco.head()

# %%
gp_vel_umido = periodo_umido.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
gp_vel_umido.head()

# %%
gp_vel_umido['frequencia'] = gp_vel_umido['frequencia'] / gp_vel_umido['frequencia'].sum() * 100
gp_vel_umido.head(5)

# %%
fig = wind_rose(gp_vel_umido, location='ps', title='<b>Período úmido</b>', tickvals=[4, 6.5, 9, 11.5, 14], bg=False)
fig.show()
# fig.write_html('plots/periodos/html/trajsPS_vel_umido.html')
# fig.write_image('plots/periodos/png/trajsPS_vel_umido.png')
# fig.write_image('plots/periodos/svg/trajsPS_vel_umido.svg')

# %%
gp_vel_seco = periodo_seco.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
gp_vel_seco.head()

# %%
gp_vel_seco['frequencia'] = gp_vel_seco['frequencia'] / gp_vel_seco['frequencia'].sum() * 100
gp_vel_seco.head(5)

# %%
fig = wind_rose(gp_vel_seco, location='ps', title='<b>Período seco</b>', tickvals=[5, 10, 15, 20, 25], bg=False)
fig.show()
# fig.write_html('plots/periodos/html/trajsPS_vel_seco.html')
# fig.write_image('plots/periodos/png/trajsPS_vel_seco.png')
# fig.write_image('plots/periodos/svg/trajsPS_vel_seco.svg')

# %%
gp_chuva_umido = periodo_umido.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva_umido.head()

# %%
gp_chuva_umido['frequencia'] = gp_chuva_umido['frequencia'] / gp_chuva_umido['frequencia'].sum() * 100
gp_chuva_umido.head()

# %%
fig = wind_rose(gp_chuva_umido, location='ps', kind='chuva', title='<b>Período úmido</b>', tickvals=[4, 6.5, 9, 11.5, 14], bg=False)
fig.show()
# fig.write_html('plots/periodos/html/trajsPS_chuva_umido.html')
# fig.write_image('plots/periodos/png/trajsPS_chuva_umido.png')
# fig.write_image('plots/periodos/svg/trajsPS_chuva_umido.svg')

# %%
gp_chuva_seco = periodo_seco.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva_seco.head()

# %%
gp_chuva_seco['frequencia'] = gp_chuva_seco['frequencia'] / gp_chuva_seco['frequencia'].sum() * 100
gp_chuva_seco.head()

# %%
fig = wind_rose(gp_chuva_seco, kind='chuva', title='<b>Período seco</b>', tickvals=[5, 10, 15, 20, 25], bg=False)
fig.show()
# fig.write_html('plots/periodos/html/trajsPS_chuva_seco.html')
# fig.write_image('plots/periodos/png/trajsPS_chuva_seco.png')
# fig.write_image('plots/periodos/svg/trajsPS_chuva_seco.svg')
