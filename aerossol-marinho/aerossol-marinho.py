# %%
from geohmount import set_chart_studio, watermark
import plotly
import plotly.graph_objects as go
import pandas as pd

# %%
set_chart_studio()

# %%
nacl = pd.read_csv('data/chuva_nacl.csv', sep=';')
nacl.head()

# %%
nacl.dtypes

# %%
nacl['Ponto'] = nacl['Amostras'].str.slice(start=0, stop=2)
nacl.head()

# %%
sb = nacl.query("Ponto == 'SB'")
ps = nacl.query("Ponto == 'PS'")
bm = nacl.query("Ponto == 'BM'")
sm = nacl.query("Ponto == 'SM'")

# %%
sm

# %%
sm = sm.drop(43)

# %%
config = {'displayModeBar': True, 'toImageButtonOptions': {'height': None, 'width': None}}

# %%
fig = go.Figure()

fig.add_trace(go.Scatter(
    name='SB',
    x=sb.iloc[:, 1], y=sb.iloc[:, 2],
    marker=dict(color='rgb(112, 173, 71)', symbol='square', size=10),
    mode='markers'
))

fig.add_trace(go.Scatter(
    name='PS',
    x=ps.iloc[:, 1], y=ps.iloc[:, 2],
    marker=dict(color='rgb(91, 155, 213)', symbol='triangle-up', size=10),
    mode='markers'
))

fig.add_trace(go.Scatter(
    name='BM',
    x=bm.iloc[:, 1], y=bm.iloc[:, 2],
    marker=dict(color='rgb(255, 192, 0)', symbol='circle', size=10),
    mode='markers'
))

fig.add_trace(go.Scatter(
    name='SM',
    x=sm.iloc[:, 1], y=sm.iloc[:, 2],
    marker=dict(color='rgb(37, 94, 145)', symbol='diamond', size=10),
    mode='markers'
))

fig.add_trace(go.Scatter(
    name='Água do mar',
    x=[0, 120], y=[0, 139.8],
    mode='lines',
    line=dict(color='darkgreen', dash='dot', width=2)
))

watermark(fig)

fig.update_traces(hovertemplate='<b>Na<sup>+</sup>: %{x:.2f}<br>'+'<b>Cl<sup>-</sup>: %{y:.2f}')
fig.update_yaxes(tickvals=(0, 20, 40, 60, 80, 100, 120), title=dict(text='<b>Cl<sup>-</sup> (mol ha<sup>-1</sup>)</b>', font_size=16), tickfont=dict(size=16))
fig.update_xaxes(title=dict(text='<b>Na<sup>+</sup> (mol ha<sup>-1</sup>)</b>', font_size=16), tickfont=dict(size=16))

fig.update_layout(template='plotly_white', width=920, height=580, legend=dict(font_size=16, orientation='h', xanchor='center', yanchor='bottom', x=0.5, y=-0.3),
updatemenus=[
    dict(
        buttons=list([
            dict(label='Linear', method='relayout', args=[{'yaxis.type': 'linear', 'yaxis.tickvals': (0, 20, 40, 60, 80, 100, 120), 'xaxis.type': 'linear', 'xaxis.tickvals': (0, 20, 40, 60, 80, 100, 120)}]),
            dict(label='Log', method='relayout', args=[{'yaxis.type': 'log', 'yaxis.tickvals': (0.1, 1, 10, 100), 'xaxis.type': 'log', 'xaxis.tickvals': (0.1, 1, 10, 100)}]), 
        ]),
        xanchor='left', yanchor='top', x=0.06, y=1.2,
    )
],
annotations=[
    dict(text='<b>Escala</b>', showarrow=False, xref='paper', yref='paper', x=-0.03, y=1.185, font_size=15)
]
)

fig.show(config=config)
# py.plot(fig, filename = 'aerossol-marinho')
# fig.write_html('nacl.html', include_plotlyjs='cdn', config=config, full_html=False)
