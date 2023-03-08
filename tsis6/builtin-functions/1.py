from functools import reduce

def multiply(x, y):
    return x * y

list = [2, 3, 6, 8]
product = reduce(multiply, list)
print(product) 
