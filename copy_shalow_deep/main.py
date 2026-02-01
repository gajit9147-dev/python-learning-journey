import copy

l1=[1, 2, [3, 4], 5,"python"]
l2=copy.copy(l1)   #shallow copy if any thing changes in l1 it will reflect in l2
l3=copy.deepcopy(l1)  #deep copy if any thing changes in l1 it will not reflect in l3
print(f"Original list l1: {l1}")
print(f"Shallow copy l2: {l2}")
print(f"Deep copy l3: {l3}")
print(id(l1), id(l2), id(l3))  #different ids for l1, l2, l3