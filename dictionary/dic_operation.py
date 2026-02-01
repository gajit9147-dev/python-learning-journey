student1={"maths":85,"science":90,"english":78,"history":88}

# Accessing values using keys
print(f"Marks in Science: {student1['science']}")
print(f"All subjects and marks: {student1}")

#get() function to access values
maths_marks = student1.get("maths")
print(f"Marks in Maths using get(): {maths_marks}")

#membership test to check if key exists
is_english_present = "english" in student1
print(f"Is English subject present? {is_english_present}")


#update existing key value
student1["history"] = 92
print(f"Updated marks in History: {student1['history']}")
#adding new key-value pair
student1["geography"] = 81
print(f"Added Geography marks: {student1['geography']}")

# delete a key-value pair using del
del student1["science"]
print(f"Dictionary after deleting Science: {student1}")