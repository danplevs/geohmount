# %%
import base64
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from trajs.functions.geohmount_plots import wind_rose

# %%
trajs = pd.read_csv('../../ps_resultado_manipulado.csv')
trajs.drop('Unnamed: 0', axis=1, inplace=True)
trajs.head()

# %%
gp_chuva = trajs.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva['frequencia'] = gp_chuva['frequencia'] / gp_chuva['frequencia'].sum() * 100
gp_chuva


# %%
dir_proportions = gp_chuva.groupby('direcao_cat')['frequencia'].sum()
dir_proportions = dir_proportions.round(0).astype(int).to_frame().reset_index().sort_values(by='frequencia', ascending=False)
dir_proportions

# %%
gp_chuva = pd.read_excel('gp_chuva.xlsx')
gp_chuva.head()
# %%
dirs = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE']


# %%
gp_chuva.query('evt_soma_chuva_cat == "20-35 mm"')
# %%
medidas = ('5-20 mm', '20-35 mm', '35-50 mm', '50-65 mm', '65-80 mm', 
            '80-95 mm', '95-110 mm', '110-125 mm', '125-130 mm')


# %%
img = '/home/daniel/geohmount/code/logos-png/GEOHMOUNT-Logo-Cinzas.png'
geohmount_logo = base64.b64encode(open(img, 'rb').read())

# %%
fig = make_subplots(rows=1, cols=2,
                    specs=[[{'type': 'table'}, {'type': 'polar'}]],
                    column_widths=[0.5, 0.5],
                    row_heights=[1])

fig.add_trace(go.Table(
    header=dict(values=['<b>Direção</b>', '<b>Frequência (%)</b>'],
                fill_color='gray',
                line_color='darkslategray', 
                font=dict(size=14, color='white')),
    cells=dict(values=[dir_proportions.direcao_cat, dir_proportions.frequencia], 
               font=dict(size=14, color='black'),
               line_color='darkslategray',
               height=30)
               ), 
               row=1, col=1)

for index, value in enumerate(medidas):
    fig.add_trace(go.Barpolar(
        theta=gp_chuva.query('evt_soma_chuva_cat == @value')['direcao_cat'],
        r=gp_chuva.query('evt_soma_chuva_cat == @value')['frequencia'],
        name=value,
        marker_color=px.colors.sequential.Blues[index]),
        row=1, col=2)
    
fig.add_layout_image(
    dict(
        source=f'data:image/png;base64,{geohmount_logo.decode()}',
        xref="paper",
        yref="paper",
        xanchor='center',
        yanchor='middle',
        x=0.5,
        y=0.5,
        sizex=0.7,
        sizey=0.7,
        sizing="contain",
        opacity=0.13,
        layer="above")
)

fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', width=1080, height=600,
                  legend=dict(traceorder='reversed', 
                                  yanchor='top', 
                                  y=0.8, 
                                  xanchor='right', 
                                  x=1.2,
                                  font_color=None,
                                  title=dict(
                                      font_size=14,
                                      font_color=None,
                                      text='<b>Precipitação</b>')
                                 ),
                  title={'font_size': 20, 'text': '<b>Pedra do Sino</b>', 'font_color': None, 'y': 0.95, 'x': 0.5, 'xref': 'paper'},
                  polar = dict(
                          radialaxis=dict(
                              showline=False,
                              showticklabels=True,
                              tickfont_color=None,
                              tickfont_size=14,
                              ticksuffix='%',
                              tickvals=[5, 8, 11, 14, 17],
                              tickangle=90,
                              angle=90), 
                          angularaxis=dict(tickfont_size=15, tickfont_color=None),
                 ),
                )   
fig.show()
fig.write_html('ps_trajs.html')
