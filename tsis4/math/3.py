import math

def area_of_polygon(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi/n))
    return area

num_sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))

area = area_of_polygon(num_sides, length)

print(round(area))
