from manim import *
from manim.utils import deprecation
import numpy as np

# gradient descent
class LinearRegression(Scene):
    def construct(self):
        dot_list = []
        coordinate_list = np.linspace(0, 3, 6)
        for i in coordinate_list:
            dot = Dot(np.random.randn(3))
            # dot = Dot(np.array([i, 0.8*i, 0.0]))
            dot_list.append(dot)
            self.add(dot)

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

        # Draw a random Line.
        reg_line = Line(np.random.randn(3), np.random.randn(3))
        reg_line.set_length(20)
        reg_line.set_color(RED)
        reg_line.align_to(ORIGIN)

        # Draw the best fit Line.
        x_all = 0.0
        y_all = 0.0
        for aDot in dot_list:
            x_all += aDot.get_x()
            y_all += aDot.get_y()

        x_mean = x_all / len(dot_list)
        y_mean = y_all / len(dot_list)

        numerator = 0.0
        denominator = 0.0
        for aDot in dot_list:
            numerator += ((aDot.get_x() - x_mean)*(aDot.get_y() - y_mean))
            denominator += ((aDot.get_x() - x_mean)**2)

        b_coeff = numerator / denominator
        alpha_coeff = y_mean - (b_coeff*x_mean)

        fitted_line = Line(np.array([0, 0+alpha_coeff, 0]), np.array([5, 5*b_coeff + alpha_coeff, 0]))
        fitted_line.set_length(20)
        fitted_line.set_color(GREEN)
        fitted_line.align_to(ORIGIN)

        self.add(grid, grid_labels)
        self.play(Create(reg_line))
        self.play(Transform(reg_line, fitted_line), run_time = 3)
        self.wait(1)
