"""
Geometric Fractal Generators.
Implements Sierpinski Triangle, Sierpinski Carpet, Koch Snowflake, and Barnsley Fern.
"""

import numpy as np
from PIL import Image, ImageDraw


def generate_sierpinski_carpet(size: int = 512) -> np.ndarray:
    """Generates Sierpinski Carpet fractal using recursive subdivision."""
    arr = np.ones((size, size), dtype=np.float32)

    def fill_carpet(x, y, s):
        if s < 3:
            return
        sub = s // 3
        arr[y + sub : y + 2 * sub, x + sub : x + 2 * sub] = 0.0
        for dx in range(3):
            for dy in range(3):
                if dx == 1 and dy == 1:
                    continue
                fill_carpet(x + dx * sub, y + dy * sub, sub)

    fill_carpet(0, 0, size)
    return arr


def generate_barnsley_fern(num_points: int = 100000, size: int = 512) -> np.ndarray:
    """Generates Barnsley Fern using Chaos Game stochastic IFS."""
    x = 0.0
    y = 0.0
    pts_x = np.zeros(num_points, dtype=np.float32)
    pts_y = np.zeros(num_points, dtype=np.float32)

    rng = np.random.default_rng(42)
    probs = rng.random(num_points)

    for i in range(num_points):
        p = probs[i]
        if p < 0.01:
            x, y = 0.0, 0.16 * y
        elif p < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif p < 0.93:
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

        pts_x[i] = x
        pts_y[i] = y

    # Map to grid
    canvas = np.zeros((size, size), dtype=np.float32)
    px = np.clip(((pts_x + 2.5) / 5.5 * (size - 1)).astype(np.int32), 0, size - 1)
    py = np.clip(((10.0 - pts_y) / 10.5 * (size - 1)).astype(np.int32), 0, size - 1)

    canvas[py, px] = 1.0
    return canvas


def generate_koch_snowflake(size: int = 512, order: int = 4) -> np.ndarray:
    """Generates Koch Snowflake boundary curve."""
    img = Image.new("L", (size, size), color=0)
    draw = ImageDraw.Draw(img)

    def koch_curve(p1, p2, depth):
        if depth == 0:
            draw.line([p1[0], p1[1], p2[0], p2[1]], fill=255, width=1)
            return

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        pA = (p1[0] + dx / 3.0, p1[1] + dy / 3.0)
        pB = (p1[0] + 2.0 * dx / 3.0, p1[1] + 2.0 * dy / 3.0)

        # Apex point rotated by 60 degrees
        apex_x = pA[0] + 0.5 * (pB[0] - pA[0]) - (np.sqrt(3)/2.0) * (pB[1] - pA[1])
        apex_y = pA[1] + (np.sqrt(3)/2.0) * (pB[0] - pA[0]) + 0.5 * (pB[1] - pA[1])
        pPeak = (apex_x, apex_y)

        koch_curve(p1, pA, depth - 1)
        koch_curve(pA, pPeak, depth - 1)
        koch_curve(pPeak, pB, depth - 1)
        koch_curve(pB, p2, depth - 1)

    # Equilateral triangle vertices
    margin = 40
    p1 = (size / 2.0, margin)
    p2 = (size - margin, size - margin * 1.8)
    p3 = (margin, size - margin * 1.8)

    koch_curve(p1, p2, order)
    koch_curve(p2, p3, order)
    koch_curve(p3, p1, order)

    return (np.array(img, dtype=np.float32) / 255.0)
