# in 
#in operation string it give persentage of a character in a string


st1 = "Ajeet Gupta"
print('A' in st1)  #True
print('a' in st1)  #False
print('Gupta' in st1)  #True
print('gupta' in st1)  #False

# not in 
# not in give boolean output if character is not present in string
print('A' not in st1)  #False
print('a' not in st1)  #True

# comprison of string
# in string comparison it compare two string lexicographically
s2 = "Ajeet Gupta"
s3 = "Ajeet gupta"
print(s2 == s3)  #False
print(s2 != s3)  #True

#strip()
s4 = "   Ajeet Gupta   "
print(s4.strip())  # Removes leading and trailing whitespace
print(s4.lstrip())  # Removes leading whitespace
print(s4.rstrip())  # Removes trailing whitespace


#replace()

s5 = "I started learning python. python is great."
print(s5)

print(s5.replace("python", "java")) # Replaces all occurrences of 'python' with 'java'