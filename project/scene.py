from manim import *
from manim_physics import * # for physics simulation

class Bacteria(Dot):
    def __init__(self, point=ORIGIN, ** kwargs):
        Dot.__init__(self, point=point, color=GREEN, ** kwargs)
        self.velocity = 6 * np.random.random_sample(3) - 3 # [-3, 3] interval

class BouncingBacteria(Scene):
    def construct(self):
        # Create objects
        box = Rectangle(width=5, height=5)
        self.play(FadeIn(box))

        bacteria_array = []
        for i in range(0, 3):
            bacteria_position = 4 * np.random.random_sample((3,)) - 2 # [-2, 2] interval
            bacteria_array.append(Bacteria(bacteria_position))
            self.play(FadeIn(bacteria_array[i]))

        # Collision detection
        def update_bacteria(bacteria, dt):
            bacteria.acceleration = 2 * np.random.random_sample(3) - 1 # [-1, 1] interval
            bacteria.velocity = bacteria.velocity + bacteria.acceleration * dt
            bacteria.shift(bacteria.velocity * dt)

            # Bounce off walls
            if bacteria.get_left()[0] <= box.get_left()[0] or bacteria.get_right()[0] >= box.get_right()[0]:
                bacteria.velocity[0] = -bacteria.velocity[0]

            # Bounce off ground and roof
            if bacteria.get_bottom()[1] <= box.get_bottom()[1] or bacteria.get_top()[1] >= box.get_top()[1]:
                bacteria.velocity[1] = -bacteria.velocity[1]

        # Attach collision detection to updater
        for bacteria in bacteria_array:
            bacteria.add_updater(update_bacteria)
        self.wait(20)