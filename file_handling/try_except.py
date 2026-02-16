try:
    fh = open("non_existent_file.txt", "r")
    content = fh.read()
    print(content)
except FileNotFoundError:
    print("The file you are trying to read does not exist. Please check the file name and try again.")  