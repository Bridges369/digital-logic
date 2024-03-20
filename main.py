from manim import *

def create_core(base=10):
    list_of_symbols = [
            "0", "1", "2", 
            "3", "4", "5", 
            "6", "7", "8", 
            "9"]
    r = 2

    cr = Cylinder(
            radius = r,
            height = 0.5,
            fill_color = BLUE,
            stroke_color = RED,
            fill_opacity = 0.0,
            direction = RIGHT,
            resolution = (1, base)
            # n_points_per_curve = 1
        ).rotate(angle = 90 * DEGREES)

    symbols = VGroup()

    for i in range(len(list_of_symbols)):
        symbols += Text(
            list_of_symbols[i]
            ).rotate(
                    # align numbers
                    angle = 90 * DEGREES
            ).rotate(
                    # align to each face of cylinder
                    angle = (i * (360 / base)) * DEGREES + (90 * DEGREES), 
                    axis = UP
            ).shift(
                    # put it on the respective face of cylinder
                    [
                    np.cos(i * 360 / base) * r, 
                    0.0, 
                    np.sin(i * 360 / base) * r
                    ]
            ).set_shade_in_3d(True)

    # text = Text("1"
    #         ).rotate(angle = PI / 2
    #         ).rotate(angle = PI / 2, axis = UP
    #         ).shift(2 * RIGHT
    #         ).set_shade_in_3d(True)

    return VGroup(cr, symbols)

class Odometer(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
                phi = 80 * DEGREES,
                theta = 30 * DEGREES
            )
    
        cy = create_core(base = 10)
    
        self.add(cy)
        self.wait()
