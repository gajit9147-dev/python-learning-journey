try:
    fh = open("non_existent_file.txt", "r")
    content = fh.read()
    print(content)
except FileNotFoundError:
    print("The file you are trying to read does not exist. Please check the file name and try again.")  

    # try is block is used to write code that may raise an exception. except block is used to handle the exception if it occurs. In this example, we are trying to open a file that does not exist, which will raise a FileNotFoundError. We catch this exception and print a user-friendly message instead of crashing the program.

    try:
        with open("non_existent_file.txt", "r") as fh:
            content = fh.read()
            print(content)  
    except FileNotFoundError as e:
        print(f"Error: {e}. The file you are trying to read does not exist. Please check the file name and try again.")
