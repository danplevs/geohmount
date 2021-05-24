import plotly.express as px

def wind_rose(dataframe, kind='vel', location='sb', title='<b>Distribuição das massas de ar resultantes em chuva no Soberbo</b>', 
             legend_title='<b>Velocidade</b>', tickvals=[4, 6, 8, 10, 12], showticklabels=True, bg=True, width=800, height=450,
             color='velocidade_cat', color_sequence= px.colors.sequential.Plasma_r, font_color=None, template='plotly'):
        
    direcoes = ("N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW")
    if location == "sb":
        medidas = ('0-5 km/h', '5-10 km/h', '10-15 km/h', '15-20 km/h', '20-25 km/h', '25-30 km/h', '30-35 km/h', '35-40 km/h','40-45 km/h')
    elif location == 'ps':
        medidas = ('0-10 km/h', '10-20 km/h', '20-30 km/h', '30-40 km/h', '40-50 km/h', '50-60 km/h', '60-70 km/h', '70-80 km/h', '80-90 km/h')
    category_orders={'direcao_cat': direcoes, 'velocidade_cat': medidas}
    
    if kind == 'chuva':
        legend_title = '<b>Precipitação</b>'
        color='evt_soma_chuva_cat'
        color_sequence = px.colors.sequential.Blues
        medidas = ('5-20 mm', '20-35 mm', '35-50 mm', '50-65 mm', '65-80 mm', '80-95 mm', '95-110 mm', '110-125 mm', '125-130 mm')
        category_orders={'direcao_cat': direcoes, 'evt_soma_chuva_cat': medidas}

    if bg == True:
        bgcolor='rgba(255,255,255,1)'
    else:
        bgcolor='rgba(0,0,0,0)'
    
    color_map = dict(zip(medidas, color_sequence))
    
    fig = px.bar_polar(dataframe, r='frequencia', theta='direcao_cat', color=color, color_discrete_map=color_map,
                       category_orders=category_orders, width=width, height=height) 

    fig.update_layout(template=template, 
                      paper_bgcolor=bgcolor,
                      legend=dict(traceorder='reversed', 
                                  yanchor='top', 
                                  y=0.99, 
                                  xanchor='right', 
                                  x=1,
                                  font_color=font_color,
                                  font_size=14,
                                  title=dict(
                                      font_size=15,
                                      font_color=font_color,
                                      text=legend_title)
                                 ), 
                      title={'text': title, 'font_color': font_color, 'y': 0.98, 'x': 0.5, 'xref': 'paper'},  
                      polar = dict(
                          radialaxis=dict(
                              showline=False,
                              showticklabels=showticklabels,
                              tickfont_color=font_color,
                              tickfont_size=14,
                              ticksuffix='%',
                              tickvals=tickvals,
                              tickangle=90,
                              angle=90), 
                          angularaxis=dict(tickfont_size=15, tickfont_color=font_color)
                      ),
                     )

    fig.update_traces(hovertemplate='<b>%{theta}</b><br>' + 'frequência: %{r:.1f}%')
    
    return fig