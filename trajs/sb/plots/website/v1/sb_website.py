# %%
import sys
sys.path.append('C:/Users/daniel/OneDrive/geohmount/code/trajs/functions')
# %%
import sys
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from watermark import plot_watermark

# %%
trajs = pd.read_csv('../../../data/sb_resultado_manipulado.csv')
trajs.drop('Unnamed: 0', axis=1, inplace=True)
trajs.head()


# %%
trajs = trajs.query('altitude == 659')
trajs.head()


# %%
gp_chuva = trajs.groupby(['direcao_cat', 'evt_soma_chuva_cat']).size().reset_index(name='frequencia')
gp_chuva['frequencia'] = gp_chuva['frequencia'] / gp_chuva['frequencia'].sum() * 100
gp_chuva


# %%
dir_proportions = gp_chuva.groupby('direcao_cat')['frequencia'].sum()
dir_proportions = dir_proportions.round(0).astype(int).to_frame().reset_index().sort_values(by='frequencia', ascending=False)


# %%
dirs = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE']


# %%
df_mapping = pd.DataFrame({
    'direction': dirs,
})

sort_mapping = df_mapping.reset_index().set_index('direction')
sort_mapping


# %%
gp_chuva['dir_num'] = gp_chuva['direcao_cat'].map(sort_mapping['index'])
gp_chuva.sort_values('dir_num', inplace=True)


# %%
medidas = ('5-20 mm', '20-35 mm', '35-50 mm', '50-65 mm', '65-80 mm', '80-95 mm', '95-110 mm', '110-125 mm', '125-130 mm')


# %%
dir_proportions
# %%
fig = make_subplots(rows=1, cols=2,
                    specs=[[{'type': 'table'}, {'type': 'polar'}]],
                    column_widths=[0.3, 0.7],
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
                  title={'font_size': 20, 'text': '<b>Soberbo</b>', 'font_color': None, 'y': 0.95, 'x': 0.5, 'xref': 'paper'},
                  polar = dict(
                          radialaxis=dict(
                              showline=False,
                              showticklabels=True,
                              tickfont_color=None,
                              tickfont_size=14,
                              ticksuffix='%',
                              tickvals=[4, 6, 8, 10, 12],
                              tickangle=90,
                              angle=90), 
                          angularaxis=dict(tickfont_size=15, tickfont_color=None),
                 ),
                )   
fig.show()
fig.write_image('sb_trajs_no_watermark.png', width=1000, height = 750)
# fig.write_html('plots/website/sb_trajs.html')
