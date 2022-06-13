# calculating how much paint cans we need to paint a wall
test_h = input("Height of the wall: ")
test_w = input("Width of the wall: ")
# assuming 1 can of paint covers 5 square meter
coverage = 5


def paint_calc(height, width, cover):
    area = (int(height) * int(width))
    number_cans = round(area / cover)
    print(f"You will need {number_cans} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage)



