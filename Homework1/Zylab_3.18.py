import math

wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

gallon_paint = 350
paint_needed = (wall_area/gallon_paint)
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

cans_needed = math.ceil(paint_needed)
print('Cans needed:', cans_needed, 'can(s)')

color = (input("\nChoose a color to paint the wall:\n"))

if color == 'red':
    paint_cost = 35 * cans_needed
    print('Cost of purchasing', color, 'paint: $' + str(paint_cost))

elif color == 'blue':
    paint_cost = 25 * cans_needed
    print('Cost of purchasing', color, 'paint: $' + str(paint_cost))

elif color == 'green':
    paint_cost = 23 * cans_needed
    print('Cost of purchasing', color, 'paint: $' + str(paint_cost))
else:
    print("Error: color doesnt exist")
