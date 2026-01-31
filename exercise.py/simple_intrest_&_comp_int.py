"""
simple intrest formula = (P * R * T) / 100
compound intrest formula = P * (1 + R/100) ** T - P
where P = principal amount
R = rate of interest
T = time period in years

"""
P = float(input("Enter the principal amount (P): "))
R = float(input("Enter the rate of interest (R) in percentage: "))
T = float(input("Enter the time period (T) in years: "))
# Calculate Simple Interest
simple_interest = (P * R * T) / 100
# Calculate Compound Interest
compound_interest = P * (1 + R / 100) ** T - P

print(f"The Simple Interest is: {simple_interest:.2f}")
print(f"The Compound Interest is: {compound_interest:.2f}")
print(f"The total amount after {T} years with Simple Interest is: {P + simple_interest:.2f}")
print(f"The total amount after {T} years with Compound Interest is: {P + compound_interest:.2f}")