"""
CSI amplitude normalization utilities.
"""

import numpy as np


def normalize_amplitude(data):
    """
    Normalize CSI values between 0 and 1.

    Parameters:
        data: list or numpy array

    Returns:
        normalized numpy array
    """

    values = np.asarray(data, dtype=float)

    minimum = values.min()
    maximum = values.max()

    if maximum == minimum:
        return np.zeros_like(values)

    return (values - minimum) / (maximum - minimum)
