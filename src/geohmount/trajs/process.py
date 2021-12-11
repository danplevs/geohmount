import pandas as pd


def degrees_to_cardinal(degrees):
    directions = ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW')
    index = round(degrees / (360 / len(directions)))
    return directions[index % len(directions)]

def continuous_to_categorical(array, bins, right=False, extra_bins=None, unit=None):
    if isinstance(bins, range):
        bins = list(bins)
    if extra_bins:
        bins = [*bins, *extra_bins]
    labels = [f"{bins[i]}-{bins[i + 1]} {unit}" for i in range(len(bins) - 1)]
    return pd.cut(x=array, bins=bins, right=right, labels=labels)
