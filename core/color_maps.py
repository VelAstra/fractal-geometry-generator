"""
Color Mapping Palettes for Fractal Renderings.
"""

from typing import Tuple
import numpy as np


def apply_colormap(normalized_data: np.ndarray, palette: str = "fire") -> np.ndarray:
    """
    Maps continuous 2D float array in [0, 1] to RGB uint8 array (H, W, 3).
    """
    v = np.clip(normalized_data, 0.0, 1.0)
    h, w = v.shape
    rgb = np.zeros((h, w, 3), dtype=np.uint8)

    # Black inside set
    inside_mask = (v == 0.0)

    if palette == "fire":
        rgb[:, :, 0] = np.clip(v * 3.0 * 255.0, 0, 255)
        rgb[:, :, 1] = np.clip((v - 0.33) * 3.0 * 255.0, 0, 255)
        rgb[:, :, 2] = np.clip((v - 0.66) * 3.0 * 255.0, 0, 255)
    elif palette == "ocean":
        rgb[:, :, 0] = np.clip((v - 0.5) * 2.0 * 180.0, 0, 255)
        rgb[:, :, 1] = np.clip(v * 220.0, 0, 255)
        rgb[:, :, 2] = np.clip(v * 255.0 + 40, 0, 255)
    elif palette == "twilight":
        rgb[:, :, 0] = np.clip(np.sin(v * np.pi) * 240.0, 0, 255)
        rgb[:, :, 1] = np.clip(v * 120.0, 0, 255)
        rgb[:, :, 2] = np.clip(np.cos(v * np.pi * 0.5) * 255.0, 0, 255)
    else:  # monochrome
        g = (v * 255.0).astype(np.uint8)
        rgb[:, :, 0] = g
        rgb[:, :, 1] = g
        rgb[:, :, 2] = g

    rgb[inside_mask] = [0, 0, 0]
    return rgb
