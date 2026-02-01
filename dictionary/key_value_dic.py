# in dictionary which datatype  is allowedd as key in dictionary
#which datatpe is not allowed as key in dictionary

"""
# Allowed datatypes as keys in dictionary: float, int, string, tuple, boolean, immutable types
# Not allowed datatypes as keys in dictionary: list, set, dictionary, mutable types
"""

d1={12.5:"float key", 100:"int key", "name":"string key", (1,2,3):"tuple key", True:"boolean key"}
print(f"Dictionary with allowed key datatypes: {d1}")

"""
#All these are not allowed as key in dictionary
d2={ [1,2,3]:"list key", {1,2,3}:"set key", {"key":"value"}:"dictionary key"}
# The above will raise TypeError: unhashable type: 'list' (or 'set'/'dict')
print(f"Dictionary with not allowed key datatypes: {d2}")
"""

#values in dictionary can be of any datatype

d3= {3:"integer value", 4.5:"float value", "fruits":["apple", "banana", "cherry"],
     "vegetables":("carrot", "broccoli"), "is_available":True, "details":{"color":"red", "size":"medium"}
     }
print(f"Dictionary with various value datatypes: {d3}")

#key()

d4={ "a":1, "b":2, "c":3 }
keys=d4.keys()
print(f"Keys in dictionary d4: {keys}")