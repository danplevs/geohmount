"""Correlation analysis"""
from typing import Callable, Dict
import numpy as np
from scipy import stats
import pandas as pd


def set_correlation_method(method: str = "spearman") -> Callable:
    """Return the scipy.stats correlation method to be used."""
    if method == "spearman":
        corr_method = stats.spearmanr
    elif method == "pearson":
        corr_method = stats.pearsonr
    else:
        raise ValueError(
            f"method must be either 'pearson' or 'spearman', '{method}' was supplied"
        )
    return corr_method

def set_correlation(x, y, method: str = "spearman") -> tuple:
    """Return the correlation result, calculated with the correct arguments."""
    corr_method = set_correlation_method(method)
    if corr_method is stats.spearmanr:
        corr = corr_method(x, y, nan_policy="omit")
    elif corr_method is stats.pearsonr:
        corr = corr_method(x, y)
    else:
        raise ValueError(
            f"method should be either 'stats.pearsonr' or 'stats.spearmanr',\
            '{corr_method}' was supplied"
        )
    return corr


def compute_confidence_interval(x, y, alpha=0.05, corr_method: str = "spearman") -> tuple:
    """Compute the confidence interval for pearson/spearman correlation coefficient.

    Parameters
    ----------
    x : (N,) array_like
        Input array.
    y : (N,) array_like
        Input array.
    alpha : float
        Significance level.
    corr_method :  Callable
        Correlation method, either `pearson` or `spearman`.

    Returns
    -------
    tuple
        The confidence interval, at the `alpha` level, of the correlation between `x` and `y`.
    """
    corr = set_correlation(x, y, corr_method)
    rho_z = np.arctanh(corr[0])
    std_error = 1 / np.sqrt(min(len(x), len(x)) - 3)
    z_score = stats.norm.ppf(1 - alpha / 2)
    norm_confidence_interval = (
        rho_z - z_score * std_error,
        rho_z + z_score * std_error,
    )
    confidence_interval = np.tanh(norm_confidence_interval)
    return confidence_interval

def compute_correlation(dataframe: pd.DataFrame, method="spearman") -> Dict[str, pd.DataFrame]:
    """Compute the correlation analysis and return a dict of pandas dataframes as results."""
    corr_dataframe = dataframe.select_dtypes(include=np.number)
    corr_method = set_correlation_method(method)
    # rho table
    rho = corr_dataframe.corr(method=method).round(2)
    rho = rho.where(np.tril(np.ones_like(rho, dtype=bool), -1))
    # p-value table
    p_value = (
        corr_dataframe.corr(method=lambda x, y: corr_method(x, y, nan_policy="omit")[1])
        - np.eye(*rho.shape)
    ).round(3)
    p_value = p_value.where(np.tril(np.ones_like(p_value, dtype=bool), -1))
    p_star = p_value.applymap(lambda x: "*" if x <= 0.05 else "")
    # report table
    str_rho = rho.applymap(lambda x: f"{x:.2f}")
    report = str_rho + p_star
    report = report.where(np.tril(np.ones_like(rho, dtype=bool), -1))
    # confidence interval table
    ci_lower_bound = corr_dataframe.corr(
        method=lambda x, y: compute_confidence_interval(x, y, corr_method=method)[
            0
        ]
    )
    ci_upper_bound = corr_dataframe.corr(
        method=lambda x, y: compute_confidence_interval(x, y, corr_method=method)[
            1
        ]
    )
    confidence_interval = (
        "["
        + ci_lower_bound.applymap(lambda x: f"{x:.2f}")
        + ", "
        + ci_upper_bound.applymap(lambda x: f"{x:.2f}")
        + "]"
    )
    confidence_interval = confidence_interval.where(
        np.tril(np.ones_like(rho, dtype=bool), -1)
    )
    return dict(rho=rho, p_value=p_value, report=report, ci=confidence_interval)

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
