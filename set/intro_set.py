# set is non-sequential collection of items,comma seperated by curly braces{}
# set is mutable,unordered,unindexed and no duplicate values allowed

# create a set
my_set = {1, 2, 3, 4, 5,"apple","banana"}
print(f"Initial set: {my_set}")

"""
No duplicates: If you put two identical red balls in, the set just sees "red ball" once
No order: It doesn't matter which item went in first—the set only cares about what is inside, not the arrangement
Anything goes: The items can be numbers, names, colors, or even other sets!
"""
#if we want to access by indexing it is not possible as set is unordered collection

## this is not allow

#duplicate values are not allowed
my_set_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(f"Set with duplicates (duplicates removed): {my_set_with_duplicates}")