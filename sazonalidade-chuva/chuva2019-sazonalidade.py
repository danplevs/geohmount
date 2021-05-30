# %%
import pandas as pd

df = pd.read_csv("chuva_2019.csv", sep=';', encoding="latin1")
df


# %%
import pandas as pd

df2 = pd.read_csv("sazonalidade.csv", sep=';', encoding="latin1")
df2.head()


# %%
# invertendo o dataframe
df2 = df2.reindex(index=df2.index[::-1])
df2.head()


# %%
# renomeando as séries históricas
df2.rename(columns={'Série Histórica (2007-2019) e DP': 'sh_SM', 'Série Histórica (2007-2019) e DP.1': 'sh_BM', 'Série Histórica (2007-2019) e DP.2': 'sh_SB'}, inplace=True)
df2.head()


# %%
config = {'displayModeBar': True, 'toImageButtonOptions': {'height': None, 'width': None}}


# %%
import plotly.graph_objects as go
from trajs.functions.watermark import plot_watermark

fig = go.Figure()

fig.add_trace(go.Bar(name='Bonfim',x=df.estacao[:3], y=df.chuva[:3], marker_color='rgb(0, 153, 216)', error_y=dict(type='data', array=df.sd[:3])
))
fig.add_trace(go.Bar(name='Soberbo',x=df.estacao[3:5], y=df.chuva[3:5], marker_color='rgb(0, 90, 74)', error_y=dict(type='data', array=df.sd[3:5])
))
fig.add_trace(go.Bar(name='Santa Marta',x=df.estacao[5:8], y=df.chuva[5:8], marker_color='rgb(86, 34, 18)', error_y=dict(type='data', array=df.sd[5:8])
))

plot_watermark(fig, layer="below")

fig.update_layout(template='plotly_white', width=1200, height=800, font_family='Open Sans',  xaxis_tickfont_size=16, yaxis=dict(title='<b>Precipitação no ano de 2019 (mm)', titlefont_size=16, tickfont_size=16), legend=dict(font_size=14))
fig.show()
#fig.write_html('C:\\Users\\daniel\\Documents\\Github\\geohmount\\geohmount-plotly\\sazonalidade-chuva\\chuva_2019.html', include_plotlyjs='cdn', config=config)


# %%
import plotly.graph_objects as go

blue = 'rgb(0, 153, 216)'
green = 'rgb(0, 90, 74)'
brown = 'rgb(86, 34, 18)'
fig2 = go.Figure()

fig2.add_trace(go.Bar(name='BM (Estação Pedro do Rio)', x=df2['mês'], y=df2['BM (Estação Pedro do Rio)'], marker=dict(color=blue)
))

fig2.add_trace(go.Scatter(mode='lines+markers', name='Série Histórica (2007-2019)', x=df2['mês'], y=df2['sh_BM'], error_y=dict(color='black', type='data', array=df2['sd_BM'] ), marker=dict(color=blue, line_width=1, line_color='black'), line=dict(color=blue, width=3), visible='legendonly'
))

fig2.add_trace(go.Bar(name='SB (Estação PARNASO)',x=df2['mês'], y=df2['SB (Estação PARNASO)'], marker=dict(color=green)
))

fig2.add_trace(go.Scatter(mode='lines+markers', name='Série Histórica (2007-2019)', x=df2['mês'], y=df2['sh_SB'], error_y=dict(color='black', type='data', array=df2['sd_SB']), marker=dict(color=green, line_width=1, line_color='black'), line=dict(color=green, width=3), visible='legendonly'
))

fig2.add_trace(go.Bar(name='SM (Estação Caparaó)',x=df2['mês'], y=df2['SM (Estação Caparaó)'], marker=dict(color=brown)
))

fig2.add_trace(go.Scatter(mode='lines+markers', name='Série Histórica (2007-2019)', x=df2['mês'], y=df2['sh_SM'], error_y=dict(color='black', type='data', array=df2['sd_SM']), marker=dict(color=brown, line_width=1, line_color='black'), line=dict(color=brown, width=3), visible='legendonly'
))

plot_watermark(fig2, layer="below")

fig2.update_layout(template='plotly_white',
                   width=1500, height=800, 
                   legend=dict(font_size=14), 
                   barmode='group',
                   font_family='Open Sans',  
                   xaxis=dict(tickangle=-45, tickfont_size=16),
                   yaxis=dict(title='<b>Precipitação (mm)', titlefont_size=16, tickfont_size=16), 
                   annotations=[dict(text='<b>Clique nas legendas para <br>habilitar as séries históricas!', xref='paper', yref='paper', x=1.11, y=0.75,                         arrowhead=1, arrowwidth=2, arrowcolor='black', ax=0, ay=45, font=dict(color='black', size=14))]
)

fig2.show()
#fig2.write_html('C:\\Users\\daniel\\Documents\\Github\\geohmount\\geohmount-plotly\\sazonalidade-chuva\\sazonalidade.html', include_plotlyjs='cdn', config=config)
