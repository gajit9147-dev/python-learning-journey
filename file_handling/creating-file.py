# x mode create a file

fh = open("first_file.txt", "xt")
#write somthing in file
#write (content)

fh.write("This is  my first file created using python. \n")
fh.write("This is a next line.")

#close the file
fh.close()