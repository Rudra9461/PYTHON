class Demo:
    a=4

o =Demo()
print(o.a)  #prints the class attributes because insatance attributes is not present

o.a = 0 # instance attributes is set
print(o.a) # prints the instance attribute because instance attribute is present 

print(Demo.a) # prints the class atributes