# %%
import base64
import pandas as pd
import json
import chart_studio.plotly as py
from trajs.functions.set_chart_studio import set_chart_studio
from trajs.functions.geohmount_plots import wind_rose
from trajs.functions.watermark import plot_watermark

# %%
trajs = pd.read_csv('../../../sb_resultado_manipulado.csv')
trajs.drop('Unnamed: 0', axis=1, inplace=True)
trajs.head()
# %%
trajs_659 = trajs.query('altitude == 659')
trajs_659.head()
# %%
trajs_659.evt_id.unique().shape
# %%
event = trajs_659.query('evt_id == 471')
# %%
gp_event = event.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
# %%
gp_event['frequencia'] = gp_event['frequencia'] / gp_event['frequencia'].sum() * 100
gp_event
# %%
img = '/home/daniel/geohmount/code/logos-png/GEOHMOUNT-Logo-Cinzas.png'
geohmount_logo = base64.b64encode(open(img, 'rb').read())

# %%
set_chart_studio()
# %%
fig = wind_rose(dataframe=gp_event, kind='chuva', title='<b>Soberbo</b>', 
                tickvals=[10, 20, 30, 40, 50], width=920, height=537, bg=False)
plot_watermark(fig, y=0.55, sizex=0.4, sizey=0.4)

fig.show()
# fig.write_html('evt_471.html', include_plotlyjs='cdn', full_html=False)
# fig.write_image('evt_471.svg')
# fig.write_image('evt_471.png')
# py.plot(fig, auto_open=False, filename='evt_471_sb')