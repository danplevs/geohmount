import base64

def plot_watermark(figure, xref="paper", yref="paper", xanchor='center', yanchor='middle', 
                   x=0.5, y=0.5, sizex=0.5, sizey=0.5, sizing='contain', opacity=0.13, layer="above"):

    img = 'C:/Users/daniel/OneDrive/geohmount/code/logos-png/GEOHMOUNT-Logo-Cinzas.png'
    geohmount_logo = base64.b64encode(open(img, 'rb').read())

    figure.add_layout_image(
    dict(
        source=f'data:image/png;base64,{geohmount_logo.decode()}',
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
        layer=layer)
)
