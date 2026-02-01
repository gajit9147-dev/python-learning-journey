#dictinory is comma separated values in curly braces{}
#{key1:value1, key2:value2, key3:value3 }
#it is an immutable

grocery= {"milk":40, "bread":20, "eggs":10, "butter":50 }

print(f"Grocery Dictionary: {grocery}")
print(f"Price of milk: {grocery['milk']}")

#it is imutable so cant change value of existing key
#grocery['milk']=45  #this will give error

grocery["milk"]=45  #this will add new key with name "milk"
print(f"Grocery Dictionary after adding new key: {grocery}")