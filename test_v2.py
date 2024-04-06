from manim import *
from config import *


class TrackerTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            phi = 80 * DEGREES,
            theta = 10 * DEGREES
        )

        # numeric_base = 3
    
        # odometer = create_odometer(
        #     self,
        #     n_of_cores = 8,
        #     hide_indicator = False,
        #     numeric_base = numeric_base,
        #     radius = 2
        # )        

        # rotate_odometer(
        #     self, 
        #     odometer,
        #     32,
        #     1
        # )
        # self.wait(5)

        
        global indicator 
        global indicator_tracker

        indicator_tracker = ValueTracker(0)

        indicator = DecimalNumber( 
                #number = 0,
                font_size = 32,
                num_decimal_places=0
            # ).set_shade_in_3d(
            #     True
            ).move_to(
                [0.0, 5, 0.0 ]
            ).rotate(
                angle = 90*DEGREES
            ).rotate(
                angle = 90*DEGREES,
                axis = UP
            ).scale(
                1.75
            ).set_value(
                indicator_tracker.get_value()
            )
        
        indicator.add_updater(lambda i: i.set_value(indicator_tracker.get_value()))

        self.add(indicator)

        self.wait(1)

        for i in range(5):
            self.play(indicator_tracker.animate.set_value(i))
            self.wait()
