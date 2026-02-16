import json

# Python dictionary
data = {
    "name": "Ajeet",
    "age": 22,
    "skills": ["Python", "JavaScript", "React"]
}

# Write JSON data into file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully")
