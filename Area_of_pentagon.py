import math as m
side_length = float(input("input side length of regular pentagon: "))
nested_root = m.sqrt(5)
area = 2.5 * (m.sqrt(5*(5+2*nested_root))*side_length**2)
print (area)