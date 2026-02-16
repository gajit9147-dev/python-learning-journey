import random

print(random.random()) #gives random number between 0 and 1(excluded 1)

#randint(a,b) gives random integer between a and b (both included)
print(random.randint(1,10))
num=(2,3,5,7,11)
print(random.choice(num)) #gives random element from the given sequence
