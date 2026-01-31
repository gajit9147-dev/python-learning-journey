# slicing list in python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Get elements from index 2 to 5
sliced_list = my_list[2:6]
print(f"Sliced list from index 2 to 5: {sliced_list}")
# Get every second element from the list
print(my_list[1:6:1])

# append element to list
#add an item to the end of the list
#syntax: list.append(item)  it take only one argument
fruits = ["lichi", "mango", "grapes"]
fruits.append("pineapple")
print(f"list after append: {fruits}")

#insert element to list
#insert an item at the specified index
#syntax: list.insert(index, item)

names = ["Ajeet","Sachin", "Anurag"]
names.insert(1,"Shiv bhukata")
print(f"list after insert: {names}")


##extend element to list
#add multiple items to the end of the list
#syntax: list.extend(iterable)
colors = ["red", "green", "blue"]
colors.extend(["yellow", "purple"])
print(f"list after extend: {colors}")

#remove element from list
#remove the first occurrence of an item from the list
#syntax: list.remove(item)
numbers = [10, 20, 30, 40, 50]  
numbers.remove(30)
print(f"list after remove: {numbers}")

#pop element from list
#remove and return an item at the specified index (default is the last item)
#syntax: list.pop([index])
animals = ["cat", "dog", "rabbit", "hamster"]
removed_animal = animals.pop(2)
print(f"list after pop: {animals}, removed animal: {removed_animal}")
