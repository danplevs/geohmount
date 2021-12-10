"""Correlation plots."""
import itertools
from typing import Union, Dict
from .utils import read_config
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from .correlation import compute_confidence_interval, set_correlation


def heatmap(
    corr_matrix,
    cmap=sns.color_palette("coolwarm", as_cmap=True),
    save=False,
    path="./tmp_plot.svg",
) -> plt.Axes:
    """Return a triangular heatmap of correlation coefficients.

    Parameters
    ----------
    corr_matrix : pandas Dataframe
        Dataframe of correlation coefficients.
    cmap : Sequence
        Plot color map.
    save: bool
        If True, save the plot to a file in the path specified at `file_name`.
    path: str
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

    if save:
        plt.savefig(path, dpi=200, bbox_inches="tight")

    return ax

def annotation(x, y, alpha=0.05, corr_method: str = "spearman") -> Dict[str, Union[str, float]]:
    """Return a dict containing the correlation results as a string and plotting information."""
    confidence_interval = compute_confidence_interval(x, y, alpha, corr_method)
    correlation = set_correlation(x, y, corr_method)
    annotation_dict = dict(
        text=f"ρ = {correlation[0]:.2f} (95% CI, [{confidence_interval[0]:.2f}, {confidence_interval[1]:.2f}], p = {correlation[1]:.3f})",
        showarrow=False,
        yref="paper",
        xref="paper",
        x=0.99,
        y=1,
    )
    return annotation_dict


def scatterplot(
    dataframe,
    corr_method: str = "spearman",
    marker_color=None,
    save=False,
    path="./tmp_plot.html",
    height=800,
    width=1000,
    title=None
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
    save: bool
        If True, save the plot to a file in the path specified at `file_name`.
    path: str
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

    if save:
        config = {"toImageButtonOptions": {"width": 1000, "height": 800}}

        fig.write_html(path, config=config)

    fig.show()

    return fig
