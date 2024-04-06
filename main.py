from manim import *
from config import *
from methods import *

class Odometer(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
                phi = 80 * DEGREES,
                theta = 10 * DEGREES
            )
        numeric_base = 2
        odometer = create_odometer(
                self,
                n_of_cores = 8,
                hide_indicator = False,
                numeric_base = numeric_base,
                radius = 2
            )        
        indicators = [
            0,
            Integer( 
                    number = 0,
                    font_size = 32
                ).set_shade_in_3d(
                    True
                ).move_to(
                    [0.0, 5, 0.0 ]
                ).rotate(
                    angle = 90*DEGREES
                ).rotate(
                    angle = 90*DEGREES,
                    axis = UP
                ).scale(3),
            Integer()
        ]; self.add(indicators[1])
        
        rotate_odometer(
            self, 
            odometer,
            8,
            1,
            indicators
        )
        self.wait(5)
