"""
concatination , repetition , membership , indexing,count , max, min,sum 

"""
#concatination
# Tuples can be concatenated using the + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated_tuple}")


#repetition
# Tuples can be repeated using the * operator
tuple3 = (7, 8, 9)
repeated_tuple = tuple3 * 3 
print(f"Repeated tuple: {repeated_tuple}")

#membership
# You can check for membership using the in keyword
tuple4 = ('a', 'b', 'c', 'd')
is_b_present = 'b' in tuple4
print(f"Is 'b' present in the tuple? {is_b_present}")
is_z_present = 'z' in tuple4
print(f"Is 'z' present in the tuple? {is_z_present}")
#in operator return boolean value

#indexing
# You can access elements of a tuple using indexing
#syntax: tuple.index(element)
tuple5 = (10, 20, 30, 40, 50)
first_element = tuple5[0]
last_element = tuple5[-1]
tuple_index = tuple5.index(30)
print(f"Index of element 30: {tuple_index}")
print(f"First element: {first_element}, Last element: {last_element}")

#count 
# Returns the number of occurrences of an item in the tuple
# syntax: tuple.count(item)
fruits = ("apple", "banana", "orange", "apple", "kiwi", "banana")
apple_count = fruits.count("apple")
print(f"Number of times 'apple' appears in the tuple: {apple_count}")
