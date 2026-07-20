"""
CSI signal filtering.
"""

import numpy as np


def moving_average(signal, window=5):
    """
    Simple smoothing filter.
    """

    values = np.asarray(signal, dtype=float)

    if len(values) < window:
        return values

    kernel = np.ones(window) / window

    return np.convolve(
        values,
        kernel,
        mode="valid"
    )
