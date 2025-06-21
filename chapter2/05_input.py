# if we take dierect inputs then the inputs were treated as strings and addition of them occurs as consatination of 2 strings 

a = input("Enter no. 1 :")
b = input("Enter no. 2 :")

print ("number a is : ", a)
print ("number b is : ", b)
print ("sum is  : ", a+b)

# to avoid this glicth we need to convert the datatype of input frst and then need to perform the operations 
c = int(input("Enter no. 3 :"))
d = int(input("Enter no. 4 :"))

print ("number a is : ", c)
print ("number b is : ", d)
print ("sum is  : ", c+d)


