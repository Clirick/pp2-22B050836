def parallelogram(l, h):
    area= (l*h)
    return area

length= int(input("Enter the length of a base: "))
height= float(input("Enter the height of parallelogram: "))

area = parallelogram(length, height)
print(area)