#frozen set is an immutable version of set
#once frozen set is created we cannot add or remove elements from it

#creating a frozen set
frozen_set1 = frozenset(["apple", "banana", "cherry"])
print(f"Frozen set 1: {frozen_set1}")   

frozen_set2=frozenset({12, 34, 56, 78})
print(f"Frozen set 2: {frozen_set2}")
#in frozen set cannot add or remove elements
#frozen_set1.add("orange")  # This will raise an AttributeError
