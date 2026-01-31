"""
reverse()
sort()
count()
membership()

"""

#reverse()
# Reverses the elements of the list in place
# syntax: list.reverse()
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"list after reverse: {numbers}")

num=12345
rev_num = int(str(num)[::-1])
print(f"reversed number: {rev_num}")


#sort()
# Sorts the elements of the list in ascending order by default
# syntax: list.sort(key=None, reverse=False)
unsorted_list = [5, 2, 9, 1, 5, 6]
unsorted_list.sort()
print(f"list after sort: {unsorted_list}")


#count()
# Returns the number of occurrences of an item in the list
# syntax: list.count(item)
fruits = ["apple", "banana", "orange", "apple", "kiwi", "banana"]
apple_count = fruits.count("apple")
print(f"Number of times 'apple' appears in the list: {apple_count}")

#membership()
# Checks if an item is present in the list
# syntax: item in list
colors = ["red", "green", "blue", "yellow"]
is_green_present = "green" in colors
print(f"Is 'green' present in the list? {is_green_present}")
is_purple_present = "purple" in colors
print(f"Is 'purple' present in the list? {is_purple_present}")