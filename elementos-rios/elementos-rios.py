# %%
from functions.set_chart_studio import set_chart_studio

set_chart_studio()


# %%
import pandas as pd

rios = pd.read_csv("data/rios_medias.csv", sep=';')
rios.head()


# %%
rios = rios.rename(columns={'?': 'Condutividade (µS cm<sup>-1</sup>)', 'Si': '[H<sub>4</sub>SiO<sub>4</sub>]', 'HCO3': '[HCO<sub>3</sub><sup>-</sup>]', 'Na': '[Na<sup>+</sup>]', 'Cl': '[Cl<sup>-</sup>]', 'Ca': '[Ca<sup>2+</sup>]','SO4': '[SO<sub>4</sub><sup>2-</sup>]', 'K': '[K<sup>+</sup>]', 'Mg': '[Mg<sup>2+</sup>]'})
rios.head()


# %%
var_principais = ['Ponto', 'pH', 'Condutividade (µS cm<sup>-1</sup>)', '[H<sub>4</sub>SiO<sub>4</sub>]', '[HCO<sub>3</sub><sup>-</sup>]', '[Na<sup>+</sup>]', '[Cl<sup>-</sup>]', '[Ca<sup>2+</sup>]', '[SO<sub>4</sub><sup>2-</sup>]', '[K<sup>+</sup>]', '[Mg<sup>2+</sup>]']

fis_qui = ['Condutividade (µS cm<sup>-1</sup>)', 'pH']
elem_principais = ['[H<sub>4</sub>SiO<sub>4</sub>]', '[HCO<sub>3</sub><sup>-</sup>]', '[Na<sup>+</sup>]', '[Cl<sup>-</sup>]', '[Ca<sup>2+</sup>]', '[SO<sub>4</sub><sup>2-</sup>]', '[K<sup>+</sup>]', '[Mg<sup>2+</sup>]']

df_principais = rios[var_principais]


# %%
config = {'displayModeBar': True, 'toImageButtonOptions': {'height': None, 'width': None}}


# %%
blue = 'rgb(0, 153, 216)'
green = 'rgb(0, 90, 74)'
brown = 'rgb(86, 34, 18)'


# %%
import plotly.express as px
import plotly.graph_objects as go
from trajs.functions.watermark import plot_watermark

bm = df_principais.iloc[0]
sb = df_principais.iloc[1]
sm = df_principais.iloc[2]

fig = go.Figure(data=[
    go.Bar(name='Rio Soberbo', x=fis_qui, y=sb[fis_qui], marker=dict(color=green)),
    go.Bar(name='Rio Bonfim', x=fis_qui, y=bm[fis_qui], marker=dict(color=blue)),
    go.Bar(name='Rio Santa Marta', x=fis_qui, y=sm[fis_qui], marker=dict(color=brown)),
])

plot_watermark(fig, y=0.6)

fig.update_layout(width=920, height=530, template='plotly_white', barmode='group', bargroupgap=0.1, title=dict(text='<b>Dados fisico-químicos</b>', x=0.5, y=0.93, font_size=20), legend=dict(font_size=13))
fig.update_yaxes(tickfont=dict(size=15), tick0=0, dtick=2)
fig.update_xaxes(tickfont=dict(size=15))
fig.show()
# py.plot(fig, filename = 'fisqui-rios')
# fig.write_html('ph_cond.html', include_plotlyjs='cdn', config=config, full_html=False)


# %%
fig = go.Figure(data=[
    go.Bar(name='Rio Soberbo', x=elem_principais, y=sb[elem_principais], marker=dict(color=green)),
    go.Bar(name='Rio Bonfim', x=elem_principais, y=bm[elem_principais], marker=dict(color=blue)),
    go.Bar(name='Rio Santa Marta', x=elem_principais, y=sm[elem_principais], marker=dict(color=brown)),
])

plot_watermark(fig, y=0.6)

fig.update_yaxes(tickfont=dict(size=15))
fig.update_xaxes(tickfont=dict(size=14))
fig.update_layout(width=920, height=530, template='plotly_white', barmode='group', bargap=0.3, title=dict(text="<b>Concentração média de H<sub>4</sub>SiO<sub>4</sub> e <br> principais íons (µmol L<sup>-1</sup>)</b>", x=0.5, y=0.91, font_size=20), legend=dict(font_size=13))
fig.show()
# py.plot(fig, filename = 'elemprincipais-rios')
# fig.write_html('elem_principais.html', include_plotlyjs='cdn', config=config)


# %%
var_tracos = ['Ponto', 'Al', 'Fe', 'Nd', 'Mn', 'Sr', 'Ba', 'Li', 'Rb', 'V']
elem_tracos = ['Al', 'Fe', 'Nd', 'Mn', 'Sr', 'Ba', 'Li', 'Rb', 'V']
df_tracos = rios[var_tracos]

bm = df_tracos.iloc[0]
sb = df_tracos.iloc[1]
sm = df_tracos.iloc[2]


# %%
import plotly.express as px
import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='Rio Soberbo', x=elem_tracos, y=sb[elem_tracos], marker=dict(color=green)),
    go.Bar(name='Rio Bonfim', x=elem_tracos, y=bm[elem_tracos], marker=dict(color=blue)),
    go.Bar(name='Rio Santa Marta', x=elem_tracos, y=sm[elem_tracos], marker=dict(color=brown)),
])

plot_watermark(fig)

fig.update_yaxes(tickfont=dict(size=15))
fig.update_xaxes(tickfont=dict(size=14))
fig.update_layout(width=920, height=518, template='plotly_white', barmode='group', bargap=0.3, title=dict(text="<b>Concentração média de elementos traço (µmol L<sup>-1</sup>)", x=0.5, y=0.93, font_size=20), legend=dict(font_size=13))
fig.show()
# py.plot(fig, filename = 'elemtracos-rios')
# fig.write_html('elem_tracos.html', include_plotlyjs='cdn', config=config, full_html=False)
