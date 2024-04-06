def test(*args, **kwargs):
    print('arguments are:')
    for i in args:
        print(i)

    print('\nkeywords are:')
    for j in kwargs:
        print(j)

return rotate_odometer(self, odometer, n_of_laps, period, index, carry)


if carry == 0 and odometer[3][index][3] != numeric_base - 1:
    self.play(Rotate(
        odometer[0][index],
        angle = (-1 * (360 / numeric_base))*DEGREES,
        axis = UP,
        run_time = period
    ))

    odometer[3][index][3] += 1
    index = 0
    carry = 0

    return rotate_odometer(self, odometer, n_of_laps, period, index, carry)
