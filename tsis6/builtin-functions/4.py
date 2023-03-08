import time
import math

number = int(input("Enter number: "))
milliseconds = int(input("Enter milliseconds: "))

time.sleep(milliseconds / 1000) 

square_root = math.sqrt(number)

print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")
