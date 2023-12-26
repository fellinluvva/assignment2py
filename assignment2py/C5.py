ox = float(input("Enter the x-coordinate: "))
oy = float(input("Enter the y-coordinate: "))
if ox > 0 and oy > 0:
    quadrant = 1
elif ox < 0 < oy:
    quadrant = 2
elif ox < 0 and oy < 0:
    quadrant = 3
elif ox > 0 > oy:
    quadrant = 4
else:
    quadrant = None

result = quadrant
if result is None:
    print("The point lies on the coordinate axes")
else:
    print(f"The point({ox}, {oy}) is in quadrant: {quadrant}")
