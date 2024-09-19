import math

a = float(input("What is 'a'?: "))
b = float(input("What is 'b'?: "))
c = float(input("What is 'c'?: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative, otherwise an error is output. 
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are: {root1} and {root2}")
else:
    print(f"the roots are less than or equal to 0")
