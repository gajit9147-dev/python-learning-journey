# w mode - open the file for writing.if the file already exist ,it will overwrite the content of the file.
fh = open("w_mode.txt", "w")
fh.write("This is my first file created using w mode in Python.\n")
fh.write ("Today i am very enjoying learning python file handling. ")
fh.close()  