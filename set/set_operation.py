#if i have tuple than i convert it into set and perform set operations
#as if have list than i convert it into set and perform set operations and vise versa

weeky_days_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#convert tuple into set
weeky_days_set = set(weeky_days_tuple)
print(f"Set of weeky days: {weeky_days_set}")

list_of_numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
#convert list into set
numbers_set = set(list_of_numbers)
print(f"Set of numbers (duplicates removed): {numbers_set}")

#set add()
numbers_set.add(10)
print(f"Set after adding 10: {numbers_set}")