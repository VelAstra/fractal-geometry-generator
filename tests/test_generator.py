"""
Unit and Integration Tests for Fractal Geometry Generator Suite.
"""

import unittest
import numpy as np

from core.mandelbrot import compute_mandelbrot, compute_julia
from core.geometric_fractals import generate_sierpinski_carpet, generate_barnsley_fern, generate_koch_snowflake
from core.color_maps import apply_colormap


class TestFractalGenerator(unittest.TestCase):

    def test_mandelbrot(self):
        m = compute_mandelbrot(width=64, height=64, max_iter=20)
        self.assertEqual(m.shape, (64, 64))
        self.assertGreaterEqual(float(np.min(m)), 0.0)
        self.assertLessEqual(float(np.max(m)), 1.0)
        # Center of cardioid (0, 0) should be inside set (value 0.0)
        self.assertEqual(m[32, 32], 0.0)

    def test_julia(self):
        j = compute_julia(width=64, height=64, max_iter=20)
        self.assertEqual(j.shape, (64, 64))

    def test_geometric(self):
        carpet = generate_sierpinski_carpet(size=81)
        self.assertEqual(carpet.shape, (81, 81))
        # Center square must be 0
        self.assertEqual(carpet[35, 35], 0.0)

        fern = generate_barnsley_fern(num_points=1000, size=64)
        self.assertEqual(fern.shape, (64, 64))

        koch = generate_koch_snowflake(size=64, order=2)
        self.assertEqual(koch.shape, (64, 64))

    def test_colormap(self):
        m = compute_mandelbrot(width=32, height=32, max_iter=10)
        rgb = apply_colormap(m, palette="fire")
        self.assertEqual(rgb.shape, (32, 32, 3))


if __name__ == "__main__":
    unittest.main()
