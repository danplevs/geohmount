# %%
import pandas as pd
import plotly.express as px
# %%
fire_outbreaks = pd.read_csv('fire_outbreaks.csv')
fire_outbreaks.head()
# %%
columns_to_hover = ('riscofogo', 'latitude', 'longitude', 'data/hora')
# %%
fig = px.density_mapbox(fire_outbreaks, lat='latitude', lon='longitude', z='riscofogo', radius=9,
                        center=dict(lat=-22.5, lon=-43), zoom=7, hover_data=columns_to_hover,
                        mapbox_style="stamen-toner",  color_continuous_scale = px.colors.diverging.RdYlGn_r,
                        width=1024, height=768)
fig.show()
fig.write_html('riscofogo_stamen-toner.html')
# %%
fig = px.density_mapbox(fire_outbreaks, lat='latitude', lon='longitude', z='frp', radius=30,
                        center=dict(lat=-22.5, lon=-43), zoom=7, mapbox_style="stamen-toner",
                        color_continuous_scale=px.colors.sequential.Plasma_r,
                        width=1024, height=768)
fig.show()
fig.write_html('frp_stamen-toner.html')
