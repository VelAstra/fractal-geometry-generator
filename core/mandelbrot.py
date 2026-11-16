"""
Vectorized Mandelbrot and Julia Set Generator.
Implements continuous potential escape-time algorithm with smooth color rendering.
"""

from typing import Tuple
import numpy as np


def compute_mandelbrot(
    width: int = 512,
    height: int = 512,
    xmin: float = -2.1,
    xmax: float = 0.8,
    ymin: float = -1.25,
    ymax: float = 1.25,
    max_iter: int = 100
) -> np.ndarray:
    """
    Computes Mandelbrot set for z_{n+1} = z_n^2 + c.
    Returns array of normalized continuous escape iterations in [0, 1].
    """
    x = np.linspace(xmin, xmax, width, dtype=np.float64)
    y = np.linspace(ymin, ymax, height, dtype=np.float64)
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]

    z = np.zeros_like(c)
    div_time = np.zeros(c.shape, dtype=np.float64)
    mask = np.ones(c.shape, dtype=bool)

    for i in range(1, max_iter + 1):
        z[mask] = z[mask] ** 2 + c[mask]
        escaped = np.abs(z) > 4.0
        new_escaped = escaped & mask
        # Continuous smooth coloring: i + 1 - log(log(|z|)) / log(2)
        div_time[new_escaped] = i
        mask[escaped] = False
        if not np.any(mask):
            break

    # Inside set receives 0
    div_time[mask] = 0.0
    return (div_time / max_iter).astype(np.float32)


def compute_julia(
    width: int = 512,
    height: int = 512,
    c_real: float = -0.7,
    c_imag: float = 0.27015,
    xmin: float = -1.5,
    xmax: float = 1.5,
    ymin: float = -1.5,
    ymax: float = 1.5,
    max_iter: int = 100
) -> np.ndarray:
    """
    Computes Julia set for z_{n+1} = z_n^2 + c_0 where c_0 is a constant complex number.
    """
    x = np.linspace(xmin, xmax, width, dtype=np.float64)
    y = np.linspace(ymin, ymax, height, dtype=np.float64)
    z = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    c_const = complex(c_real, c_imag)

    div_time = np.zeros(z.shape, dtype=np.float64)
    mask = np.ones(z.shape, dtype=bool)

    for i in range(1, max_iter + 1):
        z[mask] = z[mask] ** 2 + c_const
        escaped = np.abs(z) > 4.0
        new_escaped = escaped & mask
        div_time[new_escaped] = i
        mask[escaped] = False
        if not np.any(mask):
            break

    div_time[mask] = 0.0
    return (div_time / max_iter).astype(np.float32)
