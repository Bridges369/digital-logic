from manim import *
from config import *


class IntegerChange(VGroup):
    def __init__(self, value):
        super().__init__()
        self.content = Integer(value)
        self.add(self.content)
        
    def set_value(self, value):
        old = self.content
        self.remove(self.content)
        self.content = Integer(value).scale(2).move_to(old.get_center())
        self.add(self.content)
        return self


def create_core(numeric_base=10, radius = 2):
    if numeric_base < 2 or numeric_base > 16:
        raise TypeError("2 > numeric_base <= 16") 

    list_of_symbols = [
            "0", "1", "2", 
            "3", "4", "5", 
            "6", "7", "8", 
            "9", "A", "B",
            "C", "D", "E",
            "F"]

    if  numeric_base == 2 or numeric_base == 5 or numeric_base == 10:
        divisions = 10

    elif numeric_base == 3 or numeric_base == 4 or numeric_base == 6 or numeric_base == 12:
        divisions = 12

    elif numeric_base == 7:
        divisions = 14

    else:
        divisions = numeric_base

    cr = Cylinder(
        radius = radius,
        height = 0.5,
        color = NORD10,
        fill_color = NORD10,
        checkerboard_colors = [NORD10, NORD10],
        stroke_color = 0xffffff,
        fill_opacity = 1.0,
        direction = RIGHT,
        resolution = (
            1,
            divisions
        )
        # n_points_per_curve = 2
    #).set_fill_by_checkboard( NORD10
    ).set_shade_in_3d(True)

    symbols = VGroup()

    for i in range(numeric_base):
        symbols += Text(
            list_of_symbols[i],
            color = NORD6
            ).rotate(
                # align numbers
                angle = 90 * DEGREES
            ).rotate(
                # align to each face of cylinder
                angle = (i * (360 / numeric_base)) * DEGREES + (90 * DEGREES), 
                axis = UP
            ).shift(
                # put it on the respective face of cylinder
                [
                radius * np.cos( (2 * PI) - (i * (2 * PI / numeric_base))), 
                0.0, 
                radius * np.sin( (2 * PI) - (i * (2 * PI / numeric_base)))
                ]
            ).set_shade_in_3d(True)

    return VGroup(cr.rotate(angle = 90 * DEGREES), symbols)



def create_odometer(
        self,
        n_of_cores = 1,
        hide_indicator = False,
        numeric_base = 10,
        radius = 2
    ):

    if numeric_base < 2 or numeric_base > 16:
        raise TypeError("2 > numeric_base <= 16") 

    arr = []
    odometer = VGroup()
    position = [None] * 4
    position_of_each_core = [None] * n_of_cores

    for i in range(n_of_cores):
        position = [0.0, i * 1.0, 0.0, 0] # x, y, z, rotation
        position_of_each_core[i] = position

        arr.insert(0, create_core(
            numeric_base = numeric_base,
            radius = radius
        ).move_to(position[0:3]))

        odometer.add(*arr)

    
    #if not hide_indicator:
        
        
    self.add(odometer.move_to(ORIGIN))

    return [odometer, numeric_base, radius, position_of_each_core]


def rotate_core(self, odometer, period, indicators, *cores):
    
    rotates = list(map(
        lambda core: Rotate(
            odometer[0][core],
            angle = (-1 * (360 / odometer[1]))*DEGREES,
            axis = UP,
            run_time = period
        ),
        cores
    ))
    
    indicators[2] = Integer( 
            number = indicators[0] + 1,
            font_size = 32
        ).set_shade_in_3d(
            True
        ).move_to(
            [ 0.0, 5, 0.0 ]
        ).rotate(
            angle = 90*DEGREES
        ).rotate(
            angle = 90*DEGREES,
            axis = UP
        ).scale(3)

    last_indicator = indicators[1]

    self.play(
        *rotates,
        Transform(indicators[1], indicators[2]),
        run_time=period
    )

    self.remove(last_indicator)
    self.add(indicators[2])

    indicators[1] = indicators[2]
    indicators[0] += 1
    
    return

def rotate_odometer(self, odometer, n_of_laps, period, indicators):
    numeric_base = odometer[1]
    index = 0
    
    while n_of_laps > 0:

        print(n_of_laps)
        arr = []
        for i in range(len(odometer[3])):
            arr.insert(0, odometer[3][i][3])
        print(arr)

        if odometer[3][index][3] < numeric_base - 1:
            rotate_core(self, odometer, period, indicators, index)

            odometer[3][index][3] += 1
            n_of_laps -= 1
            index = 0

        elif odometer[3][index][3] == numeric_base - 1 and odometer[3][index + 1][3] < numeric_base - 1:
            rotate_core(self, odometer, period, indicators, index, index + 1)

            odometer[3][index][3] = 0
            odometer[3][index + 1][3] += 1
            n_of_laps -= 1
            index = 0

        elif odometer[3][index][3] == numeric_base - 1 and odometer[3][index + 1][3] == numeric_base - 1:
            to_rotate = []

            while odometer[3][index][3] == numeric_base - 1:
                odometer[3][index][3] = 0

                to_rotate.insert(0, index)
                index += 1

            to_rotate.insert(0, index)
            odometer[3][index][3] += 1
            
            rotate_core(self, odometer, period, indicators, *to_rotate)

            n_of_laps -= 1
            index = 0

    return
