import math

import pytest

import source.shapes as shapes


class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method.__name__}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print(f"Tearing down {method.__name__}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius * self.circle.radius

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
