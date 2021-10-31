from manim import *
import numpy as np

# gradient descent
class LinearRegression(Scene):
    def construct(self):
        for i in range(0, 10):
            self.add(Dot(np.random.randn(3)))

        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[0, 3, 0.5],  # step size determines num_decimal_places.
            y_range=[0, 3, 0.5],
            x_length=9,
            y_length=5.5,
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = grid.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)

        self.add(grid, grid_labels)

