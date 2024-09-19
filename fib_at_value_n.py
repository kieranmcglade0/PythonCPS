import math 
phi = (math.sqrt(5) + 1) / 2
n = float(input("calculate fibonnaci sequenence to the value of: "))
fibonnaci_sequence = (((2 + phi) / 5)*phi ** n) + (((3 - phi) / 5)*phi ** -n)
print (fibonnaci_sequence)