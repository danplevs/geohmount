# %%
import pandas as pd
import plotly.express as px
from trajs.functions.transform import direcao_categorica, velocidade_categorica, chuva_categorica
from trajs.functions.geohmount_plots import wind_rose


# %%
trajs = pd.read_csv('sb_resultado.csv', sep=";")
trajs.head()

# %%
trajs = trajs.rename(columns={'velocidade_km/h': 'velocidade', 'rain': 'chuva_gdas', 'evt_sum_rain': 'evt_soma_chuva', 
                              'evt_avg_rain': 'evt_media_chuva', 'evt_max_rain': 'evt_max_chuva', 'direcao_graus': 'direcao'})

# %%
trajs = trajs.dropna()
trajs.head()

# %%
trajs['data'] = pd.to_datetime(trajs['data'])

# %%
trajs['direcao_cat'] = trajs['direcao'].apply(direcao_categorica)
trajs.head(10)

# %%
trajs['velocidade_cat'] = trajs['velocidade'].apply(velocidade_categorica)
trajs.head(10)

# %%
trajs['evt_soma_chuva_cat'] = trajs['evt_soma_chuva'].apply(chuva_categorica)
trajs.head(10)

# %%
trajs_509 = trajs.query("altitude == 509")
trajs_659 = trajs.query("altitude == 659")
trajs_909 = trajs.query("altitude == 909")

# %%
gp_vel = trajs_659.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
gp_vel.head(5)

# %%
gp_vel['frequencia'] = gp_vel['frequencia'] / gp_vel['frequencia'].sum() * 100
gp_vel.head(5)

# %%
fig = wind_rose(gp_vel, title='<b>Soberbo</b>')
fig.show()
# fig.write_html('plots/geral/html/trajsSB_vel.html')
# fig.write_image('plots/geral/png/trajsSB_vel.png')
# fig.write_image('plots/geral/svg/trajsSB_vel.svg')

# %%
gp_chuva = trajs_659.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva.head(5)

# %%
gp_chuva['frequencia'] = gp_chuva['frequencia'] / gp_chuva['frequencia'].sum() * 100
gp_chuva.head(5)

# %%
fig = wind_rose(gp_chuva, kind='chuva', title='<b>Soberbo</b>')
fig.show()
# fig.write_html('plots/geral/html/trajsSB_chuva.html')
# fig.write_image('plots/geral/png/trajsSB_chuva.png')
# fig.write_image('plots/geral/svg/trajsSB_chuva.svg')

# %%
fig = wind_rose(gp_vel, font_color='black', title='<b>Soberbo</b>', legend_title='<b>Wind Speed</b>', color_sequence=px.colors.sequential.Inferno_r)
fig.show()
# fig.write_html('plots/artigo-yasmin/trajsSB_vel.html')
# fig.write_image('plots/artigo-yasmin/trajsSB_vel.png')
# fig.write_image('plots/artigo-yasmin/trajsSB_vel.svg')

# %%
meses_chuvosos = ('Jan', 'Feb', 'Mar', 'Apr', 'Oct', 'Nov', 'Dec')
meses_secos = ('May', 'Jun', 'Jul', 'Aug', 'Sep')

# %%
trajs_659['mes'] = trajs_659['data'].dt.strftime('%b')
trajs_659.head()

# %%
periodo_umido = trajs_659.loc[trajs_659['mes'].isin(meses_chuvosos)]
periodo_umido.head()

# %%
periodo_seco = trajs_659.loc[trajs_659['mes'].isin(meses_secos)]
periodo_seco.head()

# %%
gp_vel_umido = periodo_umido.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
gp_vel_umido.head()

# %%
gp_vel_umido['frequencia'] = gp_vel_umido['frequencia'] / gp_vel_umido['frequencia'].sum() * 100
gp_vel_umido.head(5)

# %%
fig = wind_rose(gp_vel_umido, title='<b>Período úmido</b>', tickvals=[4, 6.5, 9, 11.5, 14])
fig.show()
# fig.write_html('plots/periodos/html/trajsSB_vel_umido.html')
# fig.write_image('plots/periodos/png/trajsSB_vel_umido.png')
# fig.write_image('plots/periodos/svg/trajsSB_vel_umido.svg')

# %%
gp_vel_seco = periodo_seco.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
gp_vel_seco.head()

# %%
gp_vel_seco['frequencia'] = gp_vel_seco['frequencia'] / gp_vel_seco['frequencia'].sum() * 100
gp_vel_seco.head(5)

# %%
fig = wind_rose(gp_vel_seco, title='<b>Período seco</b>', tickvals=[4, 7, 10, 13, 16])
fig.show()
# fig.write_html('plots/periodos/html/trajsSB_vel_seco.html')
# fig.write_image('plots/periodos/png/trajsSB_vel_seco.png')
# fig.write_image('plots/periodos/svg/trajsSB_vel_seco.svg')

# %%
gp_chuva_umido = periodo_umido.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva_umido.head()

# %%
gp_chuva_umido['frequencia'] = gp_chuva_umido['frequencia'] / gp_chuva_umido['frequencia'].sum() * 100
gp_chuva_umido.head()

# %%
fig = wind_rose(gp_chuva_umido, kind='chuva', title='<b>Período úmido</b>', tickvals=[4, 6.5, 9, 11.5, 14])
fig.show()
# fig.write_html('plots/periodos/html/trajsSB_chuva_umido.html')
# fig.write_image('plots/periodos/png/trajsSB_chuva_umido.png')
# fig.write_image('plots/periodos/svg/trajsSB_chuva_umido.svg')

# %%
gp_chuva_seco = periodo_seco.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva_seco.head()

# %%
gp_chuva_seco['frequencia'] = gp_chuva_seco['frequencia'] / gp_chuva_seco['frequencia'].sum() * 100
gp_chuva_seco.head()

# %%
fig = wind_rose(gp_chuva_seco, kind='chuva', title='<b>Período seco</b>', tickvals=[4, 7, 10, 13, 16])
fig.show()
# fig.write_html('plots/periodos/html/trajsSB_chuva_seco.html')
# fig.write_image('plots/periodos/png/trajsSB_chuva_seco.png')
# fig.write_image('plots/periodos/svg/trajsSB_chuva_seco.svg')

# %%
campanhas = trajs_659['campanha'].unique()

# %%
for campanha in campanhas:
    df = trajs_659.loc[trajs_659["campanha"] == campanha]
    df = df.groupby(['direcao_cat', 'velocidade_cat']).size().reset_index(name='frequencia')
    df['frequencia'] = df['frequencia'] / df['frequencia'].sum() * 100

    fig = wind_rose(df, title=f'<b>{campanha}</b>', showticklabels=False, tickvals=None)
    fig.show()
    # fig.write_html(f'plots/campanhas/html/vel/{campanha}.html')
    # fig.write_image(f'plots/campanhas/png/vel/{campanha}.png')
    # fig.write_image(f'plots/campanhas/svg/vel/{campanha}.svg')

# %%
for campanha in campanhas:
    df = trajs_659.loc[trajs_659["campanha"] == campanha]
    df = df.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
    df['frequencia'] = df['frequencia'] / df['frequencia'].sum() * 100
    
    fig = wind_rose(df, kind='chuva', title=f'<b>{campanha}</b>', template='ggplot2',  showticklabels=False, tickvals=None)
    fig.show()
    # fig.write_html(f'plots/campanhas/html/chuva/{campanha}.html')
    # fig.write_image(f'plots/campanhas/png/chuva/{campanha}.png')
    # fig.write_image(f'plots/campanhas/svg/chuva/{campanha}.svg')
