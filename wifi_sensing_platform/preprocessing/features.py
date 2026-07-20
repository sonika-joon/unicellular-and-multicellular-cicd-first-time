"""
Feature extraction from CSI signals.
"""

import numpy as np


def extract_features(csi):

    values = np.asarray(
        csi,
        dtype=float
    )

    return {
        "mean": float(values.mean()),
        "std": float(values.std()),
        "max": float(values.max()),
        "min": float(values.min()),
        "energy": float(np.sum(values ** 2))
    }
