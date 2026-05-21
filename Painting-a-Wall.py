width = float(input('Write the width of the wall: '))
height = float(input('Write the height of the wall: '))

area = width * height

print('The wall measures {}m x {}m and its area is {}m².' .format(width, height, area))

paint = area / 2

print('To paint this wall, you will need {}L of paint.' .format(paint))
