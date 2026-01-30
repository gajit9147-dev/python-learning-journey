# count  syntax: string.count(substring, start= 0,end=len(string))

st = "Ajeet Gupta is learning python. Ajeet is a good boy."
print(st.count('a'))  #2
print(st.count('A'))  #1
s1= "Ajeet"

print(f"counting of Ajeet in string: {st.count(s1)}")
s2= " "
print(f"counting of space in string: {st.count(s2)}")
s3= "e"
print(f"counting of e in string: {st.count(s3)}")

#upper(), lower(), title(), capitalize()

s4= "ajeet gupta is learning python."
print(s4.upper())  # Converts to uppercase
print(s4.lower())  # Converts to lowercase
print(s4.title())  # Converts to title case
print(s4.capitalize())  # Capitalizes the first character

#startswith(), endswith()
s5= "Ajeet Gupta is learning python."
print(s5.startswith("Ajeet"))  #True
print(s5.endswith("python."))  #True