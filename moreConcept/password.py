correct_pass= "Ajeet@2006"
''''
password= input("Enter the password: ")
if password == correct_pass:
    print("Access granted")
else:
    print("Access denied")
'''
while True:
    password= input("Enter the password: ")
    if password == correct_pass:
        print("Access granted")
        break
    else:
        print("Access denied, try again")