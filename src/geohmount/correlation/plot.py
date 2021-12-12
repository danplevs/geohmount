"""Correlation plots."""
import itertools
from typing import Union, Sequence
from pathlib import Path
from pandas.core.frame import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from .correlation import annotation


def heatmap(
    corr_matrix: DataFrame,
    cmap: Sequence = sns.color_palette("coolwarm", as_cmap=True),
    save_path: Union[Path, str] = "",
) -> plt.Axes:
    """Return a triangular heatmap of correlation coefficients.

    Parameters
    ----------
    corr_matrix : pandas Dataframe
        Dataframe of correlation coefficients.
    cmap : Sequence
        Plot color map.
    save_path: str
        Path to save the plot.

    Returns
    -------
    ax : matplotlib Axes
        Axes object with the heatmap.
    """

    sns.set_theme(context="talk", style="white")
    plt.figure(figsize=(12, 10))

    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    ax = sns.heatmap(corr_matrix,
                    mask=mask,
                    cmap=cmap,
                    square=True,
                    linewidths=0.5,
                    vmax=1,
                    vmin=-1,
                    cbar_kws={"shrink": 0.8},
                    )

    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches="tight")

    return ax

def scatterplot(
    dataframe: DataFrame,
    corr_method: str = "spearman",
    marker_color: tuple = None,
    save_path: Union[Path, str] = "",
    height: int = 800,
    width: int = 1000,
    title: str = None
) -> go.Figure:
    """Return an interactive scatterplot that allows selection of the correlation pair.

    Parameters
    ----------
    dataframe : pandas Dataframe
        Dataframe to plot.
    corr_method : str
        Correlation method, either `pearson` or `spearman`.
    marker_color : RGB tuple
        Marker color.
    save_path: str
        Path to save the plot.

    Returns
    -------
    fig : plotly Figure
        Figure object with the scatterplot.
    """

    num_data = dataframe.select_dtypes("number")

    # Create figure
    fig = px.scatter(
        dataframe, x=num_data.columns[0], y=num_data.columns[1], custom_data=["Amostra"], width=width, height=height, title=title
    )

    fig.add_annotation(
        annotation(num_data.iloc[:, 0], num_data.iloc[:, 1], corr_method=corr_method)
    )

    fig.update_traces(
        marker=dict(size=12, color=f"rgb{marker_color}", line=dict(width=1.5)),
        selector={"mode": "markers"},
        hovertemplate="<br>".join(["x: %{x:.2f}", "y: %{y:.2f}", "%{customdata[0]}"]),
    )

    # Create buttons
    buttons = []

    for x, y in itertools.combinations(num_data.columns, 2):
        buttons.append(
            dict(
                method="update",
                label=f"{x} vs {y}",
                args=[
                    {"x": [num_data[x]], "y": [num_data[y]]},
                    {
                        "xaxis": {"title": x},
                        "yaxis": {"title": y},
                        "annotations": [
                            annotation(
                                num_data[x], num_data[y], corr_method=corr_method
                            )
                        ],
                    },
                ],
            )
        )

    # Update figure layout
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                x=0.5,
                y=1.1,
                xanchor="center",
                yanchor="top",
            )
        ],
        font_size=18,
        title=title
    )

    if save_path:
        config = {"toImageButtonOptions": {"width": width, "height": height}}

        fig.write_html(save_path, config=config)

    fig.show()

    return fig
