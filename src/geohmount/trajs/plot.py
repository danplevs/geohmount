from typing import Union
import plotly.express as px
import base64
from pandas.core.frame import DataFrame

def wind_rose(
    data: DataFrame,
    r: str,
    theta: str,
    kind="vel",
    location="sb",
    title: str = None,
    legend_title: str = "Wind Speed",
    legend_x: Union[int, float] = 1,
    legend_y: Union[int, float] = 0.99,
    tickvals: list = [4, 6, 8, 10, 12],
    showticklabels: bool = True,
    bg: bool = True,
    width: int = 800,
    height: int = 450,
    color: str = "velocidade_cat",
    color_sequence=px.colors.sequential.Plasma_r,
    font_color=None,
    template: str = "plotly",
    font_size: Union[int, float] = 14,
):

    direcoes = (
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    )
    if location == "sb":
        medidas = ("0-10 km/h", "10-20 km/h", "20-30 km/h", "30-40 km/h", "40-50 km/h")
    elif location == "ps":
        medidas = (
            "0-10 km/h",
            "10-20 km/h",
            "20-30 km/h",
            "30-40 km/h",
            "40-50 km/h",
            "50-60 km/h",
            "60-70 km/h",
            "70-80 km/h",
            "80-90 km/h",
        )
    elif location == "bm":
        medidas = (
            "0-10 km/h",
            "10-20 km/h",
            "20-30 km/h",
            "30-40 km/h",
            "40-50 km/h",
            "50-60 km/h",
        )
    category_orders = {theta: direcoes, color: medidas}

    if kind == "chuva":
        legend_title = "<b>Precipitation</b>"
        color = "evt_soma_chuva_cat"
        color_sequence = px.colors.sequential.Blues
        medidas = (
            "5-20 mm",
            "20-35 mm",
            "35-50 mm",
            "50-65 mm",
            "65-80 mm",
            "80-95 mm",
            "95-110 mm",
            "110-125 mm",
            "125-130 mm",
        )   
        category_orders = {"direcao_cat": direcoes, "evt_soma_chuva_cat": medidas}

    if bg == True:
        bgcolor = "rgba(255,255,255,1)"
    else:
        bgcolor = "rgba(0,0,0,0)"

    color_map = dict(zip(medidas, color_sequence))

    fig = px.bar_polar(
        data,
        r="frequencia",
        theta="direcao_cat",
        color=color,
        color_discrete_map=color_map,
        category_orders=category_orders,
        width=width,
        height=height,
    )

    fig.update_layout(
        template=template,
        paper_bgcolor=bgcolor,
        legend=dict(
            traceorder="reversed",
            yanchor="top",
            y=legend_y,
            xanchor="right",
            x=legend_x,
            font_color=font_color,
            font_size=font_size - 1,
            title=dict(
                font_size=font_size - 1, font_color=font_color, text=legend_title
            ),
        ),
        title={
            "text": title,
            "font_size": font_size + 1,
            "font_color": font_color,
            "y": 0.98,
            "x": 0.5,
            "xref": "paper",
        },
        polar=dict(
            radialaxis=dict(
                showline=False,
                showticklabels=showticklabels,
                tickfont_color=font_color,
                tickfont_size=font_size,
                ticksuffix="%",
                tickvals=tickvals,
                tickangle=-90,
                angle=-45,
            ),
            angularaxis=dict(tickfont_size=font_size, tickfont_color=font_color),
        ),
    )

    fig.update_traces(hovertemplate="<b>%{theta}</b><br>" + "frequência: %{r:.1f}%")

    return fig


def watermark(
    figure,
    xref="paper",
    yref="paper",
    xanchor="center",
    yanchor="middle",
    x=0.5,
    y=0.5,
    sizex=0.5,
    sizey=0.5,
    sizing="contain",
    opacity=0.13,
    layer="above",
):

    img = "~/OneDrive/geohmount/code/logos-png/GEOHMOUNT-Logo-Cinzas.png"
    geohmount_logo = base64.b64encode(open(img, "rb").read())

    figure.add_layout_image(
        dict(
            source=f"data:image/png;base64,{geohmount_logo.decode()}",
            xref=xref,
            yref=yref,
            xanchor=xanchor,
            yanchor=yanchor,
            x=x,
            y=y,
            sizex=sizex,
            sizey=sizey,
            sizing=sizing,
            opacity=opacity,
            layer=layer,
        )
    )
