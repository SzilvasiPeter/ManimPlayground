from manim import *
import numpy as np

# gradient descent
class LinearRegression(Scene):
    def construct(self):
        for _ in range(0, 20):
            self.add(Dot(np.random.randn(3)))

