# %%
import base64
import pandas as pd
import chart_studio.plotly as py
from functions.set_chart_studio import set_chart_studio
from trajs.functions.geohmount_plots import wind_rose
from trajs.functions.watermark import plot_watermark
# %%
trajs = pd.read_csv('../../../ps_resultado_manipulado.csv')
trajs.drop('Unnamed: 0', axis=1, inplace=True)
trajs.head()
# %%
event = trajs.query('evt_id == 642')
# %%
gp_event = event.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
# %%
gp_event['frequencia'] = gp_event['frequencia'] / gp_event['frequencia'].sum() * 100
gp_event
# %%
set_chart_studio()
# %%
fig = wind_rose(dataframe=gp_event, kind='chuva', title='<b>Pedra do Sino</b>', 
          tickvals=[10, 20, 30, 40, 50], width=920, height=537, bg=False)
plot_watermark(fig, y=0.48, sizex=0.4, sizey=0.4)

fig.show()
# fig.write_html('evt_642.html', include_plotlyjs='cdn', full_html=False)
# fig.write_image('evt_642.svg')
# fig.write_image('evt_642.png')
# py.plot(fig, filename='evt_642_ps', auto_open=False)
