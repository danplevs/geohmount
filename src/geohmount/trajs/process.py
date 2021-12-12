from typing import Iterable, Union
import pandas as pd
from numpy.typing import ArrayLike


def degrees_to_cardinal(degrees: Union[int, float]) -> str:
    """Convert degrees into a cardinal direction.

    Args:
        degrees (Union[int, float]): Numerical degrees.

    Returns:
        str: Cardinal direction. 
    """    
    directions = (
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
    index = round(degrees / (360 / len(directions)))
    return directions[index % len(directions)]


def continuous_to_categorical(
    array: ArrayLike,
    bins: Iterable,
    right: bool = False,
    extra_bins: Iterable = None,
    labels: bool = True,
    unit: str = ""
) -> pd.Series:
    """Convert an array of continuous values into a categorical Series of discreve interval label.

    Args:
        array (ArrayLike): Input array.
        bins (Iterable): Sequence of bins to cut the array.
        right (bool, optional): Indicates whether bins includes the rightmost edge or not. Defaults to False.
        extra_bins (Iterable, optional): Extra bins to be used in case of a regular range specified in `bins`. Defaults to None.
        unit (str, optional): Physical measure unit. Defaults to None.

    Returns:
        pd.Series: Categorical array.
    """    
    if isinstance(bins, range):
        bins = list(bins)
    if extra_bins:
        bins = [*bins, *extra_bins]
    if labels:
        labels = [f"{bins[i]}-{bins[i + 1]} {unit}".strip() for i in range(len(bins) - 1)]
    return pd.cut(x=array, bins=bins, right=right, labels=labels)
