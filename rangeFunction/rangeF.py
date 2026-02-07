"""

range() is a built-in function in Python that generates a sequence of numbers. It can take one, two, or three arguments:
for in range(start, stop, step):
- start: The starting number of the sequence (inclusive). If not provided, it defaults to 0.
- stop: The ending number of the sequence (exclusive). This argument is required.   
- step: The increment between each number in the sequence. If not provided, it defaults to 1.
"""

for i in range(1, 10, 1):
    print(i)

# both are different ways to write the same code
print("\t")
for i in range(0, 10, 2):
    print(i)

    print("\t")
    #reverse order
    for i in range(20,0,-2):
        print(i)