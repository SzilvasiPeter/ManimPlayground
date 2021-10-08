from manim import *
import numpy as np

# gradient descent
class LinearRegression(Scene):
    def construct(self):
        for i in range(0, 10):
            self.add(Dot(np.random.randn(3)))

