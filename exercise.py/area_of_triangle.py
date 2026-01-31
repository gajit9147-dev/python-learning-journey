"""
when given all lengths of triangle, calculate area using Heron's formula
for find semi perimeter use formula p = (a + b + c) / 2
area = √(p(p-a)(p-b)(p-c))   #for square root we can write p**0.5
"""

a= float(input("Enter length of side a: "))
b= float(input("Enter length of side b: "))
c= float(input("Enter length of side c: "))

s= (a+b+c)/2;
area= (s*(s-a)*(s-b)*(s-c))**0.5

print(f"The area of triangle is {area:.2f}")
print(f" The semi perimeter is {s:.2f}")