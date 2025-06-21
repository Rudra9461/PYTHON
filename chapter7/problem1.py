#code for  table

n=int(input("nter the number"))

for i in range(1 ,11):
    print(f"{n}X{i}= {n*i}")
    
print(end="")  

# printing of table in reverse order 

for i in range(1 ,11):
    print(f"{n}X{11-i}= {n*(11-i)}")
