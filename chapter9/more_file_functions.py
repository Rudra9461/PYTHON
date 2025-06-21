f = open("file.txt")

lines =f.readlines()  #it prints list of lines in a text file 
print(lines , type(lines))
f.close()