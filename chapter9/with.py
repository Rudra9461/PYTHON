f = open("file.txt")
print(f.read())
f.close()

#the same can be written as like this :

with open("file.txt") as f :
    print(f.read())

# now we dont need to write the close statement again and again    